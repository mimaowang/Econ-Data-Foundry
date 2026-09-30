---
schema_version: 3
catalog_status: grounding
id: china-merra2-pm25-chen-oliva-zhang
name: Chen, Oliva and Zhang China county PM2.5 exposure constructed from MERRA-2 aerosol diagnostics
aka:
- M2TMNXAER 5.12.4
- MERRA-2 AOD-derived China PM2.5
- Chen Oliva Zhang 2022 PM2.5 exposure
provider: >-
  NASA Global Modeling and Assimilation Office produces the MERRA-2 input;
  NASA GES DISC distributes the named M2TMNXAER 5.12.4 collection. Chen,
  Oliva and Zhang construct the paper-specific China PM2.5 exposure measure
  from that input rather than downloading a provider-delivered PM2.5 file.
china_related: true
domains:
- environment
- air pollution
- migration
- health
- urban

data_pathway:
  mode: hybrid
  origin: researcher-constructed
  target_artifact: >-
    County x five-year PM2.5 exposure used by Chen, Oliva and Zhang (2022),
    constructed from NASA MERRA-2 monthly aerosol diagnostics M2TMNXAER
    version 5.12.4. The paper says it converts the AOD-related input to PM2.5
    following Buchard et al. (2016), aggregates monthly grid values to county,
    then annual and five-year averages; this is not TAP, a generic global
    annual PM2.5 grid, or a provider-distributed final county panel.
  availability: partially-reproducible
  ordinary_researcher_feasible: false
  summary: >-
    The raw NASA collection is a realistic current starting point after an
    Earthdata login, but the paper section does not by itself supply all
    algorithm parameters, geographic crosswalk choices, code, or a released
    final county panel needed to reproduce the exact exposure. It is useful
    for understanding the paper's data lineage and for a carefully documented
    new construction, not as a ready-made PM2.5 download.
  barrier: >-
    Current NASA conversion guidance is now documented below, but equivalence
    to the authors' Buchard et al. (2016) implementation, their county crosswalk
    and aggregation choices, and a public final panel remain unverified.
    The published article's data-availability statement says the data used are
    confidential; it does not identify which components that restriction covers.

unit_of_observation: >-
  Paper target: China county x five-year period. Raw input: global
  latitude-longitude grid x month at 0.5 by 0.625 degrees.
structure: constructed county-period panel from monthly gridded input
geo_granularity:
- raw global grid
- constructed China county
geography: >-
  The raw collection is global. The checked paper constructs a China county
  exposure measure; it does not make the resulting county crosswalk public.
time_span:
  start: '1996 (paper study window)'
  end: '2010 (paper study window)'
  last_confirmed_release: 'M2TMNXAER 5.12.4 is the named paper input; current NASA access page checked 2026-09-28'
  coverage_note: >-
    The paper states that the monthly MERRA-2 input is available since 1980
    and uses it for 1996-2010. This record does not assert a current final
    PM2.5 series or continuity beyond the paper's construction.
  last_checked: '2026-09-28'
frequency:
- raw monthly
- constructed annual and five-year averages in the paper
sample_size: unknown
key_variables:
- raw aerosol optical-depth-related diagnostics in M2TMNXAER 5.12.4
- paper-derived PM2.5 concentration
- county and five-year period in the final paper measure

research_fit:
  best_for:
  - Auditing the precise PM2.5 data lineage in Chen, Oliva and Zhang's China migration study
  - Building a new documented county-period exposure only after specifying the PM2.5 conversion and grid-to-county method
  choose_over:
  - Choose this record over TAP or a global annual PM2.5 grid only when reproducing or closely auditing this paper's MERRA-2-based construction.
  - Choose a provider-delivered grid with its own documentation when the research question needs a ready-made exposure surface rather than this unreleased construction.
  not_good_for:
  - Downloading the authors' final county PM2.5 panel
  - Treating MERRA-2 aerosol diagnostics as a ready-made PM2.5 product without the paper's conversion work
  - Claiming equivalence to TAP or a Van Donkelaar global annual grid
  needs_join_for:
  - China county boundary geometry and a stated grid-to-county aggregation method
  - A fully specified PM2.5 conversion implementation before an exact replication claim
  variation_available:
  - Raw grid-month observations and the paper's constructed county five-year PM2.5 values; these are data dimensions, not an identification design
  topics:
  - PM2.5
  - MERRA-2
  - aerosol optical depth
  - county exposure

good_for:
- paper-specific data-lineage audit
- documented construction planning
identification: []
linkable_keys:
- raw latitude and longitude grid
- raw month
- constructed county and period only after an explicit crosswalk

joins:
- target: china-census
  relation: complement
  keys:
  - county
  - five-year period
  method: The cited paper combines its constructed county exposure with census-derived migration outcomes; exact geographic concordance remains unreleased.
  evidence_status: literature-used

access_routes:
- route: nasa-earthdata-raw-input
  access_status: available-with-registration
  direct_url: https://disc.gsfc.nasa.gov/datasets/M2TMNXAER_5.12.4/summary
  requirements: Create and use a NASA Earthdata Login for GES DISC download or subsetting; retain the collection version and access date.
  steps:
  - Open the M2TMNXAER 5.12.4 collection page and read its documentation and file specification.
  - Register or sign in with Earthdata Login, then select the required monthly raw files or subset.
  - Separately document a PM2.5 conversion and grid-to-county procedure; do not label the raw download as the authors' final PM2.5 panel.
  deliverable: Raw MERRA-2 monthly aerosol-diagnostic files, not a China county PM2.5 panel.
  cost: registration
  last_checked: '2026-09-28'
  caveat: NASA access closes the raw-input route only. It does not release the authors' conversion parameters, crosswalk or final analysis file.

access:
  url: https://disc.gsfc.nasa.gov/datasets/M2TMNXAER_5.12.4/summary
  cost: registration
  license: Refer to current NASA Earthdata and collection-specific terms before reuse or redistribution.
  format:
  - NetCDF
  api: false
  how_to_get: Use the Earthdata route for raw MERRA-2 input, then treat PM2.5 conversion and county aggregation as a new documented construction unless a complete paper replication package is independently found.
caveats: >-
  The paper reports the formula family only as following Buchard et al. (2016).
  Its public paper text does not close exact parameters, code or county spatial
  treatment. The raw MERRA-2 collection and the paper's PM2.5 outcome are
  therefore distinct assets.

production:
  raw_sources:
  - name: MERRA-2 M2TMNXAER version 5.12.4 monthly aerosol diagnostics
    source_type: dataset
    role: Raw AOD-related input named in the paper
    access_route: NASA Earthdata Login through GES DISC
    url: https://disc.gsfc.nasa.gov/datasets/M2TMNXAER_5.12.4/summary
    coverage: Global latitude-longitude grid, monthly; paper states 0.5 by 0.625 degrees and uses 1996-2010
    last_checked: '2026-09-28'
  acquisition_methods:
  - download
  sample_construction: >-
    The paper aggregates monthly grid data to county, then annual and five-year
    averages. Boundary files, weighting, missing-data treatment and code are
    not established by the checked materials.
  pipeline_stages:
  - stage: model
    inputs:
    - M2TMNXAER 5.12.4 aerosol-diagnostic data
    method: >-
      The paper follows Buchard et al. (2016) without listing its exact fields
      or coefficients. For a new construction, consult the provider conversion
      recipe below and verify the selected monthly file's fields and units.
      Do not assume it reproduces the authors' implementation.
    tools: []
    parameters: needs-verification
    output: Grid-level PM2.5 estimate
    evidence: Chen, Oliva and Zhang (2022), data section
  - stage: aggregate
    inputs:
    - Grid-level PM2.5 estimate
    method: Aggregate monthly grid values to county, then annual and five-year averages.
    tools: []
    parameters: County crosswalk and aggregation weights need verification
    output: County x five-year PM2.5 exposure
    evidence: Chen, Oliva and Zhang (2022), data section
  constructed_variables:
  - name: county five-year PM2.5
    concept: Paper-specific medium-run county pollution exposure
    source_fields:
    - MERRA-2 aerosol diagnostics
    method: PM2.5 conversion followed by spatial and temporal aggregation; exact implementation unresolved
    validation: Paper compares the result with ground-based data for 2013-2015, but a future reconstruction must not assume identical validation output
    limitations: Unreleased exact code, parameters and county crosswalk
  validation: []
  output:
    unit_of_observation: China county x five-year period
    structure: panel
    geography: China counties as implemented by the authors; exact boundary vintage unverified
    time_span: 1996-2010 in the paper
    key_variables:
    - PM2.5 concentration
    formats: []
  reproducibility:
    level: low
    starting_point: NASA Earthdata M2TMNXAER 5.12.4 raw collection
    code_available: false
    code_url:
    requirements:
    - Earthdata Login
    - A fully specified PM2.5 conversion implementation
    - China county boundary and documented aggregation choices
    blockers:
    - Exact paper code and parameters not established
    - Final county exposure file not established as public
  compliance:
    terms_or_license: Check current NASA Earthdata and collection terms
    robots_or_rate_limits: Not assessed
    personal_or_sensitive_data: No personal data described
    redistribution: Do not infer permission for a derived county panel from raw-input availability
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Chen, Oliva & Zhang (2022), The Effect of Air Pollution on Migration: Evidence from China'
  doi: https://doi.org/10.1016/j.jdeveco.2022.102833
  journal: Journal of Development Economics
  year: 2022
  dataset_role: County-level five-year PM2.5 exposure in the migration analysis
  evidence_type: published-paper-full-text
  evidence_url: https://pengzhang.weebly.com/uploads/3/1/7/6/31762679/pollution-migration.pdf
  data_note: >-
    The data section names M2TMNXAER 5.12.4, states monthly 0.5 by 0.625
    degree grid values, PM2.5 calculation following Buchard et al. (2016),
    county aggregation, and annual then five-year averaging for 1996-2010.

provenance:
- source: https://pengzhang.weebly.com/uploads/3/1/7/6/31762679/pollution-migration.pdf (author-hosted published paper, data section read 2026-09-28)
  field_scope:
  - actual M2TMNXAER 5.12.4 paper use
  - paper construction sequence and study window
  - boundary between raw input and final county PM2.5 measure
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://disc.gsfc.nasa.gov/datasets/M2TMNXAER_5.12.4/summary (NASA GES DISC current collection page, checked 2026-09-28)
  field_scope:
  - current raw-input collection landing page
  - Earthdata download entry point
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://disc.gsfc.nasa.gov/help (NASA GES DISC access help, checked 2026-09-28)
  field_scope:
  - Earthdata Login requirement for downloading or subsetting data
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://gmao.gsfc.nasa.gov/gmao-products/merra-2/faq_merra-2/ (PM2.5 question, read 2026-09-28)
  field_scope:
  - Current provider surface-mass conversion and organic-carbon coefficient warning
  - Formula applies to MERRA-2, not automatically to GEOS FP or the paper's historical implementation
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://gmao.gsfc.nasa.gov/media/publications/zbly36ziNFDFbmYmvhQeVqPhUo/Bosilovich785.pdf (MERRA-2 file specification, read 2026-09-28)
  field_scope:
  - Table 6.2 identifies M2TMNXAER as the monthly tavgM_2d_aer_Nx collection
  - Aerosol field table distinguishes surface mass in kg/m3 from column mass and dimensionless optical-depth fields
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://pengzhang.weebly.com/uploads/3/1/7/6/31762679/pollution-migration.pdf (published article, page 13 data-availability statement read 2026-09-28)
  field_scope:
  - Article states that the data used are confidential without separating component-level restrictions
  - This statement does not make the NASA raw collection confidential or establish release of the final county measure
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-satellite-pm25
  relation: often-confused-with
- id: china-air-quality-monitoring
  relation: complement
---

## Positioning in one sentence

This is the paper-specific MERRA-2-to-county-PM2.5 construction behind Chen, Oliva and Zhang (2022), not a ready-made China pollution grid. Start with NASA's raw collection only if you can document the missing conversion and spatial-aggregation choices.

## Select rules

- Use it to audit the paper or design a transparently new MERRA-2-based construction.
- Use a separately documented provider grid for an immediately usable exposure surface.
- Do not substitute TAP, a global annual PM2.5 grid, or official ground monitoring data without testing whether its measurement and timing fit the research question.

## Get recipe

1. Obtain M2TMNXAER 5.12.4 through NASA Earthdata.
2. Read the referenced PM2.5 method and make all conversion assumptions explicit.
3. Select a county boundary vintage and spatial aggregation method, then validate the resulting measure independently.

## Connections and Limitations

- The paper joins its county-period exposure to census migration data, but the exact geography conversion is unreleased.
- NASA provides raw input, not the authors' final PM2.5 panel.
- No causal-assignment information belongs in this record.

## Provider conversion starting point

NASA's current FAQ computes surface PM2.5 as
`DUSMASS25 + OCSMASS + BCSMASS + SSSMASS25 + (132.14 / 96.06) * SO4SMASS`.
Its sulfate factor accounts for ammonium sulfate. It warns against adding an
organic-carbon multiplier because that conversion is already represented in
MERRA-2. The FAQ presents the hourly aerosol collection; the paper uses the
monthly M2TMNXAER collection, identified in the file specification. Inspect the
actual monthly file before applying the recipe. Surface-mass units are kg/m3;
conversion to micrograms/m3 multiplies by 1e9. Column mass and optical depth
are different quantities and cannot replace these inputs.

This gives a documented starting point for a new exposure series. The authors'
exact coefficient choices, county-boundary vintage, spatial weights and missing
value handling remain unknown. Their article describes its used data as
confidential without allocating that restriction across components. A NASA
download therefore supports a new documented construction, while an exact
replication still requires the missing implementation details.
