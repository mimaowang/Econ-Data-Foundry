from __future__ import annotations

import argparse
import difflib
import hashlib
import ipaddress
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qsl, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
TASKS_PATH = ROOT / "benchmarks" / "collection" / "public_tasks.yaml"
BENCHMARK_README = ROOT / "benchmarks" / "collection" / "README.md"
SESSION_DIRNAME = ".collection_benchmark"
PROTOCOL_VERSION = 2
OUTCOMES = {"published", "updated", "consolidated", "candidate_only", "skipped", "blocked", "failed"}
PAPER_DECISIONS = {"used", "candidate", "rejected"}
JOURNAL_SCOPES = {
    "top5",
    "field-top",
    "business-top",
    "china-focused",
    "chinese-language",
    "other",
    "not-applicable",
}
SOURCE_STATUSES = {"verified", "lead_only", "blocked"}
DATASET_ACTIONS = {"new_record", "updated_record", "candidate", "rejected_alias", "no_change"}
SENSITIVE_QUERY_KEYS = {"api_key", "apikey", "auth", "key", "password", "secret", "sig", "signature", "token"}
FORBIDDEN_TASK_KEYS = {
    "expected",
    "expected_paper",
    "expected_dataset",
    "target_paper",
    "target_dataset",
    "gold",
    "score",
    "scoring",
    "rubric_answer",
}
ROOT_FILES = (
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "guides/operations.md",
    "guides/usage.md",
    "guides/worklog.md",
    "DATASET_INDEX.md",
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
)
OPTIONAL_ROOT_FILES = ("COLLECTION_PROFILE.md",)
SNAPSHOT_DIRS = ("datasets", "ledgers", "sources", "schema", "scripts", "tests", "dist", "docs")
SNAPSHOT_TEST_FILES = (
    "benchmarks/README.md",
    "benchmarks/idea-regression.yaml",
    "benchmarks/idea-routing/README.md",
    "benchmarks/idea-routing/public_cases.yaml",
    "benchmarks/collection/README.md",
)
GENERATED_FILES = {
    "DATASET_INDEX.md",
    "ledgers/aliases.md",
    "ledgers/progress.md",
    "ledgers/quality-card.md",
    "ledgers/health.json",
    "dist/catalog.json",
    "dist/catalog.jsonl",
    "dist/catalog.csv",
    "dist/catalog.jsonld",
    "dist/router_index.json",
    "dist/joins.json",
    "dist/checksums.sha256",
    "docs/catalog.json",
    "docs/catalog.jsonld",
    "docs/router_index.json",
    "docs/joins.json",
    "docs/index.html",
}
FEEDBACK_HEADINGS = (
    "## Run integrity",
    "## Executive summary",
    "## Cold-start comprehension",
    "## Discovery and source selection",
    "## Dataset identity and knowledge quality",
    "## Long-run drift",
    "## Automation reliability",
    "## Project gaps and improvements",
    "## Protocol deviations",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} must contain a JSON object")
        rows.append(value)
    return rows


def atomic_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    text = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def is_runtime_noise(relative: Path) -> bool:
    parts = relative.parts
    if not parts:
        return False
    if parts[0] == SESSION_DIRNAME:
        return True
    if any(part in {"__pycache__", ".pytest_cache", ".ruff_cache"} for part in parts):
        return True
    if len(parts) >= 2 and parts[0] == "ledgers" and parts[1] == "_fetch_cache":
        return True
    name = relative.name
    return name.endswith((".pyc", ".tmp", ".lock")) or name.startswith(".task-queue.transaction")


def file_manifest(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=lambda item: item.as_posix()):
        relative = path.relative_to(root)
        if is_runtime_noise(relative):
            continue
        result[relative.as_posix()] = sha256_file(path)
    return result


def manifest_digest(manifest: dict[str, str]) -> str:
    return sha256_bytes(json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode("utf-8"))


def compare_manifests(before: dict[str, str], after: dict[str, str]) -> dict[str, list[str]]:
    before_keys = set(before)
    after_keys = set(after)
    return {
        "added": sorted(after_keys - before_keys),
        "modified": sorted(path for path in before_keys & after_keys if before[path] != after[path]),
        "deleted": sorted(before_keys - after_keys),
    }


def find_forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        found.update(FORBIDDEN_TASK_KEYS.intersection(value))
        for child in value.values():
            found.update(find_forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_keys(child))
    return found


def load_tasks(path: Path = TASKS_PATH) -> list[dict[str, Any]]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    tasks = value.get("tasks") if isinstance(value, dict) else None
    if not isinstance(tasks, list) or not tasks:
        raise ValueError("collection benchmark must contain a non-empty tasks list")
    seen: set[str] = set()
    result: list[dict[str, Any]] = []
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not task.get("id") or not task.get("prompt") or not task.get("phase"):
            raise ValueError("every collection benchmark task needs id, phase, and prompt")
        task_id = str(task["id"])
        if task_id in seen:
            raise ValueError(f"duplicate collection benchmark task id: {task_id}")
        leaked = sorted(find_forbidden_keys(task))
        if leaked:
            raise ValueError(f"collection benchmark task {task_id} leaks evaluator fields: {leaked}")
        seen.add(task_id)
        result.append(
            {
                "sequence": index,
                "task_id": task_id,
                "phase": str(task["phase"]),
                "prompt": str(task["prompt"]).strip(),
            }
        )
    return result


def snapshot_ignore(directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()
    for name in names:
        if name in {"__pycache__", ".pytest_cache", ".ruff_cache", "_fetch_cache"}:
            ignored.add(name)
        elif name.endswith((".pyc", ".tmp", ".lock")) or name.startswith(".task-queue.transaction"):
            ignored.add(name)
    return ignored


def copy_file(source_root: Path, destination_root: Path, relative: str) -> None:
    source = source_root / relative
    if not source.is_file():
        raise FileNotFoundError(f"required snapshot file is missing: {source}")
    destination = destination_root / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_snapshot(source_root: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    for relative in ROOT_FILES:
        copy_file(source_root, destination, relative)
    for relative in OPTIONAL_ROOT_FILES:
        if (source_root / relative).is_file():
            copy_file(source_root, destination, relative)
    for directory in SNAPSHOT_DIRS:
        source = source_root / directory
        if not source.is_dir():
            raise FileNotFoundError(f"required snapshot directory is missing: {source}")
        shutil.copytree(source, destination / directory, ignore=snapshot_ignore)
    for relative in SNAPSHOT_TEST_FILES:
        copy_file(source_root, destination, relative)


def operational_source_manifest(source_root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for relative in ROOT_FILES + SNAPSHOT_TEST_FILES:
        path = source_root / relative
        if not path.is_file():
            raise FileNotFoundError(f"required source file is missing: {path}")
        result[Path(relative).as_posix()] = sha256_file(path)
    for relative in OPTIONAL_ROOT_FILES:
        path = source_root / relative
        if path.is_file():
            result[Path(relative).as_posix()] = sha256_file(path)
    for directory in SNAPSHOT_DIRS:
        root = source_root / directory
        if not root.is_dir():
            raise FileNotFoundError(f"required source directory is missing: {root}")
        for path in sorted((item for item in root.rglob("*") if item.is_file()), key=lambda item: item.as_posix()):
            relative = path.relative_to(source_root)
            if is_runtime_noise(relative):
                continue
            result[relative.as_posix()] = sha256_file(path)
    return result


def git_revision(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip() or "unknown"
    except (FileNotFoundError, subprocess.SubprocessError):
        return "unavailable"


def safe_label(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-.")
    return cleaned[:40] or "unknown"


def unique_run_dir(output_root: Path, stem: str) -> Path:
    candidate = output_root / stem
    counter = 2
    while candidate.exists():
        candidate = output_root / f"{stem}-{counter}"
        counter += 1
    return candidate


def feedback_template(manifest: dict[str, Any]) -> str:
    return f"""# Collection Benchmark Feedback

This report describes run `{manifest['run_id']}`. Diagnose the system honestly; do not self-award a score, hide unproductive searches, or rewrite sealed cycle outputs.

## Run integrity

- Agent surface: {manifest['agent_surface']}
- Model label: {manifest['model_label']}
- Orientation files read before the first task: <!-- relative paths -->
- External tools and skills that materially shaped the run: <!-- names only; no credentials or configuration -->
- Any file outside the isolated workspace opened after preparation: <!-- yes/no and why -->
- Any previous benchmark result, evaluator material, or hidden answer seen: <!-- yes/no -->
- Integrity notes: <!-- state deviations plainly; write `none` when there were none -->

## Executive summary

<!-- Summarize completion, the most consequential strengths and failures, and how confident you are in the diagnosis. Do not use record count as the main success measure. -->

## Cold-start comprehension

<!-- Explain what you inferred from the repository before acting, why the first work unit was prioritized, and whether the project made its core idea-to-dataset-to-acquisition objective and harvest/ground/consolidate choice clear without extra user context. -->

## Discovery and source selection

<!-- Cite task IDs. Discuss journal/source quality, false positives, duplicate detection, evidence hierarchy, blocked routes, and whether the run searched broadly enough without becoming indiscriminate. -->

## Dataset identity and knowledge quality

<!-- Cite task IDs and paths. Discuss whether dataset products, aliases, modules, providers, observation units, coverage, joins, and acquisition routes were resolved rather than guessed. Separate useful candidates from publishable knowledge. -->

## Long-run drift

<!-- Compare early and late tasks. Look for shorter evidence chains, weaker access recipes, status inflation, repeated sources, candidate proliferation, skipped validation, or better prioritization as the run progressed. -->

## Automation reliability

<!-- Describe queue handling, idempotency, retries, source outages, generated views, validation, context resets, rate limits, and whether the run could continue unattended without corrupting state. -->

## Project gaps and improvements

<!-- Rank a small number of changes by expected effect on sustained high-quality collection. Ground each in task IDs and distinguish project-content, retrieval/source coverage, operating guidance, tooling, benchmark, and model-specific hypotheses. -->

## Protocol deviations

<!-- Record source-repository access, previous-result access, credentials, private/login-only sources, execution of external code, prohibited project-file edits, manual intervention, skipped tasks, crashes, or timing anomalies. Write `none` only if none occurred. -->
"""


def prepare_session(
    *, source_root: Path, output_root: Path, agent_surface: str, model_label: str
) -> Path:
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    try:
        output_root.relative_to(source_root)
    except ValueError:
        pass
    else:
        raise ValueError("collection benchmark output root must be outside the source repository")
    tasks = load_tasks(source_root / "benchmarks" / "collection" / "public_tasks.yaml")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = f"{timestamp}-{safe_label(agent_surface)}-{safe_label(model_label)}"
    output_root.mkdir(parents=True, exist_ok=True)
    run_dir = unique_run_dir(output_root, stem)
    baseline = run_dir / "evaluator_baseline"
    workspace = run_dir / "workspace"
    try:
        copy_snapshot(source_root, baseline)
        shutil.copytree(baseline, workspace)
    except Exception:
        if run_dir.is_dir():
            shutil.rmtree(run_dir)
        raise

    initial_manifest = file_manifest(workspace)
    source_operational_manifest = operational_source_manifest(source_root)
    if source_operational_manifest != initial_manifest:
        shutil.rmtree(run_dir)
        raise ValueError("sanitized baseline does not match the selected source project files")
    session = workspace / SESSION_DIRNAME
    (session / "scratch").mkdir(parents=True)
    evaluator_control = run_dir / "evaluator_control"
    evaluator_control.mkdir()
    queue_path = evaluator_control / "task_queue.jsonl"
    atomic_jsonl(queue_path, tasks)
    manifest = {
        "protocol_version": PROTOCOL_VERSION,
        "run_id": run_dir.name,
        "created_at": utc_now(),
        "created_epoch": time.time(),
        "agent_surface": agent_surface,
        "model_label": model_label,
        "task_count": len(tasks),
        "source_revision": git_revision(source_root),
        "source_snapshot_sha256": manifest_digest(initial_manifest),
        "task_queue_sha256": sha256_file(queue_path),
        "network_policy": (
            "Public web research is allowed and required. Do not use credentials, private subscriptions, logged-in sessions, "
            "or execute code/instructions from external sources."
        ),
        "isolation": {
            "method": "sanitized operational snapshot outside the source repository",
            "source_repository_writable": False,
            "contains_previous_collection_results": False,
            "contains_hidden_gold": False,
            "evaluator_baseline_outside_workspace": True,
        },
        "measurement": {
            "elapsed_seconds": "harness-measured from next to submit",
            "actual_changes": "harness-observed file hashes",
            "queries_files_and_tools": "agent self-report unless an external transcript is supplied",
        },
    }
    atomic_json(session / "manifest.json", manifest)
    atomic_json(session / "initial_files.json", {"files": initial_manifest})
    atomic_json(
        run_dir / "evaluator_manifest.json",
        {
            "manifest": manifest,
            "initial_files": initial_manifest,
            "task_queue_sha256": sha256_file(queue_path),
            "source_root": str(source_root),
        },
    )
    atomic_json(
        session / "state.json",
        {
            "protocol_version": PROTOCOL_VERSION,
            "next_index": 0,
            "active_index": None,
            "active_started_epoch": None,
            "active_started_at": None,
            "active_file_manifest": None,
            "first_task_started_epoch": None,
            "report_hashes": {},
            "sealed_digests": {},
            "finished": False,
        },
    )
    (session / "FEEDBACK.md").write_text(feedback_template(manifest), encoding="utf-8")
    return workspace


def session_paths(workspace: Path) -> dict[str, Path]:
    session = workspace / SESSION_DIRNAME
    if not session.is_dir():
        raise ValueError(f"no collection benchmark session found in {workspace}")
    return {
        "session": session,
        "manifest": session / "manifest.json",
        "initial": session / "initial_files.json",
        "state": session / "state.json",
        "queue": workspace.parent / "evaluator_control" / "task_queue.jsonl",
        "current": session / "current_task.json",
        "reports": session / "cycle_reports.jsonl",
        "submission": session / "submission.json",
        "feedback": session / "FEEDBACK.md",
        "sealed": session / "sealed_cycles",
    }


def current_task(workspace: Path) -> dict[str, Any]:
    paths = session_paths(workspace)
    state = read_json(paths["state"])
    queue = read_jsonl(paths["queue"])
    if state.get("finished"):
        return {"status": "finished", "message": "This collection benchmark session has already been finalized."}
    active_index = state.get("active_index")
    if active_index is None:
        next_index = int(state.get("next_index", 0))
        if next_index >= len(queue):
            return {"status": "complete", "message": "All tasks are sealed. Complete FEEDBACK.md and run finish."}
        active_index = next_index
        state["active_index"] = active_index
        state["active_started_epoch"] = time.time()
        state["active_started_at"] = utc_now()
        state["active_file_manifest"] = file_manifest(workspace)
        if state.get("first_task_started_epoch") is None:
            state["first_task_started_epoch"] = state["active_started_epoch"]
        atomic_json(paths["state"], state)
    task = dict(queue[int(active_index)])
    task.update({"status": "active", "started_at": state.get("active_started_at")})
    atomic_json(paths["current"], task)
    return task


def ensure_string_list(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{field} must be a list of non-empty strings")
    return list(dict.fromkeys(item.strip() for item in value))


def ensure_mapping_list(value: Any, field: str) -> list[dict[str, Any]]:
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"{field} must be a list of objects")
    return value


def validate_local_paths(workspace: Path, values: list[str], field: str) -> list[str]:
    normalized: list[str] = []
    root = workspace.resolve()
    for value in values:
        path = Path(value.replace("\\", "/"))
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"{field} must contain only paths inside the isolated workspace: {value}")
        candidate = (workspace / path).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"{field} escapes the isolated workspace: {value}") from exc
        if not candidate.is_file():
            raise ValueError(f"{field} references a missing file: {value}")
        normalized.append(path.as_posix())
    return list(dict.fromkeys(normalized))


def public_url_issue(value: str) -> str | None:
    try:
        parsed = urlsplit(value.strip())
        port = parsed.port
    except ValueError:
        return "malformed URL"
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return "URL must use public http or https"
    if parsed.username or parsed.password:
        return "URL must not contain credentials"
    hostname = parsed.hostname.casefold().rstrip(".")
    if hostname in {"localhost", "localhost.localdomain"} or hostname.endswith((".local", ".internal", ".localhost")):
        return "URL must not target a local hostname"
    try:
        address = ipaddress.ip_address(hostname.strip("[]"))
    except ValueError:
        address = None
    if address is not None and not address.is_global:
        return "URL must not target a private or non-global address"
    if port not in (None, 80, 443):
        return "URL must not use a non-standard port"
    sensitive = sorted(
        key for key, _ in parse_qsl(parsed.query, keep_blank_values=True) if key.casefold() in SENSITIVE_QUERY_KEYS
    )
    if sensitive:
        return f"URL contains sensitive query keys: {sensitive}"
    return None


def normalize_report(workspace: Path, raw: dict[str, Any], task: dict[str, Any]) -> dict[str, Any]:
    task_id = str(raw.get("task_id", "")).strip()
    if task_id != task["task_id"]:
        raise ValueError(f"submission task_id must be {task['task_id']!r}")
    outcome = str(raw.get("outcome", "")).strip()
    if outcome not in OUTCOMES:
        raise ValueError(f"outcome must be one of {sorted(OUTCOMES)}")
    summary = str(raw.get("summary", "")).strip()
    priority_reason = str(raw.get("priority_reason", "")).strip()
    if not summary or not priority_reason:
        raise ValueError("summary and priority_reason must be non-empty")

    papers: list[dict[str, Any]] = []
    for index, paper in enumerate(ensure_mapping_list(raw.get("papers_reviewed"), "papers_reviewed"), start=1):
        decision = str(paper.get("decision", "")).strip()
        if decision not in PAPER_DECISIONS:
            raise ValueError(f"papers_reviewed[{index}].decision must be one of {sorted(PAPER_DECISIONS)}")
        title = str(paper.get("title", "")).strip()
        if not title:
            raise ValueError(f"papers_reviewed[{index}].title must be non-empty")
        journal_scope = str(paper.get("journal_scope", "")).strip()
        if journal_scope not in JOURNAL_SCOPES:
            raise ValueError(f"papers_reviewed[{index}].journal_scope must be one of {sorted(JOURNAL_SCOPES)}")
        evidence_url = str(paper.get("evidence_url", "")).strip()
        issue = public_url_issue(evidence_url)
        if issue:
            raise ValueError(f"papers_reviewed[{index}].evidence_url: {issue}")
        china_data_basis = str(paper.get("china_data_basis", "")).strip()
        if not china_data_basis:
            raise ValueError(f"papers_reviewed[{index}].china_data_basis must be non-empty")
        papers.append(
            {
                "title": title,
                "journal": str(paper.get("journal", "")).strip(),
                "journal_scope": journal_scope,
                "year": paper.get("year"),
                "doi": str(paper.get("doi", "")).strip(),
                "decision": decision,
                "china_data_basis": china_data_basis,
                "datasets": ensure_string_list(paper.get("datasets"), f"papers_reviewed[{index}].datasets"),
                "evidence_url": evidence_url,
            }
        )

    datasets: list[dict[str, Any]] = []
    for index, dataset in enumerate(ensure_mapping_list(raw.get("datasets_considered"), "datasets_considered"), start=1):
        action = str(dataset.get("action", "")).strip()
        if action not in DATASET_ACTIONS:
            raise ValueError(f"datasets_considered[{index}].action must be one of {sorted(DATASET_ACTIONS)}")
        name = str(dataset.get("name", "")).strip()
        if not name:
            raise ValueError(f"datasets_considered[{index}].name must be non-empty")
        identity_note = str(dataset.get("identity_note", "")).strip()
        access_note = str(dataset.get("access_note", "")).strip()
        pathway_mode = str(dataset.get("pathway_mode", "")).strip()
        production_note = str(dataset.get("production_note", "")).strip()
        if action != "no_change" and not identity_note:
            raise ValueError(f"datasets_considered[{index}].identity_note must explain the data-product boundary")
        if action in {"new_record", "updated_record", "candidate"} and not access_note:
            raise ValueError(f"datasets_considered[{index}].access_note must state the route or remaining access gap")
        if pathway_mode and pathway_mode not in {"direct", "constructed", "collected", "hybrid", "inaccessible"}:
            raise ValueError(f"datasets_considered[{index}].pathway_mode is invalid")
        if pathway_mode in {"constructed", "collected", "hybrid"} and not production_note:
            raise ValueError(f"datasets_considered[{index}].production_note is required for {pathway_mode} data")
        datasets.append(
            {
                "id": str(dataset.get("id", "")).strip(),
                "name": name,
                "action": action,
                "identity_note": identity_note,
                "access_note": access_note,
                "pathway_mode": pathway_mode,
                "production_note": production_note,
            }
        )

    sources: list[dict[str, Any]] = []
    for index, source in enumerate(ensure_mapping_list(raw.get("sources_used"), "sources_used"), start=1):
        url = str(source.get("url", "")).strip()
        issue = public_url_issue(url)
        if issue:
            raise ValueError(f"sources_used[{index}].url: {issue}")
        status = str(source.get("status", "")).strip()
        if status not in SOURCE_STATUSES:
            raise ValueError(f"sources_used[{index}].status must be one of {sorted(SOURCE_STATUSES)}")
        source_type = str(source.get("source_type", "")).strip()
        if not source_type:
            raise ValueError(f"sources_used[{index}].source_type must be non-empty")
        sources.append(
            {
                "url": url,
                "source_type": source_type,
                "status": status,
                "supports": ensure_string_list(source.get("supports"), f"sources_used[{index}].supports"),
            }
        )

    if outcome in {"published", "updated", "consolidated"} and (not datasets or not sources):
        raise ValueError(f"outcome {outcome!r} requires datasets_considered and sources_used evidence")
    return {
        "task_id": task_id,
        "outcome": outcome,
        "summary": summary,
        "priority_reason": priority_reason,
        "papers_reviewed": papers,
        "datasets_considered": datasets,
        "sources_used": sources,
        "queries": ensure_string_list(raw.get("queries"), "queries"),
        "external_tools": ensure_string_list(raw.get("external_tools"), "external_tools"),
        "files_read": validate_local_paths(
            workspace, ensure_string_list(raw.get("files_read"), "files_read"), "files_read"
        ),
        "commands_run": ensure_string_list(raw.get("commands_run"), "commands_run"),
        "uncertainties": ensure_string_list(raw.get("uncertainties"), "uncertainties"),
        "protocol_notes": str(raw.get("protocol_notes", "")).strip(),
    }


def is_allowed_change(relative: str) -> bool:
    path = Path(relative)
    parts = path.parts
    if not parts:
        return False
    if parts[0] == "datasets" and len(parts) == 2 and path.suffix.casefold() == ".md" and path.name != "template.md":
        return True
    if parts[0] == "ledgers" and len(parts) == 2:
        return path.suffix.casefold() == ".jsonl" or relative in GENERATED_FILES
    if relative in {"guides/worklog.md", "DATASET_INDEX.md"}:
        return True
    if parts[:2] == ("docs", "datasets") and len(parts) == 3 and path.suffix.casefold() == ".md":
        return True
    if parts[0] in {"dist", "docs"} and relative in GENERATED_FILES:
        return True
    return False


def frontmatter_mapping(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    value = yaml.safe_load(parts[1]) or {}
    return value if isinstance(value, dict) else {}


def paper_identity(paper: dict[str, Any]) -> str:
    for field in ("doi", "cite"):
        value = str(paper.get(field, "")).strip().casefold()
        if value:
            return f"{field}:{value}"
    return ""


def new_used_by_evidence_issues(baseline: Path, workspace: Path, changes: dict[str, list[str]]) -> list[str]:
    """Require traceable new evidence without suddenly invalidating legacy entries."""
    required = ("cite", "dataset_role", "evidence_type", "evidence_url", "data_note")
    issues: list[str] = []
    changed_records = sorted(
        path
        for path in changes["added"] + changes["modified"]
        if path.startswith("datasets/") and path.endswith(".md") and Path(path).name != "template.md"
    )
    for relative in changed_records:
        previous = frontmatter_mapping(baseline / relative).get("used_by", [])
        current = frontmatter_mapping(workspace / relative).get("used_by", [])
        previous_papers = previous if isinstance(previous, list) else []
        previous_ids = {
            paper_identity(item)
            for item in previous_papers
            if isinstance(item, dict) and paper_identity(item)
        }
        if not isinstance(current, list):
            continue
        for index, paper in enumerate(current, start=1):
            if not isinstance(paper, dict):
                continue
            identity = paper_identity(paper)
            if identity and identity in previous_ids:
                continue
            missing = [field for field in required if not str(paper.get(field, "")).strip()]
            if missing:
                issues.append(f"{relative}: new used_by[{index}] lacks {', '.join(missing)}")
    return issues


def run_gate(workspace: Path, args: list[str], timeout: int) -> dict[str, Any]:
    started = time.time()
    result = subprocess.run(
        args,
        cwd=workspace,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env={**dict(os.environ), "PYTHONDONTWRITEBYTECODE": "1"},
    )
    return {
        "command": args,
        "exit_code": result.returncode,
        "elapsed_seconds": round(time.time() - started, 3),
        "stdout": result.stdout[-8000:],
        "stderr": result.stderr[-8000:],
    }


def offline_gates(workspace: Path, *, include_tests: bool) -> list[dict[str, Any]]:
    commands = [
        ([sys.executable, "scripts/check_secrets.py"], 60),
        ([sys.executable, "scripts/validate_kb.py"], 60),
        ([sys.executable, "scripts/check_generated_views.py"], 90),
    ]
    if include_tests:
        commands.append(([sys.executable, "-m", "pytest", "-p", "no:cacheprovider"], 180))
    return [run_gate(workspace, command, timeout) for command, timeout in commands]


def copy_changed_artifacts(workspace: Path, changed: dict[str, list[str]], destination: Path) -> None:
    for relative in changed["added"] + changed["modified"]:
        source = workspace / relative
        if not source.is_file():
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def seal_cycle(
    workspace: Path,
    task: dict[str, Any],
    report: dict[str, Any],
    changes: dict[str, list[str]],
    gates: list[dict[str, Any]],
) -> tuple[Path, str]:
    paths = session_paths(workspace)
    directory = paths["sealed"] / f"{int(task['sequence']):02d}-{task['task_id']}"
    if directory.exists():
        existing = read_json(directory / "report.json")
        if existing != report:
            raise ValueError(f"sealed cycle already exists with different content: {directory}")
        return directory, manifest_digest(file_manifest(directory))
    temporary = directory.with_name(f".{directory.name}.tmp")
    if temporary.exists():
        shutil.rmtree(temporary)
    temporary.mkdir(parents=True)
    atomic_json(temporary / "report.json", report)
    atomic_json(temporary / "changes.json", changes)
    atomic_json(temporary / "offline_gates.json", {"gates": gates})
    copy_changed_artifacts(workspace, changes, temporary / "artifacts")
    temporary.rename(directory)
    return directory, manifest_digest(file_manifest(directory))


def finalize_cycle_state(
    paths: dict[str, Path],
    state: dict[str, Any],
    task: dict[str, Any],
    report: dict[str, Any],
    sealed_digest: str,
) -> None:
    report_hash = sha256_bytes(json.dumps(report, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    report_hashes = state.get("report_hashes") if isinstance(state.get("report_hashes"), dict) else {}
    sealed_digests = state.get("sealed_digests") if isinstance(state.get("sealed_digests"), dict) else {}
    report_hashes[report["task_id"]] = report_hash
    sealed_digests[report["task_id"]] = sealed_digest
    state.update(
        {
            "next_index": int(task["sequence"]),
            "active_index": None,
            "active_started_epoch": None,
            "active_started_at": None,
            "active_file_manifest": None,
            "report_hashes": report_hashes,
            "sealed_digests": sealed_digests,
        }
    )
    atomic_json(paths["state"], state)
    paths["current"].unlink(missing_ok=True)


def submit_task(workspace: Path, submission_path: Path) -> dict[str, Any]:
    paths = session_paths(workspace)
    state = read_json(paths["state"])
    queue = read_jsonl(paths["queue"])
    active_index = state.get("active_index")
    if active_index is None:
        raise ValueError("there is no active collection task; run next first")
    task = queue[int(active_index)]
    existing_reports = [item for item in read_jsonl(paths["reports"]) if item.get("task_id") == task["task_id"]]
    if existing_reports:
        if len(existing_reports) != 1:
            raise ValueError(f"task {task['task_id']} has duplicate sealed reports")
        sealed_matches = list(paths["sealed"].glob(f"*-{task['task_id']}")) if paths["sealed"].exists() else []
        if len(sealed_matches) != 1:
            raise ValueError(f"task {task['task_id']} has a report but no unique sealed cycle")
        sealed_digest = manifest_digest(file_manifest(sealed_matches[0]))
        finalize_cycle_state(paths, state, task, existing_reports[0], sealed_digest)
        return {
            "status": "recovered",
            "task_id": task["task_id"],
            "outcome": existing_reports[0].get("outcome"),
            "sealed_cycle": str(sealed_matches[0]),
            "remaining": len(queue) - len(read_jsonl(paths["reports"])),
        }
    orphaned_seals = list(paths["sealed"].glob(f"*-{task['task_id']}")) if paths["sealed"].exists() else []
    if len(orphaned_seals) > 1:
        raise ValueError(f"task {task['task_id']} has multiple orphaned sealed cycles")
    if orphaned_seals:
        shutil.rmtree(orphaned_seals[0])
    raw = read_json(submission_path)
    report = normalize_report(workspace, raw, task)
    before = state.get("active_file_manifest")
    if not isinstance(before, dict):
        raise ValueError("active task has no baseline file manifest")
    after = file_manifest(workspace)
    changes = compare_manifests({str(k): str(v) for k, v in before.items()}, after)
    prohibited = sorted(path for path in changes["added"] + changes["modified"] if not is_allowed_change(path))
    if changes["deleted"]:
        raise ValueError(f"collection benchmark tasks must not delete project files: {changes['deleted']}")
    if prohibited:
        raise ValueError(f"task changed files outside the collection/content boundary: {prohibited}")
    content_changes = changes["added"] + changes["modified"]
    if report["outcome"] in {"published", "updated", "consolidated"} and not any(
        path.startswith("datasets/") for path in content_changes
    ):
        raise ValueError(f"outcome {report['outcome']!r} requires an observed datasets/*.md change")
    if report["outcome"] == "candidate_only" and not any(path.startswith("ledgers/") for path in content_changes):
        raise ValueError("outcome 'candidate_only' requires an observed ledger change")
    used_by_issues = new_used_by_evidence_issues(workspace.parent / "evaluator_baseline", workspace, changes)
    if used_by_issues:
        raise ValueError(
            "new canonical used_by entries need cite, dataset_role, evidence_type, evidence_url, and data_note:\n"
            + "\n".join(used_by_issues)
        )

    gates = offline_gates(workspace, include_tests=False)
    failures = [gate for gate in gates if gate["exit_code"] != 0]
    if failures:
        raise ValueError("offline gate failed; fix the workspace before sealing:\n" + json.dumps(failures, ensure_ascii=False, indent=2))
    elapsed = round(max(0.0, time.time() - float(state.get("active_started_epoch") or time.time())), 3)
    report.update(
        {
            "sequence": task["sequence"],
            "phase": task["phase"],
            "started_at": state.get("active_started_at"),
            "completed_at": utc_now(),
            "elapsed_seconds": elapsed,
            "actual_changes": changes,
            "change_measurement": "harness-observed",
            "self_report_measurement": "queries, tools, commands, and files_read are agent-reported",
            # A stale generated view is now blocked by offline_gates rather than
            # merely recorded as a warning after the task is already sealed.
            "generation_warning": None,
            "generated_views_verified": True,
            "task_scope": task_scope_assessment(task, report["papers_reviewed"]),
        }
    )
    reports = read_jsonl(paths["reports"])
    if any(item.get("task_id") == report["task_id"] for item in reports):
        raise ValueError(f"task {report['task_id']} has already been submitted")
    sealed_dir, sealed_digest = seal_cycle(workspace, task, report, changes, gates)
    reports.append(report)
    atomic_jsonl(paths["reports"], reports)
    finalize_cycle_state(paths, state, task, report, sealed_digest)
    return {
        "status": "sealed",
        "task_id": report["task_id"],
        "outcome": report["outcome"],
        "elapsed_seconds": elapsed,
        "changed_files": len(content_changes),
        "sealed_cycle": str(sealed_dir),
        "remaining": len(queue) - len(reports),
    }


def paper_fingerprint(paper: dict[str, Any]) -> str:
    doi = str(paper.get("doi", "")).strip().casefold()
    if doi:
        return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi).rstrip("/")
    title = re.sub(r"[^a-z0-9]+", "", str(paper.get("title", "")).casefold())
    return f"title:{title}" if title else ""


def task_scope_assessment(task: dict[str, Any], papers: list[dict[str, Any]]) -> dict[str, str]:
    focus = str(task.get("source_focus", "open")).strip() or "open"
    relevant = [item for item in papers if item.get("decision") in {"used", "candidate"}]
    if focus == "business-top":
        met = any(item.get("journal_scope") == "business-top" for item in relevant)
        return {
            "focus": focus,
            "status": "met" if met else "not-demonstrated",
            "note": (
                "At least one used/candidate paper was classified as a high-quality business source."
                if met
                else "No used/candidate paper was classified as a high-quality business source; evaluator should inspect the reason."
            ),
        }
    return {"focus": focus, "status": "not-applicable" if focus == "open" else "not-assessed", "note": "No journal-family target was enforced for this task."}


def aggregate_metrics(reports: list[dict[str, Any]]) -> dict[str, Any]:
    elapsed = [float(item["elapsed_seconds"]) for item in reports if isinstance(item.get("elapsed_seconds"), (int, float))]
    paper_decisions = Counter(
        str(paper.get("decision")) for report in reports for paper in report.get("papers_reviewed", []) if paper.get("decision")
    )
    source_statuses = Counter(
        str(source.get("status")) for report in reports for source in report.get("sources_used", []) if source.get("status")
    )
    dataset_actions = Counter(
        str(dataset.get("action"))
        for report in reports
        for dataset in report.get("datasets_considered", [])
        if dataset.get("action")
    )
    papers = [paper for report in reports for paper in report.get("papers_reviewed", []) if isinstance(paper, dict)]
    used_events = [paper for paper in papers if paper.get("decision") == "used"]
    used_fingerprints = [paper_fingerprint(paper) for paper in used_events]
    unique_used = {item for item in used_fingerprints if item}
    journal_scopes = Counter(str(paper.get("journal_scope")) for paper in papers if paper.get("journal_scope"))
    task_scope_statuses = Counter(
        str((report.get("task_scope") or {}).get("status")) for report in reports if isinstance(report.get("task_scope"), dict)
    )
    return {
        "outcomes": dict(Counter(str(item.get("outcome")) for item in reports)),
        "paper_decisions": dict(paper_decisions),
        "source_statuses": dict(source_statuses),
        "dataset_actions": dict(dataset_actions),
        "journal_scopes": dict(journal_scopes),
        "task_scope_statuses": dict(task_scope_statuses),
        "papers_reviewed_total": len(papers),
        "used_paper_events": len(used_events),
        "unique_used_papers": len(unique_used),
        "reused_used_paper_events": len(used_events) - len(unique_used),
        "paper_identity_basis": "DOI when present; otherwise normalized title",
        "elapsed_total": round(sum(elapsed), 3),
        "elapsed_mean": round(statistics.mean(elapsed), 3) if elapsed else None,
        "elapsed_median": round(statistics.median(elapsed), 3) if elapsed else None,
        "generation_warning_tasks": [item["task_id"] for item in reports if item.get("generation_warning")],
    }


def integrity_report(workspace: Path, *, require_feedback: bool = False) -> dict[str, Any]:
    paths = session_paths(workspace)
    manifest = read_json(paths["manifest"])
    evaluator_manifest = read_json(workspace.parent / "evaluator_manifest.json")
    expected_manifest = evaluator_manifest.get("manifest")
    if not isinstance(expected_manifest, dict):
        raise ValueError("evaluator manifest is invalid")
    initial = read_json(paths["initial"]).get("files")
    if not isinstance(initial, dict):
        raise ValueError("initial file manifest is invalid")
    expected_initial = evaluator_manifest.get("initial_files")
    if not isinstance(expected_initial, dict):
        raise ValueError("evaluator initial file manifest is invalid")
    state = read_json(paths["state"])
    queue = read_jsonl(paths["queue"])
    reports = read_jsonl(paths["reports"])
    queue_ids = [str(item.get("task_id", "")) for item in queue]
    report_ids = [str(item.get("task_id", "")) for item in reports]
    missing = [item for item in queue_ids if item not in set(report_ids)]
    unexpected = sorted(set(report_ids) - set(queue_ids))
    duplicates = sorted({item for item in report_ids if report_ids.count(item) > 1})
    report_hashes = state.get("report_hashes") if isinstance(state.get("report_hashes"), dict) else {}
    modified_reports: list[str] = []
    for report in reports:
        task_id = str(report.get("task_id", ""))
        actual = sha256_bytes(json.dumps(report, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        if report_hashes.get(task_id) != actual:
            modified_reports.append(task_id)
    sealed_digests = state.get("sealed_digests") if isinstance(state.get("sealed_digests"), dict) else {}
    modified_seals: list[str] = []
    for task_id, expected in sealed_digests.items():
        matches = list(paths["sealed"].glob(f"*-{task_id}")) if paths["sealed"].exists() else []
        if len(matches) != 1 or manifest_digest(file_manifest(matches[0])) != expected:
            modified_seals.append(str(task_id))

    final_manifest = file_manifest(workspace)
    final_changes = compare_manifests({str(k): str(v) for k, v in expected_initial.items()}, final_manifest)
    prohibited = sorted(path for path in final_changes["added"] + final_changes["modified"] if not is_allowed_change(path))
    feedback_text = paths["feedback"].read_text(encoding="utf-8") if paths["feedback"].exists() else ""
    missing_headings = [heading for heading in FEEDBACK_HEADINGS if heading not in feedback_text]
    feedback_ready = len(feedback_text.strip()) >= 900 and not missing_headings and "<!--" not in feedback_text
    created_epoch = float(manifest.get("created_epoch") or time.time())
    first_task_epoch = state.get("first_task_started_epoch")
    orientation_seconds = (
        round(max(0.0, float(first_task_epoch) - created_epoch), 3)
        if isinstance(first_task_epoch, (int, float))
        else None
    )
    session_manifest_matches = manifest == expected_manifest
    initial_manifest_matches = initial == expected_initial
    queue_matches = sha256_file(paths["queue"]) == evaluator_manifest.get("task_queue_sha256")
    source_matches = manifest_digest({str(k): str(v) for k, v in expected_initial.items()}) == expected_manifest.get(
        "source_snapshot_sha256"
    )
    baseline_matches = file_manifest(workspace.parent / "evaluator_baseline") == expected_initial
    source_root_value = evaluator_manifest.get("source_root")
    source_repository_matches = bool(source_root_value) and operational_source_manifest(Path(str(source_root_value))) == expected_initial
    generation_warning_tasks = [str(item.get("task_id")) for item in reports if item.get("generation_warning")]
    complete = (
        len(reports) == len(queue)
        and not missing
        and not unexpected
        and not duplicates
        and not modified_reports
        and not modified_seals
        and not final_changes["deleted"]
        and not prohibited
        and queue_matches
        and source_matches
        and session_manifest_matches
        and initial_manifest_matches
        and baseline_matches
        and source_repository_matches
        and state.get("active_index") is None
        and not generation_warning_tasks
        and (feedback_ready or not require_feedback)
    )
    return {
        "protocol_version": PROTOCOL_VERSION,
        "run_id": manifest.get("run_id"),
        "complete": complete,
        "task_count": len(queue),
        "report_count": len(reports),
        "missing_task_ids": missing,
        "unexpected_task_ids": unexpected,
        "duplicate_task_ids": duplicates,
        "modified_after_seal": modified_reports,
        "modified_sealed_cycles": modified_seals,
        "deleted_project_files": final_changes["deleted"],
        "prohibited_final_changes": prohibited,
        "task_queue_hash_matches": queue_matches,
        "source_snapshot_hash_matches": source_matches,
        "session_manifest_matches": session_manifest_matches,
        "initial_manifest_matches": initial_manifest_matches,
        "evaluator_baseline_matches": baseline_matches,
        "source_repository_unchanged": source_repository_matches,
        "generation_warning_tasks": generation_warning_tasks,
        "feedback_ready": feedback_ready,
        "missing_feedback_headings": missing_headings,
        "orientation_seconds": orientation_seconds,
        "run_elapsed_so_far": round(max(0.0, time.time() - created_epoch), 3),
        "metrics": aggregate_metrics(reports),
        "final_changes": final_changes,
        "measurement_note": (
            "File changes and elapsed time are harness-observed. Queries, files_read, commands, and external tools are "
            "self-reported unless accompanied by a client transcript."
        ),
    }


def content_patch(baseline: Path, workspace: Path, changes: dict[str, list[str]]) -> str:
    lines: list[str] = []
    operational_ledgers = {
        "ledgers/pending_tasks.jsonl",
        "ledgers/completed_tasks.jsonl",
        "ledgers/failed_tasks.jsonl",
        "ledgers/dataset_candidates.jsonl",
        "ledgers/changes.jsonl",
    }
    relevant = [
        path
        for path in changes["added"] + changes["modified"]
        if path.startswith("datasets/") or path in operational_ledgers or path == "guides/worklog.md"
    ]
    for relative in sorted(relevant):
        old_path = baseline / relative
        new_path = workspace / relative
        try:
            old = old_path.read_text(encoding="utf-8").splitlines(keepends=True) if old_path.exists() else []
            new = new_path.read_text(encoding="utf-8").splitlines(keepends=True)
        except UnicodeDecodeError:
            continue
        lines.extend(
            difflib.unified_diff(old, new, fromfile=f"baseline/{relative}", tofile=f"workspace/{relative}", n=3)
        )
    return "".join(lines)


def finish_session(workspace: Path) -> Path:
    paths = session_paths(workspace)
    gates = offline_gates(workspace, include_tests=True)
    failures = [gate for gate in gates if gate["exit_code"] != 0]
    if failures:
        raise ValueError("final offline gate failed:\n" + json.dumps(failures, ensure_ascii=False, indent=2))
    report = integrity_report(workspace, require_feedback=True)
    if not report["complete"]:
        raise ValueError("session is not ready to finish:\n" + json.dumps(report, ensure_ascii=False, indent=2))
    run_dir = workspace.parent
    baseline = run_dir / "evaluator_baseline"
    results = run_dir / "results"
    if results.exists():
        raise ValueError(f"results directory already exists: {results}")
    results.mkdir()
    shutil.copy2(paths["manifest"], results / "manifest.json")
    shutil.copy2(run_dir / "evaluator_manifest.json", results / "evaluator_manifest.json")
    shutil.copy2(paths["queue"], results / "task_queue.jsonl")
    shutil.copy2(paths["reports"], results / "cycle_reports.jsonl")
    shutil.copy2(paths["feedback"], results / "FEEDBACK.md")
    if paths["sealed"].exists():
        shutil.copytree(paths["sealed"], results / "sealed_cycles")
    atomic_json(results / "integrity.json", report)
    atomic_json(results / "final_gates.json", {"gates": gates})
    atomic_json(results / "changes.json", report["final_changes"])
    copy_changed_artifacts(workspace, report["final_changes"], results / "final_artifacts")
    (results / "content_changes.patch").write_text(
        content_patch(baseline, workspace, report["final_changes"]), encoding="utf-8"
    )
    sources: dict[str, dict[str, Any]] = {}
    for cycle in read_jsonl(paths["reports"]):
        for source in cycle.get("sources_used", []):
            url = str(source.get("url", ""))
            if url:
                sources.setdefault(url, source)
    atomic_jsonl(results / "sources.jsonl", sources.values())
    state = read_json(paths["state"])
    state["finished"] = True
    state["finished_at"] = utc_now()
    atomic_json(paths["state"], state)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an isolated long-horizon literature-to-dataset collection benchmark.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare = subparsers.add_parser("prepare", help="create a sanitized, writable collection workspace outside the project")
    prepare.add_argument("--agent", default="unknown-agent", help="agent surface, for example claude-code")
    prepare.add_argument("--model", default="unknown-model", help="visible model label; never inspect credentials to find it")
    prepare.add_argument(
        "--output-root", type=Path, default=ROOT.parent / "econ-dataknowhow-collection-benchmark-runs"
    )
    subparsers.add_parser("next", help="show one collection task and start its harness timer")
    submit = subparsers.add_parser("submit", help="validate and seal the active task, its changes, and evidence report")
    submit.add_argument("--file", type=Path, default=Path(SESSION_DIRNAME) / "submission.json")
    subparsers.add_parser("check", help="check progress and integrity without judging research semantics")
    subparsers.add_parser("finish", help="run final gates and package the complete evaluator evidence bundle")
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            workspace = prepare_session(
                source_root=ROOT,
                output_root=args.output_root.resolve(),
                agent_surface=args.agent,
                model_label=args.model,
            )
            print(json.dumps({"status": "prepared", "workspace": str(workspace)}, ensure_ascii=False, indent=2))
        elif args.command == "next":
            print(json.dumps(current_task(ROOT), ensure_ascii=False, indent=2))
        elif args.command == "submit":
            submission = args.file if args.file.is_absolute() else ROOT / args.file
            print(json.dumps(submit_task(ROOT, submission), ensure_ascii=False, indent=2))
        elif args.command == "check":
            print(json.dumps(integrity_report(ROOT), ensure_ascii=False, indent=2))
        else:
            results = finish_session(ROOT)
            print(json.dumps({"status": "finished", "results": str(results)}, ensure_ascii=False, indent=2))
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError, subprocess.SubprocessError) as exc:
        print(f"collection benchmark error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
