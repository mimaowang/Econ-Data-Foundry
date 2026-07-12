# Econ-Data-Foundry

> **Econ-Data-Foundry uses AI coding agents to scan top economics journals and collect information on the datasets behind published research.**
> **So give a research idea, and you get the right dataset—and exactly how to obtain it.**

Econ-Data-Foundry is a living catalog of research datasets built from the economics literature. It starts with high-quality empirical papers—Top 5, FT50, UTD24, ABS 3/4-star, and leading field journals—and records the datasets those papers actually used: what research questions they fit, what variables and coverage they offer, how to access them, and what pitfalls to watch for. The goal is to turn scattered evidence into a single, decision-ready source.

Because every entry is anchored to a real published study, the catalog is more than a list of links. The intended way to use it is to hand the repository to an AI agent like Codex or Claude Code and ask it to do one of two things: **collect more records from the literature** for a target scope, or **match a new research idea** to the best dataset already recorded.

The current catalog focuses on Chinese economic and social data, so its records mix Chinese official names with English guidance. The same engine can be retargeted to any country, market, or economics subfield—finance, labor, development, trade, environment, urban, health—without changing its core logic.

---

## How to use it with an AI agent

This project is designed to be read and operated by an AI coding agent. The Markdown records, JSON indexes, and scripts are the agent's working material, not a manual interface for the user.

### Workflow 1: Expand the knowledge base

Tell the agent what domain or region you want to cover:

> "Read the project guides, then collect datasets used in top-journal empirical papers on **[topic/region]** and add verified records to the catalog. Run the validation gate when you are done."

The agent will:

1. Read `AGENTS.md`, `guides/operations.md`, and `datasets/template.md`.
2. Inspect `ledgers/health.json` and the task queue to see what already exists.
3. Claim one task at a time from `scripts/task_queue.py`.
4. Search the literature, resolve dataset identities, and ground coverage and access routes.
5. Write a new or updated canonical record in `datasets/`.
6. Run the release gate and regenerate `DATASET_INDEX.md`, `dist/`, `docs/`, and the quality card.

### Workflow 2: Match a research idea to data

Tell the agent your research idea in plain language:

> "I want to study **[your research idea]**. Read the data knowledge base, recommend the best dataset, explain why it fits, and tell me exactly how to obtain it."

The agent will:

1. Read `DATASET_INDEX.md` or `dist/router_index.json` for a shortlist.
2. Open the relevant canonical records in `datasets/`.
3. Compare `research_fit`, `time_span`, `linkable_keys`, `access_routes`, and `caveats`.
4. Recommend the strongest dataset, explain why close alternatives lose, and give an executable acquisition recipe.

You do not need to browse files, search tags, or read codebooks yourself. You ask; the agent reads the project for you.

---

## A 60-second example

You open Claude Code or Codex and say:

> "I want to study how health shocks affect household labor supply and consumption in China. Which dataset should I use and how do I get it?"

The agent reads `DATASET_INDEX.md`, `datasets/cfps.md`, and `datasets/charls.md`, then reports back:

- **Recommendation:** **CFPS** — a biennial household panel from 2010 onward, covering income, employment, consumption, and self-reported health.
- **Why it fits:** It tracks working-age adults and children, so it can capture how health shocks affect labor supply and household consumption across ages.
- **Alternative:** **CHARLS** if you only need people aged 45+ with deeper health and biomarker measures.
- **Coverage:** 25 provinces, 2010/2012/2014/2016/2018/2020/2022, ~15,000 households.
- **Not good for:** research before 2010, monthly shocks, or nationally representative provincial estimates.
- **How to get it:** Register at <https://cfpsdata.pku.edu.cn/#/home>, submit a research purpose, sign the data-use agreement, and download the approved waves. Free.
- **Caveat:** Fine geography and sensitive variables require a separate application.

In under a minute you have a justified choice, an acquisition recipe, and an honest list of limitations—without opening a single file yourself.

---

## Where the data comes from

Econ-Data-Foundry is not a generic data directory or a link list. It starts with the economics literature and works backward.

1. **Start with authoritative journals.** Top 5, FT50, UTD24, ABS 3/4-star, and respected field-top journals in economics and adjacent fields.
2. **Extract real dataset use.** For each paper, identify the actual datasets used, the research question, and the conditions under which they were used.
3. **Build a decision card.** Record coverage, variables, access steps, limitations, and join possibilities.

Because the entries are tied to published studies, you know the data has already been used to answer real research questions—not just that it exists.

Every canonical record answers:

- **Fit:** What research question is this dataset unusually strong for?
- **Limits:** What questions is it a poor choice for?
- **Coverage:** Geography, time span, observation unit, frequency, and sample size.
- **Joins:** Which other datasets can it link to, using what keys, with what risk?
- **Acquisition:** Direct URL, requirements, ordered steps, cost, deliverable, and caveats.

---

## Why this works for long-running agents

The project is designed so that an agent can run for many iterations without losing sight of the goal or inflating quality:

- **One invariant success criterion.** Every record must be sufficient to route a research idea to a dataset and explain how to obtain it, under what conditions, with what coverage and limitations.
- **Conservative status labels.** `ready`, `grounding`, `needs-review`, `candidate`, and `deprecated` make uncertainty explicit instead of hidden.
- **Offline validation gates.** `validate_kb.py`, `check_secrets.py`, and `check_generated_views.py` catch stale indexes, unsafe URLs, duplicate IDs, and missing fields before they enter the catalog.
- **Deterministic generated views.** `DATASET_INDEX.md`, `dist/`, `docs/`, and the quality card are rebuilt from canonical records, not hand-edited.
- **Task queue with provenance.** `scripts/task_queue.py` ensures one agent owns one task at a time, records failures and retries, and prevents duplicate work.
- **Blind benchmarks.** `benchmarks/idea-routing/` and `benchmarks/collection/` test whether the agent can actually match ideas to data and continue collecting without quality drift.

---

## Retarget to any country or field

The reusable asset is not the current list of Chinese datasets. It is the discipline of turning fragmented evidence into decision-sufficient, provenance-aware, acquisition-ready knowledge.

To collect data for another country or economics subfield:

1. Read [`guides/adaptation.md`](guides/adaptation.md).
2. Create a concise `COLLECTION_PROFILE.md` describing the new geography, domains, populations, access regimes, identifiers, and source ecosystem.
3. Choose an adaptation mode: **replacement fork**, **multi-scope expansion**, **thematic specialization**, or **reusable empty template**.
4. Generalize the scope model instead of renaming a country-specific boolean.
5. Adapt the literature discovery portfolio. The default starts from economics Top 5, FT50, UTD24, ABS 3/4-star, and respected field journals, then layers in domain-specific outlets.
6. Rebuild canonical records, aliases, benchmarks, and ledgers for the new scope.
7. Run the full offline gate and a small canary of real collection tasks before a long `/loop`.

---

## Release gate

When the agent has added or updated records, it should run the release gate to keep the knowledge base consistent and trustworthy.

Requirements: Python 3.10+ and PyYAML.

```powershell
python -m pip install -r requirements.txt
python scripts\check_secrets.py
python scripts\validate_kb.py --write-report
python scripts\build_views.py
python scripts\export_catalog.py
python scripts\build_site.py
python scripts\build_quality_card.py
python scripts\check_generated_views.py
python -m pytest
```

On macOS or Linux, replace backslashes with `/`.

A non-zero exit means the knowledge base should not be treated as ready for unattended expansion.

---

## Repository map

| Path | Role |
|---|---|
| `datasets/*.md` | Canonical dataset records with YAML frontmatter and research notes |
| `datasets/template.md` | Record template and minimum decision standard |
| `sources/` | Seed sources and discovery leads for future agents |
| `ledgers/` | Task queue, provenance, health reports, and progress |
| `scripts/` | Offline validator, view builder, queue tool, and catalog exporters |
| `schema/` | JSON Schema and controlled vocabularies |
| `benchmarks/` | Idea-routing and literature-collection benchmarks |
| `tests/` | Automated regression tests |
| `dist/` | Generated public catalog artifacts |
| `docs/` | Generated static Idea Router for GitHub Pages |
| `guides/adaptation.md` | How to retarget the engine to another country or domain |

---

## Data quality contract

The primary measure is not the number of records. It is whether one record is sufficient to answer:

> "Is this the right dataset for this idea, where do I obtain it, what conditions apply, and how far does it cover?"

Statuses are deliberately conservative:

- `ready` — sufficient for direct recommendation.
- `grounding` — useful, but an access or research-fit gap remains.
- `needs-review` — facts or routes need rechecking.
- `candidate` — a discovery lead, not a recommendation.
- `deprecated` — retained only to redirect to a successor.

---

## Automation safety

Agents should read [`guides/operations.md`](guides/operations.md) and [`guides/usage.md`](guides/usage.md) before editing. Canonical Markdown records are the source of truth; generated files must be rebuilt, not hand-edited. One agent should claim one task at a time, preserve source identity, and leave clear provenance.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), and [`SECURITY.md`](SECURITY.md). Dataset corrections are especially welcome when they improve research matching or turn a vague access statement into a concrete, verifiable route.

---

## License

The software and automation are licensed under the Apache License 2.0. Original catalog content is intended to be shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), while third-party dataset terms remain with their respective providers. See [`LICENSE`](LICENSE) and [`LICENSE-CC-BY-4.0.md`](LICENSE-CC-BY-4.0.md).

---

## Citation

See [`CITATION.cff`](CITATION.cff) for a machine-readable citation record.
