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
caveats: The survey follows a two-year schedule; interpolated values would be researcher-created, not observed annual responses.
  Coverage of 25 provinces does not by itself establish representativeness for every province or local subgroup; consult the sampling design and weights for the intended population.
  Some sensitive variables (such as precise income, community code) require additional application for advanced
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
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v78y2023ics1043951x23000172.html
  data_note: Use CFPS tracking data to study how income inequality affects family education expenditures - widening income
    gaps will increase competition for children's education expenditures
- cite: Hu, Zhai & Yan (2023), Do Social Interactions Foster Household Entrepreneurship? Evidence from Online and Offline
    Data from CFPS
  journal: CER
  year: 2023
  dataset_role: Key household microdata; entrepreneurship and social interactions
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v79y2023ics1043951x23000500.html
  data_note: Using CFPS family entrepreneurship + social interaction data, we found that both online and offline social interaction
    promote family entrepreneurship, and the online social interaction effect is stronger.
- cite: 'Zhang (2022), Patrilineality, Fertility, and Women''s Income: Evidence from Family Lineage in China'
  journal: CER
  year: 2022
  dataset_role: Key personal/household data; fertility and female earnings
  evidence_type: provider-literature-portal
  evidence_url: https://www.isss.pku.edu.cn/cfps/xzyj/wxzsm/1201867cfps1378615.htm
  data_note: Using CFPS data to study the lasting impact of clan culture (patrilineal family tradition) on fertility and female
    labor income
- cite: 'Huang, Luo, Ta & Wang (2024), Land Expropriation, Household Behaviors, and Health Outcomes: Evidence from China'
  journal: JDE
  year: 2024
  dataset_role: Main household panel results; joined with land acquisition shocks
  evidence_type: institutional-news
  evidence_url: https://spft.cufe.edu.cn/info/1022/6589.htm
  data_note: Use CFPS six rounds of data (2010–2020) to identify the economic and health effects of land expropriation on
    households - after expropriation, non-agricultural employment ↑, savings rate ↑14pp, subjective health improvement, but
    no significant changes in physical indicators - using event study method + staggered DID
- cite: 'Guo, Huang & Wang (2025), Public Pensions and Family Dynamics: Eldercare, Child Investment, and Son Preference in
    Rural China'
  journal: JDE
  year: 2025
  dataset_role: Family and child outcomes; combined with CHARLS, census and new rural insurance time points
  evidence_type: secondary-summary
  evidence_url: https://cec.blog.caixin.com/archives/280706
  data_note: Using CFPS+CHARLS+2015 mini-census triple data+new rural insurance DDD, it is found that public pensions significantly
    reduce dependence on sons for old-age care → reduce bride price expenditures by 32% and improve newborn sex ratio by 12.7pp
    - the social norm reshaping effect of pensions
- cite: 'Chen, Ding & Tian (2026), The Stalled Quiet Revolution: Population Control, Skewed Sex Ratios, and the Widening Gender
    Gap in Labor Force Participation'
  journal: JDE
  year: 2026
  dataset_role: Micro-outcomes of labor force participation; joined with census and family planning policies
  evidence_type: institutional-news
  evidence_url: https://cem.cau.edu.cn/art/2026/4/17/art_36277_1108087.html
  data_note: Using CFPS (2012/2014/2016 waves) + 1990/2015 census microdata, using the intensity of family planning fines
    in each province as cohort DID - it was found that the one-child policy distorted the sex ratio and made women's LFP ↓~12pp
    relative to men - explaining the mystery of the decline in China's female labor force participation rate against the global
    trend
- cite: 'Piketty, Yang & Zucman (2019), Capital Accumulation, Private Property, and Rising Inequality in China, 1978–2015'
  journal: AER
  year: 2019
  dataset_role: Wealth survey microdata (2010 and 2012 waves); combined with CHIP wealth surveys for inequality measurement
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/116194/
  data_note: Used CFPS 2010 and 2012 wealth survey microdata together with CHIP 1995/2002 to construct Distributional National
    Accounts for China. Combined with NBS national accounts, household survey income tables by decile, tax data on top earners,
    and Hurun rich list to measure China's wealth/income inequality from 1978 to 2015.
- cite: 'Zha & Zhou (2025), The Long-Term Effect of Television on Children''s Human Capital Development in China'
  doi: https://doi.org/10.1016/j.jdeveco.2025.103538
  journal: JDE
  year: 2025
  dataset_role: Main individual-level outcomes for non-cognitive skills, cognitive scores, and adult socioeconomic status
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v176y2025ics0304387825000896.html
  data_note: Uses CFPS 2010 baseline (1977-1994 birth cohorts, N=7,064) combined with community-level cable/satellite TV coverage
    timing from the CFPS community questionnaire. Exploits staggered DID across communities' TV access timing × CCTV-14 children's
    channel launch (2003) to identify the effect of exposure to quality children's television during ages 4-14. Finds significant
    improvement in non-cognitive skills (emotional stability, conscientiousness) but no lasting effect on cognitive scores —
    an asymmetric effect. Left-behind children and disadvantaged communities benefit most, showing CCTV-14 acted as a "social
    parent" substitute. Exposure also predicts higher adult SES, better health, and greater digital literacy.
- cite: 'Author (2026), The Impact of Urbanization on Child Growth: Evidence from City-County Mergers in China'
  doi: https://doi.org/10.1016/j.regsciurbeco.2025.104187
  journal: RSUE
  year: 2026
  dataset_role: CFPS household panel providing child anthropometric controls and family characteristics
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0166046225000699
  data_note: Uses CFPS child and household data as a robustness complement to CHNS to measure child anthropometric outcomes (stunting and wasting) in relation to city-county merger urbanization policy. CFPS provides broad family demographic controls, household economic status, and health indicators.
- cite: 'Author (2025), Skills and the City in China'
  doi: https://doi.org/10.1016/j.regsciurbeco.2024.104082
  journal: RSUE
  year: 2025
  dataset_role: CFPS individual-level cognitive and social skill measures matched with city characteristics
  evidence_type: data-section
  evidence_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4517629
  data_note: Uses CFPS individual-level panel data to construct cognitive and social skill measures at the individual level combined with city-level population and wage data from multiple Census waves (1982-2015). Maps occupational skill intensity using O*NET and the China Dictionary of Occupational Classification (DCOC) through text analysis. Finds larger cities disproportionately attract and reward workers with higher cognitive and social skills.
- cite: 'Jiang & Yin (2025), Delinking Social Identity From Rural-Urban Stereotypes: The Labor Market Effects of Abolishing Agricultural Hukou in China'
  doi: https://doi.org/10.1111/jors.70032
  journal: JRS
  year: 2025
  dataset_role: CFPS individual/household panel — labor market outcomes, hukou status, and income
  evidence_type: data-section
  evidence_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70032
  data_note: Uses CFPS data with CGSS validation in a staggered DiD design across 89 hukou-reform cities (2010-2015). Finds that abolishing agricultural hukou delinks social identity from rural-urban stereotypes — rural stayers gain ~17% earnings and more nonagricultural jobs, but rural-urban migrants see no income gains and urban incumbents face higher nonemployment risk. Effects are heterogeneous by education and regional development level.
- cite: 'Zhang & Zong (2025), Women''s Empowerment and Participation in Innovation: Evidence from the One-Child Policy in China'
  doi: https://doi.org/10.1016/j.respol.2025.105334
  journal: Research Policy
  year: 2025
  dataset_role: CFPS 2010-2018 waves; mechanism testing for women's human capital, domestic burden, and gender attitudes
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733325001635
  data_note: >-
    Uses CFPS 2010-2018 to test four mechanisms linking One-Child Policy to women's innovation participation — (1) increased educational attainment, (2) reduced domestic chore burden, (3) weakened traditional gender role acceptance, (4) higher probability of remaining unmarried. Combined with CNIPA patents, Census, CMDS, and CSMAR. Instrument — provincial OCP fines. CFPS provides the individual-level mechanism evidence.
- cite: 'An, Qin, Wu & You (2024), The Local Labor Market Effect of Relaxing Internal Migration Restrictions: Evidence from China'
  doi: https://doi.org/10.1086/722620
  journal: JLE
  year: 2024
  dataset_role: CFPS household panel; labor market outcomes, hukou status, and subjective satisfaction with public services
  evidence_type: data-section
  evidence_url: https://www.journals.uchicago.edu/doi/10.1086/722620
  data_note: >-
    Uses CFPS household panel data combined with CMDS and Population Census to study how China's 2014 hukou reform affected local labor markets. CFPS provides individual-level labor market outcomes (wages, employment) and subjective satisfaction with social security services. Finds migrant workers' wages fell 2.6-7.9% post-reform — competition is concentrated among migrant workers with similar skills rather than between migrants and locals. Locals' subjective satisfaction with social security declined despite no wage penalty.
- cite: 'Qin, Yi & Zhang (2025), Quarter of Birth, Gender Inequality, and Economic Development'
  doi: https://doi.org/10.1086/737993
  journal: JLE
  year: 2025
  dataset_role: CFPS individual-level panel; lifecycle outcomes (education, labor market) linked to birth quarter
  evidence_type: replication
  evidence_url: https://opendata.pku.edu.cn/dataverse/pku
  data_note: >-
    Uses CFPS as a key micro dataset alongside six Census waves (1990-2020), CEPS, CHNS, statistical yearbooks, and meteorological data. CFPS provides individual-level lifecycle outcomes (education, employment, income) linked to birth quarter. Finds people born in Q4 have better lifecycle outcomes — effect significantly larger for females, driven by agricultural seasonality interacting with son preference in neonatal investment. Economic development (post-1979 reforms) reduces the gender gap in birth quarter effects.
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
- **Not suitable for**: local analysis when the approved geography or local sample does not support it, enterprise/industry level issues, research requiring monthly/quarterly observations, and historical tracking before 2010. Fine geographic access must be checked rather than assumed impossible or guaranteed.

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
- **CHARLS**: A separate survey recorded under Peking University's National School of Development, focusing on people aged 45+ and their spouses, with deeper aging and health measures. Consult the CHARLS record for its own application route; a CFPS account does not establish CHARLS access. Compare the surveys as alternatives or complementary evidence, not as automatically person-linkable samples.
- **CHNS / CGSS / CHFS**: Both are large-scale household micro-surveys that can cross-validate main statistics (income distribution, consumption patterns, education level).
- **Macro/Policy Data**: "Province/County Code" can be used to connect provincial statistical yearbooks and policy databases to construct regional policy impact variables.

## Remarks / Pitfalls
- **Population and local inference**: The record documents coverage of 25 provinces, with six excluded. That fact alone neither establishes every province's representativeness nor invalidates inference to the survey's target population. Check weights, sampling design and the intended subgroup before reporting local estimates.
- **Two-year interval**: The confirmed waves in this record are biennial. Do not describe interpolated intervening years as observed survey rounds, or assume every variable's reference period is the interview year.
- **Variable names change across rounds**: Each round of questionnaires is revised and variable names may change. Be sure to check the codebook and variable correspondence table of each round before merging across rounds.
- **Advanced Permission Stratification**: Core variables are free and open, but precise income, community codes, some province codes, etc. require additional application for advanced permissions (approval is more stringent).
- **Individual tracking rate**: The panel tracking rate is high (about 80–85%), but there is sample attrition—be careful to check attrition bias when doing long panels.
