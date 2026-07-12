from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.dont_write_bytecode = True

from kb_lib import LEDGER_DIR, dump_json, read_jsonl, workspace_lock, write_jsonl  # noqa: E402


QUEUE = LEDGER_DIR / "pending_tasks.jsonl"
DONE = LEDGER_DIR / "completed_tasks.jsonl"
FAILED = LEDGER_DIR / "failed_tasks.jsonl"
TRANSACTION = LEDGER_DIR / ".task-queue.transaction.json"


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def parse_timestamp(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        return parsed.astimezone()
    return parsed


def load_or_fail(path: Path) -> list[dict]:
    rows, errors = read_jsonl(path)
    if errors:
        raise RuntimeError(f"{path.name} is invalid: {'; '.join(errors)}")
    return rows


def recover_transaction() -> None:
    """Restore the pre-transition snapshot after an interrupted two-file write."""
    if not TRANSACTION.exists():
        return
    try:
        transaction = json.loads(TRANSACTION.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"task queue transaction is unreadable: {TRANSACTION}") from exc
    if not isinstance(transaction, dict) or transaction.get("version") != 1:
        raise RuntimeError(f"task queue transaction has an unsupported format: {TRANSACTION}")
    snapshots = {"queue": QUEUE, "done": DONE, "failed": FAILED}
    for key, path in snapshots.items():
        rows = transaction.get(key)
        if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
            raise RuntimeError(f"task queue transaction has an invalid {key} snapshot")
        write_jsonl(path, rows)
    TRANSACTION.unlink()


def begin_transaction(queue: list[dict], done: list[dict], failed: list[dict], operation: str) -> None:
    dump_json(
        TRANSACTION,
        {
            "version": 1,
            "operation": operation,
            "created_at": now(),
            "queue": queue,
            "done": done,
            "failed": failed,
        },
    )


def finish_transaction() -> None:
    try:
        TRANSACTION.unlink()
    except FileNotFoundError:
        pass


def claim(agent: str) -> dict:
    with workspace_lock("task-queue"):
        recover_transaction()
        queue = load_or_fail(QUEUE)
        done = load_or_fail(DONE)
        failed = load_or_fail(FAILED)
        closed = {str(row.get("id")) for row in done + failed}
        for task in queue:
            if task.get("status") == "pending" and str(task.get("id")) not in closed:
                task["status"] = "claimed"
                task["claimed_by"] = agent
                task["claimed_at"] = now()
                write_jsonl(QUEUE, queue)
                return task
    raise RuntimeError("no claimable pending task")


def peek() -> dict:
    if TRANSACTION.exists():
        raise RuntimeError("task queue has an interrupted transaction; run a mutating queue command to recover it")
    queue = load_or_fail(QUEUE)
    done = load_or_fail(DONE)
    failed = load_or_fail(FAILED)
    closed = {str(row.get("id")) for row in done + failed}
    for task in queue:
        if task.get("status") == "pending" and str(task.get("id")) not in closed:
            return task
    raise RuntimeError("no claimable pending task")


def find_claimed(queue: list[dict], task_id: str, agent: str | None = None) -> tuple[int, dict]:
    for index, task in enumerate(queue):
        if str(task.get("id")) == task_id:
            if task.get("status") != "claimed":
                raise RuntimeError(f"task {task_id} is not claimed")
            if agent and task.get("claimed_by") not in (None, agent):
                raise RuntimeError(f"task {task_id} is claimed by another agent")
            return index, task
    raise RuntimeError(f"task {task_id} not found in queue")


def complete(task_id: str, result: str, datasets: list[str], note: str | None, agent: str | None = None) -> dict:
    with workspace_lock("task-queue"):
        recover_transaction()
        queue = load_or_fail(QUEUE)
        done = load_or_fail(DONE)
        failed = load_or_fail(FAILED)
        index, task = find_claimed(queue, task_id, agent)
        if any(str(row.get("id")) == task_id for row in done):
            raise RuntimeError(f"task {task_id} already exists in completed ledger")
        record = {
            "id": task_id,
            "journal": task.get("journal"),
            "title": task.get("title"),
            "year": task.get("year"),
            "type": task.get("type"),
            "source": task.get("source"),
            "doi": task.get("doi"),
            "goal": task.get("goal"),
            "result": result,
            "datasets_touched": datasets,
            "finished_at": now(),
            "claimed_by": task.get("claimed_by"),
        }
        if note:
            record["note"] = note
        queue.pop(index)
        done.append({key: value for key, value in record.items() if value is not None})
        begin_transaction(queue=load_or_fail(QUEUE), done=load_or_fail(DONE), failed=failed, operation="complete")
        try:
            write_jsonl(QUEUE, queue)
            write_jsonl(DONE, done)
        except Exception:
            raise
        else:
            finish_transaction()
        return record


def fail(task_id: str, reason: str, retryable: bool, agent: str | None = None) -> dict:
    with workspace_lock("task-queue"):
        recover_transaction()
        queue = load_or_fail(QUEUE)
        done = load_or_fail(DONE)
        failed = load_or_fail(FAILED)
        index, task = find_claimed(queue, task_id, agent)
        if any(str(row.get("id")) == task_id for row in failed):
            raise RuntimeError(f"task {task_id} already exists in failure ledger")
        record = dict(task)
        record.update(
            {
                "status": "failed",
                "reason": reason,
                "retryable": retryable,
                "last_attempt": now(),
                "attempts": int(task.get("attempts", 0)) + 1,
            }
        )
        record.pop("claimed_at", None)
        queue.pop(index)
        failed.append(record)
        begin_transaction(queue=load_or_fail(QUEUE), done=done, failed=load_or_fail(FAILED), operation="fail")
        try:
            write_jsonl(QUEUE, queue)
            write_jsonl(FAILED, failed)
        except Exception:
            raise
        else:
            finish_transaction()
        return record


def release(task_id: str, note: str | None, agent: str | None = None) -> dict:
    with workspace_lock("task-queue"):
        recover_transaction()
        queue = load_or_fail(QUEUE)
        _, task = find_claimed(queue, task_id, agent)
        task["status"] = "pending"
        task.pop("claimed_by", None)
        task.pop("claimed_at", None)
        if note:
            task["release_note"] = note
        write_jsonl(QUEUE, queue)
        return task


def reclaim_stale(older_than_hours: float, note: str | None) -> dict:
    if older_than_hours <= 0:
        raise RuntimeError("older-than-hours must be positive")
    cutoff = datetime.now().astimezone() - timedelta(hours=older_than_hours)
    with workspace_lock("task-queue"):
        recover_transaction()
        queue = load_or_fail(QUEUE)
        reclaimed: list[str] = []
        for task in queue:
            if task.get("status") != "claimed":
                continue
            claimed_at = parse_timestamp(task.get("claimed_at"))
            if claimed_at is None or claimed_at > cutoff:
                continue
            task["status"] = "pending"
            task["reclaimed_from"] = task.pop("claimed_by", None)
            task.pop("claimed_at", None)
            task["reclaimed_at"] = now()
            if note:
                task["reclaim_note"] = note
            reclaimed.append(str(task.get("id", "")))
        if reclaimed:
            write_jsonl(QUEUE, queue)
        return {"count": len(reclaimed), "reclaimed": reclaimed}


def retry_failed(task_id: str, note: str | None, force: bool) -> dict:
    with workspace_lock("task-queue"):
        recover_transaction()
        queue = load_or_fail(QUEUE)
        done = load_or_fail(DONE)
        failed = load_or_fail(FAILED)
        if any(str(row.get("id")) == task_id for row in queue + done):
            raise RuntimeError(f"task {task_id} already exists in queue or completed ledger")
        index = next((index for index, row in enumerate(failed) if str(row.get("id")) == task_id), None)
        if index is None:
            raise RuntimeError(f"failed task {task_id} not found")
        record = failed[index]
        if not record.get("retryable") and not force:
            raise RuntimeError(f"failed task {task_id} is not marked retryable; use --force to override")
        begin_transaction(queue=queue, done=done, failed=failed, operation="retry")
        task = dict(record)
        task["status"] = "pending"
        task["last_failure"] = {
            key: record.get(key)
            for key in ("reason", "last_attempt", "claimed_by")
            if record.get(key) is not None
        }
        for key in ("reason", "retryable", "last_attempt", "claimed_by"):
            task.pop(key, None)
        if note:
            task["retry_note"] = note
        failed.pop(index)
        queue.append(task)
        try:
            write_jsonl(QUEUE, queue)
            write_jsonl(FAILED, failed)
        except Exception:
            raise
        else:
            finish_transaction()
        return task


def main() -> int:
    parser = argparse.ArgumentParser(description="Atomically claim and transition knowledge-base tasks.")
    sub = parser.add_subparsers(dest="command", required=True)

    claim_parser = sub.add_parser("claim")
    claim_parser.add_argument("--agent", required=True)

    sub.add_parser("peek")

    complete_parser = sub.add_parser("complete")
    complete_parser.add_argument("--id", required=True)
    complete_parser.add_argument("--result", choices=["processed", "skipped", "needs-review"], required=True)
    complete_parser.add_argument("--dataset", action="append", default=[])
    complete_parser.add_argument("--note")
    complete_parser.add_argument("--agent")

    fail_parser = sub.add_parser("fail")
    fail_parser.add_argument("--id", required=True)
    fail_parser.add_argument("--reason", required=True)
    fail_parser.add_argument("--retryable", action="store_true")
    fail_parser.add_argument("--agent")

    release_parser = sub.add_parser("release")
    release_parser.add_argument("--id", required=True)
    release_parser.add_argument("--note")
    release_parser.add_argument("--agent")

    reclaim_parser = sub.add_parser("reclaim-stale")
    reclaim_parser.add_argument("--older-than-hours", type=float, default=6.0)
    reclaim_parser.add_argument("--note")

    retry_parser = sub.add_parser("retry")
    retry_parser.add_argument("--id", required=True)
    retry_parser.add_argument("--note")
    retry_parser.add_argument("--force", action="store_true")

    args = parser.parse_args()
    if args.command == "peek":
        result = peek()
    elif args.command == "claim":
        result = claim(args.agent)
    elif args.command == "complete":
        result = complete(args.id, args.result, args.dataset, args.note, args.agent)
    elif args.command == "fail":
        result = fail(args.id, args.reason, args.retryable, args.agent)
    elif args.command == "release":
        result = release(args.id, args.note, args.agent)
    elif args.command == "reclaim-stale":
        result = reclaim_stale(args.older_than_hours, args.note)
    else:
        result = retry_failed(args.id, args.note, args.force)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
