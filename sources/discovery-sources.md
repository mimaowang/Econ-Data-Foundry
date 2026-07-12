# Discovery Sources and Expansion Strategy

> This is a discovery map, not an automatic ingestion list. Every lead must pass dataset-identity, evidence-scope, research-fit, and acquisition checks before it becomes a canonical record.

Apply two filters throughout:

1. Does the source actually use or document Chinese data, rather than merely mention China?
2. Will processing it materially improve idea-to-dataset-to-acquisition decisions?

## Literature-first discovery

### Priority starting point

Begin with high-quality empirical economics and business research where data sections, data availability statements, appendices, or replication packages can reveal reusable dataset knowledge.

- Economics Top Five: AER, QJE, JPE, Econometrica, and Review of Economic Studies.
- AEA Data and Code Repository: `https://www.openicpsr.org/openicpsr/search/aea`
- AEA journal pages: `https://www.aeaweb.org/journals`
- Other replication repositories: Harvard Dataverse, openICPSR, Zenodo, institutional repositories, and publisher supplements.

Search by exact title or DOI whenever possible. Treat each paper as one work unit, but consolidate evidence when the same DOI supports several existing records.

### Broad but selective expansion

Rotate among strong journal families instead of repeatedly mining one convenient source:

- UTD24 and FT50 journals;
- ABS three-star and four-star journals;
- field-leading economics, finance, accounting, management, marketing, operations, and information-systems journals;
- high-quality China-focused journals when their data contribution is strong and verifiable.

Journal rank is a discovery prior, not a substitute for evidence. A top-journal paper may use inaccessible proprietary data or mention China without contributing reusable Chinese dataset knowledge. A lower-ranked source may contain an unusually valuable codebook or acquisition route. Make the final decision on evidence and future routing value.

Business journals often have weaker replication requirements than AEA journals. Read data-source footnotes, appendices, tables, and provider descriptions carefully. Resolve commercial platform names to the actual module or product used.

Use SSCI/JCR lists, working papers, RePEc, or NBER as supplements rather than the default queue. Working-paper versions can provide accessible data sections, but publication and version status must remain explicit.

## Provider-first discovery

Literature shows how researchers use data; provider sources show what can actually be obtained now. Use both routes.

### Commercial and institutional platforms

- CSMAR
- Wind
- CNRDS
- RESSET
- CEIC

Do not create one record for an entire platform. Identify the database family, module, table, geography, years, identifiers, subscription scope, and export route. Institutional subscriptions differ.

### Administrative and business data

- Annual Survey of Industrial Firms and other NBS microdata products;
- China Customs trade statistics;
- CNIPA patent data;
- national, provincial, municipal, and county statistical yearbooks;
- government procurement, bidding, fiscal expenditure, local debt, business registration, penalties, judicial, tax, invoice, and social-security records.

### Household and individual surveys

- CFPS
- CHARLS
- CGSS
- CHFS
- CHNS
- CHIP
- CMDS
- population census and sample-census products

Verify the organizer, target population, sampling frame, waves, panel design, restricted geography, application process, and deliverables. Similar acronyms and harmonized editions are not automatically the same data product.

### Spatial, environmental, and emerging sources

- air and water monitoring networks;
- firm emissions and environmental enforcement;
- satellite-derived pollution, night lights, land cover, and remote sensing;
- weather and climate reanalysis;
- land, housing, transportation, and geographic networks;
- recruitment, platform work, media, text, and online-market data;
- Chinese products from international organizations and global repositories.

For spatial products, preserve resolution, coordinate system, temporal frequency, aggregation method, file format, and matching requirements. Separate monitoring networks and model products even when they measure the same pollutant.

## Discovery workflow

```text
select a high-value catalog gap
  -> search strong literature and provider channels
  -> screen false positives and duplicates
  -> read the strongest available data evidence
  -> resolve product identity and source scope
  -> verify acquisition and coverage
  -> create, update, consolidate, record a candidate, skip, or block
  -> validate and regenerate
```

Write unresolved leads to `ledgers/dataset_candidates.jsonl` with a precise reason and next action. Use `ledgers/pending_tasks.jsonl` for bounded paper or provider work that another agent can claim.

## Quality alerts

- A `query=China` search misses papers that use Chinese data without saying China in the title and includes “China shock” papers whose outcomes are elsewhere.
- Titles and abstracts are screening evidence only. Confirm data identity in a data section, DAS, appendix, replication package, or codebook.
- Search snippets and cached HTML do not prove access.
- Topic similarity does not imply shared provider, schema, observation unit, or acquisition route.
- A commercial vendor is not the same thing as a dataset product.
- A paper-specific constructed treatment may be valuable but not reusable; record its reproducibility boundary.
- Do not expand the catalog while unresolved grounding debt, parser errors, or stale generated views are accumulating.

See [`data-channels.md`](data-channels.md) for dated channel tests and [`../guides/operations.md`](../guides/operations.md) for the governing evidence and publication rules.
