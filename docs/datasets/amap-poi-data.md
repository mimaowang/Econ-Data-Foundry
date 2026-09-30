---
schema_version: 3
catalog_status: grounding
id: amap-poi-data
name: Amap (高德地图) POI data via the Web Service API (搜索POI)
aka:
- 高德POI
- Amap POI search API
- 高德地图Web服务API-搜索POI
- AMAP place data
provider: >-
  高德地图 (Amap/AutoNavi, Alibaba group), open platform lbs.amap.com.
  Verified: POI search API documentation page (搜索POI-高级 API 文档, fetched
  200, read 2026-09-28), the key-creation guide, and the open-platform
  agreement. Key registration flows through console.amap.com.
china_related: true
domains:
- spatial
- urban
- geography
- retail
- public

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A researcher-built POI dataset assembled by querying the Amap Web
    Service POI search API (keyword/periphery/administrative queries) under a
    registered developer key. The provider supplies point-level place records
    (fields such as name, category, address, location coordinates, adcode per
    the API doc); any research table is the researcher's collection product.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Amap's official POI search API returns category-typed place records with
    coordinates for keyword/periphery/administrative-area queries, accessed
    with a registered open-platform key (Web服务API). Current first-party
    documentation confirms the developer-account, application, and Web-service
    key sequence. The agreement allows an authenticated natural person using
    the basic service for personal research or study a monthly free allowance,
    with charges after that allowance; exact allowance and QPS must be checked
    in the current pricing/console pages. The agreement also imposes important
    use, copying, storage, and redistribution limits, so a researcher must
    confirm that a proposed retained POI collection fits the current licence.
  barrier: >-
    Quota-based collection under the developer key; exact allowance, QPS,
    paid plan, and the permitted persistence/reuse scope for a research
    collection are account- and current-terms questions. Point-in-time
    snapshots only (no official historical POI dump).
  last_checked: '2026-09-28'

unit_of_observation: POI (point of interest) record with coordinates, category and address
structure: point records returned per query (snapshot)
geo_granularity:
- point coordinates (location)
- adcode/administrative code fields
geography: China (national coverage per provider; exact coverage/update frequency unread)
time_span:
  start: null
  end: null
  last_confirmed_release: null
  coverage_note: >-
    No official historical POI archive verified; records are current
    snapshots at query time. Update frequency unread.
  last_checked: '2026-09-28'
frequency:
- on-demand API query
sample_size: null
key_variables:
- POI name
- POI category (类型/行业分类)
- Address
- Location (coordinates)
- Adcode (administrative division code)

research_fit:
  best_for:
  - Building city-level or national POI point layers (retail outlets, public
    facilities, firm locations) for spatial research where Amap's place
    coverage fits
  - Place-based analysis at point granularity (distance, density,
    accessibility) with documented query dates
  choose_over:
  - Choose the Amap POI API over other map POI providers based on coverage,
    quota and cost; each provider's category scheme and coverage differ.
  - For firm identity/financials use firm platforms (qichacha/
    china-tianyancha-firm-information); POI data are place records, not
    firm registries.
  not_good_for:
  - Historical POI layers (no verified archive)
  - Complete censuses of any category (query-based collection, coverage
    auditing needed)
  - Migration/flow indices (that is the separate AMAP migration product -
    see china-amap-migration-flow-indices)
  needs_join_for:
  - Firm-level outcomes (asif, china-firm-pollution) after matching POI
    names/coordinates to firm records
  - Administrative boundaries for aggregation
  variation_available:
  - Cross-sectional spatial variation across points/cities
  topics:
  - points of interest
  - place data
  - spatial analysis
  - urban geography

good_for:
- POI point layers for spatial research
- accessibility and density analysis
identification: []
linkable_keys:
- POI coordinates
- Adcode
- POI name

joins:
- target: china-amap-migration-flow-indices
  relation: often-confused-with
  keys: []
  method: both are Amap products but different assets - POI search API (place records) vs the public migration report page (city-dyad flow indices); keep separate
  evidence_status: plausible
- target: china-tianyancha-firm-information
  relation: complement
  keys:
  - firm name/address
  method: POI place records can geolocate firm addresses; entity resolution needed
  evidence_status: plausible

access_routes:
- route: Amap Web Service API (搜索POI)
  access_status: available-with-conditions
  direct_url: https://lbs.amap.com/api/webservice/guide/api-advanced/search
  requirements:
  - Registration as an Amap open-platform developer (console.amap.com)
  - Web服务API key (Key)
  - Free-tier quota; paid upgrades for higher volumes (numbers unread)
  steps:
  - Register and create a Web服务API key per the official doc (创建应用和 Key page).
  - Issue keyword/periphery/administrative POI search requests with the key.
  - Save responses with query parameters and dates; audit coverage per category/area.
  deliverable: POI records (name, category, address, location, adcode) for the queried areas
  cost: free
  last_checked: '2026-09-28'
  caveat: The traffic guide directs users to the current pricing page and console for allowance/QPS. The agreement creates a retained-output and redistribution boundary, so an API response is not automatically a shareable research file.

access:
  url: https://lbs.amap.com/api/webservice/guide/api-advanced/search
  cost: free
  license: >-
    Amap Open Platform Service Agreement. A natural person certified as a
    developer and using basic service for personal research/study is described
    as receiving a monthly free allowance; commercial use requires a technical
    service licence. The agreement also restricts unauthorized copying,
    modification, storage/caching, crawling, and data reuse.
  format:
  - JSON API responses
  api: true
  how_to_get: Register at console.amap.com, create a Web服务API key, query the POI search API under quota.
caveats:
- The public traffic guide directs users to the pricing page and console for
  the current basic-service allowance and QPS; this record does not state a
  numeric quota or price.
- The terms are now readable at https://lbs.amap.com/home/terms/. They make
  the registered API route real, but do not by themselves establish that a
  national retained POI corpus may be redistributed or used outside the
  personal-research/basic-service setting. Confirm the intended collection and
  output use with the current licence or provider before a large harvest.
- Point-in-time snapshots; no official historical POI archive verified.
- Category scheme and coverage auditing are the researcher's responsibility.

production:
  raw_sources:
  - name: Amap Web Service API - POI search interface
    source_type: API
    role: point-level place records via keyword/periphery/administrative queries
    access_route: registered developer key (console.amap.com), quota-based
    url: https://lbs.amap.com/api/webservice/guide/api-advanced/search
    coverage: China; current snapshots (update frequency unverified)
    last_checked: '2026-09-28'
  acquisition_methods:
  - API
  sample_construction: >-
    Query areas/categories defined by the research design (administrative
    divisions, keywords, bounding regions); POI search returns paginated
    records. Sampling is query-defined - coverage auditing per category/area
    is the researcher's responsibility. Unknown: free-tier quota numbers,
    pagination limits, paid tiers (JS-gated).
  pipeline_stages:
  - stage: collect
    inputs:
    - target category/area definitions
    method: issue POI search API requests under the developer key, page through results
    tools: []
    parameters:
      query_types: keyword / periphery / administrative
    output: raw POI JSON responses (name, category, address, location, adcode)
    evidence: official API doc (read 2026-08-15)
  - stage: validate
    inputs:
    - raw responses
    method: audit coverage per category/area against known place counts; deduplicate
    tools: []
    parameters: {}
    output: cleaned POI point layer
    evidence: researcher-side work (no provider template)
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: POI point record
    structure: point layer (snapshot)
    geography: queried Chinese areas
    time_span: query-date snapshots
    key_variables:
    - POI name, category, address, location, adcode
    formats:
    - JSON -> researcher-chosen format
  reproducibility:
    level: medium
    starting_point: official API with registered key
    code_available: false
    code_url: null
    requirements:
    - Amap developer account and Web服务API key
    - quota budget for the collection size (numbers unread)
    - query metadata logging
    blockers:
    - free-tier quotas and paid pricing unread
    - terms unread (agreement page redirect-loops for automated clients)
  compliance:
    terms_or_license: >-
      Current agreement read 2026-09-28: authenticated natural persons using
      basic service for personal research/study receive a monthly free
      allowance, while commercial use requires a technical service licence;
      copying, storage/caching, crawling and data reuse are constrained by the
      agreement. Treat any retained or shared POI corpus as requiring a
      purpose-specific licence check.
    robots_or_rate_limits: >-
      Official traffic guide points to current pricing and console quota
      management for allowance/QPS. Do not use unapproved crawling or attempt
      to evade limits.
    personal_or_sensitive_data: place records (no personal data expected)
    redistribution: Not established by the agreement alone; confirm the intended output use before sharing retained API responses.
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Zhao, Wang, Yan & Jia (2024), Trip purpose prediction using travel survey data with POI information via gradient boosting decision trees'
  doi: https://doi.org/10.1049/itr2.12450
  journal: IET Intelligent Transport Systems
  year: 2024
  dataset_role: >-
    Destination-side Amap POI features for a Chengdu household-travel-survey
    model. The paper grouped Amap POIs into 13 first-level categories, counted
    them within a 200-metre destination buffer, converted category counts to
    shares, and added total POI count as a fourteenth feature.
  evidence_type: published-paper-full-text
  evidence_url: https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/itr2.12450
  data_note: >-
    Full text read 2026-09-28. Sections 1 and 3.2 say that the authors
    collected destination POI information from Amap for a Chengdu empirical
    case, list 13 first-level categories and more than 100 second-level items,
    and describe the 200-metre buffer and 14 constructed POI features. The
    paper documents a derived feature layer, not a released Amap extract, API
    key, query history, collection date, or reusable historical POI archive.

provenance:
- source: https://lbs.amap.com/api/webservice/guide/api/search (搜索POI API doc, fetched 200, read 2026-08-15)
  field_scope:
  - API identity and query types (keyword/periphery/administrative)
  - key registration flow (console.amap.com)
  - response fields (name, category, address, location, adcode)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://lbs.amap.com/ (open-platform home, fetched 200, 2026-08-15)
  field_scope:
  - open-platform home identity
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://lbs.amap.com/home/terms/
  field_scope:
  - current developer-agreement identity
  - personal-research basic-service monthly-free-allowance condition
  - commercial-licence distinction
  - copying, storage/caching, crawling, and data-use limitations
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://lbs.amap.com/api/webservice/guide/tools/flowlevel
  field_scope:
  - current guidance that basic-service allowance is on the pricing page
  - current QPS guidance through console quota management
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/itr2.12450 (published full text, read 2026-09-28)
  field_scope:
  - Actual Amap POI use in a Chengdu household-travel-survey empirical case
  - Thirteen first-level POI categories and more than 100 second-level items
  - Destination-centred 200-metre buffer and share/count feature construction
  - 'Boundary: no released POI extract, API credentials, query history, collection date, or historical-archive evidence'
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-amap-migration-flow-indices
  relation: often-confused-with
- id: china-tianyancha-firm-information
  relation: complement
---

## Positioning in one sentence

The Amap POI search API (registered Web-service key, quota-based) is the official route to point-level place records (name/category/address/coordinates) for building a current-snapshot POI layer. It is distinct from Amap's migration-index product; the route is practical for a bounded personal-research collection, but its numeric quota and any retained/redistributed corpus use require a current licence check.

## Select rules

- Use it when the research needs Amap POI point layers (retail, facilities, place density) with documented query dates.
- Do not use it for migration flows (china-amap-migration-flow-indices), firm financials (qichacha/tianyancha), or historical POI layers.
- Check the current allowance/QPS in the pricing page and console, and check that the planned retention and use fit the agreement before planning a large collection.

## Get recipe

1. Register as a developer at console.amap.com, create an application, then create a Web-service API key.
2. Confirm the account's current allowance/QPS and that the intended retained research output fits the agreement.
3. Query the POI search API (keyword/periphery/administrative) for target categories/areas, preserve only the query metadata and responses permitted by the current terms, then audit category/area coverage.

## Connections and Limitations

POI records are current snapshots and category schemes need auditing. The agreement distinguishes personal-research basic service from licensed commercial use and constrains copying, storage/caching, crawling and reuse; the numeric allowance/QPS and the intended research-output terms must be checked before collection. Coordinates allow spatial joins to administrative boundaries and firm records after entity resolution.

## Decision sufficiency check

A researcher can start a bounded personal-research POI collection through the official API with a Web-service key, knows the returned fields and snapshot limitation, and knows to confirm current quota and permitted retention before scaling up. The remaining licence boundary makes grounding, rather than an unrestricted-ready recommendation, appropriate.
