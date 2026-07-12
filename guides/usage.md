# Using Econ-Data-Foundry

Econ-Data-Foundry is both a dataset knowledge base and an operating system for agents that maintain it. Canonical records answer research questions; ledgers preserve work state; deterministic generators expose the same knowledge to humans, agents, scripts, and GitHub Pages.

## Repository map

| Path | Purpose |
|---|---|
| `README.md` | Public overview and quick start |
| `AGENTS.md` | Short cold-start orientation for coding and research agents |
| `guides/operations.md` | Mission, evidence rules, status discipline, and automation workflow |
| `guides/adaptation.md` | Retargeting the foundry to another geography or domain |
| `datasets/*.md` | Canonical dataset records; one coherent data product per file |
| `datasets/template.md` | Record schema and writing prompts |
| `DATASET_INDEX.md` | Generated human-readable dataset router |
| `dist/router_index.json` | Compact first-pass router for agents |
| `dist/catalog.json` | Full machine-readable export |
| `sources/` | Discovery channels and source seeds |
| `ledgers/pending_tasks.jsonl` | Unclaimed and claimed work |
| `ledgers/completed_tasks.jsonl` | Completed work and touched records |
| `ledgers/failed_tasks.jsonl` | Blocked work, retry state, and next actions |
| `ledgers/dataset_candidates.jsonl` | Leads below canonical publication quality |
| `ledgers/changes.jsonl` | Corrections, splits, merges, promotions, and downgrades |
| `ledgers/health.json` | Generated validator report |
| `ledgers/quality-card.md` | Generated operational quality summary |
| `benchmarks/idea-routing/` | Isolated idea-to-dataset benchmark |
| `benchmarks/collection/` | Isolated literature-to-knowledge benchmark |
| `scripts/` | Validation, queue, export, benchmark, and generation tools |
| `schema/` | JSON Schema and controlled vocabularies |
| `tests/` | Offline regression tests |
| `dist/` and `docs/` | Generated public artifacts and static site |

## Install and verify

Python 3.10 or newer is required.

```powershell
python -m pip install -r requirements-dev.txt
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

On macOS or Linux, use `/` in paths. All required release checks are offline. `scripts/check_links.py` is an optional network freshness diagnostic and never edits canonical records.

## Match a research idea to data

1. Translate the idea into population, unit of observation, outcomes, treatment or variation, geography, time, frequency, and access constraints. Do not force a polished idea when clarification is genuinely needed.
2. Search `dist/router_index.json` by aliases, topics, variables, coverage, and access status to form a small candidate set.
3. Open the corresponding canonical files in `datasets/`. The router is for recall; only canonical records support final factual claims.
4. Compare `research_fit`, coverage, observation unit, variables, variation, joins, access routes, and caveats.
5. Recommend the best record, explain why close alternatives lose, identify required joins, and give an executable acquisition recipe.
6. Distinguish recorded facts from unresolved knowledge. Never fill a repository gap with an ad hoc web search when the task is an offline routing answer.

A useful response usually covers: recommendation and alternatives; observation unit and coverage; observable variables and identification variation; required joins; direct access route, requirements, steps, cost, and deliverable; limitations and confidence.

## Maintain the knowledge base

Read [`operations.md`](operations.md) before editing. Then:

1. Inspect `ledgers/health.json`, pending work, failures, candidates, and recent changes.
2. Claim one task or define one narrow, high-value unit.
3. Verify dataset identity before collecting attractive details.
4. Use sources appropriate to each claim and record what they support.
5. Update one canonical record, consolidate an identity, record a candidate, or skip the lead honestly.
6. Complete or release the task and run the full gate.

Do not edit generated views manually. Do not commit downloaded datasets, provider HTML, credentials, private evaluator materials, or restricted microdata.

## Task queue commands

```powershell
# Inspect available work
python scripts/task_queue.py peek

# Claim one item
python scripts/task_queue.py claim --agent claude-code

# Complete the claimed task
python scripts/task_queue.py complete --id <task-id> --result processed --dataset <dataset-id> --agent claude-code

# Return unfinished work without pretending it succeeded
python scripts/task_queue.py release --id <task-id> --note "Released for the next run" --agent claude-code

# Record a retryable source failure
python scripts/task_queue.py fail --id <task-id> --reason "Provider route blocked" --retryable --agent claude-code

# Recover only confirmed stale ownership
python scripts/task_queue.py reclaim-stale --older-than-hours 6 --note "Previous agent is no longer running"

# Retry after the blocking condition changes
python scripts/task_queue.py retry --id <failed-task-id> --note "Provider route is available again"
```

Run `python scripts/task_queue.py --help` for the current command contract.

## Record and status conventions

Use the filename `<id>.md`, where `id` is lowercase ASCII with hyphens. Keep official Chinese names in `aka` when they are useful search keys. Public explanations should be English.

`ready` means directly recommendable from grounded knowledge. `grounding` means useful with a material unresolved gap. `needs-review` marks stale or conflicting knowledge. `candidate` is a lead, not a recommendation. `deprecated` is a redirect.

## Generated artifacts

`scripts/build_views.py` creates `DATASET_INDEX.md`, `ledgers/aliases.md`, and `ledgers/progress.md`. `scripts/export_catalog.py` creates deterministic JSON, JSONL, CSV, JSON-LD, router, join graph, and checksum artifacts in `dist/`. `scripts/build_site.py` publishes the read-only router to `docs/`. `scripts/check_generated_views.py` rebuilds these outputs in a temporary workspace and compares bytes, so stale checked-in views cannot pass silently.

## Benchmarks and private runs

The two public harnesses create isolated workspaces outside the repository. Keep those run directories outside the public source tree because they contain historical answers, timing, diagnostic output, and evaluator evidence that can contaminate future tests. Keep private evaluation material outside the repository entirely.

Use the benchmark READMEs as the sole start prompts:

- [`benchmarks/idea-routing/README.md`](../benchmarks/idea-routing/README.md)
- [`benchmarks/collection/README.md`](../benchmarks/collection/README.md)
