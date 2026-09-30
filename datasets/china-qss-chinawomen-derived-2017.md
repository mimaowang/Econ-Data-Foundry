---
schema_version: 3
catalog_status: ready
id: china-qss-chinawomen-derived-2017
name: QSS chinawomen public county-cohort and crop derivative
aka:
- chinawomen.csv
- QSS Table 7.4 China sex-ratio and agricultural-crop data
- QSS chinawomen R dataset
- 中国县—出生年份性别比与农作物种植派生数据
provider: Kosuke Imai, Jeffrey Arnold and Tyler Simko; QSS supplementary repository and qss R package
china_related: true
domains:
- regional
- rural
- agriculture
- demographics
- gender
- education

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: >-
    Public QSS supplementary file UNCERTAINTY/chinawomen.csv and the same table
    packaged as qss::chinawomen (chinawomen.rda). It is a compact, paper-related
    derivative for QSS Table 7.4, not the original Qian (2008 QJE) census extracts
    or a complete replication package.
  availability: reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The CSV is directly downloadable from the public QSS GitHub repository, and the
    qss-package build script copies that CSV and reads it into an R data object using
    the documented column specification. The package documentation reports 51,766
    county-birth-year rows and nine variables, so a researcher can use the released
    derivative immediately for teaching, descriptive checks, or a carefully labelled
    extension of the Qian-related exercise.
  barrier: >-
    The public route does not establish the exact upstream census files, sample weights,
    Michigan GIS concordance, or all restrictions used in Qian's final QJE analysis.
    The numeric admin code has no public codebook or province/boundary crosswalk in the
    checked package, and the data license of the underlying source material is not
    separately documented beyond the GPL-2 package license.

unit_of_observation: County identifier by birth-cohort year row
structure: County-by-cohort cross-section with county crop measures repeated across cohorts
geo_granularity:
- county identifier
geography: >-
  Chinese counties represented by the package's numeric admin codes. The checked CSV
  has 1,648 unique admin values; the package does not publish a county-name, province,
  boundary-vintage, or complete-universe codebook.
time_span:
  start: '1962'
  end: '1990'
  last_confirmed_release: '2022-04-20'
  coverage_note: >-
    biryr is the birth/cohort year and ranges from 1962 through 1990 in the checked
    CSV. This is not an annual agricultural panel: teasown, orch, and cashcrop are
    county crop fields repeated or aligned to cohort rows, while post is a supplied
    reform-period indicator.
  last_checked: '2026-09-28'
frequency:
- cohort-year
sample_size: >-
  51,766 rows, 1,648 unique admin codes, 1962-1990 birth years; the checked CSV has
  2,684 rows with birpop recorded as NA. These counts are for the public derivative,
  not proof of Qian's original 1% census sample or its final estimation sample.
key_variables:
- admin: numeric county identifier with no accompanying public crosswalk
- biryr: birth/cohort year
- birpop: birth population in the cohort row
- han: Han share or Han indicator as represented in the derivative
- sex: proportion male in the birth cohort
- teasown: quantity of tea sown in the county
- orch: quantity of orchard-type crops planted
- cashcrop: quantity of cash crops planted
- post: indicator for introduction of the price-reform period

research_fit:
  best_for:
  - Reproducing the public QSS Table 7.4 exercise and inspecting the relationship
    between county crop measures, cohorts, and sex ratios with a small R/Python/Stata
    conversion step
  - A transparent, public starting table when the research question only needs the
    released county/cohort variables and can tolerate an undocumented geography key
  - Teaching or robustness demonstrations that explicitly label the file as a Qian-
    related derivative rather than an exact QJE replication
  choose_over:
  - Choose this public derivative over the unresolved Qian census candidate when an
    immediately downloadable demonstration table is more important than exact sample
    recovery.
  - Choose the China county population/agriculture GIS record when a documented
    historical boundary layer or broader 1990 county aggregates are needed; this file
    has no public GIS geometry or county-name crosswalk.
  - Choose the China Census record or an approved census product when individual,
    household, later-wave, or raw census variables are essential.
  not_good_for:
  - Exact reproduction of Qian's 2008 QJE estimates, weights, county restrictions, or
    matched 1990/1997 census/GIS pipeline
  - A national county panel, current regional data, agricultural output or price series,
    or a file with stable cross-study county identifiers
  - Treating post as a standalone policy or causal-variation record
  needs_join_for:
  - County names, province labels, boundaries, or GIS coordinates via a separately
    verified historical concordance
  - Original population-census education, occupation, household, or migration fields
  - RCRE/NFS household labor inputs and external crop prices if the research needs the
    mechanisms documented in Qian's paper
  variation_available:
  - post is an included data field marking a reform period; it is not a classification
    of an exogenous shock and no variation record is created here.
  topics:
  - rural China
  - county demography
  - sex ratios
  - agricultural specialization
  - crop geography
  - historical regional development

good_for:
- Public county-cohort descriptive analysis using the released nine-field table
- Reproducing the QSS teaching exercise with the original column names
- A clearly bounded input for a historical rural-China data demonstration
identification:
- No standalone causal-identification design is documented for this public derivative; use it as the released county-cohort table rather than as evidence of an encoded treatment assignment.
- post is a supplied reform-period field, not a verified policy-assignment, treatment, or comparison definition.
linkable_keys:
- admin (within-file only unless a documented crosswalk is obtained)
- biryr

joins:
- target: china-county-population-agriculture-gis-1990
  relation: complement
  keys:
  - Historical county identifier or documented name crosswalk
  - 1990 reference year
  method: >-
    Use the GIS product only after obtaining and checking a concordance between its
    county key and admin. Do not assume that a six-digit-looking admin code has the
    same meaning or boundary vintage as the GIS product.
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - County code after a verified historical concordance
  - Birth/cohort year where the approved census file supports it
  method: >-
    Treat the QSS table as a derived outcome/crop table and the census record as a
    separate source for additional fields or later waves. A shared topic or county
    label is not evidence of a lossless match.
  evidence_status: plausible
- target: china-agricultural-yearbook
  relation: complement
  keys:
  - County/province crosswalk
  - Reference year
  method: >-
    Use yearbook values only for independently documented agricultural controls and
    record any change in units or geography; they do not reveal the QSS file's source
    fields or turn it into an annual panel.
  evidence_status: plausible

access_routes:
- route: QSS original repository CSV
  access_status: available
  direct_url: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
  requirements:
  - A browser, Git, or direct raw-file download
  - Acceptance of the repository's GPL-2.0 terms for the QSS materials
  steps:
  - Open the QSS repository file and use its Raw/download route.
  - Preserve the header and the nine-column layout; the public file is about 2.5 MB.
  - Record the retrieval date and inspect missing values before analysis.
  - Keep the file labelled as a QSS derivative and do not claim that it is the exact
    Qian census extract.
  deliverable: >-
    51,766-row CSV with nine columns: admin, biryr, birpop, han, sex, teasown, orch,
    cashcrop, post.
  cost: free
  last_checked: '2026-09-28'
  caveat: The repository and package license the QSS materials under GPL-2/GPL-2.0, but the underlying census/agricultural source rights and redistribution conditions are not separately documented.
- route: qss R package on GitHub
  access_status: available
  direct_url: https://github.com/kosukeimai/qss-package
  requirements:
  - R and the remotes/devtools installation path, or a prebuilt qss package copy
  - Ability to use the package under GPL-2
  steps:
  - Install with remotes::install_github("kosukeimai/qss-package") or inspect the
    repository's data/chinawomen.rda member.
  - Load data(chinawomen, package = "qss") and compare the column names with the CSV.
  - Use the package only as a convenience wrapper; the build script shows that it
    copies the original QSS CSV and parses it with a column specification.
  deliverable: qss::chinawomen R data frame with the same nine fields and 51,766 rows.
  cost: free
  last_checked: '2026-09-28'
  caveat: The R package route does not add the missing county crosswalk or prove access to Qian's upstream sources.

access:
  url: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
  cost: free
  license: QSS repository and qss-package metadata display GPL-2/GPL-2.0; verify upstream-data rights before redistributing a derived product
  format:
  - csv
  - rda
  api: false
  how_to_get: Download the QSS CSV directly, or install qss-package and load qss::chinawomen; retain the source version and the derivative label.

caveats:
- QSS documentation cites Qian's QJE paper and labels this as the QSS Table 7.4
  exercise, but it does not say that the CSV is the exact paper-delivered analysis file.
- Qian's final paper describes a matched 1% 1997 Agricultural Census, 1% 1990
  Population Census, and Michigan GIS dataset at the county/birth-year level, with
  1,621 counties in 15 southern provinces and rural residents born 1962-1990. The
  public derivative has 1,648 admin codes and does not expose those restrictions or
  the GIS/census fields; preserve this difference.
- The file is cohort-oriented, not a repeated annual agriculture panel. Crop fields,
  post, and cohort rows should not be interpreted as a complete time series.
- The package has no public county-name/province/boundary codebook in the checked
  files. Do not infer geography from the numeric admin code.
- The source CSV contains missing birpop values; decide how to handle them and record
  any exclusions rather than silently dropping rows.

production:
  raw_sources:
  - name: QSS UNCERTAINTY/chinawomen.csv
    source_type: dataset
    role: Public derivative table used in the QSS Table 7.4 exercise
    access_route: Public QSS GitHub repository
    url: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
    coverage: 51,766 county-birth-year rows, 1962-1990 cohort years, nine fields
    last_checked: '2026-08-13'
  - name: Qian (2008) paper-described census/GIS inputs
    source_type: document
    role: Documents the upstream lineage and exact-paper boundary; it is not a file delivered by QSS
    access_route: Author-hosted QJE paper PDF
    url: https://www.kellogg.northwestern.edu/faculty/qian/resources/missing-women_qje_20080407_all.pdf
    coverage: 1% 1997 Agricultural Census, 1% 1990 Population Census, Michigan GIS, county/birth-year matching, 1,621 southern counties as described in the paper
    last_checked: '2026-08-13'
  acquisition_methods:
  - repository download
  - R package installation
  - CSV-to-R-data serialization
  sample_construction: >-
    The QSS package build script copies CSV files from the supplementary qss repository,
    applies the documented chinawomen column specification, and saves the resulting
    data frame as chinawomen.rda. The checked materials do not document the upstream
    census extraction, county matching, weighting, or GIS construction that produced
    the derivative CSV.
  pipeline_stages:
  - stage: collect
    inputs:
    - QSS UNCERTAINTY/chinawomen.csv
    method: Download the public CSV from the QSS supplementary repository.
    tools:
    - GitHub or raw-file download
    output: Public nine-column CSV
    evidence: QSS repository file and repository README
  - stage: parse
    inputs:
    - chinawomen.csv
    method: Read the header using the explicit column specification and parse integer/double fields; the build script skips the header and writes the R data object.
    tools:
    - R
    output: qss::chinawomen data frame and chinawomen.rda
    evidence: qss-package data-raw/build.R and data-raw/spec/chinawomen.R
  - stage: validate
    inputs:
    - Public CSV
    - Package documentation
    method: Compare row count, nine column names, numeric types, cohort-year range, and missing-value behavior. Do not use this check as proof of the exact Qian census sample.
    tools:
    - R or Python/pandas
    output: A reproducible derivative table with an explicit provenance warning
    evidence: qss-package documentation and direct CSV inspection; no reconstruction of the Qian upstream data was performed
  constructed_variables: []
  output:
    unit_of_observation: County identifier by cohort/birth year
    structure: Cross-sectional cohort table
    geography: Numeric county admin codes; names and boundaries unresolved
    time_span: 1962-1990 cohort years
    key_variables:
    - admin
    - biryr
    - birpop
    - han
    - sex
    - teasown
    - orch
    - cashcrop
    - post
    formats:
    - csv
    - rda
  reproducibility:
    level: medium
    starting_point: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
    code_available: true
    code_url: https://raw.githubusercontent.com/kosukeimai/qss-package/master/data-raw/build.R
    requirements:
    - Public GitHub access or a local clone
    - R only if the qss-package serialization route is desired
    - A separately documented county crosswalk for spatial joins
    blockers:
    - Exact upstream census/agricultural files and GIS concordance are not included
    - County codebook and boundary vintage are not identified
    - Exact match to Qian's final estimation sample and weights is not established
  compliance:
    terms_or_license: GPL-2/GPL-2.0 for QSS materials; upstream data rights require separate verification
    robots_or_rate_limits: Use GitHub's public file/repository route; do not scrape provider systems to infer missing upstream data
    personal_or_sensitive_data: Aggregate/cohort fields as documented; no individual-level records are identified in the public CSV
    redistribution: Follow GPL terms for the package and check source-data rights before redistributing a repackaged derivative
    review_needed: true

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: partial
  last_audited: '2026-09-28'

used_by:
- cite: 'Qian (2008), Missing Women and the Price of Tea in China: The Effect of Sex-Specific Earnings on Sex Imbalance'
  doi: https://doi.org/10.1162/qjec.2008.123.3.1251
  journal: QJE
  year: 2008
  dataset_role: Related public derivative referenced by the QSS exercise; not certified as the exact QJE analysis file
  evidence_type: teaching-derivative
  evidence_url: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
  data_note: >-
    QSS documentation explicitly references Qian's paper and describes chinawomen as
    demographic and agricultural crop data for individual Chinese counties. The Qian
    paper itself documents a larger/more restricted matched census-GIS construction;
    the QSS file is therefore a usable public derivative, not evidence that the original
    1% census extract or the complete QJE replication package is public.

provenance:
- source: https://www.kellogg.northwestern.edu/faculty/qian/resources/missing-women_qje_20080407_all.pdf
  field_scope:
  - QJE paper identity and DOI context
  - 1% 1997 Agricultural Census, 1% 1990 Population Census and Michigan GIS inputs
  - county/birth-year matching, 1,621 counties in 15 southern provinces, rural 1962-1990 sample boundary
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
  field_scope:
  - Public CSV identity and download route
  - header, nine columns, and repository file boundary
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://raw.githubusercontent.com/kosukeimai/qss/master/UNCERTAINTY/chinawomen.csv
  field_scope:
  - Current direct-download route returned HTTP 200 on 2026-09-28
  - Current CSV content length was 2,618,228 bytes and retains the documented nine-field header
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://raw.githubusercontent.com/kosukeimai/qss-package/master/DESCRIPTION
  field_scope:
  - Current package metadata identifies qss as packaged QSS supplementary material and states GPL-2
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://raw.githubusercontent.com/kosukeimai/qss-package/master/data-raw/build.R
  field_scope:
  - Current build script copies QSS CSV files and serializes them as package data objects
  - The chinawomen column specification remains available in the same public repository
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://rdrr.io/github/kosukeimai/qss-data/man/chinawomen.html
  field_scope:
  - 51,766-row, nine-variable documentation
  - variable descriptions and explicit Qian/QSS reference
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://raw.githubusercontent.com/kosukeimai/qss-package/master/data-raw/build.R
  field_scope:
  - CSV-copy and CSV-to-RDA packaging steps
  - use of the column specification and public package output
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://raw.githubusercontent.com/kosukeimai/qss-package/master/DESCRIPTION
  field_scope:
  - qss package authors, supplementary-material identity and GPL-2 license
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://github.com/kosukeimai/qss/blob/master/UNCERTAINTY/chinawomen.csv
  field_scope:
  - local read-only inspection of 51,766 rows, 1,648 unique admin values, 1962-1990 cohort range, 2,684 missing birpop values, and file size about 2.5 MB
  added: '2026-08-13'
  confidence: high
  verified: true

related_datasets:
- id: china-county-population-agriculture-gis-1990
  relation: complement
- id: china-census
  relation: complement
- id: china-agricultural-yearbook
  relation: complement
---

## Positioning in one sentence

This is a small, public, QSS-packaged China county-by-cohort table related to Qian's QJE study: it is immediately usable for the nine released variables through a current direct CSV route, but it is not the original 1% census/GIS match and cannot be used as an exact QJE replication without additional evidence.

## Select rules

- Use it when the question needs the public QSS exercise table and can work with numeric county IDs, 1962-1990 cohort rows, and the nine documented fields.
- Use the unresolved Qian agricultural-census candidate when exact sample, weights, GIS linkage, or the original paper's full analysis is the goal; use the 1990 county/GIS product when a public historical spatial key is more important.
- Never silently upgrade this derivative into the 1997 Agricultural Census, 1990 Population Census, or Qian's complete matched dataset.

## Get recipe

Download `UNCERTAINTY/chinawomen.csv` from the QSS repository, retain the header, inspect missing `birpop`, and keep the file labelled as a derived teaching asset. If an R object is more convenient, install `qss-package` and load `qss::chinawomen`; the package build script simply copies and parses the CSV. Obtain a separate, documented county crosswalk before any spatial join, and do not claim exact QJE replication from the public file.

## Connections and limitations

The only safe internal key is `admin` together with `biryr`; `admin` has no verified crosswalk in the package. Joining to the 1990 county/GIS record, census waves, or yearbooks requires a historical concordance and a check of county boundaries. The data are useful precisely because the derivative is public and compact, while the unknown source lineage, weighting, and paper-sample restrictions remain visible instead of being filled by assumption.
