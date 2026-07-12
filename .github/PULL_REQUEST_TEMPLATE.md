## What changed?

<!-- State the user-visible improvement in one or two sentences. -->

## Why is it correct?

- Canonical records or scripts changed:
- Evidence or source checked:
- Access, coverage, join, or licensing implications:

## Checks

- [ ] `python scripts/check_secrets.py`
- [ ] `python scripts/validate_kb.py --write-report`
- [ ] `python scripts/build_views.py`
- [ ] `python scripts/validate_kb.py`
- [ ] `python scripts/export_catalog.py`
- [ ] `python -m pytest`

## Safety

- [ ] No credentials, restricted data, browser sessions, or raw provider challenge pages were added.
- [ ] Generated files are synchronized.
- [ ] Uncertain facts remain marked `grounding`, `needs-review`, or `candidate`.
