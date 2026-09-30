---
schema_version: 3
catalog_status: ready
id: china-senddown-county-exposure
name: Chen et al. China send-down census, gazetteer, and county education data
aka:
- Arrival of Young Talent replication data
- China send-down movement county dataset
- 上山下乡县级教育数据
- census_1990_clean.dta
provider: Yi Chen, Ziying Fan, Xiaomin Gu, and Li-An Zhou; distributed through the AEA and openICPSR
china_related: true
domains:
- rural
- regional
- education
- labor
- demography
- human-capital
- economic-history

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: openICPSR project 119690 V1 containing cleaned census files, county and county-year files, a cleaned CFPS 2010 file, NBS_data.dta, Stata code, README, and LICENSE.txt
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The AEA/openICPSR deposit provides the paper-used integrated files and code as downloadable Stata artifacts. A researcher can use the released county and census tables directly, but reproducing the upstream historical compilation requires understanding the authors' cleaning and matching code and obtaining any source materials that are only cited rather than deposited.
  barrier: openICPSR exposes file metadata and a download route, but the checked pages redirect downloads through an account or terms flow. The exact local-gazetteer source files, school-statistics books, and variable construction details must be verified from the deposited README/code; the repository itself is not a general release of the underlying Chinese censuses or gazetteers.

unit_of_observation: Individual census record, county, or county-year observation depending on the file
structure: Repeated census cross-sections plus county and county-year panels
geo_granularity:
- county
- individual
- rural population
geography: China; openICPSR describes the universe as the rural population in China and the geographic coverage as China. Exact county inclusion and boundary vintage are file-specific and require the deposit codebook or labels.
time_span:
  start: '1968'
  end: '2010'
  last_confirmed_release: '2020-10-21'
  coverage_note: The deposit contains cleaned population-census files for 1982, 1990, 2000, and 2010, county and county-year files associated with historical rural education outcomes, a CFPS 2010 extract, and a small NBS file. The paper's historical data construction concerns the send-down period and the county education series around 1978-1984, but the exact file-level time coverage must be read from labels and code.
  last_checked: '2026-08-11'
frequency:
- census wave
- annual county panel
sample_size: openICPSR reports 3,558,270 cases and 26 variables for census_1990_clean.dta; CFPS_2010_clean.dta has 6,320 cases and 20 variables; other deposited files are listed with sizes but their case counts require file-level inspection.
key_variables:
- Census-wave individual demographic and education fields
- County identifier and county-level historical measures
- County-year education or school outcomes
- Rural population and sent-down-youth related fields as defined by the deposit code
- CFPS 2010 individual and household fields used by the paper
- NBS_data.dta fields
- Stata labels and constructed variables in the deposited files

research_fit:
  best_for:
  - Historical county-level rural education and human-capital outcomes where the paper's integrated census/gazetteer files are the intended starting point
  - Comparing education, occupation, marriage, or family outcomes across the deposited census waves or county panels
  - Reusing the authors' cleaned file structure rather than reconstructing every census join from raw publications
  choose_over:
  - Choose this record over the general china-census record when the research specifically needs the paper's cleaned county/gazetteer integration and historical rural sample
  - Choose the general china-census record for current census waves, official aggregate tables, or a broader census access route not tied to this paper's cleaning choices
  - Use the separate cfps record when a general CFPS panel or survey design is needed; the deposited CFPS file is only the paper's prepared extract
  not_good_for:
  - Treating the deposit as raw local gazetteers or a complete national census release
  - Current county education monitoring or annual data after the deposited years
  - Assuming that every historical school-statistics source cited by the paper is downloadable from openICPSR
  needs_join_for:
  - School counts and enrollment series drawn from China Compendium of Statistics 1949-2008 and China Rural Statistical Yearbook 1985
  - A current or differently defined county boundary crosswalk
  - Outcomes or surveys outside the deposited census, county, and CFPS files
  variation_available:
  - Census waves and county-year education fields are data dimensions in the deposit; this record does not classify the send-down policy, treatment assignment, or causal variation
  topics:
  - rural education
  - historical human capital
  - county development
  - population census
  - migration and demography

good_for:
- Historical county-level education and rural human-capital analysis using the deposited integrated files
- Reproducing the data inputs of Chen, Fan, Gu, and Zhou (2020) before adapting them to another county panel
- Linking historical county measures to a separately verified regional outcome or survey by county code and year
identification:
- This is a paper-specific cleaned census, county, and code bundle, not a stand-alone causal-variation record. It supports reproducing the documented historical rural-education analysis and using the released data structure; any new identification claim requires separate design assessment.
linkable_keys:
- County code or normalized county name
- Census wave or year
- Individual or household identifier where present in the deposited file

joins:
- target: china-census
  relation: complement
  keys:
  - Census wave
  - County identifier
  method: compare file definitions and boundary concordances before merging
  evidence_status: literature-used
- target: cfps
  relation: complement
  keys:
  - Individual or household identifier where retained
  - County or province identifier where available
  - Survey year
  method: use the deposited CFPS extract only for the paper-compatible fields; obtain the provider's current wave and codebook separately for new work
  evidence_status: literature-used

access_routes:
- route: openICPSR AEA replication project
  access_status: available-with-registration
  direct_url: https://www.openicpsr.org/openicpsr/project/119690/version/V1/view
  requirements:
  - openICPSR account or the current repository terms/download flow
  - Sufficient storage for the 230.8MB 1990 census file and other deposited files
  steps:
  - Open project 119690 V1 and inspect the project description, SourceData, DoFile, WorkData, README, and LICENSE entries.
  - Record the exact file citation and version before downloading.
  - Download only the files needed for the research question, beginning with the relevant census, county, county-year, or CFPS file.
  - Read the deposited README and code before interpreting labels or constructing a new panel.
  deliverable: Cleaned Stata files, code, documentation, and paper-specific work data as deposited by the authors; not a new raw census or gazetteer release.
  cost: free
  last_checked: '2026-09-28'
  caveat: Current DataCite metadata verifies the active, findable deposit and matching openICPSR route, but not a deposit license or current download terms. Public metadata pages are readable without a full file download, while the download flow may require login, terms acceptance, or repository-side approval.
- route: Provider sources for new reconstruction
  access_status: available-with-conditions
  direct_url: https://www.isss.pku.edu.cn/cfps/en/
  requirements:
  - Current CFPS registration or application if a new CFPS wave is needed
  - Institutional or library access to the cited China Statistics Press books and any local-gazetteer materials
  steps:
  - Use the openICPSR deposit as the specification of the paper's prepared fields.
  - Verify the current CFPS wave, census product, and yearbook definitions with their original providers.
  - Rebuild only the missing component and compare it with the deposited file; do not infer a source field from the paper title or abstract.
  deliverable: Provider-specific survey, census, or yearbook data with its own access and license conditions.
  cost: mixed
  last_checked: '2026-08-11'
  caveat: This route is for extending or independently rebuilding the data, not proof that the paper's full upstream compilation is currently reproducible.

access:
  url: https://www.openicpsr.org/openicpsr/project/119690/version/V1/view
  cost: free
  license: See the deposited LICENSE.txt and the terms of the original census, CFPS, yearbook, and gazetteer sources; openICPSR states that material is distributed as received from the depositor.
  format:
  - dta
  - do
  - pdf
  - txt
  api: false
  how_to_get: Open the project, inspect the version and file metadata, accept the current terms, and download the needed files from SourceData, WorkData, and DoFile.
caveats:
- The integrated files are research outputs with authors' cleaning and matching choices, not neutral replacements for the original censuses or gazetteers.
- File names and metadata establish existence and size, but exact variable labels, county coverage, and constructed-field definitions require reading the deposited code and labels.
- The CFPS file in the deposit is a prepared 2010 extract; it does not replace the provider's broader CFPS archive or current access rules.
- School statistics cited in the paper may require CNKI or library access to the named China Statistics Press books.
- Administrative boundaries and county names can change across census waves; any merge to another panel needs an explicit concordance.

production:
  raw_sources:
  - name: Chinese population census waves
    source_type: dataset
    role: Individual-level census inputs for the cleaned 1982, 1990, 2000, and 2010 files
    access_route: Deposited cleaned files in SourceData; original census access is separate
    url: https://www.openicpsr.org/openicpsr/project/119690/version/V1/view?path=%2Fopenicpsr%2F119690%2Ffcr%3Aversions%2FV1%2FSourceData&type=folder
    coverage: China rural population; wave- and file-specific coverage must be read from labels
    last_checked: '2026-08-11'
  - name: Local gazetteer compilation
    source_type: document
    role: Historical county-level measures used in the paper's integrated dataset
    access_route: Cited by the paper and represented in cleaned deposited files; raw gazetteer files not confirmed in the SourceData listing
    url: https://www.aeaweb.org/articles?id=10.1257/aer.20191414
    coverage: Historical county information for the paper's rural education application
    last_checked: '2026-08-11'
  - name: CFPS 2010
    source_type: dataset
    role: Individual-level comparison or outcome component in the deposited paper files
    access_route: Deposited CFPS_2010_clean.dta; original CFPS provider route remains separate
    url: https://www.isss.pku.edu.cn/cfps/en/
    coverage: 6,320 cases and 20 variables in the deposited cleaned extract according to openICPSR metadata
    last_checked: '2026-08-11'
  - name: China Statistics Press school-statistics books
    source_type: document
    role: 1978-1984 school and enrollment series cited for tables in the paper
    access_route: CNKI or institutional/library access as documented in the authors' replication instructions
    url: https://www.cnki.net/
    coverage: China Compendium of Statistics 1949-2008 and China Rural Statistical Yearbook 1985, with table-specific use
    last_checked: '2026-08-11'
  acquisition_methods:
  - repository download
  - census-file cleaning
  - document extraction
  - entity and county matching
  sample_construction: The deposit separates SourceData, WorkData, and DoFile. The main research artifact is a set of cleaned census and county files; the paper's analysis sample and any exclusions are encoded in the deposited code and should not be inferred from the repository-wide file sizes.
  pipeline_stages:
  - stage: collect
    inputs:
    - Chinese census files
    - Local gazetteer information
    - CFPS 2010
    - School-statistics books
    method: Assemble the authors' source materials and deposit the cleaned inputs and documentation.
    tools:
    - Stata
    output: SourceData and documented source references
    evidence: AER article abstract and openICPSR project description; project 119690 V1 README and SourceData listing
  - stage: clean
    inputs:
    - Census source files
    - CFPS 2010
    method: Apply the deposited Stata cleaning scripts and retain labels and wave-specific files.
    tools:
    - Stata 14 or later
    output: census_1982_clean.dta, census_1990_clean.dta, census_2000_clean.dta, census_2010_clean.dta, and CFPS_2010_clean.dta
    evidence: openICPSR DoFile folder metadata and SourceData file metadata
  - stage: match
    inputs:
    - Cleaned census files
    - County and county-year files
    - Gazetteer-derived fields
    method: Use the authors' code to link individuals and county records and create work data for the paper's tables.
    tools:
    - Stata
    output: county_data.dta, county_year_data.dta, and paper-specific work files
    evidence: openICPSR WorkData and DoFile project structure; exact field mapping remains a code-reading item
  - stage: validate
    inputs:
    - Deposited cleaned files
    - Paper tables and appendix
    method: Run the supplied table and appendix scripts and compare sample counts and outputs with the publication.
    tools:
    - Stata
    output: Reproduction tables and documented discrepancies
    evidence: AEA replication package link and openICPSR DoFile metadata
  constructed_variables:
  - name: county and county-year historical measures
    concept: Researcher-constructed county records combining historical source material and census-based measures
    source_fields:
    - County identifiers
    - Census fields
    - Gazetteer-derived fields
    method: As specified in the deposited code; exact formulae are not asserted until the relevant do-files are inspected.
    validation: Compare code output with the released county_data.dta and county_year_data.dta and publication tables.
    limitations: The deposit does not by itself prove that the original gazetteer pages or every intermediate match are available.
  output:
    unit_of_observation: Individual, county, or county-year depending on file
    structure: Repeated cross-section and county panel
    geography: China rural population and county units described in project metadata
    time_span: 1982, 1990, 2000, 2010 census waves plus paper-specific historical county-year files
    key_variables:
    - Education and demographic fields
    - County identifiers and historical measures
    - County-year education outcomes
    formats:
    - dta
  reproducibility:
    level: medium
    starting_point: https://www.openicpsr.org/openicpsr/project/119690/version/V1/view
    code_available: true
    code_url: https://www.openicpsr.org/openicpsr/project/119690/version/V1/view?path=%2Fopenicpsr%2F119690%2Ffcr%3Aversions%2FV1%2FDoFile&type=folder
    requirements:
    - openICPSR access and storage for the large census files
    - Stata 14 or later
    - User-written Stata command logout if required by the deposited scripts
    - Source-specific access for books or any missing upstream materials
    blockers:
    - Exact source-file and variable construction provenance requires code and README inspection.
    - Raw local gazetteers are not confirmed in the public SourceData file listing.
    - Current repository download terms and original-source redistribution rights must be checked.
  compliance:
    terms_or_license: Inspect project LICENSE.txt and original provider terms; openICPSR disclaims independent processing and distributes material as received.
    robots_or_rate_limits: Use the repository download route; do not scrape census or gazetteer sites to fill undocumented fields.
    personal_or_sensitive_data: Individual census and survey records may contain sensitive demographic information; follow repository and source terms.
    redistribution: Do not redistribute downloaded microdata or derivative files without checking the deposited license and source restrictions.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-11'

used_by:
- cite: 'Chen, Fan, Gu & Zhou (2020), Arrival of Young Talent: The Send-Down Movement and Rural Education in China'
  doi: https://doi.org/10.1257/aer.20191414
  journal: AER
  year: 2020
  dataset_role: Integrated county-level historical data and population-census files for rural education, occupation, marriage, and family outcomes, with a CFPS 2010 component
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/119690/version/V1/view
  data_note: >-
    The AER page describes a county-level dataset compiled from local gazetteers and population censuses. The openICPSR V1
    SourceData listing provides cleaned census files for 1982, 1990, 2000, and 2010, county_data.dta, county_year_data.dta,
    CFPS_2010_clean.dta, and NBS_data.dta; the 1990 file has 3,558,270 cases and 26 variables, and the CFPS extract has 6,320
    cases and 20 variables. The deposit is therefore a concrete paper-used data route, but it should not be described as a
    public release of the raw gazetteers or the original national census microdata.

provenance:
- source: AER article and replication page https://www.aeaweb.org/articles?id=10.1257/aer.20191414
  field_scope:
  - paper identity
  - paper data role
  - county-level source description
  - research outcomes
  added: '2026-08-11'
  confidence: high
  verified: true
- source: openICPSR project 119690 V1 SourceData metadata https://www.openicpsr.org/openicpsr/project/119690/version/V1/view?path=%2Fopenicpsr%2F119690%2Ffcr%3Aversions%2FV1%2FSourceData&type=folder
  field_scope:
  - deposited file names
  - file sizes
  - source-folder citation
  - project universe and observation units
  added: '2026-08-11'
  confidence: high
  verified: true
- source: openICPSR census_1990_clean.dta metadata https://www.openicpsr.org/openicpsr/project/119690/version/V1/view?path=%2Fopenicpsr%2F119690%2Ffcr%3Aversions%2FV1%2FSourceData%2Fcensus_1990_clean.dta&type=file
  field_scope:
  - 1990 file size
  - variable count
  - case count
  added: '2026-08-11'
  confidence: high
  verified: true
- source: openICPSR CFPS_2010_clean.dta metadata https://www.openicpsr.org/openicpsr/project/119690/version/V1/view?path=%2Fopenicpsr%2F119690%2Ffcr%3Aversions%2FV1%2FSourceData%2FCFPS_2010_clean.dta&type=file
  field_scope:
  - CFPS file size
  - variable count
  - case count
  added: '2026-08-11'
  confidence: high
  verified: true
- source: openICPSR README and DoFile metadata https://www.openicpsr.org/openicpsr/project/119690/version/V1/view?path=%2Fopenicpsr%2F119690%2Ffcr%3Aversions%2FV1%2FREADME.pdf&type=file
  field_scope:
  - deposited documentation route
  - code and license availability
  - remaining construction questions
  added: '2026-08-11'
  confidence: med
  verified: true
- source: DataCite API record 10.3886/E119690V1, queried 2026-09-28
  field_scope:
  - current active, findable ICPSR v1 deposit identity and openICPSR route
  - title, 2020 publication year, China geography, and county-gazetteer/census dataset description
  - does not establish a deposit license, current download terms, or public reproducibility of original census, gazetteer, yearbook, or CFPS inputs
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-census
  relation: complement
- id: cfps
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is the authors' downloadable, paper-specific bundle of cleaned Chinese census, county, county-year, and CFPS files for historical rural education research. Its value is the integrated county and individual-ready starting point; its main boundary is that the public deposit does not automatically expose every original gazetteer, book, or census-production step.

## Select rules

- Prioritize it when the idea needs the paper's historical county education files or the exact prepared census inputs.
- Use the general census or CFPS records when the idea needs current waves, provider-level documentation, or a survey beyond the deposited extract.
- Read the labels and code before treating a field as a county exposure, outcome, or comparable census measure.

## Get recipe

1. Open openICPSR project 119690 V1 and inspect README, LICENSE, SourceData, WorkData, and DoFile.
2. Download the relevant cleaned census or county file and record its file citation and version.
3. Read the supplied code to identify sample restrictions, variable construction, and county-name or boundary handling.
4. For extensions, obtain the original CFPS, census, yearbook, or gazetteer source under its own terms and compare it with the deposited file before merging.

## Connections and Limitations

The natural join unit is county plus census year or county-year, but exact codes and boundary vintages must be verified in the files. The deposited CFPS extract can complement the county files for the paper's intended individual-level analyses, while the general CFPS and Census records remain the authoritative routes for new waves and access conditions. No causal or policy classification is encoded in this data record.
