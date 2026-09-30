---
schema_version: 3
catalog_status: ready
id: gfw-static-apparent-fishing-effort-v3-2012-2024
name: Global Fishing Watch static AIS-based apparent fishing effort, version 3 (2012-2024)
aka:
- GFW fishing effort v3
- Global static dataset of AIS-based apparent fishing effort
- global-fishing-watch.fishing_effort_v3
provider: Global Fishing Watch (GFW)
china_related: true
domains:
- marine
- regional
- environment
- satellite

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    GFW's fixed, quality-assured 2025 version-3 release of global AIS-based
    apparent fishing effort through December 2024. The release supplies
    gridded fishing-hour files; it is not the live Map/API stream and not
    raw AIS tracks.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    An ordinary non-commercial researcher can create a free GFW account,
    accept the terms, and select the static fishing-effort product in the
    data-download portal. GFW states that version 3 covers 2012-2024 and is
    a fixed release that received additional cleaning and manual review.
  barrier: >-
    Registration and agreement to GFW's terms are required. The download is
    a product-level route, not access to the provider's commercial raw AIS
    feed; changing AIS reception, particularly around China and Southeast
    Asia, constrains time trends.

unit_of_observation: >-
  A gridded apparent-fishing-hour aggregate: daily 0.01-degree cells by flag
  state and gear type, monthly 0.1-degree cells by flag state and gear type,
  or daily 0.1-degree cells by MMSI, depending on the selected static file.
structure: gridded spatial-time panel (product-specific daily or monthly files)
geo_granularity:
- 0.01-degree grid (daily flag-state/gear-type product)
- 0.1-degree grid (monthly flag-state/gear-type or daily MMSI product)
geography: Global oceans, including waters around China; coverage is AIS-equipped fishing vessels rather than all vessels or all fishing activity.
time_span:
  start: '2012'
  end: '2024'
  last_confirmed_release: GFW apparent fishing effort version 3, released 2025-03-11; fixed through December 2024
  coverage_note: >-
    GFW reports about 695 million apparent fishing hours from more than
    192,000 unique MMSI across the full release. It assigns apparent fishing
    hours after vessel and activity classification; it does not represent a
    census of China-flagged boats, all boats operating in Chinese waters, or
    raw AIS positions.
  last_checked: '2026-09-28'
frequency:
- daily
- monthly
sample_size: >-
  Approximately 695 million apparent fishing hours and more than 192,000
  unique MMSI in the full 2012-2024 release (provider-reported); any China
  subset depends on the selected file and researcher-defined spatial or flag
  filter.
key_variables:
- apparent fishing hours
- grid location and date or month
- flag state
- gear type
- MMSI (daily 0.1-degree product)

research_fit:
  best_for:
  - Building a transparent China-adjacent or China-flagged fishing-activity panel from a fixed, documented GFW release.
  - Describing broad spatial or temporal patterns of AIS-observed commercial fishing effort from 2012 through 2024.
  choose_over:
  - Choose this static release over the GFW Map/API when a reproducible, fixed and more heavily quality-reviewed 2012-2024 file is more important than near-real-time updates.
  - Choose the daily MMSI product only when the required analysis genuinely needs its vessel identifier; choose flag/gear aggregates when those are sufficient and more manageable.
  not_good_for:
  - Individual vessel tracks, raw AIS messages, or vessels that do not transmit AIS.
  - Treating changes in observed fishing hours as pure behavioral change without considering changing AIS reception and coverage.
  - Establishing the exact GFW file version used by a paper whose data section names GFW but does not identify a release.
  needs_join_for:
  - A China EEZ or coastline boundary when defining activity by location rather than by vessel flag.
  - A separately documented vessel registry when resolving a China fleet by owner or fleet identity rather than flag/MMSI.
  variation_available:
  - Observed apparent fishing hours are indexed by grid, date or month, and the selected flag/gear or MMSI product fields; these are data dimensions, not a causal design.
  topics:
  - fishing effort
  - AIS
  - maritime activity
  - Chinese waters

good_for:
- reproducible fishing-effort mapping
- marine spatial analysis
- China-adjacent ocean activity measures
identification:
- This data record provides no treatment assignment or causal design; such a design requires separate, project-specific evidence.
linkable_keys:
- MMSI (daily 0.1-degree product only)
- grid coordinates
- date or month
- flag state
- gear type

joins: []

access_routes:
- route: GFW data download portal
  access_status: available-with-registration
  direct_url: https://globalfishingwatch.org/data-download/
  requirements: Free self-service GFW registration, agreement to terms of use, acknowledgement in publications, and non-commercial use.
  steps:
  - Open GFW's Datasets & Code page and choose Download Data.
  - Register or log in, accept the terms, and select the static apparent-fishing-effort dataset rather than the Map/API stream.
  - Select the daily/monthly and spatial-resolution file family that matches the required unit and time range.
  - Preserve the chosen release, file names, filters, and terms acknowledgement with the analysis so that the China subset can be reproduced.
  deliverable: Static gridded apparent-fishing-effort files for the documented 2012-2024 version-3 release.
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    The account-mediated portal does not expose a stable anonymous file URL.
    GFW distinguishes this fixed release from its near-real-time Map/API
    product; do not silently substitute one for the other.
- route: Google BigQuery public dataset
  access_status: available
  direct_url: https://globalfishingwatch.org/dataset-and-code-fishing-effort/
  requirements: A Google Cloud/BigQuery environment; query and storage charges, if any, are governed by Google rather than stated here as free.
  steps:
  - Open the official fishing-effort product page and locate the named public BigQuery dataset `global-fishing-watch.fishing_effort_v3`.
  - Inspect schema and estimate query cost before extracting the intended years, cells, flags, gear types, or MMSI subset.
  - Record the query, extraction date, and selected partition/filter logic alongside the analysis.
  deliverable: Queryable copy of the same static version-3 fishing-effort release in BigQuery.
  cost: mixed
  last_checked: '2026-09-28'
  caveat: >-
    This is an alternative delivery channel, not evidence that raw AIS,
    live API output, or paper-specific cleaned panels are public.

access:
  url: https://globalfishingwatch.org/dataset-and-code-fishing-effort/
  cost: mixed
  license: CC BY-NC 4.0 for GFW data products; acknowledge GFW as required by its data-access page.
  format:
  - static gridded download files
  - Google BigQuery dataset
  api: false
  how_to_get: Create a free portal account for the static files, or use the official product page's named public BigQuery dataset after checking platform charges.
caveats: >-
  GFW builds apparent fishing effort from AIS positions using vessel
  characterization and fishing-detection models plus registry information.
  It excludes raw AIS access and cannot see non-transmitting vessels. AIS
  reception and the underlying provider mix changed over time; GFW notes a
  material 2022 reception improvement in waters around China and Southeast
  Asia. The static release removes some transit false positives and uses
  stricter fishing-vessel filtering than the Map/API, so it should not be
  concatenated with those streams as if measurements were identical.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Englander, Zhang, Villasenor-Derbez, Jiang, Hu, Deschenes & Costello (2025), Input subsidies and the depletion of natural capital: Chinese distant water fishing'
  doi: https://doi.org/10.1016/j.jeem.2025.103127
  journal: JEEM
  year: 2025
  dataset_role: >-
    Main outcome layer: GFW AIS-derived fishing-effort hours for China-flagged
    distant-water vessels, 2015-2020, matched by the authors to a separate
    RFMO/Rongcheng registry panel.
  evidence_type: data-section
  evidence_url: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content
  data_note: >-
    The accessible working-paper data section explicitly identifies GFW and
    AIS-derived fishing effort, then describes extracting China-flagged
    vessel-hours for 2015-2020. It does not name the later static version-3
    release; the ready record therefore gives a current reproducible GFW
    product with compatible coverage, not an assertion that the paper used
    these exact files.

provenance:
- source: https://globalfishingwatch.org/dataset-and-code-fishing-effort/
  field_scope:
  - product identity and construction summary
  - static-file formats and resolutions
  - BigQuery delivery channel
  - AIS coverage and reception limitations
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://globalfishingwatch.org/platform-update/global-fishing-watch-data-download-portal-version-3/
  field_scope:
  - version-3 2012-2024 coverage
  - fixed quality-assured release through December 2024
  - release scale and monthly 0.1-degree files
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://globalfishingwatch.org/datasets-and-code/
  field_scope:
  - free registration and acknowledgement requirements
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://globalfishingwatch.org/terms-of-use/
  field_scope:
  - CC BY-NC 4.0 data-product license
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content
  field_scope:
  - verified China-related paper use of GFW AIS-derived fishing effort
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: china-fishing-vessel-detection
  relation: often-confused-with
---

## Positioning in one sentence

This is the current fixed GFW AIS-based fishing-effort release, not a generic
reference to the GFW platform: it supplies documented daily or monthly gridded
fishing-hour products for 2012-2024, reachable through a free registered route
or the named BigQuery dataset. Its decisive limitation is measurement: it is a
modelled record of AIS-observed apparent effort, not raw tracks or a census of
all fishing activity.

## Select rules

- Use this when the research question needs a reproducible, fixed ocean
  activity measure during 2012-2024 and a gridded or MMSI-level static file
  matches the desired unit.
- Use a separately documented boundary to define Chinese waters, and do not
  equate vessel flag with ownership, nationality, or location.
- Switch to a GFW live API/Map product only when near-real-time coverage is
  essential and its different processing pipeline is acceptable.
- Do not use it to reconstruct a paper's proprietary registry match, detailed
  individual tracks, or activity by boats that lacked AIS transmissions.

## Get recipe

1. Decide whether the needed analysis is grid-by-time, flag/gear aggregate, or
   MMSI-by-day; that choice determines the documented file family.
2. Register at the GFW portal, accept the terms, and download the version-3
   static files for the selected time and resolution. Alternatively, use the
   named public BigQuery dataset after checking query cost.
3. Keep the provider release description, chosen files or query, spatial
   boundary, flag/gear filters, and aggregation code. Those choices—not merely
   the phrase “GFW data”—define the resulting China-oriented panel.
4. Treat changes in AIS reception and coverage as a measurement limitation
   before interpreting time patterns.

## Connections and Limitations

- A China EEZ or coastline polygon can define location-based exposure; a
  China-flagged analysis instead uses the available flag fields. They answer
  different questions and should not be silently merged.
- The daily MMSI product permits a documented identifier-based join only where
  the other source genuinely contains compatible MMSI. The paper's RFMO and
  Rongcheng registry match is a separate author construction, not included in
  this download.
- GFW's static effort product is deliberately different from its Map/API
  output. It uses extra cleaning, stricter vessel filtering, and different
  raster conventions; preserve the source version when comparing results.
