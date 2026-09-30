---
schema_version: 3
catalog_status: grounding
id: nmpa-drug-approval-database
name: NMPA drug/device/cosmetics approval and registration query database (国家药品监督管理局数据查询)
aka:
- 国家药品监督管理局数据查询
- NMPA data query
- 药监局数据查询
- NMPA datasearch
provider: >-
  国家药品监督管理局 (National Medical Products Administration, NMPA),
  official data-query portal www.nmpa.gov.cn/datasearch/ (fetched 200, read
  2026-08-15).
china_related: true
domains:
- health
- regulation
- pharma
- public

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A researcher-built database assembled from the NMPA data-query interface:
    drug (药品), medical-device (医疗器械), cosmetics (化妆品) and other
    registration/approval registry records. The public NMPA service window
    separates drug, device, product-operator, cosmetics, vaccine-label and
    pharmacist query families; the particular result service must be chosen
    before collection. No bulk download or API is verified, so collection
    would be query-by-query under site rules (terms unread).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    NMPA's official data-query portal covers drug/device/cosmetics approval
    and registration registries. Its official service window, read 2026-09-28,
    supplies a usable routing map: domestic/imported drugs; domestic/imported
    medical-device registrations, filings and historical-data queries;
    device-product operator filings/licences; domestic/imported special
    cosmetics; cosmetic-new-material filings; vaccine labels; and related
    professional or inspection-service queries. Category detail pages and
    result records remain JavaScript-driven; years, counts, exact result
    fields and any bulk route are not established.
  barrier: >-
    Query-by-query collection under unread site terms; no bulk download or
    API found; record counts and fields unverified.
  last_checked: '2026-09-28'

unit_of_observation: Registration/approval record returned by the query interface (drug/device/cosmetics registry entry)
structure: queryable registry records
geo_granularity:
- manufacturer/enterprise location fields where present in a category (unverified)
geography: China (NMPA-regulated products and enterprises)
time_span:
  start: null
  end: null
  last_confirmed_release: null
  coverage_note: >-
    The official service window identifies separate current and historical medical-device
    query families, but their years, completeness and record counts are unverified.
  last_checked: '2026-09-28'
frequency:
- on-demand query (registry updated by the agency; update cadence unverified)
sample_size: null
key_variables:
- Registry records are routed into named families including domestic/imported drug queries;
  domestic/imported medical-device registration, filing and historical-data queries;
  device-product operators; domestic/imported special cosmetics; cosmetic-new-material filings;
  vaccine labels; and related professional or inspection-service registers. Exact result fields remain unverified.
- Approval/registration numbers, product names, enterprises (exact fields per category unverified)

research_fit:
  best_for:
  - Drug/device/cosmetics approval and registration record research built
    from the official query interface (e.g. approval-count or product-level
    analysis)
  - Verifying product approval status via the official registry
  choose_over:
  - Choose the NMPA portal over secondary pharma databases when official
    registry authority is required; expect collection burden (no bulk
    download).
  not_good_for:
  - Bulk or complete registry snapshots without a documented collection
    campaign (query interface only)
  - Structured export or API access (none found)
  - Market/financial data on pharma firms (use commercial platforms)
  needs_join_for:
  - Firm outcomes (asif, qichacha/china-tianyancha-firm-information)
  - Market context (china-stat-yearbook)
  variation_available:
  - Approval timing variation across products/enterprises (subject to
    collection)
  topics:
  - drug approval
  - medical devices
  - pharmaceutical regulation
  - health regulation

good_for:
- drug approval registry research
- product registration status verification
identification: []
linkable_keys:
- Product/approval number
- Enterprise name

joins:
- target: china-tianyancha-firm-information
  relation: complement
  keys:
  - enterprise name
  method: link approval records to firm characteristics via entity resolution
  evidence_status: plausible

access_routes:
- route: NMPA data-query portal
  access_status: available
  direct_url: https://www.nmpa.gov.cn/datasearch/home-index.html
  requirements: none for browsing; query interface free and public
  steps:
  - Open the NMPA datasearch portal or official service window and select the named query family that matches the intended object; do not treat all NMPA queries as one uniform registry.
  - Query the target category; the results page is JS-driven (browser needed for full category lists and record detail).
  - If building a database, run bounded queries under site rules and audit coverage (terms unread).
  deliverable: query results (registry records) - researcher-built database
  cost: free
  last_checked: '2026-09-28'
  caveat: 'no bulk download or API found; category detail pages JS-gated; terms of use unread'

access:
  url: https://www.nmpa.gov.cn/datasearch/home-index.html
  cost: free
  license: Public government query interface (site terms unread)
  format:
  - web query results (JS)
  api: false
  how_to_get: Use the free public query interface; build any research database by bounded queries.
caveats:
- Record counts, time coverage and exact fields per category remain unverified (JS-gated); the official service window establishes query-family names, not their complete contents.
- No bulk download/API verified - do not promise a complete registry snapshot.
- Terms of use unread.

production:
  raw_sources:
  - name: NMPA data-query portal (datasearch)
    source_type: webpage
    role: drug/device/cosmetics registration and approval registry queries
    access_route: free public query interface
    url: https://www.nmpa.gov.cn/datasearch/home-index.html
    coverage: Official service-window query families for drugs, medical devices (including historical, registration and filing routes), product operators, cosmetics, vaccine labels and related registers; record counts and years unverified
    last_checked: '2026-09-28'
  acquisition_methods:
  - crawl
  sample_construction: >-
    Category-level queries defined by the research design; the portal is
    JS-driven, so query execution and result capture need a browser or
    browser-automation under site rules (terms unread). Coverage auditing is
    the researcher's responsibility.
  pipeline_stages:
  - stage: collect
    inputs:
    - target categories
    method: bounded queries against the datasearch interface
    tools: []
    parameters: {}
    output: registry query results
    evidence: official datasearch portal and official NMPA service window (read 2026-09-28)
  - stage: parse
    inputs:
    - query results
    method: parse registry fields per category (fields unverified)
    tools: []
    parameters: {}
    output: registry table
    evidence: researcher-side work
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: registration/approval record
    structure: registry table
    geography: China
    time_span: unverified
    key_variables:
    - product/approval identifiers, product names, enterprises (per category)
    formats:
    - web results -> researcher-chosen format
  reproducibility:
    level: low
    starting_point: NMPA datasearch portal
    code_available: false
    code_url: null
    requirements:
    - query execution under site rules
    - coverage audit
    blockers:
    - JS-gated category details; terms unread; no bulk export
  compliance:
    terms_or_license: public government query interface (terms unread)
    robots_or_rate_limits: unknown
    personal_or_sensitive_data: none expected (registry records)
    redistribution: reuse under official rules
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://www.nmpa.gov.cn/datasearch/home-index.html (fetched 200, read 2026-08-15)
  field_scope:
  - portal identity (国家药品监督管理局数据查询)
  - four module tabs (药品/医疗器械/化妆品/其它)
  - JS-driven query shell
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.nmpa.gov.cn/datasearch/search-result.html (fetched 200, JS shell, 2026-08-15)
  field_scope:
  - search-result page exists; content JS-gated
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://www.nmpa.gov.cn/zwfwqjd/index.html (official service window, read 2026-09-28)
  field_scope:
  - public names of domestic/imported drug, medical-device, operator, cosmetics, vaccine-label and related query families
  - distinction between medical-device historical-data, registration and filing query routes
  - boundary that the service listing does not establish fields, years, completeness, export or automation permission
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: samr-food-sampling-inspection
  relation: complement
- id: china-tianyancha-firm-information
  relation: complement
---

## Positioning in one sentence

NMPA's official data-query portal is the free public interface to drug/device/cosmetics registration and approval records - verified as an identity, but JS-gated with no bulk download, so any research database is a bounded query-by-query collection product.

## Select rules

- Use it when official registry authority on product approvals is required and a collection campaign is acceptable.
- Do not promise complete snapshots or machine-readable exports - none verified.
- For firm-level enrichment, join to qichacha/tianyancha records.

## Get recipe

1. Open the datasearch portal (browser) and identify the target category.
2. Run bounded queries; save results with query metadata.
3. Audit coverage per category (records/fields unverified this round).

## Connections and Limitations

Category coverage, fields and record counts are unverified. No bulk download or API was found. Terms unread. The portal is the public query layer; the underlying registries are agency-internal.

## Decision sufficiency check

A researcher can start an NMPA registry collection at the official portal and knows the query-only boundary and the missing coverage facts - grounding is appropriate.
