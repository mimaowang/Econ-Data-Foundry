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
  - Wei–Zhang-style savings analysis needs a Census-derived county/city sex-ratio measure matched to the CHIP sample geography;
    the paper's public appendix does not provide a general-purpose join key
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
  evidence_status: plausible
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
- route: ICPSR 21741 public-use CHIP 2002
  access_status: available
  direct_url: https://www.icpsr.umich.edu/web/DSDR/studies/21741
  requirements:
  - Create or sign in to an ICPSR account if prompted; the study page states that public-use access does not require ICPSR member affiliation.
  - Accept the current ICPSR terms and cite the study as instructed.
  steps:
  - Open the ICPSR 21741 study page and confirm version V1 and the 2002 collection.
  - Read the study description and codebooks before choosing the urban, rural, migrant, household, or village files.
  - Download the public-use files and documentation, then reproduce the paper's sample restrictions and the merge to Census-derived county/city measures separately.
  deliverable: Ten public-use CHIP 2002 files covering urban, rural, rural-urban migrant, household, individual, and village units, with ICPSR documentation.
  cost: free
  last_checked: '2026-08-11'
  caveat: This is a public-use 2002 archive held by ICPSR, not the current BNU application route for every CHIP wave; ICPSR documents its own disclosure review and file processing.
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
  paper_use_status: verified
  last_audited: '2026-08-11'
used_by:
- cite: 'Wei & Zhang (2011), The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings Rates in China'
  doi: https://doi.org/10.1086/660887
  journal: JPE
  year: 2011
  dataset_role: CHIP 2002 rural and urban household surveys for household-level savings regressions
  evidence_type: paper_and_data_appendix
  evidence_url: https://users.nber.org/~confer/2009/China09/wei.pdf
  data_note: >-
    The data appendix identifies the 2002 Chinese Household Income Project as the source for the household-level regressions,
    covering 122 rural counties and 70 cities. The savings rate is defined as log(income/consumption); the reported tables
    restrict samples to households with both parents alive and a household head younger than 40. County-level sex ratios are
    merged from the Population Census, so CHIP 2002 supplies the household outcomes while the Census supplies the external
    regional measure. The public ICPSR archive is the obtainable starting artifact; the paper's exact restricted/cleaned analysis
    file is not implied by downloading all ten public-use files.
- cite: 'Piketty, Yang & Zucman (2019), Capital Accumulation, Private Property, and Rising Inequality in China, 1978–2015'
  journal: AER
  year: 2019
  dataset_role: Wealth distribution microdata (1995 and 2002 waves); combined with CFPS wealth surveys for long-run wealth inequality
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/116194/
  data_note: Used CHIP 1995 and 2002 wealth survey microdata together with CFPS 2010/2012 to construct long-run wealth inequality
    series for China's Distributional National Accounts. Combined with NBS national accounts, household survey income tables,
    tax data on top earners, and Hurun rich list.
- cite: 'Author (2026), Tasks and the Gender Wage Gap in Urban China, 2002-2023'
  doi: https://doi.org/10.1016/j.chieco.2026.102740
  journal: CER
  year: 2026
  dataset_role: CHIP 2002/2013/2023 individual-level wage and occupation data; main outcome
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000908
  data_note: Uses CHIP three waves (2002, 2013, 2023) matched with O*NET task intensity measures via Chinese Classification of Occupations (CSCO) to decompose the gender wage gap by task content. Tracks how the changing nature of work — from routine to cognitive/interpersonal tasks — shapes gender wage differentials in urban China over two decades.
- cite: 'Wang, Liang & Lehmann (2025), Import Competition and the Rise of Precarious Employment: Evidence from Individual-Level and Firm-Level Data in China'
  doi: https://doi.org/10.1016/j.labeco.2025.102803
  journal: Labour Economics
  year: 2025
  dataset_role: CHIP three waves (1995, 2002, 2007); individual-level employment status linked to regional tariff exposure
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0927537125001277
  data_note: >-
    Uses CHIP household survey data (1995, 2002, 2007 waves) combined with World Bank Enterprise Surveys (2001-2004) for firm-level analysis. Links regional tariff exposure to individual employment status (precarious vs. long-term). Finds workers in regions more exposed to import tariff cuts were significantly more likely to be in precarious jobs — an average tariff cut increased precarious employment probability by ~15pp. Precarious employment rose sharply from ~3% (1995) to ~28% (2007). Firm-level mechanism — smaller, less productive firms hired more temporary workers in response to import competition.
provenance:
- source: https://www.journals.uchicago.edu/doi/abs/10.1086/660887
  field_scope:
  - final JPE article identity and DOI
  - cross-regional and household savings evidence context
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://users.nber.org/~confer/2009/China09/wei.pdf
  field_scope:
  - CHIP 2002 household-level use
  - 122 rural counties and 70 cities coverage stated in the paper
  - savings-rate definition and sample restrictions
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.icpsr.umich.edu/web/DSDR/studies/21741
  field_scope:
  - CHIP 2002 identity and version
  - ten public-use files, units, coverage, and public-access status
  added: '2026-08-11'
  confidence: high
  verified: true
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
- id: china-census
  relation: complement
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
