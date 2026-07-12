---
schema_version: 2
catalog_status: grounding
id: china-air-quality-monitoring
name: China National Ambient Air Quality Monitoring Data (CNEMC/MEE)
aka:
- 中国空气质量监测数据
- 城市空气质量
- CNEMC
- AQI
- API
- 空气质量监测站
- 全国城市空气质量实时发布
provider: China Environmental Monitoring Center (CNEMC) and Ministry of Ecology and Environment (MEE)
china_related: true
domains:
- environment
- health
- public
- urban
- finance
unit_of_observation: Monitoring station-hour/city-day/city-month
structure: repeated-spatiotemporal
geo_granularity:
- monitoring station
- city
- province
geography: Cities at prefecture level and above across the country; monitoring stations and pollutant coverage expand with
  each year
time_span:
  start: 2000
  end: ongoing
  coverage_note: In the early days, it was API for some cities; around 2013, it began to cover new standard pollutants such
    as PM2.5 and gradually expanded to prefecture-level cities across the country.
  last_confirmed_release: 2026-05 monthly report
  last_checked: '2026-07-10'
frequency:
- hourly
- daily
- monthly
- annual
sample_size: Monitoring station network in cities at prefecture level and above across the country; the number of cities and
  stations changes with the year.
key_variables:
- AQI
- API
- PM2.5
- PM10
- SO2
- NO2
- CO
- O3
- primary pollutants
- air quality level
- Monitoring station coordinates
research_fit:
  best_for:
  - Short-term air pollution exposure at city or monitoring station level
  - Research on air quality information disclosure, monitoring station expansion and regulatory behavior
  - The impact of pollution on market behavior, sentiment, health and short-term flows
  choose_over:
  - When hourly/daily frequency actual concentration monitoring is required, it takes priority over corporate emissions or
    annual satellite PM2.5
  not_good_for:
  - Total corporate emissions and treatment facilities
  - 1km of continuous PM2.5 exposure across the country before 2013
  needs_join_for:
  - Studying individuals, businesses or migration outcomes requires stitching together microdata by location and date
  variation_available:
  - Monitoring station expansion
  - daily pollution shock
  - Pollution differences between cities
  - Meteorologically driven changes
good_for:
- urban air pollution exposure
- AQI event research
- Monitoring information disclosure policy
- Air pollution and financial analyst behavior
identification:
- event study
- DID (Monitoring Station Extension)
- IV(temperature inversion/wind direction)
- panel fixed effects
linkable_keys:
- Monitoring station code
- Latitude and longitude
- city code
- Date
joins:
- target: china-census
  relation: complement
  keys:
  - city code
  - Year
  method: aggregate-level
  evidence_status: plausible
- target: cmds
  relation: complement
  keys:
  - city code
  - date/year
  method: spatiotemporal
  evidence_status: plausible
access_routes:
- route: official-current-and-reports
  access_status: available
  direct_url: https://www.mee.gov.cn/hjzl/dqhj/
  requirements: None
  steps:
  - Enter the atmospheric environment quality page of the Ministry of Ecology and Environment.
  - Select National Air Quality Status or City Air Quality Monthly Report.
  - Download/organize the corresponding monthly reports.
  deliverable: National and city monthly reports and current quality information; not a neat full-history site-level research
    panel.
  cost: free
  last_checked: '2026-07-10'
- route: official-realtime
  access_status: available-with-technical-friction
  direct_url: https://www.cnemc.cn/
  requirements: Real-time web pages; batch historical data may require special accounts, crawling, or third-party organization.
  steps:
  - Enter the real-time air quality page of China Environmental Monitoring Station.
  - Search by city/site.
  - Confirm historical download permissions and measurement definition before using in batch research.
  deliverable: Live or recent site/city air quality.
  cost: free
  last_checked: '2026-07-10'
access:
  url: https://www.mee.gov.cn/hjzl/dqhj/
  cost: mixed
  license: Government disclosure information; batch historical data must comply with platform conditions
  format:
  - html
  - pdf
  - csv
  api: false
  how_to_get: The official monthly report can be obtained directly; the site-level history panel is not a one-click public
    download, and you need to confirm CNEMC permissions or use a compiled version with source description.
caveats: API and AQI standards are not directly equivalent across time periods; monitoring station expansion itself will change
  coverage. The availability of real-time web pages does not mean that historical batch data has been obtained.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: Dong, Fisman, Wang & Xu (2021), Air Pollution, Affect, and Forecasting Bias
  journal: JFE
  year: 2021
  dataset_role: City-day AQI/API; joined with analyst visits and forecast dates
  evidence_type: working_paper_data_section
  evidence_url: https://sites.bu.edu/fisman/files/2019/09/Pollution_jfe.pdf
  data_note: Official environment department city daily air quality.
- cite: 'Axbard & Deng (2024), Informed Enforcement: Lessons from Pollution Monitoring in China'
  doi: https://doi.org/10.1257/app.20210386
  journal: AEJ:Applied
  year: 2024
  dataset_role: Monitoring station introduction and pollution measurement; additionally independently geocoded enforcement
    data
  evidence_type: paper_data_section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257/app.20210386
  data_note: The law enforcement record in this article cannot be equated with the investigation of corporate pollution emissions.
provenance:
- source: https://www.mee.gov.cn/hjzl/dqhj/
  field_scope:
  - provider
  - current_access
  - variables
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://sites.bu.edu/fisman/files/2019/09/Pollution_jfe.pdf
  field_scope:
  - paper_use
  - frequency
  - variables
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://www.aeaweb.org/articles?id=10.1257/app.20210386
  field_scope:
  - paper_use
  - monitoring_policy
  added: '2026-07-10'
  confidence: high
  verified: true
related_datasets:
- id: china-satellite-pm25
  relation: complement
- id: china-firm-pollution
  relation: often-confused-with
---

## Positioning in one sentence

Official air quality monitoring data provide high-frequency pollution concentrations at monitoring stations/cities, suitable for exposure and short-term behavioral studies. It is three different data objects from corporate emission surveys and satellite retrieval of PM2.5.
