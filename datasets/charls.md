---
schema_version: 2
catalog_status: ready
id: charls
name: China Health and Retirement Longitudinal Study (CHARLS)
aka:
- CHARLS
- 中国健康与养老追踪调查
- 中国健康与养老调查
- China Health and Retirement Longitudinal Study
- 北大CHARLS
provider: National School of Development, Peking University (NSD, National School of Development, Peking University)
china_related: true
domains:
- health
- labor
- development
- public
- aging
- consumption
- sociology
unit_of_observation: Individual-year/Family-year/Community-year (middle-aged and elderly people aged 45 and above and their
  spouses)
structure: longitudinal-panel
geo_granularity:
- personal
- family
- village/community
- County
- city
- province
geography: 28 provinces/cities/autonomous regions (150 counties/districts, 450 villages/communities) in mainland China, covering
  approximately 95% of China’s middle-aged and elderly population
time_span:
  start: 2011
  end: ongoing
  last_confirmed_release: 2022
  coverage_note: Six rounds confirmed for 2011/2013/2015/2018/2020/2022; 2–3 years apart
  last_checked: '2026-07-10'
frequency:
- irregular-biennial
sample_size: 'Baseline (2011): approximately 17,708 people/approximately 10,000 households; follow-up rate >85%; including
  middle-aged and elderly people aged 45 and above and their spouses (regardless of age)'
key_variables:
- Demographics (age/gender/marriage/hukou/education)
- Health status (self-rated health/chronic diseases/functional limitations ADL+IADL/depression CES-D/cognition)
- Physical measurements (height/weight/blood pressure/pulmonary function/grip strength/pace speed)
- Biomarkers (venous blood sample→HbA1c/CRP/total cholesterol/HDL/LDL, etc.)
- Medical care and insurance (medical behavior/hospitalization/medical expenditure/medical insurance type/reimbursement)
- Work and Retirement (Employment Status/Occupation/Industry/Retirement/Pension Type and Amount)
- Income and Consumption (Personal Income/Household Income/Household Expenditures/Assets and Liabilities)
- Family structure (child information/intergenerational transfers/care provision and receipt/living arrangements)
- Community level (village/community infrastructure/medical/elderly care services)
research_fit:
  best_for:
  - Health, cognition, retirement, pensions and intergenerational care in people aged 45 and over, including physical and
    selected biomarkers
  choose_over:
  - Prioritize CFPS when studying middle-aged and elderly health and retirement; use CFPS instead when studying all ages or
    children
  - Compare CHNS when studying long-term changes in deep diet; compare CHFS when studying household assets and liabilities
  not_good_for:
  - General population under 45 years old
  - child development
  - corporate research
  - Strictly Annual Panel
  needs_join_for:
  - New rural insurance and other policy time points and regional macro data need to be joined according to county/city/province
    codes, and fine codes may be limited.
  variation_available:
  - Personal and family tracking
  - mandatory retirement age
  - Pension policy implemented in phases
  - health shock
  topics:
  - retirement
  - Pension
  - pension
  - Raising children for old age
  - intergenerational transfer
  - Elder care
  - cognition
  - blood sample
  - retire
good_for:
- The impact of pension/retirement policies on the labor supply, consumption and health of middle-aged and elderly people
  - using the new rural pension insurance (NRPS) to implement DID by county and time (Gai et al. Econometrica Rural Pension
  Research Design)
- Long-term economic consequences of health shocks—trajectories of labor supply, income, and health expenditures in households
  after cardiovascular/diabetes onset
- Aging and Intergenerational Transfers—Determinants and Consequences of Money/Time Transfers from Adult Children to Elderly
  Parents
- Medical insurance and health - the causal effects of different medical insurance types (urban employees/residents/new rural
  cooperative medical care) on medical seeking behavior and health outcomes
- Retirement and cognitive decline - Estimating the impact of retirement on cognitive function and mental health using RD
  of mandatory retirement age
- Economics of care – substitution and complementarity of informal care (family/children) vs formal care (elderly care institution/nanny)
identification:
- Panel fixed effects (individual/household)
- DID (Policy County Time Sharing/Pension Reform)
- RD (retirement age)
- IV (policy exogenous impact/community characteristics)
linkable_keys:
- Personal ID
- Family ID
- Community ID (authorization required)
- County/city/province code
access_routes:
- route: pku-open-data
  access_status: available-with-application
  direct_url: https://opendata.pku.edu.cn/
  requirements: Registration, research instructions and data use agreement; sensitive variables such as community codes must
    be applied separately.
  steps:
  - Register on the Peking University Open Data Platform.
  - Search CHARLS and submit your application.
  - Download round data, questionnaire and biomarker files upon approval.
  deliverable: Public rounds of personal/household data; some biomarkers and sensitive geographic fields are provided by permission.
  cost: free
  last_checked: '2026-07-10'
access:
  url: 'https://charls.pku.edu.cn (CHARLS official website); Data application platform: https://opendata.pku.edu.cn/ (same
    platform as CFPS)'
  cost: free
  license: For academic research only, you need to register an account and sign a usage agreement
  format:
  - dta
  - csv
  api: false
  how_to_get: 1) Visit https://opendata.pku.edu.cn/ and register with an academic email or institutional documentation; 2) search for CHARLS and submit a data-use application; 3) after approval, download the available waves, questionnaires, and biomarker files. Access is free; community codes and other restricted fields require a separate application.
caveats: CHARLS only covers people aged 45+ (including spouses) - not applicable to all age questions (please use CFPS). Some
  rounds are spaced 2 years apart, some 3 years apart, and the frequency is not entirely uniform. Biomarker data are only
  collected in some rounds (2011/2015/2020), and some indicators require separate applications. Rural samples account for
  a relatively high proportion (about 60%), and urban middle-class elderly may be underrepresented.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: partial
  last_audited: '2026-07-10'
used_by:
- cite: 'Lei, Shen & Yang (2023), Digital Financial Inclusion and Subjective Well-Being: Evidence from China Health and Retirement
    Longitudinal Study'
  journal: CER
  year: 2023
  dataset_role: Main micro-data of middle-aged and elderly people; subjective well-being
  data_note: Using CHARLS data to study the causal effect of digital financial inclusion (mobile payment/digital banking)
    on the subjective well-being of middle-aged and elderly people
- cite: 'Fu, Ge, Huang & Shi (2022), The Effect of Education on Health and Health Behaviors: Evidence from the College Enrollment
    Expansion in China'
  journal: CER
  year: 2022
  dataset_role: Health and behavioral outcomes; combined with the impact of college enrollment expansion
  data_note: Using CHARLS middle-aged and elderly data + China's university enrollment expansion policy as an IV, it was found
    that education significantly improves the health behaviors and health outcomes of middle-aged and elderly people.
- cite: 'Wang, Jin & Yuan (2023), The Consequences of Health Shocks on Households: Evidence from China'
  journal: CER
  year: 2023
  dataset_role: Key tracking outcomes; health shocks, income, consumption and labor supply
  data_note: Using CHARLS tracking data to identify the dynamic causal effects of health shocks (cancer/cardiovascular/stroke)
    on household income, consumption and labor supply
- cite: 'Dai, Gong, Hu & Wei (2026), Rural Pension, Factor Reallocation and Agricultural Productivity: Evidence from China'
  journal: JDE
  year: 2026
  dataset_role: Middle-aged and elderly/pension results; combined with the new rural insurance policy
  data_note: Using CHARLS middle-aged and elderly tracking data + New Rural Security (NRPS) pension reform, we study how rural
    pensions improve agricultural productivity through labor reallocation channels
- cite: 'Guo, Huang & Wang (2025), Public Pensions and Family Dynamics: Eldercare, Child Investment, and Son Preference in
    Rural China'
  journal: JDE
  year: 2025
  dataset_role: Aged care and pensions results; linked to CFPS and census
  data_note: Using CHARLS + CFPS + 2015 mini-census triple data + new rural insurance DDD, it was found that public pensions
    reduced sons living together by 5.2pp, bride price decreased by 32%, and newborn sex ratio improved by 12.7pp - pensions
    fundamentally reshaped the tradition of 'raising children to provide for old age'
provenance:
- source: CHARLS official website https://charls.pku.edu.cn and Peking University Open Data Platform (confirm survey design,
    variable coverage and access conditions)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- cfps
- chns
- cgss
- uhs
---

## Positioning in one sentence
CHARLS is China’s most authoritative micro-tracking survey of middle-aged and elderly people’s health and retirement—launched in 2011 by the National School of Development at Peking University.
Every 2–3 years, approximately 17,000 middle-aged and elderly people aged 45+ are tracked on their health (including blood sample biomarkers), cognition, work, retirement, pension,
Full-dimensional data on intergenerational transfer and family economy. Available at no charge under the provider agreement, and on the same Peking University open data platform as CFPS.
It is irreplaceable micro data for studying China's aging, pension, health and retirement issues.

## Research questions suitable for answering/Typical identification strategies
- **Welfare effects of pension reform**: Using the differences in the implementation of China's new rural social pension insurance (NRPS) by county and year to do DID—how NRPS affects the labor supply, consumption, health and migration decisions of rural elderly people. Gai et al. (Econometrica 2025) put the NRPS into a spatial general equilibrium framework and estimated the impact of pensions on migration costs and total GDP.
- **Economic Consequences of Health Shock**: CHARLS contains venous blood samples (objective biomarkers such as blood sugar/blood lipids/CRP), which can identify new cases of chronic diseases such as cardiovascular/diabetes → track changes in income, medical expenditures, and labor supply before and after the onset of the disease.
- **Retirement and Health**: Use China's mandatory retirement age (male 60/female cadres 55/female workers 50) to do discontinuity regression - the causal effect of retirement on physical health (blood pressure/cognition), mental health (CES-D Depression Scale) and medical utilization.
- **Not suitable for use**: People under 45 years old (please use CFPS), non-China aging comparisons (international sibling surveys such as HRS/ELSA/SHARE can be used - CHARLS is their Chinese partner), child development (CFPS has a special project for 0-15 years old).

## Key variables/modules
- **Health status** (core value): self-rated health, self-report of 14 chronic diseases, ADL/IADL functional limitations, CES-D depression scale, cognitive testing (memory/calculation/clock drawing)
- **Physique and biomarkers**: Height/weight/waist circumference/blood pressure/pulmonary function/grip strength/pace speed; blood sample → HbA1c (diabetes)/CRP (inflammation)/total cholesterol/HDL/LDL/uric acid, etc.
- **Work and Retirement**: Employment status/industry/occupation, retirement status, pension type (urban employees/urban and rural residents/new rural insurance/government institutions)
- **Medical care and insurance**: Number of medical visits (outpatient + hospitalization), total medical expenditure and self-payment, type of medical insurance coverage
- **Intergenerational Economy**: Money and time help from children, transfer from the elderly to children, living arrangements, care acceptance (ADL help)
- **Community level**: Village/community infrastructure (school/hospital/nursing home), public services

## How to get
1. Visit https://opendata.pku.edu.cn/ and register with an academic email or institutional documentation.
2. Search for "CHARLS" to enter the data set page.
3. Submit a data use request (research purposes + sign a data use agreement - "Academic research only, no redistribution").
4. After passing the review (usually 1–3 weeks), all round data, questionnaires and biomarker data in Stata (.dta) format can be downloaded directly from the platform.
5. If you need sensitive variables such as community codes, you need to submit an application for advanced permissions to the CHARLS project team separately.

## Connections to other data
- **CFPS** (same platform): CFPS all ages, CHARLS 45+ - the middle-aged and older samples of both can be cross-validated, and the child/youth sample of CFPS makes up for the lower age limit of CHARLS.
- **International Comparison**: CHARLS is a member of the HRS (United States)/ELSA (UK)/SHARE (Europe) family - the questionnaire design has the same origin and can directly make international aging comparisons.
- **Macro/policy data**: Use "county code/city code" to connect policy impact variables such as NRPS implementation time, medical insurance policy, and supply of medical institutions.

## Remarks / Pitfalls
- **Minimum age limit is 45 years old** - does not cover youth/children/middle-aged people (spouse under 45 years old can be sampled but does not represent the overall age group).
- **Uneven intervals between rounds**: 2011→2013 (2 years)→2015 (2 years)→2018 (3 years)→2020 (2 years)→2022 (2 years). Pay attention to the annual panel.
- **Biomarkers only partial rounds**: 2011 and 2015 with full blood sample analysis, 2018 not collected, 2020 with partial metrics restored – be aware of data gaps when doing long-term health trajectories.
- **Death and loss to follow-up**: CHARLS has a special exit interview (retrospective interview with family members of deceased elderly people), and special weights are required when using cause-of-death data.
