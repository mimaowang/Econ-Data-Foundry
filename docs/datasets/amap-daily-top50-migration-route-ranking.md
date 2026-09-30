---
schema_version: 3
catalog_status: ready
id: amap-daily-top50-migration-route-ranking
name: AMAP public daily top-50 inter-city migration-route ranking (高德迁徙前50名)
aka:
- 高德迁徙排名
- AMAP migration top-50 routes
- 高德每日迁徙意愿指数排名
provider: Gaode Maps / AMAP (高德地图, AutoNavi/Amap, Alibaba group), through its public migration-report interface.
china_related: true
domains:
- urban
- migration
- mobility
- transport
- spatial

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The browser-visible top-50 ranked inter-city migration routes for one
    selected calendar day, with the interface's displayed 迁徙意愿指数 and
    实际迁徙指数. A researcher records this bounded ranking directly from the
    public interface; it is not AMAP's unobserved complete city-dyad panel.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The rendered official AMAP migration-ranking interface accepted the
    historical date 2019-02-05 on 2026-09-28 and visibly displayed 50 ranked
    routes with two migration-index columns. This creates a practical,
    date-specific public ranking asset for manually recorded route rankings.
    It does not establish an export, API, pagination beyond the ranking,
    complete dyad universe, historical-depth guarantee, index-normalization
    formula, or provider reuse licence.
  barrier: >-
    The route is a browser display and must be recorded manually with its date
    and displayed labels. It cannot reproduce the full 365-city daily panel
    used by a related Journal of Economic Geography paper, and bulk scraping
    is not justified by this record.

unit_of_observation: One origin-destination city route in the interface's top-50 ranking for a selected calendar day.
structure: Daily ranked top-50 route cross-section, manually transcribed or otherwise visibly recorded from the provider interface.
geo_granularity:
- city-dyad
geography: China inter-city routes shown by AMAP's public ranking; the record does not establish a fixed city universe outside the displayed top 50.
time_span:
  start: '2019-02-05'
  end: ongoing interface date selection
  last_confirmed_release: Historical date 2019-02-05 rendered successfully in the public interface on 2026-09-28
  coverage_note: >-
    The checked date is one historical day and is evidence that the browser
    accepts at least that paper-window date. It is not evidence of a complete
    2019 archive, a continuous start date, or a stable historical range.
  last_checked: '2026-09-28'
frequency:
- daily
sample_size: 50 ranked routes in the visible selected-day ranking; no claim is made about routes outside that screen.
key_variables:
- Origin city and destination city as displayed
- Rank within the visible top-50 list
- 迁徙意愿指数 (migration-willingness index)
- 实际迁徙指数 (actual-migration index)
- Selected calendar date

research_fit:
  best_for:
  - A transparent, date-specific descriptive ranking of the most prominent AMAP inter-city migration routes
  - Small, manually documented exercises comparing selected high-ranked routes on an observed day
  - Verifying whether a named route appears in AMAP's visible leading migration flows on a recorded date
  choose_over:
  - Choose this over an undocumented screenshot when the research need is precisely the public top-50 daily ranking and the researcher preserves date and labels.
  - Choose china-commuting-based-metropolitan-areas for released 2017 township commuting delineations, not daily top-route rankings.
  - Choose china-city-to-city-truck-flows for freight, not human migration indices.
  - Use china-amap-migration-flow-indices only after a separate provider-supported route is established when a complete city-dyad daily panel is essential.
  not_good_for:
  - Estimating a complete migration network, all 365-city dyads, route shares, absolute trip counts, or a rank-size polycentricity statistic that needs the full distribution
  - Individual-level mobility, population-representative migration counts, or postulated index normalization
  - Automated bulk collection, redistribution, or a multi-day panel unless current provider terms and an authorised acquisition route are independently established
  needs_join_for:
  - Normalised city names or codes when comparing the ranked routes with city-level outcomes
  - A separately verified complete mobility source if the research design requires unranked routes or a network denominator
  variation_available:
  - Cross-route differences within the visible top-50 ranking on a selected day
  - Comparisons across separately recorded dates, conditional on preserving the provider view and accepting the unverified historical-depth boundary
  topics:
  - inter-city migration
  - urban mobility
  - migration rankings
  - city networks

good_for:
- Dated descriptive evidence on publicly visible leading AMAP migration routes
- Manual acquisition of a bounded top-50 city-dyad ranking
identification:
- >-
  Identify each extract by the AMAP migration URL, selected date, retrieval
  time, rank, origin/destination labels and both displayed index labels. Do
  not relabel either index as a trip count or a population share.
linkable_keys:
- Displayed origin city
- Displayed destination city
- Selected date
- Rank

joins:
- target: china-amap-migration-flow-indices
  relation: component
  keys:
  - origin city
  - destination city
  - date
  method: >-
    This ranking is a visible subset of the AMAP product family. It does not
    supply evidence that the full paper-relevant city-dyad series is available
    or that unranked routes have zero flow.
  evidence_status: verified
- target: china-commuting-based-metropolitan-areas
  relation: often-confused-with
  keys: []
  method: >-
    AMAP's ranked migration routes and Baidu-derived commuting delineations
    have different providers, units and research roles; do not merge them.
  evidence_status: plausible

access_routes:
- route: AMAP public migration ranking interface
  access_status: available
  direct_url: https://report.amap.com/migrate/index.do#/
  requirements: A normal browser; no account was required for the observed historical ranking display.
  steps:
  - Open the AMAP migration-ranking interface in a browser.
  - Select the desired day and verify that the active date is visibly shown.
  - Record the 50 displayed route rows, their rank and both displayed index columns, retaining a retrieval time and the interface labels.
  - Stop at the visible ranking boundary; contact the provider or select another asset if a full network, export or bulk route is needed.
  deliverable: Browser-visible, manually recordable selected-day top-50 migration-route ranking with two index columns.
  cost: free
  last_checked: '2026-09-28'
  caveat: The checked interface accepted 2019-02-05 and displayed 50 routes. No file export, API, complete-route pagination, historical-depth statement or reuse terms were observed.

access:
  url: https://report.amap.com/migrate/index.do#/
  cost: free
  license: Provider terms were not exposed in the checked interface; retain attribution and do not assume bulk reuse or redistribution rights.
  format:
  - browser-visible ranking table
  api: false
  how_to_get: Open the interface, select a date, and manually preserve the displayed top-50 rows and labels with retrieval metadata.
caveats:
- The ranking is limited to 50 visible routes per selected day.
- Both values are provider indices, not verified trip counts, flows shares or population estimates.
- The interface's historical availability, normalization, full route coverage and commercial/reuse terms were not established.
- The public top-50 display is distinct from the full city-dyad daily series described in Ao et al. (2025); it cannot reproduce that paper's migration input or its polycentricity construction.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: Rendered official AMAP ranking interface https://report.amap.com/migrate/index.do#/ (browser read 2026-09-28)
  field_scope:
  - public interface identity
  - historical date selection accepting 2019-02-05
  - visible top-50 ranking size
  - displayed route rows and the two index labels
  - boundary against export, full coverage, historical-depth and terms claims
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-amap-migration-flow-indices
  relation: component
- id: china-commuting-based-metropolitan-areas
  relation: often-confused-with
- id: china-city-to-city-truck-flows
  relation: complement

---

## Positioning in one sentence

This is the small but genuinely obtainable public layer of AMAP migration data: a manually recordable top-50 city-route ranking for a selected day, not a concealed substitute for a complete daily migration network.

## Select rules

- Choose it when a dated descriptive ranking of leading inter-city routes is the actual empirical object.
- Switch to a released commuting or freight product when the question needs those different units.
- Do not use it for a full city network, an all-route denominator, absolute migration volume or a paper-level polycentricity measure.

## Get recipe

1. Open the public AMAP ranking interface and choose the date.
2. Confirm the date and index labels visible on the page.
3. Preserve all 50 displayed rows with their rank, city names, values and retrieval details.
4. Treat the result as a bounded ranking; do not infer missing routes, scrape at scale or claim a provider export.

## Connections and Limitations

City-name normalization may be needed before comparison with other city-level sources. The key limitation is selection: rank 51 and below are simply unobserved here, not zero-flow routes. The current interface demonstrates a useful descriptive layer, while the broader AMAP dyad series used in a published urban-agglomeration study remains a separate grounding question.
