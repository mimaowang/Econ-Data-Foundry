---
schema_version: 3
catalog_status: ready
id: china-jde-migration-resource-misallocation-replication-2024
name: Li–Ma–Tang Migration and Resource Misallocation in China replication data and derived firm-friction asset
aka:
- Replication Data for "Migration and Resource Misallocation in China"
- Li–Ma–Tang JDE replication package
- 中国迁移与资源错配复现数据
provider: Xiaolu Li, Lin Ma and Yang Tang; published through Mendeley Data
china_related: true
domains:
- regional
- urban
- firms
- productivity
- resource allocation
- economic geography

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: Public Mendeley Data v1 package containing the authors' README files, Stata/MATLAB/Fortran code, city lists, derived firm-level friction files, prefecture estimates, model inputs and paper tables/figures
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The package can be downloaded as a paper-specific data and code bundle and used immediately for the released derived files and reported tables. It is not a complete copy of the ASIF source: the README labels the original ASIF file, NBS city-code file, 2005 city population/GDP file and 2008 Second Economic Census input as external source data. A full source-based rerun therefore requires lawful access to those inputs in addition to the public package.
  barrier: >-
    The released replication asset is currently downloadable file by file, but the paper's raw ASIF and other external source files are not part of that claim. A source-level rerun still needs separately lawful source access and a version-concordance check; CC BY 4.0 for the Mendeley deposit does not automatically grant rights to third-party inputs.

unit_of_observation: Firm-level derived observation, prefecture-level estimated parameter, city-list or calibration row, and model scenario (separate files in the package)
structure: Paper-specific derived firm data plus prefecture panel, model inputs, code and output tables/figures
geo_granularity:
- prefecture-level city
- firm located in a prefecture
geography: 237 Chinese prefectures retained by the paper after the ASIF sample restriction; the package also contains a 279-city unbalanced intermediate path used before the final 237-prefecture restriction
time_span:
  start: '1998'
  end: '2008'
  last_confirmed_release: '2024-01-03'
  coverage_note: The paper estimates firm-friction distributions from ASIF observations in 1998-2007. The README separately identifies an external 2008 Second Economic Census file used to form a firm-count share input and an external 2005 city population/GDP file used in calibration; these inputs do not turn the package into a continuous 1998-2008 panel.
  last_checked: '2026-08-12'
frequency:
- annual
sample_size: The paper reports 237 prefectures after retaining locations with at least 500 ASIF firms; the public package contains 279-city intermediate files and prefecture-specific model/output files.
key_variables:
- Firm sales, payroll and total production costs used to estimate output and labor frictions (source ASIF; raw file external)
- Derived plant-level productivity/friction inputs in plant_tau_unbalanced279.csv and related CSV/DTA files
- Prefecture/city identifiers and city-list concordance files
- Estimated location-specific friction/productivity parameters and correlations
- Population and GDP calibration inputs and firm-count shares
- Model-generated migration, welfare and spatial-inequality outputs

research_fit:
  best_for:
  - Reproducing or extending the paper's structural measurement of firm-level output/labor frictions and productivity across Chinese prefectures
  - Starting from released derived plant and prefecture files when the research idea needs the paper's 1998-2007 regional resource-misallocation objects rather than a new raw-firm cleaning project
  choose_over:
  - Choose this paper-specific bundle over generic ASIF access when the target is the authors' released friction estimates, city restriction, model inputs or reported tables and figures
  - Choose the generic asif record when new variables, a different ASIF vintage, firm-level raw outcomes or a new sample construction are required
  - Use the released derived files before attempting to rebuild the same objects from raw ASIF, because the package preserves outputs that are otherwise costly to reconstruct
  not_good_for:
  - Treating the package as a representative household migration survey or an observed bilateral migration-flow database
  - Treating model-generated migration, welfare or inequality results as observed data
  - Rebuilding the exact paper from the source level without lawful ASIF, NBS city-code and external census inputs
  - Current city panels, service firms, post-2007 firm coverage or a causal policy/variation catalogue
  needs_join_for:
  - Household or individual migration outcomes, which require a separate survey or census asset
  - Current or alternative-year population/GDP controls not included in the paper-specific calibration files
  - New policy, treatment or identification variables; those belong in the data user's design and the separate variation repository, not in this record
  variation_available:
  - No causal or policy variation is contained in this data asset; identification belongs to the research design and the separate variation repository.
  topics:
  - firm-level resource misallocation
  - migration and spatial inequality
  - prefecture productivity
  - structural quantitative regional economics
  - China ASIF replication

good_for:
- Paper-specific regional firm-friction estimates and calibration inputs
- Prefecture-level comparisons of productivity, output/labor frictions and spatial inequality in the paper's historical window
- Reproducing tables, figures and model counterfactuals from the released code and derived files, subject to the external-input boundary
identification:
- This is a released historical firm-friction and model-replication asset, not an observed migration-flow database or an exogenous-shock record. A new causal design still requires independently chosen outcomes, treatment evidence, and identification.
linkable_keys:
- Prefecture/city name or code after checking the package's city-list files and boundary vintage
- Firm identifier and year only when the researcher has the same ASIF vintage and concordance
- Year for annual external controls

joins:
- target: asif
  relation: complement
  keys:
  - Firm identifier
  - Year
  - Prefecture/city code
  method: Match only against the same ASIF vintage and the paper's cleaning/concordance; the public package does not itself prove a stable cross-vintage key.
  evidence_status: plausible
- target: china-economic-census
  relation: complement
  keys:
  - City/prefecture code
  - 2008 reference year
  method: Use the paper package's documented firm-count-share role only after confirming the exact Second Economic Census table and code vintage.
  evidence_status: literature-used

access_routes:
- route: Mendeley Data public replication package, version 1
  access_status: available
  direct_url: https://data.mendeley.com/datasets/sffw2sbdp8/1
  requirements:
  - A browser or HTTP client able to reach the public Mendeley page
  - Read the root README and data_codes/readme.html before running code
  steps:
  - Open the Mendeley Data page or DOI and verify version 1, availability and its current licence/metadata.
  - Use the public file tree or its public file URLs to download only the needed files; the current manifest is large (4,890 completed files; about 3.43 GB total), so begin with a README and the named derived files rather than assuming a small one-click bundle.
  - Read the README files first, then inspect released derived files such as data/plant_tau_unbalanced279.csv, data/est_all.dta, data/w_city_beta.dta, data/remoteness.dta and data/ind_ratio.dta.
  - Run only the documented Stata/MATLAB stages needed for the intended table, figure or derived object; do not assume that a successful run proves the omitted ASIF source is available.
  deliverable: Public README files, code, derived firm/prefecture/model files, table/figure outputs and package metadata; not the raw ASIF or every external source file named in the README.
  cost: free
  last_checked: '2026-09-28'
  caveat: The current API shows V1 available and non-confidential, with 4,890 completed files totalling 3,433,346,234 bytes. Mendeley metadata states CC BY 4.0, while its licence notes that third-party contents may require additional permission. The manifest establishes public files and file names, not redistribution rights for external inputs.
- route: Lawful source-level rebuild using ASIF and external inputs
  access_status: available-with-conditions
  direct_url: https://doi.org/10.1016/j.jdeveco.2023.103218
  requirements:
  - Authorized access to the NBS Annual Surveys of Industrial Firms for 1998-2007
  - The NBS city-code file and the external 2005 population/GDP and 2008 Second Economic Census inputs named in the README
  - Stata and MATLAB; enough storage and computation for the model stages
  steps:
  - Obtain the source inputs through a lawful institutional, provider or author route and record their vintage and terms.
  - Place only the permitted source files in the paths expected by the README/code; do not publish restricted files in this repository.
  - Run the data-generation scripts before the SMM/model scripts and compare intermediate outputs to the released files.
  - Reproduce selected tables/figures from the package and document any version-dependent differences.
  deliverable: A researcher-built source-level reconstruction of the paper's firm-friction and prefecture/model objects, conditional on approved source access; exact equivalence is not promised.
  cost: mixed
  last_checked: '2026-08-12'
  caveat: The package does not provide a single verified acquisition route for each external source, and the source files' terms may prohibit redistribution or external joins.

access:
  url: https://data.mendeley.com/datasets/sffw2sbdp8/1
  cost: mixed
  license: CC BY 4.0 for the Mendeley deposit, subject to third-party contents and source terms
  format:
  - csv
  - dta
  - mat
  - do
  - m
  - f90
  - html
  - pdf
  - tex
  api: false
  how_to_get: Open the Mendeley page or DOI, confirm V1 is available and non-confidential, then use the public manifest to fetch the two README files and the particular released derived files or code required. Preserve paths when running code; the 3.43-GB full manifest is unnecessary for a targeted use.

caveats:
- The public package is a paper-specific derived/reproduction asset, not a public copy of the full ASIF microdata.
- The 1998-2007 ASIF window, 237-prefecture restriction and 2008 census-count input must not be read as a single balanced 1998-2008 panel.
- Exact columns, labels, missing-value treatment and code concordance for the large derived files should be checked from the current package before reuse.
- Model-generated migration, welfare and spatial-inequality values are counterfactual or calibrated outputs, not observed migration data.
- A CC BY package licence does not settle the rights of the NBS, census or other external source materials.

production:
  raw_sources:
  - name: National Bureau of Statistics Annual Surveys of Industrial Firms (ASIF), 1998-2007
    source_type: dataset
    role: Firm sales, payroll, production costs and location inputs for estimating productivity and output/labor frictions
    access_route: The package README names 98-0735cityclean.dta as external ASIF source data; use the separate asif record and a lawful provider/institutional route.
    url: https://data.mendeley.com/datasets/sffw2sbdp8/1
    coverage: ASIF firms above the paper's 5-million-RMB annual-sales threshold, restricted to prefectures with at least 500 firms; raw-file delivery is not established by the package.
    last_checked: '2026-08-12'
  - name: NBS city-code data
    source_type: dataset
    role: City/prefecture identifier and concordance used in the paper's data-generation scripts
    access_route: The README names citylist279.dta as external; exact provider delivery and vintage remain unresolved.
    url: https://data.mendeley.com/datasets/sffw2sbdp8/1
    coverage: 279-city intermediate path and final 237-prefecture selection
    last_checked: '2026-08-12'
  - name: 2008 Second Economic Census input
    source_type: dataset
    role: Firm-count share input named in data_codes/readme.html
    access_route: Use the china-economic-census record and verify the exact table before acquisition.
    url: https://data.mendeley.com/datasets/sffw2sbdp8/1
    coverage: 2008 reference input; exact table and delivered fields are not established here
    last_checked: '2026-08-12'
  - name: External city population/GDP file cityinfo_2005_total.csv
    source_type: dataset
    role: Population and GDP calibration input
    access_route: The README identifies this as external data; the original producer and current route are not identified by the checked package.
    url: https://data.mendeley.com/datasets/sffw2sbdp8/1
    coverage: 2005 city-level calibration input; exact geography and fields require file-level verification
    last_checked: '2026-08-12'
  acquisition_methods:
  - public package download
  - source-data acquisition under provider terms
  - Stata data preparation
  - MATLAB/compiled-model estimation
  - prefecture/city concordance
  sample_construction: The paper uses ASIF firms above 5 million RMB annual sales and retains locations with at least 500 firms, yielding 237 prefectures. The package retains a 279-city intermediate route and multiple zero-mean/non-zero-mean and robustness branches.
  pipeline_stages:
  - stage: collect
    inputs:
    - ASIF external source data
    - NBS city-code data
    - 2008 Second Economic Census input
    - External 2005 city population/GDP file
    method: Place permitted source data and the public package in the documented folder structure.
    tools:
    - Stata
    - MATLAB
    - file-system tools documented by the README
    output: Source and derived inputs for the paper's data-generation and model stages
    evidence: Mendeley data_codes/readme.html, section 3.1
  - stage: clean
    inputs:
    - 98-0735cityclean.dta
    - citylist279.dta
    method: Apply the authors' Stata data-generation scripts to create plant-level and city-level intermediate files.
    tools:
    - Stata do-files in data_codes and model_codes
    output: plant_tau_2007.dta, plant_tau_unbalanced279.csv and related files
    evidence: Mendeley data_codes/readme.html, sections 3.1 and 3.2
  - stage: model
    inputs:
    - Plant-level derived data
    - Firm-count share and calibration inputs
    method: Estimate location-specific productivity and friction distributions using the supplied SMM and model code, including zero-mean and non-zero-mean branches.
    tools:
    - MATLAB
    - Stata
    - supplied model source files
    output: Prefecture-specific parameter and model-input files such as est_all.dta, w_city_beta.dta and input_mat_* files
    evidence: Mendeley data_codes/readme.html, sections 2 and 3.2-3.3
  - stage: validate
    inputs:
    - Released derived files
    - tab_fig.pdf and tab_fig/*.tex outputs
    method: Re-run selected table/figure scripts and compare output names, sample restrictions and parameter files to the published results.
    tools:
    - Stata
    - MATLAB
    output: Reproduced tables, figures and documented differences
    evidence: Mendeley root README and data_codes/readme.html, section 2
  constructed_variables:
  - name: plant-level productivity and friction inputs
    concept: Firm-level productivity and output/labor distortion objects passed into the structural estimation
    source_fields:
    - ASIF sales
    - ASIF payroll
    - ASIF total production costs
    method: Apply the paper's documented ASIF cleaning and friction-estimation code; exact variable labels remain package-version dependent.
    validation: Compare generated plant_tau files and selected reported tables to the released files.
    limitations: The raw ASIF source and complete field dictionary are not part of the public Mendeley deposit.
  - name: prefecture friction distribution parameters
    concept: Location-specific standard deviations and correlations among productivity and output/labor frictions
    source_fields:
    - Derived plant-level inputs
    - Prefecture/city identifiers
    method: Supplied SMM/MATLAB model scripts under newtarget_nomean and newtarget_mean.
    validation: Compare est_all and model outputs with tab_fig tables/figures.
    limitations: These are estimated/calibrated objects, not directly observed administrative variables.
  validation:
  - Confirm the public Mendeley file tree and README version before using a file.
  - Compare 237-prefecture selection and the 279-city intermediate files with the README and paper data section.
  - Reproduce at least one table or figure from the supplied code and compare it with tab_fig outputs.
  - Keep external-source versions and any unresolved code/field differences in the project note.
  output:
    unit_of_observation: Derived plant, prefecture/city, model scenario and table/figure output
    structure: Derived firm files plus annual prefecture estimates and model branches
    geography: 237 prefectures in the paper; 279-city intermediate files in the package
    time_span: ASIF 1998-2007; separate 2005 and 2008 external calibration inputs
    key_variables:
    - Derived productivity and output/labor friction measures
    - Prefecture-specific distribution parameters and correlations
    - City/prefecture identifiers, population/GDP calibration values and firm-count shares
    - Model migration, welfare and inequality outputs
    formats:
    - csv
    - dta
    - mat
    - tex
    - pdf
  reproducibility:
    level: medium
    starting_point: https://data.mendeley.com/datasets/sffw2sbdp8/1
    code_available: true
    code_url: https://data.mendeley.com/datasets/sffw2sbdp8/1
    requirements:
    - Public Mendeley package and README files
    - Stata and MATLAB
    - Authorized ASIF and external input access for a source-level rerun
    - Storage and computation for large derived files and model branches
    blockers:
    - Raw ASIF and named external inputs are not established as downloadable components of the public package.
    - Exact current provider route, code concordance and full column dictionary remain to be verified.
  compliance:
    terms_or_license: Mendeley metadata lists CC BY 4.0; external NBS/census/source terms may impose additional conditions.
    robots_or_rate_limits: Use the public Mendeley route and provider-authorized source routes; do not scrape restricted NBS sources.
    personal_or_sensitive_data: Firm microdata source is not publicly redistributed in the package; do not add restricted ASIF files here.
    redistribution: Do not redistribute omitted ASIF, census or other third-party inputs; check package and source terms before sharing derived files.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-12'

used_by:
- cite: 'Li, Ma & Tang (2024), Migration and Resource Misallocation in China'
  doi: https://doi.org/10.1016/j.jdeveco.2023.103218
  journal: Journal of Development Economics
  year: 2024
  dataset_role: Main ASIF firm inputs and paper-specific derived plant-friction, prefecture-estimate and model-replication files
  evidence_type: replication
  evidence_url: https://data.mendeley.com/datasets/sffw2sbdp8/1
  data_note: The article's data section identifies ASIF firm-level data for 1998-2007, firms above 5 million RMB annual sales and 237 retained prefectures. The public Mendeley v1 package is linked to the article and includes README files, code, derived plant/prefecture files and paper tables/figures; its README explicitly labels 98-0735cityclean.dta, citylist279.dta, cityinfo_2005_total.csv and the 2008 Second Economic Census input as external source data. It is therefore a usable paper-specific reproduction asset, not a public copy of complete ASIF.

provenance:
- source: Mendeley Data v1 page and public API metadata https://data.mendeley.com/datasets/sffw2sbdp8/1
  field_scope:
  - package identity and article link
  - publication date and CC BY 4.0 metadata
  - public availability and top-level file structure
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Mendeley public folder/file manifests and data_codes/readme.html
  field_scope:
  - nested code/data/output folders
  - derived file names and file-level public availability
  - external-source boundary for ASIF, NBS city codes, 2005 city information and 2008 census input
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Mendeley Data public API dataset sffw2sbdp8, queried 2026-09-28
  field_scope:
  - current V1 availability and non-confidential status
  - CC BY 4.0 deposit licence
  - 4,890 completed public files and 3,433,346,234-byte manifest total
  - current public download URLs and named README, derived-data and code files
  added: '2026-09-28'
  confidence: high
  verified: true
- source: ScienceDirect article https://www.sciencedirect.com/science/article/pii/S0304387823001748 and SMU working-paper PDF https://ink.library.smu.edu.sg/context/soe_research/article/3718/viewcontent/lmt_China_sv.pdf
  field_scope:
  - paper identity, 2024 JDE publication and DOI
  - ASIF role, 1998-2007 window, sales threshold and 237-prefecture restriction
  added: '2026-08-12'
  confidence: high
  verified: true

related_datasets:
- id: asif
  relation: often-confused-with
- id: china-economic-census
  relation: complement
---

## Positioning in one sentence

This is a recent (2024) paper-specific, publicly downloadable reproduction asset for Li, Ma & Tang's China migration/resource-misallocation study: it supplies derived plant and prefecture objects, model code and reported outputs, while the original ASIF and other external inputs remain separate acquisition problems. The publication date makes it a modestly recent route to check first when the research idea matches its historical 1998-2007 regional firm-friction window, but it does not raise the evidence or reproducibility standard.

## Select rules

- Prioritize it when the question needs the paper's released firm-friction estimates, 237-prefecture restriction, SMM inputs or model tables/figures.
- Switch to the generic ASIF record when the question needs raw firm variables, a different period, a new cleaning rule or a new sample; this package does not unlock ASIF microdata.
- Do not use the package's model-generated migration or welfare series as observed migration data, and do not treat it as a policy/variation record.

## Get recipe

Open the [Mendeley Data v1 page](https://data.mendeley.com/datasets/sffw2sbdp8/1), check the current version and licence, download the public package, and read both README files before opening code. For a quick paper-specific analysis, begin with the released derived files and tables; for a full source-level rebuild, first obtain lawful ASIF and the external NBS/census inputs named in the README, record their vintages, then run the documented Stata and MATLAB stages and compare at least one output to the released figures or tables.

## Connections and Limitations

The package's city/prefecture identifiers can support a documented join to other regional data only after checking the NBS code vintage and boundary definitions. A firm-level join to a separately obtained ASIF extract is conditional on the same source vintage and the authors' cleaning/concordance. The public bundle is most useful as a stable starting point for the authors' derived objects; it does not establish a general current city panel, household migration microdata, or a reproducible copy of all original inputs.
