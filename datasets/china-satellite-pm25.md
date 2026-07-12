---
schema_version: 2
catalog_status: grounding
id: china-satellite-pm25
name: Chinese satellite retrieval and fusion of PM2.5 data
aka:
- 卫星PM2.5
- Satellite-derived PM2.5
- Global Annual PM2.5 Grids
- TAP PM2.5
- 中国网格PM2.5
provider: Multiple independent products; including global satellite retrieval grid and Tracking Air Pollution in China (TAP)
  fusion product
china_related: true
domains:
- environment
- health
- migration
- urban
- development
unit_of_observation: Grid-day / Grid-year (can be summed to counties, cities, and provinces)
structure: gridded-spatiotemporal
geo_granularity:
- grid
- County
- city
- province
geography: Full coverage in mainland China; resolution and year vary by product
time_span:
  start: 1998
  end: ongoing
  coverage_note: The paper commonly uses global annual satellite PM2.5; TAP also provides about 1km daily fusion products
    since 2000.
  last_confirmed_release: ongoing
  last_checked: '2026-07-10'
frequency:
- daily
- annual
sample_size: National regular grid; number depends on resolution and study boundaries.
key_variables:
- PM2.5 concentration
- Grid latitude and longitude
- date/year
- Uncertainty or calibration information
- Satellite AOD
- Meteorological and model auxiliary variables
research_fit:
  best_for:
  - Long-term, nationwide continuous PM2.5 exposure before and after monitoring station construction
  - Study on county and city population migration, health and productivity and medium and long-term pollution
  choose_over:
  - When continuous spatial coverage across the country or PM2.5 before 2013 is required, priority is given to monitoring
    at official sites.
  not_good_for:
  - Total pollution emissions of enterprises
  - Studies requiring full equivalence to ground-truth measurements
  needs_join_for:
  - It needs to be superimposed on the grid and administrative boundaries, and then joined with population, survey or enterprise
    location.
  variation_available:
  - Grid and annual pollution changes
  - Meteorological instrumental variables such as temperature inversion
  - Monitoring information before and after disclosure
  topics:
  - air pollution
  - PM2.5
  - long term pollution exposure
  - population migration
  - Meteorological instrumental variables
good_for:
- Long-term PM2.5 exposure
- pollution and migration
- pollution and health
- National Grid Environment Panel
identification:
- IV (thermal inversion/wind direction)
- panel fixed effects
- DID (information disclosure or policy)
- spatial matching
linkable_keys:
- Latitude and longitude
- Grid ID
- County/city administrative code
- date/year
joins:
- target: china-census
  relation: complement
  keys:
  - County/city code
  - Year
  method: spatial-aggregation
  evidence_status: literature-used
- target: cmds
  relation: complement
  keys:
  - city code
  - Year
  method: spatial-aggregation
  evidence_status: plausible
access_routes:
- route: tap
  access_status: available-with-registration-or-terms
  direct_url: http://tapdata.org.cn/
  requirements: Follow the data application, citation and usage instructions on the TAP website.
  steps:
  - Enter the TAP data platform.
  - Select contaminants, temporal and spatial resolution.
  - Apply according to the platform requirements or download and keep the version description.
  deliverable: China's high-resolution daily/annual fused pollution grid; the specific version shall be subject to the platform.
  cost: free
  last_checked: '2026-07-10'
- route: paper-specific-global-grid
  access_status: needs-verification
  direct_url: needs-verification
  requirements: First confirm the global PM2.5 grid version used in the paper data section, and then download it from the
    original data provider.
  steps:
  - Record the product name, version and resolution in the paper.
  - Get the same version from the product official website.
  - Save version and citation information.
  deliverable: Annual satellite retrieval PM2.5 grid consistent with the paper.
  cost: free
  last_checked: '2026-07-10'
access:
  url: http://tapdata.org.cn/
  cost: free
  license: Subject to product-specific data usage and citation terms
  format:
  - netcdf
  - geotiff
  - csv
  api: false
  how_to_get: First select the specific product and version. TAP can be used as a route for high-resolution fusion data in
    China; when reproducing existing papers, the same global grid version must be obtained by data section.
caveats: Satellite inversion/model fusion is not ground truth measurement; different products, versions and calibration methods
  cannot be directly mixed. Aggregation of grids into administrative districts requires area or population weighting.
quality:
  profile_status: partial
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Chen, Oliva & Zhang (2022), The Effect of Air Pollution on Migration: Evidence from China'
  doi: https://doi.org/10.1016/j.jdeveco.2022.102833
  journal: JDE
  year: 2022
  dataset_role: County-level five-year average PM2.5; joined with census migration and thermal inversion
  evidence_type: paper_data_section
  evidence_url: https://www.nber.org/system/files/working_papers/w24036/w24036.pdf
  data_note: Use satellite retrievals of PM2.5 instead of corporate emissions surveys.
- cite: Khanna, Liang, Mobarak & Song (2025), The Productivity Consequences of Pollution-Induced Migration in China
  journal: AEJ:Applied
  year: 2025
  dataset_role: City annual PM2.5; combined with migration and spatial model data
  evidence_type: online_appendix
  evidence_url: https://assets.aeaweb.org/asset-server/files/22334.pdf
  data_note: The specific product version should still be further registered in the replication package.
provenance:
- source: https://www.nber.org/system/files/working_papers/w24036/w24036.pdf
  field_scope:
  - paper_use
  - unit_of_observation
  - identification
  added: '2026-07-10'
  confidence: high
  verified: true
- source: http://tapdata.org.cn/
  field_scope:
  - alternative_access
  - coverage
  added: '2026-07-10'
  confidence: high
  verified: true
related_datasets:
- id: china-air-quality-monitoring
  relation: complement
- id: china-census
  relation: complement
- id: china-firm-pollution
  relation: often-confused-with
---

## Positioning in one sentence

Satellite/fusion PM2.5 is used for continuous, long-term pollution exposure across the country. It is not corporate emissions, nor is it equivalent to the actual measured value at official monitoring stations. The product, version, resolution and aggregation method must be clearly stated before use.
