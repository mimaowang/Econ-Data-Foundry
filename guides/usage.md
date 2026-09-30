# Using Econ-DataKnowhow

Use Econ-DataKnowhow to turn a research question into a realistic data choice. Start with `AGENTS.md` and the [mental model](mental-model.md), then read only the records relevant to the question. Asking about existing knowledge requires no Python installation, task claim, model-specific setup or file changes. Collection and maintenance are separate tasks described below.

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

## Match a research idea to data

1. Translate the idea into population, unit of observation, outcomes, treatment or variation, geography, time, frequency, and access constraints. Do not force a polished idea when clarification is genuinely needed.
2. Search `dist/router_index.json` by aliases, topics, variables, coverage, and pathway summary to form a small candidate set. The router is intentionally lossy: use targeted search rather than loading it as a substitute for the catalog.
3. Open the corresponding canonical files in `datasets/`. The router is for recall; only canonical records contain the full access recipe, production pathway, evidence, join mechanics, and limitations needed for final factual claims.
4. Compare `research_fit`, coverage, observation unit, variables, variation, joins, access routes, `data_pathway`, `production`, and caveats.
5. Decide whether the user should download a ready-made product, construct an asset from public inputs, collect it from public sources, combine these routes, or reject it as inaccessible.
6. Recommend the best record, explain why close alternatives lose, identify required joins, and give an executable acquisition or reconstruction recipe.
7. Distinguish recorded facts from unresolved knowledge. For an offline answer, report gaps without filling them from external knowledge. If the user requests current online verification, identify which new source supports each update and distinguish it from the catalog's recorded verification date; answering still does not require editing the catalog.

Read status at the level of the actual deliverable. A `ready` national series does not satisfy a city-panel question; a `grounding` historical source can remain a promising but conditional alternative. Inspect `used_by` evidence separately before saying a paper used a particular file or method. Explain the result in the user's language, using plain descriptions such as “requires an application” or “historical coverage not yet confirmed” rather than relying on status labels alone.

A useful response usually covers: recommendation and alternatives; observation unit and coverage; observable variables and identification variation; required joins; direct access or public starting point; consequential production stages; requirements, steps, cost, deliverable, validation, compliance, limitations, and confidence. For constructed or collected data, keep the target research asset separate from its raw sources and never imply that raw-source access guarantees the paper's final analysis file.

Treat user capacity as part of fit. A direct release can dominate when the user needs immediate use; a constructed or collected route may dominate when it uniquely measures the mechanism and the user can support the required tools and validation. If the user has not stated those constraints, present the extra burden rather than silently assuming either unlimited engineering capacity or zero willingness to build.

Treat the routing result as a research-design decision, not a search-result list. It may be a single asset, a combination of treatment and outcome assets, a request for one consequential clarification, an explicit knowledge gap, or an inaccessible design. For each recommended component, state its role, why it wins, what would disqualify it, the necessary joins, and the obtainable deliverable. Keep a conceptually ideal but inaccessible asset visible only as a rejected alternative; never let it outrank a feasible route without saying so.

For an unpolished idea, a compact answer should normally make five decisions easy to inspect: the interpreted population/treatment/outcome/unit/time/geography; the recommended asset or asset combination; close alternatives and rejection reasons; acquisition or production steps with effort and constraints; and unresolved gaps that prevent a stronger claim. This is an output contract for reasoning, not a requirement to manufacture certainty or fill every heading.

## Maintain the knowledge base

Read [`operations.md`](operations.md) and the current collection focus in [`sources/discovery-sources.md`](../sources/discovery-sources.md) before editing. Maintenance requires Python 3.10+; install with `python -m pip install -r requirements-dev.txt`, then follow the [release gate](operations.md#release-gate). Those checks are offline. `scripts/check_links.py` is an optional network freshness diagnostic and never edits canonical records. Then:

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

# When the queue is empty, register one bounded work unit before claiming it
python scripts/task_queue.py enqueue --id <unique-task-id> --type <paper-or-source> --goal "<evidence-backed goal>" --title "<title>"

# Complete the claimed task
python scripts/task_queue.py complete --id <task-id> --result processed --dataset <dataset-id> --note "Decision improved; evidence boundary; remaining unknown" --agent claude-code

# Close a task that produced a candidate-ledger entry but no canonical record
python scripts/task_queue.py complete --id <task-id> --result candidate --note "Candidate identity, evidence gap, and next verification recorded" --agent claude-code

# Close a periodic fresh-context semantic audit (datasets were reviewed, not edited)
python scripts/task_queue.py complete --id <audit-task-id> --result audited --dataset <reviewed-dataset-id> --audit-outcome pass --note "Idea tested, alternatives compared, route and remaining gaps checked" --agent claude-code

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

Use the filename `<id>.md`, where `id` is lowercase ASCII with hyphens. Keep official Chinese names in `aka` when they are useful search keys. Canonical explanations use English; answer researchers in their requested language.

`ready` means directly recommendable from grounded knowledge. `grounding` means useful with a material unresolved gap. `needs-review` marks stale or conflicting knowledge. `candidate` is a lead, not a recommendation. `deprecated` is a redirect.

## Generated artifacts

`scripts/build_views.py` creates `DATASET_INDEX.md`, `ledgers/aliases.md`, and `ledgers/progress.md`. `scripts/export_catalog.py` creates deterministic JSON, JSONL, CSV, JSON-LD, router, join graph, and checksum artifacts in `dist/`. `scripts/build_site.py` publishes the read-only router to `docs/`. `scripts/check_generated_views.py` rebuilds these outputs in a temporary workspace and compares bytes, so stale checked-in views cannot pass silently.

## Benchmarks and private runs

The two public harnesses create isolated workspaces outside the repository. Keep those run directories outside the public source tree because they contain historical answers, timing, diagnostic output, and evaluator evidence that can contaminate future tests. Keep private evaluation material outside the repository entirely.

Use the benchmark READMEs as the sole start prompts:

- [`benchmarks/idea-routing/README.md`](../benchmarks/idea-routing/README.md)
- [`benchmarks/collection/README.md`](../benchmarks/collection/README.md)
