---
schema_version: 2
catalog_status: ready
id: era5-land
name: ERA5-Land land surface reanalysis meteorological data (ERA5-Land)
aka:
- ERA5-Land
- ERA5陆面再分析
- ERA5气象数据
- ERA5温度数据
- 再分析气象数据
provider: Copernicus Climate Change Service（C3S）/ European Centre for Medium-Range Weather Forecasts（ECMWF）
china_related: true
domains:
- environment
- climate
- geography
- health
- agriculture
- urban
- labor
unit_of_observation: Regular latitude and longitude grid-hour (can be aggregated by user into day/month or administrative
  area-period)
structure: gridded-spatiotemporal
geo_granularity:
- grid
- County/city/province (after user space aggregation)
geography: Global land coverage, including mainland China; CDS distribution grid 0.1° × 0.1°
time_span:
  start: 1950-01
  end: ongoing
  last_confirmed_release: '2026-07-08'
  coverage_note: Official catalog confirmed hourly as of January 1950; most recent live portion may lag and be revised.
  last_checked: '2026-07-11'
frequency:
- hourly
- daily (user aggregation or CDS-derived statistics)
- monthly (user aggregation or CDS monthly product)
sample_size: Global 0.1° regular latitude and longitude land surface grid; China sample size depends on study boundary, time
  window and variable selection.
key_variables:
- 2 meters temperature
- 2 meters dew point temperature
- total precipitation
- 10m wind speed component
- surface pressure
- shortwave radiation
- evaporate
- runoff
- soil temperature
- soil moisture
- Grid latitude and longitude
- Timestamp
research_fit:
  best_for:
  - Long-term, continuous, and spatially matchable exposure to high temperature, precipitation, wind speed, and soil moisture
    in China
  - Day/period exposure matching between high temperature and micro-outcomes such as cognition, health, care and labor supply
    in middle-aged and elderly people
  - Designs that require consistent weather control or weather shocks across regions in agricultural, environmental, and urban
    research
  choose_over:
  - When long-term, regularly gridded, and reproducibly downloadable meteorological exposures are needed across the country,
    they are preferred over local observations covering only a small number of sites.
  - ERA5-Land should not be used to replace ground observations such as CMA when real site readings, urban microclimate or
    official site operational measurement definitions are required
  not_good_for:
  - Study on Treating Reanalysis Values as Measured Values of a Single Weather Station
  - Studies requiring block, room or building scale thermal exposure
  - Micro-level studies without restricted geographical information that cannot reliably match individuals/firms/villages
    to grids or boroughs
  needs_join_for:
  - Household, person, business or village results need to be matched by protected latitude/longitude/region and date; aggregation
    rules should be clear when only province-year
  - Research on pollution instrumental variables or mechanisms usually also requires joining pollution, topography, population
    or policy data and checking spatial scales separately.
  variation_available:
  - Grid - hourly weather fluctuations
  - climate differences between regions
  - Extreme heat/precipitation events
  - Long-term climate trends
  topics:
  - weather
  - Meteorology
  - high temperature
  - extreme heat
  - temperature
  - precipitation
  - heat wave
  - wind speed
  - Agricultural weather shocks
  - Meteorological instrumental variables
good_for:
- Study of exposure to extreme heat, precipitation or wind speeds on health, cognition, labor supply, migration and consumption
- Match daily or monthly weather to CHARLS, CFPS, RFD or corporate locations by latitude/longitude/borough
- Adding reproducible weather control to pollution, agricultural output or energy demand in environmental economics
identification:
- panel fixed effects
- Extreme weather event research
- DID (policy × weather heterogeneity)
- IV (weather impact; need to be separately demonstrated to exclude restrictions)
- spatial matching
linkable_keys:
- Latitude
- longitude
- Grid coordinates
- date/hour
- Administrative district code (after spatial superposition)
joins:
- target: charls
  relation: complement
  keys:
  - Restricted community/county geographic information
  - Investigation date or investigation period
  method: spatial-temporal-match
  evidence_status: plausible
- target: cfps
  relation: complement
  keys:
  - Restricted village/community/county level geographical information
  - Investigation date or investigation period
  method: spatial-temporal-match
  evidence_status: plausible
- target: rfd
  relation: complement
  keys:
  - Village/county/province spatial information
  - Year or farming season window
  method: spatial-temporal-match
  evidence_status: plausible
- target: china-satellite-pm25
  relation: complement
  keys:
  - Grid/Administrative District
  - date/year
  method: spatial-temporal-match
  evidence_status: plausible
access_routes:
- route: cds-web-download
  access_status: available-with-registration
  direct_url: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview
  requirements: Register a Copernicus Climate Data Store (CDS) account and accept the applicable terms on the data set page;
    download, use and attribution comply with the current license on this page.
  steps:
  - Register and log in to CDS; do not write personal access tokens, cookies, or account information to the project.
  - Open the ERA5-Land hourly data from 1950 to present page and select the variables, date/period, and China study boundary
    in Download.
  - Confirm the time scale, grid resolution and output format of the accumulated variables before submitting; save the request
    conditions, product page date and citation information after downloading.
  deliverable: ERA5-Land regular grid reanalysis data exported by selected variables, periods, and spatial boundaries; current
    catalog of full hourly products labeled GRIB.
  cost: registration
  last_checked: '2026-07-11'
  caveat: Account registration does not mean offline public mirroring; the service may be maintained, and near-real-time data
    may be lagging or revised. The current license and optional formats are subject to the CDS page.
- route: cds-api
  access_status: available-with-registration
  direct_url: https://cds.climate.copernicus.eu/how-to-api
  requirements: Registered for CDS, manually accepted the terms on the target dataset page, and saved the CDS access token
    in the native personal configuration.
  steps:
  - First construct and check a request on the target data set download page of CDS.
  - Use the page's Show API request code to generate a request that matches the current product; the token is only placed
    in the local private configuration and is not written to the knowledge base, logs or code.
  - After a small range trial, download in batches by year/variable, record the requested version and aggregation processing.
  deliverable: Selected ERA5-Land data files can be requested repeatedly via the CDS API; exact format, queue limits, and
    request syntax are subject to the current CDS documentation.
  cost: registration
  last_checked: '2026-07-11'
  caveat: The API facilitates bulk retrieval, but is not a reason for the agent to collect or save user tokens; any requests
    are subject to the current terms and limits of CDS.
access:
  url: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview
  cost: registration
  license: Used in accordance with the current terms of CDS and the license shown on this dataset page; you must accept the
    terms and cite as required before downloading.
  format:
  - grib
  api: true
  how_to_get: Register CDS, open the ERA5-Land product page and accept the terms, select variables, time periods and spatial
    boundaries and download from the web page; when repeated requests are required in batches, use the CDS API request code
    generated on the product page and leave the personal token in the local private configuration.
caveats: ERA5-Land is a reanalysis product driven by models and assimilation, not point-by-point actual measurements from
  Chinese ground stations. The 0.1° grid value represents the grid average land surface state; the exposure structure from
  the grid to individuals, enterprises or administrative areas requires pre-defined spatial matching, time windows and cumulative
  variable processing, and cannot be regarded as an exact match just because they are in the same city.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-07-11'
used_by: []
provenance:
- source: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview
  field_scope:
  - identity
  - coverage
  - resolution
  - frequency
  - key_variables
  - access
  - license
  added: '2026-07-11'
  confidence: high
  verified: true
- source: https://cds.climate.copernicus.eu/how-to-api
  field_scope:
  - api_access
  - registration
  - terms_acceptance
  added: '2026-07-11'
  confidence: high
  verified: true
related_datasets:
- id: china-satellite-pm25
  relation: complement
- id: china-air-quality-monitoring
  relation: complement
- id: rfd
  relation: complement
---

## Positioning in one sentence

ERA5-Land is a regular grid product for global land surface reanalysis. It is suitable for constructing long-term, continuous, and reproducible exposures to temperature, precipitation, wind speed, and soil moisture for studies in China; it is not a CMA site readout and cannot alone address microsite-constrained issues.

## Select rules

- Choose ERA5-Land first when studying high temperature, precipitation, or weather shocks and need repeatable grid exposures going back to 1950.
- When studying a certain monitoring station, site operational observations, or urban heat islands, first look for corresponding ground stations/local observations, and do not replace actual measurements with re-analysis.
- When the results for individuals, companies, and villages only have rough administrative regions or dates, design aggregation and time windows first; the matching rules themselves are part of the research design.

## Get recipe

1. Register with CDS and open the ERA5-Land product page, accepting the current terms of the product.
2. First use the web page to select variables, dates and Chinese borders in a small range, and confirm the cumulative amount, time zone, grid and file format.
3. When needed in batches, API requests are generated from this product page; the token is only placed in the local private configuration.
4. Save download requests, product update dates, variable definitions, and spatial aggregation codes to ensure they can be reproduced in the future.

## Connections and Limitations

- Matching to microdata such as CHARLS/CFPS/RFD often requires restricted sites and survey periods; without these keys, only coarser administrative area exposures can be made, and precise individual exposure cannot be claimed.
- Accumulated variables such as precipitation, radiation and runoff must be checked against the time accumulation measurement definition before being converted into daily values or flows.
- The near real-time part will be updated; when replicating the verification study, the product version downloaded at that time and the request conditions should be recorded.
