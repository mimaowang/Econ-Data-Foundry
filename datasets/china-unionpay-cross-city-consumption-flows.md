---
schema_version: 3
catalog_status: grounding
id: china-unionpay-cross-city-consumption-flows
name: UnionPay offline cross-city consumption/tourism expenditure flows 2013-2018 (China UnionPay proprietary transaction data; Wang, Chen & Yang 2025 CWE)
aka:
- 银联线下跨城消费数据
- UnionPay offline transaction data
- 中国银联跨城旅游消费
- cross-city tourism expenditure flows
provider: China UnionPay (中国银联) - the paper's abstract states the data are "UnionPay offline transaction data"; access was a research collaboration, no public product or application channel is evidenced
china_related: true
domains:
- consumption
- tourism
- payment
- finance
- regional
- transport

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    Paper-specific extract of UnionPay offline card-transaction records for
    cross-city consumption/tourism expenditure, matched with flight route
    information 2013-2018 in China (city-level; exact fields, sample, and
    aggregation unread - Wiley full text 403 for automated clients).
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    The paper (Wang, Chen & Yang 2025, China & World Economy 33(6):214-245,
    DOI 10.1111/cwe.70003) uses UnionPay offline transaction data matched with
    flight route information 2013-2018 in a DID around new direct flights:
    cross-city tourism expenditure rises 3.2%. The provider is China UnionPay
    (中国银联), a payment-institution product obtained through research
    collaboration; no public download or application form is evidenced anywhere.
    The data section (fields, city coverage, agreement terms) remains unread
    (Wiley 403 recorded in failed_tasks). This record documents the restricted
    boundary and points to the realistic substitutes (AMAP migration indices,
    coach-flow indices) for ordinary researchers.
  barrier: >-
    Proprietary payment-institution data; access requires a research
    collaboration with China UnionPay; no public route, no release, no
    application form evidenced.

unit_of_observation: City-level cross-city consumption/tourism expenditure flows derived from UnionPay offline transactions (paper-level; exact unit unread)
structure: Paper-specific panel of city pairs / city-level expenditure flows around new direct-flight events, 2013-2018 (structure unread)
geo_granularity:
- city
geography: China (city-level; exact city sample unread)
time_span:
  start: '2013'
  end: '2018'
  last_confirmed_release: null
  coverage_note: 'Abstract states "UnionPay offline transaction data matched with flight route information from 2013 to 2018 in China"; flight-route layer and exact transaction window are unread.'
  last_checked: '2026-08-15'
frequency:
- unread (likely transaction/aggregated-period; not confirmed)
sample_size: unknown (abstract does not report counts)
key_variables:
- Cross-city tourism expenditure (abstract)
- New direct-flight events (DID treatment; flight route information)
- Exact transaction fields, city identifiers, and aggregation unread

research_fit:
  best_for:
  - Understanding what UnionPay-based cross-city consumption papers actually contain and why ordinary researchers cannot obtain the data
  - Routing researchers to the realistic public substitutes for city-pair flow research when no UnionPay collaboration exists
  choose_over:
  - Do not choose this asset over china-amap-migration-flow-indices (public daily city-dyad migration indices) or the coach-flow index layer (Zheng, Li & Lu 2025 AEP) unless a UnionPay research collaboration is already in place
  not_good_for:
  - Any research design needing actual UnionPay transaction records without an existing collaboration (no public or application route evidenced)
  - Replication or extension of the paper (no data release, no DAS read)
  - Payment-level or card-level microanalysis (the paper's own use is aggregated; the abstract does not promise card-level detail)
  needs_join_for:
  - Flight route data (the paper matches UnionPay flows with flight routes; the route-source is unread)
  - City-level controls and outcomes for any expenditure analysis
  variation_available:
  - New direct-flight timing provides the paper's DID variation (design details belong to Econ-Variation; the data record only documents the flow layer)
  topics:
  - UnionPay
  - offline consumption
  - tourism expenditure
  - city-pair flows
  - payment data
  - air transport

good_for:
- Documenting the restricted boundary of UnionPay consumption-flow data
identification: []
linkable_keys:
- City identifiers (unread; likely city name/code in the paper's extract)

joins:
- target: china-amap-migration-flow-indices
  relation: complement
  keys:
  - City pair (name normalization)
  method: AMAP daily city-dyad migration indices are the public substitute for city-pair flow research when UnionPay data are unobtainable; both need city-name normalization.
  evidence_status: plausible

access_routes:
- route: Research collaboration with China UnionPay (the route the paper used)
  access_status: by-application
  direct_url: needs-verification
  requirements:
  - Institutional relationship or formal collaboration with China UnionPay; no public application form or academic-data channel is evidenced
  steps:
  - Approach China UnionPay through institutional channels; expect strict confidentiality and aggregation requirements (paper-level detail unread).
  deliverable: Paper-specific aggregated extract (exact deliverable unread)
  cost: by-application
  last_checked: '2026-08-15'
  caveat: No public route; the abstract is the only readable data characterization (Wiley full text 403 for automated clients, recorded in failed_tasks).

access:
  url: needs-verification
  cost: by-application
  license: Proprietary; terms unread
  format: []
  api: false
  how_to_get: Research collaboration with China UnionPay only; no public route evidenced.
caveats:
- Provider identity (China UnionPay) is grounded in the paper's own abstract wording ("UnionPay offline transaction data"); the exact UnionPay product/division, fields, city coverage, and agreement terms are unread.
- Wiley full text 403 for automated clients (failed_tasks 2026-08-15); no Chinese-language version found in prior searches.
- Do not confuse with china-cross-province-bank-transfer-flows (candidate; bank transfer flows, different paper/provider frame), china-online-consumption-transactions-2017-2019 (candidate; e-commerce platform transactions), or china-high-frequency-payment-consumption (candidate; China UMS offline bankcard, different provider family).

production:
  raw_sources:
  - name: China UnionPay offline transaction records
    source_type: dataset
    role: Raw expenditure/transaction records aggregated by the paper
    access_route: Research collaboration; not public
    url: needs-verification
    coverage: 2013-2018, China (city level per abstract)
    last_checked: '2026-08-15'
  - name: Flight route information
    source_type: dataset
    role: Treatment/context layer (new direct flights)
    access_route: Source unread
    url: needs-verification
    coverage: 2013-2018
    last_checked: '2026-08-15'
  acquisition_methods:
  - vendor collaboration (paper-side)
  sample_construction: unknown (data section unread)
  pipeline_stages: []
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: City-level expenditure flows (per abstract)
    structure: Panel around direct-flight events
    geography: China, city level
    time_span: 2013-2018
    key_variables: []
    formats: []
  reproducibility:
    level: not-reproducible
    starting_point: none (proprietary)
    code_available: false
    code_url: ''
    requirements: []
    blockers:
    - Proprietary UnionPay data; no release, no public route
  compliance:
    terms_or_license: Unread; proprietary
    robots_or_rate_limits: n/a
    personal_or_sensitive_data: Card-transaction-derived aggregates; confidentiality constraints per the collaboration
    redistribution: Not permitted
    review_needed: true

quality:
  profile_status: needs-verification
  access_status: blocked
  paper_use_status: grounded
  last_audited: '2026-08-15'

used_by:
- cite: 'Wang, Chen & Yang (2025). Cross-city tourism expenditure and direct flights, China & World Economy 33(6): 214-245'
  doi: 10.1111/cwe.70003
  journal: China & World Economy
  year: 2025
  dataset_role: Main data - UnionPay offline transaction data matched with flight route information 2013-2018 (DID on new direct flights; cross-city tourism expenditure +3.2%)
  evidence_type: abstract-only
  evidence_url: https://doi.org/10.1111/cwe.70003
  data_note: >-
    Crossref abstract (read 2026-08-15): "Using UnionPay offline transaction
    data matched with flight route information from 2013 to 2018 in China",
    DID on new direct flights, cross-city tourism expenditure +3.2%. Wiley
    full text 403 for automated clients (failed_tasks); the data section,
    fields, city sample, and agreement terms are unread.

provenance:
- source: Crossref record 10.1111/cwe.70003 (abstract, read 2026-08-15; cached .grounding-b17-20260815/cache/)
  field_scope:
  - provider identity (UnionPay)
  - window (2013-2018)
  - paper use (DID on direct flights; +3.2% tourism expenditure)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Wiley full text (403 for automated clients; failed_tasks 2026-08-15)
  field_scope:
  - data section, fields, city coverage, agreement terms
  added: '2026-08-15'
  confidence: low
  verified: false
- source: OpenAlex (closed access, no locations) and Semantic Scholar (no OA PDF), checked 2026-08-15
  field_scope:
  - no OA copy / no repository copy
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: china-amap-migration-flow-indices
  relation: complement
---

## Positioning in one sentence

UnionPay offline transaction data (2013-2018) used for cross-city tourism-expenditure research by Wang, Chen & Yang (2025 CWE) is a proprietary payment-institution asset reachable only through a China UnionPay research collaboration - no public route exists, so ordinary researchers should use the public AMAP migration indices or coach-flow indices instead.

## Select rules

- Use this record to understand the restricted boundary and to route researchers away from false expectations about obtaining UnionPay transaction data.
- For obtainable city-pair flow research, choose china-amap-migration-flow-indices (public) or the coach-flow index layer instead.
- Do not confuse UnionPay data with e-commerce platform transactions (china-online-consumption-transactions-2017-2019) or China UMS bankcard data (china-high-frequency-payment-consumption) - different provider families.

## Get recipe

1. There is no public recipe: the only evidenced route is a research collaboration with China UnionPay (no application form documented).
2. For the paper's own claims, read the Crossref abstract (free); the full text (Wiley) requires a human browser or library access.
3. For research needs, prefer the public AMAP migration indices (report.amap.com/migrate/page.do) or coach-flow indices (profluming.com; see the coach-flow candidate record).

## Connections and Limitations

The flow layer is city-level (per the abstract) with a 2013-2018 window; everything else - fields, city coverage, aggregation, agreement terms - is unread because the Wiley full text blocks automated clients. The paper's DID variation (new direct flights) is design knowledge that belongs to the Econ-Variation repository; this record only documents the data product and its access boundary.
