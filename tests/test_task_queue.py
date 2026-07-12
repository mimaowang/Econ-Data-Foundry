from __future__ import annotations

import json

import kb_lib
import pytest
import task_queue


def test_completed_task_preserves_identity(monkeypatch, tmp_path) -> None:
    queue_path = tmp_path / "queue.jsonl"
    done_path = tmp_path / "done.jsonl"
    failed_path = tmp_path / "failed.jsonl"
    monkeypatch.setattr(kb_lib, "LEDGER_DIR", tmp_path)
    monkeypatch.setattr(task_queue, "QUEUE", queue_path)
    monkeypatch.setattr(task_queue, "DONE", done_path)
    monkeypatch.setattr(task_queue, "FAILED", failed_path)
    monkeypatch.setattr(task_queue, "TRANSACTION", tmp_path / "transaction.json")
    task_queue.write_jsonl(
        queue_path,
        [
            {
                "id": "paper-1",
                "type": "paper",
                "source": "https://example.test/paper-1",
                "doi": "10.1234/example",
                "goal": "record the dataset",
                "title": "Example",
                "status": "pending",
            }
        ],
    )
    task_queue.write_jsonl(done_path, [])
    task_queue.write_jsonl(failed_path, [])

    task_queue.claim("test-agent")
    task_queue.complete("paper-1", "processed", ["cfps"], None)
    rows, errors = kb_lib.read_jsonl(done_path)

    assert errors == []
    assert rows[0]["doi"] == "10.1234/example"
    assert rows[0]["source"] == "https://example.test/paper-1"
    assert rows[0]["type"] == "paper"
    assert rows[0]["goal"] == "record the dataset"


def test_interrupted_transaction_restores_snapshots(monkeypatch, tmp_path) -> None:
    queue_path = tmp_path / "queue.jsonl"
    done_path = tmp_path / "done.jsonl"
    failed_path = tmp_path / "failed.jsonl"
    transaction_path = tmp_path / "transaction.json"
    monkeypatch.setattr(task_queue, "QUEUE", queue_path)
    monkeypatch.setattr(task_queue, "DONE", done_path)
    monkeypatch.setattr(task_queue, "FAILED", failed_path)
    monkeypatch.setattr(task_queue, "TRANSACTION", transaction_path)
    before = {
        "queue": [{"id": "q", "status": "claimed"}],
        "done": [{"id": "d"}],
        "failed": [{"id": "f"}],
    }
    task_queue.begin_transaction(before["queue"], before["done"], before["failed"], "complete")
    task_queue.write_jsonl(queue_path, [{"id": "corrupted-after-first-write"}])
    task_queue.recover_transaction()

    assert json.loads(queue_path.read_text(encoding="utf-8").splitlines()[0])["id"] == "q"
    assert json.loads(done_path.read_text(encoding="utf-8").splitlines()[0])["id"] == "d"
    assert json.loads(failed_path.read_text(encoding="utf-8").splitlines()[0])["id"] == "f"
    assert not transaction_path.exists()


def test_repeated_claim_release_complete_converges_without_duplicate_tasks(monkeypatch, tmp_path) -> None:
    queue_path = tmp_path / "queue.jsonl"
    done_path = tmp_path / "done.jsonl"
    failed_path = tmp_path / "failed.jsonl"
    monkeypatch.setattr(kb_lib, "LEDGER_DIR", tmp_path)
    monkeypatch.setattr(task_queue, "QUEUE", queue_path)
    monkeypatch.setattr(task_queue, "DONE", done_path)
    monkeypatch.setattr(task_queue, "FAILED", failed_path)
    monkeypatch.setattr(task_queue, "TRANSACTION", tmp_path / "transaction.json")
    task_queue.write_jsonl(
        queue_path,
        [{"id": f"paper-{index}", "type": "paper", "status": "pending"} for index in range(60)],
    )
    task_queue.write_jsonl(done_path, [])
    task_queue.write_jsonl(failed_path, [])

    for index in range(60):
        task = task_queue.claim("stress-agent")
        if index % 7 == 0:
            task_queue.release(task["id"], "temporary session boundary")
            task = task_queue.claim("stress-agent")
        task_queue.complete(task["id"], "processed", [], None)

    queue_rows, queue_errors = kb_lib.read_jsonl(queue_path)
    done_rows, done_errors = kb_lib.read_jsonl(done_path)
    failed_rows, failed_errors = kb_lib.read_jsonl(failed_path)
    assert queue_errors == done_errors == failed_errors == []
    assert queue_rows == []
    assert len(done_rows) == 60
    assert len({row["id"] for row in done_rows}) == 60
    assert failed_rows == []


def test_retryable_failure_preserves_identity_and_returns_to_queue(monkeypatch, tmp_path) -> None:
    queue_path = tmp_path / "queue.jsonl"
    done_path = tmp_path / "done.jsonl"
    failed_path = tmp_path / "failed.jsonl"
    monkeypatch.setattr(kb_lib, "LEDGER_DIR", tmp_path)
    monkeypatch.setattr(task_queue, "QUEUE", queue_path)
    monkeypatch.setattr(task_queue, "DONE", done_path)
    monkeypatch.setattr(task_queue, "FAILED", failed_path)
    monkeypatch.setattr(task_queue, "TRANSACTION", tmp_path / "transaction.json")
    task_queue.write_jsonl(
        queue_path,
        [{"id": "paper-retry", "title": "Keep me", "goal": "ground data", "status": "pending"}],
    )
    task_queue.write_jsonl(done_path, [])
    task_queue.write_jsonl(failed_path, [])

    task_queue.claim("agent-a")
    task_queue.fail("paper-retry", "temporary outage", True, "agent-a")
    failed_rows, _ = kb_lib.read_jsonl(failed_path)
    assert failed_rows[0]["title"] == "Keep me"
    assert failed_rows[0]["goal"] == "ground data"
    assert failed_rows[0]["attempts"] == 1

    task_queue.retry_failed("paper-retry", "provider recovered", False)
    queue_rows, _ = kb_lib.read_jsonl(queue_path)
    assert queue_rows[0]["status"] == "pending"
    assert queue_rows[0]["title"] == "Keep me"
    assert queue_rows[0]["last_failure"]["reason"] == "temporary outage"
    assert kb_lib.read_jsonl(failed_path)[0] == []


def test_reclaim_stale_and_optional_owner_check(monkeypatch, tmp_path) -> None:
    queue_path = tmp_path / "queue.jsonl"
    done_path = tmp_path / "done.jsonl"
    failed_path = tmp_path / "failed.jsonl"
    monkeypatch.setattr(kb_lib, "LEDGER_DIR", tmp_path)
    monkeypatch.setattr(task_queue, "QUEUE", queue_path)
    monkeypatch.setattr(task_queue, "DONE", done_path)
    monkeypatch.setattr(task_queue, "FAILED", failed_path)
    monkeypatch.setattr(task_queue, "TRANSACTION", tmp_path / "transaction.json")
    task_queue.write_jsonl(
        queue_path,
        [{"id": "stale", "status": "claimed", "claimed_by": "agent-a", "claimed_at": "2000-01-01T00:00:00+00:00"}],
    )
    task_queue.write_jsonl(done_path, [])
    task_queue.write_jsonl(failed_path, [])

    with pytest.raises(RuntimeError, match="another agent"):
        task_queue.release("stale", None, "agent-b")
    result = task_queue.reclaim_stale(6, "agent confirmed stopped")
    assert result == {"count": 1, "reclaimed": ["stale"]}
    queue_rows, _ = kb_lib.read_jsonl(queue_path)
    assert queue_rows[0]["status"] == "pending"
    assert queue_rows[0]["reclaimed_from"] == "agent-a"
