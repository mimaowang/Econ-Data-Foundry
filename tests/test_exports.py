from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

from check_generated_views import check

ROOT = Path(__file__).resolve().parents[1]


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_catalog_export_is_deterministic(tmp_path) -> None:
    export_dir = tmp_path / "dist"
    command = [sys.executable, str(ROOT / "scripts" / "export_catalog.py"), "--output-dir", str(export_dir)]
    subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    first = {path.name: file_hash(path) for path in export_dir.iterdir() if path.is_file()}
    subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    second = {path.name: file_hash(path) for path in export_dir.iterdir() if path.is_file()}
    assert first == second
    assert {"catalog.json", "catalog.jsonl", "catalog.csv", "catalog.jsonld", "joins.json", "router_index.json", "checksums.sha256"} <= set(first)
    assert b"\r\n" not in (export_dir / "catalog.csv").read_bytes()


def test_views_are_deterministic_in_a_copy(tmp_path) -> None:
    copy_root = tmp_path / "copy"
    shutil.copytree(
        ROOT,
        copy_root,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", "_fetch_cache"),
    )
    command = [sys.executable, str(copy_root / "scripts" / "build_views.py")]
    subprocess.run(command, cwd=copy_root, check=True, capture_output=True, text=True)
    generated = [copy_root / "DATASET_INDEX.md", copy_root / "ledgers" / "aliases.md", copy_root / "ledgers" / "progress.md"]
    first = [file_hash(path) for path in generated]
    subprocess.run(command, cwd=copy_root, check=True, capture_output=True, text=True)
    assert first == [file_hash(path) for path in generated]


def test_generated_view_freshness_detects_canonical_changes(tmp_path) -> None:
    copy_root = tmp_path / "copy"
    shutil.copytree(
        ROOT,
        copy_root,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", "_fetch_cache"),
    )
    assert check(copy_root)["ok"] is True
    record = copy_root / "datasets" / "cfps.md"
    record.write_text(record.read_text(encoding="utf-8") + "\nTest-only additional note.\n", encoding="utf-8")
    stale = check(copy_root)
    assert stale["ok"] is False
    assert "dist/catalog.json" in stale["stale"]
    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_views.py")], cwd=copy_root, check=True)
    subprocess.run([sys.executable, str(copy_root / "scripts" / "export_catalog.py")], cwd=copy_root, check=True)
    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_site.py")], cwd=copy_root, check=True)
    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_quality_card.py")], cwd=copy_root, check=True)
    assert check(copy_root)["ok"] is True


def test_router_index_exports_topics_for_colloquial_retrieval() -> None:
    export_dir = ROOT / "dist"
    payload = json.loads((export_dir / "router_index.json").read_text(encoding="utf-8"))
    charls = next(item for item in payload["datasets"] if item["id"] == "charls")
    assert "retirement" in charls["research_fit"]["topics"]
