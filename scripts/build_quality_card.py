from __future__ import annotations

import json
import sys
from collections import Counter

sys.dont_write_bytecode = True

from kb_lib import LEDGER_DIR, atomic_write_text, load_datasets, read_jsonl, workspace_lock  # noqa: E402


def build() -> str:
    records, failures = load_datasets()
    statuses = Counter(record.status for record in records)
    active = [record for record in records if record.status != "deprecated"]
    health_path = LEDGER_DIR / "health.json"
    health = {}
    if health_path.exists():
        health = json.loads(health_path.read_text(encoding="utf-8"))
    candidates, _ = read_jsonl(LEDGER_DIR / "dataset_candidates.jsonl")
    pending, _ = read_jsonl(LEDGER_DIR / "pending_tasks.jsonl")
    failed, _ = read_jsonl(LEDGER_DIR / "failed_tasks.jsonl")
    paper_evidence = health.get("paper_evidence") if isinstance(health.get("paper_evidence"), dict) else {}
    lines = [
        "# Quality Card",
        "",
        "> Generated from canonical records and ledgers. Do not edit by hand.",
        "",
        "## Core Gate",
        "",
        "The release question is whether recorded knowledge can route a research idea to a suitable dataset and explain how to obtain it, under what conditions, and with what coverage and limitations.",
        "",
        f"- Health status: `{health.get('status', 'not-generated')}`; errors `{len(health.get('errors', []))}`; warnings `{len(health.get('warnings', []))}`",
        f"- Canonical records: `{len(records)}` total; `{len(active)}` active; `{statuses['ready']}` ready; `{statuses['grounding']}` grounding; `{statuses['needs-review']}` needs-review; `{statuses['candidate']}` candidate; `{statuses['deprecated']}` deprecated",
        f"- Queue: `{len(pending)}` pending/claimed; `{len(failed)}` failed/blocked; candidates `{len(candidates)}`",
        f"- Parse failures: `{len(failures)}`",
        (
            "- Paper-use traceability: "
            f"`{paper_evidence.get('structured_complete', 0)}/{paper_evidence.get('total', 0)}` records include "
            "cite, role, evidence type/URL, and data note; incomplete legacy entries are a grounding backlog."
        ),
        "",
        "## Interpretation",
        "",
        "`ready` records may be recommended directly. `grounding`, `needs-review`, and `candidate` records are leads with explicit uncertainty and must not be presented as equally verified. Counts are operational signals, not a substitute for idea-routing accuracy.",
        "",
        "## Required Release Checks",
        "",
        "```text",
        "python scripts/check_secrets.py",
        "python scripts/validate_kb.py --write-report",
        "python scripts/build_views.py",
        "python scripts/export_catalog.py",
        "python scripts/build_site.py",
        "python scripts/build_quality_card.py",
        "python scripts/check_generated_views.py",
        "python -m pytest",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    with workspace_lock("derived-views"):
        atomic_write_text(LEDGER_DIR / "quality-card.md", build())
    print("generated ledgers/quality-card.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
