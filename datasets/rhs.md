---
schema_version: 2
catalog_status: grounding
id: rhs
name: National Bureau of Statistics Rural Household Survey (RHS)
aka:
- RHS
- 农村住户调查
- 中国农村住户调查
- NBS Rural Household Survey
- 国家统计局农村住户调查
provider: National Bureau of Statistics Rural Household Survey System
china_related: true
domains:
- development
- labor
- consumption
- poverty
- agriculture
unit_of_observation: Farmer-year/Family member-year
structure: rotating-or-partial-panel
geo_granularity:
- personal
- farmers
- County
- province
geography: Rural areas in mainland China; the provinces, years and sampling ranges of public document holding versions are
  not uniform
time_span:
  start: 1986
  end: 2015
  coverage_note: Around 2015, the urban and rural household surveys were integrated into the Household Income, Expenditure
    and Living Conditions Survey.
  last_confirmed_release: 2015
  last_checked: '2026-07-10'
frequency:
- annual
sample_size: Historical surveys are usually tens of thousands of households per year; the versions available to researchers
  vary greatly, and we do not regard a single number as a fixed size of the entire database for the time being.
key_variables:
- household income
- consumer spending
- Employment and Wages
- family size
- housing
- durable goods
- Some agricultural production and land variables
research_fit:
  best_for:
  - Long-term annual analysis of rural household income, consumption, poverty and labor supply
  choose_over:
  - When studying the income and expenditure of NBS households or comparing urban and rural areas with UHS, it takes priority
    over RFD.
  not_good_for:
  - Micro data that needs to be made public and immediately downloadable
  - Agricultural productivity studies requiring strong panel, crop input-output and land lease details; see RFD at this time
  - Independent RHS brand data after 2016
  needs_join_for:
  - Policy research usually requires joining provincial/county policies and macro data
  variation_available:
  - annual regional changes
  - Changes in household income and consumption
good_for:
- Rural income and consumption
- poverty and income mobility
- Comparison of income and expenditure of urban and rural households
- rural labor supply
identification:
- Household or region fixed effects
- DID (regional policy)
- IV(price/weather/policy)
linkable_keys:
- Family ID (internal)
- County code (restricted)
- Provincial code
- Year
joins:
- target: uhs
  relation: predecessor-parallel
  keys:
  - Year
  - Provincial code
  method: harmonized-aggregate
  evidence_status: plausible
- target: rfd
  relation: often-confused-with
  keys: []
  method: not-directly-joinable
  evidence_status: verified-distinct
access_routes:
- route: nbs-institutional
  access_status: no-public-download
  direct_url: https://microdata.stats.gov.cn/
  requirements: The supporting institution submits a research application; whether it contains the historical micro version
    of RHS needs to be confirmed with the platform.
  steps:
  - Registered with the Micro Data Laboratory of the National Bureau of Statistics.
  - Confirm the household survey year and level in the requisitionable data directory.
  - Submit projects, variables, and safe use requests.
  deliverable: Desensitized or controlled use data within approved scope; there is no guarantee that the complete 1986–2015
    database exists.
  cost: by-application
  last_checked: '2026-07-10'
- route: public-substitute
  access_status: available
  direct_url: https://www.isss.pku.edu.cn/cfps/
  requirements: Apply according to the CFPS process.
  steps:
  - Alternative analysis of income, consumption and household behavior using the CFPS rural subsample.
  deliverable: The household tracking data that can be applied for will be made public after 2010.
  cost: free
  last_checked: '2026-07-10'
access:
  url: https://microdata.stats.gov.cn/
  cost: by-application
  license: Controlled academic research use, no redistribution
  format:
  - dta
  - csv
  - xlsx
  api: false
  how_to_get: First confirm whether there is a household survey for the target year in the Micro Data Laboratory of the National
    Bureau of Statistics; if there is no authority, use public alternatives such as CFPS/CHIP.
caveats: The current knowledge base has not yet obtained itemized evidence from the RHS official codebook or public application
  catalog, so it remains in the grounding state. Do not put samples and paper citations from the Ministry of Agriculture and
  Rural Affairs' RFD in this entry.
quality:
  profile_status: partial
  access_status: needs-verification
  paper_use_status: none
  last_audited: '2026-07-10'
used_by: []
provenance:
- source: https://microdata.stats.gov.cn/
  field_scope:
  - possible_access
  added: '2026-07-10'
  confidence: med
  verified: false
- source: The original RHS entry of the project retains the NBS survey information after the identity split.
  field_scope:
  - identity_history
  added: '2026-07-10'
  confidence: med
  verified: false
related_datasets:
- id: rfd
  relation: often-confused-with
- id: uhs
  relation: parallel-survey
- id: cfps
  relation: substitute
---

## Positioning in one sentence

This entry only represents the rural household survey of the National Bureau of Statistics and no longer includes fixed rural observation points of the Ministry of Agriculture and Rural Affairs. It is suitable for research on rural household income and consumption, but it is difficult to obtain the historical micro version, and further grounding is still needed.

## critical exclusions

Adamopoulos et al. (2022), Chari et al. (2021) and Gai et al. (2025) used the National Fixed Point Survey of the Ministry of Agriculture and Rural Affairs, which has been moved to `rfd`; Bu & Liao (2022) used CHFS and does not belong to this entry.
