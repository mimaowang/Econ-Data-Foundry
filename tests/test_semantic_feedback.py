from __future__ import annotations

import json

import validate_kb
from validate_kb import Audit, semantic_audit_summary


def knowledge_task(index: int) -> dict:
    return {
        "id": f"task-{index}",
        "type": "paper",
        "result": "processed",
        "datasets_touched": ["cfps"],
        "finished_at": f"2026-08-{index + 1:02d}T10:00:00+08:00",
    }


def passing_audit(day: int = 1) -> dict:
    return {
        "id": "audit-pass",
        "type": "semantic-audit",
        "result": "audited",
        "audit_outcome": "pass",
        "datasets_reviewed": ["cfps"],
        "finished_at": f"2026-08-{day:02d}T09:00:00+08:00",
    }


def test_semantic_audit_is_due_when_no_prior_audit_exists() -> None:
    assert semantic_audit_summary([]) == {
        "due": True,
        "reason": "no-prior-audit",
        "interpretation": (
            "Advisory slow feedback, not a quality score or automatic status change. When due, prioritize one semantic-audit "
            "task and test recent records from a fresh context before expanding. The threshold is a maximum feedback delay, "
            "not a productivity target."
        ),
    }


def test_semantic_audit_interval_is_a_delay_not_a_progress_score() -> None:
    rows = [passing_audit(), *(knowledge_task(index) for index in range(1, 5))]
    assert semantic_audit_summary(rows)["reason"] == "current"
    rows.append(knowledge_task(5))
    assert semantic_audit_summary(rows)["reason"] == "interval-reached"


def test_failed_semantic_audit_keeps_feedback_due() -> None:
    row = passing_audit()
    row["audit_outcome"] = "repair-needed"
    assert semantic_audit_summary([row])["reason"] == "repair-needed"


def test_semantic_feedback_uses_append_order_when_timestamps_are_equal() -> None:
    audit = passing_audit()
    task = knowledge_task(1)
    task["finished_at"] = audit["finished_at"]
    rows = [audit, task, task | {"id": "task-2"}, task | {"id": "task-3"}, task | {"id": "task-4"}]
    assert semantic_audit_summary(rows)["reason"] == "current"
    rows.append(task | {"id": "task-5"})
    assert semantic_audit_summary(rows)["reason"] == "interval-reached"


def test_ledger_validation_keeps_reviewed_and_touched_semantics_separate(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(validate_kb, "LEDGER_DIR", tmp_path)
    rows = {
        "pending_tasks.jsonl": [],
        "completed_tasks.jsonl": [passing_audit()],
        "failed_tasks.jsonl": [],
        "dataset_candidates.jsonl": [],
        "changes.jsonl": [],
    }
    rows["completed_tasks.jsonl"][0]["note"] = "Fresh-context comparison found the route usable"
    for name, values in rows.items():
        (tmp_path / name).write_text(
            "".join(json.dumps(value) + "\n" for value in values),
            encoding="utf-8",
        )

    audit = Audit()
    validate_kb.validate_ledgers(audit, {"cfps"}, {"cfps"})

    assert audit.errors == []


def test_ledger_validation_allows_review_of_deprecated_canonical_identity(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(validate_kb, "LEDGER_DIR", tmp_path)
    row = passing_audit()
    row["datasets_reviewed"] = ["china-pollution"]
    row["note"] = "Verified that the deprecated identity redirects to the three coherent pollution products"
    files = {
        "pending_tasks.jsonl": [],
        "completed_tasks.jsonl": [row],
        "failed_tasks.jsonl": [],
        "dataset_candidates.jsonl": [],
        "changes.jsonl": [],
    }
    for name, values in files.items():
        (tmp_path / name).write_text("".join(json.dumps(value) + "\n" for value in values), encoding="utf-8")

    audit = Audit()
    validate_kb.validate_ledgers(audit, {"cfps"}, {"cfps", "china-pollution"})

    assert audit.errors == []
