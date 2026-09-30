---
schema_version: 3
catalog_status: grounding
id: china-dsp-mortality-records
name: China Disease Surveillance Points (DSP) / National Mortality Surveillance System mortality records
aka:
- 全国疾病监测系统
- 死因监测
- 疾病监测点
- DSP
- NMSS
- 全国死因监测系统
- 中国死因监测数据集
- Disease Surveillance Points
- National Mortality Surveillance System
provider: >-
  Chinese Center for Disease Control and Prevention (中国疾病预防控制中心,
  China CDC), in particular the National Center for Chronic and
  Non-communicable Disease Control and Prevention (中国疾控中心慢病中心,
  NCD Center). Surveillance points (county/district) are run with local
  CDCs. Since 2013 the integrated National Mortality Surveillance System
  (全国死因监测系统, NMSS) combines the former Disease Surveillance Points (DSP)
  and the vital-registration (death reporting) system.
china_related: true
domains:
- health
- mortality
- demography
- public

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    Individual-level death records (age, sex, cause of death, location,
    timing) from the DSP/NMSS surveillance points - the recurring asset in
    Chinese mortality studies (the four Layer-2b papers plus the AER
    fog-to-smog paper's DSP city-week-age-cause mortality component). Public
    alternatives are TABULATIONS: GHDx redistributions of China CDC DSP
    tabulations (age/sex/cause, urban-rural; verified records for 2009, 2013,
    2021), the 公共卫生科学数据中心 vital-registration databases
    (application-based), and the annual 中国死因监测数据集 (China Death
    Surveillance Data Set) book series.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    Provider-first grounding (2026-08-15): institutional identity and system
    coverage confirmed from first-hand sources - the WHO Bulletin 2016 system
    description (Liu et al., PMC4709796, read via Europe PMC XML) documents
    the 2013 merger of the DSP (161 points, ~6% of population) and the
    vital-registration system into the NMSS with 605 surveillance points
    (county/district level, ~24% of population, covering all 31 provinces
    via multistage stratified sampling); the China CDC NCD Center article
    (ncncd.chinacdc.cn, 2025-05-06) confirms the death-surveillance system
    and its role; the 公共卫生科学数据中心 resource directory (phsciencedata.cn,
    read 2026-08-15) lists vital-registration databases including 全国疾病监测
    系统死因监测网络报告数据库 and 1991-2000 DSP data with an apply-for-data flow
    behind registration; GHDx record "China Disease Surveillance Points 2021
    - China CDC" (ghdx.healthdata.org, read 2026-08-15) confirms tabulations
    by age/sex/cause, urban-rural, provider CCDC. Individual-level microdata
    are restricted: application-based CDC cooperation, no public route
    evidenced. Which exact extract (DSP vs NMSS vs mixed) the four anchor
    papers use is unverified (data sections unread, Elsevier 403).
  barrier: >-
    Individual-level mortality microdata are restricted (China CDC
    institutional agreement; no public download). Only tabulations are
    publicly obtainable (GHDx, phsciencedata application, annual book
    series). Paper-specific extract identity (DSP vs NMSS, years, geography)
    unverified.

unit_of_observation: >-
  Restricted version: individual death records within surveillance points
  (county/district). Public tabulations: point/county-district aggregates by
  age, sex, and cause of death, split urban/rural.
structure: repeated-cross-section (annual system) with individual-level panel in restricted version
geo_granularity:
- surveillance point (county/district)
- city (aggregated, e.g., 131 DSP cities in the fog-to-smog paper)
- province
- national
geography: >-
  National, 31 provinces: 605 surveillance points (post-2013 NMSS, ~24% of
  population, county/district level); before 2013 the DSP had 161 points
  (~6% of population).
time_span:
  start: '1990'
  end: ongoing
  last_confirmed_release: 'GHDx "China Disease Surveillance Points 2021 - China CDC" (annual tabulation)'
  coverage_note: >-
    DSP system generations since 1990 (fourth generation 2004: 161 points);
    2013 merger created the 605-point NMSS; GHDx hosts annual tabulations
    (verified records: 2009, 2013, 2021); phsciencedata lists 1991-2000 DSP
    data and the 全国疾病监测系统死因监测网络报告数据库. Exact annual coverage of
    each route unverified.
  last_checked: '2026-08-15'
frequency:
- annual
- continuous (reporting through the network)
sample_size: >-
  605 surveillance points covering ~24% of the Chinese population (post-2013
  NMSS); before 2013: 161 points ~6%. The fog-to-smog paper (2011-2016)
  used DSP city-week-age-cause mortality in 131 cities (~73M persons).
key_variables:
- Death records: age, sex, cause of death (ICD-10), location (surveillance point), date
- Tabulations: deaths by age group x sex x cause, urban/rural split
- Derived: mortality rates (with population denominators), cause-specific mortality

research_fit:
  best_for:
  - Mortality outcomes in China at point/city level for pollution-health, climate-health, and policy studies (anchor papers: winter-heating PM2.5 mortality, ozone mortality, natural-gas rollout, low-carbon-pilot mortality)
  - Cause-of-death composition and mortality-rate panels by age/sex
  choose_over:
  - Choose this over china-census for cause-specific mortality; census provides population denominators, not death records.
  - The annual 中国死因监测数据集 and GHDx tabulations are the obtainable public layer; individual microdata require CDC cooperation.
  not_good_for:
  - Full national vital registration (the NMSS covers 24% of population; not a complete death registry for every county)
  - Morbidity/disease incidence beyond the surveillance scope
  - Reconstructing the exact paper extracts: the four anchor papers' sample definitions are unread
  needs_join_for:
  - Population denominators: china-census
  - Pollution exposure: china-air-quality-monitoring, china-satellite-pm25 (pollution-mortality studies)
  - Other microdata: china-aer-fog-to-smog-behavioral-2024 (uses DSP mortality as one of seven components)
  variation_available:
  - Spatial variation across 605 surveillance points (county/district)
  - Temporal variation in cause-specific mortality
  - Policy/regime changes (2013 system merger; heating policy boundaries in the Huai River design)
  topics:
  - mortality
  - cause of death
  - death surveillance
  - pollution and health
  - climate and health

good_for:
- mortality outcomes
- cause-of-death structure
- pollution-mortality studies
- health policy evaluation
identification:
- quasi-experimental designs (Huai River heating boundary, policy rollout)
- staggered DiD (low-carbon pilots)
- event studies
linkable_keys:
- Surveillance point code (county/district)
- City code
- Date/year
- Age, sex, cause of death

joins:
- target: china-census
  relation: complement
  keys:
  - county/district code
  - year
  method: population denominators for rates
  evidence_status: plausible
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - city
  - date
  method: 'pollution exposure to mortality (literature pattern: Ebenstein et al. 2015)'
  evidence_status: literature-used
- target: china-aer-fog-to-smog-behavioral-2024
  relation: complement
  keys:
  - city
  - week
  method: DSP mortality component of a multi-source panel
  evidence_status: verified

access_routes:
- route: ghdx-tabulations
  access_status: available-with-registration
  direct_url: https://ghdx.healthdata.org/record/china-disease-surveillance-points-2021-china-cdc
  requirements: GHDx account (free registration)
  steps:
  - Open the GHDx record "China Disease Surveillance Points 2021 - China CDC" (original title: 2021 全国疾病监测系统; provider CCDC; tabulations only; urban-rural; age/sex/cause).
  - Register and download the tabulations; other DSP years exist on GHDx (e.g., 2009 record 270007; 2013 record 223780).
  deliverable: Annual DSP tabulations by age, sex, cause of death, urban/rural; free after registration.
  cost: registration
  last_checked: '2026-08-15'
  caveat: Tabulations only - no individual records; redistribution layer is IHME's GHDx, not China CDC's own portal.
- route: phsciencedata-application
  access_status: needs-verification
  direct_url: https://www.phsciencedata.cn/Share/ky_sjml.jsp?id=6b5fc8c0-cffb-4a57-af26-a72070c65954
  requirements: Registered account on the China CDC public scientific data platform (公共卫生科学数据中心); application/approval flow
  steps:
  - Register at phsciencedata.cn (user guide read 2026-08-15; registration + login required).
  - Open the 生命登记 (vital registration) resource directory: 全国疾病监测系统死因监测网络报告数据库, 1991-2000年全国疾病监测系统死因监测数据, 1973-1975第一次死因调查, 2004-2005第三次死因回顾抽样调查.
  - Apply for the target database (apply-for-data flow behind login); terms and approval conditions unverified.
  deliverable: Application-based access to CDC vital-registration databases; approval conditions unverified.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: The resource pages are JS-rendered; actual data deliverable and approval conditions not verified end-to-end.
- route: annual-dataset-book
  access_status: available
  direct_url: https://www.chinacdc.cn/
  requirements: Purchase/library access to the annual book
  steps:
  - Obtain the annual 中国死因监测数据集 (China Death Surveillance Data Set; earlier volumes titled 全国疾病监测系统死因监测数据集, e.g., 2013 volume) published by the NCD Center (official procurement records confirm the series: 2013 volume ccgp.gov.cn 2014; 2019 volume cn-bid.org.cn 2020).
  - Use the published aggregate tables (county-level and above).
  deliverable: Published aggregate death-surveillance tables; paid book/library access.
  cost: paid
  last_checked: '2026-08-15'
  caveat: Book series verified via procurement notices and library listings only; current volumes and exact table content not inspected.
- route: ncd-center-cooperation
  access_status: needs-verification
  direct_url: https://ncncd.chinacdc.cn/
  requirements: Institutional research agreement with the China CDC NCD Center (慢病中心); human negotiation
  steps:
  - Contact the NCD Center for individual-level death-surveillance microdata access.
  - Expect a restricted-data agreement; terms unverified.
  deliverable: Individual-level mortality microdata under agreement (restricted).
  cost: by-application
  last_checked: '2026-08-15'
  caveat: No public route evidenced; do not promise obtainability.

access:
  url: https://ncncd.chinacdc.cn/
  cost: by-application
  license: Restricted health data; individual-level access by institutional agreement only
  format:
  - xlsx
  - dta
  - csv
  api: false
  how_to_get: >-
    Individual-level DSP/NMSS microdata: China CDC NCD Center institutional
    cooperation (restricted). Public alternatives: GHDx tabulations (free
    after registration), 公共卫生科学数据中心 application, and the annual
    中国死因监测数据集 book.
caveats: >-
  The 605-point figure is the post-2013 NMSS; papers using "DSP" data before
  2013 refer to the 161-point system. The four Layer-2b anchor papers' exact
  extracts (DSP vs NMSS; individual vs county-cause counts; years) are
  unread. Aggregate tabulations do not reproduce individual-level analysis.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: partial
  last_audited: '2026-08-15'

used_by:
- cite: 'Ebenstein, Fan, Greenstone, He & Zhou (2015), Growth, Pollution, and Life Expectancy: China from 1991-2012'
  doi: https://doi.org/10.1257/aer.p20151094
  journal: AER P&P
  year: 2015
  dataset_role: DSP mortality data combined with city-level air pollution for life-expectancy analysis (Huai River design)
  evidence_type: paper_data_section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257/aer.p20151094
  data_note: DSP mortality use is documented in the existing china-air-quality-monitoring record; earliest cataloged use of the DSP asset.
- cite: 'Cao, Han, Li, Yin & Yin (2026), low-carbon pilot mortality study'
  doi: https://doi.org/10.1016/j.jce.2026.02.001
  journal: JCE
  year: 2026
  dataset_role: Older-adult deaths by cause around low-carbon pilot cities (staggered DiD)
  evidence_type: abstract-only
  evidence_url: https://doi.org/10.1016/j.jce.2026.02.001
  data_note: Abstract read via OpenAlex (Layer-2b); common CDC coauthors (Maigeng Zhou / Peng Yin family); exact mortality extract unread.
- cite: 'Salvo, Tang, Yang, Yin & Zhou (2024), winter-heating PM2.5 mortality 2013-2018'
  doi: https://doi.org/10.1016/j.jeem.2024.102945
  journal: JEEM
  year: 2024
  dataset_role: Mortality outcomes for winter-heating pollution study
  evidence_type: title-level
  evidence_url: https://doi.org/10.1016/j.jeem.2024.102945
  data_note: Abstract channels empty (Layer-2b); mortality source unread.
- cite: 'Qiu, Liu, Shi & Zhou (2024), ozone mortality study'
  doi: https://doi.org/10.1016/j.jeem.2024.102980
  journal: JEEM
  year: 2024
  dataset_role: Mortality outcomes for ozone study
  evidence_type: title-level
  evidence_url: https://doi.org/10.1016/j.jeem.2024.102980
  data_note: Abstract channels empty; mortality source unread.
- cite: 'Lai, Lin, Shen & Zhou (2025), natural-gas rollout mortality study'
  doi: https://doi.org/10.1016/j.jeem.2025.103131
  journal: JEEM
  year: 2025
  dataset_role: Mortality outcomes for natural-gas rollout study
  evidence_type: title-level
  evidence_url: https://doi.org/10.1016/j.jeem.2025.103131
  data_note: Abstract channels empty; mortality source unread.
- cite: 'Barwick, Li, Lin & Zou (2024), From Fog to Smog: The Value of Pollution Information'
  doi: https://doi.org/10.1257/aer.20200956
  journal: AER
  year: 2024
  dataset_role: CDC DSP city-week-age-cause mortality component (131 cities, 2011-2016)
  evidence_type: paper_data_section
  evidence_url: https://www.nber.org/papers/w30276
  data_note: DSP as one of seven panel components; documented in the canonical china-aer-fog-to-smog-behavioral-2024 record (openICPSR 10.3886/E193441V1).

provenance:
- source: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4709796/fullTextXML
  field_scope:
  - system_identity
  - coverage
  - sampling
  - history
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://ncncd.chinacdc.cn/zxdt/202505/t20250506_311191.htm
  field_scope:
  - producer
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.phsciencedata.cn/Share/ky_sjml.jsp?id=6b5fc8c0-cffb-4a57-af26-a72070c65954
  field_scope:
  - access_route
  - databases
  added: '2026-08-15'
  confidence: med
  verified: true
- source: https://ghdx.healthdata.org/record/china-disease-surveillance-points-2021-china-cdc
  field_scope:
  - access_route
  - tabulation_content
  added: '2026-08-15'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-dsp-mortality-records, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-aer-fog-to-smog-behavioral-2024
  relation: complement
- id: china-census
  relation: complement
- id: china-air-quality-monitoring
  relation: complement
---

## Positioning in one sentence

The China CDC DSP/NMSS system is the country's surveillance-point mortality infrastructure (605 points covering ~24% of the population since 2013) - its individual-level death records are restricted, but tabulations (age/sex/cause, urban-rural) are obtainable via GHDx, the CDC public-data platform, and the annual 数据集 book.

## Select rules

- Use for mortality outcomes at point/city level in pollution-health and policy studies; pair with china-census denominators and pollution exposure series.
- Do not equate the 605-point NMSS (24% population) with full vital registration; coverage claims must match the paper's era (pre-2013 = 161-point DSP).
- For individual-level analysis, expect the restricted CDC cooperation route; public routes deliver tabulations only.

## Get recipe

1. For tabulations: register at GHDx and download the annual "China Disease Surveillance Points" records (2009/2013/2021 verified), or apply at phsciencedata.cn for the vital-registration databases, or obtain the annual 中国死因监测数据集 book.
2. For individual-level microdata: pursue a China CDC NCD Center institutional agreement; no public route evidenced.
3. Always verify the paper's extract identity (DSP vs NMSS, years, geography) from the paper's data section before matching.

## Connections and Limitations

- The four Layer-2b anchor papers' exact extracts are unread; the family identity is the DSP/NMSS system, not one confirmed extract.
- Population coverage changed from ~6% (pre-2013 DSP) to ~24% (605 points); panel studies crossing 2013 must handle the system change.
- Tabulations cannot reproduce individual-level analyses; the fog-to-smog record shows the aggregate use pattern (city-week-age-cause counts).
