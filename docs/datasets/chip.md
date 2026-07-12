---
schema_version: 2
catalog_status: ready
id: chip
name: Chinese Household Income Project (CHIP)
aka:
- CHIP
- CHIPs
- 中国家庭收入调查
- 中国居民收入调查
- Chinese Household Income Project
- 北京师范大学CHIP
provider: China Household Income Survey Project; organized by the School of Economics and Business Administration of Beijing
  Normal University since 2007, and has cooperated with the survey system of the National Bureau of Statistics for several
  rounds
china_related: true
domains:
- labor
- development
- consumption
- inequality
- poverty
- public
unit_of_observation: Individual/Family (three subsamples of urban, rural and post-2002 floating population)
structure: repeated-cross-section
geo_granularity:
- personal
- family
- province
geography: Each round selects representative provinces in the east, middle and west, and not all 31 provinces are covered;
  the specific provinces and sample frames change with the rounds.
time_span:
  start: 1988
  end: 2018
  last_confirmed_release: 2018
  coverage_note: The six public rounds are 1988/1995/2002/2007/2013/2018; CHIP2023 has been launched but is not listed as
    published data on the current application page.
  last_checked: '2026-07-10'
frequency:
- irregular-cross-section
sample_size: There are approximately 15,000-20,000 households in each round; each round is an independent cross-section and
  does not track the same household.
key_variables:
- Household and personal income
- wages and employment
- working time
- Business activities
- consumer spending
- family property
- education and health
- social security
- housing
- Household registration
- family relationship
- floating population
- land management
- loan
- retired
research_fit:
  best_for:
  - Long historical repeated cross-section of income distribution, poverty, wages and urban-rural gap in China from 1988 to
    2018
  - Comparable study on income and labor market of urban, rural and floating population
  choose_over:
  - When studying the history of income distribution from 1980s to 2000s, priority is given to CFPS/CHFS, which started in
    2010.
  - Use CFPS/CHFS when you need to track the same family; give priority to CHFS when you need the depth of assets and liabilities.
  - When the strict measurement definition of NBS original UHS/RHS is required, CHIP cannot be directly regarded as the same survey.
  not_good_for:
  - Personal or family panel cause and effect tracing
  - Requires continuous observation every year
  - Provincial representative estimates of the country’s 31 provinces
  needs_join_for:
  - Regional policies and macro indicators can usually only be joined by province/year at the public geographic level
  variation_available:
  - Six historical sections
  - Urban-rural and floating population samples
  - Income distribution and institutional period changes
good_for:
- Long-term income inequality, poverty and income source disaggregation
- Wage gaps, returns to education, and labor market transformations
- Comparison of income, consumption and social security between urban and rural areas and floating population
identification:
- Duplicate Section DID
- Age-period-cohort analysis
- Regional policy differences
- Distribution decomposition
linkable_keys:
- Province
- Survey year
- Urban and rural/migrant population sample identification
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province
  - Year
  method: aggregate-level
  evidence_status: plausible
- target: uhs
  relation: related-sampling-frame
  keys:
  - Year
  - town sample
  method: harmonized-comparison
  evidence_status: official-description
access_routes:
- route: bnu-chip-platform
  access_status: available-with-application
  direct_url: http://chip.bnu.edu.cn/
  requirements: Register an account, select the CHIP data sub-project and submit the application.
  steps:
  - Register an account on the China Household Income Data Sharing Platform.
  - After logging in, select the desired CHIP year sub-project and submit the application.
  - Administrators usually review within 2 working days.
  - After passing the review, download it from the link in the email; the official reminder link will be valid within 5 days.
  deliverable: CHIP1988/1995/2002/2007/2013/2018 approved data and related documents.
  cost: free
  last_checked: '2026-07-10'
access:
  url: http://chip.bnu.edu.cn/
  cost: free
  license: Used for academic research; implemented in accordance with the platform agreement and results feedback requirements
  format:
  - unknown
  api: false
  how_to_get: Register at chip.bnu.edu.cn, select the CHIP sub-project of a specific year and submit the application; it usually
    takes 2 working days to review, and the download link will be sent by email and must be used within 5 days.
caveats: The six rounds are repeated cross-sections rather than household panels; provinces and questionnaires change across
  rounds. The CHIP sample comes from the NBS regular household survey large sample frame and has an independent questionnaire
  design, which cannot be equated with the UHS/RHS original micro data.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: none
  last_audited: '2026-07-10'
used_by: []
provenance:
- source: https://bs.bnu.edu.cn/zgjmsrfpdcsjk/sjjs/index.html
  field_scope:
  - identity
  - waves
  - sample
  - structure
  - variables
  - sampling
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://bs.bnu.edu.cn/zgjmsrfpdcsjk/sjsq/index.html
  field_scope:
  - access
  - application_steps
  - released_waves
  added: '2026-07-10'
  confidence: high
  verified: true
related_datasets:
- id: uhs
  relation: related-sampling-frame
- id: rhs
  relation: related-sampling-frame
- id: cfps
  relation: substitute
- id: chfs
  relation: substitute
---

## Positioning in one sentence

CHIP is a long-term repeated cross-section of China's income distribution and labor market research, covering six rounds of urban, rural and later migrant population samples from 1988 to 2018. Its biggest advantage is the historical span and income details, its biggest limitation is that it cannot track the same household.

## Select rules

- Studying income distribution, poverty and wage history since reform and opening up: Priority CHIP.
- Requires home panel: use CFPS/CHFS instead.
- Full balance sheet required: CHFS preferred.
- CHIP has a sampling partnership with the NBS Household Survey, but they are not the same data product with interchangeable names.

## Get recipe

Register at `chip.bnu.edu.cn`, choose the subproject for the required wave, and submit an application. The provider states that review usually takes two working days; approved download links are sent by email and normally expire after five days.
