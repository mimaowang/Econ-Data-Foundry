---
schema_version: 3
catalog_status: grounding
id: china-flood-inundation-firm-exposure
name: China firm-level flood inundation exposure panel 2000-2009 (GFD satellite inundation x ASIF)
aka:
- Global Flood Database (GFD)
- 卫星洪水淹没数据
- Chang-Zheng flood firm exposure
provider: >-
  Two-layer construction by Pao-Li Chang (Singapore Management University)
  and Fan Zheng (Dongbei University of Finance and Economics): flood
  inundation layer from the Global Flood Database (GFD), developed by
  Tellman et al. (2021, Nature), hosted at global-flood-database.cloudtostreet.ai
  (Cloud to Street); firm layer from the NBS Annual Surveys of Industrial
  Firms (ASIF). The matched panel itself is paper-constructed and not
  released.
china_related: true
domains:
- environment
- firm
- disaster
- regional
- spatial

data_pathway:
  mode: constructed
  origin: researcher-constructed
  target_artifact: >-
    A firm-year panel (2000-2009, China) identifying for each flood event
    which firms are inundated (GFD inundation polygons enlarged by 1 km)
    and the distances of all non-inundated firms from inundation areas;
    joined to ASIF firm performance (output, capital, labor, productivity).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Grounding pass (2026-08-15): the working-paper full text (Zheng Fan JMP,
    2022-10-30, SMU site, read in full) documents the construction
    first-hand: flood inundation from the GFD (Tellman et al. 2021) - raster
    GeoTIFF, WGS84, 250 m pixels, per-pixel flooded/days-inundated/cloud-free
    days/clear-observation share - built from the DFO flood-event catalog
    plus filtered satellite imagery with water-detection algorithms; of 137
    DFO events in China 2000-2009, GFD mapped 39; DFO affected areas are ~20x
    larger than GFD inundation (8,844,619 vs 442,026 km2) and would imply 47x
    more inundated firm-years (516,908 vs 10,658); the paper enlarges GFD
    inundation by a 1 km buffer, yielding 81,861 inundated firm-year
    observations. Firm layer: ASIF (NBS, all above-scale industrial firms,
    sales > 5M RMB, 2000-2009). The published JEEM article (2026,
    DOI 10.1016/j.jeem.2025.103276) is closed access; its abstract (RePEc)
    confirms the same construction plus I-O linkage propagation analysis.
  barrier: >-
    The matched firm-level panel and code are not released (no DAS found in
    the JMP; Elsevier article closed). GFD v1's public GeoTIFF and Earth
    Engine routes are now independently verified, but the exact China event
    selection and the paper's raster-to-firm construction still have to be
    recreated. ASIF remains the restricted acquisition gate (see asif record).

unit_of_observation: >-
  Firm-year observations with flood exposure: inundated (within GFD
  inundation + 1 km) or distance band to inundation area (analysis);
  flood-event polygons (GFD rasters)
structure: firm-year panel (constructed) + flood-event inundation rasters/polygons
geo_granularity:
- firm (geocoded location)
- flood-event polygon (250 m raster cells)
- km distance bands
geography: China nationwide (firms), 2000-2009; 39 GFD-mapped flood events in China of 137 DFO-catalogued
time_span:
  start: '2000'
  end: '2009'
  last_confirmed_release: 'Paper window 2000-2009; GFD itself covers a longer global span (per-paper, Landsat permanent-water baseline 1985-2016)'
  coverage_note: >-
    The paper restricts to 2000-2009 (ASIF years and China flood events);
    GFD's global coverage years are not verified this round (Nature 2021
    paper unread).
  last_checked: '2026-08-15'
frequency:
- event (flood)
- annual (firm panel)
sample_size: >-
  China 2000-2009: 137 DFO flood events, 39 mapped by GFD; 10,658 inundated
  firm-year observations (GFD only) rising to 81,861 with the 1 km buffer
  (paper Section 2.1)
key_variables:
- Inundation status (flooded or not, per 250 m pixel)
- Days inundated; cloud-free days; proportion of clear observations (GFD raster layers)
- Firm geocoded location and distance to inundation area
- Firm performance: output, capital, labor inputs, productivity (ASIF)
- Flood event area (GIS-computed)

research_fit:
  best_for:
  - Firm-level flood exposure measurement with high-resolution satellite inundation (250 m) rather than coarse DFO polygons
  - Spatial spillover analysis of floods (distance bands) on industrial firms
  choose_over:
  - Choose GFD-based exposure over DFO polygons alone: the paper documents DFO affected areas overstate inundation ~20x and would inflate inundated firm-years ~47x.
  - Choose GFD over GFMS/DART-type products when the research needs per-event inundation rasters with the documented construction in this paper.
  - For city-level disaster analysis with night lights, other products may fit better; this asset is firm-level.
  not_good_for:
  - Claiming the matched Chang-Zheng panel is downloadable (not released)
  - Firm-level analysis outside 2000-2009 with this exact construction (ASIF window)
  - Measuring flood risk ex ante (GFD maps observed events, not hazard probability)
  needs_join_for:
  - Firm outcomes beyond ASIF variables (external joins by firm identifier)
  - County/city controls and I-O tables (paper's aggregate and linkage analyses)
  variation_available:
  - Firm-level flood exposure variation across events, years, and distance bands
topics:
- floods
- firm performance
- satellite inundation
- spatial spillovers
- disaster economics

good_for:
- Firm-level flood exposure panels for Chinese industrial firms
- Spillover-distance analysis around inundation areas
- Understanding the GFD-DFO measurement gap (overstatement)
identification: []
linkable_keys:
- Firm identifier (ASIF)
- Flood event (DFO event id)
- Firm coordinates (geocoded)
- Distance to inundation polygon

joins:
- target: asif
  relation: complement
  keys:
  - Firm identifier
  - Year
  method: ASIF is the firm layer of this panel; use the canonical asif record for acquisition routes and restrictions
  evidence_status: literature-used
- target: china-county-population-agriculture-gis-1990
  relation: complement
  keys:
  - County
  method: Historical county boundaries for flood-prone-county heterogeneity analyses (paper-level use unverified)
  evidence_status: plausible

access_routes:
- route: gfd-v1-public-raster-input
  access_status: available
  direct_url: https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase
  requirements: >-
    GFD v1 is available through the producer-documented public GCS archive
    (`gs://gfd_v1_4`) or, after registration, Earth Engine collection
    `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`; retain selected event IDs and export
    parameters.
  steps:
  - Select GFD v1 events by country/date/DFO ID using the documented GCS or Earth Engine route (China 2000-2009: 39 paper-screened events).
  - Download or export relevant event images and inspect flooded, duration, permanent-water and observation-quality layers.
  - Convert rasters to polygons with GIS software; apply the 1 km buffer as in the paper.
  deliverable: Per-event inundation GeoTIFFs (flooded/days/cloud-free/clear-obs layers)
  cost: free
  last_checked: '2026-08-15'
  caveat: >-
    This direct input route does not supply the paper's ASIF match, firm
    geocoding, 1 km buffer or final panel. See the separate GFD v1 record for
    archive/collection mechanics and terms.
- route: asif-restricted
  access_status: available-with-restrictions
  direct_url: https://microdata.stats.gov.cn/
  requirements: See the canonical asif record - NBS Micro Data Lab application or commercial library versions; confidentiality agreement
  steps:
  - Obtain ASIF 2000-2009 through the documented asif routes.
  - Geocode firm addresses; match to inundation polygons; build the panel per the paper's rules.
  deliverable: ASIF firm-year panel with geocoded locations
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Restricted data; the paper's exact geocoding method (address fields, geocoder) is not fully documented in the JMP.
- route: paper-panel
  access_status: unavailable
  direct_url: needs-verification
  requirements: Not released; no DAS or replication package found (JMP has none; Elsevier closed)
  steps:
  - No public route evidenced; the matched panel must be rebuilt from the public inputs (routes above).
  - Contact the authors (Pao-Li Chang, SMU; Fan Zheng, DUFE) only if a data-sharing agreement is being negotiated.
  deliverable: None - the matched panel must be rebuilt
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Author contact possible (Pao-Li Chang, SMU; Fan Zheng, DUFE) but no release is evidenced.

access:
  url: https://global-flood-database.cloudtostreet.ai/
  cost: free
  license: >-
    GFD data license/terms not read this round (JS portal); the Nature 2021
    paper is the data descriptor; ASIF restrictions per asif record
  format:
  - GeoTIFF
  - shapefile (derived)
  api: false
  how_to_get: >-
    Download GFD event rasters from the portal, convert to polygons, apply
    the 1 km buffer, geocode ASIF firms (asif routes), and match per the
    paper's Section 2 rules.
caveats:
- The matched panel is not released; reproducibility requires both the GFD rasters and restricted ASIF data.
- GFD v1 is public under CC BY-NC 4.0, but the paper's China selection and spatial construction must still be recreated.
- GFD maps only 39 of 137 DFO China events 2000-2009 (cloud cover, flash floods, small events); event coverage is incomplete.
- The paper's geocoding method for firms is not fully documented in the JMP.
- DFO polygons (if used instead) overstate inundation ~20x - do not substitute casually.

production:
  raw_sources:
  - name: Global Flood Database (GFD) event rasters
    source_type: dataset
    role: Inundation extent per flood event (250 m GeoTIFF)
    access_route: Producer GCS archive (`gs://gfd_v1_4`) or Earth Engine collection `GLOBAL_FLOOD_DB/MODIS_EVENTS/V1`
    url: https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase
    coverage: 'China 2000-2009: 39 mapped events (of 137 DFO); global events per Nature 2021 (unread this round)'
    last_checked: '2026-08-15'
  - name: DFO flood event catalog
    source_type: dataset
    role: Event dates and approximate locations (basis for GFD mapping)
    access_route: https://floodobservatory.colorado.edu/ (official page fetched 2026-08-15; catalog details unread)
    url: https://floodobservatory.colorado.edu/
    coverage: 137 China events 2000-2009 (paper)
    last_checked: '2026-08-15'
  - name: ASIF (NBS Annual Surveys of Industrial Firms)
    source_type: dataset
    role: Firm locations and performance 2000-2009
    access_route: Restricted - see asif canonical record
    url: https://microdata.stats.gov.cn/
    coverage: Above-scale industrial firms (sales > 5M RMB), 2000-2009
    last_checked: '2026-08-15'
  acquisition_methods:
  - direct download
  - GIS processing
  - restricted application
  sample_construction: >-
    Per JMP Section 2 (read in full): all GFD-mapped China flood events
    2000-2009; firms from ASIF geocoded; firm-year inundated if located in
    GFD inundation polygon enlarged by 1 km; non-inundated firms assigned
    distance to inundation areas.
  pipeline_stages:
  - stage: collect
    inputs:
    - GFD event rasters (China 2000-2009)
    method: Download per-event GeoTIFFs (250 m, WGS84); use the flooded/not-flooded layer
    tools:
    - GIS software
    output: Event inundation rasters
    evidence: JMP Section 2.1
  - stage: geocode
    inputs:
    - ASIF 2000-2009
    method: Geocode firm location data (exact geocoder not fully documented in JMP)
    tools: []
    output: Geocoded firm-year observations
    evidence: JMP Section 2.2 (firm layer description; geocoding method partially documented)
  - stage: match
    inputs:
    - Inundation polygons
    - Geocoded firms
    method: Transform rasters to polygon shapefiles; match firms; compute distances for non-inundated firms; apply 1 km buffer (10,658 -> 81,861 inundated firm-years)
    tools:
    - GIS software
    output: Firm-year flood exposure panel
    evidence: JMP Section 2.1 (buffer results), Section 2.2
  constructed_variables:
  - name: Inundated firm-year indicator
    concept: Firm located within GFD inundation area + 1 km buffer during a flood event year
    source_fields:
    - GFD flooded layer
    - Firm coordinates
    method: Spatial match; 1 km buffer enlargement
    validation: Comparison vs DFO-based matching (47x overstatement documented)
    limitations: Fragmented/small GFD inundation areas may under-map events (cloud cover, flash floods)
  - name: Distance to inundation
    concept: Distance of non-inundated firms to inundation polygons (spillover rings)
    source_fields:
    - Inundation polygons
    - Firm coordinates
    method: GIS distance computation; concentric rings (e.g., within 4 km; 6-18 km)
    validation: Ring analysis in paper
    limitations: None documented beyond measurement error in geocoding
  validation:
  - Paper compares GFD vs DFO mapping (extent 20x difference; firm obs 47x).
  - Robustness checks and extended analyses in the paper (moderators, aggregate effects, I-O propagation).
  output:
    unit_of_observation: Firm-year
    structure: Panel with inundation status and distances
    geography: China (firm locations), 2000-2009
    time_span: 2000-2009
    key_variables:
    - Inundation indicator
    - Distance bands
    - Output, capital, labor, productivity (ASIF)
    formats:
    - not released
  reproducibility:
    level: low
    starting_point: https://global-flood-database.cloudtostreet.ai/ + asif routes
    code_available: false
    code_url:
    requirements:
    - GFD rasters (public)
    - ASIF 2000-2009 (restricted)
    - GIS skills (raster-to-polygon, buffering, distance)
    - Firm geocoding (method partially documented)
    blockers:
    - GFD v1 is public, but exact China event selection and paper-specific GIS processing require reconstruction
    - ASIF restricted acquisition
    - Paper panel/code not released; exact geocoder and firm universe cleaning unverified
  compliance:
    terms_or_license: GFD v1 is CC BY-NC 4.0; ASIF confidentiality agreement required (asif record)
    robots_or_rate_limits: Portal is JS-based; automated download limits unknown
    personal_or_sensitive_data: Firm-level data (ASIF) restricted; GFD is open geospatial data
    redistribution: Do not redistribute matched firm-level panel; ASIF terms apply
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Chang & Zheng (2026), Using satellite-observed geospatial inundation data to identify the impacts of floods on firm-level performance: The case of China during 2000-2009'
  doi: https://doi.org/10.1016/j.jeem.2025.103276
  journal: JEEM
  year: 2026
  dataset_role: >-
    Main treatment/exposure: firm-level inundation status and distances from
    GFD inundation polygons; outcomes from ASIF (output, capital, labor,
    productivity)
  evidence_type: data-section
  evidence_url: https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/2023-09/Zheng%20Fan_JMP.pdf
  data_note: >-
    Working-paper full text (JMP 2022-10-30, 40 pp) read in full 2026-08-15:
    Section 2.1 documents GFD (Tellman et al. 2021) construction, 250 m
    GeoTIFFs, DFO event basis, China 39/137 events 2000-2009, DFO-vs-GFD
    overstatement (20x area, 47x firm-years), 1 km buffer (10,658 -> 81,861
    inundated firm-years); Section 2.2 identifies ASIF (NBS, above-scale,
    sales > 5M RMB) 2000-2009. Published version (JEEM 137, 2026, closed
    access): RePEc abstract confirms the same construction and adds I-O
    linkage propagation analysis. Findings: ~6% output / ~5% productivity
    annual losses for inundated firms, persistent; 4 km-ring negative ~2%;
    6-18 km expansion.

provenance:
- source: https://economics.smu.edu.sg/sites/economics.smu.edu.sg/files/2023-09/Zheng%20Fan_JMP.pdf (read in full 2026-08-15)
  field_scope:
  - GFD data construction, resolution, fields, China event coverage
  - DFO-vs-GFD comparison numbers
  - ASIF firm layer identity and window
  - buffer/distance construction and results
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://econpapers.repec.org/article/eeejeeman/v_3a137_3ay_3a2026_3ai_3ac_3as0095069625001603.htm (read 2026-08-15)
  field_scope:
  - published version identity, abstract (GFD-filtered satellite imagery), keywords, JEL
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://global-flood-database.cloudtostreet.ai/ (fetched 2026-08-15)
  field_scope:
  - GFD official host exists (JS app; matches JMP footnote 4 URL)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://floodobservatory.colorado.edu/ (fetched 2026-08-15)
  field_scope:
  - DFO official site (Flood Observatory) reachable; catalog details unread
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.openalex.org/works/W3190581971 (read 2026-08-15)
  field_scope:
  - GFD descriptor paper identity: Tellman et al. 2021, Nature, DOI 10.1038/s41586-021-03695-w
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: asif
  relation: complement
- id: china-satellite-pm25
  relation: often-confused-with
- id: global-flood-database-v1-modis-events-2000-2018
  relation: predecessor
---

## Positioning in one sentence

The Chang-Zheng (JEEM 2026) firm-level flood exposure panel combines public Global Flood Database (GFD) inundation rasters (250 m, Tellman et al. 2021) with restricted ASIF firm data (2000-2009) via raster-to-polygon matching, a 1 km buffer and distance rings - the construction is fully documented in the working paper, but the matched panel and code are not released, so the route is rebuilding from GFD + ASIF.

## Select rules

- Use this record for firm-level flood exposure research: GFD-based exposure beats DFO polygons (documented ~20x overstatement).
- Rebuild the panel via the GFD portal + asif routes; do not promise the paper's panel as a download.
- For city-level or night-lights flood studies, other products fit better; this asset is firm-level.

## Get recipe

1. Obtain GFD v1 event rasters through its documented GCS archive or Earth Engine collection; filter the paper's China 2000-2009 event set and preserve IDs/exports.
2. Convert rasters to polygons; apply the 1 km buffer per the paper.
3. Obtain ASIF 2000-2009 via the asif routes; geocode firms; match and compute distances.

## Connections and Limitations

The panel joins GFD (public) with ASIF (restricted); both acquisition gates must clear. GFD coverage is incomplete for small/cloudy events (39/137 DFO events); DFO alternatives overstate inundation. The paper's exact firm-geocoding method and cleaning are not fully documented; the matched panel is not released. The GFD v1 input is independently documented as public under CC BY-NC 4.0, but that does not remove ASIF or reconstruction barriers.
