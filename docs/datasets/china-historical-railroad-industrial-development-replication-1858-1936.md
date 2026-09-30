---
schema_version: 3
catalog_status: ready
id: china-historical-railroad-industrial-development-replication-1858-1936
name: Bo--Chen--Liu--Zhou historical China railroad and industrial-development replication package (1858-1936)
aka:
- On the Right Track replication package
- BoChenLiuZhou_replicate.zip
- China historical railroad expansion and industrial-development data
provider: Shiyu Bo, Ting Chen, Cong Liu, and Yan Zhou; deposited through Mendeley Data
china_related: true
domains:
- regional
- urban
- development
- transportation
- firms
- economic history
data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: >-
    Public Mendeley Data v1 replication package for the JDE article. It delivers the
    authors' released historical county-year and county/prefecture cross-section files,
    rail-construction spreadsheets, supporting series, a codebook, and six Stata do-files.
    It is a paper-specific derived research asset, not a release of every historical map,
    archive, or upstream source used to construct it.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    A researcher can directly download a CC BY 4.0 package and rerun or adapt the documented
    analysis files. The verified ZIP contains CountyYear.dta, CountyAggregate5years.dta,
    CountyCrosssection.dta, CountyPopulation3years.dta, PrefCrosssection.dta, railroad
    spreadsheets, and Stata programs. It supports the released historical measures, but not
    an independent reconstruction of the authors' digitized rail network, firm-entry inputs,
    boundary work, or every covariate from original archives.
  barrier: >-
    Re-running the supplied analysis requires Stata and user-written commands. The archive has
    no observed README/run-all file, and the codebook has not been treated as proof of every
    upstream-source lineage; inspect the package and code before extending it.
unit_of_observation: >-
  Historical Chinese county-year in CountyYear.dta and CountyAggregate5years.dta; separate
  county, prefecture, and annual-series observations appear in the other released files.
structure: Paper-specific historical panel and cross-sectional analysis files, plus annual railway/transport series and support spreadsheets.
geo_granularity:
- historical county
- historical prefecture
geography: Historical China as defined in the paper package; the released files use historical county and prefecture identifiers rather than a current administrative panel.
time_span:
  start: '1858'
  end: '1936'
  last_confirmed_release: 'Mendeley Data v1, published 2026-05-26'
  coverage_note: >-
    The article and its released annual files cover the paper's 1858-1936 setting. Some cross-sectional
    and supporting inputs refer to particular benchmark years; their coverage is file-specific.
  last_checked: '2026-09-28'
frequency:
- annual
- five-year aggregate
- cross-section
sample_size: >-
  File-specific. Publisher text describes a 1,442-county China-proper analysis sample for part of the
  paper; do not treat that as the row count or common universe of every released file.
key_variables:
- Historical county/prefecture identifiers and year
- County industrial firm-entry and firm-stock measures
- Railroad-construction, railway-distance, and related historical transport measures
- Historical county/prefecture controls and selected industrial-output measures
research_fit:
  best_for:
  - Reproducing or extending this article's historical China county-level industrial-development analysis for 1858-1936
  - Research needing the authors' released historical county-year railroad and firm-entry measures rather than a present-day rail map
  choose_over:
  - Choose this package over china-high-speed-rail-network for nineteenth- or early-twentieth-century historical counties and the authors' released measures.
  - Choose this package over china-transportation-networks-travel-time-1994-2024 when the required period is 1858-1936.
  - Use a new historical-source construction when original source lineage, another boundary vintage, or absent variables are essential.
  not_good_for:
  - Present-day rail schedules, modern city panels, or post-1936 outcomes
  - Claiming that the released files are a complete raw rail-network archive or a neutral historical-firm census
  - Extending values to another historical boundary system without a documented crosswalk
  needs_join_for:
  - Outcomes or covariates outside the released period and geographic definitions
  - Any modern data after an explicit historical-boundary concordance
  variation_available:
  - Released files contain historical geography, year, rail-network and industrial-development dimensions; causal interpretation is outside this catalog.
  topics:
  - historical railroads
  - industrial development
  - historical counties
  - firm entry
  - China economic history
good_for:
- Historical regional-development replication
- Historical county-year industrial-entry measurement
- Historical railroad-network research using the released paper files
identification:
- The package supplies paper-specific empirical inputs and code; it does not establish a general historical transport database or a causal-design record.
linkable_keys:
- Historical county identifier and year after checking the package's boundary vintage
- Historical prefecture identifier in cross-sectional files
joins:
- target: china-high-speed-rail-network
  relation: complement
  keys:
  - no common period without a documented historical-to-modern geography bridge
  method: Treat as separate historical and modern transport assets; do not join merely on a reused place name.
  evidence_status: plausible
- target: china-transportation-networks-travel-time-1994-2024
  relation: complement
  keys:
  - no direct package key
  method: Use only for a separately designed long-run comparison with a clear boundary and measurement bridge.
  evidence_status: plausible
access_routes:
- route: Mendeley Data v1 replication package
  access_status: available
  direct_url: https://data.mendeley.com/datasets/z8g82cmktz/1
  requirements:
  - A web browser and acceptance of current Mendeley Data terms
  - Approximately 3.43 MB for BoChenLiuZhou_replicate.zip
  - Stata or compatible software plus commands called by the selected do-file
  steps:
  - Open the Mendeley Data record and retain dataset DOI 10.17632/z8g82cmktz.1 and version 1.
  - Download BoChenLiuZhou_replicate.zip and preserve its Program and Data folders together.
  - Read BoChenLiuZhou_Codebook.pdf and inspect the file for the intended unit before running code.
  - Start from the matching Program do-file, review dependencies, then run it in a disposable project copy.
  - Treat an extension to new boundary vintages or original archives as a new documented construction task.
  deliverable: >-
    Public ZIP with a codebook, six Stata do-files, nine Stata data files, and three XLSX support files.
    The public manifest names one completed 3,426,490-byte ZIP.
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    The deposit displays CC BY 4.0, but that does not establish independent rights for every underlying historical source.
access:
  url: https://data.mendeley.com/datasets/z8g82cmktz/1
  cost: free
  license: CC BY 4.0 as displayed on Mendeley Data v1; assess upstream-source rights separately for a new derivative or redistribution.
  format:
  - zip
  - dta
  - do
  - xlsx
  - pdf
  api: true
  how_to_get: Download public version 1, retain DOI/version and folders, inspect the codebook and matching do-file, then use the appropriate released data file.
caveats: >-
  The public package resolves access to the released analysis artifact, not complete provenance of every historical input.
  Do not call its files raw archives, assume they share one sample, or use historical county labels as present-day geography.
production:
  raw_sources:
  - name: Author-released Mendeley replication package
    source_type: dataset
    role: Current direct delivery of paper-specific historical analysis files and code
    access_route: Public Mendeley Data v1 ZIP
    url: https://data.mendeley.com/datasets/z8g82cmktz/1
    coverage: Codebook, Program and Data folders; file-specific historical coverage
    last_checked: '2026-09-28'
  - name: Original historical rail, industrial, geography, and covariate sources
    source_type: archive
    role: Upstream construction inputs to the authors' released files
    access_route: Not established from the inspected package manifest and programs
    url: needs-verification
    coverage: Unresolved at source level
    last_checked: '2026-09-28'
  acquisition_methods:
  - repository download
  - researcher construction
  - aggregation
  - geospatial matching
  sample_construction: >-
    The authors released prepared historical analysis files. The publisher says they digitized railroad expansion
    and compiled micro-level industrial-development information; source-by-source digitization and boundary construction
    are not inferred here.
  pipeline_stages:
  - stage: collect
    inputs:
    - Historical source materials assembled by the authors
    method: Not fully exposed by the inspected manifest and programs.
    tools: []
    parameters: {}
    output: Released historical analysis inputs
    evidence: Publisher article description and Mendeley package manifest
  - stage: aggregate
    inputs:
    - Released county-level files
    method: The supplied programs operate on their matching named released data files.
    tools:
    - Stata 17 or compatible software
    parameters: {}
    output: Paper tables, figures, and file-specific analysis samples
    evidence: Released Program do-files
  - stage: validate
    inputs:
    - Released Data and Program folders
    method: Run the matching supplied do-file after reviewing dependencies; compare output with the article.
    tools:
    - Stata 17 or compatible software
    parameters: {}
    output: Reproduction outputs or a documented dependency discrepancy
    evidence: Released Program do-files; no rerun performed for this catalog record
  constructed_variables:
  - name: Historical county-year railroad and industrial-development measures
    concept: Paper-specific measures distributed in CountyYear.dta and related released files
    source_fields:
    - county identifiers
    - year
    - rail-distance and railway fields
    - firm-entry and firm-stock fields
    method: Provided as author-released files; programs use these fields but do not establish every upstream construction choice.
    validation: Re-run the matching program and compare to published tables/figures.
    limitations: Variable names do not establish raw-source lineage or general comparability beyond the paper.
  output:
    unit_of_observation: Historical county-year plus file-specific county/prefecture cross-sections and annual series
    structure: Panel, aggregated panel, cross-sections, and supporting time series
    geography: Historical Chinese counties and prefectures as encoded by the authors
    time_span: 1858-1936 for the paper setting; exact file coverage varies
    key_variables:
    - historical rail and transport measures
    - industrial firm-entry and firm-stock measures
    - selected historical controls and cross-sectional industrial outcomes
    formats:
    - dta
    - do
    - xlsx
    - pdf
  reproducibility:
    level: medium
    starting_point: https://data.mendeley.com/datasets/z8g82cmktz/1
    code_available: true
    code_url: https://data.mendeley.com/public-api/datasets/z8g82cmktz/files?folder_id=root&version=1
    requirements:
    - Public package download
    - Stata 17 or compatible software
    - Installation of commands called by the selected program
    - Review of the codebook and file-specific dependencies
    blockers:
    - No observed run-all README or complete upstream-source reconstruction recipe
    - Original historical sources, geospatial processing, and boundary concordances remain unestablished
  compliance:
    terms_or_license: CC BY 4.0 displayed on Mendeley Data v1; reassess rights for upstream source material.
    robots_or_rate_limits: Use the Mendeley Data public download route and current terms.
    personal_or_sensitive_data: None expected from historical aggregate and firm-entry files; inspect before redistribution.
    redistribution: The deposited package is CC BY 4.0; do not infer permission for upstream archival inputs beyond the deposit.
    review_needed: true
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'
used_by:
- cite: 'Bo, Chen, Liu & Zhou (2026), On the right track? Railroads, industrial development, and distributional effects in historical China'
  doi: https://doi.org/10.1016/j.jdeveco.2026.103827
  journal: Journal of Development Economics
  year: 2026
  dataset_role: Historical county/prefecture railroad and industrial-development inputs for the paper's 1858-1936 analyses
  evidence_type: published-paper-full-text-and-replication-package
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0304387826001100
  data_note: >-
    Publisher-visible text states that the authors digitize railroad expansion and compile micro-level industrial-development
    information for 1858-1936. Mendeley v1 supplies the named historical panel/cross-section files and programs; it does not
    establish complete independent reconstruction of every input.
provenance:
- source: https://www.sciencedirect.com/science/article/pii/S0304387826001100
  field_scope:
  - paper identity and 1858-1936 historical-China scope
  - statement that railroad-expansion and industrial-development data were digitized/compiled
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://data.mendeley.com/datasets/z8g82cmktz/1
  field_scope:
  - public replication-package identity, version 1, DOI, and displayed CC BY 4.0 licence
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://data.mendeley.com/public-api/datasets/z8g82cmktz/files?folder_id=root&version=1
  field_scope:
  - completed public BoChenLiuZhou_replicate.zip manifest and direct public download URL
  - 3,426,490-byte package size and delivery availability
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Public ZIP inspected in memory from the Mendeley manifest download URL (2026-09-28)
  field_scope:
  - Program folder with six Stata do-files and a codebook PDF
  - Data folder with named historical county/prefecture .dta files, annual supporting files, and railway spreadsheets
  - program-to-file relationships and Stata 17 header comments
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-high-speed-rail-network
  relation: complement
- id: china-transportation-networks-travel-time-1994-2024
  relation: complement
---

## Positioning in one sentence

This is the directly downloadable, paper-specific historical China railroad and industrial-development package for 1858-1936. It is the right starting point for reproducing or carefully extending the released county/prefecture analysis files, but not for independently rebuilding its archival inputs.

## Select rules

- Choose it when a project needs the authors' historical county-year railroad and firm-entry measures or their released cross-sectional historical outcomes.
- Use another historical-source construction when source lineage, a different boundary vintage, or absent variables are essential.
- Do not use it as a modern rail, current city, or general all-purpose historical-firm database.

## Get recipe

1. Download version 1 of `BoChenLiuZhou_replicate.zip` from Mendeley and retain its DOI/version.
2. Read the codebook and select the data file matching the intended unit; released files do not necessarily share the same coverage.
3. Review the matching Stata program and its dependencies before execution.
4. Treat a new archive, geospatial, or boundary reconstruction as a separate documented extension.

## Connections and Limitations

The files use historical county and prefecture geography. A modern place name or code is not enough for a valid join. The released package preserves paper-compatible derived measurements but does not reveal every upstream data source, boundary concordance, or digitization choice needed to recreate them independently.
