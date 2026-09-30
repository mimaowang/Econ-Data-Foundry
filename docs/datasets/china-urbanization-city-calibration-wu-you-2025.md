---
schema_version: 3
catalog_status: ready
id: china-urbanization-city-calibration-wu-you-2025
name: Wu–You China urbanization city-calibration replication asset
aka:
- Should Governments Promote or Restrain Urbanization replication package
- Wu & You (2025) JIE urbanization replication bundle
- 中国城市化模型地级市校准数据
provider: Wenbin Wu and Wei You; upstream inputs named by the authors include Chinese census, statistical, spatial, fiscal, and price sources
china_related: true
domains:
- urban
- regional
- migration
- labor
- spatial

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: Public Google Drive ZIP containing the paper's raw, intermediate, and final files plus Stata/Matlab programs; the released model-input files include prefecture-level variables and bilateral migration flows
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The author-linked package is a usable paper-specific starting point for the China urbanization calibration. It contains public prepared inputs, intermediate files, outputs, and code, but the confidential census and urban-household-survey microdata named by the programs are omitted and must be obtained separately before rebuilding every stage.
  barrier: The archive is about 1.46GB and its package licence and redistribution terms were not displayed in the checked pages. Full reconstruction also requires confidential NBS census/UHS files, Stata and Matlab, and the paper's exact boundary and code concordances.

unit_of_observation: Prefecture-year model inputs, bilateral prefecture-pair migration flows by skill, and paper-specific intermediate or survey-derived files in separate package members
structure: paper-specific urbanization-calibration replication bundle
geo_granularity:
- prefecture-level city
- prefecture pair
- county or province in source-specific files
geography: Mainland China; the README identifies 340 prefectures in the final prefecture-level model-input file, while exact boundary and code vintages remain file-specific
time_span:
  start: '1990'
  end: '2070'
  last_confirmed_release: '2025-03-22'
  coverage_note: The paper's observed calibration uses prefecture data centred on 2000-2010 and tests 2020 out of sample. The README says the final Matlab baseline represents the actual economy from 2000 to 2010 and expectations for 2015-2070 in five-year periods; the future periods are model expectations, not observed survey years. The package also contains 1990 migration-destination inputs and 2000/2010 census-related files.
  last_checked: '2026-09-28'
frequency:
- five-year periods
- panel
- bilateral flow
sample_size: 340 prefectures in data_pref_levels.csv; the exact dimensions of data_mig_flows.csv and file-level samples require reading the downloaded CSVs
key_variables:
- Prefecture-level population, GDP, housing, land, fiscal-transfer, and skill-related inputs as represented in the released files
- Origin-destination migration flows by skill
- Prefecture and county codes or names where present
- Actual and expected population, GDP, migrant population, and other model-state variables in Matlab outputs
- Survey-derived housing-expenditure and demographic inputs where the public package includes them

research_fit:
  best_for:
  - Reusing the authors' prepared prefecture-level inputs and bilateral migration flows for quantitative urbanization, internal-migration, city-size, hukou, or spatial-equilibrium research
  - Starting from a documented 340-prefecture paper-compatible bundle when the question needs the same model-input boundary rather than a generic current city panel
  choose_over:
  - Choose this over raw census access when the intended work needs the paper's prepared city-level calibration files and migration-flow definition.
  - Choose the China Census record when individual microdata or a different census wave and outcome definition is required; this bundle does not replace the NBS application.
  - Choose the China Statistical Yearbook record when only annual published regional controls are needed and no paper-specific migration or model reconstruction is required.
  not_good_for:
  - A general unrestricted individual census or household-survey microdata release
  - A current city-year panel with guaranteed modern boundaries, a complete variable dictionary, or all raw source files
  - Treating the model's counterfactual policy outputs as observed data or as evidence of causal identification
  needs_join_for:
  - Individual, household, firm, land, weather, or current city outcomes not present in the released model inputs
  - Approved NBS census/UHS microdata if the researcher must recreate the omitted micro-level aggregation
  - A documented prefecture concordance when joining to a different administrative vintage
  variation_available:
  - Migration, urbanization, and policy-simulation dimensions are data or model dimensions only; no causal or exogenous-shock classification is recorded here.
  topics:
  - urbanization
  - internal migration
  - city size
  - hukou
  - spatial equilibrium
  - regional development

good_for:
- Reusing the released prefecture-level inputs and bilateral migration-flow files behind Wu & You's quantitative China urbanization exercise
- Reproducing the public Stata-to-Matlab preparation path when the required confidential inputs and software are available
- Building carefully documented joins between the paper's prefecture units and other regional or urban datasets
identification:
- Direct paper-specific replication asset: the authors' public ZIP combines prepared prefecture-level calibration inputs, bilateral migration-flow inputs, code, and model outputs; it is not a release of the raw census or Urban Household Survey microdata named by some programs.
linkable_keys:
- Prefecture code or normalized prefecture name as stored in the package
- Origin prefecture and destination prefecture
- Year or five-year model period
- Skill group
- County or province code where a source-specific file supplies one

joins:
- target: china-census
  relation: complement
  keys:
  - Prefecture or county identifier
  - Census year or five-year reference period
  method: Preserve the paper's boundary and code vintage, then align the approved census wave and migration definitions before joining; do not assume the public derived flow file is a raw census release.
  evidence_status: literature-used
- target: china-stat-yearbook
  relation: complement
  keys:
  - Prefecture or city identifier
  - Year
  method: Use the yearbook only for variables and definitions that match the paper's published regional controls; reconcile administrative names, units, and price bases before merging.
  evidence_status: literature-used

access_routes:
- route: Author-linked Google Drive replication package
  access_status: available-with-conditions
  direct_url: https://drive.google.com/file/d/1fcsr9IOBv_i7VG_PC47cOy-oicrulP8A/view?usp=drive_link
  requirements:
  - Download approximately 1.46GB only if the intended artifact justifies the storage and bandwidth.
  - Read readme.txt before opening or running the numbered Stata and Matlab programs.
  - Keep the public package separate from the confidential microdata it explicitly omits.
  steps:
  - Open the author or publisher route and confirm the current Google Drive file and version.
  - Read the package README and inspect Data, Stata, Matlab, and Results folders before selecting files.
  - Start with Matlab/1_baseline/data_pref_levels.csv and Matlab/1_baseline/data_mig_flows.csv only after checking the package's code and variable labels; the README places the final CSVs under that folder.
  - If full reproduction is needed, obtain the omitted NBS census and UHS files through the official application route and run the numbered Stata stages before the numbered Matlab stages.
  deliverable: Public raw, intermediate, and final files, Stata/Matlab code, and paper-specific outputs; not the confidential micro2000/micro2005/micro2010/micro2015 census files or UHS_2006h/UHS_2006p/UHS2007 individual files.
  cost: mixed
  last_checked: '2026-09-28'
  caveat: The current public Drive route shows a virus-scan confirmation page for Data and Programs for Publication.zip (1.4G) and offers Download anyway without a login prompt. This confirms the acquisition start, not a package licence, permission to redistribute every included upstream file, or a full original-source rerun.
- route: National Bureau of Statistics Microdata Laboratory application
  access_status: by-application
  direct_url: https://microdata.stats.gov.cn/
  requirements:
  - Submit a request for the specific census and urban-household-survey waves and variables needed for the intended reconstruction.
  - Follow NBS review, confidentiality, and use conditions; approval and fees, if any, are not established by this record.
  steps:
  - Identify the missing micro2000, micro2005, micro2010, micro2015 and UHS files required by the selected code path.
  - Apply through the official NBS microdata route and keep the approved files outside this repository.
  - Re-run only the documented processing stages needed for the target artifact and compare with the released outputs.
  deliverable: Approved confidential microdata, if granted; the route does not promise redistribution or public release.
  cost: by-application
  last_checked: '2026-08-12'
  caveat: The README identifies the NBS route but does not establish approval time, fees, exact wave availability, or a universal code concordance.

access:
  url: https://drive.google.com/file/d/1fcsr9IOBv_i7VG_PC47cOy-oicrulP8A/view?usp=drive_link
  cost: free
  license: Package-level licence and redistribution terms were not displayed in the checked version; follow Google Drive, upstream-source, NBS, and author terms.
  format:
  - zip
  - csv
  - dta
  - xlsx
  - mat
  - m
  - do
  - txt
  api: false
  how_to_get: Use the author-linked Google Drive package as the public starting point, read its README, and apply separately to NBS for omitted confidential files. Record the exact downloaded version, file names, and rights before sharing any derivative.

caveats:
- This is a paper-specific calibration and replication bundle, not a neutral national city database or a current administrative panel.
- The public ZIP contains many prepared and intermediate files, but the README explicitly says that the census microdata and UHS individual files used by some programs are confidential and omitted.
- The 2015-2070 Matlab baseline is an expectation or counterfactual model object, not observed population or migration data; do not mix it with observed coverage in a new panel.
- The exact variable dictionary, prefecture boundary/code vintage, public-file licence, and file-level upstream provenance still require inspection of the selected downloaded members.
- The bundle describes data inputs and model outputs only; claims about treatment, exogeneity, or policy identification belong in the separate variation project.

production:
  raw_sources:
  - name: Chinese Population Census and mini-census microdata
    source_type: dataset
    role: Individual-level population, migration, registration, and demographic inputs used by the paper's aggregation programs
    access_route: National Bureau of Statistics Microdata Laboratory application; confidential files are omitted from the public ZIP
    url: https://microdata.stats.gov.cn/
    coverage: Programs name micro2000, micro2005, micro2010, and micro2015; exact approved variables and wave availability are access-dependent
    last_checked: '2026-08-12'
  - name: Urban Household Survey files
    source_type: dataset
    role: Housing-expenditure and household inputs used by selected paper programs
    access_route: Confidential source named in the replication README; current access route and permission conditions require separate verification
    url: https://microdata.stats.gov.cn/
    coverage: Programs name UHS_2006h, UHS_2006p, and UHS2007; the public ZIP omits the individual files
    last_checked: '2026-08-12'
  - name: Public statistical, spatial, fiscal, and price inputs named by the paper
    source_type: mixed-public-sources
    role: Aggregate population, GDP, housing, land-use, terrain, fiscal-transfer, price, and other prefecture-level inputs used in the released preparation files
    access_route: Public members of the author-linked replication ZIP; individual upstream provider routes and rights are file-specific
    url: https://drive.google.com/file/d/1fcsr9IOBv_i7VG_PC47cOy-oicrulP8A/view?usp=drive_link
    coverage: Package members include census aggregates, fiscal_transfer_07.xlsx, land and terrain-related files, housing and population intermediates, and other paper-specific inputs; exact upstream coverage must be read from each file's documentation
    last_checked: '2026-08-12'
  acquisition_methods:
  - download
  - apply
  - clean
  - match
  - aggregate
  - model
  sample_construction: The public README documents a numbered Stata preparation sequence followed by numbered Matlab baseline, counterfactual, and robustness stages. It identifies the final 340-prefecture inputs and bilateral migration-flow CSVs, but does not by itself certify every field transformation or boundary concordance.
  pipeline_stages:
  - stage: collect
    inputs:
    - Author-linked public ZIP
    - NBS census and UHS files when approved
    tools:
    - Google Drive download
    - NBS application route
    method: Keep public package members and confidential upstream inputs separate; do not redistribute omitted microdata.
    output: Raw and supplied intermediate files in the package, with confidential inputs obtained outside the repository when permitted
    evidence: Replication README read from the public ZIP
  - stage: clean
    inputs:
    - Census and UHS inputs
    - Public aggregate, spatial, fiscal, price, and survey files
    tools:
    - Stata
    method: Execute the numbered Stata/Estimation and related preparation programs in the documented order; exact program-level transformations remain file-specific.
    output: Processed prefecture and migration inputs, including data_pref_levels.csv and data_mig_flows.csv
    evidence: Replication README and public ZIP manifest
  - stage: model
    inputs:
    - data_pref_levels.csv
    - data_mig_flows.csv
    tools:
    - Matlab
    method: Execute the numbered Matlab/1_baseline, 2_counterfactual, and 3_robustness programs as needed for the intended artifact.
    output: Baseline_economy_all_years.mat and paper-specific quantitative outputs for observed and expected periods
    evidence: Replication README and public ZIP manifest
  - stage: other
    inputs:
    - Matlab outputs
    - Stata table and figure programs
    tools:
    - Stata
    - Matlab
    method: Run the documented table, figure, and counterfactual programs only after verifying the public/confidential input boundary.
    output: Paper tables, figures, and derived model files
    evidence: Replication README
  constructed_variables:
  - name: Prefecture-level calibration inputs
    concept: Prepared prefecture-year variables used by the quantitative urbanization model
    source_fields:
    - Census and survey aggregates
    - Public statistical, spatial, fiscal, and price inputs
    method: Paper-specific Stata cleaning, matching, and aggregation; exact field transformations must be read from the selected do-files.
    validation: Compare released CSV headers, observations, and code outputs with the README's 340-prefecture description.
    limitations: Boundary vintage, missing confidential inputs, and file-specific source rights limit general reuse.
  - name: Bilateral migration-flow inputs by skill
    concept: Origin-destination prefecture flows used by the model
    source_fields:
    - Census migration and skill fields
    method: Paper-specific aggregation and matching; the public CSV is a prepared analysis input, not a raw census table.
    validation: Compare origin/destination dimensions and skill labels with the associated Stata/Matlab code before joining.
    limitations: Exact flow definition, years, codes, and treatment of missing or confidential source records require file-level inspection.
  validation:
  - Confirm the README, ZIP name, archive size, and 666-entry manifest before downloading or using selected members.
  - Preserve the public-versus-confidential boundary and do not claim a full rerun unless the omitted files and software are available.
  - Compare released 340-prefecture CSVs and code outputs with the paper's reported calibration scope.
  output:
    unit_of_observation: Prefecture-year, prefecture-pair-year-or-period, and model-state records depending on the file
    structure: Public paper-specific raw/intermediate/final files plus Stata/Matlab replication outputs
    geography: Mainland China prefecture-level units and source-specific county/province files
    time_span: 1990-2070 across file-specific observed, expected, and model-output periods
    key_variables:
    - Prefecture population and GDP inputs
    - Skill-specific bilateral migration flows
    - Housing, land-use, terrain, fiscal-transfer, and price inputs where present
    - Model-state population, migrant, and GDP variables
    formats:
    - csv
    - dta
    - xlsx
    - mat
    - m
    - do
  reproducibility:
    level: medium
    starting_point: Author-linked Google Drive Data and Programs for Publication.zip plus readme.txt
    code_available: true
    code_url: https://drive.google.com/file/d/1fcsr9IOBv_i7VG_PC47cOy-oicrulP8A/view?usp=drive_link
    requirements:
    - Approximately 1.46GB download and working storage
    - Stata for the numbered preparation and estimation programs
    - Matlab for the baseline, counterfactual, and robustness programs
    - Approved confidential NBS census and UHS files for a full rerun
    - File-level boundary, variable, and rights checks before new joins or redistribution
    blockers:
    - Omitted confidential census and UHS microdata
    - Package-level licence and third-party redistribution terms not displayed
    - Exact code-version, variable-label, and prefecture-concordance requirements need file-level verification
  compliance:
    terms_or_license: Follow the author package terms, Google Drive access conditions, NBS confidentiality rules, and each upstream provider's rights; no package licence was displayed in the checked version.
    robots_or_rate_limits: Not applicable to the checked direct file route; provider availability may change.
    personal_or_sensitive_data: Omitted NBS census and UHS microdata are confidential and must not be copied into this repository.
    redistribution: Share only files whose package and upstream rights permit redistribution; treat the public ZIP as a starting point rather than blanket permission.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-12'

used_by:
- cite: 'Wu & You (2025), Should Governments Promote or Restrain Urbanization?'
  doi: https://doi.org/10.1016/j.jinteco.2025.104084
  journal: Journal of International Economics
  year: 2025
  dataset_role: Paper-specific prefecture-level calibration inputs, bilateral migration-flow inputs, and model replication files for a China urbanization exercise
  evidence_type: publisher_data_section_and_replication_readme
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0022199625000406
  data_note: The publisher identifies a 340-prefecture China calibration using 2000-2020 data and provides a Google Drive replication-package route. The package README confirms public raw/intermediate/final files and Stata/Matlab programs, identifies data_pref_levels.csv and data_mig_flows.csv, and states that the confidential census and UHS microdata named by the programs are omitted and must be obtained separately.

provenance:
- source: https://www.sciencedirect.com/science/article/pii/S0022199625000406
  field_scope:
  - JIE paper identity, China urbanization calibration, and publisher data-availability route
  - Paper-level 340-prefecture and 2000-2020 scope used to identify the candidate asset
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://drive.google.com/uc?export=download&id=1fcsr9IOBv_i7VG_PC47cOy-oicrulP8A
  field_scope:
  - current public download-confirmation route
  - ZIP filename and displayed 1.4G size
  - no-login acquisition start after the Google Drive virus-scan confirmation
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://sites.google.com/site/youweilucky/research
  field_scope:
  - Author research page and replication-package link
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://drive.google.com/file/d/1fcsr9IOBv_i7VG_PC47cOy-oicrulP8A/view?usp=drive_link
  field_scope:
  - ZIP filename, 1,455,650,449-byte archive size, 666-entry central-directory manifest, and last-modified date observed from the direct file route
  - Public file families including census aggregates, fiscal_transfer_07.xlsx, final prefecture and migration CSVs, and Stata/Matlab code
  - README distinction between public files and omitted confidential census/UHS microdata, NBS application route, and numbered reproduction sequence
  added: '2026-08-12'
  confidence: high
  verified: true

related_datasets:
- id: china-census
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is the authors' paper-specific public starting point for a 340-prefecture China urbanization calibration: it gives prepared city-level and bilateral migration inputs plus code, while leaving confidential census/UHS files, exact file-level provenance, and full-reproduction rights as explicit boundaries.

## Select rules

- Use it when a project needs Wu & You's prepared prefecture calibration or skill-specific bilateral migration inputs, not when it needs unrestricted individual microdata.
- Treat `data_pref_levels.csv`, `data_mig_flows.csv`, and Matlab outputs as distinct paper-specific artifacts; do not collapse observed inputs and future model expectations into one panel.
- Join to census, yearbooks, land, firm, or household outcomes only after preserving the package's prefecture codes and documenting the boundary concordance.
- Keep claims about policies, assignment, and identification in the separate variation repository.

## Get recipe

Open the author-linked Google Drive package, read `readme.txt`, and inspect the manifest before selecting files. The public package is large but the final CSVs and numbered code paths are identifiable. If the intended question requires the missing micro-level stages, apply through the NBS Microdata Laboratory for the named census/UHS files, keep approved files outside this repository, and rerun only the Stata/Matlab stages needed for the target artifact. Record the downloaded version and rights before sharing any derivative.

## Connections and limitations

The strongest reusable key is the paper's prefecture code/name plus year or five-year period, with origin/destination and skill for migration flows. Boundary changes, code labels, and the distinction between observed 2000-2010 inputs and 2015-2070 expectations can change the meaning of a join. A public replication ZIP therefore makes the paper-compatible starting point reachable, but it does not make the underlying census microdata public, certify every upstream redistribution right, or guarantee that a new researcher can reproduce the complete model without the omitted files and software.
