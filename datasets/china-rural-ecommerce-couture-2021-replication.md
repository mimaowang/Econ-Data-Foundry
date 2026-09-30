---
schema_version: 3
catalog_status: ready
id: china-rural-ecommerce-couture-2021-replication
name: 'Data and Code for: Connecting the Countryside via E-Commerce (Couture, Faber, Gu & Liu 2021 AER:Insights replication package, openICPSR 117506 V2)'
aka:
- openICPSR project 117506 V2
- 10.3886/E117506V2
- Connecting the Countryside via E-Commerce replication data
- Rural Taobao RCT survey and price data
- 农村电商入户随机实验复现数据
provider: American Economic Association [publisher] / ICPSR [distributor]; deposited by Victor Couture (UC Berkeley Haas), Benjamin Faber (UC Berkeley), Lizhi Liu (Georgetown), Yizhen Gu (Jinan University)
china_related: true
domains:
- rural
- e-commerce
- regional
- digital-economy
- consumption
- trade-costs

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: "openICPSR project 117506 version V2: README.pdf (52 KB) plus Data_and_Code/Code, Data, Output, and Survey_Material. The current public tree lists three Stata scripts and nine named deidentified survey/price data files; it does not show the internal Alibaba transaction universe."
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The AEA/openICPSR deposit supplies deidentified household-survey and retail-price files, survey material, code, and output for the paper's 100-village Rural Taobao evaluation. The current public listing names three Stata scripts and nine deidentified survey/price files; downloading them follows ICPSR login. The paper's second layer - the firm's internal transaction database covering about 12,000 villages in 5 provinces (27.3M purchase records Nov 2015-Apr 2017) - is described in the paper but is not shown in the public package tree.
  barrier: The public listing does not state all nested content, exact download terms, or whether any part of the internal Alibaba transaction database is released. Login is required for download, and deidentification limits external linkage even for released microdata.

unit_of_observation: Household (survey waves), retail price quote (store price survey), village (RCT unit and village-level aggregates), transaction (deidentified firm-data extracts if present in the package)
structure: Two-wave household panel (baseline end-2015/early-2016, endline ~12 months later) plus a two-round retail price survey plus village-level files
geo_granularity:
- village
- county
geography: "RCT: 8 counties in Anhui, Henan and Guizhou provinces (100 villages: 40 control + 60 treatment drawn from 432 candidates). Firm admin database: ~12,000 program villages in 5 provinces (Anhui, Guangxi, Guizhou, Henan, Yunnan)"
time_span:
  start: '2015-12'
  end: '2017-04'
  last_confirmed_release: '2021-02-18'
  coverage_note: 'openICPSR project metadata (DataCite): Time Period 12/1/2015 - 5/31/2017, Geographic Unit village, Data Type survey data, Geographic Coverage China. Paper data section (NBER WP w24384 and AER:Insights supplemental appendix, read 2026-08-14): baseline household survey end-2015/early-2016; endline one year later; purchase transaction DB Nov 2015 - Apr 2017 (~27.3M records, ~12,000 villages, 5 provinces); sales/out-shipment DB Jan 2016 - Apr 2017 (~500,000 shipments).'
  last_checked: '2026-09-27'
frequency:
- two survey waves
- monthly transaction series (firm DB, not confirmed in package)
sample_size: 100 RCT villages (60 treatment / 40 control) in 8 counties of 3 provinces, sampled from 432 candidates; ~28 households per village at baseline (14 inner-zone + 14 outer-zone) plus 10 added inner-zone households at endline; ~115 price quotes per village; ~27.3M purchase records and ~500K out-shipments in the firm DB (paper-level, not confirmed as released files)
key_variables:
- Household retail consumption expenditures split across 9 categories, production inputs
- Household incomes, hours worked, occupations and sectors of members, asset ownership, financial accounts, internet use, migration
- Retail price quotes at barcode-equivalent product level (baseline and endline)
- Village treatment assignment (randomized) and actual treatment status
- Deidentified price file (price_raw_deidentified_round2.dta per prior repository-metadata search)
- "Firm purchase DB fields (paper): product category, number of units, amount paid, unique buyer identifier"
- "Firm sales DB fields (paper): village of origin, out-shipment weight in kg"

research_fit:
  best_for:
  - Replicating or extending the paper's RCT estimates of rural e-commerce (Rural Taobao terminal) effects on household consumption, cost of living, and local retail prices in 100 Chinese villages
  - Studying the 2015-2017 window of the Alibaba Rural Taobao rollout with the authors' deidentified survey/price files
  - Using the paper's survey instruments and sampling design (inner/outer zone, price-quote protocol) as a template
  choose_over:
  - Choose this package over the MOFCOM demonstration-county lists when the research needs household-level microdata from a randomized e-commerce rollout rather than a county program roster
  - Choose this package over general surveys (CFPS etc.) when the exact RCT treatment contrast and price data are required; use CFPS for nationally representative household measures (the paper itself uses CFPS 2012 consumption shares for survey weights)
  not_good_for:
  - A nationally representative picture of rural China (the RCT covers 100 villages in 3 provinces)
  - "The full Alibaba transaction universe (27.3M records): the paper describes the firm's internal database; the public package is not confirmed to contain it"
  - Effects after April 2017 or outside the 5 program provinces
  - The MOFCOM demonstration program counties (a different program from Alibaba's Rural Taobao)
  needs_join_for:
  - County/population context (the paper uses 2010 census township-level data for market-access measures and the 2008 economic census for village establishment counts)
  - CFPS 2012 microdata for expenditure weights
  - GIS/distance measures (village locations, distances to terminals)
  variation_available:
  - Village-level randomized treatment assignment (ITT/TOT) and village exposure spillovers within 3/10 km are data dimensions of the released files; causal claims and design threats belong to the Econ-Variation repository
  topics:
  - rural e-commerce
  - e-commerce RCT
  - consumption and cost of living
  - retail prices
  - trade costs
  - digital economy

good_for:
- RCT-based evaluation of rural e-commerce access effects on households and local retailers
- Reuse of the authors' deidentified survey and price data for the 2015-2017 window
identification:
- The released files support replication of the paper's documented deidentified survey and price analyses; they do not establish availability of Alibaba's internal transaction universe or independently settle causal interpretation.
linkable_keys:
- Village identifier (within the released deidentified files)
- Household identifier (survey rounds)
- County (8 RCT counties; exact identifiers per released files)

joins:
- target: cfps
  relation: complement
  keys:
  - None required: CFPS enters only as expenditure shares for survey design
  method: Use CFPS only for nationally representative consumption weights or broader household context; do not merge individual records
  evidence_status: literature-used
- target: china-census
  relation: complement
  keys:
  - Township-level units
  method: The paper's market-access measures use 2010 census township populations; replicate the authors' township match if extending their analysis
  evidence_status: literature-used
- target: china-mofcom-rural-ecommerce-demo-counties
  relation: often-confused-with
  keys:
  - County name
  method: "Keep the two programs separate: Alibaba Rural Taobao (this package) vs the MOFCOM demonstration program (that record)"
  evidence_status: verified

access_routes:
- route: openICPSR AEA replication project 117506 V2
  access_status: available-with-login
  direct_url: https://doi.org/10.3886/E117506V2
  requirements:
  - ICPSR login and acceptance of the current download terms; the current download action redirects to the ICPSR login flow.
  steps:
  - Open the DOI https://doi.org/10.3886/E117506V2 (resolves to https://www.openicpsr.org/openicpsr/project/117506/version/V2/view).
  - Read the project description and version history (V2 published 2021-02-18 by AEA/ICPSR).
  - Read README.pdf before downloading; inspect Data_and_Code/Code, Data, Output, and Survey_Material.
  - Download the files needed after login. The visible Code folder lists do_file_analysis.do, retail_data_processing.do, and survey_data_processing.do.
  - The visible Data folder lists Merge_Village_Vars.dta, deidentified round-1/round-2 price and store files, retail_data_analysis.dta, survey_data_analysis.dta, and deidentified round-1/round-2 survey files.
  - Record the version and file citation (Couture, Faber, Liu & Gu 2021, 10.3886/E117506V2).
  deliverable: >-
    Login-mediated public V2 materials: README.pdf (52 KB), Code, Data, Output,
    and Survey_Material. The current public directory enumerates three Stata scripts
    and nine named data files, including deidentified survey and price rounds; the
    full internal transaction database is not shown.
  cost: registration
  last_checked: '2026-09-27'
  caveat: The current public tree confirms the listed folders and files, but the download flow is login-mediated and it does not establish that Alibaba's internal transaction database or every paper input is included.
- route: AEA article page and materials
  access_status: available
  direct_url: https://www.aeaweb.org/articles?id=10.1257/aeri.20190382
  requirements:
  - Public web access
  steps:
  - Confirm article identity, abstract, citation, and the Replication Package link (DOI 10.3886/E117506V2) and Supplemental Appendix (https://www.aeaweb.org/articles/materials/14082, read 2026-08-14).
  - Use the published PDF (complimentary download per AEA page; automated fetch returned 403 in this environment) and the supplemental appendix for the data construction details.
  deliverable: Article text, supplemental appendix, disclosure statement
  cost: free
  last_checked: '2026-08-14'
  caveat: The complimentary PDF link returned 403 to an automated client (2026-08-14); the NBER working paper w24384 PDF (fetched and read 2026-08-14) contains the same data section for the pre-publication version.
- route: NBER working paper w24384 (open full text)
  access_status: available
  direct_url: https://www.nber.org/system/files/working_papers/w24384/w24384.pdf
  requirements:
  - Public web access
  steps:
  - Download the PDF and read the Experimental Design and Data section (fetched and read in full 2026-08-14).
  deliverable: Full working-paper text with the data section
  cost: free
  last_checked: '2026-08-14'
  caveat: Working-paper version (2018); the published AER:Insights version may differ in detail.

access:
  url: https://doi.org/10.3886/E117506V2
  cost: registration
  license: openICPSR standard terms for public AEA replication projects; material distributed as received from the depositor; original data sources (Alibaba transaction DB, survey fieldwork) remain private
  format:
  - dta
  - pdf
  - do
  - xlsx
  api: false
  how_to_get: Open project 117506 V2 through the DOI, inspect the current public folder tree, use the ICPSR login-mediated download flow, read README.pdf, and download only the needed deidentified survey, price, code, output, or survey-material files.
caveats:
- The paper's firm-admin transaction database (27.3M records across ~12,000 villages) is described in the paper as internal firm data; the public package is not confirmed to include it. Do not promise the full transaction universe to a researcher.
- The current public V2 tree lists the Code/Data/Output/Survey_Material structure, three Stata scripts, and nine named survey/price data files. It does not prove every nested item, exact download terms, or inclusion of any internal firm database.
- Download actions redirect to ICPSR login; use the browser flow and inspect README.pdf before reuse.
- The survey covers 100 villages in 3 provinces; representativeness for China's countryside is limited (the paper itself compares RCT villages with the 5-province program population in the appendix).

production:
  raw_sources:
  - name: Alibaba Rural Taobao program village candidate lists (8 county operations teams, 432 candidate villages)
    source_type: other
    role: Sampling frame for the RCT (village candidates extended by 5 per county)
    access_route: Internal program lists obtained by the authors; not publicly released
    url: https://www.nber.org/system/files/working_papers/w24384/w24384.pdf
    coverage: 432 villages in 8 counties (Anhui, Henan, Guizhou)
    last_checked: '2026-08-14'
  - name: Household survey fieldwork (baseline end-2015/early-2016; endline ~12 months later; RCCC-trained teams)
    source_type: dataset
    role: Main survey microdata in the deposit (consumption, income, labor, assets, internet, migration)
    access_route: Released deidentified in the openICPSR package
    url: https://doi.org/10.3886/E117506V2
    coverage: 100 villages; ~28 households/village baseline, +10 inner-zone households at endline
    last_checked: '2026-08-14'
  - name: Local retail price survey (two rounds)
    source_type: dataset
    role: Price-quote data (target 115 quotes per village) in the deposit; deidentified price file price_raw_deidentified_round2.dta per prior metadata search
    access_route: Released deidentified in the openICPSR package
    url: https://doi.org/10.3886/E117506V2
    coverage: Stores in/within 15-minute walk of sample villages; two rounds
    last_checked: '2026-08-14'
  - name: Anonymous Firm (Alibaba) internal transaction database
    source_type: dataset
    role: Paper's second analysis layer - purchase DB (Nov 2015-Apr 2017, ~27.3M records, ~12,000 villages, 5 provinces) and sales/out-shipment DB (Jan 2016-Apr 2017, ~500K shipments)
    access_route: Internal firm data described in the paper; release status in the public package NOT confirmed
    url: https://www.nber.org/system/files/working_papers/w24384/w24384.pdf
    coverage: 5 provinces (Anhui, Guangxi, Guizhou, Henan, Yunnan), Nov 2015-Apr 2017
    last_checked: '2026-08-14'
  - name: CFPS 2012 microdata and 2008 economic census (auxiliary)
    source_type: dataset
    role: CFPS 2012 used for consumption-category weights in Anhui/Henan; 2008 economic census establishment data used for village-level stratification variables
    access_route: Separate provider routes (see cfps and china-economic-census records)
    url: https://www.isss.pku.edu.cn/cfps/en/
    coverage: As documented in the paper's appendix
    last_checked: '2026-08-14'
  acquisition_methods:
  - repository download
  - field survey
  - price survey
  sample_construction: "The RCT sample is 40 control + 60 treatment villages randomly selected per county from extended candidate lists (432 candidates, average 54 per county), stratified on delivery-service status, applicant test score, village population, and economic-census establishment counts, with a 2.5 km minimum distance between list villages where possible. Households: 14 inner-zone (within 300 m of planned terminal) + 14 outer-zone per village at baseline, 10 additional inner-zone at endline, selected by random walk from mapped residences."
  pipeline_stages:
  - stage: collect
    inputs:
    - Village candidate lists
    - Household and price survey fieldwork
    method: Field surveys conducted by trained teams (RCCC supervisors and local university students); paper-based questionnaires with transaction-level recall spreadsheets aggregated into final questionnaires; price data per IMF/ILO-style protocol with product pictures.
    tools:
    - Field survey teams
    output: Raw household and price survey files
    evidence: Supplemental appendix F (read 2026-08-14)
  - stage: clean
    inputs:
    - Raw survey files
    - Firm transaction extracts
    method: Clean the household survey (exclude 0.25% unreliable households per surveyor ratings), winsorize tails, build expenditure/income aggregates, deidentify firm-price data.
    tools:
    - Stata
    output: Cleaned household dataset, price dataset (e.g. price_raw_deidentified_round2.dta per prior metadata search), village files
    evidence: Supplemental appendix F; openICPSR file names (prior metadata search)
  - stage: aggregate
    inputs:
    - Firm transaction database
    method: Aggregate the purchase/sales transaction DB to village-month outcomes (number of buyers, transactions, terminal sales, out-shipments) for the paper's appendix analyses.
    tools:
    - Stata
    output: Village-month outcomes used in the paper's appendix tables
    evidence: Paper and appendix D (read 2026-08-14); release status of these aggregates in the package not confirmed
  - stage: validate
    inputs:
    - Deposited files
    - Paper tables
    method: Run the released code against the deposited data and compare with the published tables.
    tools:
    - Stata
    output: Reproduced tables
    evidence: Replication package; not executed this pass
  constructed_variables:
  - name: treatment indicators (ITT/TOT)
    concept: Randomized village assignment and actual terminal rollout status
    source_fields:
    - Village assignment records
    method: ITT = assigned treatment (60 villages); TOT = actual rollout (38 of 60 treatment, 5 of 40 control) instrumented by assignment
    validation: Compliance pattern documented in the paper (2026-08-14 read)
    limitations: Compliance incomplete; one county's endline data collection was suspended (4 of 100 villages without endline)
  - name: e-commerce uptake and expenditure shares
    concept: Household use of and spending through the Rural Taobao option
    source_fields:
    - Household survey consumption module
    method: Constructed from the survey's modality-coded purchase transactions (online vs offline, in/out of village)
    validation: Paper tables 1-3
    limitations: Self-reported; survey months differ across villages (seasonality addressed in appendix with the firm DB)
  output:
    unit_of_observation: Household, price quote, village
    structure: Two-wave household panel + two-round price survey + village files
    geography: 8 counties in Anhui, Henan, Guizhou (RCT); 5-province program universe in paper-level appendix analyses
    time_span: Survey 2015-12 to 2017 (two rounds); paper-level transaction window Nov 2015-Apr 2017
    key_variables:
    - Consumption by 9 categories
    - Income and labor outcomes
    - Retail price quotes
    - Treatment/uptake variables
    - Deidentified price file
    formats:
    - dta
  reproducibility:
    level: medium
    starting_point: https://doi.org/10.3886/E117506V2
    code_available: true
    code_url: https://www.openicpsr.org/openicpsr/project/117506/version/V2/view
    requirements:
    - ICPSR login and browser access
    - Stata (authors' code)
    - Time to read README.pdf and confirm any nested file or licensing detail not visible in the public tree
    blockers:
    - The paper's full transaction database is internal firm data; any released extract is deidentified and partial
    - Survey instruments and deidentification choices must be read from the deposit
  compliance:
    terms_or_license: openICPSR terms for AEA replication projects; material distributed as received; deidentified data only
    robots_or_rate_limits: Public file-tree browsing is available; download uses the repository's login flow. Do not automate authenticated retrieval.
    personal_or_sensitive_data: Household survey data are deidentified in the deposit; do not attempt re-identification
    redistribution: Follow the openICPSR terms and the AEA data/code policy for redistribution
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

used_by:
- cite: 'Couture, Victor, Benjamin Faber, Yizhen Gu, and Lizhi Liu (2021), Connecting the Countryside via E-Commerce: Evidence from China, AER: Insights 3(1): 35-50'
  doi: https://doi.org/10.1257/aeri.20190382
  journal: 'AER: Insights'
  year: 2021
  dataset_role: Main data for the RCT evaluation - household survey, retail price survey, and firm transaction database used for consumption, income, price, and take-up outcomes
  evidence_type: replication
  evidence_url: https://doi.org/10.3886/E117506V2
  data_note: >-
    AEA article page (read 2026-08-14) lists the Replication Package (DOI 10.3886/E117506V2) and Supplemental Appendix.
    DataCite (read 2026-08-14) confirms title "Data and Code for: Connecting the Countryside via E-Commerce", version 2,
    ICPSR publisher, collected 2015-12-01/2017-05-31, issued 2021, creators Couture/Faber/Liu/Gu. NBER WP w24384 and the
    supplemental appendix (read in full 2026-08-14) document the RCT design (100 villages, 8 counties, 3 provinces), the
    household and price surveys, and the firm's internal purchase/sales databases (5 provinces, Nov 2015-Apr 2017). The
    current V2 public tree confirms README.pdf plus Code/Data/Output/Survey_Material and lists three Stata scripts and nine
    named deidentified survey/price files. The public tree does not show the full internal Alibaba transaction database.

provenance:
- source: AEA article page https://www.aeaweb.org/articles?id=10.1257/aeri.20190382 (read 2026-08-14)
  field_scope:
  - paper identity and citation
  - replication package DOI
  - supplemental appendix link
  - abstract
  added: '2026-08-14'
  confidence: high
  verified: true
- source: DataCite API https://api.datacite.org/dois/10.3886/E117506V2 (read 2026-08-14)
  field_scope:
  - package title, version, publisher, creators
  - collection dates and issue year
  - related identifier (isVersionOf 10.3886/e117506)
  added: '2026-08-14'
  confidence: high
  verified: true
- source: NBER working paper w24384 PDF https://www.nber.org/system/files/working_papers/w24384/w24384.pdf (read in full 2026-08-14)
  field_scope:
  - RCT design and sample
  - survey content
  - firm transaction database scope
  added: '2026-08-14'
  confidence: high
  verified: true
- source: AER:Insights supplemental appendix https://www.aeaweb.org/articles/materials/14082 (read in full 2026-08-14)
  field_scope:
  - sampling and field protocols
  - deidentification and cleaning
  - appendix estimation details
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Wayback snapshots of openICPSR project 117506 (V2 view 2022-12-25; V1 Data_and_Code folder 2024-01-16; V2 Data_and_Code folder 2025-03-19; fetched 2026-08-14)
  field_scope:
  - V2 top-level manifest (README.pdf 52 KB + Data_and_Code)
  - V2 Data_and_Code folder structure (Code/Data/Output/Survey_Material)
  - project description fields (village unit, survey data type, time period)
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Current openICPSR project 117506 V2 public file tree https://www.openicpsr.org/openicpsr/project/117506/version/V2/view
  field_scope:
  - current V2 project identity, China village survey scope, and 2015-12 to 2017-05 time period
  - README.pdf and Data_and_Code/Code, Data, Output, Survey_Material structure
  - three named Stata scripts and nine named deidentified survey/price data files with displayed sizes
  - current ICPSR login-mediated download boundary
  added: '2026-09-27'
  confidence: high
  verified: true
- source: openICPSR direct pages (https://www.openicpsr.org/openicpsr/project/117506/version/V2/view and OAI endpoints)
  field_scope:
  - live V2 file manifest
  - README contents
  added: '2026-08-14'
  confidence: low
  verified: false

related_datasets:
- id: china-mofcom-rural-ecommerce-demo-counties
  relation: often-confused-with
- id: china-senddown-county-exposure
  relation: benchmark
- id: cfps
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

This is the login-mediated AEA/ICPSR replication package behind Couture, Faber, Gu & Liu (2021 AER:Insights): it visibly contains deidentified household-survey and retail-price files, Stata code, output, and survey material from a 100-village Rural Taobao RCT (2015-2017). The paper's full 27.3M-record Alibaba transaction universe remains internal firm data and is not shown as part of the public package.

## Select rules

- Prioritize it when the research needs the paper's RCT microdata (household consumption/income, retail prices, take-up) for rural e-commerce access.
- Switch to the MOFCOM demonstration-county lists when the question is the national policy program's county rollout; the two programs are different and must not be merged.
- Use CFPS for nationally representative rural household measures; this package is a 100-village experiment, not a national sample.

## Get recipe

1. Open https://doi.org/10.3886/E117506V2 and inspect the public V2 tree: README.pdf plus Data_and_Code/Code, Data, Output, and Survey_Material.
2. Use the ICPSR login-mediated download flow. The visible Data folder names deidentified round-1/round-2 survey and price files, while the Code folder names three Stata scripts; inspect README.pdf before treating any file as a paper analysis input.
3. Download the survey/price files, code, output, or survey material needed; record version V2 and the file citation.
4. Read the paper data section (NBER w24384 or the published PDF) and supplemental appendix for variable construction.

## Connections and Limitations

The natural units are household, price quote, and village within the 8 RCT counties; village identifiers inside the deidentified files are the link keys, and any extension needs the paper's township-level census market-access construction. The public package is not confirmed to include the full Alibaba transaction database, and the sample covers 100 villages in 3 provinces, so national generalization requires the authors' own representativeness checks rather than assumption. The remaining data-side check is whether a particular nested file and its terms meet an extension's needs.
