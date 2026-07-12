---
schema_version: 2
catalog_status: ready
id: china-stat-yearbook
name: China Statistical Yearbook System (including statistical yearbooks at national/provincial/municipal/county levels)
aka:
- 统计年鉴
- 中国统计年鉴
- 省统计年鉴
- 市统计年鉴
- China Statistical Yearbook
- China City Statistical Yearbook
- NBS年鉴
- 中国城市统计年鉴
- 中国县域统计年鉴
provider: National Bureau of Statistics (NBS) and provincial/municipal statistical bureaus
china_related: true
domains:
- macro
- development
- public
- labor
- trade
- finance
- demography
- IO
unit_of_observation: National/provincial/city/county-year (aggregated statistics, not micro)
structure: aggregate-panel
geo_granularity:
- Nationwide
- province
- prefecture-level city
- County (some indicators)
geography: All provinces + prefecture-level cities + some districts and counties in mainland China
time_span:
  start: 1981
  end: ongoing
  last_confirmed_release: 2025
  coverage_note: Different yearbooks of the country, province, city, and county have different starting years and latest release
    years.
  last_checked: '2026-07-10'
frequency:
- annual
sample_size: N/A (aggregated full statistics)
key_variables:
- GDP (total/growth rate/per capita/by industry)
- Population (total number/birth rate/mortality rate/urbanization rate/sex ratio)
- Employment (number of employees/registered urban unemployment rate/wage/employment by industry)
- Finance (local fiscal revenue/expenditure/transfer payment; government debt measurement definition and level need to be verified table
  by table)
- Investment and construction (fixed asset investment/real estate investment/construction area)
- Industry (industrial added value/main product output)
- Trade (import and export volume/foreign investment utilization)
- Price Index (CPI/PPI/House Price Index)
- Household income and expenditure (per capita disposable income/consumption expenditure)
- Education (number of schools/enrolled students/teacher-student ratio)
- Health (number of hospitals/number of beds/number of doctors)
- Technology (R&D expenditure/number of patents)
- Energy and Environment (Energy Consumption/Carbon Emissions/Air Quality)
- Transportation (road mileage/railway mileage/freight volume)
research_fit:
  best_for:
  - Provincial/city/county annual macro panel, regional results of policy DID and control variables
  choose_over:
  - Prioritize over micro-surveys when regional annual aggregate indicators are needed
  - Cannot replace micro-level data such as CFPS/ASIF when individual, household or firm heterogeneity is required
  not_good_for:
  - High Frequency Daily/Monthly Research
  - Precise business or personal mechanism
  - City panels that do not check the city/municipal district measurement definition
  - Research on city/county local government debt, implicit debt or urban investment bonds without table-by-table verification
  needs_join_for:
  - Policy time points, enterprise or survey data need to be joined through administrative division codes and years.
  variation_available:
  - Regional year-to-year changes
  - Differences in administrative levels
  - Local policy staging
  topics:
  - local finance
  - public service
  - Education expenditure
  - medical expenditures
  - Local debt (need to be verified table by table)
  - Broadband China (requires external policy list)
good_for:
- DID of prefecture-level city/provincial-level policy impacts—using statistical yearbooks to construct explained variables
  (GDP/employment/pollution) and control variables
- China’s economic growth accounting and convergence—provincial/municipal level GDP, capital stock, TFP measurement and beta
  convergence test
- Fiscal decentralization and local government behavior - measures of fiscal revenue and expenditure, land finance and transfer
  payment dependence; debt ratios are only used when specific yearbook tables and levels are verified
- Urbanization and urban system - Empirical characterization of urban size distribution (Zipf's law) and urban agglomeration
  growth
- Environmental Kuznets Curve - Test of the inverted U-shaped relationship between provincial/municipal economic growth and
  pollution
- Infrastructure and economic growth - the causal effect of road/rail density on regional economic growth (DID+IV)
identification:
- Panel fixed effects (province/city/year)
- DID (policy by region/year)
- IV (Geographical/Historical Instrumental Variables)
- RD
- synthetic control method
linkable_keys:
- Provincial code
- City code
- County code (GB/T 2260 administrative division code)
- Industry code
access_routes:
- route: nbs-public
  access_status: available
  direct_url: https://data.stats.gov.cn/
  requirements: None
  steps:
  - Enter the National Bureau of Statistics data platform.
  - Select annual data/region/metric.
  - Download or export the form and record the measurement definition.
  deliverable: Countries and some regions make public aggregate indicators.
  cost: free
  last_checked: '2026-07-10'
- route: local-yearbooks
  access_status: available-with-fragmentation
  direct_url: https://www.stats.gov.cn/
  requirements: Search electronic yearbooks from provincial and municipal statistical bureaus; format and historical coverage
    are not uniform.
  steps:
  - Positioning corresponds to the local statistics bureau.
  - Enter the Statistical Yearbook/Statistical Data section.
  - Download Excel or PDF and record the table name, units and measurement definition.
  deliverable: Local yearbook form or PDF.
  cost: free
  last_checked: '2026-07-10'
access:
  url: https://data.stats.gov.cn (National Bureau of Statistics Data Query Platform); Websites of provincial/municipal statistics
    bureaus; and other university subscription databases such as EPS Data Platform
  cost: mixed
  license: Government public data, free to use, source required
  format:
  - xlsx
  - csv
  - PDF (Scanned Yearbook)
  api: false
  how_to_get: 1) National Bureau of Statistics data.stats.gov.cn → 'Annual Data' or 'Statistical Yearbook' → Select the year/region/indicator
    → Download Excel; 2) Provincial/municipal Bureau of Statistics website → Electronic version of the respective statistical
    yearbook; 3) EPS/CNKI statistical database (university subscription) → Batch download panel format. The most trouble-free
    thing is to use the 'China City Database' and 'China County Database' modules of EPS Data Platform, which have been organized
    into a panel format.
caveats: The measurement definitions of prefecture-level city and county-level data in different yearbooks are not completely consistent
  - for example, the 'municipal district' measurement definition vs. the 'city' measurement definition. Some indicators have measurement definition changes between years
  (such as adjustments to GDP accounting methods around 2012). Inadequate coverage of county-level indicators (many indicators
  only cover prefecture-level cities). Local government debt, implicit debt and urban investment bonds are not automatically
  guaranteed to be continuous city/county panels by this article. The release level, debt measurement definition and deficiencies must be
  checked table by table. There is a lot of missing data in remote areas such as Tibet and Xinjiang. The statistical standards
  of local yearbooks may differ from national standards.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Wu, Yu & Zhang (2023), Road Expansion, Allocative Efficiency, and Pro-Competitive Effect of Transport Infrastructure:
    Evidence from China'
  journal: JDE
  year: 2023
  dataset_role: Urban road and area control variables; joined with ASIF firm results
  data_note: Use China's prefecture-level city road infrastructure data (statistical yearbook/traffic yearbook) + industrial
    enterprise database to study the impact of highway expansion on resource allocation efficiency and competition promotion
- cite: 'Cao, Ni & Guo (2025), Broadband Internet and Income Inequality among the Floating Population: Evidence from the ''Broadband
    China'' Strategy'
  journal: CER
  year: 2025
  dataset_role: Urban broadband/ICT and macro control; joining with CMDS
  data_note: Using the China Urban Statistical Yearbook (broadband coverage/ICT infrastructure) + CMDS floating population
    data, and using the 'Broadband China' policy as DID, we study the impact of Internet infrastructure on the income inequality
    of the floating population.
provenance:
- source: National Bureau of Statistics https://data.stats.gov.cn (supports the yearbook system and data-query functions)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: EPS China city/county database introduction page (confirm the university subscription to obtain the panel format
    compiled version)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- china-census
- china-io-table
- china-air-quality-monitoring
---

## Positioning in one sentence
The China Statistical Yearbook system is an annual administrative summary data released by the National Bureau of Statistics and local statistical bureaus at all levels——
From GDP to birth rate to industrial output to fiscal revenue and expenditure, covering the four levels of the country/province/city/county,
It is "infrastructure-level" data that cannot be bypassed in China's macroeconomics, regional economy, public finance and urban research.
Almost every empirical paper that uses prefecture-level or provincial-level panels in China,
The explained variables and control variables are directly or indirectly derived from statistical yearbooks.

## Research questions suitable for answering/Typical identification strategies
- **DID of prefecture-level city panels**: Statistical yearbooks are a common source for constructing explained variables (GDP growth rate, fiscal revenue and expenditure, pollution emissions, school enrollment rate) of prefecture-level cities - use city codes to match policy time points, and do standard DID or staggered DID.
- **Empirical evidence of economic growth**: Provincial/municipal GDP + capital formation + labor force + human capital → do growth accounting, beta convergence or Barro-type growth regression.
- **Measurement of "land finance"**: Use land transfer revenue (fiscal yearbook or land and resources yearbook) + local fiscal revenue (fiscal yearbook) to calculate land fiscal dependence - the core explanatory variable of China's urban economics.
- **Not suitable for**: Issues that require enterprise/household/individual micro-data (please use ASIF/CFPS/CHARLS), require higher than annual frequency (statistical yearbooks are summarized by year), require extremely fine internal spatial analysis of cities (please use geographical data such as night lights/POI).

## Key variables/modules
- **National Economic Accounts**: GDP total/growth rate/per capita/tertiary industries
- **Population**: permanent population/registered population/birth rate/death rate/natural growth rate/urbanization rate
- **Finance**: General public budget revenue/expenditure, tax revenue, land transfer revenue; local government debt can only be used after checking the measurement definition and level of the yearbook table one by one.
- **Industry**: Added value of industries above designated size, output of main products
- **Investment**: Fixed asset investment (total amount/sector), real estate development investment
- **Trade**: Total import and export volume (in US dollars and RMB), actual utilization of foreign capital
- **Price**: CPI, PPI, commodity retail price index
- **People's Livelihood**: Per capita disposable income, per capita consumption expenditure
- **Science, Education, Culture and Health**: Number of schools/enrolled students, number of hospital beds/number of doctors, R&D expenditure/patents

## How to get
1. **Direct to the source (free)**: data.stats.gov.cn → Select "Annual Data"/"Monthly Data"/"Quarterly Data" → Select Indicator/Region/Year → Download Excel. The NBS website is free.
2. **EPS Platform (the most trouble-free)**: Enter the EPS Data Platform through the university library → "China City Database" or "China County Database" → It has been organized into a panel format, select indicator + year to directly export Stata/CSV.
3. **CNKI statistical database** (subscribed by some universities): Provides yearbook PDF + data extraction function.

## Connections to other data
- **CFPS/CGSS/CHARLS**: Use "province code/city code + year" to connect the macro indicators (GDP/finance/public services) of the statistical yearbook with micro survey data to construct a research design of "macro impact → micro response".
- **ASIF/Customs/Pollution Database**: Use "industry code + region code" to compare the industry-region summary indicators of the statistical yearbook with micro-enterprise data - the yearbook provides an overall benchmark.
- **Census/Input-Output Table**: Together with the Statistical Yearbook, they constitute the NBS's "three-piece macro data set" - each has its own focus but is complementary.

## Remarks / Pitfalls
- **Measurement definition Trap**: "City" vs. "Municipal District" - The statistical measurement definition of prefecture-level cities is sometimes "the whole city" (including counties under its jurisdiction), and sometimes it is "municipal district" (only urban areas) - the unified measurement definition must be confirmed when making a city panel.
- **GDP Revision**: National and provincial GDP were significantly revised after the fourth economic census in 2018 - provincial GDP around 2018 is discontinuous and requires the use of revised data or breakpoint processing.
- **Administrative division change**: The removal of counties and establishment of districts/cities will change the definition of "city" - the long-term panel needs to use the "adjusted" version of the database (such as the retrospective version of EPS's zoning adjustment).
- **Missing and Lagging**: There are many missing indicators in remote areas (Tibet/Xinjiang/some prefecture-level cities in Qinghai); the latest year usually has a release lag of 1–2 years.
