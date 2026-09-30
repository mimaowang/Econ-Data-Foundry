from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

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
    stale_health = subprocess.run(
        [sys.executable, str(copy_root / "scripts" / "validate_kb.py")],
        cwd=copy_root,
        capture_output=True,
        text=True,
    )
    assert stale_health.returncode == 1
    assert "health report is stale" in stale_health.stdout
    subprocess.run(
        [sys.executable, str(copy_root / "scripts" / "validate_kb.py"), "--write-report"],
        cwd=copy_root,
        check=True,
    )
    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_views.py")], cwd=copy_root, check=True)
    subprocess.run([sys.executable, str(copy_root / "scripts" / "export_catalog.py")], cwd=copy_root, check=True)
    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_site.py")], cwd=copy_root, check=True)
    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_quality_card.py")], cwd=copy_root, check=True)
    assert check(copy_root)["ok"] is True


def test_generated_view_freshness_detects_unexpected_dataset_page(tmp_path) -> None:
    copy_root = tmp_path / "copy"
    shutil.copytree(
        ROOT,
        copy_root,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", "_fetch_cache"),
    )
    extra = copy_root / "docs" / "datasets" / "orphan.md"
    extra.write_text("orphan generated page\n", encoding="utf-8")

    subprocess.run([sys.executable, str(copy_root / "scripts" / "build_site.py")], cwd=copy_root, check=True)
    assert extra.read_text(encoding="utf-8") == "orphan generated page\n"

    result = check(copy_root)

    assert result["ok"] is False
    assert "docs/datasets/orphan.md" in result["unexpected"]


def test_router_index_exports_topics_for_colloquial_retrieval() -> None:
    export_dir = ROOT / "dist"
    payload = json.loads((export_dir / "router_index.json").read_text(encoding="utf-8"))
    charls = next(item for item in payload["datasets"] if item["id"] == "charls")
    assert "retirement" in charls["research_fit"]["topics"]


def test_router_exports_compact_research_data_pathway() -> None:
    payload = json.loads((ROOT / "dist" / "router_index.json").read_text(encoding="utf-8"))
    land = next(item for item in payload["datasets"] if item["id"] == "china-land-transaction")
    assert land["data_pathway"]["mode"] == "collected"
    assert land["data_pathway"]["target_artifact"]
    assert "production" not in land
    assert all("steps" not in route and "deliverable" not in route for route in land["access"]["routes"])


def test_catalog_reports_actual_record_schema_versions() -> None:
    payload = json.loads((ROOT / "dist" / "catalog.json").read_text(encoding="utf-8"))
    actual = sorted({item["schema_version"] for item in payload["datasets"]})
    assert payload["dataset_record_schema_versions_present"] == actual
    assert payload["latest_dataset_record_schema_version"] == max(actual)


def test_static_router_tokenizes_full_research_ideas() -> None:
    html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    assert "const queryTerms" in html
    assert "const matchScore" in html
    assert "const matchCount" in html
    assert "const termWeights" in html
    assert ".slice(0, 12)" in html
    assert "result.matches >= 2" in html
    assert ".includes(needle)" not in html


def test_household_weather_route_exposes_both_assets() -> None:
    payload = json.loads((ROOT / "dist" / "router_index.json").read_text(encoding="utf-8"))
    chfs = next(item for item in payload["datasets"] if item["id"] == "chfs")
    assert any(join["target"] == "era5-land" and join["evidence_status"] == "plausible" for join in chfs["joins"])


def test_static_record_links_stay_in_the_published_project() -> None:
    html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    template = re.search(r'<h2><a href="([^"]+)"', html).group(1)
    payload = json.loads((ROOT / "docs" / "catalog.json").read_text(encoding="utf-8"))
    for base in ("https://example.org/Econ-DataKnowhow/", "http://localhost:8000/"):
        for item in payload["datasets"]:
            link = template.replace("${esc(source)}", item["source_path"])
            resolved = urljoin(base, link)
            assert resolved.startswith(base)
            relative = urlparse(resolved).path.removeprefix(urlparse(base).path)
            published = ROOT / "docs" / relative
            assert published.read_bytes() == (ROOT / item["source_path"]).read_bytes()
    assert (ROOT / "docs" / ".nojekyll").is_file()


def test_local_fetch_cache_does_not_change_public_health(tmp_path) -> None:
    copy_root = tmp_path / "copy"
    shutil.copytree(
        ROOT,
        copy_root,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache", "_fetch_cache"),
    )
    report_path = copy_root / "ledgers" / "health.json"
    before = report_path.read_bytes()
    cache = copy_root / "ledgers" / "_fetch_cache"
    cache.mkdir()
    (cache / "local-note.txt").write_text("A local fetch note, not catalog evidence", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(copy_root / "scripts" / "validate_kb.py"), "--write-report"],
        cwd=copy_root, capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout
    assert "local-note.txt: unclassified content" in result.stdout
    assert report_path.read_bytes() == before
    (cache / "challenge.html").write_text("<html>Just a moment</html>", encoding="utf-8")
    blocked = subprocess.run(
        [sys.executable, str(copy_root / "scripts" / "validate_kb.py")],
        cwd=copy_root, capture_output=True, text=True,
    )
    assert blocked.returncode == 1
    assert "challenge page not recorded in failure ledger" in blocked.stdout
    assert report_path.read_bytes() == before
