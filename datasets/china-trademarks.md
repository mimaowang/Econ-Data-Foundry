---
schema_version: 3
catalog_status: ready
id: china-trademarks
name: China Trademark Registration Data (CNIPA 中国商标数据)
aka:
- 商标数据
- 中国商标
- 商标注册数据
- CNIPA商标
- 国家知识产权局商标
- 中国商标注册
- 中国商标网数据
- China Trademark Database
- CNIPA trademark registration records
provider: National Intellectual Property Administration (CNIPA), Trademark Office (国家知识产权局商标局)
china_related: true
domains:
- innovation
- firm
- finance
- marketing
- brand

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The official CNIPA trademark database: registered-trademark records including
    historical data and incremental updates, downloadable through the Trademark Data
    Open (商标数据开放) section of the Trademark Online Service System by registered
    users since 2018-12-26; per-record searching is publicly available through the
    Trademark Online Search (商标网上查询). A separate, researcher-constructed asset
    is the paper-specific trademark-firm linked panel of Xiao et al. (2024 Research
    Policy), which is not publicly released.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CNIPA's official service guide states the operational route: register as a
    Trademark Data Open user, hold a trademark digital certificate, log in to China
    Trademark Network, then download the opened trademark data. The 2018 opening
    announcement states that the download covers historical data and subsequent
    incremental updates; the public online search remains the separate route for
    individual records. This makes the official raw registration data a directly
    obtainable source for researchers who meet the registration condition. The
    paper-specific trademark-firm linked panel of Xiao et al. (2024) remains a
    separate, unreleased research product.
  barrier: >-
    The data-open route has conditions rather than being an anonymous download: a
    registered data-open user and trademark digital certificate are required, and use
    must comply with applicable law. The exact file inventory, formats, update cadence,
    current redistribution terms and eligibility of a researcher without a Chinese
    identity document remain unverified; no official public API was identified. The
    Xiao et al. (2024) trademark-firm matching algorithm and full construction details
    were not visible in the publisher-indexed text available this round.

unit_of_observation: Trademark registration record (one record per trademark application/registration, linked to a registrant and goods/services classes)
structure: Event/registration records with application and legal-status dates; can be aggregated to registrant-, firm-, city- or province-level panels
geo_granularity:
- registrant address (province/city/county where recorded)
- city
- province
geography: China national — trademarks registered with CNIPA, including China registrations by foreign applicants and Madrid (international) extension records
time_span:
  start: unknown
  end: ongoing
  last_confirmed_release: '2026-09-28'
  coverage_note: >-
    The 2018-12-25 opening announcement states that historical trademark data and
    incremental data are downloadable but does not give a start year, table list, or
    update cadence. The current official service guide (checked 2026-09-28) confirms
    the user-registration, digital-certificate, login and download sequence. The
    trademark gazette search reportedly
    covers issues since 1980, but this was not verified first-hand.
  last_checked: '2026-09-28'
frequency:
- incremental updates (cadence not specified in the official announcement)
sample_size: China has held the world's highest annual trademark application volume for many years; the database covers all CNIPA-registered trademarks, but no official total count was verified this round
key_variables:
- Trademark registration/application number and current status
- Trademark text/name and design image where retained
- Application, registration and legal-status dates
- Registrant (applicant/owner) name and address (province/city/county)
- Goods/services classification (Nice classes) where retained
- Agent/representative record where retained
- Madrid international registration and priority fields where retained
- Exact table/field inventory requires the current download-system documentation (the 2018 announcement does not enumerate tables)

research_fit:
  best_for:
  - Measuring trademark activity and brand-related innovation of Chinese firms, including non-listed firms when the official database is used
  - Building trademark-firm linked panels (with CSMAR or firm-registry records) for market-value, IP-portfolio or IPR-protection studies
  - Distinguishing trademarks from patents as a distinct IP form capturing brand value, product differentiation and marketing innovation
  choose_over:
  - Choose trademark data over patent data when the question concerns brand value, product differentiation, or marketing-related innovation.
  - Choose the official CNIPA database over a commercial trademark module when the research needs full registrant-level records, non-listed firms, or firm name-based construction.
  - Choose a commercial library such as CSMAR's trademark module for listed-firm-matched convenience only when the module's product boundary is verified.
  not_good_for:
  - Questions about unregistered marks, actual market use, or sales/brand-consumer outcomes that registration records cannot measure
  - Equating trademark registration counts with patents or with realized brand value
  - A nationally representative trademark-firm match without an explicit applicant-name matching procedure
  needs_join_for:
  - Firm financials, market value and governance outcomes (CSMAR or similar) via a documented trademark-to-firm entity-resolution procedure
  - Firm registration identifiers and industry codes (china-firm-registry, ASIF) for non-listed firms
  - IPR-protection or policy context when such variables are not embedded in the trademark records
  variation_available:
  - Application/registration timing, Nice classes, and legal-status events are data dimensions only and are not recorded here as a treatment or variation database.
  topics:
  - trademarks
  - intellectual property
  - brand value
  - firm innovation
  - IPR protection
  - market value

good_for:
- Trademark-firm linked market-value and innovation research
- Trademark portfolio construction and classification by use status and business relatedness
- City/province trademark activity panels from registrant addresses
- Complementing patent data for a full IP portfolio
identification:
- Select the official raw product by its service name 商标基础数据开放 / 商标数据开放, accessed through 中国商标网, rather than by a commercial trademark module or a paper's matched analysis file.
- A usable download route produces historical and incremental official trademark basic data after data-open registration and digital-certificate login; public per-record search, aggregate statistics, and trademark-gazette pages are separate delivery products.
- The Xiao et al. linked SSE/SZSE firm-year panel is a different researcher-constructed asset: it cannot be obtained merely by downloading the official raw trademark data.
linkable_keys:
- Applicant/registrant name
- Unified social credit code where recorded
- Registrant address codes (province/city/county)
- Trademark registration/application number
- Nice class codes
- Application/registration dates

joins:
- target: china-patents
  relation: complement
  keys:
  - Applicant/registrant name
  - Unified social credit code where recorded
  method: Match by normalized applicant name and, where present, unified code to combine trademark and patent portfolios for one firm; name variations are a real matching risk.
  evidence_status: plausible
- target: csmar
  relation: complement
  keys:
  - Applicant name matched to listed-firm names
  method: Xiao et al. (2024) explicitly link CNIPA trademark-registration records to CSMAR listed-firm data; the publisher-indexed text does not expose the matching key, algorithm, or treatment of name variants.
  evidence_status: literature-used
- target: china-firm-registry
  relation: complement
  keys:
  - Applicant name
  - Unified social credit code where recorded
  method: Registry records can resolve applicant-name variants for non-listed firms; the registry itself is restricted administrative data.
  evidence_status: plausible

access_routes:
- route: Trademark Data Open bulk download (商标数据开放, Trademark Online Service System)
  access_status: available-with-conditions
  direct_url: https://sbj.cnipa.gov.cn/
  requirements:
  - Registered user of the Trademark Online Service System (商标网上服务系统)
  - CNIPA digital certificate (商标数字证书; soft or hard certificate depending on user type) and real-name verification
  - Eligibility and documents for researchers without a Chinese identity document remain unverified
  steps:
  - Register through the official trademark data-open system, providing true, accurate and complete registration information.
  - Obtain the required trademark digital certificate and log in to 中国商标网 / Trademark Data Open.
  - Download the historical trademark database and incremental updates as offered.
  - Record the received file inventory, formats and terms before reuse.
  deliverable: Historical trademark data plus incremental updates; the 2018 opening announcement confirms the scope but not the table list or file formats.
  cost: registration
  last_checked: '2026-09-28'
  caveat: The official service guide establishes registration, certificate, login and download; it does not enumerate files, formats, start dates, update cadence or redistribution terms. The old system URL in the 2018 announcement (wssq.sbj.cnipa.gov.cn:9080) may be stale, so begin from the current 中国商标网 service entry.
- route: Trademark Online Search (商标网上查询) - public per-record query
  access_status: available
  direct_url: https://sbj.cnipa.gov.cn/sbcx/
  requirements: A web browser; no account stated for single-record queries
  steps:
  - Open the Trademark Online Search page from the CNIPA homepage.
  - Query by trademark name, number, or registrant.
  - Export or record results one query at a time; this is not a bulk channel.
  deliverable: Per-record trademark query results; not a bulk download.
  cost: free
  last_checked: '2026-09-28'
  caveat: Public search is for verification and small samples; bulk collection by scraping is not an authorized route and no official public API was identified in the checked sources.

access:
  url: https://sbj.cnipa.gov.cn/
  cost: registration
  license: CNIPA opened the database to the public on 2018-12-26 per the official announcement; current redistribution terms of the download system are unverified.
  format:
  - download formats not verified
  api: false
  how_to_get: For raw bulk data, register as a 商标基础数据开放 user, obtain the trademark digital certificate, log in to 中国商标网 and download the opened historical/incremental data; retain the received file inventory and governing terms. For single-record verification, use the public online search.

caveats:
- The Xiao et al. (2024) trademark-firm linked panel is a researcher-constructed derivative, not the official database itself. Publisher-indexed paper text verifies its CNIPA/CSMAR inputs, SSE/SZSE scope, 2007--2017 span and firm-year unit, but not the matching key, cleaning, use-status coding inputs, or released final file.
- No public replication package was identified for the paper (DataCite and GitHub searches on 2026-08-13 returned nothing; Mendeley search page was not reachable); absence of a found package is a negative finding, not proof that no author-held route exists.
- The 2018 opening announcement does not enumerate tables or data items; the widely repeated "8 tables, 60 data items" figure comes from guide articles and is unverified first-hand.
- The publisher's live page returned 403 to direct automated fetch on 2026-09-28, but its publisher-indexed data-and-sample text verifies the paper's listed-firm scope, 2007--2017 period, CSMAR financial input and firm-year panel. It does not make the full construction section, appendix, code, or final panel available.
- Bulk download requires real-name registration and a digital certificate; eligibility of researchers without a Chinese identity document is not established.
- Registrant identity and address fields are personal/entity data; redistribution is subject to unverified current system terms.

production:
  raw_sources:
  - name: CNIPA trademark registration database
    source_type: dataset
    role: Official raw registration records (historical plus incremental) used as the trademark side of the paper's linked data
    access_route: Trademark Data Open download system (registered users) or public online search
    url: https://sbj.cnipa.gov.cn/
    coverage: All CNIPA-registered trademarks, nationwide; start year and exact fields not verified
    last_checked: '2026-08-13'
  - name: CSMAR listed-firm data (China Stock Market & Accounting Research)
    source_type: dataset
    role: Listed-firm financials and market value used for the firm side of the linked dataset; see the csmar record for its own product boundary
    access_route: Commercial subscription; see the csmar canonical record
    coverage: SSE/SZSE listed firms per the paper's abstract summary
    last_checked: '2026-08-13'
  acquisition_methods:
  - registered bulk download from CNIPA
  - commercial subscription (CSMAR)
  - applicant-name matching (paper-specific)
  sample_construction: >-
    Xiao et al. (2024) construct a trademark--firm linked dataset by linking CNIPA
    trademark-registration records with CSMAR data for all SSE/SZSE listed firms from
    January 2007 through December 2017. The paper says the end date permits at least
    a three-year window to observe trademark usage, and its financial-data panel is at
    the firm-year level. It categorizes marks by current use and business relatedness.
    The available publisher-indexed text does not show the linkage key, cleaning,
    observation rules, or the inputs and protocol for the use-status classification.
  pipeline_stages:
  - stage: collect
    inputs:
    - CNIPA trademark registration records
    method: The paper identifies CNIPA trademark-registration records as its trademark input; the available text does not disclose whether authors used the official download system, a commercial compilation, or another acquisition channel.
    output: Raw trademark registration records
    evidence: Publisher-indexed paper text identifies CNIPA registration records; the 2018-12-25 CNIPA announcement documents a current public database route, but neither source identifies the authors' acquisition channel.
  - stage: match
    inputs:
    - Raw trademark registration records
    - CSMAR listed-firm records
    method: Link trademark registrations to their listed-firm owners. The exact matching key, entity-resolution algorithm, deduplication and treatment of name variants are not exposed in the publisher-indexed text.
    output: Trademark-firm matched records
    evidence: Publisher-indexed data-and-sample text verifies that a trademark--listed-firm linked dataset was constructed; full matching details remain unavailable.
  - stage: aggregate
    inputs:
    - Trademark-firm matched records
    method: Build a firm-year panel and classify trademarks by current use and relationship to a firm's current businesses. The full coding and aggregation protocol is not exposed in the available text.
    output: Firm-year trademark panel used for market-value regressions
    evidence: Publisher-indexed paper text verifies the firm-year panel and the use/business-relatedness distinction; variable-construction details remain unverified.
  constructed_variables:
  - name: trademark counts by use status
    concept: In-use versus unused trademarks, and unused trademarks registered for current businesses versus unrelated ones
    source_fields: Trademark registration records and firm business scope
    method: Paper-specific classification; procedure in the unread appendix
    validation: Reported robustness results in the paper
    limitations: Exact classification inputs and code are not public
  validation: []
  output:
    unit_of_observation: Listed-firm year (paper-specific panel); trademark registration record (official database)
    structure: Firm-year panel (paper derivative) or registration-record files (official database)
    geography: China national; firm-level with subnational IPR-protection interactions in the paper
    time_span: Firm-year panel, January 2007--December 2017 (publisher-indexed data-and-sample text); official database historical plus incremental
    key_variables:
    - Trademark counts by use status (paper derivative)
    - Tobin's Q and firm controls (paper derivative, from CSMAR)
    - Registration fields (official database)
    formats:
    - paper package formats unknown
    - official download formats unknown
  reproducibility:
    level: needs-verification
    starting_point: https://sbj.cnipa.gov.cn/ (official database) plus a CSMAR subscription
    code_available: false
    requirements:
    - CNIPA registered download access (digital certificate)
    - CSMAR subscription for listed-firm side
    - Matching algorithm from the paper appendix (paywalled)
    blockers:
    - No public replication package identified (DataCite/GitHub searches 2026-08-13)
    - Matching code and use-status classification not released
    - Appendix access is paywalled
  compliance:
    terms_or_license: CNIPA announcement opened the database to the public (2018-12-26); download-system terms and redistribution rights unverified
    robots_or_rate_limits: No official public API identified; do not scrape the public search interface for bulk collection
    personal_or_sensitive_data: Registrant identity and address fields; treat as entity/personal data under applicable rules
    redistribution: Unverified; assume redistribution of downloaded or matched files requires explicit permission
    review_needed: true

quality:
  profile_status: partial
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Xiao, Han, Li, Ran, Zhou & Tong (2024), Trademarks and firm market value: Evidence from new trademark-firm linked data in China'
  doi: https://doi.org/10.1016/j.respol.2023.104941
  journal: Research Policy
  year: 2024
  dataset_role: Main explanatory data - constructed trademark-firm linked dataset linking CNIPA trademark registrations to CSMAR listed firms for market-value (Tobin's Q) analysis
  evidence_type: publisher-indexed paper text (direct automated page access blocked)
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0048733323002251
  data_note: >-
    Publisher-indexed text in the paper's Data and sample construction section says
    the study begins with all Shanghai and Shenzhen listed firms from January 2007 to
    December 2017, obtains financial data from CSMAR, creates a firm-year panel, and
    constructs a dataset linking trademarks to listed firms that own them. Elsevier's
    page also identifies the trademark input as CNIPA registration records and states
    the current-use/business-relatedness findings. Direct automated access to that
    page was blocked on 2026-09-28, and the available text does not expose the exact
    matching/classification protocol, author acquisition channel, code, or final file.

provenance:
- source: https://sbj.cnipa.gov.cn/sbj/ssbj_gzdt/201812/t20181225_19877.html
  field_scope:
  - opening date (2018-12-26) and public-access decision
  - historical plus incremental data scope
  - download via the Trademark Data Open section of the Trademark Online Service System by registered users
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://sbj.cnipa.gov.cn/
  field_scope:
  - current existence of the Trademark Data Open and Trademark Online Search services
  - SSO login route and public search entry point
  - absence of an exposed bulk/API entry on the homepage
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://www.cnipa.gov.cn/module/download/downfile.jsp?classid=0&filename=d2fc1ff4b9f0490f859129f57aa58cd8.pdf&showname=%E7%9F%A5%E8%AF%86%E4%BA%A7%E6%9D%83%E6%94%BF%E5%8A%A1%E6%9C%8D%E5%8A%A1%E4%BA%8B%E9%A1%B9%E5%8A%9E%E4%BA%8B%E6%8C%87%E5%8D%97.pdf
  field_scope:
  - Official 商标基础数据开放 service conditions, obtaining route, required trademark digital certificate and registration-to-login-to-download process
  - Boundary that data use must comply with applicable laws and that the guide does not enumerate files or redistribution terms
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.samr.gov.cn/xw/zj/art/2023/art_8e80bc49477042eb969f4d9c2b21b3b9.html
  field_scope:
  - 2018 public opening of existing trademark basic information and registered-user download of historical and incremental data
  - Historical opening-date scale only (about 35 million basic records at the announcement); not treated as a current total
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.colorado.edu/business/faculty-research/2024/03/18/strategy-entrepreneurship
  field_scope:
  - paper identity, first-of-its-kind trademark-firm linked dataset claim
  - in-use/unused classification and IPR-protection findings
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://api.crossref.org/works/10.1016/j.respol.2023.104941
  field_scope:
  - DOI, exact title, full author list, journal, volume, issue and pages
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://www.sciencedirect.com/science/article/pii/S0048733323002251
  field_scope:
  - paper actual use of CNIPA trademark-registration records and CSMAR financial data
  - all SSE/SZSE listed firms, January 2007--December 2017, and firm-year panel
  - stated three-year usage-observation rationale and use/business-relatedness categories
  - boundary that matching key, classification protocol, author acquisition channel, code and final panel are not exposed in available publisher-indexed text
  added: '2026-09-28'
  confidence: medium
  verified: true
- source: https://api.datacite.org/dois and https://api.github.com/search/repositories
  field_scope:
  - negative finding: no public replication package or dataset DOI for the paper found
  added: '2026-08-13'
  confidence: med
  verified: true

related_datasets:
- id: china-patents
  relation: complement
- id: csmar
  relation: complement
- id: china-firm-registry
  relation: complement
---

## Positioning in one sentence

This is the official CNIPA trademark registration database — a publicly opened (2018-12-26), directly downloadable raw source of Chinese trademark records that an ordinary researcher can reach with a registered system account, plus the paper-specific trademark-firm linked panel of Xiao et al. (2024 Research Policy) as a researcher-constructed derivative with no public release found.

## Select rules

- Prioritize it when the question measures brand-related innovation or trademark activity, or builds a trademark-firm linked panel; trademarks capture a different IP dimension than patents.
- Switch to patent data when the question is technological innovation; choose CSMAR's trademark module only when its product boundary and matching are verified.
- Do not use it for unregistered marks, actual brand use, or market outcomes that registration records cannot measure.

## Get recipe

Start with the 2018 CNIPA opening announcement and the current homepage to confirm the route, then register at the Trademark Online Service System and obtain the digital certificate before attempting the bulk download; use the public online search for verification and small samples. For a trademark-firm linked panel, acquire the CNIPA and CSMAR inputs separately, then design and document an entity-resolution procedure rather than assuming the paper's unreleased matching key or rules. The paper confirms a 2007--2017 listed-firm, firm-year design, but its available text does not expose the match, cleaning, or use-status coding protocol.

## Connections and Limitations

The strongest current knowledge is the product identity, the public opening and download route, and the paper's verified CNIPA/CSMAR, 2007--2017 firm-year use. The exact download-system mechanics, file inventory and formats, paper-level matching and use-status coding, author acquisition channel, code, final panel, and redistribution terms remain intentionally open. A researcher should verify the first group from inside the system and design or obtain the second group before treating the linked panel as reproducible.
