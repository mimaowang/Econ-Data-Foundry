---
schema_version: 3
catalog_status: grounding
id: nbs-monthly-labor-force-survey
name: NBS Monthly Labor Force Survey (全国月度劳动力调查) and urban surveyed unemployment rate (城镇调查失业率)
aka:
- 全国月度劳动力调查
- 劳动力调查
- urban surveyed unemployment rate
- China Labor Force Survey (CLFS)
provider: >-
  国家统计局 (National Bureau of Statistics of China, NBS). The monthly labor
  force survey is a State-Council-approved statistical survey system
  implemented by NBS (调查失业率的基础数据来源 page, stats.gov.cn, read
  2026-08-15).
china_related: true
domains:
- labor
- macro
- public
- urban
- unemployment

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Household-level microdata of the monthly labor force survey, which is not
    publicly downloadable. The separately catalogued national monthly urban
    surveyed unemployment rate is a public aggregate output, not this target.
    The official microdata portal microdata.stats.gov.cn
    (微观数据实验室, fetched 200, 2026-08-15) is a JavaScript application;
    its catalog and application terms were not readable without a browser.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The monthly labor force survey is the official source of China's urban
    surveyed unemployment rate: ~340,000 sampled households per month across
    urban and rural areas of 31 provinces, established nationally in 2016,
    with household microdata not released for download; the microdata-lab
    application route is unverified. The public aggregate output is separately
    catalogued and cannot establish microdata access.
  barrier: >-
    Microdata application terms on microdata.stats.gov.cn are JS-gated and
    unread (browser check needed); the monthly release is an aggregate series,
    not a household file.

unit_of_observation: >-
  Public layer: national (and province-level, where released) monthly
  unemployment-rate series. Survey layer: sampled households and their current
  residents/permanent residents (design facts from the official NBS page).
structure: repeated-cross-section (monthly rotating household sample)
geo_granularity:
- national (monthly 城镇调查失业率, published since 2018)
- 31 province-level divisions are surveyed; province-level monthly series
  release pattern NOT verified this round
geography: >-
  China, all 31 provinces (autonomous regions/municipalities); sample covers
  urban and rural areas; ~2,800+ counties/districts and ~21,000
  communities/villages in the monthly sample (official NBS page, read
  2026-08-15)
time_span:
  start: '2016'
  end: null
  last_confirmed_release: null
  coverage_note: >-
    Official NBS page: the nationwide labor force survey system was formally
    established in 2016; the national urban surveyed unemployment rate has
    been published monthly since 2018. Ongoing monthly series.
  last_checked: '2026-08-15'
frequency:
- monthly
sample_size: >-
  ~340,000 households/month nationally (about 250,000 urban + 90,000 rural),
  covering 2,800+ counties/districts and ~21,000 communities/villages
  (official NBS page, read 2026-08-15)
key_variables:
- Employment status, unemployment status and unemployment duration
- 'Hours worked and job-search behavior (ILO classification: employed = worked in reference period; unemployed = no job + actively searched + able to start; labor force = employed + unemployed)'
- 'Household sampling rotation (2-10-2 pattern: 2 months in, 10 months out, 2 months in again the following year)'
- Survey-weighted aggregates by urban/rural, region, age, gender and
  population structure

research_fit:
  best_for:
  - China's official monthly urban surveyed unemployment rate as a macro
    indicator (national series, monthly, published since 2018)
  - Employment/unemployment conditions measured on the internationally
    comparable ILO definition
  choose_over:
  - Choose the survey-based 调查失业率 over the discontinued 登记失业率
    (registered-unemployment) series when an ILO-comparable, survey-based
    measure is required.
  - For household-level employment panels with rich covariates use cfps/chip/
    clds/uhs; the labor force survey's public layer is an aggregate series.
  not_good_for:
  - Household-level or individual-level microdata analysis (no public
    microdata release verified; the survey microdata are restricted)
  - Province-level monthly series unless the release pattern is verified
  - Causal identification (aggregate series only; no assignment variation)
  needs_join_for:
  - Macro context (GDP, prices) from china-stat-yearbook or WDI
  - Subnational labor-market covariates (province-year series) from
    china-stat-yearbook family
  variation_available:
  - Monthly time-series variation in the national unemployment rate since 2018
  topics:
  - unemployment
  - labor force survey
  - macro statistics
  - employment
  - urban labor market

good_for:
- national monthly unemployment monitoring
- macro labor-market indicators
identification: []
linkable_keys:
- Month/year
- Province (if province-level series used; release pattern unverified)

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - year/month
  method: combine the monthly unemployment series with annual yearbook macro variables at national or province-year level
  evidence_status: plausible

access_routes:
- route: NBS official explanation pages (institutional documentation)
  access_status: available
  direct_url: https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html
  requirements: none
  steps:
  - Open the two official pages (什么是调查失业率; 调查失业率的基础数据来源) to confirm the survey design and definitions.
  deliverable: methodology documentation only
  cost: free
  last_checked: '2026-08-15'
  caveat: pages are explanatory, not data
- route: "Boundary reference: separately ready national monthly unemployment series"
  access_status: documentation-only
  direct_url: https://www.stats.gov.cn/sj/zxfb/
  requirements: none
  steps:
  - Use nbs-national-monthly-urban-surveyed-unemployment-rate for the public aggregate product; do not treat it as a microdata route.
  deliverable: Documentation-only cross-reference to the separate public aggregate record.
  cost: free
  last_checked: '2026-08-15'
  caveat: The public rate does not establish the survey microdata catalog, application terms or household-level delivery.
- route: NBS microdata lab (microdata.stats.gov.cn) for survey microdata
  access_status: needs-verification
  direct_url: https://microdata.stats.gov.cn/
  requirements: 'unknown - the portal (title 微观数据实验室) is a JavaScript app; registration/application terms not readable from an automated client'
  steps:
  - Open in a human browser; check the catalog and application terms for the monthly labor force survey microdata.
  deliverable: unverified
  cost: by-application
  last_checked: '2026-08-15'
  caveat: no evidence that labor-force microdata are currently available through this portal

access:
  url: https://www.stats.gov.cn/sj/zxfb/
  cost: free
  license: Government statistical releases; reuse under official data-publication rules
  format:
  - HTML tables in release pages
  - (unverified) microdata formats via the microdata lab
  api: false
  how_to_get: The public national rate is separately documented in nbs-national-monthly-urban-surveyed-unemployment-rate. For microdata, use microdata.stats.gov.cn only if a human-browser check confirms the survey and its application terms.
caveats:
- The survey design facts (340k households/month, 2-10-2 rotation, 2,800+ counties, 21,000 communities, ILO classification, weighting) come from the official NBS explanation pages read 2026-08-15; they document the survey, not the availability of any microdata file.
- Province-level monthly 调查失业率 release pattern NOT verified this round.
- The 登记失业率 (registered unemployment rate) is a different, discontinued indicator; do not merge the series.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html (什么是调查失业率, fetched+read 2026-08-15)
  field_scope:
  - survey system established 2016
  - monthly national urban surveyed unemployment rate published since 2018
  - ILO-comparable definition
  - stratified two-stage housing-unit-proportional sampling, ~340k households/month
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/zs/tjws/zytjzbqs/tcsyl/202501/t20250121_1958390.html (调查失业率的基础数据来源, fetched+read 2026-08-15)
  field_scope:
  - State-Council-approved survey system
  - 340k households/month (250k urban + 90k rural)
  - 2,800+ counties, 21,000 communities
  - 2-10-2 rotation
  - weighting by 城乡/地区/年龄/性别/人口结构
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://microdata.stats.gov.cn/ (probe, 200, JS app title 微观数据实验室, 2026-08-15)
  field_scope:
  - microdata portal exists
  - application terms NOT readable (JS-gated)
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: nbs-national-monthly-urban-surveyed-unemployment-rate
  relation: successor
- id: clds
  relation: often-confused-with
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

The NBS monthly labor force survey is the official source of China's 城镇调查失业率 (urban surveyed unemployment rate): a monthly rotating sample of ~340,000 households documented on official NBS pages, with a monthly national aggregate published since 2018 and household microdata restricted behind an unverified application portal.

## Select rules

- Use it for the official national monthly unemployment series (2018-present), the only ILO-comparable unemployment indicator China publishes monthly.
- Switch to cfps/chip/clds/uhs household panels when the research needs household-level employment microdata.
- Do not use it for province-level monthly series until the release pattern is verified, and never merge it with the discontinued registered-unemployment (登记失业率) series.

## Get recipe

1. Confirm the design and definitions on the two official NBS explanation pages.
2. Collect the monthly national 城镇调查失业率 from NBS monthly releases (stats.gov.cn/sj/zxfb/), transcribing values into a researcher-built series.
3. Only if household microdata are needed: open microdata.stats.gov.cn in a human browser and check whether the labor force survey is offered and under what terms (unverified this round).

## Connections and Limitations

The public layer is an aggregate series; the survey microdata are restricted. The survey covers all 31 provinces in its sampling frame, but the release pattern for province-level monthly rates was not verified. All design facts above trace to the two official NBS pages read on 2026-08-15; nothing in this record proves that microdata can be obtained.

## Decision sufficiency check

A researcher can now choose the official monthly national unemployment series, knows the design behind it, and knows that microdata access is an unverified portal question rather than a public download. The record is grounding, not ready, because the microdata route and the province-level release pattern are unresolved.
