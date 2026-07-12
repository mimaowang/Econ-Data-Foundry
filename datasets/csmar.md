---
schema_version: 2
catalog_status: ready
id: csmar
name: Guotai'an CSMAR China Economic and Financial Research Database
aka:
- CSMAR
- 国泰安
- China Stock Market & Accounting Research Database
- 希施玛
- CSMAR Solution
provider: Shenzhen Xishma Data Technology Co., Ltd.
china_related: true
domains:
- finance
- accounting
- firm
- governance
- innovation
- macro
unit_of_observation: Listed companies - day/month/quarter/year; securities - trading day; directors/executives - term of office;
  events - announcement date; macro indicators - period
structure: multi-module-panel
geo_granularity:
- Nationwide
- province
- city
- listed company
- securities
- personal
geography: Mainly China mainland capital market and listed companies; there are also Hong Kong stocks, overseas and thematic
  sub-databases, depending on institutional subscriptions
time_span:
  start: 1990
  end: ongoing
  coverage_note: The starting year of each sub-library, table and field is different, and 1990 cannot be used to represent
    all modules.
  last_confirmed_release: ongoing
  last_checked: '2026-07-10'
frequency:
- daily
- monthly
- quarterly
- annual
- event
sample_size: A complete sample of China's A-share listed companies and securities history; special libraries such as figures,
  patents, and green economy cover different objects and years.
key_variables:
- Stock Returns and Transactions
- Three financial statements and financial indicators
- Equity structure
- corporate governance
- Board of Directors and Executive
- Analyst forecasts
- Mergers and Acquisitions
- Violation penalties
- bank loan
- Bonds and Funds
- Patents and innovation
- ESG and green economy
research_fit:
  best_for:
  - Research on finance, corporate governance, accounting and capital market events of Chinese listed companies
  - Requires company-year panel with standardized ticker, financial statements, and governance topic tables
  - Connect listed companies with CSMAR topic sub-databases such as patents, violations, character characteristics, etc.
  choose_over:
  - When focusing on academic table structure, corporate governance and accounting topics, they are usually given priority
    over Wind.
  - When focusing on real-time market conditions, macro high-frequency, bond terminals and APIs, Wind is usually preferred.
  - ASIF/Business Registration data should not be used as a substitute when studying unlisted industrial companies
  not_good_for:
  - Overall representative study of unlisted small and medium-sized enterprises
  - Promise that a certain topic can be downloaded without confirming the institution's specific order for the sub-database.
  - Household or individual research
  needs_join_for:
  - Original records of corporate pollution, customs transactions or non-CSMAR patents must be externalized by company name/unified
    code
  variation_available:
  - Listed company long panel
  - daily market events
  - Changes in policy rules
  - Corporate Governance and Personal Changes
good_for:
- Corporate governance, board monitoring, executive characteristics and firm performance
- Corporate DID/incident research on anti-corruption, subsidies, regulation and capital market opening
- Stock returns, financial reporting quality, analyst and institutional investor research
- Research on Innovation, ESG, Non-compliance and Financing Constraints of Listed Companies (depending on subscription module)
identification:
- Firm and year fixed effects
- DID (Policy/Eligibility/Inclusion)
- event study
- RD (rule threshold)
- IV (industry or regional impact)
linkable_keys:
- Stock code
- Securities code
- Full company name
- Unified social credit code
- Personnel name
- Announcement date
joins:
- target: wind
  relation: substitute-and-benchmark
  keys:
  - Stock code
  - Date
  method: exact
  evidence_status: routinely-used
- target: china-patents
  relation: complement
  keys:
  - Full company name
  - Unified social credit code
  method: deterministic-plus-fuzzy
  evidence_status: literature-used
- target: china-land-transaction
  relation: complement
  keys:
  - Full company name
  method: fuzzy-name-match
  evidence_status: plausible
access_routes:
- route: institutional-web
  access_status: available-with-subscription
  direct_url: https://data.csmar.com/
  requirements: School/institution subscription; usually access on campus network, VPN, WebVPN, Shibboleth or OpenAthens environment,
    and register a personal account.
  steps:
  - First check the CSMAR resource page of the school library to confirm the access method and purchased sub-library.
  - Go to data.csmar.com and complete your institutional identification/personal login.
  - Locate data by series, database, category and table in Data Center -> Single Table Query.
  - Set the stock/company code, time and fields, and export to Excel/CSV/TXT after previewing.
  deliverable: Table-level data in subdatabases purchased by the institution; subdatabases not purchased may only be able
    to view fields or may need to be purchased separately.
  cost: paid
  last_checked: '2026-07-10'
- route: wrds
  access_status: available-with-subscription
  direct_url: https://wrds-www.wharton.upenn.edu/
  requirements: Institutions subscribe to WRDS and the corresponding CSMAR library at the same time.
  steps:
  - Check CSMAR permissions from WRDS.
  - Query and export according to the WRDS table structure.
  deliverable: Some of the CSMAR stock, financial, governance and other databases provided by WRDS are not all modules.
  cost: paid
  last_checked: '2026-07-10'
access:
  url: https://data.csmar.com/
  cost: paid
  license: Institutional subscription; restricted to authorized users and authorized uses, no redistribution
  format:
  - xlsx
  - csv
  - txt
  - database-feed
  api: true
  how_to_get: First confirm the purchased module and off-campus access method through the school library; log in to data.csmar.com,
    select the series/database/table in the data center - single table query, set the code, time and fields and export.
caveats: The sub-pools purchased by institutions vary widely. When answering specific ideas, suggested modules/table families
  must be given, and users must be reminded to check the school's permissions first; CSMAR cannot be used as a single table
  where all variables are naturally available.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Cai, Jiang & Kang (2023), Remote Board Meetings and Board Monitoring Effectiveness: Evidence from China'
  journal: RFS
  year: 2023
  dataset_role: Corporate governance, board meetings, director dissent and CEO departures
  evidence_type: paper_data_description
  evidence_url: needs-verification
  data_note: Study remote board meetings and oversight effectiveness.
- cite: Fang, Lerner, Wu & Zhang (2023), Anticorruption, Government Subsidies, and Innovation
  journal: Management Science
  year: 2023
  dataset_role: Listed company subsidies and finance; joining with CNIPA patents
  evidence_type: paper_data_description
  evidence_url: needs-verification
  data_note: Anti-corruption impact, subsidy allocation and innovation.
- cite: 'Shan & Chen (2025), Valuing Reform: How China''s Stock Connect Programs Correct Firm Mispricing'
  journal: CER
  year: 2025
  dataset_role: Listed Company Transactions and Financial Results
  evidence_type: abstract_only
  evidence_url: needs-verification
  data_note: Shanghai-Shenzhen-Hong Kong Stock Connect and mispricing.
provenance:
- source: https://data.csmar.com/
  field_scope:
  - provider
  - access
  - query_workflow
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://lib.ecnu.edu.cn/91/f1/c38585a496113/page.htm
  field_scope:
  - institutional_access
  - module_variation
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://file.csmar.com/group1/M00/AA/99/CuIKV2XAnKiABeLbAB4nDGC5Ano840.pdf
  field_scope:
  - query_steps
  - export_formats
  added: '2026-07-10'
  confidence: high
  verified: true
related_datasets:
- id: wind
  relation: substitute-and-benchmark
- id: china-patents
  relation: complement
- id: asif
  relation: complement
---

## Positioning in one sentence

CSMAR is the main academic database for research on finance, accounting and governance of Chinese listed companies. It is not a table, but a collection of a large number of series, sub-databases and data tables; whether specific research can be done depends on which module the institution subscribes to and which year the module actually covers.

## idea selection rules

- List of listed corporate governance, financial statements, directors and senior management, violations and academic topics: give priority to CSMAR.
- High frequency market, bond terminal, macro high frequency and programmatic interface: compare Wind simultaneously.
- Unlisted manufacturing, customs transactions, corporate pollution: CSMAR cannot replace ASIF/customs/corporate pollution data.

## Get recipe

First check the CSMAR page of the school library to confirm the purchased sub-library and off-campus access method; then log in to `data.csmar.com`, select series, databases, categories and tables layer by layer from "Data Center -> Single Table Query", set the code, time and fields and then export. When answering the user, try to give the module/table family instead of just saying "Go to CSMAR".
