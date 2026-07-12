---
schema_version: 2
catalog_status: grounding
id: uhs
name: China Urban Household Survey (UHS)
aka:
- UHS
- 城镇住户调查
- 城市住户调查
- 中国城镇住户调查
- Urban Household Survey
- NBS Urban Household Survey
- 中国城市住户调查
provider: National Bureau of Statistics (NBS, National Bureau of Statistics of China)
china_related: true
domains:
- labor
- development
- public
- consumption
- health
- education
- macro
unit_of_observation: Household-Year/Individual-Year/Journal (three-layer structure, flexible aggregation)
structure: rotating-or-partial-panel
geo_granularity:
- province
- city
- household
- personal
geography: Urban areas in mainland China; covered some representative provinces in the early stage, and expanded to the whole
  country after 2002
time_span: 1986–2015 (the commonly used version in academia ends around 2009; there are major changes in measurement definition around 2002)
frequency:
- annual
- monthly (journal)
sample_size: 'Early period (1986): about 12,437 households/47,221 people; 1992–2001: about 5,500 households (9 provinces);
  expanded to about 16,000–140,000+ households/year after 2002; a total of more than 140,000 households from 2002–2009'
key_variables:
- total household income
- salary income
- operating income
- property income
- Transfer income (public + private)
- 消费支出(八大类: Food/clothing/medical/transportation and communication/education/housing/miscellaneous)
- Age of family members
- gender
- education level
- Employment status
- Career type
- Industry
- housing type
- Housing area
- housing property rights
- family demographics
good_for:
- The impact of retirement on consumption - Using China's mandatory retirement age to do regression discontinuity (RD)
- Micro-observation and decomposition of income inequality and consumption inequality - within cities and towns, across provinces/cross
  industries
- Household consumption responds to policy shocks (tax reform/subsidies/pension reform)—panel DID
- Micro-level estimates of labor supply, education returns, and gender wage gaps
- The impact of housing spending/changes in housing ownership on household savings and consumption
- Income shocks and consumption smoothing—micro-evidence at the household level
identification:
- Panel Fixation Effect (Household/Year)
- RD (Mandatory Retirement Age/Policy Break)
- DID (policy pilot/inter-provincial differences)
- IV (Exogenous Changes in Family Structure/Policy)
linkable_keys:
- Province code
- city code
- Household Code (Internal)
- It can be compared at the macro level with CHIP/CHFS/CFPS
research_fit:
  best_for:
  - NBS annual historical micro-study of urban household income, consumption, and employment, especially the design of mandatory
    retirement age
  choose_over:
  - Select UHS when NBS urban household annual measurement definition and specific historical versions are required
  - If you do not have NBS authorization and are researching income distribution history, priority is given to applying for
    independent CHIP; CFPS/CHFS is needed for home panels after 2010
  not_good_for:
  - Download now and publicly
  - Rural families
  - UHS became independent after 2016
  - Complete balance sheet
  needs_join_for:
  - Policies and macro variables need to be stitched together by province/city and year
  variation_available:
  - Annual household records
  - mandatory retirement age
  - Differences in interprovincial policies
access:
  url: https://microdata.stats.gov.cn/
  cost: by-application
  license: For academic research only, a confidentiality agreement is required; Most researchers use it indirectly through
    partner institutions or public subsamples (CHIP).
  format:
  - dta
  - csv
  api: false
  how_to_get: Confirm whether the target UHS year can be applied for at the Micro Data Laboratory of the National Bureau of
    Statistics, and submit the project according to controlled usage requirements. If it is impossible to obtain and study
    income distribution history, apply for independent CHIP data; CHIP is associated with the NBS sampling frame, but it is not
    a synonymous subsample of the UHS raw data.
caveats: Around 2002, there were significant changes in questionnaires, variable definitions, and sampling scopes (starting
  in 2002, non-urban household registration residents residing in towns). When making cross-period comparisons, variables
  need to be aligned item by item. Housing spending around 2007 was severely discontinuous and multi-negative. Original micro-level
  data are not publicly available—most scholars actually use CHIP subsamples or truncated versions obtained through institutional
  collaboration. After 2015, UHS was integrated into the National Household Income and Living Conditions Survey and no longer
  exists independently.
access_routes:
- route: NBS microdata laboratory application
  access_status: needs-verification
  direct_url: https://microdata.stats.gov.cn/
  requirements:
  - formal research project
  - Relying institution
  - Pass review and sign a confidentiality or controlled use agreement
  - Use in designated safe environment
  steps:
  - Confirm that the target UHS year is still in the available list
  - Submit project, variant and usage requests
  - Wait for review and sign the agreement
  - Using data in approved environments and complying with non-redistributable requirements
  deliverable: Approved UHS microdata or controlled access permissions; The year, fields, and removal range are subject to
    the approval results
  cost: by-application
  last_checked: '2026-07-10'
- route: CHIP substitute application
  access_status: available-with-application
  direct_url: http://chip.bnu.edu.cn/
  requirements:
  - Submit your application according to the CHIP project requirements
  - Accept CHIP's independent licensing and data usage terms
  steps:
  - Confirm the CHIP target wave, questionnaire, and variables
  - Submit your application via the CHIP project page
  - Download or use within the scope of the license after approval
  - The paper clearly states that CHIP is not a synonymous subsample of UHS raw data
  deliverable: CHIP's independently investigated controlled data products; It cannot claim UHS original data
  cost: by-application
  last_checked: '2026-07-10'
quality:
  profile_status: partial
  access_status: needs-verification
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: Li, Shi & Wu (2015), The Retirement Consumption Puzzle in China
  journal: AER (P&P)
  year: 2015
  data_note: Using UHS urban household survey micropanel data and mandatory retirement age for RD, it is estimated that the
    causal effect of retirement on household nondurable goods consumption (decreased by about 20%)
- cite: 'Cai & Zhao (2024), Uniform Agricultural Tax Abolition and Differential Household Labor Supply: Evidence from China''s
    Urban Household Survey'
  journal: CER
  year: 2024
  data_note: Using UHS data, the abolition of agricultural tax is used to study the differentiated impact of abolishing agricultural
    taxes on urban household labor supply—abolishing agricultural taxes indirectly affects urban residents' behavior through
    food price channels
provenance:
- source: Crossref abstract for https://doi.org/10.1257/aer.p20151007 (supports use of China's Urban Household Survey)
  added: '2026-07-08'
  confidence: high
  verified: false
- source: Central University of Finance and Economics CHIP Project Documentation and UHS Usage Instructions from Multiple
    Universities (including questionnaire structure, sampling methods, and list of variables)
  added: '2026-07-08'
  confidence: high
  verified: false
related_datasets:
- chip
- cfps
- chfs
- chns
- cgss
---

## Positioning in one sentence
The China Urban Household Survey (UHS) is a continuous urban household income and expenditure survey conducted by the National Bureau of Statistics since 1986.
Covering core micro-variables such as income, consumption, employment, and housing, it is a classic data source for research on urban household consumption and labor supply in China.
Due to its panel structure and long duration, it is especially suitable for causal identification of life cycles such as "retirement-consumption" and "income shock-consumption smoothing."
However, the original data is not publicly available. CHIP can serve as a practical alternative, but it has independent questionnaire and publishing platforms and cannot be considered the same data product as UHS.

## Research questions suitable for answering/Typical identification strategies
- **The Mystery of Retirement Consumption**: Using the mandatory retirement age of 60 for men and 50–55 for Chinese women as a breakpoint regression (RD), we estimate the causal effects of retirement on various household consumption expenditures (classic practice from Li, Shi & Wu 2015 AER).
- **Income Inequality and Consumption Inequality**: Using long panels to break down income and consumption gap trends within towns (coverage expanded around 2002 was an important structural breakpoint).
- **Consumption Effects of Tax Reform/Subsidy/Pension Reform**: Leveraging policy differences across provinces and years for DID.
- **The Impact of Housing on Household Behavior**: Changes in housing ownership and housing expenditure affect household savings rates, consumption structure, and labor supply (attention should be paid to the quality of housing expenditure data around 2007).
- **Education Return Rate / Gender Wage Gap**: At the individual level, there is education level and employment income, which can be done using the Mincer equation and gender decomposition.
- **Not suitable for**: rural households (UHS only for urban areas; rural areas require the Rural Household Survey RHS or CHNS/CFPS), after 2015 (UHS has been incorporated into the new National Household Income and Expenditure Survey), and those requiring detailed household investment/asset information (UHS focuses on income and expenditure flow, asset information is limited).

## Key variables/modules
- Income Module (Tiered): Wage income, operating income, property income, transfer income (from public and private transfers)
- Consumption Module (Eight Major Categories): Food (including at home/out), clothing, household appliances, healthcare, transportation and communications, education, culture and entertainment, housing, miscellaneous
- Population characteristics module: age, gender, education level, employment status, occupation, industry, family relationships
- Housing module: housing type, building area, property ownership type

## How to get
1. **Raw UHS Micro Data**: First, confirm whether the target year is in the applicable catalog at the Micro Data Laboratory of the National Bureau of Statistics; It must be operated by an institution and used according to controlled environment requirements.
2. **CHIP Alternatives**: Six independent surveys were submitted from the Beijing Normal University CHIP platform, suitable for income distribution and labor market history research, but not UHS original data.
3. **Internal Use of Partner Institutions**: Some universities may hold authorized years and must apply according to internal regulations.

## Connections to other data
- **CHIP** is associated with the NBS household survey sampling box and can serve as a proxy for historical income distribution and macro comparison, but it has independent questionnaire and data product identities.
- Compared to **CFPS / CHFS**: also a household micro-survey that can cross-validate consumption/income distribution, but with different coverage years and sampling frames.
- Macro level: "Province codes" can be used to connect provincial statistical yearbooks and policy databases to build regional-level policy impact variables.

## Remarks / Pitfalls
- **2002 was the biggest breakthrough**: In 2002, UHS underwent major reforms—the sampling range expanded from "urban residents" to "all households living in urban areas" (including non-registered populations such as migrant workers), with sample sizes increasing from 5,500 to 16,000+ households, and significant changes in variable definitions. When making panels around 2002, you need to check continuity variably by variable.
- **Unreliable housing expenditure data**: Around 2007, the methods for estimating housing rents changed, with many negative values and abnormal jumps—most studies either avoided housing expenditures or treated them as conuter.
- **Raw data not open** — This is the biggest threshold for UHS. If there is no authorization from a partner institution, it is recommended to directly replace it with CHIP or switch to CFPS/CHFS.
- **UHS Has Ended**: After 2015, the National Bureau of Statistics merged urban and rural household surveys into the 'National Household Income and Living Conditions Survey,' and UHS ceased to operate independently. Micro-level data on urban households after 2016 should be accessed through the new survey system.
