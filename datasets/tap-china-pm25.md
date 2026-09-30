---
schema_version: 3
catalog_status: ready
id: tap-china-pm25
name: Tracking Air Pollution in China (TAP) gridded PM2.5 products
aka:
- TAP PM2.5
- Tracking Air Pollution in China
- 中国大气污染追踪 PM2.5
provider: TAP research team, hosted at tapdata.org.cn; the product paper identifies the platform as a China multisource air-pollution data service.
china_related: true
domains:
- environment
- air pollution
- health
- urban

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    TAP provider-delivered gridded PM2.5 concentration products for China. Its
    public product catalogue exposes distinct PM2.5 download pages for the
    documented daily 10 km product and for a 1 km product; the latter page
    visibly offers CSV and NetCDF choices. The provider FAQ separately explains
    that 1 km requests are delivered as tiled links by email. It is a fused
    exposure surface, not ground-monitor readings, MERRA-2 raw diagnostics, or
    a global annual grid.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    TAP's live Chinese site states that users may apply for an account and
    download permission, that data products are public online, and that TAP
    products use CC BY-NC-ND 4.0. Its FAQ identifies concentration units as
    micrograms per cubic metre, grid coordinates as cell centres, a 60-day
    release delay for quality assurance, and a request-email tiled route for
    the 1 km product. The public catalogue now supplies concrete product-specific
    routes: the 10 km PM2.5 download page and a distinct 1 km page that visibly
    labels CSV and NetCDF. The product paper documents the 10 km daily
    full-coverage PM2.5 series since 2000, and a readable economics working
    paper verifies use of yearly-average 10 km grids aggregated to 338 Chinese
    prefectures for 2000-2020. A researcher can choose one of these provider
    products and apply for access, but must retain the approved vintage and
    supplied file metadata because approval and the delivered file set are
    provider-controlled.
  barrier: >-
    Account/download permission is application based, so delivery is not
    automatic and the approved files, quota and current catalogue details can
    change. The record supports choosing and starting a provider route, not
    claiming a particular request will be approved or that TAP supplies a
    paper's final city/county aggregation.

unit_of_observation: Grid cell x day (10 km baseline product; 1 km tiled product separately documented)
structure: gridded daily concentration surface
geo_granularity:
- 10 km grid
- 1 km grid (tiled request product)
geography: China; exact spatial boundary must be confirmed for the selected product request
time_span:
  start: '2000 for the documented 10 km PM2.5 series'
  end: ongoing with a stated 60-day delay in the provider FAQ
  last_confirmed_release: 'Live provider registration, licence and FAQ pages read 2026-09-28'
  coverage_note: The paper establishes 10 km daily coverage since 2000. The FAQ establishes that current public release can lag by 60 days; do not infer a particular latest date or 1 km historical start without the selected product metadata.
  last_checked: '2026-09-28'
frequency:
- daily
sample_size: Product and requested area dependent
key_variables:
- PM2.5 concentration in micrograms per cubic metre
- Grid-centre latitude and longitude

research_fit:
  best_for:
  - China-wide gridded PM2.5 exposure where a fused, full-coverage daily surface is required and the selected TAP product is approved
  choose_over:
  - Choose TAP over monitoring-station data when a continuous exposure surface is required rather than observed values only at stations.
  - Choose the paper-specific MERRA-2 construction record when reproducing Chen, Oliva and Zhang (2022), because TAP is a different product.
  not_good_for:
  - Ground-monitor readings, source emissions, or an unmodified satellite-AOD series
  - A ready-made county/city panel: geographic aggregation and weighting remain researcher steps
  - Claiming an economics paper used a specific TAP product without its data section
  needs_join_for:
  - Administrative boundaries or geocoded outcomes for aggregation from grid cells to research units
  - Population surfaces when calculating population-weighted exposure
  variation_available:
  - Daily PM2.5 across China grid cells; these measurements are data dimensions rather than a treatment definition
  topics:
  - PM2.5
  - air pollution
  - gridded exposure

good_for:
- China gridded PM2.5 exposure construction
identification:
- TAP is a provider-delivered, multisource fused PM2.5 concentration grid. Select either its 10 km or 1 km product route before requesting access; neither is a monitoring-station feed, a raw satellite product, or a ready-made administrative-unit panel.
linkable_keys:
- Grid-centre latitude and longitude
- Date

joins:
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - date
  - station location mapped to grid cell
  method: Compare or validate an exposure surface against monitoring observations only after matching the selected product and timing.
  evidence_status: plausible

access_routes:
- route: TAP account and requested download
  access_status: available-with-registration
  direct_url: http://tapdata.org.cn/?page_id=342&lang=zh
  requirements: Submit TAP's online account and download-permission application; comply with CC BY-NC-ND 4.0 attribution, non-commercial and no-derivatives conditions.
  steps:
  - Start at the TAP data-products catalogue, then choose the public 10 km PM2.5 download page (`?page_id=59&item=pm25`) or the distinct 1 km PM2.5 page (`?page_id=1162&item=pm25`).
  - On the 1 km page, choose CSV or NetCDF as appropriate; preserve the provider's tile/link metadata because this is not a single national administrative panel.
  - Read the TAP registration notice and submit the account/download-permission application for the selected product, resolution and period.
  - For a 1 km request, retain the email-delivered tile links and associated grid-coordinate metadata; for any product, record vintage and access date.
  - Confirm the requested product's current coverage, format and citation before analysis.
  deliverable: Provider-delivered gridded concentration files or tiled download links, conditional on account/download approval; the current public 1 km page exposes CSV and NetCDF choices.
  cost: registration
  last_checked: '2026-09-28'
  caveat: The registration notice proves an application route, not automatic approval or a fixed catalogue/download quota.

access:
  url: http://tapdata.org.cn/
  cost: registration
  license: CC BY-NC-ND 4.0 according to TAP's registration notice; cite TAP and do not redistribute modified derivatives without separate permission.
  format:
  - csv (1 km product page)
  - netCDF (1 km product page)
  - 10 km format requires confirmation in the approved delivery
  api: false
  how_to_get: Open TAP's public data-products catalogue, choose its 10 km or 1 km PM2.5 download page, then apply for account and download permission for the needed time/resolution. Retain the approved product vintage and supplied grid metadata.
caveats: >-
  TAP is a multisource fused product. Its value and limitations are distinct
  from monitoring data, global satellite grids, and the author-built MERRA-2
  PM2.5 record. The site documents a 60-day release delay and restricts
  derivatives under its stated licence; do not assume direct public bulk access
  or that a provider product reproduces any paper's aggregated exposure panel.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Li & Song (2024), Environmental Policy Coordination'
  journal: working paper
  year: 2024
  dataset_role: >-
    Yearly average TAP 10 km PM2.5 density, spatially aggregated with Chinese
    prefecture boundaries to a city-year PM2.5 measure for 338 prefectures,
    2000-2020.
  evidence_type: working_paper_data_section
  evidence_url: https://www.china-ces.org/Files/3058abstract/202501101937224713.pdf
  data_note: >-
    Section 3.4 states that the authors access TAP yearly-average 10 km grid
    estimates and aggregate them to city level with a Chinese prefecture map.
    This verifies paper use and a researcher aggregation step; it does not
    establish that TAP delivers the authors' final city panel or that the
    current provider account flow grants identical access.

provenance:
- source: http://tapdata.org.cn/?page_id=129&lang=zh (official data-products catalogue, read 2026-09-28)
  field_scope:
  - distinct public PM2.5 product links for the 10 km and 1 km download pages
  - catalogue boundary: these are provider product routes, not a city/county panel or a paper-specific final file
  added: '2026-09-28'
  confidence: high
  verified: true
- source: http://tapdata.org.cn/?page_id=1162&item=pm25&lang=zh (official 1 km PM2.5 download page, read 2026-09-28)
  field_scope:
  - 1 km PM2.5 product-page identity
  - visible CSV and NetCDF format choices
  - boundary that access still proceeds through TAP account/download approval
  added: '2026-09-28'
  confidence: high
  verified: true
- source: http://tapdata.org.cn/?page_id=342&lang=zh (official registration notice, read 2026-09-28)
  field_scope:
  - account and download-permission application route
  - CC BY-NC-ND 4.0 terms as stated by provider
  added: '2026-09-28'
  confidence: high
  verified: true
- source: http://tapdata.org.cn/?page_id=323&lang=zh (official FAQ, read 2026-09-28)
  field_scope:
  - concentration units and grid-centre coordinates
  - 60-day release delay
  - 1 km tiled request/download-link workflow
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://doi.org/10.1021/acs.est.1c01863 (TAP product paper, read 2026-09-28)
  field_scope:
  - multisource product construction
  - daily full-coverage 10 km PM2.5 product since 2000
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.china-ces.org/Files/3058abstract/202501101937224713.pdf (Li & Song working paper, section 3.4 read 2026-09-28)
  field_scope:
  - paper actual use of TAP
  - 10 km yearly-average grid input
  - city-level aggregation with Chinese prefecture boundaries
  - 338 prefectures, 2000-2020 analysis context
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-merra2-pm25-chen-oliva-zhang
  relation: often-confused-with
- id: china-air-quality-monitoring
  relation: complement
---

## Positioning in one sentence

TAP is an application-gated, provider-delivered China PM2.5 exposure surface: choose it for gridded daily concentration after selecting a named product, not as a substitute for monitoring stations or the paper-specific MERRA-2 construction.

## Select rules

- Use it when a continuous China exposure surface is required and its resolution, vintage and licence fit the project.
- Switch to monitoring data for observed station values and to the MERRA-2 record for the exact Chen–Oliva–Zhang lineage.
- Do not describe its grid as an administrative-unit panel until an explicit aggregation method has been applied.

## Get recipe

1. Apply for a TAP account and download permission.
2. Select the specific pollutant product, resolution and period in the provider interface.
3. Retain supplied file/grid metadata, the product vintage and the licence/citation information before constructing any city or county measure.

## Connections and Limitations

- The provider's 60-day delay is a live-product boundary.
- The 1 km product uses tiled delivery and has a distinct request workflow.
- Li and Song's documented 10 km city aggregation is an example of actual economics use, not evidence that TAP supplies a ready-made city panel or that every approved request includes the same vintage.
