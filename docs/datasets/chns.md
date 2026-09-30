---
schema_version: 2
catalog_status: ready
id: chns
name: China Health and Nutrition Survey (CHNS)
aka:
- CHNS
- 中国健康与营养调查
- China Health and Nutrition Survey
- 中国营养与健康调查
- 北卡CHNS
provider: Jointly implemented by the UNC Carolina Population Center and the Institute of Nutrition and Health, Chinese Center
  for Disease Control and Prevention (NINH, China CDC)
china_related: true
domains:
- health
- nutrition
- labor
- development
- demography
- sociology
unit_of_observation: Individual-Year/Family-Year/Community-Year (Track Panel Design)
structure: longitudinal-panel
geo_granularity:
- personal
- family
- community
- County
- province
geography: Initially covering 9 provinces (Liaoning/Heilongjiang/Jiangsu/Shandong/Henan/Hubei/Hunan/Guangxi/Guizhou); after
  2011, Beijing/Shanghai/Chongqing was added; in 2015, Shaanxi/Yunnan/Zhejiang were added - the coverage gradually expanded
time_span:
  start: 1989
  end: ongoing
  last_confirmed_release: 2018
  coverage_note: A total of 11 rounds from 1989 to 2018 have been confirmed; the intervals between rounds are 2–4 years
  last_checked: '2026-07-10'
frequency:
- irregular
sample_size: 'Baseline (1989): about 3,800 households/15,000 people; subsequent rounds tracking rate >80%; cumulative coverage
  of about 4,400 households/26,000 people'
key_variables:
- Demographics (age/gender/marriage/education/hukou)
- Health (self-rated health/chronic diseases/blood pressure/BMI/functional status)
- Nutrition (Dietary Intake/24-Hour Review/Food Frequency/Macro and Micronutrients)
- Physical measurement (height/weight/waist/hip/triceps skinfold thickness/bioimpedance antibody composition)
- Labor Force (Employment/Occupation/Industry/Income/Hours Worked)
- Household economy (household income/consumption/assets/housing)
- Community (Infrastructure/Market/Medical Institution/Food Price)
- Reproductive history
- Time allocation (housework/caregiving)
- Smoking and drinking
- physical activity
research_fit:
  best_for:
  - Long panel of dietary intake, food prices, body measurements, and nutritional health since 1989
  - Urban housing tenure, self-reported rental values, housing quality, and household adjustment around the 1994 housing reform,
    when the early nine-province panel and urban-only sample are acceptable
  choose_over:
  - Prioritize CHNS over CFPS/CHARLS when detailed diet, food prices, body measurements, and long-run nutrition transitions are central
  - Compare CHARLS when studying biomarkers over age 45 and in retirement; switch to CHFS when studying household assets and
    liabilities
  - Choose CHNS over later household surveys when the research needs a pre-1994 and early post-reform urban household panel with
    self-reported housing values; use CHFS/CFPS instead for broader housing-wealth or nationally representative urban coverage
  not_good_for:
  - Requires representation from 31 provinces across the country
  - Strictly Annual Panel
  - Fine assets and liabilities
  - social attitudes
  - Transaction-level or nationally representative house-price series; CHNS reports household housing measures rather than a
    complete market transaction database
  needs_join_for:
  - Policies and macro-environment need to be joined by community/province and year
  variation_available:
  - Personal family long panel
  - community food prices
  - Urbanization and changes in community facilities
good_for:
- Nutrition Transition - the long-term trend and health consequences of the dietary structure of Chinese residents changing
  from grains to high-fat/high-sugar/processed foods
- Long-term tracking of obesity and chronic diseases - cross-life cycle changes in BMI/waist circumference/blood pressure
  and their association with diet/income/urbanization
- Intergenerational transmission of health inequalities – the causal effects of parental health/nutritional status on children’s
  health and socioeconomic outcomes in adulthood
- Food Prices and Consumption Behavior—The Impact of Community-Level Food Price Changes on Household Nutritional Intake and
  Health
- Economic shocks and health – immediate and lagged effects of income shocks/financial crises/food price fluctuations on nutritional
  status
- China’s longest micro-panel, tracking across 30 years from 1989–2018, is a unique resource for studying life cycle and cohort
  effects
identification:
- Panel fixed effects (individual/household/community)
- DID (Policy/Food Prices/Community Changes)
- IV (price/policy shock)
- Brothers and sisters FE
- Age-period-cohort decomposition
linkable_keys:
- Personal ID
- Family ID
- Community ID (authorization required)
- Provincial code
access_routes:
- route: unc-chns
  access_status: available-with-application
  direct_url: https://www.cpc.unc.edu/projects/china
  requirements: Register an account and indicate the purpose of academic research.
  steps:
  - Register on the CHNS official website.
  - Submit a research use application.
  - After approval, download each round of data, questionnaire and codebook.
  deliverable: CHNS public rounds of SAS/Stata data and documents.
  cost: free
  last_checked: '2026-07-10'
- route: CHNS confidential/community/spatial data agreement
  access_status: available-with-conditions
  direct_url: https://www.cpc.unc.edu/projects/china/data/datasets/DataUseAgreementCHNS_20201020.pdf
  requirements:
  - Complete the CHNS data-use agreement and name the authorized research team and institution.
  - For community, county, or spatial data, obtain local IRB/ethics approval and describe the data-security controls.
  - Budget the provider's stated processing and linkage fees; the official agreement is dated 2018/2020 and should be rechecked
    before a new application.
  steps:
  - Apply for the household/individual files through the CHNS portal and identify any community, county, or external-link request.
  - If a spatial or county-level join is needed, submit the agreement, IRB materials, team list, and security plan to CHNS staff.
  - Use the staff-mediated join rather than attempting to recover or distribute community coordinates; retain the approved linkage
    definition and any obfuscation in the project log.
  deliverable: Household/individual files may be distributed free of charge; community/county files and administrative or spatial
    joins are controlled deliverables whose fields, geography, and fees depend on approval.
  cost: mixed
  last_checked: '2026-08-11'
  caveat: The agreement says geocoordinates are never distributed as-is and that external joins are performed or reviewed by CHNS
    staff; do not treat the public household files as carrying unrestricted community coordinates.
access:
  url: https://www.cpc.unc.edu/projects/china (UNC CHNS official website)
  cost: free
  license: For academic research only, you need to register an account and sign a usage agreement
  format:
  - dta
  - sas
  - csv
  api: false
  how_to_get: 1) Visit https://www.cpc.unc.edu/projects/china → register an account; 2) Submit a data use application (fill
    in name/institution/research purpose); 3) Download all rounds of data, questionnaires and codebooks after passing the
    review (usually 1–2 weeks). Free. Data formats are available in SAS and Stata.
caveats: The longest advantage of CHNS is also its complexity - the 11-round questionnaire structure and variable definitions
  have undergone many major changes (especially 1997/2004/2011), and each round codebook needs to be carefully checked before
  merging across rounds. Provincial coverage was expanded to include large cities only in 2011. In the early days, the nine
  provinces were not representative of the country. Panel tracking has sample attrition—selective exit needs to be checked
  when doing a full 30-year panel. Dietary data (24-hour recall) is for 3 consecutive days - subject to recall bias and daily
  fluctuations.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-08-11'
used_by:
- cite: 'Zhao & Qu (2024), Place-Based Policies, Rural Employment, and Intra-Household Resources Allocation: Evidence from
    China''s Economic Zones'
  journal: JDE
  year: 2024
  dataset_role: Intra-household resource allocation and labor results; combined with development zone policy timing
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v167y2024ics0304387823001669.html
  data_note: Using CHNS 1997-2011 tracking data + the establishment of development zones as a quasi-experiment (simple + structural
    collective family model), it was found that development zones improve gender equality within families by creating non-agricultural
    employment for women → female household resource share ↑1.68pp, girls dropping out of school ↓ > 4% - industrial policy
- cite: 'Wang (2011), State Misallocation and Housing Prices: Theory and Evidence from China'
  doi: https://doi.org/10.1257/aer.101.5.2081
  journal: AER
  year: 2011
  dataset_role: CHNS urban household panel for housing consumption, self-reported rental values, housing quality, and province-level
    housing-price comparisons around the 1994 reform
  evidence_type: article_and_replication
  evidence_url: https://www.nyudri.org/assets/publications/2011/statemisallocation.pdf
  data_note: >-
    The AER data section identifies nine provinces, a multistage random-cluster design, approximately 4,400 households, and six
    waves (1989, 1991, 1993, 1997, 2000, and 2004). The analysis is restricted to urban households because the housing reform
    was urban; it uses self-reported monthly market rental value, floor space, utilities, ownership status, and household
    characteristics, with rental values deflated to real 1990 RMB. The official E112454V1 deposit exposes
    `data_aersubmit.dta`, two Stata do-files, and `readme.pdf`, but the file manifest does not list the raw CHNS wave files;
    downloading the deposit therefore supplies a paper-specific analysis/replication artifact, not an unrestricted replacement
    for the CHNS application route.
- cite: 'Cheng & Xu (2025), The Effect of Broadband Internet on Children''s Weight: Evidence from China'
  doi: https://doi.org/10.1016/j.chieco.2025.102540
  journal: CER
  year: 2025
  dataset_role: CHNS ten-wave panel 1989-2015; main child anthropometric outcomes matched to broadband infrastructure
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001981
  data_note: Uses CHNS 10 waves (1989-2015) to study how broadband internet expansion affects children's weight outcomes. Exploits China's 2000-2001 national internet exchange center construction as exogenous variation for staggered DiD. Finds broadband increases overweight probability by 14.14pp per SD, driven by increased sedentary screen time, reduced physical activity, and higher snack/calorie intake. Effects stronger for older and urban children.
- cite: 'Author (2026), The Impact of Urbanization on Child Growth: Evidence from City-County Mergers in China'
  doi: https://doi.org/10.1016/j.regsciurbeco.2025.104187
  journal: RSUE
  year: 2026
  dataset_role: CHNS child anthropometric panel (stunting and wasting outcomes) 2000-2019
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0166046225000699
  data_note: Uses CHNS longitudinal child anthropometric data (stunting and wasting rates) matched with county-level panel data (1,594 counties, 2000-2019) to study how city-county merger (CCM) urbanization affects children's physical growth. Finds CCM urbanization significantly reduces child stunting through improved maternal education, health service access, and household income. CHNS provides the longitudinal nutrition and health outcome measures.
- cite: 'Hu, Liu & Wen (2024), Working Hours and Employee Health: Evidence from China''s Workweek Reduction Policy'
  doi: https://doi.org/10.1016/j.labeco.2024.102543
  journal: Labour Economics
  year: 2024
  dataset_role: CHNS panel 1991-2000; main health and employment outcomes for workweek reduction analysis
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0927537124000381
  data_note: >-
    Uses CHNS data from 1991-2000 to study the health effects of China's 1995 Workweek Reduction Policy (48 to 40 hours). DID estimates find the workweek reduction adversely affected health — state employees became 3.5pp less likely to report good health and had higher odds of being overweight (+4.8pp) and sick (+2.8pp). Negative health effect partially explained by increased alcohol consumption, particularly among male workers. Income and nutrition intake remained unaffected.
- cite: 'Qin, Yi & Zhang (2025), Quarter of Birth, Gender Inequality, and Economic Development'
  doi: https://doi.org/10.1086/737993
  journal: JLE
  year: 2025
  dataset_role: CHNS data as supplementary validation for birth quarter effects on lifecycle outcomes
  evidence_type: replication
  evidence_url: https://opendata.pku.edu.cn/dataverse/pku
  data_note: >-
    Uses CHNS as one of multiple micro datasets (alongside Census 1990-2020, CFPS, CEPS, statistical yearbooks, and meteorological data) to study how birth quarter affects lifecycle outcomes in China. Finds Q4 births have better outcomes, with effect significantly larger for females — driven by agricultural seasonality interacting with son preference in neonatal investment. Economic development reduces the gender gap in birth quarter effects.
provenance:
- source: https://www.aeaweb.org/articles?id=10.1257%2Faer.101.5.2081
  field_scope:
  - final AER article identity, DOI, and regional/urban JEL scope
  - paper's housing reform question and replication-package link
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.nyudri.org/assets/publications/2011/statemisallocation.pdf
  field_scope:
  - CHNS nine-province, six-wave, approximately 4,400-household scope
  - urban-only analysis sample and housing/rental-value variables
  - paper-specific construction and limits of the housing-price proxy
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/112454/version/V1/view
  field_scope:
  - E112454V1 identity, citation, version, and public project boundary
  - depositor-versus-ICPSR processing disclaimer
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/112454/version/V1/view?path=%2Fopenicpsr%2F112454%2Ffcr%3Aversions%2FV1%2Faer_wang_data_files
  field_scope:
  - visible `data_aersubmit.dta`, Stata do-files, and README file manifest
  - deposited derived artifact versus raw CHNS boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.cpc.unc.edu/projects/china/data/datasets/DataUseAgreementCHNS_20201020.pdf
  field_scope:
  - household/individual versus community/county/spatial access distinction
  - IRB, security, fee, and staff-mediated linkage conditions
  added: '2026-08-11'
  confidence: high
  verified: true
- source: CHNS official site https://www.cpc.unc.edu/projects/china (supports survey design, waves, variable coverage, and access conditions)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: CHNS data documentation and technical report (confirming longitudinal weights, dietary data collection methods,
    and anthropometric protocols)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- cfps
- charls
- cgss
- chfs
---

## Positioning in one sentence
CHNS (China Health and Nutrition Examination Survey) is China's **longest longevity tracking panel survey** jointly conducted by UNC and the Chinese Center for Disease Control and Prevention since 1989——
Spanning 30 years and 11 rounds of data, with **Nutrition and Health** as the core variable (including 24-hour dietary recalls, body measurements, and community food prices),
It is the "golden long panel" for studying China's nutritional transformation, obesity epidemic and health inequality.
Compared with CFPS/CHARLS, CHNS’s depth of dietary and nutritional indicators is unmatched by any other Chinese micro-survey.
However, its provincial coverage (only 9 provinces in the early stage) and round frequency (ranging from 2–4 years) are not as good as CFPS.

## Research questions suitable for answering/Typical identification strategies
- **Nutrient Transition**: China's 30-year dietary changes from "not enough to eat" to "eating too well/eating wrong" - CHNS uses a 24-hour dietary review + food weighing method to record what and how much each respondent ate at each meal → macro and micronutrient intake can be directly calculated → associated with obesity/chronic disease/death.
- **Obesity Epidemic**: CHNS is the best data available to study time trends in BMI and waist circumference in China - from 1989 (when China's obesity rate was almost zero) to 2018 (when overweight/obesity rates were close to those in developed countries), CHNS's 30 years of anthropometric data cannot be replaced by other surveys.
- **Intergenerational Health Transmission**: CHNS tracks multiple generations of family members → can study the impact of parents' nutrition/health on children's adult outcomes - this is the classic design of the "Fetal Origin Hypothesis" and "Early 1000 Days of Life" in development economics.
- **Not suitable for**: Accurate income/asset measures (please use CFPS/CHFS), mid-life and above health (45+ please use CHARLS), attitudes/values (please use CGSS), agricultural production details (please use RHS).

## Key variables/modules
- **Meal Module** (the most unique to CHNS): 24-hour meal review for 3 consecutive days (record food name/weight/cooking method of each meal) + household food inventory weighing + community food prices → personal daily intake of energy/protein/fat/carbohydrates/vitamins/minerals can be calculated
- **Anthropometric measurements**: Height, weight, waist circumference, hip circumference, and triceps skinfold thickness—all measured by interviewers rather than self-reported
- **Blood pressure**: systolic blood pressure/diastolic blood pressure - take the average of three measurements
- **Health**: Self-assessed health, chronic medical history (hypertension/diabetes/myocardial infarction/stroke), functional status
- **Workforce**: Employment/Occupation/Industry/Income/Working Hours/Work Intensity
- **Community module**: market/supermarket/hospital/clinic/school/transportation - including food prices at the community level (rice/noodles/pork/eggs/vegetables, etc.)

## How to get
1. Visit https://www.cpc.unc.edu/projects/china → Register an account.
2. Submit a data use request (name, institution, brief research purpose).
3. After approval (usually 1–2 weeks) → Download all 11 rounds of data (SAS/Stata format) + questionnaire PDF + codebook on the website.
4. Publicly available at no charge - one of the lowest access barriers among micro surveys in China.

## Connections to other data
- **CFPS**: The nutritional and dietary depth of CHNS far exceeds that of CFPS, but the sample size (~26,000 people) and provincial coverage (early 9 provinces) are not as extensive as CFPS (~15,000 households/25 provinces). The two can be cross-validated on common variables such as income/consumption/education.
- **CHARLS**: CHARLS's 45+ sample of middle-aged and older adults and the overlapping population of CHNS can be analyzed jointly - CHARLS with blood biomarkers, CHNS with diet and long-term tracking.
- **Statistical Yearbook/Price Data**: Use "community/year" to connect food price CPI/agricultural production data.

## Remarks / Pitfalls
- **Limited provinces in early years**: 1989–2009 only 9 provinces → not nationally representative. After 2011, it was gradually expanded to Shanghai/Beijing/Chongqing/Zhejiang, etc.—you need to pay attention when making nationwide inferences.
- **Unequal intervals between rounds**: 1989 → 1991 (2 years) → 1993 (2 years) → 1997 (4 years) → 2000 (3 years) →… → 2018 (3 years) - Panels with unequal wounds are not suitable for "annual" frequency research designs.
- **Meal recall bias**: The 24-hour meal recall relies on the respondent's memory, and certain 3 days of "3 consecutive days" may not be representative of the "usual diet" - it needs to be smoothed by the average of multiple days.
- **Changes in variable names and questionnaires**: 11 rounds, 30 years - changes in questionnaires and variable names are inevitable. Be sure to use CHNS's "Longitudinal Master ID" file and variable comparison table before merging panels.
