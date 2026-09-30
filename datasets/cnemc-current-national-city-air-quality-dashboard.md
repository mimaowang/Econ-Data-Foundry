---
schema_version: 3
catalog_status: ready
id: cnemc-current-national-city-air-quality-dashboard
name: CNEMC public current national city air-quality dashboard (全国城市实时空气质量展示)
aka:
- 全国实时空气质量监测
- CNEMC city AQI dashboard
- 中国环境监测总站城市空气质量实时数据
provider: China National Environmental Monitoring Centre (CNEMC, 中国环境监测总站)
china_related: true
domains:
- environment
- air quality
- urban
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The public, browser-visible current national city air-quality display: a
    timestamped city list with AQI, air-quality level and primary pollutant,
    plus the page's prior-day city summary. It is a dated display that a
    researcher can manually document, not a released historical monitoring
    panel.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CNEMC's public homepage rendered a national real-time city list on
    2026-09-28. It visibly supplied city name, primary pollutant, quality
    level and AQI alongside a timestamp, and separately displayed the
    previous day's city summary list. The homepage also visibly identifies
    CNEMC as operator and links to its national real-time air-quality page.
    A researcher can preserve a bounded snapshot with its displayed time and
    fields. This observation does not establish a downloadable archive, API,
    historical look-back function, stable city universe, or reuse licence.
  barrier: >-
    This is an on-screen current/previous-day display. It cannot stand in for
    the historic city-day or station-hour research panels used in papers, and
    it provides no basis for bulk collection or for treating unshown cities as
    zero or missing observations.

unit_of_observation: One city row in a timestamped current display or one city row in the page's previous-day summary display.
structure: Browser-visible national city cross-section; current and prior-day layers must be retained as separately dated observations.
geo_granularity:
- city
geography: China cities and prefecture-level areas visibly listed by CNEMC on the selected display; the page does not state a fixed or balanced city universe.
time_span:
  start: '2026-09-27'
  end: ongoing current display
  last_confirmed_release: Current display timestamp 2026-09-28 13:00:00 and prior-day summary dated 2026-09-27
  coverage_note: >-
    Only the observed current and prior-day displays are established. Neither
    is evidence of a complete 2026 archive, an earlier start date, continuous
    daily coverage, or a stable geographic roster.
  last_checked: '2026-09-28'
frequency:
- current timestamped display
- daily summary display
sample_size: Page-specific city list; no city count or complete universe is claimed.
key_variables:
- City name as displayed
- AQI
- Air-quality level
- Primary pollutant label
- Current-display timestamp or summary date

research_fit:
  best_for:
  - A transparently dated descriptive snapshot of currently visible national city air quality
  - Manually documented short-horizon comparisons of the displayed city AQI and pollution labels
  choose_over:
  - Choose this record when the question is about what CNEMC publicly displayed on a specific current or prior day.
  - Choose china-mee-monthly-city-air-quality-reports for dated monthly PDF summaries.
  - Use china-air-quality-monitoring only after a separate route for the required historic city-day or station-hour panel is established.
  not_good_for:
  - A balanced historical city-day panel, station-hour panel, exposure history, or event study requiring dates beyond the retained snapshots
  - Exact pollutant concentrations, station locations, an AQI methodology change analysis, or a causal treatment assignment
  - Automated bulk collection, redistribution, or claims about cities not visible in a retained display
  needs_join_for:
  - A documented city-name or administrative-code crosswalk before linking the snapshot to city outcomes
  - A separately verified historical data route when research needs repeated observations
  variation_available:
  - Cross-city differences in the values displayed at one retained timestamp
  - Differences across separately preserved dates, subject to the unverified historical-depth and roster boundary
  topics:
  - city air quality
  - urban environmental conditions
  - descriptive pollution monitoring

good_for:
- Dated descriptive snapshots of CNEMC's public city-level AQI display
- Verifying whether an observed city appears in the official current dashboard
identification:
- >-
  Identify an extract by the CNEMC page URL, page type (current or prior-day
  summary), displayed timestamp/date, city label, AQI, quality level and
  primary-pollutant label. Do not relabel AQI as a concentration.
linkable_keys:
- Displayed city name
- Displayed timestamp or summary date

joins:
- target: china-air-quality-monitoring
  relation: component
  keys:
  - city name
  - timestamp/date
  method: >-
    This is the actually visible public slice of the broader official
    monitoring family. It does not establish access to the latter's historic
    research panel or station readings.
  evidence_status: verified
- target: china-mee-monthly-city-air-quality-reports
  relation: complement
  keys:
  - city name
  - month
  method: >-
    A dashboard snapshot and a monthly PDF are distinct publication layers;
    preserve their different dates, universes and measures before comparison.
  evidence_status: plausible

access_routes:
- route: CNEMC public homepage real-time and prior-day city displays
  access_status: available
  direct_url: https://www.cnemc.cn/
  requirements: A normal browser; no account was required for the observed display.
  steps:
  - Open CNEMC's homepage and locate the national real-time city-air-quality display.
  - Record whether the row is from the current display or the prior-day summary, then retain its visible timestamp or date.
  - Preserve the city label, AQI, quality level and primary-pollutant label with the page URL and retrieval time.
  - Stop at the visible layer; use another documented source if a historical panel, file, API or station measurements are needed.
  deliverable: Manually recordable, timestamped current-city or prior-day city AQI display rows.
  cost: free
  last_checked: '2026-09-28'
  caveat: The observed page proves a visible display only, not a historical archive, bulk export, API, stable city universe or reuse permission.

access:
  url: https://www.cnemc.cn/
  cost: free
  license: Provider terms were not separately read; do not assume permission for bulk reuse or redistribution.
  format:
  - browser-visible city list
  api: false
  how_to_get: Preserve the page's displayed city rows and their timestamp/date manually, with the exact labels shown by CNEMC.
caveats:
- A current display and a prior-day summary have different observation times and must not be merged without labels.
- AQI and air-quality levels are displayed indices/categories, not verified raw pollutant concentrations.
- The page does not establish a fixed city roster, historic download route, API, archive depth or bulk-use terms.
- This ready public layer is distinct from the underlying monitoring-data family and cannot reproduce a paper's historical city-day or station-hour panel.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'
used_by: []
provenance:
- source: Rendered CNEMC homepage https://www.cnemc.cn/ (browser read 2026-09-28)
  field_scope:
  - CNEMC public homepage identity and operator attribution
  - visible national real-time city list with city, primary pollutant, level, AQI and 2026-09-28 13:00:00 timestamp
  - visible prior-day city summary dated 2026-09-27 with the same displayed categories
  - boundary against archive, API, bulk-export, fixed-universe and reuse claims
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-air-quality-monitoring
  relation: component
- id: china-mee-monthly-city-air-quality-reports
  relation: complement
---

## Positioning in one sentence

This is the genuinely obtainable public display layer of CNEMC city air quality: a dated, manually preservable current or prior-day city AQI list, not a replacement for a historical pollution panel.

## Select rules

- Choose it for a dated description of the city values CNEMC visibly displayed.
- Use the monthly-report record when a dated official PDF is enough.
- Do not use it when the design needs historical completeness, raw readings, stations, a balanced panel or a causal treatment.

## Get recipe

1. Open the CNEMC homepage and find the national real-time city display.
2. Note whether the observation is current or the prior-day summary, and keep the displayed time/date.
3. Transcribe the visible city label, AQI, quality level and primary pollutant with URL and retrieval time.
4. If more dates or raw readings are required, stop and establish a separate authorised historical route.

## Connections and limitations

City names can be connected to city outcomes only after a documented crosswalk. The key limitation is temporal and institutional: the visible screen says what the public site showed at that moment, not what it can deliver for research at scale.
