---
schema_version: 3
catalog_status: ready
id: china-zero2ipo-pedata-vc-pe
name: Zero2IPO / PEDATA MAX (清科数据) China PE/VC database
aka:
- Zero2IPO
- PEDATA
- PEDATA MAX
- 清科数据
- 清科数据库
- Zero2IPO Group PE/VC database
provider: >-
  清科控股 (Zero2IPO Holdings Inc., HKEX 01945.HK) and its subsidiary 清科研究中心
  (Zero2IPO Research Center). The product page states "PEDATA MAX（现品牌名称升级为：
  清科数据）是清科控股(01945.HK)旗下的国内私募股权投资领域专业SaaS系统". The
  清科研究中心 page (zero2ipo.com.cn/service3/40/) describes 清科数据 as the
  Zero2IPO Holdings SaaS product for the private-equity investment industry,
  built on a database covering 20,000+ domestic and foreign investment
  institutions with 26 years of China VC/PE industry tracking.
china_related: true
domains:
- finance
- firm
- vc-pe
- private-equity
- government-capital

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    PEDATA MAX / 清科数据 web SaaS - the commercial multi-dimensional database of
    China's VC/PE market: investment institutions (GPs), limited partners (LPs),
    funds, investment events (deals), fundraising, and registry information
    (company name, founding date, headquarters location, registered capital),
    plus 7x24 news extraction, industrial-commercial (工商) data cross-validation,
    investment-relationship mining, and LP smart-advisory features. Per the JPE
    paper's data section, the underlying Zero2IPO database aggregates multiple
    sources (AMAC registry, NECIPS business-registration data, GP/LP-reported
    deal information) and supports GP-LP-fund matching at fund level.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider identity and access terms are grounded from official pages read
    2026-08-15: the max.pedata.cn product page, the 清科数据 User License and
    Service Agreement (updated 2025-03-19, effective 2025-04-05 - paid digital
    service, 3-day free trial, 1-year and 3-year terms, full prepayment
    non-refundable, personal non-transferable license, monitoring of frequent
    query/export operations), and the 清科研究中心 page (20,000+ institutions,
    26 years of tracking). Paper use is grounded from the published JPE full
    text (Colonnelli, Li & Liu 2024): the Zero2IPO database is the primary
    administrative data source (section III.A), government ownership is measured
    with NECIPS business-registration data via the Tianyancha API (section
    III.B), and the active-GP sample (as of December 2019, investments 2015-19)
    defines the sample (section III.C); the China Equity Investment Survey
    (Q4 2019, 688 GPs / 312 LPs) was run with Zero2IPO as research partner.
    A 2026-09-28 check of the group site confirms that 清科数据 remains a
    current affiliated application and that the research center continues to
    describe its PE/VC-focused SaaS service. The product host timed out when
    independently fetched, so this confirms brand continuity, not a successful
    current trial, login, or export. Module-level catalog, current pricing, and
    any academic-access route remain unverified; the paper's replication package
    contains CODE AND README ONLY (Harvard Dataverse, CC0) - the proprietary data
    is not included.
  barrier: >-
    Paid subscription with unpublished pricing; purchase guide is JS-gated
    (contact pedatamax@zero2ipo.com.cn / 13120273086); module catalog and
    academic-access terms not documented on public pages; the agreement
    authorizes monitoring and account bans for frequent query/export/scan
    operations (no bulk download route).

unit_of_observation: >-
  VC/PE entities: investment institution (GP), limited partner (LP), fund,
  investment event/deal; the JPE paper matches GPs and LPs using fund-level
  data (GP managing the fund and LPs that committed capital)
structure: Multi-module commercial database (entity records, deal events, fund records) delivered as a SaaS
geo_granularity:
- China national
- cross-border (20,000+ domestic and foreign institutions per provider)
- firm/institution level
geography: China's VC/PE market (private equity and venture capital), with fund/GP/LP entity-level records
time_span:
  start: '2001'
  end: ongoing
  last_confirmed_release: '2026'
  coverage_note: >-
    Zero2IPO founded 2001 (per JPE text: "leading integrated service and data
    provider in the China VCPE market since its founding in 2001"); 清科研究中心
    tracks the VC/PE industry for 26 years (provider page, 2026). The JPE paper's
    sample uses the database as of December 2019 with investments 2015-19.
  last_checked: '2026-08-15'
frequency:
- event-level (deals, fundraising)
- continuously updated (7x24 news extraction)
sample_size: >-
  Provider claims 20,000+ domestic and foreign investment institutions covered;
  JPE paper's active-GP universe flagged by Zero2IPO as of December 2019
  (surveys sent to 1,600 GPs and 790 LPs; 1,000 responses)
key_variables:
- Fund/company identity: name, founding date, headquarters location, registered capital
- GP-LP-fund relationships (fund-level matching)
- Investment events/deals and fundraising records
- Ownership structure of entities (paper measures government ownership via NECIPS business-registration data through the Tianyancha API, not PEDATA itself)
- IRRs reported by GPs to Zero2IPO (subset)
- Sector focus of GPs (coarsest categorization used in the paper)

research_fit:
  best_for:
  - Research on China's VC/PE industry: funds, GPs, LPs, investment deals, fundraising, GP-LP matching
  - Government capital in private markets (government-owned GPs/LPs, government guidance funds) - the JPE 2024 application
  - VC/PE market structure and descriptive analysis of the private-equity universe in China
  choose_over:
  - Choose this over csmar and wind when the entities are UNLISTED VC/PE funds, GPs, and LPs (private markets); csmar/wind cover listed-company finance and market data.
  - Choose this over asif (industrial firms) for financial-market-side research on investors and funds.
  - For the JPE replication: expect CODE ONLY in the Harvard Dataverse package; the data itself requires the Zero2IPO route (or the paper's research-partner agreement).
  not_good_for:
  - Listed-company financials, stock markets, or corporate governance (use csmar / wind)
  - Household or individual-level data
  - Bulk academic downloads: the agreement monitors and may ban frequent query/export/scan operations
  - Re-identifying the JPE paper's exact analysis extract: the paper's data is proprietary and not in the replication package
  needs_join_for:
  - Business-registration ownership chains: NECIPS via Tianyancha (as the JPE paper does) or china-firm-registry
  - Macro context: provincial/city statistics
  variation_available:
  - GP/LP government-ownership variation (constructed from NECIPS/Tianyancha in the JPE paper)
  - GP-LP matching links in the administrative data
  - The JPE experimental survey variation is a paper-specific instrument, not part of the product; design details belong to Econ-Variation.
  topics:
  - venture capital
  - private equity
  - limited partners
  - government capital
  - fundraising
  - GP-LP matching

good_for:
- Chinese VC/PE industry descriptive and structural research
- Government-capital studies in private markets (GPGP/LPGP matching)
- GP/LP/fund universe construction with registry fields
identification:
- >-
  The delivered database is a VC/PE entity, fund, relationship and deal
  product. In the JPE application, GP/LP government ownership is not a
  PEDATA field: the authors construct it separately from NECIPS
  registration information through Tianyancha. Keep that external
  ownership layer distinct from provider-delivered GP-LP-fund links when
  selecting fields or planning a join.
linkable_keys:
- Fund/company name
- Founding date and registered capital (registry fields)
- GP/LP identity within the database (paper-internal keys; public key mapping unverified)

joins:
- target: china-firm-registry
  relation: complement
  keys:
  - Company name
  - Unified social credit code (unverified in PEDATA)
  method: Ownership-chain measurement can be replicated via NECIPS/Tianyancha as the JPE paper did; exact PEDATA identifiers unverified.
  evidence_status: plausible
- target: csmar
  relation: complement
  keys:
  - Company name (listed companies only)
  method: For listed-firm investors or exits, join via company name; PEDATA entities are mostly unlisted, so overlap is limited.
  evidence_status: plausible

access_routes:
- route: PEDATA MAX (清科数据) web SaaS subscription
  access_status: available-with-subscription
  direct_url: https://max.pedata.cn/
  requirements:
  - Registration (phone/QR login); 3-day free trial; then paid 1-year or 3-year subscription, full prepayment, non-refundable
  - Personal, non-transferable, non-exclusive license; non-commercial use on a single device per the user agreement
  steps:
  - Apply for the free trial on max.pedata.cn or contact pedatamax@zero2ipo.com.cn / 13120273086 (客服, also WeChat work account).
  - Confirm module scope and pricing with the vendor (purchase guide 购买攻略 is behind the app UI).
  - Log in via web version and query/export within the agreement's usage limits (frequent query/export/scan operations are monitored and can lead to account bans).
  deliverable: SaaS access to the VC/PE multi-dimensional database (modules per purchased scope); export formats per product terms (not documented on public pages).
  cost: paid
  last_checked: '2026-09-28'
  caveat: Module catalog, current prices, and academic/research pricing are not on public pages; the 2025 user agreement remains the detailed terms evidence. The official group site still links to this product, but the product host timed out in an independent 2026-09-28 check, so complete the trial or purchase step only through the official route and verify the terms in-session.
- route: JPE replication package (code + readme only, no data)
  access_status: available
  direct_url: https://doi.org/10.7910/DVN/JVC1XQ
  requirements: None (CC0-1.0; Harvard Dataverse)
  steps:
  - Download the replication package; read the README which explains the data structure.
  - The data itself is NOT included (proprietary, obtained through an agreement with a private party - the deposit description).
  deliverable: 5 files (docx readme + python/R/Stata code) per DataCite; data absent.
  cost: free
  last_checked: '2026-08-15'
  caveat: Code-only replication; the analysis data must come from the Zero2IPO route or the authors' research agreement.
- route: Paper full text (green OA)
  access_status: available
  direct_url: https://knowledge.uchicago.edu/record/12784
  requirements: None
  steps:
  - Download the UChicago Knowledge deposit (main text + 2022-05-25 appendix) for the data documentation (sections III-IV).
  deliverable: Published-version full text and appendix; not the data.
  cost: free
  last_checked: '2026-08-15'
  caveat: Deposit metadata says published 2023-12-07; journal version JPE 132(1), January 2024.

access:
  url: https://max.pedata.cn/
  cost: paid
  license: 清科数据 user license (paid SaaS; personal, non-transferable; no redistribution; monitoring of bulk queries)
  format:
  - SaaS web access
  - export formats not documented publicly
  api: false
  how_to_get: Apply for the 3-day free trial on max.pedata.cn, then purchase a 1-year/3-year subscription; contact pedatamax@zero2ipo.com.cn for module scope and pricing.

caveats:
- The product page, user agreement, and 清科研究中心 page confirm provider identity and general access terms; the module catalog, prices, and any academic discount are not public.
- The JPE paper's Zero2IPO database access was a research-partner arrangement (surveys run jointly with Zero2IPO); ordinary researchers use the paid SaaS route, which is not the same access as the authors had.
- The Harvard Dataverse replication package (10.7910/DVN/JVC1XQ, CC0) contains code and README only; do NOT tell researchers the JPE data is downloadable.
- Frequent query/export/scan operations can trigger account bans per the user agreement (section 6.3.1) - bulk collection is not a sanctioned route.
- Data updates/deletions happen without notice (agreement 4.4); verify coverage at purchase time.

production:
  raw_sources:
  - name: AMAC (Asset Management Association of China) registry
    source_type: dataset
    role: Fund and manager registration inputs aggregated by Zero2IPO (per JPE section III.A)
    access_route: Aggregated by the provider; not a direct research route
    url: needs-verification
    coverage: Registered fund managers
    last_checked: '2026-08-15'
  - name: NECIPS (National Enterprise Credit Information Publicity System) business-registration data
    source_type: dataset
    role: Entity registration information; the JPE paper additionally accesses NECIPS via the Tianyancha API for ownership chains
    access_route: Via commercial APIs (Tianyancha in the paper); see china-firm-registry for the registration family
    url: needs-verification
    coverage: Legal business entities in China
    last_checked: '2026-08-15'
  - name: GP/LP-reported deal and fund information
    source_type: dataset
    role: Investment events, fundraising, IRRs (subset), cross-checked across parties
    access_route: Collected by Zero2IPO from multiple parties; not public
    url: needs-verification
    coverage: VC/PE deals and funds in China
    last_checked: '2026-08-15'
  acquisition_methods:
  - provider aggregation of registries and reported data (per JPE section III.A description)
  sample_construction: >-
    Product-level: Zero2IPO continuously aggregates registry and reported data
    (per the JPE data section). Paper-level: JPE active-GP sample = GPs flagged
    active by Zero2IPO as of December 2019 (at least one investment 2015-19,
    high data-quality confidence).
  pipeline_stages:
  - stage: collect
    inputs:
    - AMAC registry
    - NECIPS data
    - GP/LP-reported deal information
    method: Zero2IPO continuous aggregation and validation across multiple parties (per JPE section III.A)
    output: GP/LP/fund/investment database
    evidence: JPE 132(1) section III.A (paper text read in full)
  constructed_variables: []
  validation:
  - Zero2IPO cross-checks information reported by multiple parties (JPE section III.A)
  output:
    unit_of_observation: VC/PE entity and deal records
    structure: Multi-module database
    geography: China VC/PE market
    time_span: Since 2001 (Zero2IPO founding); 26 years tracking per provider
    key_variables:
    - Entity identity and registry fields
    - GP-LP-fund relationships
    - Deals and fundraising
    formats:
    - SaaS web access; export formats not documented
  reproducibility:
    level: low
    starting_point: https://max.pedata.cn/ (product) or https://doi.org/10.7910/DVN/JVC1XQ (code only)
    code_available: true
    code_url: https://doi.org/10.7910/DVN/JVC1XQ
    requirements:
    - Paid subscription for the data; code package for the analysis pipeline
    - README in the package explains the data structure
    blockers:
    - Data is proprietary; the replication package explicitly does not include it
    - Pricing and module scope not public
  compliance:
    terms_or_license: 清科数据 user agreement (2025-03-19 update); paid SaaS, non-transferable, no redistribution
    robots_or_rate_limits: Frequent query/export/scan operations monitored; account bans possible (agreement 6.3.1)
    personal_or_sensitive_data: Account and behavior data collected per privacy policy
    redistribution: Not permitted without vendor license
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Colonnelli, Emanuele; Li, Bo; Liu, Ernest (2024), Investing with the Government: A Field Experiment in China, Journal of Political Economy 132(1): 248-294'
  doi: https://doi.org/10.1086/726237
  journal: Journal of Political Economy
  year: 2024
  dataset_role: 'Main administrative data (Zero2IPO VC/PE database: GPs, LPs, funds, investments); sample definition and descriptive facts; matching-link analysis'
  evidence_type: data-section
  evidence_url: https://knowledge.uchicago.edu/record/12784
  data_note: >-
    Published full text (UChicago Knowledge deposit, read in full) sections
    III.A-III.C: the primary administrative data is "the full database created
    and maintained by our research partner Zero2IPO" (GPs/LPs/funds/investments,
    aggregating AMAC and NECIPS records; registry fields incl. company name,
    founding date, HQ, registered capital; GP-LP matching at fund level);
    government ownership measured via NECIPS business-registration data accessed
    through the Tianyancha API; main sample = GPs flagged active by Zero2IPO as
    of December 2019 (investments 2015-19). Section IV.A: the China Equity
    Investment Survey (Q4 2019, 1,600 GPs + 790 LPs invited, 1,000 responses)
    was run with Zero2IPO as research partner. The DAS (UChicago record) points
    to the Harvard Dataverse replication package 10.7910/DVN/JVC1XQ, which
    contains code and README only (data not provided).

provenance:
- source: Published JPE full text (UChicago Knowledge deposit, cached jpe_investing_gov_main.txt; appendix jpe_investing_gov_appendix.txt), sections III.A-IV.A
  field_scope:
  - Zero2IPO database as primary administrative data; collection method (AMAC, NECIPS, reported data)
  - sample definition (active GPs as of Dec 2019)
  - government-ownership measurement via NECIPS/Tianyancha
  - survey design and response rates
  - data availability statement (Harvard Dataverse JVC1XQ)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: max.pedata.cn product page (cached pedata_max.html) and 清科数据 user agreement / privacy policy (fetched 2026-08-15, cached max_agreement.html / max_privacy.html)
  field_scope:
  - provider identity (清科控股 01945.HK; PEDATA MAX renamed 清科数据)
  - paid SaaS terms (trial, 1/3-year terms, prepayment, license, monitoring)
  - contact route
  added: '2026-08-15'
  confidence: high
  verified: true
- source: zero2ipo.com.cn 清科研究中心 page (fetched 2026-08-15, cached zero2ipo_service3_40.html) and b8-cached zero2ipo.com.cn pages
  field_scope:
  - group structure and 清科数据 positioning
  - coverage claims (20,000+ institutions, 26 years tracking)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.zero2ipo.com.cn/contact.html and https://www.zero2ipo.com.cn/service3/40/ (read 2026-09-28)
  field_scope:
  - Current official group site lists 清科数据 as an affiliated application and links it to max.pedata.cn
  - Current research-center description of the PE/VC-focused SaaS product and its data-service positioning
  - Boundary: independent retrieval of the product host timed out; this source does not prove a successful trial, login, purchase, export, or current price
  added: '2026-09-28'
  confidence: high
  verified: true
- source: DataCite record 10.7910/DVN/JVC1XQ
  field_scope:
  - replication package existence, contents (code + readme only), license (CC0-1.0), formats, dates (2023-04-19, updated 2023-06-07)
  - explicit statement that the data is not provided (proprietary)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Crossref record 10.1086/726237; OpenAlex work (green OA location)
  field_scope:
  - publication identity (JPE 132(1), 2024-01)
  - green-OA full-text location (UChicago Knowledge)
  added: '2026-08-15'
  confidence: high
  verified: true
related_datasets:
- id: csmar
  relation: complement
- id: wind
  relation: complement
- id: china-firm-registry
  relation: complement
---

## Positioning in one sentence

Zero2IPO's PEDATA MAX (清科数据) is the Chinese VC/PE industry's commercial SaaS database (funds, GPs, LPs, deals; 20,000+ institutions, 26 years tracking) - obtainable only by paid subscription (3-day trial, 1/3-year terms), with the JPE 2024 paper's replication package containing code and README only because the underlying data is proprietary.

## Select rules

- Prioritize it for private-market (VC/PE) research: fund-GP-LP universes, government capital in private markets, deal and fundraising activity in China.
- Switch to csmar/wind for listed-company finance, stock markets, or corporate governance; switch to china-firm-registry for registration-record research.
- Do not promise that the JPE paper's data is downloadable: the Harvard Dataverse package (CC0) has code and README only; the data requires the Zero2IPO subscription or the authors' research agreement.

## Get recipe

1. For the data: contact pedatamax@zero2ipo.com.cn / 13120273086 or apply for the 3-day free trial at max.pedata.cn; confirm module scope and pricing with the vendor (purchase guide is inside the app).
2. Purchase the 1-year or 3-year subscription (full prepayment, non-refundable) and use within the agreement's limits - bulk query/export/scan can trigger account bans.
3. For replication of the JPE paper: download the Harvard Dataverse package (10.7910/DVN/JVC1XQ, CC0) - code + README explaining the data structure; the data is NOT included.
4. Use the UChicago Knowledge full text (free) for the data documentation (sections III-IV) before designing any analysis.

## Connections and Limitations

The database's key structure is GP-LP-fund matching at fund level, which is what the JPE paper exploits for its descriptive and matching-link analyses; government ownership is not a PEDATA field but is constructed from NECIPS business-registration data (via Tianyancha in the paper). Module catalog, prices, academic pricing, and export formats are not on public pages - the decisive remaining verification is a vendor inquiry or trial login. Bulk academic extraction is contractually risky (monitoring + bans), and the paper's exact extract is not recoverable without the authors' research-partner access.
