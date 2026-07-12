from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from kb_lib import ROOT  # noqa: E402


CORE_ARTIFACTS = (
    "DATASET_INDEX.md",
    "ledgers/aliases.md",
    "ledgers/progress.md",
    "ledgers/quality-card.md",
    "dist/catalog.json",
    "dist/catalog.jsonl",
    "dist/catalog.csv",
    "dist/catalog.jsonld",
    "dist/joins.json",
    "dist/router_index.json",
    "dist/checksums.sha256",
)
SITE_ARTIFACTS = (
    "docs/catalog.json",
    "docs/catalog.jsonld",
    "docs/joins.json",
    "docs/router_index.json",
    "docs/index.html",
)
INPUT_DIRECTORIES = ("datasets", "ledgers")
SCRIPT_FILES = ("kb_lib.py", "build_views.py", "export_catalog.py", "build_quality_card.py", "build_site.py")


def prepare_rebuild_root(source_root: Path, temporary_root: Path) -> None:
    """Copy only canonical inputs and the deterministic generators into a scratch root."""
    for directory in INPUT_DIRECTORIES:
        source = source_root / directory
        if not source.is_dir():
            raise RuntimeError(f"missing generator input directory: {source}")
        shutil.copytree(source, temporary_root / directory)
    script_directory = temporary_root / "scripts"
    script_directory.mkdir()
    for name in SCRIPT_FILES:
        source = source_root / "scripts" / name
        if not source.is_file():
            raise RuntimeError(f"missing generator script: {source}")
        shutil.copy2(source, script_directory / name)


def run_generator(temporary_root: Path, script_name: str) -> dict[str, Any]:
    command = [sys.executable, "-B", f"scripts/{script_name}"]
    result = subprocess.run(
        command,
        cwd=temporary_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    return {
        "command": command,
        "exit_code": result.returncode,
        "stdout": result.stdout[-4000:],
        "stderr": result.stderr[-4000:],
    }


def artifact_paths(root: Path) -> tuple[str, ...]:
    """Docs are optional for retargeted workspaces, but checked when published here."""
    if not (root / "docs").is_dir():
        return CORE_ARTIFACTS
    dataset_docs = tuple(
        f"docs/datasets/{path.name}"
        for path in sorted((root / "datasets").glob("*.md"), key=lambda item: item.name)
        if path.name != "template.md"
    )
    return (*CORE_ARTIFACTS, *SITE_ARTIFACTS, *dataset_docs)


def check(root: Path = ROOT) -> dict[str, Any]:
    """Rebuild generated views in isolation and compare bytes without writing to *root*."""
    root = root.resolve()
    with tempfile.TemporaryDirectory(prefix="kb-generated-check-") as directory:
        temporary_root = Path(directory)
        prepare_rebuild_root(root, temporary_root)
        gates = [
            run_generator(temporary_root, "build_views.py"),
            run_generator(temporary_root, "export_catalog.py"),
            run_generator(temporary_root, "build_quality_card.py"),
        ]
        if (root / "docs").is_dir():
            gates.append(run_generator(temporary_root, "build_site.py"))
        failures = [item for item in gates if item["exit_code"] != 0]
        if failures:
            return {"ok": False, "generator_failures": failures, "stale": [], "missing": []}

        stale: list[str] = []
        missing: list[str] = []
        for relative in artifact_paths(root):
            expected = temporary_root / relative
            actual = root / relative
            if not expected.is_file():
                return {
                    "ok": False,
                    "generator_failures": [
                        {
                            "command": ["internal", "artifact-check"],
                            "exit_code": 1,
                            "stdout": "",
                            "stderr": f"generator did not create expected artifact: {relative}",
                        }
                    ],
                    "stale": [],
                    "missing": [],
                }
            if not actual.is_file():
                missing.append(relative)
            elif actual.read_bytes() != expected.read_bytes():
                stale.append(relative)
        return {"ok": not stale and not missing, "generator_failures": [], "stale": stale, "missing": missing}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that generated views and catalog exports match canonical records without modifying the workspace."
    )
    parser.add_argument("--root", type=Path, default=ROOT, help="knowledge-base root to inspect")
    args = parser.parse_args()
    result = check(args.root)
    if result["generator_failures"]:
        print("generated_view_check=error")
        for failure in result["generator_failures"]:
            print(f"ERROR: {' '.join(failure['command'])}")
            if failure["stderr"]:
                print(failure["stderr"])
        return 1
    print(
        f"generated_view_check={'ok' if result['ok'] else 'stale'} "
        f"stale={len(result['stale'])} missing={len(result['missing'])}"
    )
    for relative in result["missing"]:
        print(f"MISSING: {relative}")
    for relative in result["stale"]:
        print(f"STALE: {relative}")
    if not result["ok"]:
        print("Run: python scripts/build_views.py; python scripts/export_catalog.py; python scripts/build_quality_card.py")
        if (args.root / "docs").is_dir():
            print("Then run: python scripts/build_site.py")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
