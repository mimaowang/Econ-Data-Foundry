---
schema_version: 2
catalog_status: grounding
id: china-firm-pollution
name: Environmental Survey of Industrial Firms
aka:
- 中国工业企业环境统计
- 企业污染排放数据
- Environmental Survey Database
- ESD
- 工业企业污染排放调查
- 重点污染源企业调查
provider: Department of Ecology and Environment and National Statistics Department; research often uses academic institutions
  or commercial platforms to compile versions
china_related: true
domains:
- environment
- firm
- development
- IO
- trade
unit_of_observation: Enterprise-Year
structure: unbalanced-panel
geo_granularity:
- enterprise
- County
- city
- province
geography: Mainland China's key polluting industrial enterprises; each research version has different coverage and cleaning
  measurement definitions
time_span:
  start: 1998
  end: 2014
  best_documented_range: 2000–2012
  last_confirmed_release: 2014
  last_checked: '2026-07-10'
frequency:
- annual
sample_size: The commonly used version studies about tens of thousands to 100,000 key polluting enterprises every year; the
  specific samples vary with the year, the measurement definition of pollution sources and the cleaning version.
key_variables:
- Company name
- Business address/coordinates
- Industry code
- Output and employment
- wastewater
- COD
- Ammonia nitrogen
- SO2
- NOx
- smoke dust
- solid waste
- Governance facilities
- Sewage charges
- governance investment
research_fit:
  best_for:
  - The impact of environmental regulations on corporate emissions, productivity, employment, entry and exit
  - Joint research on corporate pollution emissions and ASIF, customs and patents
  choose_over:
  - When studying actual emissions and governance behaviors of enterprises, priority is given to city AQI or satellite PM2.5
  not_good_for:
  - Personal pollution exposure, urban air quality, or health outcomes
  - Service industry companies and public real-time air quality
  needs_join_for:
  - Productivity and financial results often require joining of ASIF/corporate financial libraries
  - Pollution exposure requires additional monitoring stations or satellite concentrations
  variation_available:
  - Corporate annual changes
  - Regional temporal differences in environmental policies
  - Spatial differences between the upstream and downstream monitoring stations
good_for:
- Corporate productivity effects of environmental regulations—spatial RD or DID of corporate emissions and production data
- The impact of environmental taxes, sewage charges, environmental inspections and environmental courts on corporate emission
  reductions
identification:
- Space RD (upstream and downstream of monitoring station)
- DID (environmental policy)
- IV (meteorology or geography)
- firm fixed effects
linkable_keys:
- Company name
- Legal person/organization code
- address
- Industry code
- Administrative division code
- Latitude and longitude
joins:
- target: asif
  relation: complement
  keys:
  - Company name
  - Legal person/organization code
  - address
  method: deterministic-plus-fuzzy
  evidence_status: literature-used
- target: china-customs
  relation: complement
  keys:
  - Company name
  method: fuzzy-name-match
  evidence_status: plausible
- target: china-patents
  relation: complement
  keys:
  - Company name
  method: fuzzy-name-match
  evidence_status: plausible
access_routes:
- route: eps-commercial
  access_status: needs-verification
  direct_url: http://microdata.sozdata.com/
  requirements: EPS subscription for universities/institutions; you need to confirm whether the subscription includes green
    development or corporate pollution modules.
  steps:
  - Enter EPS from the university library.
  - Find green development/corporate pollution related modules.
  - Export after verifying the year and variables.
  deliverable: Enterprise-year data compiled by a third party; may vary by subscription version.
  cost: paid
  last_checked: '2026-07-10'
- route: institutional-original
  access_status: no-public-download
  direct_url: https://www.mee.gov.cn/
  requirements: Formal research projects, authorization from competent authorities or partner institutions, and confidentiality
    requirements.
  steps:
  - Clarify the data year and survey scope.
  - Apply through the competent authority or partner agency holding the data.
  deliverable: Raw or redacted corporate data within approved scope.
  cost: by-application
  last_checked: '2026-07-10'
access:
  url: http://microdata.sozdata.com/
  cost: mixed
  license: Institutional subscription or project authorization
  format:
  - dta
  - csv
  - xlsx
  api: false
  how_to_get: Priority is given to confirming whether university EPS subscriptions include corporate pollution/green development
    modules; the original data does not have a public download entrance for the entire database.
caveats: Enterprise self-reporting, directory changes, industry code changes and thermal power sample breakpoints will all
  affect the long panel. Different paper versions may not be identical data products.
quality:
  profile_status: partial
  access_status: needs-verification
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: He, Wang & Zhang (2020), Watering Down Environmental Regulation in China
  doi: https://doi.org/10.1093/qje/qjaa024
  journal: QJE
  year: 2020
  dataset_role: Enterprise-level geocoding emissions and production results
  evidence_type: paper_abstract
  evidence_url: https://academic.oup.com/qje/article-abstract/135/4/2135/5860784
  data_note: Combined with the location of water quality monitoring stations to create upstream and downstream space RD.
- cite: Qi, Tang & Xi (2021), The Size Distribution of Firms and Industrial Water Pollution
  journal: AEJ:Macro
  year: 2021
  dataset_role: Corporate water pollution discharge; integration with ASIF
  evidence_type: paper_data_description
  evidence_url: needs-verification
  data_note: For quantitative analysis of firm size distribution, clean technology and water pollution.
- cite: Zhou, Huang & Song (2024), The Deterrent Effect of Environmental Judicature on Firms' Pollution Emissions
  journal: CER
  year: 2024
  dataset_role: Enterprise pollution emission results
  evidence_type: abstract_only
  evidence_url: needs-verification
  data_note: In conjunction with the establishment of the Environmental Court.
provenance:
- source: https://academic.oup.com/qje/article-abstract/135/4/2135/5860784
  field_scope:
  - identity
  - paper_use
  - unit_of_observation
  added: '2026-07-10'
  confidence: high
  verified: true
- source: http://microdata.sozdata.com/
  field_scope:
  - access
  added: '2026-07-10'
  confidence: med
  verified: false
related_datasets:
- id: asif
  relation: complement
- id: china-air-quality-monitoring
  relation: often-confused-with
- id: china-satellite-pm25
  relation: often-confused-with
---

## Positioning in one sentence

This is corporate emission and governance behavior data, not urban air quality concentration data. Use it when studying corporate emission reductions, environmental regulations and productivity; when studying personal exposure, migration or urban AQI, monitoring stations or satellite PM2.5 should be used instead.
