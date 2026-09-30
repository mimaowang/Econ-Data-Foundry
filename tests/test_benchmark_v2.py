from __future__ import annotations

import json

from benchmark_session import find_forbidden_keys
from benchmark_v2 import load_public_cases, score_answer, score_answers, trace_drift
from export_catalog import router_index_payload
from kb_lib import load_datasets


def test_public_benchmark_has_no_answer_leakage() -> None:
    cases = load_public_cases()
    assert len(cases) >= 20
    forbidden = {
        "expected_top",
        "acceptable",
        "avoid",
        "must_explain",
        "required_any",
        "required_mentions",
        "must_not_claim",
        "gold",
    }
    assert all(not forbidden.intersection(case) for case in cases)


def test_public_benchmark_leakage_check_is_recursive() -> None:
    assert find_forbidden_keys({"variants": {"oral": {"gold": "secret"}}}) == {"gold"}


def test_answer_precheck_rewards_a_correct_shortlist_and_required_limits() -> None:
    reference = {
        "decision": "recommend",
        "expected_top": ["chfs"],
        "acceptable": ["cfps"],
        "avoid": ["charls"],
        "required_any": [["assets", "liabilities"], ["consumption"]],
        "required_mentions": ["application"],
        "must_not_claim": ["unrestricted public download"],
    }
    result = score_answer(
        {
            "case_id": "test",
            "recommended": ["chfs"],
            "shortlist": ["chfs", "cfps"],
            "answer": "CHFS is preferred for deeper assets, liabilities, and consumption; the files are not downloadable without approval.",
            "files_read": ["DATASET_INDEX.md", "datasets/chfs.md"],
        },
        reference,
    )
    assert result["choice_hit"] is True
    assert result["avoid_recommended"] == []
    assert result["shortlist_recall"] == 1.0
    assert result["critical_failure"] is False


def test_answer_precheck_prefers_observed_file_trace() -> None:
    result = score_answer(
        {
            "case_id": "trace",
            "recommended": ["chfs"],
            "answer": "CHFS",
            "files_read": ["claimed-but-not-observed.md"],
            "observed_files_read": ["DATASET_INDEX.md", "datasets/chfs.md"],
        },
        {"expected_top": ["chfs"]},
    )
    assert result["files_read"] == 2
    assert result["files_read_source"] == "tool-observed"
    assert result["self_reported_files_read"] == 1


def test_router_index_keeps_decision_fields_and_access_routes_compact() -> None:
    records, failures = load_datasets()
    assert not failures
    payload = router_index_payload(records)
    assert payload["router_index_schema_version"] == 2
    assert payload["record_count"] == len(records)
    census = next(item for item in payload["datasets"] if item["id"] == "china-census")
    assert census["research_fit"]["best_for"]
    assert census["research_fit"]["choose_over"]
    assert census["linkable_keys"]
    assert census["access"]["routes"]
    assert all("steps" not in route and "requirements" not in route for route in census["access"]["routes"])
    assert "description_markdown" not in census
    assert "production" not in census
    json.dumps(payload, ensure_ascii=False)


def test_answer_scoring_rejects_incomplete_and_duplicate_runs(tmp_path) -> None:
    answer_path = tmp_path / "answers.jsonl"
    answer_path.write_text(
        '{"case_id":"chfs-asset-consumption","recommended":["chfs"],"answer":"Use after application."}\n'
        '{"case_id":"chfs-asset-consumption","recommended":["chfs"],"answer":"Duplicate."}\n',
        encoding="utf-8",
    )
    public = [{"id": "chfs-asset-consumption", "prompt": "test"}]
    reference = {"chfs-asset-consumption": {"decision": "recommend", "expected_top": ["chfs"]}}
    result = score_answers(answer_path, public[:1], reference)
    assert result["complete"] is False
    assert any("duplicate" in error for error in result["errors"])
    assert result["missing_case_ids"] == []


def test_trace_drift_flags_material_quality_regression(tmp_path) -> None:
    trace_path = tmp_path / "trace.jsonl"
    rows = []
    for turn in range(1, 7):
        rows.append(
            json.dumps(
                {
                    "turn": turn,
                    "heuristic_score": 95 if turn <= 3 else 75,
                    "choice_hit": 1 if turn <= 3 else 0,
                    "critical_failure": 0 if turn <= 3 else 1,
                    "elapsed_seconds": 10,
                }
            )
        )
    trace_path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    result = trace_drift(trace_path, window=3)
    assert result["degradation_flag"] is True
    assert result["metrics"]["heuristic_score"]["delta_last_minus_first"] == -20.0
