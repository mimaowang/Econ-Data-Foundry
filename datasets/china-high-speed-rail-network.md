---
schema_version: 3
catalog_status: ready
id: china-high-speed-rail-network
name: Borusyak–Hull China high-speed-rail network and market-access replication asset
aka:
- China HSR network replication package
- BH replication package
- 中国高铁网络数据
- Non-Random Exposure to Exogenous Shocks replication data
provider: Kirill Borusyak and Peter Hull; upstream sources include China Statistics Press, CityPopulation.de, and OCHA regional shapefiles
china_related: true
domains:
- transport
- regional
- urban
- labor
- infrastructure
- spatial

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: Public Zenodo package BH replication.zip containing the paper's HSR line/station inputs, prefecture population and coordinates, Chinese City Statistical Yearbooks, GIS files, processing instructions, code, and derived market-access outputs
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The author's replication package is directly downloadable and includes the public raw inputs and construction code used for the China HSR application. A researcher can use the released line and station files or rebuild the documented prefecture-year outputs, but a full rebuild requires the stated Stata/Python/GIS environment and substantial computation for the simulated networks.
  barrier: The current Zenodo record labels the released replication archive CC-BY-4.0, but that deposit-level license does not by itself settle redistribution rights for every third-party yearbook or upstream input. Current upstream CNKI yearbook links have changed; use the released package or verify institutional/purchase access before rebuilding from upstream sources.

unit_of_observation: HSR line or line-section, ordered prefecture stop, prefecture-year outcome, and scenario-specific prefecture-year market-access output (separate files in the replication package)
structure: network-plus-panel replication bundle
geo_granularity:
- prefecture-level city
- sub-prefecture city
- HSR line/section
geography: 340 mainland-China prefecture and sub-prefecture units used by the paper, excluding Hainan, Taiwan, Hong Kong, and Macau; six sub-prefecture cities are included
time_span:
  start: '2000'
  end: '2019-04'
  last_confirmed_release: '2023-08-30'
  coverage_note: Population inputs cover 2000 and 2010; city yearbooks in the package cover 2000-2017 (with 2007-2016 outcomes because each yearbook covers the preceding year); the network includes lines open by the end of 2016 and lines planned or under construction as of April 2019 but not yet open by the end of 2016.
  last_checked: '2026-08-10'
frequency:
- annual
- event-dated line opening
sample_size: 340 prefecture or sub-prefecture units; the paper's main employment outcome retains 275 prefectures; the package contains the actual network plus 1,999 counterfactual line assignments (2,000 scenarios including the actual network)
key_variables:
- Line and line-section identity
- Ordered prefecture stops and station information
- Official opening date when open
- Actual or planned operating speed
- Opened versus planned or under-construction status
- 2000 and 2010 prefecture population
- Prefecture coordinates and centroids
- Travel time between prefectures under actual and simulated networks
- Market-access levels and 2007-2016 changes
- HSR stop/connectivity indicators
- City-yearbook employment and regional controls

research_fit:
  best_for:
  - Reproducing or adapting a prefecture-level China HSR network and market-access input for regional employment or transport research
  - Studies that need ordered stops, opening dates, planned-line information, and the distinction between the network input and the derived market-access panel
  choose_over:
  - Choose this package over a generic current HSR map when the research needs the paper's historical 2007-2016 definition and its planned-line snapshot
  - Choose the standalone China Statistical Yearbook record when only annual regional outcomes or controls are needed and no railway-network reconstruction is required
  - Use the package's released files before attempting to re-collect yearbooks or infer line histories from current maps
  not_good_for:
  - Current HSR operations after the package's 2019 planning snapshot
  - Treating the market-access output as a nationally representative household, firm, or worker dataset
  - Assuming that every yearbook table or upstream source can be redistributed under the Zenodo record's unspecified license
  needs_join_for:
  - Firm, household, worker, land, or policy outcomes not contained in the package
  - A different prefecture boundary vintage or a finer-than-prefecture spatial unit
  variation_available:
  - Historical network states (opened or planned) and annual line-opening dates are fields in this asset; no causal or exogenous-shock classification is recorded here.
  topics:
  - high-speed rail
  - transport infrastructure
  - market access
  - regional employment
  - urban development
  - prefecture networks

good_for:
- Constructing historical prefecture-level HSR connectivity, travel-time, or market-access measures
- Reproducing the paper's 2007-2016 regional employment application while keeping line inputs, yearbook outcomes, and transformations distinct
- Using ordered network stops and planned lines as inputs to a new spatial aggregation, subject to boundary and licensing checks
identification:
- This is a historical network-and-market-access replication asset, not an exogenous-shock record: it can support spatial exposure construction only after a researcher independently chooses and defends a treatment or research design.
linkable_keys:
- Prefecture or city name after documented normalization
- Prefecture coordinates or centroid
- Year
- Ordered HSR stop sequence

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Prefecture or city identifier
  - Year
  method: administrative-name and boundary concordance
  evidence_status: literature-used
- target: china-census
  relation: complement
  keys:
  - Prefecture or city identifier
  - 2000 population reference year
  method: population-weight and administrative concordance
  evidence_status: literature-used

access_routes:
- route: Zenodo replication package
  access_status: available
  direct_url: https://zenodo.org/records/8286785
  requirements:
  - Download the 101.6MB BH replication.zip
  - Stata 17 and Python 3.9 for the documented pipeline; ArcMap 10.8.2 is used for some GIS steps
  steps:
  - Open the Zenodo record and verify the current CC-BY-4.0 deposit licence, 101,647,028-byte archive, and MD5 checksum e062e3aaa0af23dd65f6a971db94e358.
  - Download BH replication.zip and read README_ECMA before opening any code.
  - Use the released raw/stations.xlsx, raw/Population.xlsx, GIS files, yearbooks, and processing instructions as the starting point.
  - Run only the documented preparation stages needed for the intended artifact; do not assume the package grants rights to redistribute third-party yearbook files.
  deliverable: Author-released raw inputs, line and GIS files, code, processing metadata, yearbook extracts, and paper-specific derived files; exact file names and permissions should be checked against the downloaded version.
  cost: free
  last_checked: '2026-09-28'
  caveat: Current Zenodo API confirms public access and CC-BY-4.0 at the deposit level. Third-party source rights and current CNKI access remain separate checks.
- route: Rebuild from upstream sources
  access_status: available-with-conditions
  direct_url: https://back.nber.org/appendix/w27845/shock_exposure_v91_apdx.pdf
  requirements:
  - China City Statistical Yearbooks or an institutional CNKI route
  - Public CityPopulation and OCHA spatial inputs
  - Manual line-history verification from the documented sources
  steps:
  - Read the data appendix and the package's source manifest.
  - Obtain the relevant yearbook editions and record their table definitions and access terms.
  - Reconstruct the line/station inventory and prefecture concordance, preserving manual corrections.
  - Re-run the cleaning and aggregation code, then compare outputs with the released files.
  deliverable: Independently rebuilt network and prefecture-year inputs, conditional on upstream coverage and legal access.
  cost: mixed
  last_checked: '2026-08-10'
  caveat: The package README says the historical CNKI links used by the authors are no longer operational; institutional or paid PDF access may be needed.

access:
  url: https://zenodo.org/records/8286785
  cost: free
  license: CC-BY-4.0 for the Zenodo deposit; third-party source rights remain separate
  format:
  - zip
  - xlsx
  - csv
  - shp
  - dta
  - do
  - py
  api: false
  how_to_get: Download the Zenodo package, inspect its README and rights notes, and use the released artifacts before attempting an upstream rebuild.
caveats:
- The network is a historical, paper-specific inventory, not a live railway timetable or a guarantee of current service.
- A line opening date, planned status, operating speed, and ordered stop list are author-assembled fields; preserve their definitions rather than substituting a current map.
- The paper's market-access formula and simulated scenarios are derived products. Access to the raw line and population files does not imply that a new researcher will reproduce every cleaned table without running the pipeline.
- Administrative boundaries and city names require concordance when joining to a different panel or later boundary vintage.

production:
  raw_sources:
  - name: Population by Chinese prefecture
    source_type: webpage
    role: 2000 and 2010 population weights
    access_route: CityPopulation.de and released raw/Population.xlsx
    url: https://www.citypopulation.de/en/china/admin/
    coverage: Chinese prefecture population with a manually documented Hubei correction
    last_checked: '2026-08-10'
  - name: Characteristics of HSR lines and stations
    source_type: spreadsheet
    role: Line identity, ordered stops, opening/planned status, and operating speed
    access_route: Released raw/stations.xlsx; authors' manual compilation from railway references and web checks
    url: https://zenodo.org/records/8286785
    coverage: Opened lines plus planned or under-construction lines as of April 2019
    last_checked: '2026-08-10'
  - name: Chinese City Statistical Yearbooks
    source_type: dataset
    role: Prefecture and county regional employment and control variables
    access_route: Released raw/yearbooks files; historical CNKI route documented in the package README
    url: https://oversea.cnki.net/KNavi/YearbookDetail?pcode=CYFD&pykm=YZGCA
    coverage: 2000-2017 yearbook editions, with prefecture and county-level folders
    last_checked: '2026-08-10'
  - name: OCHA China administrative boundaries and capitals
    source_type: shapefile
    role: Prefecture coordinates, centroids, and GIS crosswalk
    access_route: Public OCHA/HumData downloads and released GIS inputs
    url: https://data.humdata.org/dataset/china-administrative-boundaries
    coverage: Administrative boundary and capital coordinate inputs used by the paper
    last_checked: '2026-08-10'
  acquisition_methods:
  - direct download
  - manual compilation
  - spreadsheet extraction
  - geocoding
  - administrative concordance
  sample_construction: The package covers 340 mainland prefecture or sub-prefecture units. The main outcome panel uses 275 units with cleaned non-missing 2007-2016 employment growth; this is a paper sample, not the coverage of the line inventory itself.
  pipeline_stages:
  - stage: collect
    inputs:
    - Population by Chinese prefecture
    - HSR line references and station list
    - Chinese City Statistical Yearbooks
    - OCHA spatial files
    method: Assemble public and author-produced inputs into the package's raw folders and retain source-specific corrections.
    tools:
    - Stata
    - Python
    - ArcGIS
    output: Raw population, station, line, yearbook, and spatial inputs
    evidence: README_ECMA sections Data Availability and Details on each Data Source; Zenodo package 10.5281/zenodo.8286785
  - stage: clean
    inputs:
    - raw/stations.xlsx
    - raw/Population.xlsx
    - raw GIS files
    method: Normalize city names, clean line and station fields, and build the prefecture concordance.
    tools:
    - Stata do-files in code/build_data
    - Python scripts
    output: Clean line, station, population, and city-coordinate tables
    evidence: README_ECMA program description and code/build_data/3_clean_lines.do
  - stage: parse
    inputs:
    - raw/yearbooks
    - raw/input processing indexes
    method: Unlock, extract, translate, and clean yearbook tables before constructing prefecture and county outcomes.
    tools:
    - Python
    - Stata
    output: Yearbook-derived regional panels
    evidence: README_ECMA program description and code/build_data/9_clean_yearbook.py
  - stage: geocode
    inputs:
    - OCHA boundaries and capitals
    - City and prefecture names
    method: Use released centroids and capital coordinates to map prefecture units and network stops.
    tools:
    - ArcMap
    - GIS files
    output: Prefecture coordinate and line geometry inputs
    evidence: README_ECMA City Centroids and Coordinates of Capitals sections
  - stage: aggregate
    inputs:
    - Clean line and station tables
    - Prefecture coordinates
    - Population table
    method: Compute travel-time and market-access outputs for the actual network and the documented counterfactual scenarios.
    tools:
    - Stata
    - Optional SLURM or Torque cluster
    output: Prefecture-year market-access, connectivity, scenario, and combined analysis files
    evidence: README_ECMA program description; paper online appendix A.1
  constructed_variables:
  - name: market_access
    concept: Population-weighted accessibility across prefectures under the assembled HSR and traditional-transport network
    source_fields:
    - Ordered stops
    - Operating speed
    - Prefecture coordinates
    - 2000 population
    method: Use the paper's documented travel-time and population-weighted formula for actual and simulated networks.
    validation: Compare the released outputs with the package's scenario and analysis files.
    limitations: Formula choices, speed adjustment, and boundary concordance are paper-specific and are not a generic HSR measure.
  - name: hsr_connectivity
    concept: Whether a prefecture has an HSR stop by a given year or scenario
    source_fields:
    - Ordered stops
    - Opening date
    method: Annualize the line opening information as documented in the replication code.
    validation: Cross-check against the line and station tables and released figures.
    limitations: Historical opening and planned status are author-assembled; current operations are outside scope.
  validation:
  - Cross-check network links across Lawrence et al. (2019), China Railway Yearbooks, Lin (2017), and web sources as documented by the authors.
  - Compare yearbook sources where overlapping editions are available.
  - Preserve the package's manual city-name and Hubei population corrections.
  - Compare reproduced outputs with the released line, scenario, and analysis files before adapting the asset.
  output:
    unit_of_observation: Line/section, prefecture-stop, and prefecture-year output files
    structure: Network inventory plus panel and scenario tables
    geography: 340 mainland prefecture or sub-prefecture units; main employment sample 275
    time_span: 2000-2019 source and network window; 2007-2016 main outcome window
    key_variables:
    - HSR line and stop fields
    - Opening/planned status and speed
    - Population and prefecture coordinates
    - Travel time, market access, and connectivity
    - City-yearbook employment and controls
    formats:
    - xlsx
    - csv
    - shp
    - dta
  reproducibility:
    level: medium
    starting_point: https://zenodo.org/records/8286785
    code_available: true
    code_url: https://zenodo.org/records/8286785
    requirements:
    - Stata 17 with the packages listed in README_ECMA
    - Python 3.9 and requirements.txt
    - ArcMap 10.8.2 for documented GIS steps
    - Approximately 15 minutes for local non-cluster steps and optional cluster resources for scenario generation
    requirements_note: The README reports roughly 100 parallel jobs and about three hours for the cluster portion in the authors' run; local execution is possible but slower.
    blockers:
    - Current CNKI yearbook route and historical access terms need rechecking.
    - Third-party redistribution permissions must still be assessed source by source; the deposit-level CC-BY-4.0 label is not a substitute for them.
  compliance:
    terms_or_license: Zenodo API currently labels the deposit CC-BY-4.0; third-party yearbook, CityPopulation, OCHA, and web-source terms remain applicable.
    robots_or_rate_limits: Do not scrape current railway or yearbook sites merely because the historical package used web checks.
    personal_or_sensitive_data: No personal microdata are identified in the package description.
    redistribution: Do not redistribute package contents or extracted third-party files until the current rights and source terms are verified.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-10'

used_by:
- cite: 'Borusyak & Hull (2023), Nonrandom Exposure to Exogenous Shocks'
  doi: https://doi.org/10.3982/ECTA19367
  journal: Econometrica
  year: 2023
  dataset_role: Paper-constructed China HSR line and station inputs, prefecture population and coordinates, market-access outputs, and simulated network files for the 2007-2016 regional employment application
  evidence_type: replication
  evidence_url: https://zenodo.org/records/8286785
  data_note: >-
    The public package contains BH replication.zip, raw population and station files, Chinese City Statistical Yearbooks,
    GIS inputs, processing indexes, Stata/Python code, and derived analysis files. The README identifies the network as a manual
    compilation from Lawrence et al. (2019), China Railway Yearbooks, Lin (2017), and web cross-checks, with lines open by the end
    of 2016 and planned or under-construction lines as of April 2019. It reports the 340-unit geography, the 2007-2016 outcome
    window, and the actual plus simulated network outputs. This is evidence of a released paper-specific data product, not a
    claim that current railway operations or every upstream source has the same access terms.

provenance:
- source: Zenodo replication package 10.5281/zenodo.8286785 and its README_ECMA data-availability and program descriptions
  field_scope:
  - target artifact
  - raw source manifest
  - file-level components
  - software requirements
  - reproduction runtime
  - rights caveat
  added: '2026-08-10'
  confidence: high
  verified: true
- source: Zenodo API record 8286785 (queried 2026-09-28)
  field_scope:
  - current public record, CC-BY-4.0 deposit licence, publication date, archive name, size and MD5 checksum
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Borusyak & Hull online data appendix https://back.nber.org/appendix/w27845/shock_exposure_v91_apdx.pdf
  field_scope:
  - 340-unit geography
  - network construction boundary
  - line fields and speed definition
  - population and yearbook inputs
  - 2007-2016 output window
  added: '2026-08-10'
  confidence: high
  verified: true
- source: Econometrica article manuscript https://pmc.ncbi.nlm.nih.gov/articles/PMC10795685/
  field_scope:
  - published paper use
  - data appendix context
  added: '2026-08-10'
  confidence: high
  verified: true

related_datasets:
- id: china-stat-yearbook
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

This is the authors' downloadable, paper-specific China HSR network and market-access replication asset: it gives a researcher historical line/station inputs, spatial files, yearbook inputs, code, and derived prefecture outputs in one reproducible starting point, while leaving current-service coverage and third-party redistribution rights as explicit boundaries.

## Select rules

- Prioritize it when a study needs the 2007-2016 historical HSR definition, ordered prefecture stops, planned-line information, or the paper's market-access transformations.
- Use the China Statistical Yearbook record alone when the research needs regional outcomes but not the railway network.
- Treat the Zenodo package as the starting artifact. Rebuild from CNKI, CityPopulation, OCHA, or web sources only after checking current access and terms.

## Get recipe

1. Download BH replication.zip from the Zenodo record and read README_ECMA.
2. Decide whether the released line, station, GIS, yearbook, or derived panel file already answers the data question.
3. If a rebuild is necessary, use the package's source indexes and documented Stata/Python/GIS steps; keep the raw source, constructed network, and market-access output as separate layers.
4. Compare the resulting fields and counts with the released files, then record any boundary concordance or source-access change before joining another dataset.

## Connections and Limitations

Join regional outcomes by a documented prefecture/city concordance and year. The package's prefecture definitions, six sub-prefecture units, city-name corrections, and city-proper versus whole-prefecture yearbook distinctions matter more than a generic “China city” label. The asset is useful for historical regional data work; it is not a live HSR schedule, a household/firm microdata source, or evidence that a particular causal design is valid.
