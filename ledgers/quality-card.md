# Quality Card

> Generated from canonical records and ledgers. Do not edit by hand.

## Core Gate

The release question is whether recorded knowledge can route a research idea to a suitable dataset and explain how to obtain it, under what conditions, and with what coverage and limitations.

- Health status: `ok`; errors `0`; warnings `0`
- Canonical records: `25` total; `24` active; `11` ready; `13` grounding; `0` needs-review; `0` candidate; `1` deprecated
- Queue: `46` pending/claimed; `2` failed/blocked; candidates `10`
- Parse failures: `0`
- Paper-use traceability: `13/67` records include cite, role, evidence type/URL, and data note; incomplete legacy entries are a grounding backlog.

## Interpretation

`ready` records may be recommended directly. `grounding`, `needs-review`, and `candidate` records are leads with explicit uncertainty and must not be presented as equally verified. Counts are operational signals, not a substitute for idea-routing accuracy.

## Required Release Checks

```text
python scripts/check_secrets.py
python scripts/validate_kb.py --write-report
python scripts/build_views.py
python scripts/export_catalog.py
python scripts/build_site.py
python scripts/build_quality_card.py
python scripts/check_generated_views.py
python -m pytest
```
