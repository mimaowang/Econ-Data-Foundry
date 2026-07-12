from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from collection_benchmark_session import (
    FEEDBACK_HEADINGS,
    aggregate_metrics,
    current_task,
    find_forbidden_keys,
    finish_session,
    integrity_report,
    prepare_session,
    public_url_issue,
    submit_task,
)


def make_source(tmp_path: Path, task_count: int = 1) -> Path:
    source = tmp_path / "source"
    source.mkdir()
    root_files = (
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
    for name in root_files:
        content = "[tool.pytest.ini_options]\ntestpaths=['tests']\n" if name == "pyproject.toml" else f"# {name}\n"
        path = source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    (source / "COLLECTION_PROFILE.md").write_text("# Collection profile\n\nChina\n", encoding="utf-8")
    for directory in ("datasets", "ledgers", "sources", "schema", "scripts", "tests", "dist", "docs"):
        (source / directory).mkdir()
    (source / "datasets" / "example.md").write_text("---\nid: example\n---\nold\n", encoding="utf-8")
    for name in ("pending_tasks.jsonl", "completed_tasks.jsonl", "failed_tasks.jsonl", "changes.jsonl", "dataset_candidates.jsonl"):
        (source / "ledgers" / name).write_text("", encoding="utf-8")
    (source / "ledgers" / "health.json").write_text("{}\n", encoding="utf-8")
    (source / "sources" / "discovery-source.md").write_text("# sources\n", encoding="utf-8")
    (source / "schema" / "schema.json").write_text("{}\n", encoding="utf-8")
    (source / "dist" / "catalog.json").write_text("{}\n", encoding="utf-8")
    (source / "docs" / "catalog.json").write_text("{}\n", encoding="utf-8")
    for name in (
        "collection_benchmark_session.py",
        "check_generated_views.py",
        "build_views.py",
        "export_catalog.py",
        "build_quality_card.py",
        "build_site.py",
        "kb_lib.py",
    ):
        shutil.copy2(Path(__file__).resolve().parents[1] / "scripts" / name, source / "scripts" / name)
    (source / "scripts" / "check_secrets.py").write_text("print('findings=0')\n", encoding="utf-8")
    (source / "scripts" / "validate_kb.py").write_text("print('errors=0 warnings=0')\n", encoding="utf-8")
    (source / "tests" / "test_ok.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    benchmark = source / "benchmarks" / "collection"
    benchmark.mkdir(parents=True)
    (benchmark / "README.md").write_text("# Collection Benchmark\n", encoding="utf-8")
    tasks = [
        {"id": f"task-{index}", "phase": "test", "prompt": f"Collect source {index}."}
        for index in range(task_count)
    ]
    (benchmark / "public_tasks.yaml").write_text(
        yaml.safe_dump({"version": 1, "tasks": tasks}, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    (source / "benchmarks" / "README.md").write_text("# Tests\n", encoding="utf-8")
    (source / "benchmarks" / "idea-regression.yaml").write_text("version: 1\ncases: []\n", encoding="utf-8")
    blind = source / "benchmarks" / "idea-routing"
    blind.mkdir()
    (blind / "README.md").write_text("# Blind\n", encoding="utf-8")
    (blind / "public_cases.yaml").write_text("version: 2\ncases: []\n", encoding="utf-8")
    (source / "agent-review-reports").mkdir()
    (source / "agent-review-reports" / "old.md").write_text("old answer\n", encoding="utf-8")
    rebuild_generated(source)
    return source


def rebuild_generated(workspace: Path) -> None:
    for script in ("build_views.py", "export_catalog.py", "build_quality_card.py", "build_site.py"):
        subprocess.run([sys.executable, str(Path("scripts") / script)], cwd=workspace, check=True)


def write_submission(workspace: Path, task_id: str, outcome: str = "updated") -> Path:
    submission = {
        "task_id": task_id,
        "outcome": outcome,
        "summary": "Reviewed one public source and preserved the evidence boundary.",
        "priority_reason": "This was the highest-value unresolved identity and access question.",
        "papers_reviewed": [
            {
                "title": "A Test Paper",
                "journal": "AER",
                "journal_scope": "top5",
                "year": 2024,
                "doi": "10.0000/test",
                "decision": "used",
                "china_data_basis": "The public data section identifies the Chinese sample.",
                "datasets": ["example"],
                "evidence_url": "https://example.org/paper",
            }
        ],
        "datasets_considered": [
            {
                "id": "example",
                "name": "Example Dataset",
                "action": "updated_record",
                "identity_note": "Kept separate from similarly named products.",
                "access_note": "The public application page was checked.",
            }
        ],
        "sources_used": [
            {
                "url": "https://example.org/access",
                "source_type": "access_page",
                "status": "verified",
                "supports": ["access route"],
            }
        ],
        "queries": ["test paper China data"],
        "external_tools": ["WebSearch"],
        "files_read": ["guides/operations.md", "datasets/example.md"],
        "commands_run": ["python scripts/validate_kb.py"],
        "uncertainties": ["Approval time remains unknown."],
        "protocol_notes": "",
    }
    path = workspace / ".collection_benchmark" / "submission.json"
    path.write_text(json.dumps(submission, ensure_ascii=False), encoding="utf-8")
    return path


def complete_feedback(workspace: Path) -> None:
    text = "# Collection Benchmark Feedback\n\n" + "\n\n".join(
        f"{heading}\n\n{'task evidence and diagnostic detail ' * 25}" for heading in FEEDBACK_HEADINGS
    )
    (workspace / ".collection_benchmark" / "FEEDBACK.md").write_text(text, encoding="utf-8")


def test_collection_task_leakage_detection_is_recursive() -> None:
    assert find_forbidden_keys({"nested": [{"expected_dataset": "secret"}]}) == {"expected_dataset"}


def test_collection_source_urls_reject_credentials_and_sensitive_queries() -> None:
    assert public_url_issue("https://user:pass@example.org/data") == "URL must not contain credentials"
    assert "sensitive query" in str(public_url_issue("https://example.org/data?token=secret"))
    assert public_url_issue("https://example.org/data") is None


def test_collection_metrics_separate_unique_papers_from_evidence_reuse() -> None:
    reports = [
        {
            "outcome": "updated",
            "elapsed_seconds": 1,
            "papers_reviewed": [
                {"title": "One Paper", "doi": "10.1000/example", "decision": "used", "journal_scope": "top5"}
            ],
            "sources_used": [],
            "datasets_considered": [],
            "task_scope": {"status": "met"},
        },
        {
            "outcome": "updated",
            "elapsed_seconds": 1,
            "papers_reviewed": [
                {"title": "One Paper again", "doi": "https://doi.org/10.1000/example", "decision": "used", "journal_scope": "top5"}
            ],
            "sources_used": [],
            "datasets_considered": [],
            "task_scope": {"status": "met"},
        },
    ]
    metrics = aggregate_metrics(reports)
    assert metrics["used_paper_events"] == 2
    assert metrics["unique_used_papers"] == 1
    assert metrics["reused_used_paper_events"] == 1


def test_prepare_is_sanitized_and_outside_source(tmp_path: Path) -> None:
    source = make_source(tmp_path, task_count=2)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    assert workspace.parent.parent == tmp_path / "runs"
    assert (workspace / "datasets" / "example.md").is_file()
    assert (workspace / "COLLECTION_PROFILE.md").is_file()
    assert not (workspace / "agent-review-reports").exists()
    assert (workspace / "benchmarks" / "collection" / "public_tasks.yaml").is_file()
    assert (workspace.parent / "evaluator_baseline" / "datasets" / "example.md").is_file()


def test_integrity_detects_source_repository_changes_after_isolation(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    (source / "README.md").write_text("changed outside the workspace\n", encoding="utf-8")
    report = integrity_report(workspace)
    assert report["source_repository_unchanged"] is False
    assert report["complete"] is False


def test_collection_cycle_observes_changes_and_seals_artifacts(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    task = current_task(workspace)
    record = workspace / "datasets" / "example.md"
    record.write_text(record.read_text(encoding="utf-8") + "new evidence\n", encoding="utf-8")
    rebuild_generated(workspace)
    submission = write_submission(workspace, task["task_id"])
    submission.write_text("\ufeff" + submission.read_text(encoding="utf-8"), encoding="utf-8")
    result = submit_task(workspace, submission)
    assert result["remaining"] == 0
    assert result["changed_files"] > 1
    sealed = Path(result["sealed_cycle"])
    assert (sealed / "artifacts" / "datasets" / "example.md").is_file()
    report = json.loads((sealed / "report.json").read_text(encoding="utf-8"))
    assert "datasets/example.md" in report["actual_changes"]["modified"]
    assert report["generated_views_verified"] is True


def test_collection_rejects_stale_generated_views(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    task = current_task(workspace)
    record = workspace / "datasets" / "example.md"
    record.write_text(record.read_text(encoding="utf-8") + "unpublished evidence\n", encoding="utf-8")
    with pytest.raises(ValueError, match="generated_view_check=stale"):
        submit_task(workspace, write_submission(workspace, task["task_id"]))


def test_collection_rejects_new_used_by_without_traceable_evidence(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    task = current_task(workspace)
    record = workspace / "datasets" / "example.md"
    record.write_text(
        "---\nid: example\nused_by:\n  - cite: Incomplete Evidence Paper\n---\nupdated\n",
        encoding="utf-8",
    )
    rebuild_generated(workspace)
    with pytest.raises(ValueError, match="new canonical used_by entries need cite, dataset_role"):
        submit_task(workspace, write_submission(workspace, task["task_id"]))


def test_collection_cycle_rejects_changes_to_project_logic(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    task = current_task(workspace)
    (workspace / "guides/operations.md").write_text("changed instructions\n", encoding="utf-8")
    with pytest.raises(ValueError, match="outside the collection/content boundary"):
        submit_task(workspace, write_submission(workspace, task["task_id"], outcome="skipped"))


def test_collection_submit_recovers_after_report_was_sealed_before_state_update(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    task = current_task(workspace)
    record = workspace / "datasets" / "example.md"
    record.write_text(record.read_text(encoding="utf-8") + "new evidence\n", encoding="utf-8")
    rebuild_generated(workspace)
    submission = write_submission(workspace, task["task_id"])
    submit_task(workspace, submission)

    state_path = workspace / ".collection_benchmark" / "state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state.update({"next_index": 0, "active_index": 0, "active_started_epoch": 1.0, "active_started_at": "old"})
    state["report_hashes"] = {}
    state["sealed_digests"] = {}
    state_path.write_text(json.dumps(state), encoding="utf-8")

    recovered = submit_task(workspace, submission)
    assert recovered["status"] == "recovered"
    restored = json.loads(state_path.read_text(encoding="utf-8"))
    assert restored["next_index"] == 1
    assert restored["active_index"] is None
    assert task["task_id"] in restored["report_hashes"]


def test_complete_collection_run_packages_diff_and_final_gates(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
    )
    task = current_task(workspace)
    record = workspace / "datasets" / "example.md"
    record.write_text(record.read_text(encoding="utf-8") + "verified route\n", encoding="utf-8")
    rebuild_generated(workspace)
    submit_task(workspace, write_submission(workspace, task["task_id"]))
    complete_feedback(workspace)
    assert integrity_report(workspace, require_feedback=True)["complete"] is True
    results = finish_session(workspace)
    assert (results / "content_changes.patch").read_text(encoding="utf-8")
    assert (results / "final_artifacts" / "datasets" / "example.md").is_file()
    assert json.loads((results / "integrity.json").read_text(encoding="utf-8"))["complete"] is True
    assert all(gate["exit_code"] == 0 for gate in json.loads((results / "final_gates.json").read_text())["gates"])
