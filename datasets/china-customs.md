---
schema_version: 2
catalog_status: grounding
id: china-customs
name: China Customs Trade Statistics (CCTS)
aka:
- 中国海关数据库
- 海关数据
- 海关进出口
- China Customs
- CCTS
- 海关交易级数据
- 中国海关贸易统计
provider: General Administration of Customs of China; researchers often obtain the processed version through the EPS
  China Microeconomic Data Query System
china_related: true
domains:
- trade
- IO
- firm
- development
- macro
unit_of_observation: Enterprise-Product-Import and Export Country-Transaction (at the level of customs declaration, which
  can be summed up to Enterprise-Year/Product-Year)
structure: transaction-records
geo_granularity:
- enterprise
- City (customs port)
- province
- country
geography: All import and export customs declaration transactions in mainland China; counterparties cover countries around
  the world
time_span: 2000–2017 (different platform versions vary slightly, core range 2000–2016)
frequency:
- monthly
- annual
sample_size: Approximately 10-20 million transaction records per year (approximately 300,000-500,000 import and export companies
  per year)
key_variables:
- Company name
- Enterprise customs code
- Import and export marking (import/export)
- HS 8-bit code (product)
- Trade volume (USD)
- Trade volume (quantity + unit)
- Country of origin/country of destination
- Trade method (general trade/processing with supplied materials/processing with imported materials, etc.)
- Transportation method
- transit country
- customs port
- Business address/phone/zip code (partial years 2000–2006)
good_for:
- An Empirical Analysis of Enterprise Export Behavior and Export Dual Margin (Expanded Margin/Intensive Margin)
- The impact of trade liberalization (WTO accession/tariff reduction/trade war) on the import and export of Chinese enterprises
- Calculation of corporate global value chain participation (DVAR/upstream degree/domestic value added rate)
- Differentiated behaviors between processing trade and general trade - export product quality, imported intermediate goods
  effect
- 'After joining with the enterprise database: the relationship between exports and enterprise productivity (TFP), wages,
  and innovation'
- The impact of Sino-US trade policy uncertainty and anti-dumping sanctions on Chinese enterprises’ exports
identification:
- Panel fixed effects (firm × year)
- DID (Tariff/Policy/Trade War)
- IV (tariff changes/exchange rate shocks/geographical distance)
- Natural experiment (joining the WTO)
linkable_keys:
- Company name
- Enterprise customs code
- Postal code
- phone number
- HS code (matching industry/tariff)
research_fit:
  best_for:
  - Extended/intensive margin, product quality and global value chain measures of firm-product-destination trade
  - The impact of tariffs, trade policies and destination demand shocks on corporate exports
  choose_over:
  - Choose customs data when enterprise-product-country transaction levels and trade methods are required, rather than just
    using yearbooks or macro trade statistics
  - Join customs data with ASIF, patent or industrial and commercial data when business productivity, wages or innovation
    results are needed
  not_good_for:
  - Services trade and purely domestic transactions
  - Household consumption, education or health outcomes
  - Business financial and productivity results without additional matching
  needs_join_for:
  - Enterprise productivity, wages, innovation and exit results need to match ASIF/patent/business data
  - Tariff and policy impacts need to be joined by HS, destination and year
  variation_available:
  - Enterprise × Year × HS Product × Destination Transaction
  - Annual and partial monthly records from 2000–2017
  - Changes in HS codes, trade methods, destinations and tariff policies
access:
  url: http://microdata.sozdata.com (EPS China Microeconomic Data Query System, institutional subscription); Original data
    must be applied for with the General Administration of Customs
  cost: PAID (university libraries often have subscriptions)
  license: Institutional subscription (IP certification + personal account), academic research only
  format:
  - csv
  - dta
  - xlsx
  api: false
  how_to_get: 1) Through the library of your university → China Microeconomic Data Query System (EPS) → Customs Enterprise
    Database Module, select the year/variable to export; 2) Original transaction-level data requires formal application from
    the General Administration of Customs (high threshold); 3) Processed versions of some years can be obtained at CNRDS.
caveats: 'The amount of transaction-level data is huge and needs to be cleaned: the missing company name rate is 0–15% (depending
  on the year), trade intermediaries need to be filtered (according to the method of Ahn et al. 2011), HS coding version changes
  need to be aligned (1996/2002/2007/2012), and the measurement definition of processing trade is different from that of general trade. Excludes
  service trade. There are differences in import and export record formats.'
access_routes:
- route: EPS processed customs module
  access_status: available-with-subscription
  direct_url: http://microdata.sozdata.com/
  requirements:
  - Subscriptions from universities or research institutions
  - Institutional IP certification or personal account
  - Comply with database license terms
  steps:
  - Confirm EPS subscription through your institutional library
  - Enter the customs enterprise database module of China’s microeconomic data query system
  - Select the year, import and export direction, HS level and variables
  - Export in batches and record filter conditions
  deliverable: Processed firm- and transaction-level data supplied by the platform; fields, years, and export limits depend on the subscribed module
  cost: paid
  last_checked: '2026-07-10'
- route: Original customs data application
  access_status: needs-verification
  direct_url: https://www.customs.gov.cn/
  requirements:
  - formal research project
  - Relying institution
  - Submit the required application and accept the General Administration of Customs data-security and confidentiality conditions
  steps:
  - Confirm target year, transaction level and variable requirements
  - Confirm the current application channel with the General Administration of Customs or an authorized route
  - Submit research description and data security plan
  - Receive or use the data in the designated environment within the approved scope
  deliverable: Approved raw or de-identified customs data; immediate public download should not be expected
  cost: by-application
  last_checked: '2026-07-10'
quality:
  profile_status: partial
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Kee & Tang (2016), Domestic Value Added in Exports: Theory and Firm Evidence from China'
  journal: AER
  year: 2016
  dataset_role: Customs transaction data as the export-transaction component for estimating the domestic value-added ratio of Chinese exports
  evidence_type: article_and_replication
  evidence_url: https://www.aeaweb.org/articles?id=10.1257/aer.20131687
  data_note: Combines firm-level and customs transaction data to estimate the domestic value-added ratio of Chinese exports
- cite: 'Zhang, Liu & Wei (2023), Digital Product Imports and Export Product Quality: Firm-level Evidence from China'
  journal: CER
  year: 2023
  dataset_role: Customs transaction data as the import-export transaction input for studying how digital-product imports affect export product quality
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v79y2023ics1043951x23000664.html
  data_note: Combines customs transactions with firm data to study how digital-product imports affect export product quality
- cite: Zhang & Zhou (2023), Quota Removal, Destination-Specific Export Shocks, and Skill Acquisition in China
  journal: JDE
  year: 2023
  dataset_role: China Customs export transaction data as the source of destination-specific export shocks (with quota cancellation) for studying effects on skills training and education investment
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v165y2023ics0304387823001049.html
  data_note: Use China Customs export transaction data + quota cancellation as exogenous shocks to study how export destination-specific
    demand shocks affect corporate skills training and education investment
- cite: 'Handley & Limão (2017), Policy Uncertainty, Trade, and Welfare: Theory and Evidence for China and the United States'
  journal: AER
  year: 2017
  dataset_role: Firm-product-destination export transaction data for measuring trade policy uncertainty effects
  evidence_type: data-section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257/aer.20141419
  data_note: Used China Customs transaction-level export data (2000–2006) to estimate the impact of WTO accession and trade policy
    uncertainty reduction on Chinese export entry, volume, and prices. Shows that TPU reduction accounts for substantial export
    growth to the US, with heterogeneous effects across products and firm types.
- cite: 'Long & Fan (2026), Can Green Mergers and Acquisitions Drive Firms'' Transition to Green Exports? Evidence from China''s Manufacturing Sector'
  doi: https://doi.org/10.1016/j.chieco.2026.102738
  journal: CER
  year: 2026
  dataset_role: Chinese Customs transaction records 2007-2016; main export outcome matched to CSMAR listed manufacturing firms
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000544
  data_note: Matches Customs export transaction records (2007-2016) with A-share listed manufacturing firms to study how green M&As affect green product exports. Proposes a technology-qualification framework where green M&As promote green export entry and continuity through green innovation and environmental legitimacy. Finds stronger effects for firms with higher operational efficiency, weaker green foundation, private ownership, and processing trade.
- cite: 'Mo & Zhang (2024), Neighboring Capital Imports and Non-Importer Productivity: Evidence from Geocoded Manufacturing Firms in China'
  doi: https://doi.org/10.1016/j.jue.2024.103692
  journal: JUE
  year: 2024
  dataset_role: Customs import transaction data matched with ASIF geocoded firm panel (2000-2006)
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0094119024000627
  data_note: Uses geocoded ASIF-Customs matched firm panel (2000-2006) with NLP product description-HS code matching. Finds neighboring firms' capital goods imports within 10km generate significant TFP spillovers to non-importing firms — raising non-importer productivity by 0.99% on average, six times the productivity gain from own R&D. Spillovers operate through supply-chain linkages (upstream-downstream capital goods) and decay beyond 10km.
- cite: 'Hau & Ouyang (2024), Can Real Estate Booms Hurt Firms? Evidence on Investment Substitution'
  doi: https://doi.org/10.1016/j.jue.2024.103695
  journal: JUE
  year: 2024
  dataset_role: Customs trade transaction data matched with ASIF; firm-level exports/imports
  evidence_type: data-section
  evidence_url: https://ideas.repec.org/a/eee/juecon/v144y2024ics0094119024000652.html
  data_note: Uses Customs trade data matched with ASIF manufacturing firms (~900K firms, 2002-2007) to study how real estate booms crowd out firm productive investment. Combined with 172 city-level housing price and land supply data. Exploits exogenous variation in residential land supply as IV for housing prices — finds real estate price increases divert firm resources from capital investment and R&D toward real estate.
- cite: 'Huang, Jia & Ge (2024), Forced to Innovate? Consequences of United States'' Anti-Dumping Sanctions on Innovations of Chinese Exporters'
  doi: https://doi.org/10.1016/j.respol.2023.104899
  journal: Research Policy
  year: 2024
  dataset_role: China Customs firm-level export data to the US (HS 8-digit); matched with WTO anti-dumping case data
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S004873302300183X
  data_note: Uses Customs transaction data (HS 8-digit, 2000-2009) matched with WTO anti-dumping case records to identify targeted Chinese exporters. Combined with ASIF firm data and CNIPA patents. DiD finds that firms hit by US anti-dumping duties significantly increase invention patent output — sanctions act as a "forced innovation" shock. Effect is stronger during China's 2006 pro-innovation policy period.
- cite: 'Wang, Wu & Wu (2025), Export Slowdown and Increasing Land Supply: Local Government''s Responses to Export Shocks in China'
  doi: https://doi.org/10.1016/j.jue.2025.103796
  journal: JUE
  year: 2025
  dataset_role: City-year export panel and HS-8 product exports used to measure export shocks and construct a leave-one-out Bartik instrument
  evidence_type: data_section_and_working_paper
  evidence_url: https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf
  data_note: The paper's data section states that the full GACC export sample is aggregated from raw customs records to national HS-8 totals and then to city-year HS-8 exports for 2007-2017, covering 326 prefecture-level cities. The recorded paper uses these aggregates, not a downloadable replacement for the underlying transaction database; the paper-specific cleaning code and current GACC microdata access remain separate questions.
provenance:
- source: Crossref abstract for https://doi.org/10.1257/aer.20131687 (supports use of firm- and customs transaction-level data)
  added: '2026-07-08'
  confidence: high
  verified: false
- source: EPS China Microeconomic Data Query System http://microdata.sozdata.com and university-library database descriptions
  added: '2026-07-08'
  confidence: high
  verified: true
- source: Wang, Wu & Wu (2025) working-paper data section https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf and JUE DOI https://doi.org/10.1016/j.jue.2025.103796
  field_scope:
  - GACC source identity
  - HS-8 aggregation
  - 2007-2017 period
  - 326-city panel role
  added: '2026-08-12'
  confidence: high
  verified: true
related_datasets:
- asif
- china-patents
- china-stat-yearbook
---

## Positioning in one sentence
The China Customs Import and Export Database is a record of all import and export declaration transactions in China, covering 2000-2017 and tens of millions of transactions each year.
It is the core micro-data for studying international trade, enterprise heterogeneity and global value chains**. After joining with the industrial enterprise database (ASIF),
It constitutes the "golden partner" of China's empirical trade research - relied on by almost every top international trade paper using Chinese enterprise data.

## Research questions suitable for answering/Typical identification strategies
- **Dyadic Margin of Firms’ Exports**: Export participation (extended margin) vs. export intensity (intensive margin)—how tariff/exchange rate changes drive firms’ export adjustments.
- **Global Value Chain and Domestic Value Added (DVAR)**: Use the distinction between processing trade/general trade + enterprise imported intermediate product information to measure the domestic value added rate and upstream degree at the enterprise level (Kee & Tang 2016 AER approach).
- **Enterprise-level identification of trade liberalization**: Make use of cross-industry differences in tariff reductions before and after WTO accession, or the decline in trade policy uncertainty (TPU), to conduct DID/IV identification.
- **Trade War/Anti-dumping**: Use the changes in the U.S. anti-dumping tax rate against China to identify the impact of trade barriers on corporate export behavior.
- **Imported intermediate goods and productivity**: Study import competition and learning effects through changes in the types/source countries of enterprises’ imported intermediate goods.
- **Not suitable for**: service trade, domestic trade, exports after 2017 (the public version ends in about 2017), macro trade issues that do not require product-destination country details (just look for the Statistical Yearbook/TRAINS).

## Key variables/modules
- Transaction basis: company name/customs code, import and export mark, HS 8-digit code, trade volume (USD), quantity, unit price
- Trade model: general trade / processing with supplied materials / processing with imported materials / bonded warehouse, etc.
- Geography: country of destination/country of origin, transit country, customs port (city)
- Company information: Company name, address (partial years), phone number/postal code (2000–2006 only)

## How to get
1. **The most trouble-free**: Access the "China Microeconomic Data Query System" (EPS, microdata.sozdata.com) through the library of your university, enter the "Customs Enterprise Database" module, select the year/variables/filtering conditions and directly export csv/dta.
2. **Original data**: Applying to the General Administration of Customs requires formal research project establishment and confidentiality agreement (long cycle, high threshold).
3. **Third party**: CNRDS provides processed versions for some years, which can be purchased together with industrial enterprise data.

## Connections to other data
- **With ASIF (Industrial Enterprise Database)**: Use "enterprise name + zip code + phone" multi-key matching (Brandt et al. 2012 / Upward et al. 2013 method), which is a standard connection for empirical trade research. ——This is the "vertebral level connection" of China's empirical research.
- **With patent data (CNIPA)**: Use "company name" matching to study the impact of trade on corporate innovation.
- **With HS code→Industry/Tariff**: Use HS code to correspond to industry classification (GB/T)→connect input-output table or tariff data.
- **With industrial and commercial registration database**: Use "Company Name/Unified Social Credit Code" to obtain basic information of the enterprise.

## Remarks / Pitfalls
- **Cleaning is a compulsory course**: The missing company name rate fluctuates from year to year (0–15%), and records with no name/no HS code/no transaction amount must be cleared.
- **Trading intermediaries**: About 20–30% of exports are conducted through intermediaries. According to the method of Ahn, Khandelwal & Wei (2011), they are marked and filtered with keywords such as "import and export/trade/economic trade/foreign economic" in the company name.
- **HS coding version switching**: 1996 / 2002 / 2007 / 2012 four versions. When making long panels, UN SD comparison table needs to be used for alignment.
- **Processing trade import tax exemption**: Processing trade enterprises import intermediate goods free of tariffs, so their import behavior is essentially different from that of general trade enterprises, and must be distinguished when studying the effects of tariffs.
- **Excluding service trade**: The import and export of services are not included in the customs declaration system.
