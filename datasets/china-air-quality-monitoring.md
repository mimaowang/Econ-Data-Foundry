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
data_pathway:
  mode: hybrid
  origin: ready-made
  target_artifact: >-
    Underlying CNEMC/MEE monitoring readings used for city-day or station-hour research
    panels. The separately published MEE monthly-report PDFs are a different asset,
    recorded as china-mee-monthly-city-air-quality-reports, and are not an acquisition
    route for these underlying readings.
  availability: partially-reproducible
  ordinary_researcher_feasible: false
  summary: >-
    Papers in this record demonstrate use of official monitoring readings at city-day,
    city-year or station-related resolution. Their availability does not follow from the
    public MEE report archive: that archive is independently catalogued as
    china-mee-monthly-city-air-quality-reports. No ordinary public route to the complete
    historic station-hour or city-day readings behind those research panels has been
    verified here.
  barrier: >-
    No official, public, bulk historical station- or city-day delivery, API, full
    archive completeness statement, or machine-readable schema was verified in this
    unit. A researcher needing a panel must establish the exact provider route or use a
    separately documented compiled product; monthly report PDFs alone do not close that
    gap.
unit_of_observation: Monitoring station-hour/city-day/city-month underlying readings
structure: >-
  Underlying monitoring-data family; its station/hour and historic city/day delivery
  remain unverified as an ordinary research route
geo_granularity:
- monitoring station
- city
- province
geography: Cities at prefecture level and above across the country; monitoring stations and pollutant coverage expand with
  each year
time_span:
  start: unknown
  end: ongoing
  coverage_note: >-
    Papers establish that historical observations were used, but this record has not
    verified the first available measurement, a complete historical delivery, or a
    continuous public station/city panel. The visible MEE report sequence belongs to
    the separate monthly-report asset and must not be used to fill this gap.
  last_checked: '2026-09-28'
frequency:
- hourly
- daily
- monthly
sample_size: Monitoring station network in cities at prefecture level and above across the country; the number of cities and
  stations changes with the year. No complete historic station or city-day universe has been verified for this asset.
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
  - Evaluating a separately verified source of high-frequency ambient-pollution readings for city or monitoring-station research
  - Understanding what the cited papers' underlying monitoring inputs represent before seeking a provider route
  choose_over:
  - When hourly/daily frequency actual concentration monitoring is required, it takes priority over corporate emissions or
    annual satellite PM2.5
  not_good_for:
  - Total corporate emissions and treatment facilities
  - 1km of continuous PM2.5 exposure across the country before 2013
  needs_join_for:
  - Studying individuals, businesses or migration outcomes requires stitching together microdata by location and date
  variation_available:
  - Observed pollutant readings vary by monitoring station/city and timestamp.
  - Network coverage, station composition, and pollutant definitions change over time and must be checked before constructing a panel.
good_for:
- urban air pollution exposure
- AQI event research
- Monitoring information disclosure policy
- Air pollution and financial analyst behavior
identification: []
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
- route: boundary-reference-separate-monthly-report-series
  access_status: documentation-only
  direct_url: https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/
  requirements: None; this is a route for a different canonical asset, not for the readings in this record.
  steps:
  - If report-level monthly summaries are sufficient, switch to china-mee-monthly-city-air-quality-reports and follow its acquisition route.
  - Do not treat a downloaded report PDF or its city list as access to the monitoring readings represented by this record.
  deliverable: Documentation boundary only; the separately ready report-PDF asset, not a delivery of this asset.
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    Its archive page and July 2026 PDF were checked, but neither documents a bulk,
    machine-readable or complete historical delivery of underlying monitoring readings.
- route: official-realtime
  access_status: available-with-technical-friction
  direct_url: https://www.cnemc.cn/
  requirements: Real-time web pages; batch historical data may require a separately verified provider route.
  steps:
  - Enter the real-time air quality page of China Environmental Monitoring Station.
  - Search by city/site.
  - Confirm historical download permissions and measurement definition before using in batch research.
  deliverable: A current/recent monitoring display if the provider page allows it; a historic research-panel delivery was not verified.
  cost: free
  last_checked: '2026-09-28'
access:
  url: https://www.cnemc.cn/
  cost: mixed
  license: Historical batch access and reuse terms remain to be verified from the provider route.
  format:
  - html
  - pdf
  api: false
  how_to_get: >-
    For a city-day or station-hour panel, begin with the provider and verify an actual
    delivery route, scope, terms and historical completeness before collecting. The MEE
    monthly-report archive is only a pointer to the separate report-PDF asset and cannot
    establish access to this one.
caveats: >-
  API and AQI standards are not directly equivalent across time periods; monitoring
  station expansion itself changes coverage. A dated free monthly report is a different
  deliverable from the underlying readings. Neither report visibility nor real-time
  pages prove historic batch access, an API, a stable station roster, or a complete
  machine-readable city-day panel.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'
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
- cite: 'Ebenstein, Fan, Greenstone, He & Zhou (2015), Growth, Pollution, and Life Expectancy: China from 1991–2012'
  doi: https://doi.org/10.1257/aer.p20151094
  journal: AER
  year: 2015
  dataset_role: City-year pollution levels (PM10, SO2) for health impact analysis
  evidence_type: paper_data_section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257/aer.p20151094
  data_note: Combined city-year PM10 and SO2 measures from MEP/Environmental Yearbooks with DSP mortality data for a health-analysis dataset. The separate policy-identification argument is not part of this data record.
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
- source: https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/ and 2026-07 report page/PDF link (read 2026-09-28)
  field_scope:
  - current dated MEE monthly-report archive
  - direct report-page-to-PDF delivery for July 2026
  - boundary between report PDFs and unverified historical station/city panel access
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Rendered CNEMC homepage https://www.cnemc.cn/ (browser read 2026-09-28)
  field_scope:
  - visible current national city AQI display and its timestamped city rows
  - visible prior-day city summary display
  - boundary that these public displays do not establish historic panel, API or bulk access
  added: '2026-09-28'
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
- id: cnemc-current-national-city-air-quality-dashboard
  relation: component
- id: china-mee-monthly-city-air-quality-reports
  relation: successor
- id: china-satellite-pm25
  relation: complement
- id: china-firm-pollution
  relation: often-confused-with
---

## Positioning in one sentence

This record is the underlying official monitoring-reading family needed for high-frequency exposure work, not the separately obtainable MEE monthly-report PDF product. The latter is now recorded independently as `china-mee-monthly-city-air-quality-reports`; a bulk historical station-hour or city-day route for this asset remains unverified. Both differ from corporate emissions and satellite PM2.5.
