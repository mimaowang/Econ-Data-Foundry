# Contributing

Thank you for improving the knowledge base. The most valuable contribution is a record that lets a future agent match a research idea to a dataset and actually obtain it.

## Before You Change Anything

Start with [`AGENTS.md`](AGENTS.md) and [`guides/mental-model.md`](guides/mental-model.md) to understand the decisions the records should support. Use [`guides/operations.md`](guides/operations.md) for maintenance and [`datasets/template.md`](datasets/template.md) when writing a record. Treat `datasets/*.md` as canonical source files. `DATASET_INDEX.md`, `ledgers/aliases.md`, `ledgers/progress.md`, `dist/` and `docs/` are generated outputs.

## Dataset Record Standard

Prefer a small, well-grounded change over a broad speculative addition. A useful record should make these decisions explicit:

- the best research ideas and the nearby ideas for which the dataset is a poor choice;
- unit of observation, structure, geography, frequency, time coverage, and the latest confirmed release;
- variables and real identifying variation, including important exclusions;
- stable identifiers and realistic join conditions;
- the best acquisition route, direct URL, requirements, steps, deliverable, cost, license, and last checked date;
- evidence and provenance for claims that matter to research or access.

Do not promote a record to `ready` merely because it has a familiar name or a landing page. `grounding` is the correct status when the dataset is promising but the access route, coverage, or research-fit evidence is not yet sufficiently verified.

## Local Checks

Use Python 3.10 or later:

```text
python -m pip install -r requirements-dev.txt
python scripts/check_secrets.py
python scripts/validate_kb.py --write-report
python scripts/build_views.py
python scripts/export_catalog.py
python scripts/build_site.py
python scripts/build_quality_card.py
python scripts/check_generated_views.py
python scripts/validate_kb.py
python -m pytest
python -m ruff check .
```

On Windows, use backslashes if preferred. Do not commit credentials, restricted data, raw downloads, browser profiles, or provider challenge pages. Network access is not required for the local quality gate.

## Queue and Agent Work

Claim one queue item, preserve its source identity, and complete or release it with a concise result. Keep task ledgers machine-readable. If an external source is blocked, record the failure and a useful next action rather than filling facts from memory.

## Pull Requests

Describe the user-visible improvement, the records or scripts affected, the evidence used, and the checks you ran. Keep generated files in sync. A pull request that changes a canonical record should normally include the regenerated views and catalog artifacts.

When publishing accumulated local work, review the file list as well as the diff: new canonical records and linked guides belong in the update, while downloaded source files, temporary scripts and personal run logs stay local. The ignore patterns cover known scratch locations without excluding `datasets/` or the durable ledgers. Keep existing local materials in place; publication does not require deleting them. Check the remote changes before updating workflows or dependencies so a content release preserves fixes already merged upstream.
