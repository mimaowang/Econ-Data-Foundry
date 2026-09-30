---
schema_version: 3
catalog_status: grounding
id: china-cnrds
name: China Research Data Services Platform (CNRDS 中国研究数据服务平台)
aka:
- CNRDS
- 中国研究数据服务平台
- Chinese Research Data Services
- 经禾数据
- CNRDS 财经商学数据库
provider: Shanghai Jing He Information Technology Co., Ltd. (上海经禾信息技术有限公司)
china_related: true
domains:
- finance
- accounting
- firm
- governance
- innovation
- macro
- regional
- industry

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Module-level research data tables exported through the institutional web
    platform (www.cnrds.com). The platform markets three series: the Basic Library
    (基础库, ~29 databases covering listed-company stocks, financials and governance,
    macro and regional economy, bonds), the Company Featured Library (公司特色库,
    ~99-109 databases covering listed-company operations, news and sentiment, text,
    personnel, banks and bonds, and socio-economic organizations), and the Economic
    Featured Library (经济特色库, ~57-82 databases covering macro, regional, industry,
    foreign-trade, humanities/social-science and public-finance series, including
    topics such as digital economy, industrial robots, high-speed rail, night lights,
    green finance and local debt). Exact counts vary by source and over time.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    CNRDS is a commercial research-data platform built by Shanghai Jing He on the
    WRDS model, offering hundreds of topic databases on Chinese listed companies,
    macro/regional economy and industry topics through institutional subscriptions.
    It is a convenient processed distribution channel for several official products
    already recorded in this catalog (processed ASIF editions, customs-trade modules,
    patent modules, land-market modules, high-speed-rail data), but a researcher
    needs a subscribing institution, a verified personal account and a signed data-use
    agreement to obtain data; module availability depends on what the institution
    purchased. Paper-use grounding (2026-09-28) directly verifies one concrete
    regional-economics use: a county-panel study obtained patent records from
    CNRDS, which the paper describes as cleaned and standardized from CNIPA
    records with geocoded applicant addresses for county-level counts.
  barrier: >-
    Registration is restricted to institutions that purchased the platform (the
    registration page refuses non-subscribing schools); the data-use agreement assigns
    data ownership to the provider, allows academic research only and prohibits
    transfer or redistribution. The exact module inventory, subscription scope and
    update cadence are commercial and change over time; the current module list was
    not verified inside the platform this round. The verified paper establishes
    a patent-data workflow, not access to every CNRDS module or the paper's
    compiled analytic panel.

unit_of_observation: Module-dependent — listed company/security/day or period; macro indicator per period; region (province/city/county) per period; patent, land, customs or other record per transaction/event; bank, bond, organization or person per record
structure: Multi-module platform; most modules are panels or event/record tables that can be exported and aggregated by the researcher
geo_granularity:
- Nationwide
- province
- city
- county
- listed company
- security
- bank
- person
geography: China national; modules cover mainland capital-market participants, NBS-style macro/regional/industry series, and official transaction databases; scope of each module depends on the subscription
time_span:
  start: unknown
  end: ongoing
  last_confirmed_release: ongoing
  coverage_note: >-
    Stock-market modules typically begin in the 1990s, but every module, table and
    field has its own start year; the platform itself does not publish a single
    start date. Module coverage windows are commercial and were not verified inside
    the platform this round.
  last_checked: '2026-08-13'
frequency:
- daily
- monthly
- quarterly
- annual
- event
sample_size: Platform-wide universe depends on the module (e.g. all A-share listed companies and their histories, NBS industrial-firm editions, official trademark/patent/land/customs records); no single platform-level count was verified this round
key_variables:
- Listed-company stock, financial, governance, news, text and personnel variables (Basic and Company Featured Libraries)
- Macroeconomic, regional and industrial time series (Basic Library and Economic Featured Library)
- Topic databases: digital economy, industrial robots, high-speed rail, night lights, green finance, local debt, BRI, carbon neutrality (Economic Featured Library)
- Processed editions of official data: industrial enterprises (ASIF-type), customs trade, patents, land market, government procurement, depending on module
- Verified CNRDS patent use: CNIPA-sourced patent records cleaned and standardized by the platform, including geocoded applicant addresses for county aggregation in one paper
- Exact variables are table- and module-specific; confirm inside the purchased module before promising any field

research_fit:
  best_for:
  - Listed-company research needing a curated, ready-made module when the institution subscribes (similar role to CSMAR for finance, governance and accounting topics)
  - Convenient processed editions of official Chinese microdata (industrial firms, customs, patents, land, procurement) delivered as exportable tables, when a module exists and is subscribed
  - Chinese macro/regional/industry time series and topic data (digital economy, robots, HSR, night lights, green finance, local debt) in a single commercial platform
  choose_over:
  - Choose CNRDS over CSMAR for modules where CNRDS's coverage is verified and subscribed (e.g. its economic topic series and some processed official microdata editions); for finance/accounting/governance tables CSMAR and CNRDS are close substitutes and the deciding factor is what the institution actually purchased.
  - Choose CNRDS over building from raw official sources when a processed, parsed and structured module exists and the subscription is confirmed; it trades away control over cleaning for convenience.
  - Do not choose CNRDS when the institution does not subscribe, when the needed module is not purchased, or when the research requires the original raw records with full field control (use the official provider route instead).
  not_good_for:
  - Research requiring full original microdata with unrestricted fields; CNRDS modules are processed, commercial editions whose cleaning and field coverage are not fully documented in public sources.
  - Unlisted-firm research unless the specific industrial-firm or registry module is purchased and its coverage verified.
  - Reproducing the exact analysis files of a paper whose module, cleaning and matching steps are not disclosed.
  - Any module whose subscription the institution has not purchased; never assume platform membership implies all modules.
  needs_join_for:
  - Firm financials and governance outcomes for listed companies may need CSMAR/Wind cross-checks; unlisted-firm and transaction-level research needs ASIF, customs, land or registry records
  - Outcomes, treatments or context not embedded in the purchased modules require the official sources recorded in this catalog (NBS, CNIPA, SAMR, customs)
  variation_available:
  - Data dimensions such as policy-timing series (local debt, green finance, BRI) are data, not treatment definitions; treatment/assignment knowledge belongs in the complementary variation repository and is not recorded here.
  topics:
  - Chinese listed companies
  - corporate finance
  - corporate governance
  - macroeconomic time series
  - regional economy
  - industrial economy
  - digital economy
  - high-speed rail
  - green finance
  - local government debt
  - innovation and patents

good_for:
- Listed-company finance, governance, news, text and personnel research (module permitting)
- Chinese macro, regional and industry panels in a single commercial interface
- Processed editions of official microdata (industrial firms, customs, patents, land, procurement)
identification:
- Patent applications, grants, applicants and locations can vary by county and year in the documented CNRDS patent workflow; the platform's geocoded applicant addresses support aggregation to a researcher-defined county-year panel
- Other listed-company, macro, regional and topic-module variation is module-dependent and must be checked inside the subscribed product; these data dimensions do not define policy treatment or assignment
linkable_keys:
- Stock code
- Full company name
- Unified social credit code where recorded
- Region codes (province/city/county) where recorded by module
- Patent, land, customs or procurement record identifiers by module

joins:
- target: csmar
  relation: substitute-and-benchmark
  keys:
  - Stock code
  - Full company name
  method: Both platforms cover listed-company finance/governance tables; join or cross-check by stock code with attention to different variable definitions and reporting vintages.
  evidence_status: plausible
- target: wind
  relation: substitute-and-benchmark
  keys:
  - Stock code
  - Macro indicator name
  method: Wind is preferred for real-time market, bond-terminal and API use; CNRDS modules are table-oriented academic exports; cross-check definitions before pooling.
  evidence_status: plausible
- target: asif
  relation: complement
  keys:
  - Firm name
  - Unified social credit code where recorded
  method: CNRDS markets processed editions of NBS industrial-firm data (recorded in the asif record as a distribution channel); the exact module, cleaning and fields must be verified before treating it as ASIF.
  evidence_status: plausible
- target: china-customs
  relation: complement
  keys:
  - Firm name
  - Customs record identifiers where recorded
  method: CNRDS provides processed customs-trade modules for some years per the china-customs record; verify module scope before substituting for the original customs route.
  evidence_status: plausible
- target: china-patents
  relation: complement
  keys:
  - Full company name
  - Unified social credit code
  - Patent number
  method: CNRDS patent modules provide matched listed-firm patent panels; the official CNIPA database remains the original source and the module's matching procedure is commercial.
  evidence_status: plausible
- target: china-land-transaction
  relation: complement
  keys:
  - Full company name
  - City/county codes
  method: The Company Featured Library includes a listed-company land-market database (LMID); treat it as a processed convenience route and verify coverage against the official land-transfer record route.
  evidence_status: plausible
- target: china-high-speed-rail-network
  relation: complement
  keys:
  - Station names
  - City codes
  method: The Economic Featured Library includes a high-speed-rail/airline database (CRAD) used by papers for HSR connectivity; compare its station/route fields and vintage with the dedicated network record before use.
  evidence_status: plausible

access_routes:
- route: institutional-web (www.cnrds.com registration + export)
  access_status: available-with-subscription
  direct_url: https://www.cnrds.com/
  requirements:
  - The researcher's institution must have purchased CNRDS; the registration page refuses users from non-subscribing schools
  - Personal registration with institution selection, identity tier (teacher/PhD student/master/undergraduate/other researcher), phone verification, name/college/department/email/student-ID details, photo ID upload, and upload of a personally signed data-use agreement
  - On-campus IP access (school login) for the Basic Library; a verified personal account can access subscribed modules and log in off-campus with phone+code per library guides
  steps:
  - Confirm with the school library which CNRDS series/modules are purchased and the off-campus access method.
  - Register a personal account at www.cnrds.com under the institution, complete phone verification, identity details and the signed data-use agreement upload.
  - Log in and locate the target module; export the table fields of interest to the platform-supported format.
  - Record the module name, coverage window, field list and any download limits before reuse.
  deliverable: Module-level data tables from the series purchased by the institution; the Basic Library is available when a specialty library is subscribed; unpurchased modules are not accessible.
  cost: paid
  last_checked: '2026-08-13'
  caveat: The registration page and data-use agreement were read directly on 2026-08-13; module counts, current inventory, update cadence and download mechanics were not verified inside the platform. Some institutions offer limited trial accounts with partial data; treat trial data as a preview, not a research archive.
- route: trial account (where offered)
  access_status: available-with-conditions
  direct_url: https://www.cnrds.com/
  requirements:
  - A trial account issued by a participating institution (per library guides, some institutions publish trial credentials)
  - Trial scope is limited (e.g. roughly three years of history or about 20% of cross-section databases per library guides); not a full archive
  steps:
  - Obtain the trial account and password from the institution's library page or database administrator.
  - Log in and verify which modules and years are actually accessible.
  - Treat trial data as a preview; do not build a research archive on it.
  deliverable: Limited preview of selected modules with partial history.
  cost: registration
  last_checked: '2026-08-13'
  caveat: Trial scope descriptions come from library guides and vary by institution; the provider does not publish a fixed trial policy.

access:
  url: https://www.cnrds.com/
  cost: paid
  license: >-
    The platform data-use agreement assigns ownership of the data and documentation
    to the provider, permits academic (non-commercial) research use of the user's own
    research, prohibits transfer, sale or disclosure to third parties, and requires
    citing CNRDS as the data source. No redistribution right was identified.
  format:
  - platform export formats (verified inside the platform by the subscriber)
  api: false
  how_to_get: Confirm the institution's subscription with the school library, register a personal account at www.cnrds.com with institution verification and a signed data-use agreement, then export the purchased modules.

caveats:
- CNRDS is a commercial processing/redistribution channel for official Chinese data (NBS industrial-firm editions, customs, CNIPA patents, land market, procurement); the original provider remains the authority for coverage, and the module's cleaning and matching procedures are commercial and not fully documented in public sources.
- Module counts differ across sources (29 basic libraries; roughly 99-109 company featured and 57-82 economic featured libraries, with totals reported variously as ~168 to ~218) and change over time; verify the current module list inside the platform before promising a module.
- Institutional subscriptions differ; "CNRDS is available" never implies a specific module is available.
- A verified 2025 county-panel paper establishes CNRDS patent-record use, cleaning/standardization from CNIPA and geocoded applicant addresses, but does not name the purchasable module or release the author-built county panel. The two older JRS/RSUE entries remain abstract/bibliographic leads only; do not generalize any one paper's module to the platform.
- No public API was identified in the checked sources; export happens through the web platform.
- Registration requires a subscribing institution and identity verification; eligibility for researchers without an institutional subscription is not established.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Li, Yang, Zhang, Ye & Lin (2025), The impact of upgrading administrative rank on regional innovation from an agglomeration perspective: a quasi-natural experiment based on the establishment of Chongqing as a province-level municipality'
  doi: https://doi.org/10.3389/fpos.2025.1676094
  journal: Frontiers in Political Science
  year: 2025
  dataset_role: >-
    CNRDS patent records as county-year regional-innovation outcomes and robustness outcomes for a 1992-2010 Sichuan-Chongqing county panel.
  evidence_type: published-paper-full-text
  evidence_url: https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2025.1676094/full
  data_note: >-
    The open data section says CNRDS cleaned and standardized raw CNIPA records
    and provided geocoded applicant addresses, which the authors used to form
    county-level counts of domestic invention grants, invention applications
    and utility-model applications. The final 219-county/4,161-observation
    analytic panel, the authors' aggregation choices and any CNRDS module name
    are not represented as delivered CNRDS data.
- cite: 'Author (2025), Industrial Robots, Resource Misallocation, and Firm Innovation Performance: Evidence From China'
  doi: https://doi.org/10.1111/jors.70035
  journal: JRS
  year: 2025
  dataset_role: CNRDS patent records combined with the CSMAR firm panel (2011-2019) for patent quantity/quality outcomes
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/bla/jregsc/v66y2026i2p399-425.html
  data_note: >-
    Abstract/bibliographic level only, downgraded on 2026-08-13: the RePEc record
    confirms the paper identity, and the abstract-level claim that the paper combines
    CSMAR firm data with CNRDS/SIPO patent records is cross-referenced from the csmar
    record, whose own entry is anchored on the same RePEc abstract page. The paper's
    data section was not read this round, the exact CNRDS patent module was not
    confirmed from the paper itself, and the author names remain unresolved in this
    record; the abstract content was not re-verified on 2026-08-13 (repec.org fetch
    blocked). Do not treat this entry as data-section evidence.
- cite: 'Author (2026), Transportation Infrastructure and College Admissions Quality: Evidence from China''s National College Entrance Examination'
  doi: https://doi.org/10.1016/j.regsciurbeco.2026.104223
  journal: RSUE
  year: 2026
  dataset_role: CNRDS high-speed-rail data for HSR connectivity measures (2006-2018 window with Sina Gaokao cutoffs)
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/regeco/v119y2026ics0166046226000335.html
  data_note: >-
    Abstract/bibliographic level only, downgraded on 2026-08-13: the RePEc record
    confirms the paper identity, and the claim that the paper measures HSR
    connectivity with CNRDS high-speed-rail data and validates with census-based
    population mobility is cross-referenced from the china-census record, whose own
    entry is anchored on the same RePEc abstract page. The paper's data section was
    not read this round, the exact CNRDS module (CRAD or another) and the paper's
    station/route construction were not confirmed from the paper itself, and the
    author names remain unresolved in this record; the abstract content was not
    re-verified on 2026-08-13 (repec.org fetch blocked). Do not treat this entry as
    data-section evidence.

provenance:
- source: https://www.cnrds.com/
  field_scope:
  - provider identity (Shanghai Jing He copyright line) and official domain
  - registration flow: institution requirement, identity tiers, phone verification, ID upload, signed data-use agreement
  - data-use agreement: provider ownership, academic-use-only, no third-party transfer, citation requirement
  - refusal of non-subscribing institutions
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://lib.zqu.edu.cn/info/1141/7427.htm
  field_scope:
  - three-series structure (Basic 29 libraries, Company Featured 109, Economic Featured) and topic families
  - access model: basic library via school login; specialty libraries via personal account; off-campus phone+code access
  added: '2026-08-13'
  confidence: med
  verified: true
- source: https://utszlib.edu.cn/dynamicResource/view/id-1549.html
  field_scope:
  - English name (Chinese Research Data Services), WRDS-style positioning, ~218 topic databases cumulative
  - specialty-library series descriptions and topic lists (macro, regional, industrial, foreign-trade, humanities, public finance; digital economy, robots, night lights, BRI, carbon neutrality, green finance, local debt)
  added: '2026-08-13'
  confidence: med
  verified: true
- source: CNRDS data handbook references and university library module lists (searches on 2026-08-13)
  field_scope:
  - named modules: 中国高铁航线数据库 (CRAD), 中国工业统计数据库 (CISD), 工业企业专利数据库 (IIED), 中国海关贸易数据库 (CCTD), 上市公司土地市场信息数据库 (LMID)
  - module counts vary by version and source
  added: '2026-08-13'
  confidence: med
  verified: false
- source: Existing canonical records (asif, china-customs, china-patents, china-land-transaction, csmar, china-census, wind)
  field_scope:
  - paper-use entries for CNRDS patent and HSR data (JRS 2025, RSUE 2026), anchored on RePEc abstract pages and record cross-references, not on a direct reading of either paper's data section (downgraded to abstract on 2026-08-13)
  - CNRDS as a distribution channel for processed ASIF, customs, patent and land editions
  added: '2026-08-13'
  confidence: med
  verified: true
- source: https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2025.1676094/full (read 2026-09-28)
  field_scope:
  - actual CNRDS patent-record use in a 1992-2010 Sichuan-Chongqing county panel
  - CNRDS cleaning and standardization from CNIPA records and geocoded applicant addresses
  - paper-specific county aggregation, outcome construction and non-release boundary
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: csmar
  relation: substitute-and-benchmark
- id: wind
  relation: substitute-and-benchmark
- id: asif
  relation: complement
- id: china-customs
  relation: complement
- id: china-patents
  relation: complement
- id: china-land-transaction
  relation: complement
- id: china-high-speed-rail-network
  relation: complement
---

## Positioning in one sentence

CNRDS is a commercial, WRDS-style Chinese research-data platform run by Shanghai Jing He: it sells curated modules covering listed-company finance/governance/news/text, macro-regional-industry series, and processed editions of official microdata (industrial firms, customs, patents, land, procurement), obtainable only through a subscribing institution, a verified personal account and a signed data-use agreement; direct 2025 paper evidence verifies its CNIPA-derived, cleaned and geocoded patent workflow, but never assume platform membership implies a specific module.

## Select rules

- Prioritize it when the institution subscribes and the needed module is verified, especially for ready-made processed editions of official data (industrial firms, customs, patents, land, procurement) and for topic series (digital economy, robots, HSR, green finance, local debt).
- Compare with CSMAR/Wind before deciding: for listed-company finance, governance and accounting tables CSMAR and CNRDS are close substitutes, and the deciding factor is the purchased module; for high-frequency market or API work Wind is preferred.
- Do not use it for research needing full original microdata with unrestricted fields, for modules the institution did not purchase, or as a substitute for the official provider when the research needs the raw records and full cleaning control.

## Get recipe

Confirm the institution's purchased series and modules with the school library first; then register a personal account at www.cnrds.com under the institution, complete phone verification, identity details and the signed data-use agreement upload, log in, and export the module tables. Before promising a module to a researcher, check the module name, coverage window and field list inside the platform; treat library trial accounts as previews only.

## Connections and Limitations

The strongest current knowledge is the platform identity, provider, three-series structure, registration/terms, and one directly verified patent-data workflow: CNRDS cleaned and standardized CNIPA records and supplied geocoded applicant addresses for a county-panel study. The two older JRS/RSUE leads remain abstract/bibliographic only, so their modules are unconfirmed. The exact current module inventory, per-module coverage windows, download mechanics, update cadence and redistribution terms remain commercial and were not verified inside the platform; a future agent should confirm the specific module inside the platform or from a paper's data section before recommending it, and should not treat CNRDS editions as identical to the original official sources.
