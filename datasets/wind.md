---
schema_version: 2
catalog_status: grounding
id: wind
name: Wind financial terminal
aka:
- Wind
- 万得
- Wind资讯
- Wind Information
- Wind金融终端
provider: Wind Information Co., Ltd.
china_related: true
domains:
- finance
- accounting
- macro
- firm
- trade
unit_of_observation: Listed companies - daily/quarterly/annual; Macro indicators - monthly/quarterly/yearly; Banks - quarterly/yearly;
  Bonds - days; Fund - Day (Multi-level Structure)
structure: multi-module-panel
geo_granularity:
- Nationwide
- province
- city
- enterprise
- Industry
geography: Mainly Chinese mainland (A-shares/A-bonds/China macro market) + Hong Kong stocks + US Chinese concept + major global
  market indices
time_span:
  start: 1990
  end: ongoing
  last_confirmed_release: ongoing
  coverage_note: The starting years for stocks, bonds, banks, funds, and macro modules vary greatly
  last_checked: '2026-07-10'
frequency:
- daily
- monthly
- quarterly
- annual
sample_size: All A-share listed companies (5000+), all public funds, all A-bonds, and thousands of macro indicators
key_variables:
- Stock Quotes (Daily OHLCV)
- Financial statements (balance sheet/income statement/cash flow statement)
- Earnings forecast
- Analyst reports
- Corporate Governance (Equity/Board of Directors/Executive Roles)
- Mergers and Acquisitions
- IPO data
- Bonds (interest rates/credit spreads/defaults)
- Macro (GDP/CPI/M2/PMI/Trade/Fiscal)
- Industry indicators
- Bank wealth management
- Fund net value/holdings
- Shanghai-Shenzhen-Hong Kong Stock Connect
- Futures options
- Exponential components
- Unanimous expectations
research_fit:
  best_for:
  - High-frequency data from China's capital markets, bonds, banking, and macroeconomics, as well as bulk query via terminal/API
  choose_over:
  - When focusing on high-frequency markets, bonds, macro EDB, and program interfaces, CSMAR is usually prioritized
  - When considering academic governance/accounting topic tables and reproducible table structures, CSMAR is compared
  not_good_for:
  - Non-listed SMEs overall
  - Household personal survey
  - Batch downloads are promised without confirming the institution's terminal/API permissions
  needs_join_for:
  - Non-listed companies, patents, and customs must be externally connected by company name or code
  variation_available:
  - daily market events
  - Corporate and banking panels
  - Macro rose frequency
  - Bond issuance and trading
good_for:
- Financial/Corporate Governance Empirical Evidence for Listed Companies — Asset Pricing, Corporate Finance, and Accounting
  Information Quality
- China's Monetary Policy Transmission and Bank Behavior—Analysis of Bank Balance Sheets (Chen et al. 2018 AER using Wind
  to extract quarterly ARIX of 16 listed banks, etc.)
- China's bond market — credit spreads, local government bonds, urban investment bonds, interest rate term structure
- Capital market responses to macro events—event research, policy shock DID
- Analyst behavior — consensus expectation bias, research report information content
identification:
- Panel Fixed Effect (Enterprise/Industry × Year)
- DID (Policy Event/Rule Change)
- IV (Industry/Macro Shocks)
- event study
- RD
linkable_keys:
- Stock code
- Bond code
- Fund code
- Full company name
- Unified social credit code
access_routes:
- route: institutional-terminal
  access_status: available-with-subscription
  direct_url: https://www.wind.com.cn/
  requirements: Institutions purchase Wind terminals and offer appointments, campus networks, or remote use; Export volume
    and module permissions are contractually required.
  steps:
  - Check the Wind entrance and reservation rules for our school library/finance lab.
  - Position stocks, bonds, banking, or macro modules at the terminal.
  - Save indicator codes, frequencies, units, and export conditions.
  deliverable: Terminal export data of purchased modules by the institution.
  cost: paid
  last_checked: '2026-07-10'
- route: wind-api-edb
  access_status: needs-verification
  direct_url: https://www.wind.com.cn/
  requirements: The account must have Wind API/EDB permissions and install the client; Not all school terminals allow programmatic
    batch calls.
  steps:
  - Confirm API/EDB permissions with the university's resource administrator.
  - Install and authorize the client.
  - Calls and records the measurement definition using indicator codes, dates, and frequencies.
  deliverable: Programmatic data within the scope of authorization; Quotas and concurrency restrictions are subject to the
    contract.
  cost: paid
  last_checked: '2026-07-10'
access:
  url: https://www.wind.com.cn
  cost: paid (institutional subscription, prices close to Bloomberg but lower for Chinese customers)
  license: Institutional subscriptions (most Chinese university libraries have Wind terminals); Some universities offer Wind
    EDB batch download services
  format:
  - xlsx
  - csv
  - api
  api: true (Wind Python, C++, and R APIs; some universities provide Wind EDB)
  how_to_get: '1) View and export via the Wind terminal in your university''s library/finance lab; 2) Wind EDB (Economic Database):
    Frequently ordered by universities, capable of bulk import of economic, industry, and company data via API; 3) Individuals
    purchasing a Wind account (extremely costly, usually about 40,000-50,000 RMB per year).'
caveats: Expensive and requires institutional subscription; Financial data standards occasionally differ from CSMAR/CNRDS
  and need to be reconciled during cross-database consolidation; The Wind interface (API) and Excel plugin versions update
  quickly; Each module started in different years, so for long panels, inspection and coverage are required; Some macro and
  historical data processing methods are not transparent.
quality:
  profile_status: partial
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: Chen, Ren & Zha (2018), The Nexus of Monetary Policy and Shadow Banking in China
  journal: AER
  year: 2018
  data_note: Wind was used to extract quarterly balance sheet data for 16 listed banks (including ARIX—accounts receivable
    investments, used to measure shadow banking assets), from Q1 2009 to Q4 2015
- cite: 'Gao, Ru & Tang (2021), Subnational Debt of China: The Politics-Finance Nexus'
  journal: JFE
  year: 2021
  data_note: Using Wind's chengtou bond data and political association data of local officials, the political-financial interaction
    in local bond issuance was studied
- cite: 'Tian, Tu & Wang (2024), The Real Effects of Shadow Banking: Evidence from China'
  journal: Management Science
  year: 2024
  data_note: Using Wind's entrusted loan data + innovation data from listed companies, it was found that shadow banks correct
    bank credit mismatches through capital reallocation—promoting innovative output among borrowing enterprises
- cite: Liu, Yu, Tang & Chen (2025), External Trade Policy Uncertainty, Corporate Risk Exposure, and Stock Market Volatility
  journal: CER
  year: 2025
  data_note: Using Wind's listed company financial + stock trading data, we study how uncertainty in US-China trade policies
    affects corporate risk exposure and stock price fluctuations
provenance:
- source: openICPSR replication package https://doi.org/10.3886/E113177V1 (supports Wind as a bank-data source used alongside Bankscope)
  added: '2026-07-08'
  confidence: high
  verified: false
- source: Wind official website https://www.wind.com.cn and introduction pages for databases of multiple university libraries
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- csmar
- china-stat-yearbook
---

## Positioning in one sentence
Wind (Wind) is the "Bloomberg terminal" of China's capital markets—covering a full spectrum of financial data from A-shares, bonds, funds, macro, and industries.
It is one of the most widely used commercial databases in Chinese corporate finance, asset pricing, banking, and monetary policy empirical research.
Due to its wide coverage, fast updates, and API interface, it is used as the main data source or complementary to CSMAR by many top journal papers.

## Research questions suitable for answering/Typical identification strategies
- **Corporate Finance and Asset Pricing**: Analysis of capital structure, dividend policy, IPO/SEO, and stock yields—Wind's financial and analytical modules are highly complementary to CSMAR.
- **Banking and Monetary Policy Transmission**: Shadow banking activities on bank balance sheets (such as ARIX), LDR, capital adequacy ratios, etc. (Chen, Ren & Zha 2018 AER constructed the banking dashboard for 2009-2015 using only Wind+ Bankscope).
- **Fixed Income and Credit Risk**: China's Bond Market—Yields, credit spreads, default events for interest rate bonds, credit bonds, and LGFV bonds.
- **Macro Strategies and Industry Rotation**: Research on quantitative strategies linking macro indicators + industry indices + individual stock market trends.
- **Event Research**: Accurately gauge market reactions to M&A/Policy/Regulatory Announcements using stock day quotes + event dates.
- **Not suitable for**: Micro-household or individual level surveys (Wind does not conduct household surveys), non-listed SMEs at the enterprise level (limited coverage).

## Key variables/modules
- **Stock Module**: Market trends (daily/minute), finances (three tables + notes), valuation, share capital structure, consensus expectations, leaderboard
- **Bond Module**: Interest rate bonds, credit bonds, ABS, credit ratings and spreads
- **Macro Module**: National Economic Accounting, Prices, Currency, Trade, Finance, Real Estate (thousands of indicators)
- **Banking Module**: Bank balance sheets, regulatory indicators (capital adequacy ratio/non-performing loan ratio/LDR), wealth management products
- **Fund Module**: Public/Private Equity Net Value, Holdings, Fund Manager
- **Corporate Governance Module**: Board of Directors/Executive/Equity Structure (overlaps with CSMAR but also has strengths)

## How to get
1. **University Wind Terminal (Most Common)**: Most Chinese university libraries and finance labs have Wind terminals, allowing students to book and directly export Excel.
2. **Wind EDB Bulk Download**: Some universities have subscribed to Wind EDB (Economic Database), which can use Python/C++/R APIs to batch pull economic, industry, and company data for large-scale academic research.
3. **Personal Subscription**: Directly purchase an account from Wind (extremely costly, only suitable for funded research groups).

## Connections to other data
- Connect **CSMAR / CNRDS / RESSET** with the "stock code" — data from four Chinese listed companies can be cross-verified (note individual financial differences due to differences).
- Use the "Company Full Name/Unified Social Credit Code" to connect **ASIF / Business Registration Database / Patent Data**.
- Connect **CEIC / Statistical Yearbook** with "Industry Code/Macro Indicator Name" — Wind's macro module overlaps with CEIC but focuses more on capital market relevance.

## Remarks / Pitfalls
- **Differences in Financial Standards**: Wind and CSMAR do not fully align in terms of measurement definition and calculation methods for certain financial indicators (such as R&D expenses and non-recurring gains and losses). When cross-validating multiple databases, it is recommended to use one as the standard for stability.
- **Fast API Version Updates**: The Wind Python API (WindPy) is updated annually, so older code may need to be adapted.
- **Uneven historical coverage**: A-share listed companies started in 1990, but early financial data is incomplete; The bank/bond/fund modules have shorter coverage periods.
- **Weak coverage of unlisted companies**: Wind mainly covers listed companies and bond-issuing companies, with limited information on non-listed SMEs.
