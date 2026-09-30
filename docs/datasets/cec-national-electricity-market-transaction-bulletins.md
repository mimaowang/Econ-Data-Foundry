---
schema_version: 3
catalog_status: ready
id: cec-national-electricity-market-transaction-bulletins
name: CEC national electricity-market transaction bulletins (全国电力市场交易简况)
aka:
- 全国电力市场交易简况
- CEC electricity-market transaction bulletin
- 全国电力市场交易电量
provider: China Electricity Council (CEC, 中国电力企业联合会), Planning and Development Department (中电联规划发展部).
china_related: true
domains:
- energy
- electricity
- regional
- industry
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Public CEC HTML bulletins reporting national electricity-market transaction
    volumes for a stated monthly or year-to-date reporting window, including
    national totals and separately reported intra-provincial, inter-provincial,
    State Grid-region, Southern Grid-region, Inner Mongolia and named exchange
    aggregates where the bulletin supplies them.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CEC's browser-readable information-release page lists successive 2026
    market bulletins, and the 2026 January--July bulletin is a public official
    HTML page with the release date, source department and reported figures.
    It states national cumulative and July transaction volumes, their
    year-on-year changes, and the breakdowns published for that window. A
    researcher can construct a traceable bulletin panel by transcribing each
    page while preserving its stated window and release date.
  barrier: >-
    These are aggregate published bulletins, not raw exchange transactions, a
    province-by-month panel, a bulk file, or a stable API. Cumulative windows
    must not be silently treated as single-month observations or differenced
    without recording revision and window conventions.

unit_of_observation: One official CEC bulletin for a stated observation window, containing national and selected regional aggregate electricity-market transaction volumes.
structure: Repeated official aggregate releases; each page can contain both a year-to-date cumulative window and the latest calendar-month observation.
geo_granularity:
- national
- grid-region aggregate where published
- inter-provincial aggregate
geography: China national electricity market; named grid-region aggregates are not a complete province/city panel.
time_span:
  start: '2026-01'
  end: ongoing
  last_confirmed_release: 2026-01 through 2026-07 window, released 2026-08-31
  coverage_note: >-
    The checked CEC homepage visibly listed 2026 January--March through
    January--July cumulative bulletins. The January--July page also reports
    July itself. This confirms the current 2026 release family, not a complete
    historical archive or every reporting-window convention.
  last_checked: '2026-09-28'
frequency:
- monthly releases
- year-to-date cumulative windows
sample_size: One national bulletin per published reporting window; each contains a small set of published aggregates.
key_variables:
- National electricity-market transaction volume (亿千瓦时) and year-on-year change
- Intra-provincial and inter-provincial market transaction volumes
- Long-term, spot and generation-contract-transfer transaction volumes where reported
- Green-electricity and grid-procurement subcategories where reported
- State Grid-region, Southern Grid-region and Inner Mongolia market aggregates where reported

research_fit:
  best_for:
  - National high-frequency monitoring of published electricity-market activity in China
  - Aggregate controls or descriptive series for energy, industrial and regional-development research
  - Comparing published inter-provincial transaction activity with the national market total
  choose_over:
  - Choose this record when the research object is CEC's published market-transaction aggregate, rather than general generation or electricity-consumption statistics.
  - Use cec-electricity-statistics for the broader CEC yearbook, CECI and report family; that record does not establish these bulletin values as a single data product.
  - Use china-stat-yearbook or a verified provincial source when a province/city panel is required.
  not_good_for:
  - Raw bilateral power trades, plant or firm electricity use, electricity prices, or household consumption
  - A complete province-month panel or a causal treatment assignment
  - Treating a cumulative January--July figure as the July-only value
  needs_join_for:
  - National monthly macro and energy indicators for aggregate empirical work
  - A separately verified subnational electricity series for place-level analysis
  variation_available:
  - Published time variation across reporting windows and national/selected grid-region aggregate categories
  topics:
  - electricity markets
  - power transactions
  - energy demand
  - interprovincial trade

good_for:
- Traceable reconstruction of CEC-published national electricity-market transaction aggregates
identification:
- Published aggregate market activity only; this record makes no statement about policy assignment or causal variation.
linkable_keys:
- Observation window
- Calendar month where separately reported
- Release date
- Published geographic aggregate label

joins:
- target: cec-electricity-statistics
  relation: component
  keys:
  - observation window
  method: The bulletin is one distinct public output within the broader CEC information family; retain the source page and reporting-window label rather than assuming its measures equal a yearbook series.
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - year
  method: Add annual macro or subnational context only after making the frequency conversion explicit.
  evidence_status: plausible

access_routes:
- route: CEC official electricity-market bulletin pages
  access_status: available
  direct_url: https://www.cec.org.cn/detail/index.html?3-358748
  requirements: None beyond browser/web access.
  steps:
  - Open CEC's 信息发布 / 电力市场 listing or a known bulletin page.
  - Record the bulletin title, stated observation window, source department, publication date, URL and each desired published aggregate.
  - Keep year-to-date cumulative values separate from the latest-month paragraph on the same page.
  - Retain category labels and units; flag revisions or definition changes instead of filling them by inference.
  deliverable: Official HTML observations assembled by the researcher into a documented aggregate time series.
  cost: free
  last_checked: '2026-09-28'
  caveat: The checked route proves readable 2026 pages, not a bulk download, complete archive or province-level microdata.

access:
  url: https://www.cec.org.cn/detail/index.html?3-358748
  cost: free
  license: CEC website publication terms; reuse and redistribution conditions were not separately read.
  format:
  - HTML bulletin pages
  api: false
  how_to_get: Transcribe the needed figures from each official bulletin, retaining the page URL, publication date, observation window, units and category labels.
caveats:
- National and grid-region aggregates are not city or province observations.
- Bulletins can contain both cumulative and single-month numbers; their observation windows must remain distinct.
- The record does not prove an uninterrupted historical archive, a machine-readable data release, or raw exchange-level trades.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'
used_by: []
provenance:
- source: https://www.cec.org.cn/
  field_scope:
  - official CEC information-release interface visibly lists successive 2026 electricity-market bulletins
  - titles for 2026 January--March through January--July reporting windows
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.cec.org.cn/detail/index.html?3-358748
  field_scope:
  - bulletin identity, CEC Planning and Development Department source and 2026-08-31 publication date
  - January--July national cumulative total, July total and published category/grid-region breakdowns
  - page is browser-readable public HTML rather than a metadata-only listing
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: cec-electricity-statistics
  relation: component
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is a directly readable, public CEC bulletin series for published national electricity-market transaction aggregates; it is useful for a transparent aggregate time series, but not for local electricity use or the underlying trades.

## Select rules

- Choose it for published national market-transaction volumes and the explicitly supplied grid-region aggregates.
- Choose the broader CEC record for yearbooks, CECI or reports, and a verified provincial source for local electricity analysis.
- Do not transform cumulative figures into month-only values unless the two relevant windows and any revisions have been retained.

## Get recipe

1. Open a CEC electricity-market bulletin and record its stated observation window and release date.
2. Transcribe the desired figures with their exact category labels and units.
3. Store cumulative and current-month values as different observations, with the source URL beside each.

## Connections and Limitations

The natural key is the observation window plus the published aggregate label. A later user may pair this source with macro outcomes, but neither the national total nor a grid-region subtotal identifies a province, a city, a power plant or a bilateral transaction.

## Decision sufficiency check

A future agent can choose this source for an official aggregate market-transaction series, open an actual bulletin, obtain the figures, keep the reporting windows straight, and stop before claiming local or raw-trade coverage.
