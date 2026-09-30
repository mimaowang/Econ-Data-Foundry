---
schema_version: 3
catalog_status: ready
id: china-aer-squeaky-wheel-citizen-appeals-2020
name: Buntaine et al. China CEMS and citizen-appeals replication bundle (AER 2024)
aka:
- Does the Squeaky Wheel Get More Grease? replication data
- China pollution appeals experiment data
- CEMS-citizen appeals paper bundle
- 中国污染企业公民申诉数据
provider: >-
  Michael Buntaine, Meredith Fowlie/Edward Greenstone, and coauthors, distributed as a
  paper-specific openICPSR deposit; the project names 2020 CEMS, 12369 Environmental
  Appeals Center, and State Administration for Market Regulation (SAMR) inputs.
china_related: true
domains:
- environment
- firm
- urban
- regional
- governance

data_pathway:
  mode: hybrid
  origin: researcher-constructed
  target_artifact: >-
    openICPSR project 194521 V1: a public paper-specific bundle containing README and
    Stata code plus 26 Stata data files such as citizen_data.dta, CEMS-derived
    emissions/violation files, appeal files, penalty files, industry data, and
    promotion/Weibo-related files.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The deposited bundle is directly obtainable from openICPSR and is the practical
    starting point for reproducing the AER paper's firm-level analyses. It is not a
    general public release of the underlying national CEMS, 12369, or SAMR systems:
    the package is researcher-assembled, file-specific, and distributed as received.
    Public code and data therefore make the paper-specific artifact usable, while
    independent reconstruction of every upstream input remains conditional. The
    current DataCite record confirms that ICPSR DOI 10.3886/E194521V1 is a findable
    v1 dataset for this title and points to the same openICPSR project.
  barrier: >-
    The released paper-specific bundle is an acquisition route, but its current
    depositor terms, field definitions, and original extraction route for each
    upstream source remain separate questions. Several files are hundreds of megabytes
    or about a gigabyte, so storage and Stata are practical requirements; ICPSR states
    that depositor files are not independently reviewed.

unit_of_observation: Firm-level research records; CEMS and derived files have file-specific row grain
structure: Paper-specific mixed firm-level panel and event/record tables
geo_granularity:
- firm
- monitoring point
- prefecture/city where retained
- province
geography: >-
  Mainland China. The project metadata describes a nationwide universe of 24,620
  polluting firms required to install CEMS by 2020-01-01; the geographic detail and
  row coverage vary by deposited file.
time_span:
  start: '2020-05-06'
  end: '2020-12-31'
  last_confirmed_release: '2023-12-11'
  coverage_note: >-
    The project reports the paper period as 2020-05-06 through 2020-12-31 and the
    collection period as 2021-01-01 through 2021-03-31. CEMS inputs are labelled 2020;
    pre-period, appeal, penalty, and derived files can have narrower or different
    windows, which must be read from the README and code.
  last_checked: '2026-09-28'
frequency:
- hourly CEMS measurements
- event-level appeals and violations
- firm-level derived records
sample_size: >-
  Project metadata reports 24,620 polluting firms in the CEMS universe. The 26
  deposited files contain different numbers of monitor, appeal, penalty, and derived
  records; their row counts are not interchangeable with the firm universe.
key_variables:
- Firm name and firm identifiers where retained
- CEMS monitor point, pollutant/item, measurement method and frequency
- Lower and upper limits, monitor value, and compliance status
- Violation, penalty, and pre-violation indicators
- Public and private citizen-appeal records and appeal-channel fields
- Industry and prefecture/city fields where retained
- Promotion, Weibo, and derived prefecture-level variables in the named files

research_fit:
  best_for:
  - Firm-level environmental compliance and pollution outcomes linked to citizen appeals
  - Reproducing the AER paper's public/private appeal and environmental-governance data pipeline
  - Studying how high-frequency CEMS measurements become firm-level violation or emissions records
  choose_over:
  - Choose this bundle over the general china-firm-pollution record when the question needs the paper-specific CEMS/appeal linkage, its 2020 files, or the public Stata replication route.
  - Choose china-air-quality-monitoring when the outcome is ambient city or station exposure rather than a polluting firm's own compliance record.
  - Choose the general firm-pollution record for a longer or independently sourced enterprise-emissions panel; the two products are not interchangeable.
  not_good_for:
  - A current, continuously updated national CEMS release or a guaranteed complete historical CEMS panel
  - Personal exposure, city-wide ambient concentration, or outcomes for firms outside the CEMS universe
  - Treating the paper's appeal arms or prefecture proportions as a separate policy/variation database
  needs_join_for:
  - Firm productivity, employment, ownership, or financial outcomes from ASIF or another firm panel
  - City or prefecture economic outcomes, weather, health, or ambient pollution measures
  - A longer firm history or a boundary-harmonized city panel
  variation_available:
  - Public/private appeal-channel fields and prefecture-level treatment proportions are observed variables in the paper bundle; they are data dimensions only, while treatment interpretation belongs to the paper and the separate variation repository.
  topics:
  - environmental governance
  - firm pollution
  - citizen participation
  - CEMS monitoring
  - China regional environmental economics

good_for:
- Firm-level pollution compliance and emissions research using the paper's 2020 data artifact
- Linking environmental appeals or violations to firm and city characteristics after checking file-specific keys
- Reproducing the published tables and figures from the supplied Stata code
identification:
- This is a paper-specific firm-monitoring and citizen-appeals data/code bundle, not a stand-alone causal-variation record. It supports reproducing the documented study and inspecting its observed appeal/compliance fields; any new causal design requires separate identification assessment.
linkable_keys:
- Firm name or retained firm identifier
- Monitor point identifier
- Prefecture/city name or code where present
- Date/time
- Pollutant/item code
- Industry code where present

joins:
- target: china-firm-pollution
  relation: complement
  keys:
  - Firm name or identifier
  - Industry code
  - Address/city
  - Year
  method: Normalize names and administrative codes, then inspect the exact file-level definitions before matching; do not assume that two pollution products share a firm universe.
  evidence_status: plausible
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - City or prefecture code
  - Date
  method: Aggregate or align firm records to the city/date level only after checking whether the deposited file retains a stable location and time field.
  evidence_status: plausible
- target: china-firm-registry
  relation: complement
  keys:
  - Firm name
  - Legal registration identifier where retained
  - Registered address
  method: Use deterministic identifiers if present and otherwise a documented name/address match; the SAMR input named by the project is not evidence that the current registry record is identical.
  evidence_status: plausible

access_routes:
- route: openICPSR project 194521 V1
  access_status: available-with-conditions
  direct_url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
  requirements:
  - An openICPSR account or the repository's current terms/download flow
  - Stata and enough local storage for files ranging from kilobytes to about one gigabyte
  - Reading the depositor README and code before interpreting any file
  steps:
  - Open project 194521 V1 and record the citation and version.
  - Read README.pdf and inspect the Data_and_Code_2023/code and data folders.
  - Download only the files needed for the question, beginning with the relevant data dictionary or do-file.
  - Check the current license/terms and the source boundary before redistributing or joining files.
  - Run Master.do only after fixing paths and checking the required Stata commands.
  deliverable: 26 depositor-provided Stata data files plus README and Stata do-files; not a new release of the underlying CEMS, 12369, or SAMR systems.
  cost: free
  last_checked: '2026-09-28'
  caveat: The project pages state that the files are distributed as received and have not been independently reviewed or harmonized by ICPSR.
- route: underlying CEMS/appeals/SAMR source reconstruction
  access_status: needs-verification
  direct_url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
  requirements:
  - The deposited README/code and any author or source-provider permission required for the original inputs
  - Separate review of provider terms and field-level coverage
  steps:
  - Treat the openICPSR bundle as the specification and starting point, not proof of a raw-source download.
  - Identify which source-level fields are actually present in each deposited file.
  - Contact the authors or the named provider only for a missing component, and record the delivered version separately.
  deliverable: A source-specific input or a documented reason it cannot be obtained; it must not be silently substituted for the paper bundle.
  cost: mixed
  last_checked: '2026-08-12'
  caveat: No public raw CEMS/12369/SAMR access route was inferred from the project description alone.

access:
  url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
  cost: free
  license: OpenICPSR/depositor terms for the public bundle; rights and redistribution conditions of the named upstream sources may differ.
  format:
  - dta
  - do
  - pdf
  api: false
  how_to_get: Open project 194521 V1, read the README and current terms, inspect the code/data folders, and download the required files with their version recorded.

caveats:
- A public replication package is not the same thing as a complete public CEMS, 12369, or SAMR database.
- File names and sizes establish the deposited artifact, but exact labels, joins, thresholds, and row grain require reading the README and do-files.
- CEMS monitor records, citizen appeals, penalties, and derived outcomes are distinct files; do not merge them by name alone.
- The public package may be large and computationally inconvenient; a successful download does not guarantee an independent rerun without the same Stata environment and paths.
- Underlying provider terms and any sensitive or identifying fields in appeal/firm records must be checked before sharing or creating a derivative.

production:
  raw_sources:
  - name: 2020 Continuous Emissions Monitoring System (CEMS) records
    source_type: dataset
    role: Hourly emissions, limits, monitor values, and compliance inputs for the paper's firm pollution outcomes
    access_route: Deposited paper bundle; original provider route is not confirmed by the checked pages
    url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
    coverage: 24,620 polluting firms required to install CEMS by 2020-01-01 according to project metadata; file-specific coverage remains to be read from labels
    last_checked: '2026-08-12'
  - name: 12369 Environmental Appeals Center records (2020)
    source_type: dataset
    role: Citizen appeal observations and private/public appeal-channel inputs named by the project
    access_route: Deposited paper bundle; the original center's export or application route is not confirmed
    url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
    coverage: 2020 paper period and file-specific appeal records
    last_checked: '2026-08-12'
  - name: State Administration for Market Regulation (SAMR) firm records
    source_type: dataset
    role: Firm identity or registration information named as a project source
    access_route: Deposited paper bundle; current raw SAMR access is separate and unresolved
    url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
    coverage: File-specific firms in the paper package; exact fields and vintage require code/README inspection
    last_checked: '2026-08-12'
  acquisition_methods:
  - repository download
  - administrative-record assembly
  - web scraping as listed in the project metadata
  - paper-specific field-record collection
  sample_construction: >-
    The authors assembled firm pollution, appeal, penalty, industry, and related records
    for the 2020 study period. The project metadata supplies the CEMS universe and named
    sources; exact exclusions, matching rules, and file-level samples are encoded in the
    deposited README and Stata code rather than inferred here.
  pipeline_stages:
  - stage: collect
    inputs:
    - 2020 CEMS records
    - 12369 Environmental Appeals Center records
    - SAMR firm records
    method: Assemble the named administrative and paper-collected records; project metadata lists web scraping and other collection modes.
    tools:
    - Provider systems and author collection scripts (exact implementation not confirmed)
    output: Source and paper-specific firm/appeal records represented in the deposited files
    evidence: openICPSR project metadata and its named data sources/collection modes
  - stage: clean
    inputs:
    - Deposited source and intermediate Stata files
    method: Apply the authors' supplied Stata preparation code; exact cleaning and matching rules must be read from the scripts.
    tools:
    - Stata
    output: Cleaned and derived .dta files in Data_and_Code_2023/data
    evidence: openICPSR code folder listing 0_Setup.do, 1_Figures.do, 2_Tables.do, and Master.do
  - stage: validate
    inputs:
    - Deposited data files
    - Supplied Stata code
    method: Run the supplied master/table/figure scripts after checking paths and dependencies, then compare generated outputs with the published paper.
    tools:
    - Stata
    output: Reproduction tables/figures and a record of any missing inputs or discrepancies
    evidence: openICPSR project code folder and AER paper/replication citation
  constructed_variables:
  - name: paper-specific violation and compliance outcomes
    concept: Derived firm pollution/violation measures combining CEMS readings with limits and related records
    source_fields:
    - Monitor value
    - Lower and upper limits
    - Compliance status
    - Violation and penalty files
    method: As implemented in the deposited Stata code; thresholds, windows, and exclusions require code-level verification.
    validation: Compare code outputs and sample counts with the paper's tables and appendix.
    limitations: These are paper-specific derived fields, not a universal environmental-violation standard or a complete CEMS release.
  output:
    unit_of_observation: Firm-level records with file-specific monitor, appeal, event, and derived row grain
    structure: Mixed firm-level panel and event/record tables
    geography: Mainland China; nationwide CEMS universe described in project metadata
    time_span: 2020 paper period, with file-specific pre-period and event windows
    key_variables:
    - CEMS emissions and compliance fields
    - Appeal channels and appeal outcomes
    - Violation, penalty, industry, and location fields where present
    formats:
    - dta
    - do
    - pdf
  reproducibility:
    level: medium
    starting_point: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
    code_available: true
    code_url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view?path=%2Fopenicpsr%2F194521%2Ffcr%3Aversions%2FV1%2FData_and_Code_2023%2Fcode&type=folder
    requirements:
    - Current openICPSR terms/account and the deposited version
    - Stata and enough storage for the largest .dta files
    - README/code reading to resolve paths, packages, and file-specific labels
    - Separate permission or source access if an upstream input is missing from the deposit
    blockers:
    - Exact raw-source extraction, rights, and field lineage are not closed by the repository metadata.
    - ICPSR states that depositor files are distributed as received and not independently reviewed.
    - File-level row counts, stable identifiers, and complete join keys require inspection of the files/code.
  compliance:
    terms_or_license: Check the openICPSR depositor terms and any source-provider conditions before reuse or redistribution.
    robots_or_rate_limits: Use the repository's download route; do not scrape openICPSR to reconstruct missing files.
    personal_or_sensitive_data: Inspect the documentation for any identifying fields in citizen-appeal or firm records before sharing.
    redistribution: Do not redistribute the package or derived joins until repository and upstream-source terms are confirmed.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-12'

used_by:
- cite: 'Buntaine, Greenstone, He, Liu, Wang & Zhang (2024), Does the Squeaky Wheel Get More Grease? The Direct and Indirect Effects of Citizen Participation on Environmental Governance in China'
  doi: https://doi.org/10.1257/aer.20221215
  journal: AER
  year: 2024
  dataset_role: Main firm-level CEMS, pollution-violation, and citizen-appeal inputs for the paper's China environmental-governance analyses
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
  data_note: >-
    The project metadata describes a nationwide field experiment involving 24,620
    polluting firms required to install CEMS, covering the 2020 paper period, and names
    CEMS, 12369 Environmental Appeals Center, and SAMR inputs. Its public V1 deposit
    contains code and 26 Stata files, but that public package is a paper-specific
    researcher-assembled artifact and does not by itself prove access to the raw
    provider systems or reproduce every upstream extraction step.

provenance:
- source: https://doi.org/10.1257/aer.20221215
  field_scope:
  - AER paper identity
  - publication year and DOI
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view
  field_scope:
  - project identity and citation
  - 2020 period and collection dates
  - 24,620-firm universe
  - named CEMS/12369/SAMR sources
  - unit of observation and collection modes
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view?path=%2Fopenicpsr%2F194521%2Ffcr%3Aversions%2FV1%2FData_and_Code_2023%2Fdata&type=folder
  field_scope:
  - public data-folder route
  - 26-file manifest and file-size range
  - depositor-provided Stata artifact boundary
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/194521/version/V1/view?path=%2Fopenicpsr%2F194521%2Ffcr%3Aversions%2FV1%2FData_and_Code_2023%2Fcode&type=folder
  field_scope:
  - README/code route
  - 0_Setup.do, 1_Figures.do, 2_Tables.do, and Master.do metadata
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.nber.org/system/files/working_papers/w30539/w30539.pdf
  field_scope:
  - CEMS nationwide scope
  - 24,620 major polluting plants and hourly monitoring context
  - paper field-experiment context
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://epic.uchicago.cn/wp-content/uploads/sites/2/2022/10/MG-China-Pollution-Appeals_Research-Summary-2.pdf
  field_scope:
  - CEMS example fields
  - public/private citizen-appeal context
  - environmental-governance data role
  added: '2026-08-12'
  confidence: high
  verified: true
- source: DataCite API record 10.3886/E194521V1, queried 2026-09-28
  field_scope:
  - current findable v1 ICPSR dataset identity and openICPSR project route
  - paper title, China geography, 2020 collection windows, and 24,620-firm CEMS sample description
  - does not establish current file-download terms, a deposit license, or access to the underlying CEMS, appeals, or SAMR systems
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-firm-pollution
  relation: complement
- id: china-air-quality-monitoring
  relation: often-confused-with
- id: china-firm-registry
  relation: complement
---

## Positioning in one sentence

This is a public, paper-specific bundle of Chinese firm-monitoring, pollution-violation, and citizen-appeal files used by the 2024 AER study. It is valuable because the code and data are obtainable together, but it should not be mistaken for a complete current CEMS or raw 12369/SAMR release.

## Select rules

- Prioritize it when the idea needs the AER paper's 2020 firm-level CEMS and appeal linkage or a starting point for reproducing its tables.
- Switch to china-firm-pollution for a longer, independently sourced enterprise-emissions panel, and to china-air-quality-monitoring for ambient city/station exposure.
- Before joining anything, inspect the actual file labels and code: a shared firm name or city name is not proof of a stable identifier or common universe.

## Get recipe

Open the openICPSR V1 project, record the version, read the README and current terms, inspect the code and data folders, and download only the relevant files. Allocate enough storage for the large Stata files, repair paths in the supplied scripts, and compare generated outputs with the paper before treating a derived field as a reusable variable. If a raw CEMS, appeal, or SAMR component is missing, record that as a separate source-access problem rather than silently replacing the paper artifact.

## Connections and Limitations

Firm-name, address, city, date, and pollutant keys are file-specific and may require normalization or a documented fuzzy match. Aggregating to city-day outcomes can make this bundle useful beside ambient monitoring data, but aggregation changes the estimand and must be recorded. The public package's existence establishes a reproducible starting artifact, not the current availability, licensing, or completeness of the upstream administrative systems.
