from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Iterable

sys.dont_write_bytecode = True

from kb_lib import ROOT  # noqa: E402


MAX_TEXT_BYTES = 10 * 1024 * 1024
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", "_fetch_cache"}
EXCLUDED_PREFIXES = {(".claude", "skills", "anthropics-skills")}
PLACEHOLDER_MARKERS = ("example", "placeholder", "redacted", "your", "xxxx", "<token", "<key")
SECRET_PATTERNS = {
    "api-key": re.compile(r"(?<![A-Za-z0-9_-])sk-(?:ant-|proj-|kimi-)?[A-Za-z0-9_-]{20,}"),
    "github-token": re.compile(r"(?<![A-Za-z0-9_-])(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "aws-access-key": re.compile(r"(?<![A-Za-z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Za-z0-9])"),
    "private-key": re.compile(r"-----BEGIN(?: [A-Z]+)? PRIVATE KEY-----"),
}


def excluded(relative: Path) -> bool:
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return True
    return any(relative.parts[: len(prefix)] == prefix for prefix in EXCLUDED_PREFIXES)


def candidate_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().casefold()):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if excluded(relative) or path.stat().st_size > MAX_TEXT_BYTES:
            continue
        yield path


def scan_text(text: str) -> list[tuple[str, int, str]]:
    findings: list[tuple[str, int, str]] = []
    for kind, pattern in SECRET_PATTERNS.items():
        for match in pattern.finditer(text):
            value = match.group(0)
            if any(marker in value.casefold() for marker in PLACEHOLDER_MARKERS):
                continue
            line = text.count("\n", 0, match.start()) + 1
            fingerprint = hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]
            findings.append((kind, line, fingerprint))
    return findings


def scan(root: Path) -> tuple[list[dict[str, object]], int]:
    findings: list[dict[str, object]] = []
    scanned = 0
    for path in candidate_files(root):
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if b"\x00" in raw:
            continue
        scanned += 1
        text = raw.decode("utf-8", errors="replace")
        for kind, line, fingerprint in scan_text(text):
            findings.append(
                {
                    "path": path.relative_to(root).as_posix(),
                    "line": line,
                    "kind": kind,
                    "fingerprint": fingerprint,
                }
            )
    return findings, scanned


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan repository text for high-confidence credential patterns.")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    findings, scanned = scan(args.root.resolve())
    print(f"secret_scan_files={scanned} findings={len(findings)}")
    for item in findings:
        print(f"ERROR: {item['path']}:{item['line']} {item['kind']} fingerprint={item['fingerprint']}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
