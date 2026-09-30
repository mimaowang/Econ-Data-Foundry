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
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v162y2023ics0304387823000056.html
  data_note: Use China's prefecture-level city road infrastructure data (statistical yearbook/traffic yearbook) + industrial
    enterprise database to study the impact of highway expansion on resource allocation efficiency and competition promotion
- cite: 'Cao, Ni & Guo (2025), Broadband Internet and Income Inequality among the Floating Population: Evidence from the ''Broadband
    China'' Strategy'
  journal: CER
  year: 2025
  dataset_role: Urban broadband/ICT and macro control; joining with CMDS
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v90y2025ics1043951x25000276.html
  data_note: Using the China Urban Statistical Yearbook (broadband coverage/ICT infrastructure) + CMDS floating population
    data, and using the 'Broadband China' policy as DID, we study the impact of Internet infrastructure on the income inequality
    of the floating population.
- cite: 'Song, Storesletten & Zilibotti (2011), Growing Like China'
  journal: AER
  year: 2011
  dataset_role: Aggregate NBS statistics for structural model calibration targets
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/112395/
  data_note: Calibrated a two-sector growth model using NBS Statistical Yearbook aggregates (GDP, savings, employment shares
    by ownership, industry-level output and TFP, provincial panels) to explain China's sustained high growth and capital returns
    despite massive investment.
- cite: 'Piketty, Yang & Zucman (2019), Capital Accumulation, Private Property, and Rising Inequality in China, 1978–2015'
  journal: AER
  year: 2019
  dataset_role: National accounts and household survey income tables for Distributional National Accounts
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/116194/
  data_note: Used NBS national accounts (GDP, capital stock, savings) and household survey income distribution tables (by decile
    and income source) from the Statistical Yearbook system to construct China's Distributional National Accounts. Combined with
    CHIP, CFPS wealth surveys, tax data, and Hurun rich list to document rising wealth/income inequality from 1978 to 2015.
- cite: 'Author (2025), How Government Fiscal Decentralization Shapes Bank Competition Dynamics: City-Level Evidence from China'
  doi: https://doi.org/10.1016/j.chieco.2025.102570
  journal: CER
  year: 2025
  dataset_role: China City Statistical Yearbook municipal fiscal expenditure data; fiscal decentralization measure
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25002365
  data_note: Uses City Statistical Yearbook fiscal expenditure data combined with CSMAR bank-level financial data (2011-2022, 250 banks across 1,472 bank-year observations) to study how fiscal decentralization affects bank competition at the city level.
- cite: 'Gerritse, Wang & van Oort (2026), Industrial Transfer Policy in China: Migration and Development'
  doi: https://doi.org/10.1016/j.jue.2025.103815
  journal: JUE
  year: 2026
  dataset_role: China City Statistical Yearbook city-level GDP, wage, employment, and related urban-development outcomes linked to the migrant survey
  evidence_type: paper_data_section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0094119025000804
  data_note: The paper's data section identifies China City Statistical Yearbooks issued by the NBS as the source for city-level GDP, wage, and employment variables used alongside the CMDS migration measures and ASIF firm outcomes. The checked evidence does not establish a paper-specific yearbook extract, exact editions, or a new download route; use the main Statistical Yearbook record and verify definitions and city boundaries before joining.
- cite: 'Author (2025), Structural Transformation and the Urban Growth Shadows: County-Level Evidence from China, 1990-2020'
  doi: https://doi.org/10.1016/j.regsciurbeco.2025.104141
  journal: RSUE
  year: 2025
  dataset_role: County Statistical Yearbook industrial structure and socioeconomic indicators
  evidence_type: data-section
  evidence_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4765694
  data_note: Uses county-level Statistical Yearbook data to construct industrial structure measures (agricultural vs. service employment shares) and socioeconomic controls across 2,225 counties over 1990-2020. Combined with Population Census and Economic Census data to document urban growth shadows — structural transformation interacts with city proximity to determine county-level population growth.
- cite: 'Wang & Felice (2026), Internal Migration and Structural Change in China'
  doi: https://doi.org/10.1111/jors.70049
  journal: JRS
  year: 2026
  dataset_role: City Statistical Yearbook — GDP per capita, industrial output, disposable income, wages, and land area
  evidence_type: data-section
  evidence_url: https://ideas.repec.org/a/bla/jregsc/v66y2026i2p602-625.html
  data_note: Uses City Statistical Yearbook economic indicators (GDP per capita, industrial output, wages, disposable income) alongside CMDS and IPUMS Census data to estimate how internal migration drives structural change across prefecture-level cities via 2SLS/3SLS. City-level economic controls from yearbooks provide the regional economic context for migration-induced structural transformation.
- cite: 'Fan, Li & Song (2025), Factor Market Segmentation and Regional Innovation: Evidence From China'
  doi: https://doi.org/10.1111/jors.70031
  journal: JRS
  year: 2025
  dataset_role: City-level economic statistics across 279 prefecture-level cities (1999-2019) for factor market segmentation index
  evidence_type: data-section
  evidence_url: https://metatoc.com/papers/121633-factor-market-segmentation-and-regional-innovation-evidence-from-china
  data_note: Uses City Statistical Yearbook economic indicators to construct a price-method factor market segmentation index across 279 prefecture-level cities (1999-2019). Combined with patent data to test how labor and capital market segmentation affects regional innovation under fiscal decentralization.
- cite: 'Hau & Ouyang (2024), Can Real Estate Booms Hurt Firms? Evidence on Investment Substitution'
  doi: https://doi.org/10.1016/j.jue.2024.103695
  journal: JUE
  year: 2024
  dataset_role: City-level housing prices and land supply data across 172 prefecture-level cities
  evidence_type: data-section
  evidence_url: https://ideas.repec.org/a/eee/juecon/v144y2024ics0094119024000652.html
  data_note: Uses 172 prefecture-level city housing price and residential land supply data from statistical yearbooks as instrumental variables. Exogenous variation in city-level residential land supply identifies the causal effect of housing booms on manufacturing firms' investment and productivity. Combined with ASIF firm panel and Customs trade data.
- cite: 'Rong, Wang & Zhang (2026), Does Real Estate Expansion Hurt Manufacturing Employment: Evidence from China'
  doi: https://doi.org/10.1016/j.labeco.2026.102889
  journal: Labour Economics
  year: 2026
  dataset_role: City-level real estate investment, housing prices, GDP growth, and minimum wage statistics across 70 major cities (2000-2009)
  evidence_type: replication
  evidence_url: https://data.mendeley.com/datasets/btk3vktc2s/2
  data_note: >-
    Uses city-level statistical yearbook data (real estate investment, housing prices, GDP growth, minimum wages, fiscal conditions) across 70 major Chinese cities (2000-2009) combined with ASIF firm panel. IV estimates using province-level residential land transfer as instrument find a 10% increase in real estate investment reduces manufacturing firm employment by 1.46%. Rising wage costs are the primary mechanism rather than reduced capital formation.
- cite: 'Qin, Yi & Zhang (2025), Quarter of Birth, Gender Inequality, and Economic Development'
  doi: https://doi.org/10.1086/737993
  journal: JLE
  year: 2025
  dataset_role: Statistical yearbooks and meteorological data for agricultural seasonality and weather shock measurement
  evidence_type: replication
  evidence_url: https://opendata.pku.edu.cn/dataverse/pku
  data_note: >-
    Uses statistical yearbook data combined with meteorological records to construct measures of agricultural seasonality and weather shocks as exogenous variation in household resource abundance at birth. Combined with six Census waves (1990-2020), CFPS, CEPS, and CHNS. Finds birth quarter effects on lifecycle outcomes — driven by agricultural seasonality interacting with son preference in neonatal investment.
- cite: 'Li & Yang (2005), The Great Leap Forward: Anatomy of a Central Planning Disaster'
  doi: https://doi.org/10.1086/430804
  journal: JPE
  year: 2005
  dataset_role: Provincial agricultural output, sown area, draft animals, farm capital, grain retention/procurement, population and mortality controls for the 1954-1989 panel
  evidence_type: data-section
  evidence_url: https://www3.nd.edu/~nmark/ChinaCourse/TheWeeks/Li_Yang_GLF_JPE.pdf
  data_note: >-
    The paper's Appendix B states that provincial agricultural inputs and outputs come mainly from Compilation of China's Rural Economic Statistics: 1949-86 (Ministry of Agriculture, 1989), with missing years cross-checked against the China Statistical Yearbook and provincial agricultural statistical yearbooks. The authors also conducted a 1999 retrospective province survey with the General Organization of Rural Socio-economic Survey for weather, collective-unit scale, and exit-rights variables. The published yearbook component is therefore a grounded use of this canonical source; the retrospective survey is a separate paper-built source and is not treated as publicly reproducible data.
- cite: 'Borusyak & Hull (2023), Nonrandom Exposure to Exogenous Shocks'
  doi: https://doi.org/10.3982/ECTA19367
  journal: Econometrica
  year: 2023
  dataset_role: Prefecture-level urban employment outcome for the 2007-2016 China high-speed-rail market-access application
  evidence_type: data_appendix
  evidence_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10795685/
  data_note: >-
    The article's data appendix states that prefecture employment is taken from the 2008-2017 China City Statistical Yearbooks
    (each yearbook covers the previous year), using the series “The Average Number of Staff and Workers” for the whole prefecture,
    not only the main urban core. The final outcome sample is 275 prefectures with non-missing, cleaned 2007-2016 employment
    growth. The paper also uses the 2000 Census for prefecture populations and a separately constructed high-speed-rail network;
    those inputs are not silently folded into the yearbook record.
- cite: 'Au & Henderson (2006), Are Chinese Cities Too Small?'
  doi: https://doi.org/10.1111/j.1467-937X.2006.00387.x
  journal: ReStud
  year: 2006
  dataset_role: City-level output, employment, population, capital, industry mix, FDI, amenities and price controls for the 1990-1997 urban agglomeration analysis
  evidence_type: data_appendix
  evidence_url: https://www.brown.edu/Departments/Economics/Faculty/henderson/papers/chinatoosmallcities0905.pdf
  data_note: >-
    Appendix B identifies the 1991-1998 annual Urban Statistical Yearbook of China (covering data years 1990-1997) as the main
    source, supplemented by the compiled volume Cities China 1949-1998. The estimating sample starts from 223 prefecture-level
    cities and ends at 205 after exclusions; variables are measured for the confined city proper (shi qu), not the entire
    municipal district (di qu). The paper's historical city compilation and GIS education input remain separate candidate sources.
- cite: 'Jin & Qian (1998), Public Versus Private Ownership of Firms: Evidence from Rural China'
  doi: https://doi.org/10.1162/003355398555748
  journal: QJE
  year: 1998
  dataset_role: China Statistical Yearbook component of a provincial rural-enterprise and rural-income panel
  evidence_type: data_appendix
  evidence_url: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
  data_note: >-
    The paper's Appendix Table I uses CSY 1987-1994 for gross industrial real output of state enterprises, annual rural consumer
    price indices used to deflate rural income, and the 1981-1994 CSY editions listed in the bibliography. The paper is a provincial
    rural-enterprise study with 28 provinces and year-specific measures; the other named inputs (CRSY, CTESY, CRFSY, CAY, CPY,
    CICAS/CDTSY, and TESM) are distinct products and are tracked as unresolved candidates rather than folded into this record.
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
- source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
  field_scope:
  - QJE article identity and DOI
  - provincial-data scope and rural-enterprise research context
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
  field_scope:
  - Appendix Table I CSY variables and year ranges
  - distinction between the CSY component and the paper's other named yearbooks
  added: '2026-08-12'
  confidence: med
  verified: true
- source: https://www.stats.gov.cn/sj/ndsj/2024/html/note.htm
  field_scope:
  - current official NBS China Statistical Yearbook publication identity and contents
  - current public yearbook reading route, not historical-edition availability
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.sciencedirect.com/science/article/pii/S0094119025000804
  field_scope:
  - JUE paper identity, Gerritse/Wang/van Oort authorship, volume 151 (2026), and city-yearbook role
  - city-level GDP, wage, employment, and urban-development linkage to CMDS/ASIF
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://papers.tinbergen.nl/24020.pdf
  field_scope:
  - NBS China City Statistical Yearbook source description for GDP, wage, and employment controls/outcomes
  - distinction between yearbook aggregate data and the paper's migrant/firm microdata
  added: '2026-08-12'
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
