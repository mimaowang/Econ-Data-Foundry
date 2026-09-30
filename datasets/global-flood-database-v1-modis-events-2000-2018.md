---
schema_version: 3
catalog_status: ready
id: global-flood-database-v1-modis-events-2000-2018
name: Global Flood Database v1 MODIS event inundation maps (2000-2018)
aka:
- GFD v1
- GLOBAL_FLOOD_DB/MODIS_EVENTS/V1
- Tellman et al. Global Flood Database
provider: Cloud to Street / Dartmouth Flood Observatory
china_related: true
domains:
- environment
- disaster
- spatial
- satellite
- regional

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The version-1 Global Flood Database event image collection: satellite
    observed MODIS inundation maps and event metadata for 913 mapped floods
    between 2000 and 2018. It is a raw spatial input, not the Chang-Zheng
    China firm-exposure panel.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The producer's public repository documents two usable routes: copy the
    complete GeoTIFF database from the public GCS bucket `gfd_v1_4` with
    `gsutil`, or access the named Earth Engine image collection after
    registering for Earth Engine's free research/education/nonprofit use.
    The Earth Engine catalog supplies the collection identity, band meaning,
    date range, country and DFO-ID filters, and licence.
  barrier: >-
    The product contains only successfully mapped, large satellite-observed
    flood events. A China event absent from GFD is not evidence that no flood
    occurred; cloud cover, event size and the source-event selection affect
    coverage. Exporting a large subset requires enough local/cloud storage
    and a documented selection rule.

unit_of_observation: One ImageCollection image per successfully mapped flood event, with 250 m MODIS-derived raster pixels and event-level DFO metadata.
structure: event-level geospatial raster collection
geo_granularity:
- 250 m raster pixels
- flood event
geography: Global, with country-filterable event metadata; China is included where GFD successfully mapped the event.
time_span:
  start: '2000-02-17'
  end: '2018-12-10'
  last_confirmed_release: Global Flood Database v1 (2000-2018), Earth Engine catalog and producer repository checked 2026-09-28
  coverage_note: >-
    The Earth Engine catalog describes 913 successfully mapped events. The
    Chang-Zheng paper identifies 39 GFD-mapped China events among 137 DFO
    events in its 2000-2009 study window; that paper-specific count must not
    be generalized to all China floods or all years.
  last_checked: '2026-09-28'
frequency:
- event
sample_size: 913 successfully mapped flood events globally
key_variables:
- flooded (maximum flood extent, binary)
- duration (inundation duration in days)
- jrc_perm_water (permanent-water reference layer)
- clear_views and clear_perc (event observation quality)
- DFO event ID, dates, country, centroid and event metadata

research_fit:
  best_for:
  - Measuring observed inundation extent for documented flood events in China or elsewhere, when an event-level satellite raster is the needed input.
  - Constructing a transparent spatial exposure measure after documenting the boundary, event filter, raster treatment and any buffer rule.
  choose_over:
  - Choose GFD v1 over a broad DFO affected-area polygon when the question requires mapped inundation rather than approximate affected area.
  - Choose this direct public input over the Chang-Zheng firm panel when the researcher has a different outcome layer or cannot obtain restricted ASIF.
  not_good_for:
  - A census of all floods, flood risk before an event, raw satellite imagery, or individual firm outcomes.
  - Claiming that a particular China flood was observed when it is absent from the selected GFD event collection.
  - Reproducing the Chang-Zheng firm panel without separately obtaining ASIF, geocoding firms, and following the paper's spatial construction.
  needs_join_for:
  - Firm, household, agricultural, population or administrative outcomes, joined through a separately documented spatial unit or coordinate procedure.
  - A China boundary or study-area geometry when producing a China-only event or pixel extract.
  variation_available:
  - Observed flood-event maps differ by event, pixel and event date; these are measurement dimensions, not a causal assignment rule.
  topics:
  - flood inundation
  - satellite observation
  - spatial exposure

good_for:
- event-level inundation mapping
- spatial disaster exposure construction
- China flood-event screening
identification:
- This data record provides observed spatial exposure, not a treatment-assignment or causal design.
linkable_keys:
- GFD image/event ID
- DFO original flood ID
- event date range
- raster coordinates
- country metadata

joins: []

access_routes:
- route: producer-documented public GCS GeoTIFF bucket
  access_status: available
  direct_url: https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase
  requirements: Install Google Cloud Storage tooling (`gsutil`) and have sufficient storage for the selected GeoTIFF download.
  steps:
  - Read the producer repository's Flood Maps section and decide whether the full raster archive is necessary.
  - Use the documented `gsutil -m cp -r gs://gfd_v1_4 <local-directory>` command, or restrict the copy only after inspecting the bucket layout and preserving the exact selected paths.
  - Retain source paths, retrieval date, GFD/DFO event IDs, and any raster-to-polygon transformation with the derived analysis.
  deliverable: GFD v1 event GeoTIFF flood maps plus the producer's accompanying code and supporting data repository.
  cost: mixed
  last_checked: '2026-09-28'
  caveat: >-
    The producer documents a whole-database copy command, not a promise that
    a particular derived China subset or paper-specific GIS output already
    exists as a separate file.
- route: Google Earth Engine collection
  access_status: available-with-registration
  direct_url: https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1
  requirements: Register for Google Earth Engine access; research, education and nonprofit use is described by Google as free.
  steps:
  - Register for Earth Engine and open `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`.
  - Filter by date, country metadata or DFO original ID; inspect the chosen event images and their flooded, duration, permanent-water and observation-quality bands.
  - Export only the documented spatial/time subset and preserve the collection ID, filters and export parameters.
  deliverable: Selected GFD v1 event images or derived spatial files under the collection's terms.
  cost: free
  last_checked: '2026-09-28'
  caveat: Earth Engine access and exports are a separate delivery route from the repository's GeoTIFF archive; record which route and exact filters produced an analysis file.

access:
  url: https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1
  cost: mixed
  license: CC BY-NC 4.0
  format:
  - GeoTIFF (producer GCS archive)
  - Google Earth Engine ImageCollection
  api: false
  how_to_get: Use the producer's documented public GCS bucket for the archive or register for Earth Engine and query `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`; preserve event selection and export parameters.
caveats: >-
  GFD v1 maps successfully observed flood extent, not all flooding. Its 913
  events are selected from the DFO catalog and classified with MODIS imagery;
  permanent water and cloud/clear-view layers must be considered before using
  the flooded band. The data licence is non-commercial. This asset does not
  include ASIF, firm coordinates, a 1 km buffer, or a paper's matched panel.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Chang & Zheng (2026), Using satellite-observed geospatial inundation data to identify the impacts of floods on firm-level performance: The case of China during 2000-2009'
  doi: https://doi.org/10.1016/j.jeem.2025.103276
  journal: JEEM
  year: 2026
  dataset_role: >-
    Public inundation input: the paper obtains GFD event rasters, converts
    them to polygons, applies a documented 1 km buffer, and joins them to a
    separate restricted ASIF firm panel.
  evidence_type: data-section
  evidence_url: https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/2023-09/Zheng%20Fan_JMP.pdf
  data_note: >-
    The accessible working-paper Section 2.1 identifies GFD, its 250 m
    GeoTIFF layers and the China 2000-2009 event screen. It establishes
    actual paper use of GFD, but the derived firm-exposure panel and code
    were not released.

provenance:
- source: https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase
  field_scope:
  - producer repository identity
  - public GCS bucket and GeoTIFF-copy command
  - code and supporting-data availability
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://developers.google.com/earth-engine/datasets/catalog/GLOBAL_FLOOD_DB_MODIS_EVENTS_V1
  field_scope:
  - collection ID, producer, 2000-2018 span and 913-event count
  - band meanings, event filters, Earth Engine access and CC BY-NC 4.0 terms
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/2023-09/Zheng%20Fan_JMP.pdf
  field_scope:
  - China-related GFD use and paper-specific construction boundary
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: china-flood-inundation-firm-exposure
  relation: predecessor
---

## Positioning in one sentence

GFD v1 is a directly obtainable collection of 913 satellite-observed flood
event maps from 2000-2018, suitable as a documented spatial input for China
research, but it is not a complete flood census and it does not contain the
restricted firm outcomes or paper-specific matching work needed for a
firm-exposure panel.

## Select rules

- Choose this asset when the question needs actual observed inundation extent
  and the study can define a defensible event, area and raster-processing rule.
- Use the raw GFD event ID and filters to make the China selection auditable;
  do not label all DFO-reported China events as GFD-mapped.
- Choose the separate `china-flood-inundation-firm-exposure` record only when
  ASIF access, firm geocoding and its paper-specific reconstruction burden
  are all in scope.

## Get recipe

1. Start from the producer repository's documented GCS route or the official
   Earth Engine collection; choose one route and keep its collection/bucket
   identity in the project record.
2. Define country, date or DFO-ID filters before exporting; inspect the flood,
   duration, permanent-water and clear-observation layers for each event.
3. If converting pixels into an exposure measure, record the chosen boundary,
   masking, raster-to-polygon method and any buffer. Those are new analysis
   choices, not defaults supplied by GFD.

## Connections and Limitations

- Join outcomes through a documented shared geography or coordinates. GFD has
  no firm identifier, household identifier or administrative outcome values.
- Missing or poorly observed flood events are a coverage limitation, not zero
  exposure. A derived panel should preserve event coverage diagnostics.
- The non-commercial CC BY-NC 4.0 licence and Earth Engine/GCS route terms
  govern use; the MIT licence in the code repository applies to code, not a
  replacement licence for the data product.
