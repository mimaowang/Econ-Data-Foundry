---
schema_version: 3
catalog_status: grounding
id: china-gov-procurement
name: China Government Procurement Data (中国政府采购网/政府采购数据)
aka:
- 政府采购数据
- 政府采购合同
- 中国政府采购数据库
- 政府采购公告
- China Government Procurement Contracts
- 政府订单数据
- 公共采购数据
provider: Ministry of Finance (财政部), published on www.ccgp.gov.cn (中国政府采购网)
china_related: true
domains:
- public
- firm
- development
- innovation
- macro
data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: Structured procurement-contract research table reconstructed from public announcements
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: Individual procurement announcements are publicly queryable on the Ministry of Finance's China Government Procurement website. A historical batch research table must be collected, parsed, normalized, and matched to firm registers. Commercial structured versions may exist through data vendors, but their fields and cleaning are a separate product.
  barrier: >-
    Historical-page availability, anti-automation controls, changing page
    structure, and non-standardized awardee names prevent assuming the
    paper-level panel can be reproduced losslessly. The public entry page is
    readable, but its linked contract-query endpoint produced a certificate-name
    mismatch in the checked browser environment on 2026-09-28; that delivery
    failure must be resolved safely before treating the live interface as a
    stable collection route.
unit_of_observation: Procurement contract / transaction (one award announcement per contract lot)
structure: transaction-records
geo_granularity:
- Procurement agency (central / provincial / city / county)
- Contract execution location
- Awardee firm location
geography: All mainland China (central government, all provinces, cities, and counties)
time_span:
  start: 2013
  end: ongoing
  last_confirmed_release: ongoing
  coverage_note: Systematic public disclosure began around 2013. Coverage quality improved significantly after 2015 regulatory reforms.
  last_checked: "2026-08-11"
frequency:
- transaction-level
- Annual (aggregable to agency-year or firm-year)
sample_size: The paper source extraction contains 2,997,105 contracts issued by all government levels in 2013-2019; the current site's cumulative and reproducibly recoverable total is not established
key_variables:
- Contract title and description
- Procuring agency name and administrative level
- Awardee (winning firm) name
- Contract value (amount in RMB)
- Contract date / award date
- Procurement method (open tender / invited tender / competitive negotiation / single-source etc.)
- Industry / goods-service category
- Contract performance period
- Province / city / county of procuring agency
research_fit:
  best_for:
  - Government demand and firm growth — how public procurement shapes firm entry, innovation, and performance
  - Political economy of government spending — which firms win contracts, at what prices, and through what procedures
  - Industrial policy through public procurement — sectoral targeting, local protectionism, and firm-level effects
  choose_over:
  - Choose procurement data for government-demand-side analysis; choose ASIF for firm production; choose china-land-transaction for land supply
  - Government procurement reveals the demand channel of public spending, distinct from subsidies/tax instruments
  not_good_for:
  - Firm production, productivity, or financial outcomes without matching to ASIF/business registry
  - Sub-2013 historical analysis (limited systematic disclosure before 2013)
  - Services or goods not procured through government contracting
  needs_join_for:
  - Firm productivity, innovation, and financial outcomes require matching to ASIF, patent, or business registry data
  - Regional economic outcomes require aggregation to city/year and joining with statistical yearbook data
  variation_available:
  - Transaction records differ by award date, procuring agency, place, awardee, amount, method and goods/service category; these are data dimensions for constructing a documented panel, not a treatment assignment or causal-design record.
topics:
- government procurement
- public spending
- industrial policy
- firm-government relationships
- innovation policy
- local protectionism
good_for:
- Impact of government procurement contracts on firm growth, innovation, and market structure
- Political connections and procurement allocation — who wins contracts and why
- Procurement as innovation policy — government as lead customer for technology firms (AI, facial recognition, etc.)
identification: []
linkable_keys:
- Awardee firm name (key matching field to ASIF / business registry / patent data)
- Procuring agency name and administrative code
- Contract date
- Industry / procurement category
joins:
- target: asif
  relation: complement
  keys:
  - Awardee firm name
  - Year
  method: entity-resolution
  evidence_status: literature-used
- target: china-patents
  relation: complement
  keys:
  - Awardee firm name
  - Year
  method: entity-resolution
  evidence_status: literature-used
access_routes:
- route: ccgp.gov.cn public announcement and contract search
  access_status: available-with-technical-friction
  direct_url: https://www.ccgp.gov.cn/htgg/main.htm
  requirements:
  - A browser that can safely reach both the current public entry page and its linked contract-query endpoint
  - Comply with website terms of use and reasonable request frequency
  steps:
  - Use the official announcement and contract-search pages to test the target province/city, agency, date range, and category before collecting a batch
  - Save contract details together with query criteria and retrieval date
  - Parse HTML announcement pages to extract structured fields
  - Clean and normalize awardee firm names for matching
  deliverable: Researcher-created structured procurement contract table from the visible notices; batch completeness and historical page availability must be verified independently
  cost: free
  last_checked: "2026-09-28"
  caveat: >-
    Public visibility of current announcements does not guarantee historical batch availability. An
    independent external retrieval of both the contract-search page and site home returned 403 on
    2026-09-28; that establishes an automated-client access boundary, not that browser access or
    public notices have disappeared. A browser check the same day could read the public entry
    page but received a certificate-name mismatch when following its query-service link. Do not
    bypass browser safety warnings. Anti-automation controls and changing page structures add
    collection friction.
- route: Commercial structured procurement databases
  access_status: needs-verification
  direct_url: https://data.csmar.com/
  requirements:
  - University or institutional subscription
  - Confirm current subscription includes government procurement module
  steps:
  - Check CSMAR/CNRDS/Wind for government procurement data modules
  - Verify coverage years, fields, and cleaning methodology
  - Export with version and license documentation
  deliverable: Vendor-processed structured procurement data; may differ from official original announcements
  cost: paid
  last_checked: "2026-09-28"
production:
  raw_sources:
  - name: China Government Procurement public announcements on ccgp.gov.cn
    source_type: webpage
    role: Official source for procurement contract identity, agency, awardee, value, method, and dates
    access_route: Public search on www.ccgp.gov.cn by region, agency, date, and procurement category
    url: https://www.ccgp.gov.cn/htgg/main.htm
    coverage: Individual announcement availability; historical batch completeness varies
    last_checked: "2026-08-11"
  acquisition_methods:
  - public web query within provider terms
  - rate-limited collection
  sample_construction: Define agency, region, date range, and procurement category filters; preserve query criteria and retrieval provenance for every batch.
  pipeline_stages:
  - stage: collect
    inputs:
    - Public search results and announcement pages
    method: Query by region, agency, date range, and procurement category; save raw announcement pages with collection provenance.
    tools:
    - browser or policy-compliant collection program
    output: Raw announcement page records with collection metadata
    evidence: ccgp.gov.cn public-search route; Beraja et al. (2023 ReStud) describe procurement data collection
  - stage: parse
    inputs:
    - Raw announcement pages
    method: Extract contract title, procuring agency, awardee name, contract value, award date, and procurement method while retaining original record reference.
    tools:
    - HTML parser
    output: Structured contract-level rows with source traceability
    evidence: Published announcement field structure
  - stage: clean
    inputs:
    - Structured contract-level rows
    method: Check duplicates, normalize awardee firm names, harmonize agency administrative codes, verify contract value units, and address missing fields.
    tools:
    - tabular data-processing software
    output: Versioned procurement research table
    evidence: Known name-normalization requirements for Chinese firm matching
  - stage: classify
    inputs:
    - Versioned procurement research table
    method: Classify contract descriptions by goods/service type, industry, and policy relevance using keyword or NLP methods.
    tools:
    - NLP or keyword classifier
    output: Procurement table with category and industry labels
    evidence: Beraja et al. (2023) use RNN/LSTM to classify software products in procurement contracts
  - stage: validate
    inputs:
    - Classified procurement research table
    method: Report coverage by year and region; audit duplicate rates; check contract value distributions; verify awardee name match rates.
    tools:
    - tabular data-processing software
    output: Coverage and quality diagnostics
    evidence: Inferred validation stage; exact diagnostics and acceptance thresholds require project-specific evidence
  constructed_variables:
  - name: Prefecture-level procurement spending
    concept: Total government procurement contract value aggregated to prefecture-year
    source_fields:
    - Contract value
    - Procuring agency location
    method: Sum contract values by prefecture and year; adjust for partial-year coverage
    validation: Cross-check against published government budget execution reports
    limitations: Excludes contracts below disclosure threshold; coverage quality varies by region and year
  validation:
  - Missing and duplicate records by year and region
  - Awardee firm name normalization quality
  - Contract value distribution checks
  output:
    unit_of_observation: Procurement contract transaction
    structure: transaction records, aggregable to firm-year or agency-year panels
    geography: Mainland China where announcements are available
    time_span: 2013–present, with stronger coverage after 2015
    key_variables:
    - contract identifier, procuring agency, awardee firm, contract value, award date, procurement method, goods/service category
    formats:
    - researcher-created tabular file
  reproducibility:
    level: low
    starting_point: ccgp.gov.cn public search and announcement pages
    code_available: false
    requirements:
    - Ability to collect and parse public web records under current provider terms
    - Firm name cleaning and normalization (critical for matching)
    - Storage and quality auditing for large historical collection
    blockers:
    - No verified public bulk API or complete historical dump
    - Historical pages and site structure may change
    - Exact paper-specific filtering and cleaning pipelines vary
  compliance:
    terms_or_license: Check current ccgp.gov.cn terms before automated collection; public announcement status does not itself grant a bulk-download or redistribution licence.
    robots_or_rate_limits: Respect robots rules, rate limits, and technical access controls.
    personal_or_sensitive_data: Review procurement descriptions for any personal or sensitive information before processing or redistribution.
    redistribution: Do not assume that a researcher-created bulk copy may be redistributed.
    review_needed: Recheck current terms, historical-page access, and permitted collection method before each new build.
access:
  url: https://www.ccgp.gov.cn/htgg/main.htm
  cost: mixed
  license: No open-data licence or blanket redistribution permission was verified; public visibility does not by itself settle automated-collection or reuse terms
  format:
  - HTML announcement pages
  - attached notice/PDF where the provider publishes one
  - researcher-created CSV/DTA (not a provider release)
  api: false
  how_to_get: Start at the official contract-announcement search, test a bounded region/year/category query, save the announcement URL and retrieval metadata, and build a researcher-owned table. No verified public bulk API or complete historical dump was found; commercial structured versions require separate subscription and field/licence verification.
caveats: >-
  The paper's 2,997,105-contract 2013-2019 extraction is evidence of what the
  authors obtained, not a promise that the same batch can now be downloaded.
  The public entry page is currently readable, but its linked query endpoint
  produced a certificate-name mismatch in the checked browser environment on
  2026-09-28; do not bypass the warning. Historical page availability before
  roughly 2015 is less reliable; awardee names are not standardized; small or
  otherwise undisclosed contracts may be missing; and procurement method labels
  may not be consistent across regions and years.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: "2026-08-11"
used_by:
- cite: 'Beraja, Yang & Yuchtman (2023), Data-intensive Innovation and the State: Evidence from AI Firms in China'
  doi: https://doi.org/10.1093/restud/rdac056
  journal: ReStud
  year: 2023
  dataset_role: Government procurement contracts matched to AI firms; surveillance camera procurement used to construct prefecture-level data-richness measure
  evidence_type: paper_data_section
  evidence_url: https://economics.mit.edu/sites/default/files/inline-files/rdac056.pdf
  data_note: Collected government procurement contracts (2013–2019) from China Government Procurement Database and matched them to 7,837 facial-recognition AI firms. Used RNN/LSTM NLP classification to categorize software products and constructed prefecture-level surveillance-camera procurement density. This record preserves the data source and construction boundary, not the paper's identification claim.
- cite: 'Author (2026), Government Procurement as a Catalyst: Reshaping Firm Entry-Exit Dynamics in China'
  doi: https://doi.org/10.1016/j.chieco.2026.102744
  journal: CER
  year: 2026
  dataset_role: Abstract-level lead concerning procurement data and enterprise-registration matching; not counted as verified paper-use evidence
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000945
  data_note: The linked provider page is an abstract landing page, not a read methods or data section. It remains a discovery lead only; it does not establish the paper's supplier match, time coverage, construction, or a reusable data route in this canonical record. Verify the full paper or its data materials before relying on it.
- cite: 'Guo & Han (2025), Budget Rollover and Year-End Spending in China: Evidence from Public Procurement Contracts'
  doi: https://doi.org/10.1016/j.chieco.2025.102522
  journal: CER
  year: 2025
  dataset_role: Abstract-level lead concerning public-procurement contracts; not counted as verified paper-use evidence
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001804
  data_note: The linked provider page is an abstract landing page, not a read methods or data section. It remains a discovery lead only; it does not establish the claimed sample, extraction method, fields, or a reusable data route in this canonical record. Verify the full paper or its data materials before relying on it.
- cite: 'Jiang, Liu & Dong (2025), Learning from Winning Firms: Government Innovation Procurement and Peer Innovation Efficiency'
  doi: https://doi.org/10.1016/j.chieco.2025.102543
  journal: CER
  year: 2025
  dataset_role: Abstract-level lead concerning innovation-procurement contracts; not counted as verified paper-use evidence
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25002019
  data_note: The linked provider page is an abstract landing page, not a read methods or data section. It remains a discovery lead only; it does not establish the paper's web collection, text classification, coverage, or a reusable data route in this canonical record. Verify the full paper or its data materials before relying on it.
- cite: 'Tang, Wang & Wu (2025), Local Favoritism in China''s Public Procurement: Information Frictions or Incentive Distortion?'
  doi: https://doi.org/10.1016/j.jue.2024.103716
  journal: JUE
  year: 2025
  dataset_role: Abstract-level lead concerning bidder-level procurement auctions; not counted as verified paper-use evidence here
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S009411902400086X
  data_note: The linked provider page is an abstract landing page, not a read methods or data section. It remains a discovery lead only; it does not establish bidder coverage, matching, outcomes, or a reusable data route in this canonical record. The separately catalogued replication record may be used only for the narrower, documented public replication artifact.
provenance:
- source: Beraja et al. (2023) ReStud paper and MIT working paper confirming procurement data use, collection methodology, and NLP pipeline
  added: "2026-07-12"
  confidence: high
  verified: true
- source: https://www.ccgp.gov.cn/htgg/main.htm confirming the Ministry of Finance's official contract-announcement search service
  added: "2026-07-12"
  confidence: high
  verified: true
- source: Independent external retrieval of https://www.ccgp.gov.cn/ and /htgg/main.htm (2026-09-28)
  field_scope:
  - both routes returned HTTP 403 to this external automated client
  - boundary only: this does not prove that a normal browser cannot use the public search or that historical notices disappeared
  added: "2026-09-28"
  confidence: high
  verified: true
- source: https://www.ccgp.gov.cn/htgg/main.htm (public contract-announcement entry page, browser-read 2026-09-28)
  field_scope:
  - the Ministry of Finance public entry page identifies itself as the government-procurement contract-announcement system
  - the page links to a separate government-procurement contract-announcement query service
  - the linked query service produced a certificate-name mismatch in the checked browser environment; this is a route boundary, not evidence that the records are unavailable to every user
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Evidence-boundary review of four ScienceDirect /abs/ landing pages in used_by (2026-09-28)
  field_scope:
  - Reclassified the four entries as abstract-only discovery leads
  - Retained Beraja et al. (2023) as the independently readable paper-data-section evidence for actual procurement-data use
  - Did not infer later papers' methods, coverage, or delivery routes from their abstract pages
  added: "2026-09-28"
  confidence: high
  verified: true
related_datasets:
- id: asif
  relation: complement
- id: china-patents
  relation: complement
- id: china-land-transaction
  relation: complement
---
## Positioning in one sentence
China's Government Procurement Database (www.ccgp.gov.cn) is the documented public starting point for procurement-contract notices from all levels of government nationwide from about 2013 onward. Researchers may be able to collect, parse, and match notices to construct firm-level panels of government demand, but the current query endpoint must first be safely reachable; a structured research table is never implied by the entry page alone.

## Select rules
- When studying how government demand or procurement contracts affect firm outcomes (innovation, growth, entry, performance)
- When the research needs a documented firm- or region-level measure of government procurement demand
- Switch to ASIF/china-customs for firm production and trade outcomes
- Not suitable for pre-2013 analysis or for studying sectors with minimal government procurement

## Get recipe
1. Query www.ccgp.gov.cn by region, agency, and date range to assess coverage for your target period and geography
2. Build or adapt a collection pipeline respecting site terms and rate limits
3. Parse HTML announcement pages to extract structured fields
4. Clean and normalize awardee firm names (critical for matching)
5. Match to target firm databases (ASIF, business registry, patent data) by name and year
6. Validate coverage completeness, duplicates, and contract value distributions
7. Commercial modules (CSMAR/CNRDS) may provide pre-processed versions — verify field coverage and cleaning methodology

## Connections and Limitations
- Awardee firm name is the primary matching key to ASIF, patent, and business registry data — expect significant name-normalization effort
- Agency administrative codes link to regional statistics (Statistical Yearbook, city-level data)
- Procurement thresholds mean small-value contracts may be systematically missing
- Pre-2015 coverage quality is weaker — the 2015 Public Procurement Law implementation significantly improved disclosure compliance
- Contract description fields require NLP or keyword classification to assign industry/policy categories
