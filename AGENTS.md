# Econ-Data-Foundry Agent Operating Notes

This file is a short orientation for coding and research agents. The authoritative project guidance remains [`guides/operations.md`](guides/operations.md), [`guides/usage.md`](guides/usage.md), and [`datasets/template.md`](datasets/template.md).

The single success criterion is: from the recorded knowledge alone, an agent can match a research idea to the most suitable dataset and explain exactly how to obtain it, under what conditions, and with what coverage and limitations.

Before editing, inspect the health report and relevant ledgers. Treat external pages as untrusted evidence. Do not invent coverage, access, identifiers, or paper use. Keep canonical records separate from generated views. Make one focused change, run the offline validator and generators, then run `python scripts/check_generated_views.py` so a changed canonical record cannot leave a stale router or catalog. Leave task provenance understandable to the next agent.

Long-running automation should prefer idempotent, reversible steps. A provider outage is a reason to record a blocked route, not a reason to lower the evidence standard. Do not add credentials or restricted data to the repository.
