---
schema_version: 3
catalog_status: grounding
id: china-amap-migration-flow-indices
name: Gaode Maps (AMAP) inter-city human migration flow indices (高德地图城际迁徙指数)
aka:
- 高德迁徙
- 中国主要城市迁徙意愿排行榜
- AMAP migration report
- Gaode Maps human flow dataset
- report.amap.com/migrate
provider: "Gaode Maps / AMAP (高德地图, AutoNavi/Amap, Alibaba group) - the paper's data section names 'Gaode Maps, a leading online maps provider' and its footnote 6 points to the public AMAP migration report page https://report.amap.com/migrate/page.do ('China major city migration willingness ranking')."
china_related: true
domains:
- urban
- migration
- transport
- mobility
- spatial
- resilience

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: "The full daily city-dyad AMAP migration-index series described by Ao et al. (2025): per city-dyad inflow and outflow indices built from anonymous Gaode Maps users' location-based services (LBS), covering 365 Chinese cities. The separately catalogued public top-50 ranking display is a narrower, browser-visible product and is not evidence that this full series can be downloaded."
  availability: ready-made
  ordinary_researcher_feasible: false
  summary: "Paper use is verified from full text (Ao, Li, Schwanen & Wojcik 2025 JEG 25(5):749-770, DOI 10.1093/jeg/lbaf015): a 2019 Spring Festival window of Gaode city-dyad indices supports a migration proxy and rank-size polycentricity slopes. A live browser check on 2026-09-28 confirmed that the rendered official ranking view accepts the paper-window date 2019-02-05, but it visibly exposes only a top-50 route ranking. That narrower browser asset is separately ready as amap-daily-top50-migration-route-ranking. No bulk export, complete-route pagination, historical-depth statement, or terms were observed for this paper-relevant full 365-city-dyad series. Indices are not absolute trip counts or individual data. No data-availability statement or replication package was found."
  barrier: "The public browser view supports historical date selection and shows ranked route indices, but the observable interface has not established a complete city-dyad retrieval or lawful bulk-export route. It should not be represented as a directly downloadable 365-city panel."

unit_of_observation: "City-dyad (origin city x destination city) daily flow index - the paper describes 'inflow and outflow indices for each city-dyad to reflect the intensity of inter-city human flows in a manner consistent across time and space'"
structure: "Daily repeated cross-section / time series of city-dyad indices (index values, not counts)"
geo_granularity:
- city (365 Chinese cities, ~full prefecture-level list)
geography: China, 365 cities; city-dyad pairs
time_span:
  start: null
  end: null
  last_confirmed_release: null
  coverage_note: "Product updated daily (as of 2026-08-14 page verified online); product history start year unverified. Paper's analysis window: 2019 Chinese Spring Festival (Chinese New Year to Lantern Festival, 15 days)."
  last_checked: '2026-09-28'
frequency:
- daily
sample_size: "365 cities (city-dyad flow indices); the paper aggregates the 15-day 2019 CSF window"
key_variables:
- "Inflow index and outflow index per city-dyad (intensity of inter-city human flows, comparable across time and space)"
- "2019 CSF home-bound and work-bound legs (paper's constructed window; flows highly symmetric during CSF per paper Fig. 4)"
- "Rank-size polycentricity slope per urban agglomeration (constructed from migration inflow ranks; 4 most-central cities per UA)"

research_fit:
  best_for:
  - "Assessing whether the paper-documented AMAP city-dyad series would fit an inter-city migration question, while first obtaining a provider-supported full-panel route"
  - "Replicating or extending a polycentricity design only after a complete flow distribution is independently obtained; the public top-50 ranking cannot supply it"
  - "Documenting the paper's COVID-era mobility layer and its missing acquisition route, rather than treating the visible ranking as a substitute"
  choose_over:
  - "Choose this over china-commuting-based-metropolitan-areas (Baidu Maps township commuting matrix, 2017, released Mendeley delineations) when the need is current, daily, city-pair migration indices rather than a one-off commuting delineation"
  - "Choose over china-mobile-signaling-mobility-data (operator partnerships, no public product) - AMAP is the only public daily mobility index product evidenced by these JEG papers"
  - "For freight flows use china-city-to-city-truck-flows (G7, openICPSR release); AMAP indices cover people, not freight"
  not_good_for:
  - "Absolute migration counts or trip volumes (indices only; sample = Gaode Maps LBS users, not the whole population)"
  - "Individual-level mobility analysis (fully anonymized aggregates)"
  - "Researcher-side reconstruction of the paper's exact analysis file: no DAS, no replication package found, and the paper's own processing (CSF window selection, rank-size slope construction, UA assignment) is paper-side work"
  - "Post-2021 enterprise dynamics: the resilience outcome layer (Tianyancha registrations) covers Jan 2020-Jul 2021 only"
  needs_join_for:
  - "Enterprise entries/exits for resilience outcomes: Tianyancha registration data (see china-tianyancha-firm-information; paper uses daily net registrations Jan 2020-Jul 2021 aggregated to weekly averages)"
  - "Pandemic wave definitions and control-measure timelines (paper compiles from public policy chronology; variation-side detail belongs to the variation repository)"
  - "Regional delineations (urban agglomerations per national policy list, Table A.1 of the paper) for aggregation"
  variation_available:
  - "Daily temporal variation within the CSF window and across days; cross-city and city-dyad spatial variation (365 cities)"
  - "Polycentricity slopes vary across 19 urban agglomerations (paper's sample; list in Table A.1)"
  topics:
  - human mobility
  - migration flows
  - polycentric urban development
  - economic resilience
  - COVID-19
  - urban agglomerations

good_for:
- Understanding the documented full AMAP migration-index asset and the acquisition evidence still required before a complete city-dyad design is feasible
- Paper-use and design comparison once a provider-supported full-panel route has been independently established
identification:
- Cross-city / cross-period flow differences; no causal identification is supplied by the data itself
linkable_keys:
- City names (365 prefecture-level cities; official prefecture lists vary by year per paper footnote 5)
- City-dyad pair (origin-destination)

joins:
- target: china-tianyancha-firm-information
  relation: complement
  keys:
  - city (prefecture-level name matching)
  method: "Paper-level fusion: AMAP flow indices (2019 CSF) for functional polycentricity; Tianyancha daily net registrations (Jan 2020-Jul 2021) for resilience outcomes, both aggregated to city-week/city-wave"
  evidence_status: literature-used
- target: china-commuting-based-metropolitan-areas
  relation: often-confused-with
  keys: []
  method: "Both are mobility-layer assets but different products: Baidu-Maps-derived 2017 township commuting delineations (released) vs AMAP daily city-pair migration indices (provider-run public page)"
  evidence_status: plausible

access_routes:
- route: "Boundary reference: separately ready AMAP daily top-50 ranking display"
  access_status: documentation-only
  direct_url: https://report.amap.com/migrate/index.do#/
  requirements: See amap-daily-top50-migration-route-ranking for the manually readable top-50 daily ranking route.
  steps:
  - Do not use this route to infer full dyad coverage or paper-level acquisition.
  deliverable: Documentation-only cross-reference; the distinct top-50 asset is not this record's target artifact.
  cost: free
  last_checked: '2026-09-28'
  caveat: The visible top-50 ranking is a narrowed public product. It cannot close the full 365-city daily dyad series required by this record.
- route: "AMAP public migration report page (高德迁徙) - the paper's own footnote 6 URL"
  access_status: partial
  direct_url: https://report.amap.com/migrate/page.do
  requirements:
  - Human browser (page is JavaScript-rendered; python client got the HTML shell with title '中国主要城市迁徙意愿排行榜', HTTP 200, 2026-08-14)
  requirements_note: "Historical index values, export format, and download terms were not verifiable from this environment"
  steps:
  - "Open https://report.amap.com/migrate/index.do#/ in a normal browser."
  - "Use the date selector to inspect the desired day; the rendered interface accepted 2019-02-05 on 2026-09-28."
  - "Record the displayed ranked route values only after checking which ranking scope and date are active."
  - "Before planning a full panel, establish through a provider-supported interface or written permission whether complete route coverage, historical export and reuse are available."
  deliverable: "Browser-visible ranked route indices for the selected day (top-50 display observed); complete daily city-dyad delivery remains unverified."
  cost: free
  last_checked: '2026-09-28'
  caveat: "The rendered official ranking interface accepted 2019-02-05 and showed 50 ranked routes with two index columns on 2026-09-28. This is evidence of browser-visible historical display, not of complete dyad coverage, a bulk endpoint, a file export or reuse permission. Index values are not trip counts and reflect the Gaode LBS user sample."

access:
  url: https://report.amap.com/migrate/page.do
  cost: free
  license: null
  format: []
  api: false
  how_to_get: "Human-browser access to the public AMAP migration report page; exact export route unverified"
caveats:
- "No data-availability statement in the paper; no replication package (DataCite query for the DOI, 2026-08-14, 0 hits)"
- "OpenAlex reports the article as hybrid OA (CC BY-NC-ND); the read copy used for this record is the KU Leuven Lirias green-OA PDF (handle 20.500.12942/774812, OAI GetRecord + retrieve URL verified 2026-08-14)"
- "Product history start year and index construction details (normalization base) are unverified; the paper describes the indices as 'consistent across time and space' without giving the normalization formula"

production:
  raw_sources:
  - name: "Gaode Maps LBS user location data (provider-internal)"
    source_type: dataset
    role: "Provider-side raw input; the public product is already-aggregated city-dyad indices"
    access_route: unavailable
    url: "not-public (provider-internal; only the aggregated public product at https://report.amap.com/migrate/page.do is reachable)"
    coverage: "365 Chinese cities, daily"
    last_checked: '2026-08-14'
  acquisition_methods:
  - download
  sample_construction: "Paper side: (1) 2019 Chinese Spring Festival window (Chinese New Year to Lantern Festival, 15 days) selected from the daily index series; home-bound and work-bound legs used; flows highly symmetric per paper Fig. 4; (2) polycentricity: rank-size regression (Gabaix-Ibragimov offset -1/2) of migration inflows within each urban agglomeration, 4 most-central cities per UA"
  pipeline_stages:
  - stage: collect
    inputs:
    - AMAP public index series (2019 CSF days)
    method: "Download daily city-dyad inflow/outflow indices (paper does not specify the download mechanics)"
    tools: []
    parameters:
      window: 2019-02-05..2019-02-19 (Chinese New Year + 15 days to Lantern Festival)
    output: Daily city-dyad flow indices for the 15-day window
    evidence: "Ao et al. 2025 JEG data section 3.3 and footnote 6"
  - stage: aggregate
    inputs:
    - Daily indices
    method: "Rank-size slope of migration inflow distribution per UA (4 largest cities); flow-based polycentricity measure"
    tools: []
    parameters: {}
    output: UA-level polycentricity measure per agglomeration
    evidence: "Paper section 3.4"
  constructed_variables:
  - name: functional polycentricity
    concept: "Balancedness of migration inflows across cities within an urban agglomeration"
    source_fields:
    - city-dyad inflow indices (AMAP)
    method: "Slope of rank-size regression of migration inflows (Gabaix-Ibragimov offset); flatter slope = more polycentric"
    validation: "Sensitivity to number of cities fixed at 4 (Bartosiewicz & Marcinczak 2020)"
    limitations: "Index-based, 4-city subsample per UA; sensitive to city-count choice"
  - name: economic resilience (resistance/recovery)
    concept: "Deviation of actual net enterprise registration change from expected counterfactual change"
    source_fields:
    - daily enterprise entries/exits (Tianyancha)
    method: "Aggregate daily net registrations to weekly averages; compare actual vs expected change during recession and recovery of each pandemic wave (Equations 1-2)"
    validation: "Counterfactual expected-change construction per paper section 3.4"
    limitations: "Excludes informal economy (paper cites Chen et al. 2021: informal employment 31.3-32.6% of total)"
  validation: []
  output:
    unit_of_observation: "City-wave (resilience) and UA (polycentricity) aggregates"
    structure: "UA-level panel across pandemic waves (regression sample)"
    geography: "Chinese urban agglomerations (19 UAs per paper Table A.1)"
    time_span: "2019 CSF flows; enterprise registrations Jan 2020-Jul 2021"
    key_variables:
    - polycentricity slope
    - resistance index
    - recovery index
    formats: []
  reproducibility:
    level: low
    starting_point: "AMAP public index page (historical series availability unverified) + Tianyancha (commercial/API route; see china-tianyancha-firm-information)"
    code_available: false
    code_url: null
    requirements:
    - Human browser for AMAP historical index series
    - Tianyancha access for enterprise registration series
    - Paper-side slope and resilience computations (no released code found)
    blockers:
    - No replication package; historical AMAP series download terms unverified
  compliance:
    terms_or_license: "Unverified; public report page (provider terms govern use)"
    robots_or_rate_limits: "JS-rendered page; bulk scraping terms unverified"
    personal_or_sensitive_data: "Aggregated anonymized indices only"
    redistribution: "Unverified; treat as provider-owned product"
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: "Ao, X., Li, Q., Schwanen, T. & Wojcik, D. (2025) Does polycentric regional development promote economic resilience? Empirical evidence from urban agglomerations in China. Journal of Economic Geography 25(5): 749-770"
  doi: 10.1093/jeg/lbaf015
  journal: Journal of Economic Geography
  year: 2025
  dataset_role: explanatory variable
  evidence_type: data-section
  evidence_url: https://lirias.kuleuven.be/handle/20.500.12942/774812
  data_note: "Full text read from the Lirias green-OA copy (2026-08-14): data section 3.3 names Gaode Maps human flow dataset (public, daily, 365 cities, city-dyad inflow/outflow indices; footnote 6 = report.amap.com/migrate/page.do); 2019 Spring Festival window used as migration proxy; enterprise layer = Tianyancha registrations Jan 2020-Jul 2021 (see china-tianyancha-firm-information). No DAS in the paper."

provenance:
- source: "Ao et al. 2025 JEG full text, Lirias OAI GetRecord (20.500.12942/774812, oai_dc: openAccess, CC BY-NC-ND 4.0) + retrieve PDF"
  field_scope:
  - provider identity
  - product description
  - city coverage
  - paper use
  - CSF window
  added: '2026-08-14'
  confidence: high
  verified: true
- source: "Crossref + OpenAlex metadata (10.1093/jeg/lbaf015; hybrid OA per OpenAlex; published online 2025-04-01; vol 25 issue 5 pp 749-770 per Lirias OAI)"
  field_scope:
  - publication identity
  - OA status
  added: '2026-08-14'
  confidence: high
  verified: true
- source: "Probe of https://report.amap.com/migrate/page.do (HTTP 200, HTML shell titled '中国主要城市迁徙意愿排行榜', 2026-08-14); DataCite DOI query for lbaf015 (0 hits)"
  field_scope:
  - route liveness
  - no replication package
  added: '2026-08-14'
  confidence: med
  verified: false
- source: "Recheck of https://report.amap.com/migrate/page.do and its public baseline map helper (HTTP 200, 2026-09-28)"
  field_scope:
  - current public-page liveness
  - boundary that unrendered public resources did not document historical export, bulk download or terms
  added: '2026-09-28'
  confidence: high
  verified: true
- source: "Rendered official AMAP ranking interface https://report.amap.com/migrate/index.do#/ (browser read 2026-09-28)"
  field_scope:
  - live rendered ranking interface
  - selectable historical date 2019-02-05 (the paper's Spring Festival window begins on this day)
  - visible top-50 route ranking and the two displayed index labels (迁徙意愿指数 and 实际迁徙指数)
  - boundary: no observed complete-dyad pagination, bulk export, historical-depth statement or reuse terms
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: amap-daily-top50-migration-route-ranking
  relation: successor
- id: china-tianyancha-firm-information
  relation: complement
- id: china-commuting-based-metropolitan-areas
  relation: often-confused-with
- id: china-city-to-city-truck-flows
  relation: complement
- id: china-mobile-signaling-mobility-data
  relation: complement
---

## Positioning in one sentence

The paper-documented AMAP daily city-dyad migration-index family (Gaode/AMAP LBS users, 365 cities) is verified as the travel layer of Ao et al. (2025 JEG), but its complete delivery route is not. The public interface proves only a narrower, separately catalogued top-50 ranking display; it is not a usable substitute for a full network or the paper's aggregation.

## Select rules

- Use it to assess fit or document paper use when the research need is a complete city-pair migration series over time; do not select it for implementation until a provider-supported full-panel route is established.
- Switch to china-commuting-based-metropolitan-areas for released township-level commuting delineations (2017, one-off); switch to truck-flows for freight; do not use this record for absolute migration counts, individual trips, or post-2021 enterprise outcomes.
- The enterprise registration layer of the same paper belongs to china-tianyancha-firm-information, not here.

## Get recipe

1. Open https://report.amap.com/migrate/index.do#/ in a normal browser and select the desired date. The rendered interface accepted 2019-02-05 and displayed 50 ranked routes on 2026-09-28.
2. Treat that as a route for inspecting a dated ranking, not for downloading the paper's all-city-dyad series. Confirm full coverage, export mechanics and terms with a provider-supported route before planning bulk use.
3. If a complete historical series is essential, contact the provider or choose an asset with a documented downloadable route; the paper itself does not document its download mechanics.
4. For the resilience layer, follow the Tianyancha route in china-tianyancha-firm-information.

## Connections and Limitations

- Index values are relative intensities, not trip counts; the Gaode LBS user base is a sample, so levels are not population-representative - the paper uses within-series consistency across time and space.
- No data-availability statement and no replication package (DataCite 0 hits, 2026-08-14): the paper's CSF-window selection, rank-size slope construction and UA assignment are paper-side work.
- City name matching must account for prefecture-list changes across years (paper footnote 5); join to other city-level assets by prefecture name/code with normalization.

<!--
Before publishing ready: verify the current export/download terms and historical depth of the AMAP report page in a human browser; verify the index normalization base; consider recording the 2019 CSF series availability.
-->

## Decision sufficiency check

A researcher can choose this asset to inspect public dated route rankings and understand the paper's mobility source. They must not assume that the public view supplies the paper's complete 365-city-dyad daily panel: only the top-50 ranking display, a historical date control and two index columns were directly observed. A full series needs a separate provider-supported acquisition route; grounding remains appropriate until that route, its coverage and terms are verified.
