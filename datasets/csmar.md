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
  evidence_status: literature-used
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
- cite: 'Guo, He, Ren & Zhang (2026), Digital Transformation and Climate Transition Risk Management: Evidence from Chinese Listed Firms'
  doi: https://doi.org/10.1016/j.chieco.2026.102732
  journal: CER
  year: 2026
  dataset_role: Main firm-level panel; CSMAR digital transformation index and financial data, 2011-2021
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000829
  data_note: Uses CSMAR's multi-dimensional Digital Transformation Index (DTI) and A-share listed firm financials to study how digital maturity affects climate transition risk management. Identification via staggered DiD using National Big Data Comprehensive Experimental Zones.
- cite: 'Yang, Wan & Yang (2026), How Polluting Enterprises Respond to Pigovian Tax: Evidence from China''s Environmental Protection Tax Law'
  doi: https://doi.org/10.1016/j.chieco.2026.102742
  journal: CER
  year: 2026
  dataset_role: A-share listed firm financial and pollution data 2008-2021; main firm-level outcomes
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000738
  data_note: >-
    Uses CSMAR A-share heavy-polluting industry listed firms (2008-2021) to analyze how the 2018 Environmental Protection Tax Law (Pigovian tax) affects enterprise pollution behavior. Finds significant pollution reduction especially for wastewater. Identifies three-stage response — source prevention, process modification, and end-of-pipe treatment. Enterprises primarily rely on green utility-model innovation rather than substantive invention. Effect weakens gradually over time.
- cite: 'Author (2025), Industrial Robots, Resource Misallocation, and Firm Innovation Performance: Evidence From China'
  doi: https://doi.org/10.1111/jors.70035
  journal: JRS
  year: 2025
  dataset_role: CSMAR A-share listed manufacturing firm panel 2011-2019; firm financials and innovation
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/bla/jregsc/v66y2026i2p399-425.html
  data_note: >-
    Abstract/bibliographic level only, downgraded on 2026-08-13: the RePEc record
    confirms the paper identity and states the combined use of CSMAR firm data, IFR
    industry-level robot adoption and CNRDS/SIPO patent records for Chinese listed
    manufacturing firms (2011-2019). The paper's data section was not read when this
    entry was recorded, so the exact CSMAR module and variables are not verified from
    the paper itself; the finding summary is abstract-derived and the author names
    remain unresolved in this record. Do not treat this entry as data-section
    evidence.
- cite: 'Li & Branstetter (2024), Does "Made in China 2025" Work for China? Evidence from Chinese Listed Firms'
  doi: https://doi.org/10.1016/j.respol.2024.105009
  journal: Research Policy
  year: 2024
  dataset_role: CSMAR firm financials, government subsidies (innovation vs non-innovation), and R&D expenditure
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733324000581
  data_note: Uses CSMAR listed firm data (2015-2018) with DiD, panel event study, and CEM matching to test whether MIC 2025 increased targeted firms' innovation. Text-searches annual reports for MIC 2025 mentions (~1,120 potential beneficiaries). Finds subsidies and R&D intensity increased but no significant improvement in patenting or productivity.
- cite: 'Hua, Wang, Xia & Zhang (2025), Industrial Policy, Congruence, and Innovation: Evidence from "Chinese NASDAQ"'
  doi: https://doi.org/10.1016/j.respol.2025.105298
  journal: Research Policy
  year: 2025
  dataset_role: CSMAR NEEQ-listed firm financial data 2013-2019; firm balance sheets and financial variables
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0048733325001271
  data_note: Uses CSMAR firm financial data for NEEQ (新三板) listed companies (2013-2019, 88 two-digit industries) combined with Wind, CNIPA/Incopat patents, tax records, census, and city statistics. Introduces "congruence" — the match between firm factor input structure and local factor endowments — finding positive congruence-innovation relationship that MIC 2025 weakens by increasing bank leverage.
- cite: 'Shi & Zhang (2025), Short Technology Cycle Time and Firm Innovation: Evidence from China'
  doi: https://doi.org/10.1016/j.respol.2025.105305
  journal: Research Policy
  year: 2025
  dataset_role: CSMAR A-share listed firm financial data for 3,079 firms (1990-2022)
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733325001349
  data_note: Uses CSMAR financial data for 3,079 A-share listed firms (1990-2022) combined with CNIPA patents and CNRDS. Constructs technology cycle time (TCT) from patent backward citations. Finds shorter TCT significantly boosts firm innovation (~1.1% per unit TCT decrease), with stronger effects for private firms, high-competition industries, and early-lifecycle firms. Human capital and R&D intensity positively moderate.
- cite: 'He & Lyu (2025), Export Controls and Innovation Transfer within Chinese Business Groups: Evidence from the U.S. Entity List'
  doi: https://doi.org/10.1016/j.respol.2025.105311
  journal: Research Policy
  year: 2025
  dataset_role: CSMAR A-share listed firm financials and group equity structure data 2010-2022
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733325001404
  data_note: Uses CSMAR data for A-share listed firms (2010-2022) combined with incoPat patent data and BIS U.S. Entity List information. Multi-period DiD finds indirectly-affected firms in sanctioned business groups increase invention patent applications by 19.62% through intra-group patent transactions and capital/talent reallocation. Documents innovation transfer as structural reallocation within business groups rather than net increase.
- cite: 'Zhang, Bai, He & Guo (2026), Greening but Concentrating? The Unintended Effects of China''s Voluntary Participatory Environmental Regulations on Firms'' Innovation Portfolios'
  doi: https://doi.org/10.1016/j.respol.2026.105531
  journal: Research Policy
  year: 2026
  dataset_role: CSMAR Chinese listed manufacturing firm data; patent-based innovation portfolios
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733326001228
  data_note: Uses CSMAR listed manufacturing firm data in a multi-period DiD with double/debiased machine learning to study China's Green Factory certification. Finds green knowledge recombination creation increases (+0.029) and reuse increases (+0.135), but non-green creation is crowded out (-0.031). Market competition mitigates crowding-out while media attention amplifies it.
- cite: 'Yu, Zheng & Liu (2026), Digital Innovation as a Bank Risk Mitigator: Empirical Insights from Chinese Commercial Banks'
  doi: https://doi.org/10.1016/j.respol.2026.105501
  journal: Research Policy
  year: 2026
  dataset_role: CSMAR bank-level financial data for 391 Chinese commercial banks (2009-2018, 2,370 bank-year obs)
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0048733326000922
  data_note: Uses CSMAR bank financial data combined with CNIPA digital patent records, Wind, and BankFocus for 391 banks (2009-2018). Constructs a hand-collected five-dimensional digital innovation index from bank patents. Finds digital innovation reduces both default and operating risk through market discipline and market power channels. Stronger for non-SOEs and banks in regions with stronger legal enforcement.
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
