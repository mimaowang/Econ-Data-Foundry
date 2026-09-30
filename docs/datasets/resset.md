---
schema_version: 3
catalog_status: ready
id: resset
name: RESSET Financial and Economic Research Database
aka:
- RESSET
- RESSET/DB
- 锐思数据
- 锐思金融研究数据库
- 锐思数据库
- RESSET金融研究数据库
- RESSET经济数据库
- RESSET/ED
provider: >-
  北京聚源锐思数据科技有限公司 (Beijing Juyuan RESSET Data Technology
  Co., Ltd.), a Chinese high-tech enterprise focused on financial databases
  and finance teaching/research software; HQ in Beijing (official about page,
  read 2026-08-15)
china_related: true
domains:
- finance
- accounting
- firm
- macro
- market
- industry

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Institutional subscription to the RESSET data platform at db.resset.com
    (IP-based on campus, CARSI federated login, or user registration), with
    table-level query and export of the modules the institution purchased;
    separate sub-platforms exist per product family (e.g., madb.resset.com
    macro database login page, uni.resset.com global financial news platform,
    edp.resset.com enterprise big-data platform).
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider-first grounding (2026-08-15): the official RESSET site
    (www.resset.cn) renders product families machine-readably, and three
    independent university library pages (NUFE subscription, FZFU trial,
    HFNU trial) confirm the module families, the db.resset.com entry, and
    IP/CARSI-based access. The financial-research line (RESSET/DB) is a
    multi-module database (stock, bond, fund, FX, futures, gold, research
    reports, margin trading, macro/industry/financial statistics, plus
    STAR/NEEQ/HK/option/quant-factor families) with 20+ export formats
    including SAS/SPSS; the economic line (RESSET/ED) covers macro, county,
    city, financial-market, industry and international-economic databases
    with close to one million indicators from NBS and other official sources.
    Paper-use grounding (2026-09-28) additionally verifies a distinct RESSET
    China Enterprise Big Data Platform use: a 2026 Scientific Data article
    used its enterprise-registration data as Excel input for a Greater Bay
    Area urban land-use construction workflow.
  barrier: >-
    The verified paper establishes actual use of the China Enterprise Big
    Data Platform only, not availability, fields, coverage, or export rights
    for every RESSET/DB or RESSET/ED module. Module availability depends on
    each institution's purchased scope; export limits/API conditions are not
    documented on any machine-readable official page read so far.

unit_of_observation: >-
  Securities/instruments (stocks, bonds, funds, FX, futures, gold) - trading
  day or high-frequency; listed companies - reporting period; macro/industry
  indicators - period; county/city economic indicators - period
structure: multi-module-panel
geo_granularity:
- Nationwide
- province
- city
- county
- listed company
- securities
geography: Mainland China financial markets and economy; HK/US stock modules and
  international economic-financial databases are separate families
time_span:
  start: '1990'
  end: ongoing
  last_confirmed_release: >-
    Official and library pages state full market history from 1990 to
    present (30+ years of financial market data); per-module coverage varies
    (unread at table level)
  coverage_note: >-
    The 1990 start applies to the financial-market families per official
    wording; macro/industry modules include multi-decade history ("decades
    to over a century" per official econo page) - per-table coverage must be
    checked in the platform.
  last_checked: '2026-08-15'
frequency:
- daily
- monthly
- quarterly
- annual
- event
- high-frequency
sample_size: >-
  Official claims: financial research database "T-level" (terabyte-scale)
  data; macro database up to 140,000 indicators (official) or 200,000
  (FZFU library page); industry database 21 sectors / 1,400+ sub-industries
  / 700,000+ indicators; economic family close to one million indicators.
  These are provider marketing figures, not independently audited counts.
key_variables:
- Stock, bond, fund, FX, futures, gold quotes and transactions
- Financial statements and derived indicators (holding-period returns, risk factors, volatility, Fama-French factors, valuation metrics)
- Research reports database
- Margin trading (融资融券) records
- STAR Market / NEEQ / HK / US stock modules
- Options, wealth-management products, quantitative-factor and FF-factor families
- High-frequency futures/options datasets
- Macro, industry, financial statistics series
- County (区县) and city economic databases
- Enterprise big-data platform (工商-registered entities)

research_fit:
  best_for:
  - Research on Chinese financial markets (stocks, bonds, funds, futures, FX, gold) with derived indicator families precomputed for model building
  - Macro/industry/city/county economic indicator series from one commercial platform with official-source data lineage
  - Teaching and quant-lab workflows (SAS/SPSS export formats; RESSET also sells teaching/quant platforms)
  choose_over:
  - Choose CSMAR when the question needs the standard academic table structure for corporate governance/accounting topics of listed companies; RESSET is a substitute family with similar coverage but different table organization and derived indicators.
  - Choose Wind when real-time market conditions, bond terminal, or programmatic terminal access matter more than academic table structure.
  - For unlisted industrial firm microdata, use ASIF/business-registration products - RESSET's firm coverage is primarily listed companies plus its enterprise big-data platform (工商-registered entities), not the ASIF survey universe.
  not_good_for:
  - Treating the verified Enterprise Big Data Platform example as evidence that every RESSET module, table, or a paper's cleaned analysis file is obtainable
  - Assuming a module is subscribed just because an institution lists RESSET - check the institution's purchased module list (e.g., NUFE lists 13 modules)
  - Household or individual-level survey research
  needs_join_for:
  - Firm-level unlisted-company outcomes (ASIF family), customs transactions, or patent records - external joins by company name/code
  - Policy timing/assignment design evidence (see Econ-Variation)
  variation_available:
  - Long listed-company and market time series; event-level market data; cross-sectional variation across modules
topics:
- financial markets
- listed companies
- macro indicators
- industry statistics
- county economy
- derived indicators

good_for:
- Market-level and listed-firm financial research with institutional subscription
- Macro/industry/county/city indicator extraction from one commercial platform
- Quant and teaching-lab workflows needing SAS/SPSS/CSV exports
identification:
- Within-module time-series and cross-sectional variation in listed firms, securities, and market indicators, subject to the purchased table's coverage
- Geographic and period variation in the separately documented county and city economic-indicator families, subject to the purchased module and table
- Enterprise-name and sector-label heterogeneity in the separately documented China Enterprise Big Data Platform; this supports data matching or classification work, not a policy-treatment definition
linkable_keys:
- Stock code
- Security code
- Company name
- Indicator codes (per table)
- Date

joins:
- target: csmar
  relation: substitute-and-benchmark
  keys:
  - Stock code
  - Date
  method: exact on stock code/date; cross-check derived indicators
  evidence_status: plausible
- target: wind
  relation: substitute-and-benchmark
  keys:
  - Stock code
  - Date
  method: exact on stock code/date
  evidence_status: plausible
- target: china-patents
  relation: complement
  keys:
  - Company name
  method: deterministic-plus-fuzzy
  evidence_status: plausible

access_routes:
- route: institutional-web
  access_status: available-with-subscription
  direct_url: https://db.resset.com/
  requirements: >-
    School/institution subscription; on-campus IP access without credentials
    (per NUFE library page), or CARSI federated login (sp-ressetdb.carsi.edu.cn
    authorize endpoint on the login page), or personal registration with
    institution-provided account.
  steps:
  - Check the school library's RESSET resource page for purchased modules and off-campus access method.
  - Open db.resset.com and log in (IP, CARSI, or registered account).
  - Select the module/table, set code, time range and fields, then export (20+ formats incl. Txt, Excel, SAS, SPSS, MATLAB, CSV, XML).
  deliverable: >-
    Table-level data of the modules the institution subscribes to; unsubscribed
    modules are not exportable. Citation obligation: 数据来源：锐思数据库（www.resset.cn）.
  cost: paid
  last_checked: '2026-08-15'
  caveat: >-
    Module scope differs by institution (NUFE 2024-2026 subscription lists 13
    modules incl. 股票/新三板/科创板/外汇/债券/期货/基金/黄金/研究报告/融资融券/金融统计/宏观统计/行业统计);
    trial institutions (FZFU, HFNU) get access until 2026-12-31.
- route: trial
  access_status: available-with-conditions
  direct_url: https://db.resset.com/
  requirements: Institution-level trial agreement; on-campus IP or trial account
  steps:
  - Ask the library to request a trial; use the trial login/URL provided (e.g., db.resset.com/UserLogin with the institution's trial credentials).
  - Export within trial scope and period.
  deliverable: Time-limited access to the trial module family
  cost: free
  last_checked: '2026-08-15'
  caveat: Trial scope and period set by provider; not a substitute for subscription evidence.

access:
  url: https://db.resset.com/
  cost: paid
  license: >-
    Institutional subscription per 用户授权使用说明 (terms of use page on
    db.resset.com, read 2026-08-15): license for given scope and time only,
    no transfer/rental of accounts, no redistribution; users citing data in
    teaching/research must state 数据来源：锐思数据库（www.resset.cn）
  format:
  - txt
  - xlsx
  - csv
  - sas
  - spss
  - matlab
  - xml
  - html
  api: false
  how_to_get: >-
    Confirm the institution's subscription and modules via the library;
    enter db.resset.com (IP/CARSI/account), query the module table, and
    export. 20+ export formats are officially claimed; the official site
    reports no public API in the pages read.
caveats:
- Paper-use evidence in this catalog is absent - do not claim any paper used RESSET without reading its data section.
- Institutional module scope varies; always check the library's module list first.
- Provider coverage counts (T-level, 140k-1M indicators) are marketing figures; treat per-table coverage as unverified.
- Export limits, API, and off-campus terms are not documented in any machine-readable official page read this round.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Li et al. (2026), Urban land use of national economic sectors in Guangdong-Hong Kong-Macao Greater Bay Area from 2015-2022'
  doi: https://doi.org/10.1038/s41597-026-06968-z
  journal: Scientific Data
  year: 2026
  dataset_role: >-
    Enterprise-registration input from RESSET China Enterprise Big Data
    Platform for BERT training in a Greater Bay Area sectoral urban-land-use
    construction workflow.
  evidence_type: published-paper-full-text
  evidence_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC13079856/
  data_note: >-
    The open full text identifies Excel enterprise data from
    edp.resset.com/company/index. It says the input contained current and
    historical enterprise names and sectoral labels covering 97 major GB/T
    4754-2017 sectors; the authors corrected or removed inconsistent entries
    and formed a 598,703-record training dataset. This is evidence of actual
    use of that enterprise-platform input, not a released copy of the
    authors' cleaned training data, model, or final land-use product.

provenance:
- source: https://www.resset.cn/index/home/ (read 2026-08-15)
  field_scope:
  - product family structure (investment-research/teaching/lab lines)
  - financial research database module list
  - macro/industry/enterprise platform subdomains
  - provider name in footer
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.resset.cn/index/db/fin.jsp (read 2026-08-15)
  field_scope:
  - RESSET/DB module families and export formats (20+, SAS/SPSS)
  - data lineage claim (regulators, exchanges, financial information providers)
  - derived indicator families
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.resset.cn/index/db/econo.jsp (read 2026-08-15)
  field_scope:
  - RESSET/ED families (macro, county, city, financial-market, industry, international)
  - data sources (NBS, local statistical bureaus, GACC, CRB, etc.)
  - indicator volume claims
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.resset.cn/index/about/contact.jsp (read 2026-08-15)
  field_scope:
  - provider legal name 北京聚源锐思数据科技有限公司
  - HQ address/contact
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://db.resset.com/ and https://db.resset.com/db/main/termofuseIn.jsp (read 2026-08-15)
  field_scope:
  - platform entry (新版 RESSET 数据库 login; CARSI authorize endpoint)
  - terms of use (license scope, account rules, citation obligation)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://lib.nufe.edu.cn/2024/1010/c438a9020/page.htm (read 2026-08-15)
  field_scope:
  - NUFE subscribed module list (13 modules)
  - on-campus IP access without credentials
  - subscription period
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.fzfu.com/lib/info/1103/2134.htm (read 2026-08-15)
  field_scope:
  - trial route and login URL pattern
  - 13-module description; macro database 23 modules / 200,000 indicators claim
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://tsg.hfnu.edu.cn/info/1501/6531.htm (read 2026-08-15)
  field_scope:
  - trial route db.resset.com; macro database 23 modules / 140,000 indicators claim
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://pmc.ncbi.nlm.nih.gov/articles/PMC13079856/ (read 2026-09-28)
  field_scope:
  - actual 2026 paper use of RESSET China Enterprise Big Data Platform
  - enterprise-registration input form (Excel), current and historical names, and sector labels
  - paper-specific cleaning and 598,703-record BERT training dataset boundary
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: csmar
  relation: substitute-and-benchmark
- id: wind
  relation: substitute-and-benchmark
- id: china-cnrds
  relation: substitute-and-benchmark
---

## Positioning in one sentence

RESSET (锐思数据, provider 北京聚源锐思数据科技有限公司) is a commercial Chinese financial-and-economic research database family - RESSET/DB for financial markets (stock, bond, fund, FX, futures, gold, margin trading, research reports, STAR/NEEQ/HK/option/quant-factor modules) and RESSET/ED for macro/county/city/industry/international indicators - reached through an institutional subscription at db.resset.com with IP/CARSI login and table-level exports in 20+ formats; an open 2026 paper also verifies actual use of its separate China Enterprise Big Data Platform (edp.resset.com) for enterprise-registration input, without proving access to every module.

## Select rules

- Choose RESSET when the institution subscribes and the question needs Chinese financial-market series or official-source macro/industry/county/city indicators in a commercial platform with derived-indicator families.
- Compare with CSMAR (academic table structure for governance/accounting) and Wind (real-time/bond-terminal workflows) before recommending; check the institution's purchased module list first.
- The verified 2026 paper establishes the enterprise-platform use only; do not extrapolate it to every RESSET module or assume all modules are subscribed.

## Get recipe

1. Check the school library's RESSET page for purchased modules and off-campus access (e.g., NUFE lists 13 modules; FZFU/HFNU trials run through 2026-12-31).
2. Open https://db.resset.com and log in (on-campus IP, CARSI, or registered account).
3. Select module/table, set code, time range and fields, and export (Txt/Excel/SAS/SPSS/MATLAB/CSV/XML among 20+ formats).
4. Cite as 数据来源：锐思数据库（www.resset.cn） per the terms of use.

## Connections and Limitations

RESSET is a substitute-and-benchmark neighbor of CSMAR and Wind (stock code + date joins) and complements patent/firm layers by company name. Its China Enterprise Big Data Platform has verified use as an enterprise-registration input with current/historical names and sector labels, but a paper-specific cleaned training set is not a delivered file. Module scope, export limits, API availability and off-campus terms are institution-specific and not documented by any machine-readable official page read this round; provider coverage counts are marketing figures.
