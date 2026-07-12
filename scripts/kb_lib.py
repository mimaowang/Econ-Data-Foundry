from __future__ import annotations

import json
import ipaddress
import os
import re
import socket
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qsl, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT / "datasets"
LEDGER_DIR = ROOT / "ledgers"
BENCHMARK_PATH = ROOT / "benchmarks" / "idea-regression.yaml"
URL_PLACEHOLDERS = {"", "needs-verification", "n/a", "na", "none", "null"}
SENSITIVE_QUERY_KEYS = {"api_key", "apikey", "auth", "key", "password", "secret", "sig", "signature", "token"}


@dataclass(frozen=True)
class DatasetRecord:
    path: Path
    data: dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return str(self.data.get("id", "")).strip()

    @property
    def status(self) -> str:
        return str(self.data.get("catalog_status", "")).strip()


def read_frontmatter(path: Path) -> DatasetRecord:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("file does not start with YAML frontmatter delimiter '---'")

    match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        raise ValueError("frontmatter closing delimiter not found")

    raw = match.group(1)
    loaded = yaml.safe_load(raw)
    if not isinstance(loaded, dict):
        raise ValueError("frontmatter must decode to a mapping")
    return DatasetRecord(path=path, data=loaded, body=text[match.end() :])


def load_datasets() -> tuple[list[DatasetRecord], list[tuple[Path, str]]]:
    records: list[DatasetRecord] = []
    failures: list[tuple[Path, str]] = []
    for path in sorted(DATASET_DIR.glob("*.md"), key=lambda item: item.name.casefold()):
        if path.name == "template.md":
            continue
        try:
            records.append(read_frontmatter(path))
        except Exception as exc:  # validation must report every broken file
            failures.append((path, str(exc)))
    return records, failures


def public_http_url_issues(value: Any, *, resolve_dns: bool = False) -> list[str]:
    """Return safety issues for a URL that may be rendered or fetched."""
    text = str(value or "").strip()
    if text.casefold() in URL_PLACEHOLDERS:
        return []
    issues: set[str] = set()
    try:
        parsed = urlsplit(text)
        hostname = parsed.hostname
        port = parsed.port
    except ValueError:
        return ["invalid-url"]
    if parsed.scheme.casefold() not in {"http", "https"}:
        issues.add("non-http-scheme")
    if not hostname:
        issues.add("missing-host")
    if parsed.username or parsed.password:
        issues.add("userinfo-not-allowed")
    query_keys = {key.casefold() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    if query_keys & SENSITIVE_QUERY_KEYS:
        issues.add("sensitive-query-parameter")
    if hostname:
        folded_host = hostname.casefold().rstrip(".")
        if folded_host == "localhost" or folded_host.endswith((".localhost", ".local", ".internal", ".home.arpa")):
            issues.add("local-hostname")
        try:
            literal = ipaddress.ip_address(folded_host)
        except ValueError:
            literal = None
        if literal is not None and not literal.is_global:
            issues.add("non-public-ip")
        if resolve_dns and not issues:
            try:
                addresses = {
                    item[4][0]
                    for item in socket.getaddrinfo(hostname, port or (443 if parsed.scheme.casefold() == "https" else 80), type=socket.SOCK_STREAM)
                }
            except (OSError, socket.gaierror):
                issues.add("dns-resolution-failed")
            else:
                if not addresses:
                    issues.add("dns-resolution-failed")
                for address in addresses:
                    try:
                        if not ipaddress.ip_address(address).is_global:
                            issues.add("dns-resolves-to-non-public-ip")
                    except ValueError:
                        issues.add("invalid-resolved-address")
    return sorted(issues)


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.exists():
        return [], ["file does not exist"]
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError("row is not a JSON object")
            rows.append(value)
        except Exception as exc:
            errors.append(f"line {number}: {exc}")
    return rows, errors


def related_ids(value: Any) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        return []
    result: list[str] = []
    for item in value:
        if isinstance(item, str):
            result.append(item.strip())
        elif isinstance(item, dict) and item.get("id"):
            result.append(str(item["id"]).strip())
    return [item for item in result if item]


def used_by_count(record: DatasetRecord) -> int:
    value = record.data.get("used_by")
    return len(value) if isinstance(value, list) else 0


def normalize_alias(value: str) -> str:
    return re.sub(r"[\s\-_/·（）()]+", "", value).casefold()


def aliases(record: DatasetRecord) -> list[str]:
    value = record.data.get("aka", [])
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def access_cost(record: DatasetRecord) -> str:
    access = record.data.get("access")
    if isinstance(access, dict) and access.get("cost") is not None:
        return str(access["cost"]).strip()
    routes = record.data.get("access_routes")
    if isinstance(routes, list):
        costs = sorted(
            {str(route.get("cost", "")).strip() for route in routes if isinstance(route, dict) and route.get("cost")}
        )
        if len(costs) == 1:
            return costs[0]
        if costs:
            return "mixed"
    return "unknown"


def time_summary(record: DatasetRecord) -> str:
    value = record.data.get("time_span")
    if isinstance(value, dict):
        start = value.get("start", "?")
        end = value.get("end", value.get("last_confirmed_release", "?"))
        if str(end).casefold() == "ongoing":
            release = value.get("last_confirmed_release")
            if release not in (None, "ongoing", "unknown"):
                end = f"ongoing (confirmed through {release})"
            elif release == "unknown":
                end = "ongoing (latest available release needs verification)"
            else:
                end = "ongoing"
        return f"{start}–{end}"
    return str(value or "unknown").strip()


def strongest_use(record: DatasetRecord) -> str:
    fit = record.data.get("research_fit")
    if isinstance(fit, dict):
        best = fit.get("best_for")
        if isinstance(best, list) and best:
            return str(best[0]).strip()
    good_for = record.data.get("good_for")
    if isinstance(good_for, list) and good_for:
        return str(good_for[0]).strip()
    if isinstance(good_for, str):
        return good_for.strip()
    return "needs completion"


def compact(value: Any, limit: int = 70) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip().replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def dump_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2, default=str) + "\n")


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temp.write_bytes(text.encode("utf-8"))
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def atomic_write_bytes(path: Path, value: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temp.write_bytes(value)
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    text = "".join(json.dumps(row, ensure_ascii=False, default=str) + "\n" for row in rows)
    atomic_write_text(path, text)


def _process_is_alive(pid: Any) -> bool:
    """Return whether a local process still exists without requiring psutil."""
    try:
        value = int(pid)
    except (TypeError, ValueError):
        return False
    if value <= 0:
        return False
    if os.name == "nt":
        try:
            import ctypes

            process_query_limited_information = 0x1000
            handle = ctypes.windll.kernel32.OpenProcess(process_query_limited_information, False, value)
            if not handle:
                return False
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        except (AttributeError, OSError):
            return False
    try:
        os.kill(value, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


@contextmanager
def workspace_lock(name: str = "writer", stale_seconds: int = 3600):
    lock_path = LEDGER_DIR / f".{name}.lock"
    token = uuid.uuid4().hex
    payload = {
        "token": token,
        "pid": os.getpid(),
        "host": socket.gethostname(),
        "created_at_epoch": time.time(),
    }
    while True:
        try:
            descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, ensure_ascii=False)
            break
        except FileExistsError:
            try:
                age = time.time() - lock_path.stat().st_mtime
            except FileNotFoundError:
                continue
            if age > stale_seconds:
                # An old timestamp is not enough evidence that a long-running
                # local agent has stopped. Never evict a live same-host PID.
                try:
                    existing = json.loads(lock_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    existing = {}
                same_host = existing.get("host") == socket.gethostname()
                if same_host and _process_is_alive(existing.get("pid")):
                    raise RuntimeError(f"workspace is locked by a live process: {lock_path}")
                try:
                    lock_path.unlink()
                except FileNotFoundError:
                    pass
                continue
            raise RuntimeError(f"workspace is locked by another writer: {lock_path}")
    try:
        yield
    finally:
        try:
            current = json.loads(lock_path.read_text(encoding="utf-8"))
            if current.get("token") == token:
                lock_path.unlink()
        except FileNotFoundError:
            pass



def duplicate_values(values: Iterable[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates
