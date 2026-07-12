---
schema_version: 2
catalog_status: grounding
id: rfd
name: National Rural Fixed Point Survey (NFP/NFPS)
aka:
- 全国农村固定观察点
- 农村固定观察点
- National Fixed Point Survey
- NFP
- NFPS
- National Rural Fixed Observation Point Survey
provider: Research Center for Rural Economy, Ministry of Agriculture and Rural Affairs (RCRE, formerly Research Center for
  Rural Economy, Ministry of Agriculture)
china_related: true
domains:
- agriculture
- development
- labor
- land
- public
- migration
unit_of_observation: Farmer-year/Family member-year/Farmer-crop-year/Village-year
structure: longitudinal-panel
geo_granularity:
- personal
- farmers
- village
- province
geography: Fixed observation villages in various provinces in mainland China; the provinces, villages and sample periods of
  the version used in the paper are not exactly the same
time_span:
  start: 1986
  end: unknown
  known_gaps:
  - 1992
  - 1994
  last_confirmed_release: unknown
  last_checked: '2026-07-10'
frequency:
- annual
sample_size: The full survey covers more than 300 villages and more than 20,000 households; the specific research versions
  vary greatly. For example, Chari et al. used 2003–2010, 399 villages, and more than 19,000 households, and Adamopoulos et
  al. used 1993–2002, 110 villages in 10 provinces, and about 8,000 households each year.
key_variables:
- Family members and labor force allocation
- Farm and non-farm work days
- Migration and employment
- household income and expenses
- Land holding and leasing out
- Crop sown area and physical output
- Agricultural inputs such as fertilizers and machinery
- agricultural production costs
- Village economy and public services
research_fit:
  best_for:
  - A long-term panel study on rural land allocation, land rental and farmer household productivity
  - Intra-household allocation of rural labor migration to non-agricultural sectors and cities
  - Farmer-level causal assessment of agricultural policies, land rights and pension policies
  choose_over:
  - Priority is given to CFPS/CHFS when crop input-output, land lease and long-term farmer panel are required.
  - Research on household balance sheets or publicly downloadable data should not take precedence over CHFS/CFPS
  not_good_for:
  - Projects that have no institutional cooperation channels and require immediate public downloading
  - Research on urban households or listed companies
  - Studies that require a unified national sample and do not allow differences between different paper versions
  - Studies requiring confirmed subdivision boundaries, parcel coordinates, or parcel-by-parcel property rights information
  needs_join_for:
  - When researching specific policies, it is usually necessary to join county/provincial policy time points, prices, weather
    or traffic data
  variation_available:
  - Farmer, village and year panel changes
  - Regional phased implementation of land system and pension policies
  topics:
  - land transfer
  - rural land reform
  - Crop productivity
  - Farmer productivity
  - Agricultural input and output
  - rural pension
good_for:
- Rural Land System and Agricultural Productivity—Using Regional Time Differences in Land Rights Reform to Do DID
- Land and capital misallocation - using farmer-crop input and output to estimate TFP and marginal product dispersion
- Rural pensions, migration costs and cross-sector allocation of labor
identification:
- Farmer fixed effects
- Village fixed effects
- DID (policy implemented in phases)
- IV (Policy Eligibility or Geographic Impact)
- structural model
linkable_keys:
- Farmer ID (internal)
- Village code (restricted)
- Provincial code
- Year
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Provincial code
  - Year
  method: exact
  evidence_status: plausible
- target: china-census
  relation: benchmark
  keys:
  - Provincial code
  - Year
  method: aggregate-level
  evidence_status: plausible
access_routes:
- route: institutional-cooperation
  access_status: no-public-download
  direct_url: https://www.rcre.agri.cn/
  requirements: Rely on universities/research institutions to contact the Rural Economic Research Center of the Ministry of
    Agriculture and Rural Affairs; usually requires formal projects, cooperative relationships, and confidentiality commitments.
  steps:
  - First confirm the year, questionnaire level and variables required for the study.
  - Explain the institution, project and data needs through the contact/message channel on the official website of the Rural
    Economic Research Center.
  - Submit research plans, data usage instructions and confidential materials as required by the other party.
  deliverable: The approved version may be a desensitized farmer/village panel in a specified year and region, and is not
    a unified public disclosure of the entire database.
  cost: by-application
  last_checked: '2026-07-10'
  caveat: As of the verification date, no standard download or online application page for the public has been found; we cannot
    guarantee that the application will be successful or give a fixed period.
- route: public-alternative
  access_status: available
  direct_url: https://www.isss.pku.edu.cn/cfps/
  requirements: Proxy using CFPS rural subsample.
  steps:
  - Obtain public data by application route for CFPS entries.
  deliverable: Common variables such as income, consumption, employment, and family structure; agricultural crop input and
    output are significantly weaker.
  cost: free
  last_checked: '2026-07-10'
access:
  url: https://www.rcre.agri.cn/
  cost: by-application
  license: For approved research use only, no redistribution
  format:
  - unknown
  api: false
  how_to_get: There is no public download entrance. The supporting institution should contact the Rural Economic Research
    Center of the Ministry of Agriculture and Rural Affairs, explain the year, variables and research purpose, and submit
    cooperation and confidentiality materials as required; if it is not available, use the CFPS/CHNS rural subsample instead.
caveats: Different papers hold different years, provinces, and questionnaire levels. The sample size of a certain paper cannot
  be regarded as a fixed attribute of the entire database. What has been verified is the input and output at the farmer-crop
  level, which does not mean that all versions have been confirmed to contain plot boundaries or plot coordinates. Data non-disclosure
  is the biggest obstacle.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Adamopoulos, Brandt, Leight & Restuccia (2022), Misallocation, Selection, and Productivity: A Quantitative Analysis
    with Panel Data from China'
  doi: https://doi.org/10.3982/ECTA16598
  journal: Econometrica
  year: 2022
  dataset_role: Key farmer-crop panel; used to estimate household productivity, land and capital misallocation
  evidence_type: paper_data_section
  evidence_url: https://onlinelibrary.wiley.com/doi/10.3982/ECTA16598
  data_note: RCRE/Ministry of Agriculture survey, 1993–2002, 110 villages in 10 provinces, approximately 8,000 households
    per year.
- cite: Chari, Liu, Wang & Wang (2021), Property Rights, Land Misallocation, and Agricultural Efficiency in China
  doi: https://doi.org/10.1093/restud/rdaa072
  journal: ReStud
  year: 2021
  dataset_role: Main farmers-crop panel; joined with the implementation time of rural land contract laws in each province
  evidence_type: working_paper_data_section
  evidence_url: https://www.nber.org/system/files/working_papers/w24099/w24099.pdf
  data_note: National Fixed Point Survey, 2003–2010, 399 villages, more than 19,000 households.
- cite: Gai, Guo, Li, Shi & Zhu (2025), Rural Pensions, Labor Reallocation, and Aggregate Income
  doi: https://doi.org/10.3982/ECTA19699
  journal: Econometrica
  year: 2025
  dataset_role: Main individual/farmer panel; joined with the county-level implementation of the new rural insurance
  evidence_type: paper_data_section
  evidence_url: https://onlinelibrary.wiley.com/doi/10.3982/ECTA19699
  data_note: Using the 2003–2013 NFP, the agricultural and migrant labor force is tracked.
provenance:
- source: https://onlinelibrary.wiley.com/doi/10.3982/ECTA16598
  field_scope:
  - identity
  - sample
  - variables
  - paper_use
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://www.nber.org/system/files/working_papers/w24099/w24099.pdf
  field_scope:
  - identity
  - sample
  - variables
  - paper_use
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://www.rcre.agri.cn/
  field_scope:
  - provider
  - access
  added: '2026-07-10'
  confidence: med
  verified: true
related_datasets:
- id: rhs
  relation: often-confused-with
- id: cfps
  relation: substitute
- id: chns
  relation: substitute
---

## Positioning in one sentence

The national rural fixed observation point is the annual panel of rural households and villages organized continuously by the Rural Economic Research Center of the Ministry of Agriculture and Rural Affairs. It is significantly stronger than the general household survey in terms of land, crop input and output, and labor allocation. It is a high-value data for agricultural productivity and rural land research, but there is no public download entrance, and access depends on institutional cooperation.

## Select reminder

- Choose RFD/NFP when you need agricultural production details and long annual farmer panels.
- When only claimable household income, consumption, or employment need to be disclosed, look to CFPS/CHNS first.
- Don’t think of it as the same data as the Office for National Statistics Rural Household Survey (RHS).
- The farmer-crop information available in the paper does not equal the spatial information of plots confirmed by the current record; when plot boundaries or coordinates are involved, a separate questionnaire/approved version must be checked.

## How to get

Confirm the contact channel from the official website of the Rural Economic Research Center, prepare the specific year, variables and research plan and then apply for institutional cooperation. There is currently no public application process that promises success, so answers to users must clarify the thresholds and provide CFPS/CHNS alternatives.
