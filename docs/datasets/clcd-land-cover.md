---
schema_version: 3
catalog_status: ready
id: clcd-land-cover
name: CLCD 30 m annual land cover dataset of China (中国30米年度土地覆被数据集)
aka:
- CLCD
- China Land Cover Dataset
- 中国土地覆被数据集
- Yang and Huang land cover
- 30m annual land cover China
provider: >-
  Produced by Jie Yang and Xin Huang, Wuhan University (per the DataCite
  record 10.5281/zenodo.5816591, fetched 2026-08-15); distributed openly via
  Zenodo (DOI 10.5281/zenodo.5816591, version 1.0.1, issued 2022-08-09,
  CC-BY-4.0) with a mirror on the National Tibetan Plateau / Third Pole
  Environment Data Center (TPDC, data.tpdc.ac.cn; page JS-gated this round).
  The companion paper is Yang & Huang (2021), Earth System Science Data
  13:3907-3916, DOI 10.5194/essd-13-3907-2021, which states the data are
  freely available at DOI 10.5281/zenodo.4417810 (an earlier deposit;
  discrepancy with 10.5281/zenodo.4417809 recorded in caveats).
china_related: true
domains:
- environment
- land
- urban
- agriculture
- spatial
- climate
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Annual land-cover classification rasters for China at 30 m resolution,
    one GeoTIFF for 1985 and one for each year 1990-2021, downloadable from
    Zenodo (files include *_albert.tif projected variants per the record
    description; projection: AEA +proj=aea +lat_1=25 +lat_2=47 +lat_0=0
    +lon_0=105 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs).
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider-first grounding (2026-08-15): the DataCite record for
    10.5281/zenodo.5816591 was fetched and read - title "The 30 m annual
    land cover datasets and its dynamics in China from 1990 to 2021",
    creators Jie Yang and Xin Huang (Wuhan University), Zenodo v1.0.1,
    CC-BY-4.0 Open Access; description confirms construction from 335,709
    Landsat images on Google Earth Engine with random-forest classification
    and spatial-temporal filtering, and that "CLCD in 2021 is now
    available". The companion ESSD paper abstract (Crossref, read) confirms
    the 1990-2019 version, training from CLUD + visual interpretation,
    overall accuracy 79.31% on 5,463 visually interpreted samples and
    outperformance of MCD12Q1/ESACCI_LC/FROM_GLC/GlobeLand30 on 5,131
    third-party test samples. The TPDC mirror page is JS-gated (200 shell
    only). The current Zenodo API is now readable and lists the file manifest;
    its single-file content endpoint returned HTTP 403 to this environment's
    generic HTTP client, so normal-browser download remains the appropriate
    acquisition route.
  barrier: >-
    Large file sizes (30 m national rasters per year) are the main practical
    constraint. The current manifest includes a classification-system workbook,
    but its internal class-code meanings were not parsed in this unit; read it
    before producing class-specific outcomes. TPDC mirror terms remain separate.

unit_of_observation: >-
  30 m grid cell (pixel) x year; annual land-cover class per pixel across
  China's land surface
structure: gridded raster time series (annual)
geo_granularity:
- 30 m pixel (grid)
- aggregateable to county/city/province or any zonal unit
geography: China (mainland land surface; provincial-level coverage)
time_span:
  start: '1985'
  end: '2021'
  last_confirmed_release: 'CLCD v1.0.1 covers 1990-2021 (DataCite record 10.5281/zenodo.5816591, issued 2022-08-09)'
  coverage_note: >-
    The current v1.0.1 manifest has a 1985 national raster, then annual
    national rasters for every year 1990-2021; it does not supply 1986-1989.
    Whether later years are released in a newer record was not verified.
  last_checked: '2026-09-28'
frequency:
- annual
sample_size: >-
  National 30 m grid (~pixel counts in the tens of billions per year; exact
  grid dimensions per file unread)
key_variables:
- Land-cover class per pixel per year (the current deposit includes CLCD_classificationsystem.xlsx; read it before assigning class meanings)
- Raster format GeoTIFF (tif; *_albert.tif projected variants)
- Derived trend facts from the paper: impervious surface +148.71%, water +18.39%, cropland -4.85%, grassland -3.29%, forest +4.34% over 1985-2019

research_fit:
  best_for:
  - Land-use and land-cover change outcomes or controls for China at 30 m annual resolution (urban expansion, cropland change, ecological programs)
  - Zonal aggregation of land-cover composition to county/city units for panel designs
  - Urbanization measurement via impervious surface area where satellite night lights are too coarse or correlated with other channels
  choose_over:
  - Choose CLCD over the RESDC 30 m land-use remote-sensing monitoring dataset when a direct, openly licensed download (CC-BY-4.0, Zenodo) matters and annual 1990-2021 coverage suffices; RESDC uses a different land-use scheme and its own registration route.
  - Choose CLCD over MCD12Q1/GlobeLand30 for China-specific 30 m annual series (accuracy evidence per the companion paper).
  - For activity/energy intensity use night lights (china-nighttime-lights) instead; land cover measures physical land class, not activity.
  not_good_for:
  - Sub-annual (seasonal/intra-year) land dynamics (annual only)
  - Non-China coverage (national product)
  - Land-use *transactions* or ownership (use china-land-transaction)
  - Built-environment structure beyond the impervious class (no building heights etc.)
  needs_join_for:
  - Admin boundary maps for zonal aggregation (county/city polygons)
  - Outcomes: firm, household or policy panels (asif, cfps, china-gov-procurement etc.)
  - Complement with china-nighttime-lights for activity-based urban measures
  variation_available:
  - Pixel/year variation in land-cover class; annual transitions (e.g. cropland-to-built, afforestation) usable as exposure or outcome
  topics:
  - land cover
  - land use
  - urban expansion
  - cropland
  - impervious surface
  - remote sensing
  - Landsat

good_for:
- land-use change measurement
- urban expansion outcomes
- agricultural land change
- zonal land-cover composition panels
identification:
- land-cover transition events
- panel variation with zonal aggregation
linkable_keys:
- Pixel coordinates (lat/lon)
- Year
- Aggregation zones (county/city codes via boundary join)

joins:
- target: china-nighttime-lights
  relation: complement
  keys:
  - pixel/zone
  - year
  method: physical land cover (CLCD) vs activity intensity (NTL) joint measures of urbanization
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - county/city
  - year
  method: zonal land-cover aggregates joined to statistical panels
  evidence_status: plausible

access_routes:
- route: zenodo-download
  access_status: available
  direct_url: https://zenodo.org/records/5816591
  requirements: A normal browser and enough local storage for the selected annual raster(s) or province ZIP(s); the current record is CC-BY-4.0 and open.
  steps:
  - Open the Zenodo record 10.5281/zenodo.5816591 (or resolve the DOI).
  - Choose either the national `*_albert.tif` raster or its corresponding `*_albert_province.zip` delivery for the needed year; the manifest has 33 of each, for 1985 and 1990-2021.
  - Download CLCD_classificationsystem.xlsx alongside the raster and read it before class-specific aggregation.
  - Cite the dataset and companion paper (Yang & Huang 2021 ESSD) per CC-BY-4.0.
  deliverable: Thirty-three national projected GeoTIFFs, thirty-three province ZIP deliveries, and a classification-system workbook in v1.0.1; open deposit license.
  cost: free
  last_checked: '2026-09-28'
  caveat: Zenodo's current API lists 67 files totalling 64,554,946,550 bytes, but a direct request to the workbook content URL returned HTTP 403 to this environment's generic HTTP client. Use the normal Zenodo record/browser route and verify the selected file checksum before analysis.
- route: tpdc-mirror
  access_status: available-with-registration
  direct_url: https://data.tpdc.ac.cn/
  requirements: TPDC account (registration); page JS-gated this round
  steps:
  - Search 国家青藏高原科学数据中心 for CLCD (中国土地覆被).
  - Register and download through the TPDC flow.
  deliverable: Same CLCD family via the Chinese mirror; download terms per TPDC.
  cost: free
  last_checked: '2026-08-15'
  caveat: The specific TPDC dataset page could not be read (JS shell); the mirror's exact dataset entry is unverified.

access:
  url: https://zenodo.org/records/5816591
  cost: free
  license: CC-BY-4.0 (DataCite rightsList, read 2026-08-15)
  format:
  - GeoTIFF
  api: true
  how_to_get: Open Zenodo record 10.5281/zenodo.5816591 in a normal browser, choose the needed 1985 or 1990-2021 projected GeoTIFF or provincial ZIP, download CLCD_classificationsystem.xlsx, and verify its listed checksum before aggregation. TPDC is a separate registered mirror.
caveats: >-
  The companion paper states availability at 10.5281/zenodo.4417810 while the
  DataCite record lists its versionOf as 10.5281/zenodo.4417809 - the earlier
  deposit identity has this unresolved DOI discrepancy; both point to the
  same CLCD family and the v1.0.1 (1985 plus 1990-2021) record is the verified
  current one. The classification workbook is available, but its class codes
  were not parsed in this unit.
  Post-2021 releases unverified.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://api.datacite.org/dois/10.5281/zenodo.5816591 (fetched 2026-08-15)
  field_scope:
  - identity
  - creators
  - coverage_years
  - license
  - version
  - construction_description
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.crossref.org/works/10.5194/essd-13-3907-2021 (abstract, fetched 2026-08-15)
  field_scope:
  - accuracy
  - trends
  - method_summary
  - availability_statement
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://data.tpdc.ac.cn/ (mirror page, fetched 2026-08-15; JS shell)
  field_scope:
  - mirror_existence
  added: '2026-08-15'
  confidence: med
  verified: false
- source: Zenodo API record 5816591, queried 2026-09-28
  field_scope:
  - current v1.0.1 title, dataset type and CC-BY-4.0 deposit licence
  - 67-file manifest and total byte count
  - 33 national GeoTIFFs and 33 province ZIPs for 1985 and 1990-2021
  - CLCD_classificationsystem.xlsx presence, sizes, checksums and browser-route caveat
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-nighttime-lights
  relation: complement
- id: china-land-transaction
  relation: complement
---

## Positioning in one sentence

CLCD is the openly licensed (CC-BY-4.0) 30 m annual land-cover dataset of China built from Landsat/GEE (Yang & Huang, Wuhan University), downloadable directly from Zenodo for 1990-2021 - the standard high-resolution land-use change layer for zonal outcomes and controls in Chinese spatial research.

## Select rules

- Prioritize for pixel/zonal land-cover composition and land-use change in China at 30 m annual resolution with an open direct download.
- Choose RESDC land-use remote-sensing products instead only when their different classification scheme or registration route fits the design; verify scheme differences before switching.
- Do not use land cover as a proxy for economic activity intensity - use china-nighttime-lights for activity channels; use china-land-transaction for land transfer/price events.

## Get recipe

1. Open the Zenodo record 10.5281/zenodo.5816591 (v1.0.1, 1990-2021).
2. Download the annual GeoTIFF files (confirm the file inventory on the record page first).
3. Aggregate pixels to the analysis zones (county/city) with a boundary layer; keep the exact version in the analysis record.
4. Cite the dataset and the companion ESSD paper per CC-BY-4.0.

## Connections and Limitations

- Unresolved DOI discrepancy between the paper's availability statement (10.5281/zenodo.4417810) and the DataCite versionOf (10.5281/zenodo.4417809) is retained; the v1.0.1 record (10.5281/zenodo.5816591) is the verified current download.
- Class scheme (class list/codes) and file inventory were not read this round; verify on the record page before building class-level outcomes.
- Post-2021 releases were not verified; check for newer records if the design needs 2022+.
- Zenodo itself was unreachable from this environment; the DataCite API and Crossref were used as authoritative metadata sources - download flow should be confirmed by the researcher.
