---
schema_version: 2
catalog_status: grounding
id: china-census
name: China Census (Population Census/National 1% Population Sample Survey)
aka:
- 人口普查
- 全国人口普查
- Population Census of China
- Chinese Census
- 中国人口普查数据
- 五普/六普/七普
- 1%抽样调查
- 小普查
- Mini-Census
- 全国1%人口抽样调查
provider: National Bureau of Statistics (NBS, National Bureau of Statistics of China)
china_related: true
domains:
- labor
- demography
- development
- public
- macro
- health
- education
unit_of_observation: Individual/family household/collective household (micro level); can be aggregated to counties/cities/provinces
structure: decennial-census-and-sample
geo_granularity:
- personal
- family household
- village/community
- Township/street
- County
- city
- province
geography: All of mainland China (including all provinces/autonomous regions/municipalities except Hong Kong, Macao and Taiwan)
time_span: 'Large census: 1990 (fourth census)/2000 (fifth census)/2010 (sixth census)/2020 (seventh census); minor census
  (1%): 1995/2005/2015; and 1982 (third census) and earlier historical censuses'
frequency: A census is conducted every ten years; Small census (1% sampling) between two major censuses (approximately every
  10 years, and in recent years every 5 years)
sample_size: Large censuses cover the entire population of the country (billions); small censuses sample about 1% (tens of
  millions); microdata samples (long table/short table) usually range from millions to tens of millions of personal records
key_variables:
- age
- gender
- nation
- Household registration type (agricultural/non-agricultural)
- Place of household registration
- Current residence (province/city/county)
- Migration status (whether you left the place of household registration, length of departure, reason for departure)
- education level
- Marital status
- Number of children born
- Employment status
- Career
- Industry
- housing type
- Housing area
- Year when the house was built
- Household structure (head of household/spouse/children/parents)
- place of birth
- Place of permanent residence five years ago (Fifth Census/Sixth Census)
- Is it literate?
- Health status (some years)
good_for:
- Determinants and consequences of internal migration - gravity model estimation of bilateral migration flows (Tombe & Zhu
  2019 AER uses the Fifth Census and the 2005 Small Census to construct an inter-provincial migration matrix)
- The economic consequences of skewed sex ratios—how regional/cohort-level marriage market pressure affects savings rates
  (classic identification of Wei & Zhang 2011 JPE)
- Population structure and economic growth - the impact of working-age population proportion, dependency ratio, and aging
  on regional economic growth
- Human capital and returns to education - Estimating wage premiums by education/experience/region using census microdata
- Household registration/household registration system and welfare inequality—differences in living conditions, education,
  and employment between agricultural and non-agricultural household registrations
- Urbanization and urban systems—micro-observations of city size distribution, commuting patterns, and urban agglomeration
  formation
identification:
- IV (Geographical/Historical Instrumental Variables)
- DID (Policy/Household Registration Reform)
- RD (policy threshold)
- Panel (county/provincial level
- using multiple rounds of census)
- Gravity model (bilateral migration)
linkable_keys:
- County code
- City code
- Provincial code
- Industry code
- Occupation code
research_fit:
  best_for:
  - County/city/provincial measures of population migration matrix, sex ratio and population structure
  - Census cross-sectional comparison of household registration, education and labor force structure
  choose_over:
  - Select Census when you need nationwide county-level coverage, usual residence five years ago, or cross-census population
    benchmarks
  - Choose CFPS/CHFS when annual household panels, balance sheets or detailed causal results are needed rather than treating
    the census as a panel
  not_good_for:
  - annual family panel
  - Full balance sheet of household financial results
  - Enterprise production and trade micro results
  needs_join_for:
  - Pollution, policy, education and economic results need to be joined by county/city/province and year
  - Household or business behavioral results usually require micro data such as CFPS/CHFS/ASIF
  variation_available:
  - 1990/2000/2010/2020 general census and some 1% minor census
  - County/city/province spatial differences
  - Differences between household registration and current residence, permanent residence five years ago, and birth cohort
access:
  url: 'https://data.stats.gov.cn (National Bureau of Statistics Data Query Platform, summary table); Micro Data: https://microdata.stats.gov.cn
    (National Bureau of Statistics Micro Data Laboratory, application required)'
  cost: 'Summary table: free (published on the National Bureau of Statistics website); Micro data: by-application (academic
    research only, confidentiality agreement required)'
  license: Academic research only; microscopic data may not be redistributed and must be used in a secure environment (some
    require on-site analysis in NBS designated laboratories)
  format:
  - csv
  - xlsx (summary table)
  - DTA (microscopic sample)
  api: false
  how_to_get: '1) Summary table: Directly access data.stats.gov.cn to query summary indicators at the national/provincial/city/county
    levels; 2) Micro data: Submit a formal application to the National Bureau of Statistics → Review → Sign a confidentiality
    agreement → Obtain desensitized samples (usually 1% of the long form or 10% of the short form); 3) Some universities/institutions
    (Renmin University, Peking University, Tsinghua University, etc.) have been authorized to be used on campus; 4) IPUMS
    International (international.ipums.org) provides micro-samples in the unified format of the Fifth Population Census (2000),
    which can be registered and downloaded for free.'
caveats: The microdata acquisition threshold is high and the approval cycle is long (usually 3–6 months); the microscopic
  samples provided by NBS have been desensitized (precise addresses/dates of birth, etc. have been removed); the questionnaires
  and variable definitions of each round of census have changed, and cross-round comparisons need to be aligned; the sampling
  methods and coverage of the small census (1%) and the large census (100%) are essentially different. IPUMS only provides
  the fifth census in 2000 - subsequent censuses must go through domestic channels.
access_routes:
- route: NBS aggregate data portal
  access_status: available
  direct_url: https://data.stats.gov.cn/
  requirements:
  - No registration is required to query the public summary table; the specific export capabilities are subject to the current
    functions of the website.
  steps:
  - Open the National Bureau of Statistics data query platform
  - Filter indicators by census topic, region and year
  - Export or record summary tables and save query conditions
  deliverable: Publicly available aggregated indicators at the province/city/county level; not a census microsample
  cost: free
  last_checked: '2026-07-10'
- route: NBS microdata laboratory application
  access_status: needs-verification
  direct_url: https://microdata.stats.gov.cn/
  requirements:
  - formal research project
  - Relying institution
  - Pass review and sign a confidentiality or controlled use agreement
  - Use in designated safe environment
  steps:
  - Confirm target census waves and catalogs in microdata lab
  - Submit project, variant and usage requests
  - Wait for review and sign the agreement
  - Use desensitized samples in approved environments
  deliverable: Approved census micro-sample; waves, variables and carryout ranges are subject to the approval results
  cost: by-application
  last_checked: '2026-07-10'
- route: IPUMS International 2000 census sample
  access_status: available-with-registration
  direct_url: https://international.ipums.org/
  requirements:
  - Register an account
  - Accept IPUMS Terms of Use
  steps:
  - Register and search China 2000 Census
  - Select required variables and extract in unified format
  - Download and review IPUMS wave, sampling and variable definitions
  deliverable: Unified format micro-sample of the fifth census in 2000; cannot replace subsequent census waves
  cost: free
  last_checked: '2026-07-10'
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Tombe & Zhu (2019), Trade, Migration, and Productivity: A Quantitative Analysis of China'
  journal: AER
  year: 2019
  data_note: The 2000 Fifth Census and the 2005 1% Minor Census were used to construct a bilateral migration matrix of inter-provincial
    + sub-sector (agricultural/non-agricultural) as the key data input of the spatial general equilibrium model.
- cite: 'Wei & Zhang (2011), The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings Rates in China'
  journal: JPE
  year: 2011
  data_note: Using the county-level sex ratio data and household savings rate data from the census, the sex ratio imbalance
    is used as a proxy variable for competitive pressure in the regional marriage market to identify competitive savings motives.
- cite: Khanna, Liang, Mobarak & Song (2025), The Productivity Consequences of Pollution-Induced Migration in China
  journal: 'AEJ: Applied'
  year: 2025
  data_note: Using China's population migration data and air pollution data, we quantify the impact of pollution-induced migration
    of skilled labor on total productivity and welfare under a spatial equilibrium framework.
- cite: 'Chen, Oliva & Zhang (2022), The Effect of Air Pollution on Migration: Evidence from China'
  journal: JDE
  year: 2022
  data_note: Using county-level migration data from previous censuses + atmospheric temperature inversion as IV, it was found
    that a 10% increase in air pollution led to a decrease in net in-migration population of approximately 2.8% - migration
    was mainly driven by highly educated young people
- cite: Guo, Zhang & Zhou (2024), The Demography of the Great Migration in China
  journal: JDE
  year: 2024
  data_note: Using the 2010 Sixth National Population Census to construct a bilateral migration matrix between 331 prefecture-level
    cities, and using the birth cohort size differences caused by the famine and family planning in the 1960s as an IV—identifying
    how the push and pull forces of demographic structure shape the largest internal migration in human history
- cite: 'Chen, Ding & Tian (2026), The Stalled Quiet Revolution: Population Control, Skewed Sex Ratios, and the Widening Gender
    Gap in Labor Force Participation'
  journal: JDE
  year: 2026
  data_note: Using 1990/2015 census microdata + CFPS, using the intensity of family planning fines in each province as a cohort
    DID - it is found that the gender ratio imbalance caused by the one-child policy makes women's LFP relative to men's LFP
    through the marriage market channel (female marriage ↑/bargaining power ↑ → leisure choice) ↓~12pp
provenance:
- source: Tombe and Zhu openICPSR replication package https://doi.org/10.3886/E113071V1 (supports bilateral migration flows from the 2000 Census and 2005 Mini-Census)
  added: '2026-07-08'
  confidence: high
  verified: false
- source: IPUMS International https://international.ipums.org (supports availability of a Chinese 2000 Census microdata sample)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: National Bureau of Statistics data.stats.gov.cn and microdata.stats.gov.cn (confirm summary table and microdata
    application channels)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- china-stat-yearbook
- china-satellite-pm25
- cfps
- uhs
---

## Positioning in one sentence
China's census is a comprehensive survey covering the entire country's population once every 10 years - from personal information to migration history to housing conditions.
It is the "underlying geo-demographic information infrastructure" for research on China's population structure, migration, urbanization and labor force.
Summary tables are publicly available, and microdata (1% or short form sampling) can be obtained through application or IPUMS International.
It has been repeatedly used by top journals to construct inter-provincial/inter-county migration matrices, sex ratio instrumental variables and population structure indicators.

## Research questions suitable for answering/Typical identification strategies
- **Internal migration and spatial economy**: Use "Place of permanent residence five years ago" (Fifth Census/Sixth Census) and "Place of household registration" to construct a bilateral migration flow matrix to estimate the impact of migration costs and trade costs on the spatial allocation of labor (Tombe & Zhu 2019 AER's approach: use two rounds of data in 2000 and 2005 to make inter-provincial migration matrices for the agricultural/non-agricultural sectors respectively).
- **Gender Ratio and Household Economic Decisions**: Use the gender ratio imbalance at the county/cohort level (exogenous variation caused by family planning + boy preference) to identify how the gender ratio affects household savings rate, housing prices, entrepreneurship and other economic behaviors (Wei & Zhang 2011 JPE's classic study - the gender ratio is one of the most commonly used Chinese region IVs in empirical research).
- **Urbanization and the household registration system**: Taking advantage of the intersection of population type and current residence, measure the scale and distribution of "person-household separation" and study the labor market effect of household registration reform.
- **Not suitable for use**: Enterprise/industry level issues (please use ASIF/Economic Census), microeconomics below the county level before 2010 (only IPUMS was available before the Five-Year Plan), and research that requires annual frequency (the census is point-in-time data).
- **IPUMS version**: only covers the year 2000 (Fifth Census). When using it, please pay attention to the subtle differences in variable definitions and weights with the domestic official version.

## Key variables/modules
- **Demographic Basics**: age, gender, ethnicity, marital status, literacy level
- **Migration Core** (highest value): Place of household registration (province/city/county), current place of residence, length of time away from the place of household registration, reason for migration, place of permanent residence five years ago
- **Human capital**: education level (from illiterate to graduate student), study status, graduation time
- **Labor force**: employment status, occupation (major category/medium category), industry (category/major category), reason for not working
- **Housing**: Type of housing, year of construction, building area, number of rooms, kitchen/toilet/water facilities
- **Fertility**: number of live births, number of surviving children (special for women of childbearing age)

## How to get
1. **Summary table (the simplest)**: data.stats.gov.cn → Census special topic → Check summary indicators by province/city/county/township/industry/occupation and other dimensions, download Excel/CSV for free.
2. **Microdata (formal application)**: Submit an application to the Microdata Laboratory of the National Bureau of Statistics (microdata.stats.gov.cn) → review and approval (3-6 months) → sign a confidentiality agreement → obtain desensitized long form 1% or short form 10% samples.
3. **IPUMS International (International Alternative)**: international.ipums.org provides standardized micro-samples of the Fifth Census (2000), free registration and download, and variable names consistent with other global censuses - suitable for international comparative research.
4. **University authorization channels**: Some universities such as Renmin University, Peking University, and Tsinghua University are authorized by NBS to use more detailed microscopic samples in on-campus laboratories.

## Connections to other data
- Use "county code/city code/province code" to connect **Statistical Yearbook** and **Policy Database** (various district and county level policies/impacts) to build a regional panel.
- Use "Industry/Occupation Code" to connect **Economic Census** or **Enterprise Database** to construct an industry-regional matrix of the labor market.
- Baseline weights and sampling frames can be provided for sample surveys such as **CFPS / UHS / CGSS** - the census is the parent frame for these surveys.

## Remarks / Pitfalls
- **Micro data threshold is extremely high** - This is not a public data set. The alternative paths adopted by most scholars are: ①Use summary tables to create provincial/municipal/county-level panels; ②Use the fifth census (2000) micro-samples of IPUMS; and ③Switch to public micro-surveys such as CFPS/CHNS.
- **Changes in the definition of migration data**: The definition of migration (threshold of departure time/whether intra-city migration is included) in the Fourth Census/Fifth Census/Sixth Census is not completely consistent. Cross-census comparisons require careful checking of the definitions.
- **Industry/occupation code alignment**: Each census round uses different versions of the national standard (GB/T 4754) → manual alignment is required for comparison across rounds.
- **IPUMS Restrictions**: 2000 only, excluding update years - to do research in the 2010s you can only use the NBS formal application or fall back to the summary table.
