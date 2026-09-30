---
schema_version: 3
catalog_status: ready
id: china-harmonized-nighttime-lights-li-et-al
name: Li et al. harmonized DMSP–VIIRS nighttime-light grid, including China (1992–2024)
aka:
- Harmonized NTL
- Harmonized_DN_NTL
- Li–Zhou harmonized nighttime lights
- DMSP-VIIRS harmonized nighttime lights
- 协调夜间灯光数据
provider: Xuecao Li, Yuyu Zhou, Min Zhao and Xia Zhao; public versioned archive on figshare
china_related: true
domains:
- urban
- regional
- spatial
- development
- environment

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: >-
    A versioned public set of annual global 30-arc-second GeoTIFF nighttime-light
    grids: calibrated DMSP-like DN files for 1992–2013 and simulated DMSP-like
    files derived from VIIRS for 2014–2024. China is obtained by spatially
    clipping or aggregating the global grids; it is not a separate China-only file.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    figshare article 9828827 version 10 is public, has downloading enabled, and
    exposes 34 GeoTIFF files under CC BY 4.0. It provides one harmonized annual
    file for each year 1992–2024 plus a companion 2013 simulated-VIIRS file.
    This is a concrete direct-download route for a China long-run light series,
    distinct from EOG raw composites and the China-only PANDA product.
  barrier: >-
    The files are global rasters (about 1.09 GB total), so China use requires
    spatial clipping or zonal aggregation and an explicit boundary vintage. The
    DN measure remains a proxy for human activity, not direct economic output.

unit_of_observation: 30-arc-second raster cell (about 1 km at the equator) x annual observation
structure: Annual global gridded time series, 1992–2024
geo_granularity:
- grid
- county/city/province after researcher aggregation
geography: Global terrestrial coverage including mainland China
time_span:
  start: '1992'
  end: '2024'
  last_confirmed_release: figshare article 9828827 version 10, modified 2025-08-10
  coverage_note: >-
    Version 10 lists calibrated DMSP files for 1992–2013 and simulated-VIIRS
    files for 2014–2024. The manifest also has DN_NTL_2013_simVIIRS.tif as a
    companion file; do not silently substitute it for the named 2013 calibrated
    DMSP series without making that choice explicit.
  last_checked: '2026-09-28'
frequency:
- annual
sample_size: >-
  34 public GeoTIFF files in figshare version 10 (33 named annual
  Harmonized_DN_NTL files for 1992–2024 plus one companion 2013 simulated-VIIRS
  GeoTIFF); China row/pixel count depends on the chosen boundary and clipping rule.
key_variables:
- Harmonized nighttime-light digital number (DN)
- Raster-cell latitude/longitude position
- Annual file vintage and source-family label (calDMSP or simVIIRS)

research_fit:
  best_for:
  - Long-run China city, county, or grid studies needing one annual nighttime-light measure across the DMSP–VIIRS transition
  - Constructing boundary-consistent annual zonal light measures as a proxy for urban activity or built-up intensity
  choose_over:
  - Choose this over raw EOG DMSP/VIIRS products when a published, single harmonized annual DN series from 1992 through 2024 is more important than monthly frequency or raw-sensor control.
  - Choose the China-only PANDA product when its earlier 1984 start and China-specific construction are required; verify its separate TPDC access route and method rather than treating it as this dataset.
  not_good_for:
  - Monthly or daily light analysis, because this product is annual.
  - Treating DN as radiance, physical electricity use, GDP, or population without validation.
  - Reproducing an article that merely says it used nighttime lights; the exact paper product and aggregation must be verified separately.
  needs_join_for:
  - Administrative boundaries of the relevant historical vintage to aggregate grid values to counties, cities, or provinces.
  - Survey, firm, census, or yearbook outcomes after matching the same geography and year.
  variation_available:
  - Annual grid-cell and researcher-aggregated spatial variation in harmonized nighttime-light intensity.
  topics:
  - nighttime lights
  - urbanization
  - regional development
  - remote sensing
  - DMSP
  - VIIRS

good_for:
- China long-run annual nighttime-light panels after explicit spatial aggregation
- Urban expansion and regional-development proxy measures
identification:
- The raster series is a descriptive outcome or proxy, not a causal design; any causal interpretation requires independently supported treatment, comparison, and measurement choices.
linkable_keys:
- Raster-cell longitude/latitude
- Year
- Researcher-created administrative-unit identifier after zonal aggregation

joins:
- target: china-census
  relation: complement
  keys:
  - boundary geometry or documented administrative concordance
  - census year
  method: Aggregate the raster to the census geography using a documented boundary vintage; do not equate a later county polygon with the historical census unit by name alone.
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - city/province geometry or documented name-code concordance
  - year
  method: Create the light aggregate first, then join it to the matching administrative-year outcome; preserve any boundary mismatch.
  evidence_status: plausible

access_routes:
- route: figshare version-10 direct download
  access_status: available
  direct_url: https://doi.org/10.6084/m9.figshare.9828827.v10
  requirements: No account; cite the dataset and comply with CC BY 4.0 attribution.
  steps:
  - Open figshare article 9828827 version 10 or its public API record.
  - Select the needed Harmonized_DN_NTL_YYYY_calDMSP.tif (1992–2013) or Harmonized_DN_NTL_YYYY_simVIIRS.tif (2014–2024) file.
  - Download the GeoTIFF, retain the version/date and filename, and clip or aggregate it using the chosen China boundary.
  deliverable: Public GeoTIFF files totaling about 1.09 GB, with direct file download URLs in the figshare manifest.
  cost: free
  last_checked: '2026-09-28'
  caveat: The separate DN_NTL_2013_simVIIRS.tif companion file is not the named annual harmonized 2013 calDMSP file; choose and document the 2013 convention deliberately.

access:
  url: https://doi.org/10.6084/m9.figshare.9828827.v10
  cost: free
  license: CC BY 4.0
  format:
  - GeoTIFF
  api: true
  how_to_get: Download the required annual GeoTIFFs from the public figshare version-10 manifest, then clip or zonally aggregate to the intended China geography while retaining the version and filenames.
caveats:
- This is a global raster product; China is a derived spatial subset, not a provider-published China panel.
- The product’s harmonization does not eliminate the need to state whether the analysis uses sums, means, thresholds, log transformations, or area/population weighting.
- The source manifest recommends pixels with DN greater than 7; that is a provider suggestion, not a universal analytic rule.
- The broader china-nighttime-lights record retains separate EOG and PANDA routes; they must not be treated as interchangeable files.

production:
  raw_sources:
  - name: Calibrated DMSP-OLS nighttime-light series
    source_type: imagery
    role: Input for the 1992–2013 calDMSP portion of the released harmonized series
    access_route: Incorporated in the released figshare product; raw EOG route is documented separately in china-nighttime-lights
    url: https://doi.org/10.6084/m9.figshare.9828827.v10
    coverage: 1992–2013 annual output files
    last_checked: '2026-09-28'
  - name: VIIRS nighttime-light series
    source_type: imagery
    role: Input for the released 2014–2024 simulated DMSP-like portion
    access_route: Incorporated in the released figshare product; raw EOG route is documented separately in china-nighttime-lights
    url: https://doi.org/10.6084/m9.figshare.9828827.v10
    coverage: 2014–2024 annual output files
    last_checked: '2026-09-28'
  acquisition_methods:
  - download
  sample_construction: The provider releases complete global annual raster files; China selection, clipping, and aggregation are downstream researcher choices.
  pipeline_stages:
  - stage: model
    inputs:
    - DMSP-OLS nighttime-light observations
    - VIIRS nighttime-light observations
    method: The released product labels 1992–2013 outputs calDMSP and 2014–2024 outputs simVIIRS; detailed model implementation should be taken from the cited product publication rather than inferred from filenames.
    tools: []
    parameters: {}
    output: Annual harmonized DN GeoTIFFs
    evidence: figshare version-10 manifest and its linked publication reference
  - stage: aggregate
    inputs:
    - Downloaded annual GeoTIFF
    - Researcher-selected China boundary geometry
    method: Clip and compute a documented zonal summary for the intended administrative or study area.
    tools:
    - GIS or raster-analysis software
    parameters: {}
    output: Researcher-created China grid subset or administrative-year panel
    evidence: downstream researcher work; not supplied as a precomputed China table
  constructed_variables: []
  validation:
  - Confirm filename, figshare version, and source-family label before combining years.
  - Retain the chosen boundary vintage and aggregation statistic with every China-derived panel.
  output:
    unit_of_observation: Annual 30-arc-second grid cell; China administrative-year outputs are researcher aggregates
    structure: Annual gridded time series
    geography: Global including China
    time_span: 1992–2024
    key_variables:
    - Harmonized DN nighttime-light intensity
    formats:
    - GeoTIFF
  reproducibility:
    level: high
    starting_point: https://api.figshare.com/v2/articles/9828827
    code_available: false
    code_url: null
    requirements:
    - Approximately 1.09 GB download/storage for the full version-10 archive
    - GIS or raster tooling and an explicit China boundary for derived local panels
    blockers:
    - The provider releases global rasters rather than a pre-aggregated China administrative panel; a researcher must document the boundary vintage and zonal statistic for any China-derived table.
  compliance:
    terms_or_license: CC BY 4.0 as stated in the figshare version-10 record
    robots_or_rate_limits: Use ordinary figshare downloads; no bulk scraping beyond the supplied file manifest is needed
    personal_or_sensitive_data: None
    redistribution: Attribution required under CC BY 4.0; retain the dataset version and citation
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://api.figshare.com/v2/articles/9828827
  field_scope:
  - public status, download-enabled status, version, license, total archive size, and manifest count
  - 34 named GeoTIFF files and direct file-download URLs
  - calDMSP 1992–2013 and simVIIRS 2014–2024 filename coverage
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://doi.org/10.6084/m9.figshare.9828827.v10
  field_scope:
  - versioned dataset citation and CC BY 4.0 route
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-nighttime-lights
  relation: parent-family
- id: china-satellite-pm25
  relation: complement
---

## Positioning in one sentence

This is the directly downloadable, versioned harmonized nighttime-light product for China use: a global annual 30-arc-second DN raster series covering 1992–2024 under CC BY 4.0. It is the clearest choice when a study needs one published annual light series across the DMSP–VIIRS transition, but China panels must still be built with an explicit boundary and aggregation rule.

## Select rules

- Choose it for annual China long-run light panels when consistent cross-sensor coverage matters more than raw-sensor detail or monthly frequency.
- Choose the EOG products for raw DMSP/VIIRS files or monthly VIIRS analysis; choose PANDA for its separate China-specific 1984–2020 product.
- Do not claim that an article used this product merely because it says “nighttime lights”; verify the article’s product, vintage, and aggregation separately.

## Get recipe

1. Open the public figshare version-10 record and select the required annual GeoTIFFs.
2. Keep the filename and version with the analysis materials; use calDMSP for 1992–2013 and simVIIRS for 2014–2024 unless a different, documented 2013 convention is justified.
3. Clip or zonally aggregate the global grid to an explicit China boundary, then join only to outcomes at the compatible geography and year.

## Connections and Limitations

The file’s natural keys are grid location and year. A city, county, or province value does not exist until the researcher aggregates pixels using a particular boundary vintage and statistic. DN is a harmonized remote-sensing proxy, not a direct measure of output or population, and the transition treatment cannot replace a documented measurement decision.
