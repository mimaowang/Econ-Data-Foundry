---
schema_version: 3
catalog_status: ready
id: china-jue-pmc-fiscal-reform-replication-2026
name: Chen–Li–Sun China Province-Managing-County reform replication data package
aka:
- Flattening Governments, Flattening Growth replication data
- JUE 2026 PMC reform replication package
- 中国省直管县改革县级、省级与企业级复现数据
provider: Shawn Xiaoguang Chen, Pei Li and Saijie Sun; deposited through Mendeley Data
china_related: true
domains:
- regional
- urban
- public finance
- firms
- productivity
- inequality

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: >-
    Public Mendeley Data v1 package for the JUE paper, containing a README,
    output manifest, Stata do-files, raw_county_level_data.dta,
    raw_province_level_data.dta, and raw_firm_level_data.dta. The package creates
    the paper's stacked samples, aggregates, tables, and figures when the supplied
    code is run; generated result files are not pre-filled in the downloaded package.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The public package is a usable, paper-specific starting artifact: the data files
    and code can be downloaded directly, and the README documents the Stata setup and
    execution order. It is not a release of every upstream statistical or enterprise
    database. In particular, the README says the China Annual Surveys of Industrial
    Firms input is restricted and that the released firm file uses anonymized firm IDs;
    the source lineage of the county panel is not identified in the package.
  barrier: >-
    Full reconstruction requires Stata 18-compatible tooling and the listed user-written
    commands. The anonymized firm identifiers cannot be used to recover original ASIF
    identities or make an external firm-level join. The package does not establish a
    public route to the underlying restricted ASIF source, and the exact original
    provider and boundary concordance of the county file remain open questions.

unit_of_observation: County-year, province-year aggregate, and anonymized firm-year (separate files)
structure: Annual panel plus paper-specific derived stacked samples and aggregates
geo_granularity:
- county
- province
- firm located in a county
geography: >-
  Mainland China. The released county file has 13,808 rows, 1,726 unique county
  codes, and 23 provinces; the firm file has 287,798 rows and 124,520 anonymized
  firm IDs. These file-level counts describe the deposited artifact, not a claim of
  complete national coverage or a common universe across files.
time_span:
  start: '2000'
  end: '2007'
  last_confirmed_release: '2026-05-26'
  coverage_note: >-
    All three raw files and the supplied analysis scripts use 2000-2007. County and
    province analyses derive inequality, GDP-per-capita, fiscal, and reform-related
    variables from the county panel. The firm script merges anonymized firm-year data
    to county-year fields and estimates firm productivity outcomes. No later years
    are present in the checked raw files.
  last_checked: '2026-09-27'
frequency:
- annual
sample_size: >-
  County file: 13,808 rows and 1,726 unique county codes; firm file: 287,798 rows
  and 124,520 anonymized firm IDs; province file: 88 rows covering 11 provinces.
  Counts are file-specific and should not be added together or interpreted as a
  single balanced panel.
key_variables:
- County and province identifiers/names, year, city and administrative fields
- GDP, population, CPI, real GDP-per-capita inputs, and inequality components
- Local, prefecture, and province revenue/expenditure and transfer variables
- PMC/reform-year and county classification fields such as pmc_year, county_city,
  poor_county, food_county, and provboundary_county
- Terrain and fiscal controls including slope, altitude, urban_rate00, fiscal_gap99,
  cpe, and VAT-sharing fields
- Anonymized firm ID, county, year, industry code, labor and capital inputs, and
  productivity measures lnL, lnK, op, lp, and acf

research_fit:
  best_for:
  - Reproducing or extending the JUE paper's 2000-2007 county fiscal/economic panel,
    province inequality aggregates, and anonymized firm productivity analysis
  - Starting a regional or urban project that needs the exact paper-compatible county
    fields and public code rather than a generic current city panel
  - Learning which county-year and firm-year inputs are actually available before
    seeking restricted source data
  choose_over:
  - Choose this package over a general China Statistical Yearbook download when the
    paper-specific 2000-2007 county fields, stacked samples, or supplied Stata code
    are the object to reproduce.
  - Choose ASIF or another firm panel when original firm identifiers, a different
    period, or independent firm-level linkage is essential; this package cannot
    restore those identifiers.
  - Choose a current county or city panel when the research needs recent years; this
    package ends in 2007 and should not be silently updated with another source.
  not_good_for:
  - A current or continuously updated county panel, a guaranteed all-county census,
    or a national firm database with public original IDs
  - Linking the paper's anonymized firms to ASIF, registry, patent, or pollution
    records by guessing names or codes
  - Treating PMC reform timing or its causal interpretation as a variation record
  needs_join_for:
  - Current county/city outcomes, weather, land, housing, or other external controls
  - A boundary-harmonized city or county panel outside the 2000-2007 window
  - Firm-level ownership, registration, innovation, or emissions outcomes when the
    anonymized ID cannot be matched
  variation_available:
  - The county file contains reform-related fields such as pmc_year and classification
    variables used by the paper; they are data dimensions only. Institutional change,
    treatment interpretation, and identification threats belong in the separate
    Econ-Variation repository.
  topics:
  - fiscal federalism
  - county administration
  - regional inequality
  - local economic growth
  - firm productivity
  - China county economy

good_for:
- Paper-compatible county-year and province-year regional analysis for 2000-2007
- Anonymized firm-level productivity analysis using the supplied county-year merge
- Reproducing the paper's tables and figures after installing the documented Stata
  packages and running the supplied scripts
identification:
- The public package supports replication of the paper's documented county, province, and anonymized-firm analyses; it does not by itself identify the original county-data provider, restore ASIF identifiers, or establish a causal interpretation.
linkable_keys:
- County code/name and year, after checking the paper's administrative vintage
- Province code/name and year
- Anonymized firm ID only within the released firm file
- Industry code and county/year for the package's internal firm-to-county merge

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - County or province code/name
  - Year
  method: >-
    Use published statistical controls only after checking definitions, price basis,
    administrative boundaries, and missingness against the package's county/province
    fields. A matching county name alone is not enough.
  evidence_status: plausible
- target: asif
  relation: often-confused-with
  keys:
  - No verified external firm key
  method: >-
    Keep the anonymized firm file separate from ASIF. The README identifies restricted
    ASIF as an upstream source but states that released firm IDs are anonymized; do not
    claim a firm-level merge unless the authors provide a lawful concordance.
  evidence_status: verified
- target: china-land-transaction
  relation: complement
  keys:
  - County/city and year, only for documented contextual joins
  method: >-
    A land or development indicator can be joined at county/city-year after boundary
    checks, but it is not part of this replication package and cannot replace the
    package's fiscal or firm variables.
  evidence_status: plausible

access_routes:
- route: Mendeley Data v1 replication package
  access_status: available
  direct_url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
  requirements:
  - A web browser and acceptance of the current Mendeley Data terms
  - Approximately 7.2 MB for Replication_Package.zip
  - Stata 18 or compatible tooling and the documented user-written packages for a rerun
  steps:
  - Open the Mendeley record and cite dataset DOI 10.17632/x7t7fcwsxg.1.
  - Download Replication_Package.zip and keep its README, output_manifest.csv, code,
    and data folders together; do not rename them.
  - Read README.pdf and inspect output_manifest.csv before running anything.
  - Run code/0_setup.do and code/run_all.do, or a single analysis do-file, after
    reviewing the package-install setting and local paths.
  - Compare generated tables/figures with the paper and record any missing Stata
    packages or output differences.
  deliverable: >-
    Public ZIP containing README.pdf, output_manifest.csv, five Stata do-files, three
    raw .dta files, and empty result directories that are populated when the code runs.
  cost: free
  last_checked: '2026-09-27'
  caveat: >-
    The Mendeley deposit is public and labelled CC BY 4.0, but rights to any
    third-party upstream content and the restricted ASIF source must be checked
    separately before redistribution or a new derivative.
- route: Underlying China Annual Surveys of Industrial Firms (ASIF)
  access_status: restricted
  direct_url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
  requirements:
  - A lawful route approved by the relevant data provider or institution
  - The exact paper-compatible ASIF wave, fields, and firm identifier permissions
  steps:
  - Treat the public package as the starting artifact and read its README/code for the
    fields that the restricted source would have supplied.
  - Seek the source through an official or institutional route; do not infer access
    from the public anonymized file.
  - Keep any approved restricted files outside this repository and document the
    concordance before attempting a join.
  deliverable: Restricted source data if separately approved; the Mendeley package does not restore original firm IDs.
  cost: by-application
  last_checked: '2026-08-13'
  caveat: The checked README confirms the restriction and anonymization but does not provide a public ASIF download route.

access:
  url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
  cost: mixed
  license: CC BY 4.0 for the Mendeley dataset as displayed on the deposit page; verify third-party source terms before redistribution
  format:
  - zip
  - dta
  - do
  - pdf
  - csv
  api: true
  how_to_get: >-
    Open the Mendeley Data page or its public file endpoint, download the version-1
    Replication_Package.zip, read the README and manifest, and retain the package
    version and file layout when reproducing the analyses.

caveats:
- The package is a researcher-constructed replication artifact, not a neutral release
  of the county statistical system or ASIF.
- The county file's original statistical provider and exact county-code/boundary
  vintage are not identified in the checked package; do not fill that gap with a
  presumed yearbook source.
- The README states that raw_firm_level_data.dta is anonymized because ASIF is
  restricted; firm_anon_id is useful inside this package but not an original ASIF key.
- The raw files cover 2000-2007. The presence of reform-year fields does not expand the
  temporal coverage or prove that every county-year is observed.
- The package does not include precomputed result files in the checked download; a
  successful download is not the same as having run or validated Stata output.
- A paper replication package may include cleaned or constructed inputs labelled raw;
  treat the file names as package labels, not proof of an untouched provider extract.

production:
  raw_sources:
  - name: Paper-specific county-level economic and fiscal panel
    source_type: dataset
    role: County GDP, population, CPI, fiscal, classification, terrain, and reform-related inputs
    access_route: Public Mendeley replication package
    url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
    coverage: 13,808 rows, 1,726 unique county codes, 23 provinces, 2000-2007 in raw_county_level_data.dta; original provider not identified
    last_checked: '2026-08-13'
  - name: China Annual Surveys of Industrial Firms (ASIF) input
    source_type: dataset
    role: Firm labor, capital, industry, and productivity inputs represented in the paper's firm analysis
    access_route: Restricted upstream source named in the replication README; public package contains an anonymized derivative
    url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
    coverage: 287,798 anonymized firm-year rows, 2000-2007, in raw_firm_level_data.dta; original ASIF identifiers are not released
    last_checked: '2026-08-13'
  - name: Province aggregate derived from county panel
    source_type: dataset
    role: Province-year inequality and weighted GDP-per-capita analysis
    access_route: Public Mendeley replication package
    url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
    coverage: 88 rows, 11 provinces, 2000-2007 in raw_province_level_data.dta; this is a paper-package aggregate rather than a separate provider release
    last_checked: '2026-08-13'
  acquisition_methods:
  - repository download
  - researcher construction
  - cleaning
  - aggregation
  - internal county-year merge
  sample_construction: >-
    The package supplies county, province, and anonymized firm files. The code creates
    province aggregates and stacked samples, derives real GDP-per-capita and inequality
    measures, and merges firm-year observations to county-year fields using the
    documented county/year and classification fields. It does not document a public
    reconstruction route for the restricted ASIF identifiers.
  pipeline_stages:
  - stage: collect
    inputs:
    - Paper-specific county economic/fiscal panel
    - Restricted ASIF-derived firm input
    method: Keep the three released .dta files as the public starting artifact; retain the distinction between package files and upstream providers.
    tools:
    - Mendeley Data
    - Stata
    output: raw_county_level_data.dta, raw_firm_level_data.dta, and raw_province_level_data.dta
    evidence: Mendeley README, file manifest, and local inspection of the released files
  - stage: clean
    inputs:
    - raw_county_level_data.dta
    - raw_firm_level_data.dta
    method: Use code/1_province_level_analysis.do and code/2_county_level_analysis.do to create real GDP-per-capita, fiscal, classification, and stacked-sample variables; use code/3_firm_level_analysis.do for firm outcomes.
    tools:
    - Stata 18
    - ftools
    - reghdfe
    - outreg2
    - asdoc
    - inequal
    - event_plot
    - did_multiplegt
    - csdid
    - eventstudyinteract
    - did2s
    output: Paper-specific county/province analysis files and firm outcomes under data/stacked_sample and result folders when run
    evidence: Supplied do-files and README
  - stage: aggregate
    inputs:
    - County-level panel
    method: Aggregate county observations to province/year and calculate population-weighted GDP-per-capita and inequality measures including Gini, Theil, RMD, and MLD as coded.
    tools:
    - Stata
    output: Province-level analysis inputs and reported tables/figures
    evidence: code/1_province_level_analysis.do
  - stage: match
    inputs:
    - raw_firm_level_data.dta
    - raw_county_level_data.dta
    method: Merge firm-year rows to county-year rows using pmc_year, cpe, county_city, poor_county, food_county, provboundary_county, slope, altitude, urban_rate00, fiscal_gap99, and the county identifier/year fields in the supplied script.
    tools:
    - Stata
    output: Firm-level analysis sample with county context
    evidence: code/3_firm_level_analysis.do
  - stage: validate
    inputs:
    - Released data files
    - README.pdf
    - output_manifest.csv
    - Supplied do-files
    method: Install the documented Stata packages, run the setup and analysis scripts, and compare generated output with the manifest and the paper's tables/figures.
    tools:
    - Stata 18
    output: Reproduction outputs and a record of any missing dependency or discrepancy
    evidence: README and output manifest; no Stata rerun was performed for this catalog entry
  constructed_variables:
  - name: County real GDP per capita and fiscal measures
    concept: Paper-specific county economic and fiscal outcomes
    source_fields:
    - gdp
    - pop
    - cpi
    - local_fiscal_expenditure
    - transfer_and_tax_rebate
    method: As coded in code/1_province_level_analysis.do and code/2_county_level_analysis.do.
    validation: Compare variable construction and generated outputs with the supplied scripts and paper tables.
    limitations: Source lineage, price-base documentation, and administrative-vintage concordance are not fully identified in the package.
  - name: Province inequality measures
    concept: Population-weighted inequality and GDP-per-capita aggregates
    source_fields:
    - county GDP per capita
    - population weights
    method: Province/year aggregation and Gini, Theil, RMD, and MLD calculations in the supplied province script.
    validation: Re-run the script and compare output manifest entries and paper results.
    limitations: This is a paper-specific aggregate; it should not be treated as a general inequality database.
  - name: Firm productivity outcomes
    concept: Labor, capital, output, and productivity variables used in firm-level tables
    source_fields:
    - lnL
    - lnK
    - op
    - lp
    - acf
    method: Use the anonymized firm file and supplied firm-analysis script; the released IDs cannot recover original ASIF linkage.
    validation: Check firm-year counts, merge behavior, and table outputs against the script and paper.
    limitations: Anonymization prevents external firm matching and the public package does not establish the full ASIF extraction process.
  output:
    unit_of_observation: County-year, province-year, or anonymized firm-year depending on the file or generated sample
    structure: Annual panel and paper-specific derived analysis files
    geography: Chinese counties/provinces and firms assigned to counties in the package
    time_span: 2000-2007
    key_variables:
    - County/province identifiers and year
    - GDP, population, CPI, fiscal, inequality, reform/classification, and terrain fields
    - Anonymized firm identifiers, industry, labor, capital, output, and productivity measures
    formats:
    - dta
    - do
    - csv or table outputs generated by Stata
  reproducibility:
    level: medium
    starting_point: https://data.mendeley.com/datasets/x7t7fcwsxg/1
    code_available: true
    code_url: https://data.mendeley.com/public-api/datasets/x7t7fcwsxg/files?folder_id=root&version=1
    requirements:
    - Public Mendeley download and current terms
    - Stata 18 or a compatible environment
    - ftools, reghdfe, outreg2, asdoc, inequal, event_plot, did_multiplegt, csdid, eventstudyinteract, and did2s
    - Enough time for firm-level high-dimensional regressions
    - Separate lawful access if the original restricted ASIF data or identifiers are required
    blockers:
    - No public original ASIF identifiers or complete upstream source route
    - County-panel provider and exact boundary concordance not identified
    - Stata rerun and output comparison remain to be performed by a future user
  compliance:
    terms_or_license: Mendeley deposit displays CC BY 4.0; follow any third-party source and ASIF restrictions separately
    robots_or_rate_limits: Use the public Mendeley route; do not scrape restricted sources or the publisher to recreate missing files
    personal_or_sensitive_data: Firm identifiers are anonymized in the released file; inspect any future author-provided source before handling
    redistribution: Do not redistribute restricted ASIF inputs or derived joins unless the applicable terms permit it
    review_needed: true

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

used_by:
- cite: 'Chen, Li & Sun (2026), Flattening governments, flattening growth: Equalization–efficiency trade-off in jurisdictional reform'
  doi: https://doi.org/10.1016/j.jue.2026.103885
  journal: Journal of Urban Economics
  year: 2026
  dataset_role: Main county, province, and firm-level data and supplied code for the paper's China regional fiscal and productivity analyses
  evidence_type: replication-package
  evidence_url: https://data.mendeley.com/datasets/x7t7fcwsxg/1
  data_note: >-
    The public v1 deposit contains the README, manifest, code, and three raw .dta
    files used by the supplied province-, county-, firm-, and balance-analysis scripts.
    The package's county and firm files confirm 2000-2007 coverage; the README states
    that ASIF is restricted and that raw_firm_level_data.dta has anonymized firm IDs.
    This establishes a public paper-specific artifact, not unrestricted access to the
    underlying ASIF source or a verified external provider for the county panel.

provenance:
- source: https://www.sciencedirect.com/science/article/pii/S0094119026000562
  field_scope:
  - JUE paper identity, authors, DOI, publication timing, China PMC context, county-level panel role, and 2000-2007 study period
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://data.mendeley.com/datasets/x7t7fcwsxg/1
  field_scope:
  - Replication deposit identity, version 1, publication date, authors, public access route, CC BY 4.0 display, and description of code/replication data
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://data.mendeley.com/public-api/datasets/x7t7fcwsxg/files?folder_id=root&version=1
  field_scope:
  - Public file manifest showing Replication_Package.zip, its direct download route, completed status, and file size
  added: '2026-08-13'
  confidence: high
  verified: true
- source: Current Mendeley Data v1 record and public file API recheck (2026-09-27)
  field_scope:
  - version-1 identity, publication date, contributor names, public download control, and CC BY 4.0 display
  - current completed Replication_Package.zip endpoint, application/zip type, and 7,200,551-byte size
  added: '2026-09-27'
  confidence: high
  verified: true
- source: https://data.mendeley.com/public-files/datasets/x7t7fcwsxg/files/acec2ee0-d99f-4971-a8f0-329b65edd25a/file_downloaded
  field_scope:
  - README, output manifest, code files, raw .dta file names, and the package's explicit statement that the ASIF-derived firm file is anonymized because ASIF is restricted
  added: '2026-08-13'
  confidence: high
  verified: true

related_datasets:
- id: asif
  relation: often-confused-with
- id: china-stat-yearbook
  relation: complement
- id: china-land-transaction
  relation: complement
---

## Positioning in one sentence

This is a very recent (2026) and currently downloadable paper-specific asset for a China county/province/firm study: the live Mendeley v1 record offers its 7.2 MB replication ZIP, which contains the already documented 2000-2007 data files and Stata code. Its county-source lineage is not identified and its ASIF-derived firm IDs are intentionally anonymized.

## Select rules

- Prioritize it when the intended question needs the JUE paper's exact county-year fiscal/economic fields, province inequality construction, or anonymized firm productivity sample.
- Use China Statistical Yearbooks for a separately documented public regional panel, and use ASIF or another firm product only when original firm identifiers or a different period are essential.
- Do not call the public county file a raw yearbook extract or call the anonymized firm file a linkable ASIF panel without additional evidence.

## Get recipe

Open the Mendeley Data v1 record and download the current `Replication_Package.zip` (7,200,551 bytes at the latest check), then read README.pdf and output_manifest.csv and keep the package folders unchanged. Install the listed Stata commands, run code/0_setup.do and code/run_all.do (or a selected analysis script), and compare the generated outputs with the paper. If the question requires original firm linkage or a full source rerun, pursue the restricted ASIF route separately and document the missing concordance rather than replacing it with a guessed match.

## Connections and limitations

The safest internal keys are county/year and province/year; the firm ID is only a stable key within the released anonymized file. Administrative names, county boundaries, and price definitions must be checked before joining an external yearbook, land, weather, or outcome file. The package is a reproducible starting point for the paper's supplied artifact, not proof that the underlying county system or ASIF source can be independently reconstructed.
