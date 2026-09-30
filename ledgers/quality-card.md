# Quality Card

> Generated from canonical records and ledgers. Do not edit by hand.

## Core Gate

The release question is whether recorded knowledge can route a research idea to a suitable dataset and explain how to obtain it, under what conditions, and with what coverage and limitations.

- Health status: `ok`; errors `0`; warnings `1`
- Canonical records: `157` total; `155` active; `89` ready; `65` grounding; `1` needs-review; `0` candidate; `2` deprecated
- Queue: `0` pending/claimed; `157` failed/blocked; candidates `49`
- Parse failures: `0`
- Data pathways: `collected` 15; `constructed` 4; `direct` 86; `hybrid` 7; `inaccessible` 21; `legacy-v2` 22
- Data origins: `legacy-v2` 22; `mixed` 3; `ready-made` 73; `researcher-collected` 31; `researcher-constructed` 25; `unknown` 1
- Paper-use field completeness: `331/331` paper-use entries include cite, role, evidence type/URL, and data note. This counts populated fields, not full-text verification.
- Semantic feedback: `due`; reason `interval-reached`

## Interpretation

`ready` records may be recommended within their documented coverage and access conditions; this does not imply a free download or verified full-text evidence for every paper listed. Producer-grounded products can lack a verified paper-use entry. `grounding`, `needs-review`, and `candidate` records retain explicit uncertainty and must not be presented as equally verified. Counts are operational signals, not a substitute for idea-routing accuracy. A due semantic audit is an advisory request for fresh-context testing, not a failing score or an automatic status change.

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
python -m ruff check .
```
