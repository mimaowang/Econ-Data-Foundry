---
schema_version: 2
catalog_status: ready
id: cfps
name: China Family Panel Studies (CFPS)
aka:
- CFPS
- 中国家庭追踪调查
- 中国家庭动态跟踪调查
- China Family Panel Studies
- 北大CFPS
provider: Institute of Social Science Survey, Peking University (ISSS, Institute of Social Science Survey, Peking University)
china_related: true
domains:
- labor
- development
- health
- education
- consumption
- public
- sociology
- demography
unit_of_observation: Individual-year/Family-year/Community-year (three-tier tracking design)
structure: longitudinal-panel
geo_granularity:
- personal
- family
- village/community
- County
- city
- province
geography: 25 provinces/municipalities/autonomous regions in mainland China (accounting for approximately 95% of China’s total
  population); excluding Tibet, Qinghai, Ningxia, Hainan, Inner Mongolia, and Xinjiang
time_span:
  start: 2010
  end: ongoing
  last_confirmed_release: 2022
  coverage_note: Seven rounds confirmed for 2010/2012/2014/2016/2018/2020/2022
  last_checked: '2026-07-10'
frequency:
- biennial
sample_size: 'Baseline (2010): approximately 14,960 households/42,590 people; subsequent rounds approximately 40,000–50,000
  people/round'
key_variables:
- Household income (salary/business/transfer/property)
- Household expenditure and consumption
- Household assets (real estate/finance/liabilities)
- personal age
- gender
- marriage
- Hukou
- education level
- Employment status
- Careers and Industries
- Self-rated health
- BMI/height and weight
- chronic history
- Cognitive skills (vocabulary/math/memory)
- Child Development (Specialized for 0-15 years old)
- parenting style
- Community infrastructure and public services
- Family relationships (intergenerational transfers, living arrangements)
- Subjective attitude (happiness/trust/values)
research_fit:
  best_for:
  - Whole-family tracking from childhood to old age, as well as joint research on income, education, health and family relationships
  choose_over:
  - Priority over CHARLS when all-age family panels, child development, or intergenerational relationships are required
  - Prioritize CHFS when you need a complete balance sheet; give priority to CHNS when you need in-depth meals; compare CGSS
    when you need repeated cross-sections of attitudes.
  not_good_for:
  - Research before 2010
  - monthly or quarterly shocks
  - corporate research
  - Representative analysis of regions without gaps in 31 provinces across the country
  needs_join_for:
  - Regional policies and macro impacts need to be joined according to province/county codes; fine regional codes may require
    advanced permissions
  variation_available:
  - Biennial Panel for Individuals and Families
  - family relationship
  - Regional policy differences
  topics:
  - Education investment
  - Children’s education expectations
  - family education
  - Tuition (need to be verified according to round of questionnaire)
  - Parental participation (needs to be verified according to rounds of questionnaires)
  - Pension
  - Raising children for old age
  - intergenerational transfer
good_for:
- Income inequality and intergenerational mobility - parent-child income/education correlation, dynamic decomposition of opportunity
  inequality
- The causal effect of health shocks (disease/policy) on household labor supply, consumption and savings - panel fixed effects
  + DID
- Human capital accumulation—early childhood development, returns to education, cognitive abilities, and labor market performance
- Demographic changes - fertility decisions, aging, intergenerational cohabitation and transfer payments
- Urban-rural gap and household registration discrimination - Comparison of income/education/health of urban and rural families
  under the same framework
- Social attitudes and subjective well-being—the determinants and changing trends of happiness and social trust
identification:
- Panel fixed effects (individual/household)
- DID (policy pilot/inter-provincial differences)
- IV (community/policy exogenous impact)
- RD
- Brothers and sisters FE
linkable_keys:
- Province code
- County code
- Village/community code (ISSS authorization required)
- CFPS Personal ID
access_routes:
- route: cfps-official-platform
  access_status: available-with-application
  direct_url: https://cfpsdata.pku.edu.cn/#/home
  requirements: Register an account, fill in the research purpose and sign a data use agreement; apply separately for sensitive
    geographical variables.
  steps:
  - Enter the CFPS official data platform and register.
  - Select the desired survey round, fill in the purpose of the research and submit the application.
  - It usually takes about 3 working days to review; download the data, questionnaire and codebook after approval.
  - If the official platform is temporarily unavailable, use the Peking University Open Data Platform as an alternative entrance
    and check the current release round.
  deliverable: Personal/family/community data of the public rounds; permissions for fine geography and other sensitive fields
    below the county level are additional.
  cost: free
  last_checked: '2026-07-10'
- route: pku-open-data-fallback
  access_status: available-with-application
  direct_url: https://opendata.pku.edu.cn/
  requirements: Register an account, fill in the research purpose and sign a data use agreement; the platform release status
    needs to be confirmed on site.
  steps:
  - Register on the Peking University Open Data Platform.
  - Search CFPS and submit an application.
  - After approval, data, questionnaires and codebooks will be downloaded in rounds.
  deliverable: Alternate acquisition route when the official platform is temporarily unavailable; sensitive field permissions
    are additional.
  cost: free
  last_checked: '2026-07-10'
access:
  url: 'https://www.isss.pku.edu.cn/cfps/ (Peking University China Social Science Survey Center); Official data platform:
    https://cfpsdata.pku.edu.cn/#/home'
  cost: free
  license: For academic research only, you need to register an account and sign a usage agreement
  format:
  - dta
  - csv
  api: false
  how_to_get: 1) Visit the CFPS official data platform https://cfpsdata.pku.edu.cn/#/home and register; 2) Select a round,
    fill in the research purpose and sign a data use agreement; 3) It usually takes about 3 working days to review, and download
    the data, questionnaire and codebook of the public round after passing; 4) Sensitive fields such as fine geography must
    be applied for separately. When the official platform is unavailable, use https://opendata.pku.edu.cn/ as the backup entrance
    and check the release status on-site.
caveats: The round interval is two years, non-annual data, and annual panels require interpolation or only use even years.
  Includes 25 provinces that are not national – provincial/regional estimates are not fully representative of the country
  when used. Some sensitive variables (such as precise income, community code) require additional application for advanced
  permissions. The content of the questionnaire is fine-tuned in each round (variable names and definitions may change), and
  cross-round matching requires consulting the codebook of each round.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: partial
  last_audited: '2026-07-10'
used_by:
- cite: 'Chen, Yuan & Zhang (2023), Income Inequality and Educational Expenditures on Children: Evidence from the China Family
    Panel Studies'
  journal: CER
  year: 2023
  dataset_role: Key household microdata; education spending and income inequality
  data_note: Use CFPS tracking data to study how income inequality affects family education expenditures - widening income
    gaps will increase competition for children's education expenditures
- cite: Hu, Zhai & Yan (2023), Do Social Interactions Foster Household Entrepreneurship? Evidence from Online and Offline
    Data from CFPS
  journal: CER
  year: 2023
  dataset_role: Key household microdata; entrepreneurship and social interactions
  data_note: Using CFPS family entrepreneurship + social interaction data, we found that both online and offline social interaction
    promote family entrepreneurship, and the online social interaction effect is stronger.
- cite: 'Zhang (2022), Patrilineality, Fertility, and Women''s Income: Evidence from Family Lineage in China'
  journal: CER
  year: 2022
  dataset_role: Key personal/household data; fertility and female earnings
  data_note: Using CFPS data to study the lasting impact of clan culture (patrilineal family tradition) on fertility and female
    labor income
- cite: 'Huang, Luo, Ta & Wang (2024), Land Expropriation, Household Behaviors, and Health Outcomes: Evidence from China'
  journal: JDE
  year: 2024
  dataset_role: Main household panel results; joined with land acquisition shocks
  data_note: Use CFPS six rounds of data (2010–2020) to identify the economic and health effects of land expropriation on
    households - after expropriation, non-agricultural employment ↑, savings rate ↑14pp, subjective health improvement, but
    no significant changes in physical indicators - using event study method + staggered DID
- cite: 'Guo, Huang & Wang (2025), Public Pensions and Family Dynamics: Eldercare, Child Investment, and Son Preference in
    Rural China'
  journal: JDE
  year: 2025
  dataset_role: Family and child outcomes; combined with CHARLS, census and new rural insurance time points
  data_note: Using CFPS+CHARLS+2015 mini-census triple data+new rural insurance DDD, it is found that public pensions significantly
    reduce dependence on sons for old-age care → reduce bride price expenditures by 32% and improve newborn sex ratio by 12.7pp
    - the social norm reshaping effect of pensions
- cite: 'Chen, Ding & Tian (2026), The Stalled Quiet Revolution: Population Control, Skewed Sex Ratios, and the Widening Gender
    Gap in Labor Force Participation'
  journal: JDE
  year: 2026
  dataset_role: Micro-outcomes of labor force participation; joined with census and family planning policies
  data_note: Using CFPS (2012/2014/2016 waves) + 1990/2015 census microdata, using the intensity of family planning fines
    in each province as cohort DID - it was found that the one-child policy distorted the sex ratio and made women's LFP ↓~12pp
    relative to men - explaining the mystery of the decline in China's female labor force participation rate against the global
    trend
provenance:
- source: CFPS official website https://www.isss.pku.edu.cn/cfps/ and Peking University Open Data Platform https://opendata.pku.edu.cn/
  added: '2026-07-08'
  confidence: high
  verified: true
- source: CFPS technical report and questionnaire (multiple rounds), verified sampling design, variable coverage and access
    conditions
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- charls
- chns
- cgss
- chfs
- uhs
---

## Positioning in one sentence
CFPS (China Family Panel Survey) is a nationwide, large-scale, multidisciplinary social tracking survey initiated by Peking University.
Full-dimensional micro-data on income, education, health, cognition and development of approximately 15,000 households are tracked every two years.
Because it covers a wide range of areas, is available at no charge under the provider agreement, and has been tracked for more than ten years,
It is one of the most frequently used publicly released data sets in China's micro-level empirical research - it can almost serve as the "benchmark micro-data" for Chinese households.

## Research questions suitable for answering/Typical identification strategies
- **Intergenerational Mobility and Inequality**: Using father-son/mother-son pairs and long panels, we estimate intergenerational elasticities of education and income (IGE/IGC) and decompose the sources of inequality of opportunity. This is one of the "flagship uses" of CFPS.
- **Health and Aging**: Using multiple rounds of tracking + cognitive testing + health examination data, we study how health shocks affect family economic decision-making, labor participation and intergenerational transfer. Complementary to CHARLS (special program for middle-aged and elderly people).
- **Child Development and Human Capital**: CFPS includes special items on child development (cognitive testing, parenting environment, parental investment) aged 0–15 years old - long-term follow-up studies on child development are relatively scarce in Chinese data.
- **Urban-rural gap and social stratification**: CFPS covers urban and rural areas + different household registration types, and can be used for urban-rural income/education/health gap decomposition and Blinder-Oaxaca decomposition.
- **Not suitable for**: extremely segmented regional analysis (25 provinces other than the whole country + cannot be identified below counties), enterprise/industry level issues, research requiring monthly/quarterly frequency, and historical tracking before 2010.

## Key variables/modules
- **Economic Module**: Total household income (four categories: salary/business/transfer/property), household expenditure (eight categories of consumption), housing conditions and value
- **Education Module**: Personal academic qualifications (from kindergarten to doctorate), school status, training experience, cognitive test (vocabulary/mathematics/memory)
- **Health Module**: Self-rated health, BMI (height and weight measured by interviewer), chronic medical history, medical treatment behavior, medical insurance
- **Children Special (0–15 years old)**: Parity/Birth Weight, Parenting Style (Kessler Scale), Children’s Cognitive Development (WAIS Simplified Version)
- **Community Module**: Village/community infrastructure, public services (schools/hospitals/roads), labor market characteristics
- **Subjective Attitude Module**: Self-evaluation of happiness, social trust, values, and social status

## How to get
1. Visit the CFPS official data platform https://cfpsdata.pku.edu.cn/#/home and register.
2. Search for the required rounds, fill in the purpose of the study and sign a data use agreement.
3. Under the current platform process, the public round usually takes about 3 working days to review; after passing, download the data, questionnaire and codebook. The specific timeliness and release status are subject to the current page of the platform.
4. If the official platform is temporarily unavailable, use https://opendata.pku.edu.cn/ as a backup entrance and check the current release round on site.
5. If you need sensitive variables (accurate income, community codes, etc.), you need to submit a separate application for advanced permissions to ISSS.

## Connections to other data
- **CHARLS**: Also produced by Peking University ISSS and on the same application platform - CHARLS focuses on middle-aged and elderly people aged 45+, including biomarkers and physical examination data; it complements CFPS in covering all ages.
- **CHNS / CGSS / CHFS**: Both are large-scale household micro-surveys that can cross-validate main statistics (income distribution, consumption patterns, education level).
- **Macro/Policy Data**: "Province/County Code" can be used to connect provincial statistical yearbooks and policy databases to construct regional policy impact variables.

## Remarks / Pitfalls
- **Not representative of the entire country**: CFPS covers 25 provinces (excluding Hainan, Inner Mongolia, Ningxia, Qinghai, Tibet, and Xinjiang), and provincial-level estimates are biased.
- **Two-year interval**: CFPS is a bi-annual survey (even years), please note when doing the "annual" panel - there are no data points for odd years.
- **Variable names change across rounds**: Each round of questionnaires is revised and variable names may change. Be sure to check the codebook and variable correspondence table of each round before merging across rounds.
- **Advanced Permission Stratification**: Core variables are free and open, but precise income, community codes, some province codes, etc. require additional application for advanced permissions (approval is more stringent).
- **Individual tracking rate**: The panel tracking rate is high (about 80–85%), but there is sample attrition—be careful to check attrition bias when doing long panels.
