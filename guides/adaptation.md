# Adapting Econ-Data-Foundry to Another Country, Market, or Research Domain

This repository is not merely a list of Chinese datasets. It is an AI-maintained research-data decision system: given a research idea, an agent should identify the most suitable dataset, explain why it is preferable to nearby alternatives, state what it covers and cannot support, and give an executable acquisition route using only the knowledge recorded in the repository.

A successful adaptation preserves that product behavior while changing the collection scope. After adaptation, a new Claude Code, Codex, or similar agent with no prior context should understand the new scope from the repository itself, continue collecting high-quality knowledge from a simple instruction, and remain aligned during long unattended runs.

Do not begin with a global search-and-replace of "China." Geography, research domain, source ecosystem, identifiers, access law, and empirical practice interact. The goal is to separate the reusable engine from its current China-specific profile, then rebuild the profile and accumulated knowledge deliberately.

## The Shortest Way to Use This Guide

A user may provide only one sentence:

```text
Read guides/adaptation.md and adapt this project for [the data scope I need].
Preserve the core idea-to-dataset-to-acquisition mission and the long-running quality controls.
Infer reasonable defaults, state the few assumptions that materially affect the design, and implement the adaptation in small verified steps.
```

Examples of a target description include:

- United States household, labor, health, and administrative data.
- United Kingdom economic and social research data, including secure-access data.
- Global financial markets, firms, securities, and regulatory filings.
- Environmental economics data on pollution, weather, climate, land use, and remote sensing.
- Urban economics data on transport networks, mobility, parcels, housing, geography, and satellite-derived measures.
- A multi-country development database with harmonized surveys and administrative indicators.

The description is not a form that the user must complete. The adapting agent should infer ordinary defaults and ask only when an unresolved choice would materially change the architecture, such as whether to replace the China catalog or expand it into a multi-region catalog.

## The One Invariant

The following outcome remains the sole measure of success:

> From the recorded knowledge alone, an agent can route a concrete research idea to the most suitable empirical dataset and explain where and how to obtain it, under what conditions, with what coverage, joins, identification-relevant variation, and limitations.

Dataset counts, journal counts, geographic breadth, polished documentation, and schema completeness are useful only when they improve that outcome. A smaller catalog with decision-sufficient records is more valuable than a large catalog of vague names and homepage links.

The adaptation must also preserve the second-order objective: a newly started agent should be able to continue maintaining the target catalog without relying on memories from a previous session. The repository, canonical records, ledgers, validation, and benchmarks must carry the intent across context resets.

## Think in Three Layers

Classify every part of the current project before changing it. This prevents useful infrastructure from being discarded and China-specific assumptions from surviving invisibly.

| Layer | Meaning | Typical treatment |
|---|---|---|
| Invariant core | The decision objective, evidence discipline, dataset identity, lifecycle states, executable access routes, provenance, queue safety, generated views, and blind evaluation principles | Preserve behavior; generalize wording only where needed |
| Collection profile | Geography, domains, populations, empirical units, time focus, source languages, journal mix, provider ecosystem, access constraints, identifiers, and exclusions | Replace or extend according to the user's target |
| Accumulated knowledge | Dataset records, aliases, candidates, completed tasks, failures, seed sources, examples, benchmarks, and generated catalogs | Rebuild, archive, or retain based on the chosen adaptation mode; never merely rename |

This separation is the conceptual center of the migration. If a rule is truly universal, keep it in the operating system. If it describes what to collect, put it in the collection profile. If it is evidence about a particular dataset or paper, keep it in canonical content or a ledger.

## Choose the Adaptation Mode First

The user does not need to know these names, but the agent should determine which mode best matches the request.

### Replacement fork

Use this when the user wants, for example, a United States data knowledge base instead of a China knowledge base. Existing China records should not remain active simply because deleting them feels wasteful. Preserve them in version history or an explicit archive, then rebuild active records, seeds, aliases, benchmarks, and ledgers for the new scope.

This is usually the safest default when the user says "change this project to collect X data" without asking for a multi-region catalog.

### Multi-scope expansion

Use this when the user wants China plus other countries or several research domains in one router. Existing content may remain, but records need explicit scope facets and the router must be able to filter by geography, domain, population, access regime, and data family. A multi-scope catalog should not make the user read every region's records before reaching a shortlist.

### Thematic specialization

Use this when geography is broad but the empirical domain is narrow, such as global financial data or environmental remote sensing. Keep generic infrastructure, then add domain-specific metadata only where it changes dataset choice or acquisition. Avoid turning every optional domain field into a universal requirement.

### Reusable empty template

Use this when the objective is to publish a framework that others will populate themselves. Keep a few clearly labeled example records and tests, but do not leave old production content in the active catalog where an agent could mistake it for the new target.

## Create a Compact Collection Profile

During an actual adaptation, consider creating a concise `COLLECTION_PROFILE.md` or similarly obvious source-of-truth document. It should be short enough to read at every cold start and specific enough to prevent scope drift.

It will usually describe:

- The research users and ideas the catalog should serve.
- Geographic coverage: countries, regions, subnational levels, or global scope.
- Thematic domains and populations that are in scope, adjacent, or explicitly out of scope.
- Important observation units, time periods, frequencies, and spatial scales.
- Expected access regimes: open download, registration, application, secure lab, institutional subscription, paid vendor, or compute-to-data.
- Languages and local terminology that aliases and searches must recognize.
- Common identifiers and join systems.
- The literature-discovery mix and the independent data-source discovery track.
- A few representative success cases and honest knowledge-gap cases.

Do not duplicate the full profile across many prompts. Other agent-facing documents should point to the profile. A single compact source of truth is easier to maintain during long loops than several nearly identical mission statements.

If the user gives only a short target description, useful conservative defaults are:

- Treat the project as a replacement fork unless multi-region expansion is requested.
- Serve empirical academic research rather than general data journalism.
- Record both open and restricted datasets, while making access constraints explicit.
- Preserve local-language and English aliases when relevant.
- Use leading journals for discovery, but do not make journal prestige the only route into the catalog.
- Keep the current lifecycle, validation, provenance, and benchmark philosophy.

State these assumptions before implementation. Ask the user only about choices whose consequences are large and difficult to reverse.

## A Safe Adaptation Sequence

The stages below are a reasoning path, not a rigid ceremony. The agent may combine small stages when the repository is simple, but should preserve the dependency order.

### 1. Freeze and understand the baseline

Read the authoritative operating documents, schema, template, validator, queue logic, seed sources, representative records, generated views, tests, and benchmarks. Run the existing offline checks before changing scope.

Why: without a baseline, a migration can silently remove working behavior and later mistake an old defect for a new one.

Record which current capabilities already work, especially:

- Canonical record parsing and status gates.
- Research-fit comparison and access-route structure.
- Alias and compact-router generation.
- Queue recovery and provenance.
- Secret, URL, and untrusted-source protections.
- Blind benchmark separation.

### 2. Produce an assumption and impact map

Search the whole repository for geography- and domain-specific assumptions. Do not limit the search to obvious names such as "China" or a country code. Inspect provider names, identifiers, examples, source rankings, field vocabularies, access procedures, benchmark ideas, URLs, geography descriptions, and generated outputs.

Classify each finding as invariant core, collection profile, accumulated content, or generated artifact. Explain why it should be retained, generalized, replaced, archived, or regenerated.

Why: a global rename can leave deeper assumptions intact. For example, replacing `china_related` with another boolean does not solve cross-country coverage, and keeping Chinese administrative codes as generic join keys will misroute later research ideas.

### 3. Generalize the scope model conservatively

The current `china_related` field is useful for this catalog but should not become `usa_related`, `uk_related`, or a succession of country-specific booleans. Prefer a general representation that can express the target without forcing every future adaptation to change the schema again.

Depending on scope, the adapted record may need concepts such as:

- Countries or territories, preferably with stable standard codes plus a human description.
- National, subnational, cross-border, global, or non-geographic coverage.
- Population or sector universe.
- Spatial support: point, pixel, parcel, tract, county, region, network edge, station, or grid.
- Data family and product version.

Migrate compatibly when possible: introduce general fields, update parsers and exports, migrate canonical records, run tests, and remove an obsolete compatibility field only after nothing depends on it. Do not perform a hard schema cut merely for elegance.

Keep the decision-bearing structures unless the target proves they are insufficient:

- Dataset identity and aliases.
- Observation unit, structure, geography, time span, frequency, and sample universe.
- Key variables and real identification-relevant variation.
- `research_fit`: best uses, comparisons, exclusions, required joins, and available variation.
- Structured access routes, requirements, steps, deliverables, costs, and verification dates.
- Join targets, keys, methods, access compatibility, and evidence status.
- Provenance, paper use, quality status, and caveats.

### 4. Add domain modules only when they change decisions

Different empirical domains fail in different ways. Add optional fields or structured notes where they prevent a wrong recommendation; do not design one enormous schema in advance.

| Target domain | Decision-critical concepts to consider |
|---|---|
| Household or survey data | Sample frame, weights, strata, panel attrition, respondent linkage, restricted geocodes, questionnaire modules, redesign breaks |
| Administrative microdata | Legal basis, population universe, event versus stock records, secure access, approval process, linkage identifiers, disclosure controls |
| Financial and firm data | Point-in-time versus restated values, survivorship and look-ahead bias, security/company identifiers, corporate actions, market calendar, vendor modules, historical constituents, license limits |
| Environmental and remote-sensing data | Physical variable and units, sensor/product/version, retrieval algorithm, spatial and temporal resolution, coordinate system, tiles, cloud or missingness, calibration, validation, download/API mechanics |
| Urban, transport, and mobility data | Network versus trip versus origin-destination unit, topology, modes, schedules, real-time versus historical data, boundary versions, map matching, routing assumptions, privacy |
| Geospatial and parcel data | Geometry type, coordinate reference system, positional accuracy, boundary vintage, geocoding quality, spatial joins, licensing of base maps |
| Cross-country harmonized data | Country coverage by wave, harmonization method, classification versions, currency and price basis, purchasing-power adjustment, comparability breaks, revisions and vintages |

These are examples of questions to ask, not a mandatory field checklist. If a concept does not affect selection, acquisition, linkage, or interpretation in the target catalog, it may remain a concise caveat rather than a new schema field.

### 5. Rebuild the discovery strategy

Use two complementary discovery routes.

#### Literature route

A common foundation may still include leading general economics and business journals, such as the economics Top 5, FT50, UTD24, ABS 3-star and above, and other respected outlets. Adapt the field-journal layer to the user's research domain. Environmental, urban, finance, labor, health, development, trade, public, macro, and spatial research expose different datasets.

The journal set is a discovery portfolio, not a prestige quota or exhaustive whitelist. Its purpose is to reveal datasets that support serious empirical work. A paper in a preferred journal is evidence of use, not proof that the dataset is accessible, correctly identified, or best for a future idea.

#### Data-source route

Search official statistical agencies, regulators, central banks, research archives, survey programs, administrative-data centers, remote-sensing agencies, repositories, exchanges, vendors, and data infrastructures directly. This route finds important datasets that the current paper sample has not yet surfaced.

Examples might include national statistical agencies for a country-focused fork, securities regulators and exchanges for finance, environmental regulators and Earth-observation programs for environmental work, or transport authorities and mapping infrastructures for urban research. These examples should inspire source mapping, not become a fixed global checklist.

For each source family, record what it is good at discovering, its coverage gaps, authentication or subscription requirements, common failure modes, and when to stop retrying.

### 6. Rebuild canonical content rather than translate it

For a replacement fork, old records should leave the active router once the new content path is ready. Preserve useful history through version control or an explicit archive; do not keep out-of-scope records active merely to preserve record counts.

For a multi-scope expansion, retain records only with explicit scope metadata and filters. The router should shortlist locally relevant records before opening full files.

Begin with a small set of reference-quality records that exercise different cases:

- A genuinely open, directly downloadable dataset.
- A registration or application dataset.
- A secure or paid dataset with a realistic alternative route.
- A dataset that requires an important join.
- Two easily confused products that must remain separate.
- A useful candidate that is deliberately not yet `ready`.

Why: these records calibrate the template, validator, agent writing style, and benchmark before large-scale collection. They reveal schema problems much earlier than hundreds of shallow entries.

Reset or reinterpret operational history carefully. Completed China-paper tasks do not prove progress in a United States or environmental fork. Candidate, failure, and completed ledgers should describe the new collection effort, while old ledgers remain available through history or archive if needed.

### 7. Rewrite the cold-start path

Update agent-facing documents so that a new session learns the adapted purpose quickly. Usually this includes the short agent orientation, operating guide, usage guide, record template, collection profile, seed-source map, examples, and user-facing README.

Keep the first screen simple:

1. What the adapted project is for.
2. What scope it currently covers.
3. How an agent resumes work safely.
4. How a user asks an idea-routing question.

Do not compensate for weak records with an enormous startup prompt. Progressive disclosure works better: read the mission and profile, use the compact router to shortlist, then open a few canonical records and evidence files.

### 8. Rebuild evaluation without leaking answers

Old China benchmark cases are not proof that the adapted catalog works. Create new public prompts and keep expected datasets, exclusions, scoring notes, and final holdouts outside the tested workspace.

Use original research ideas rather than paper titles. Include a mix of:

- Formal, conversational, and incomplete descriptions.
- Single-dataset and multi-dataset designs.
- Open, restricted, paid, secure, and unavailable access cases.
- Similar products with different units, years, populations, or spatial scales.
- Time or geography mismatches.
- Genuine knowledge gaps where clarification or refusal is the correct action.
- Domain-specific traps such as look-ahead bias in finance or incompatible resolution and coordinate systems in spatial work.

Evaluate more than the final dataset name:

- Correct shortlist and comparison with nearby alternatives.
- Coverage, variables, population, time, geography, and frequency.
- Real treatment, outcome, variation, and identification constraints.
- Required joins, identifiers, standardization, permissions, and match loss.
- Executable access route, requirements, cost, deliverable, and fallback.
- Honest uncertainty and state calibration.
- Actual file-tool traces and time to shortlist, not a model's self-reported reading behavior.

Retain a final holdout that is never used to tune records or prompts.

### 9. Run a canary before unattended collection

Before a long `/loop`, run a modest sequence of real collection tasks and session restarts. Include successful sources, paywalls, conflicting pages, renamed products, invalid HTML, and a retryable outage.

Inspect whether the agent:

- Restarts from the collection profile, health report, and ledgers rather than prior conversational memory.
- Preserves dataset identity instead of merging products by topic.
- Uses `candidate`, `grounding`, `ready`, and `needs-review` conservatively.
- Completes, retries, releases, and reclaims queue tasks coherently.
- Improves existing records when quality debt is more important than expansion.
- Rebuilds generated views and leaves no partial files or credentials.
- Maintains or improves blind idea-routing performance over time.

Only then increase loop length or concurrency. A system that works for one polished task but drifts after fifty tasks is not a successful adaptation.

## Access Knowledge Must Remain Executable

Access regimes vary substantially across countries and domains, but the standard does not change. "Available from the official website," "use WRDS," "apply to the agency," or "download from NASA" is not enough.

An adapted record should make it possible to answer:

- Which exact product, series, module, table family, release, sample, or processing level is meant?
- What is the direct entry point?
- Is the route open, registered, application-based, secure, subscription-based, paid, or partner-only?
- What institution, account, proposal, agreement, fee, or computing environment is required?
- What steps lead from the entry page to the actual deliverable?
- What years, geography, variables, granularity, format, and identifiers are delivered through that route?
- When was the route last checked, and what evidence supports it?
- If access fails, what alternative dataset is realistic and what is lost?

Do not promise approval, institutional coverage, current pricing, or legal permission. Record conditions and verification status, then let the user make the final acquisition decision.

## Protect Dataset Identity

One canonical record should represent one identifiable data product or a carefully documented product family. Similar research use does not imply identical data.

Common adaptation errors include:

- Treating a public aggregate portal and restricted microdata as the same deliverable.
- Combining a raw provider release, a harmonized archive version, and a commercial cleaned product without distinguishing them.
- Merging sensor observations with modelled or satellite-derived estimates because they measure the same concept.
- Treating different vendor modules as one financial database.
- Combining changing survey programs across a redesign without documenting the break.
- Using a broad paper phrase such as "administrative records" as if it identified a downloadable product.

When identity remains uncertain, create a candidate or `needs-review` item. Honest incompleteness is safer than a polished but false record.

## Long-Running Alignment

Adaptation is not complete when the first records look good. The maintenance system must defend the new scope over many sessions.

Useful mechanisms include:

- A compact collection profile read at every cold start.
- Health signals that distinguish coverage growth from quality debt.
- `harvest`, `ground`, and `consolidate` modes selected from current conditions rather than fixed quotas.
- Idempotent task identities and preserved source metadata.
- Bounded retry, explicit blocked states, stale-claim recovery, and provider-level backoff.
- Periodic checks for out-of-scope records and unexplained profile drift.
- A compact router that scales without requiring every full record to enter context.
- Blind routing and record-sufficiency cases rerun after schema, prompt, or canonical-content changes.
- Human review for high-impact identity, licensing, or access claims when evidence conflicts.

Do not optimize the loop for continuous activity. Optimize it for continuous trustworthy progress.

## Changes That Usually Deserve Extra Caution

Avoid these shortcuts unless there is a specific, tested reason:

- Global replacement of country or domain names.
- Keeping a country-specific boolean as the main scope model.
- Deleting old content before a baseline and migration map exist.
- Carrying old candidates, completed tasks, benchmarks, or generated outputs into a replacement fork as if they represented new progress.
- Copying the old journal list without adding the relevant field and data-source ecosystems.
- Building one universal schema containing every possible finance, survey, spatial, and environmental field.
- Promoting records to `ready` to make the adapted catalog appear populated.
- Using publication prestige as a substitute for dataset identity or access evidence.
- Putting benchmark answers in the workspace visible to the tested agent.
- Solving weak routing by making the startup prompt longer and more repetitive.
- Expanding to hundreds of records before a few representative records and hidden ideas work end to end.

## Evidence That the Adaptation Is Complete

Treat completion as a body of evidence, not a filename checklist. A strong adaptation should be able to demonstrate that:

- A new agent can explain the target scope and mission after reading the cold-start documents.
- No active schema, prompt, example, seed, alias, test, or generated view silently assumes the old scope.
- Representative target records support a full idea-to-acquisition answer without outside research.
- Nearby datasets can be compared using actual units, populations, time, geography, variables, and access conditions.
- The router exposes knowledge gaps instead of forcing an answer.
- Public prompts do not contain gold, and hidden cases include novel target-domain ideas.
- Existing commands and generated interfaces still work, or any deliberate interface migration is documented and tested.
- Secret, URL, untrusted-source, queue, and atomic-write protections remain active.
- A multi-session canary adds and improves knowledge without status inflation, duplicate tasks, or quality decline.

An adapted project does not need to be large on day one. It does need to be self-consistent, demonstrably useful for its target ideas, and safe to grow.

## Suggested Agent Handoff

At the end of an adaptation, leave a concise report that another agent can use without the adaptation conversation. It should state:

- The user's target scope and the assumptions made.
- The adaptation mode and why it was chosen.
- Which elements were preserved, generalized, archived, reset, or regenerated.
- Schema and compatibility decisions.
- The new literature and data-source discovery strategy.
- Representative records and benchmark slices created.
- Baseline versus post-adaptation validation and routing results.
- Remaining content, evidence, access, and model-validation gaps.
- The safest next collection tasks and the conditions for starting a long loop.

The best handoff is not the longest report. It is the one that lets the next agent continue correctly without needing the previous agent's memory.

## Final Reminder for the Adapting Agent

The reusable asset in this repository is not its current list of Chinese datasets. It is the discipline of turning fragmented evidence into decision-sufficient, provenance-aware, acquisition-ready knowledge that survives autonomous maintenance.

Change the scope boldly when the user asks. Preserve that discipline carefully.
