from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from benchmark_session import (
    FEEDBACK_HEADINGS,
    build_queue,
    current_case,
    finish_session,
    integrity_report,
    prepare_session,
    submit_case,
)


def make_source(tmp_path: Path, case_count: int = 3) -> Path:
    source = tmp_path / "source"
    source.mkdir()
    for name in ("AGENTS.md", "README.md", "guides/operations.md", "guides/usage.md", "DATASET_INDEX.md"):
        path = source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {name}\n", encoding="utf-8")
    (source / "COLLECTION_PROFILE.md").write_text("# Collection profile\n\nChina\n", encoding="utf-8")
    (source / "datasets").mkdir()
    (source / "datasets" / "example.md").write_text("---\nid: example\n---\nexample\n", encoding="utf-8")
    (source / "dist").mkdir()
    (source / "dist" / "router_index.json").write_text(
        '{"datasets":[{"id":"example","source_path":"datasets/example.md"}]}\n', encoding="utf-8"
    )
    (source / "scripts").mkdir()
    shutil.copy2(Path(__file__).resolve().parents[1] / "scripts" / "benchmark_session.py", source / "scripts")
    benchmark_dir = source / "benchmarks" / "idea-routing"
    benchmark_dir.mkdir(parents=True)
    (benchmark_dir / "README.md").write_text("# Benchmark\n", encoding="utf-8")
    cases = []
    for index in range(case_count):
        cases.append(
            {
                "id": f"case-{index}",
                "family": "test",
                "difficulty": "medium",
                "prompt": f"formal {index}",
                "variants": {"oral": f"oral {index}", "incomplete": f"incomplete {index}"},
            }
        )
    import yaml

    (benchmark_dir / "public_cases.yaml").write_text(
        yaml.safe_dump({"version": 2, "cases": cases}, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    (source / "benchmarks" / "idea-regression.yaml").write_text("expected_top: [secret]\n", encoding="utf-8")
    (source / "benchmarks" / "latest-development-result.md").write_text("secret result\n", encoding="utf-8")
    (source / "agent-review-reports").mkdir()
    (source / "agent-review-reports" / "secret.md").write_text("secret report\n", encoding="utf-8")
    return source


def write_submission(workspace: Path, case_id: str) -> Path:
    path = workspace / ".benchmark" / "submission.json"
    path.write_text(
        json.dumps(
            {
                "case_id": case_id,
                "decision": "recommend",
                "recommended": ["example"],
                "shortlist": ["example"],
                "confidence": "medium",
                "answer": "The isolated local record supports this recommendation and states its limits.",
                "evidence_files": ["datasets/example.md"],
                "claim_traces": [
                    {
                        "dataset_id": "example",
                        "kind": "fit",
                        "claim": "The local record is the relevant canonical dataset.",
                        "evidence_file": "datasets/example.md",
                        "evidence_anchor": "body",
                    },
                    {
                        "dataset_id": "example",
                        "kind": "access",
                        "claim": "The local record states the available access boundary.",
                        "evidence_file": "datasets/example.md",
                        "evidence_anchor": "body",
                    },
                ],
                "files_read": ["dist/router_index.json", "datasets/example.md"],
                "search_terms": ["example"],
                "diagnostic_notes": "No protocol issue observed.",
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return path


def test_balanced_queue_is_reproducible_and_balanced(tmp_path: Path) -> None:
    source = make_source(tmp_path, case_count=6)
    import yaml

    cases = yaml.safe_load((source / "benchmarks" / "idea-routing" / "public_cases.yaml").read_text(encoding="utf-8"))["cases"]
    first = build_queue(cases, 42, "balanced")
    second = build_queue(cases, 42, "balanced")
    assert first == second
    assert {variant: sum(item["variant"] == variant for item in first) for variant in ("formal", "oral", "incomplete")} == {
        "formal": 2,
        "oral": 2,
        "incomplete": 2,
    }


def test_prepare_uses_an_allowlisted_answer_free_snapshot(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="claude-code",
        model_label="test-model",
        seed=42,
        variant_mode="balanced",
    )
    assert (workspace / "datasets" / "example.md").is_file()
    assert (workspace / "COLLECTION_PROFILE.md").is_file()
    assert not (workspace / "benchmarks" / "idea-regression.yaml").exists()
    assert not (workspace / "benchmarks" / "latest-development-result.md").exists()
    assert not (workspace / "agent-review-reports").exists()
    assert not (workspace / "benchmarks" / "idea-routing" / "public_cases.yaml").exists()
    manifest = json.loads((workspace / ".benchmark" / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["isolation"]["contains_hidden_gold"] is False
    assert manifest["case_count"] == 3


def test_prepare_rejects_a_run_directory_inside_the_source(tmp_path: Path) -> None:
    source = make_source(tmp_path)
    with pytest.raises(ValueError, match="outside the source repository"):
        prepare_session(
            source_root=source,
            output_root=source / "runs",
            agent_surface="test-agent",
            model_label="test-model",
            seed=42,
            variant_mode="balanced",
        )


def test_session_seals_answers_and_packages_complete_feedback(tmp_path: Path) -> None:
    source = make_source(tmp_path, case_count=1)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="kimi-code",
        model_label="test-model",
        seed=7,
        variant_mode="formal",
    )
    case = current_case(workspace)
    result = submit_case(workspace, write_submission(workspace, case["case_id"]))
    assert result["remaining"] == 0
    assert integrity_report(workspace)["complete"] is True

    feedback = "# Benchmark Run Feedback\n\n" + "\n\n".join(f"{heading}\n\n{'evidence ' * 30}" for heading in FEEDBACK_HEADINGS)
    (workspace / ".benchmark" / "FEEDBACK.md").write_text(feedback, encoding="utf-8")
    results = finish_session(workspace)
    assert (results / "answers.jsonl").is_file()
    assert json.loads((results / "integrity.json").read_text(encoding="utf-8"))["complete"] is True


def test_integrity_detects_post_submission_or_snapshot_changes(tmp_path: Path) -> None:
    source = make_source(tmp_path, case_count=1)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="test-agent",
        model_label="test-model",
        seed=1,
        variant_mode="formal",
    )
    case = current_case(workspace)
    submit_case(workspace, write_submission(workspace, case["case_id"]))
    answers = workspace / ".benchmark" / "answers.jsonl"
    answers.write_text(answers.read_text(encoding="utf-8").replace("medium", "high"), encoding="utf-8")
    (workspace / "README.md").write_text("changed\n", encoding="utf-8")
    report = integrity_report(workspace)
    assert report["complete"] is False
    assert report["modified_after_submission"] == [case["case_id"]]
    assert report["source_snapshot_hash_matches"] is False


def test_recommendation_requires_canonical_claim_traces(tmp_path: Path) -> None:
    source = make_source(tmp_path, case_count=1)
    workspace = prepare_session(
        source_root=source,
        output_root=tmp_path / "runs",
        agent_surface="test-agent",
        model_label="test-model",
        seed=1,
        variant_mode="formal",
    )
    case = current_case(workspace)
    submission = write_submission(workspace, case["case_id"])
    raw = json.loads(submission.read_text(encoding="utf-8"))
    raw["claim_traces"] = []
    submission.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(ValueError, match="needs a fit or coverage claim trace"):
        submit_case(workspace, submission)
