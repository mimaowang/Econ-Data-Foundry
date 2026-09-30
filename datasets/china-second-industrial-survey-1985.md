---
schema_version: 3
catalog_status: grounding
id: china-second-industrial-survey-1985
name: China Second Industrial Survey (1985) firm-level dataset
aka:
- Second Industrial Census
- 第二次工业普查
- 1985 Industrial Survey
- 1985年第二次工业普查数据
provider: National Bureau of Statistics of China (Statistics China)
china_related: true
domains:
- firm
- industrialization
- regional
- urban
- productivity
- economic-history

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: 1985 firm-level survey records for the largest industrial firms, with paper-specific matching to the 139 final 156-Project projects
  availability: restricted
  ordinary_researcher_feasible: false
  summary: The survey is a historical cross-section that the ReStud authors manually digitised and matched to project firms. It supplies output, sales, profits, fixed assets, and employees for 7,592 large firms across 40 industries, but the original records and the authors' cleaned match are not publicly released.
  barrier: Access requires formal NBS approval or a controlled institutional route. The paper's Zenodo package contains synthetic data and code, not the confidential 1985 survey.

unit_of_observation: Firm record in the 1985 industrial survey
structure: cross-sectional-firm-survey
geo_granularity:
- firm
- county
- province
geography: Mainland Chinese industrial firms covered by the 1985 survey; the paper uses 7,592 largest firms and matches 139 projects
time_span:
  start: '1985'
  end: '1985'
  last_confirmed_release: '2026-05-05'
  coverage_note: The paper reports 7,592 firms across 40 industries. Exact geographic inclusion, identifiers, questionnaire version, and missingness require an approved file or codebook.
  last_checked: '2026-08-11'
frequency:
- cross-sectional
sample_size: 7,592 largest firms in the paper's reported extract
key_variables:
- Firm name and location
- Industry
- Output
- Sales
- Profits
- Fixed assets
- Employees
- Ownership and capital fields where present

research_fit:
  best_for:
  - Historical 1985 firm performance and baseline comparisons for early industrialization research
  - Matching large industrial firms to the 156-Project register when a pre-ASIF benchmark is needed
  choose_over:
  - Choose this survey over ASIF when the question is specifically about the 1985 cross-section and the project-compatible firm universe.
  - Choose ASIF for annual 1998-2013 firm panels and later manufacturing dynamics.
  - Use the Zenodo synthetic package only to inspect code and output structure, not as a substitute for the actual 1985 observations.
  not_good_for:
  - Annual firm panels, current firms, household outcomes, or small enterprises outside the survey universe
  - Treating the paper's manual match as a public NBS release
  needs_join_for:
  - 156-Project identity and plant outcomes
  - County/city population and regional controls
  - Post-1998 firm outcomes from ASIF
  variation_available:
  - 1985 firm characteristics and cross-sectional regional differences are data dimensions; no causal or treatment assignment classification is recorded here.
  topics:
  - historical firms
  - industrialization
  - early Chinese manufacturing
  - regional development
  - firm productivity

good_for:
- Historical firm-level output and capital benchmarks around the early industrialization period
- A documented pre-ASIF cross-section when a researcher can obtain controlled access
identification: []
linkable_keys:
- Firm name
- County or province
- Industry
- 1985

joins:
- target: china-million-rouble-plant-register
  relation: complement
  keys:
  - Firm/project name
  - Location
  method: Use the paper's manual name/location/province matching and preserve unmatched cases
  evidence_status: literature-used
- target: asif
  relation: complement
  keys:
  - Firm name
  - County/province
  - Industry
  method: Construct a documented concordance; do not assume firm identifiers persist from 1985 to 1998
  evidence_status: literature-used
- target: china-census
  relation: complement
  keys:
  - County
  - Province
  - Year
  method: Administrative concordance and 1985 timing alignment
  evidence_status: plausible

access_routes:
- route: NBS formal application or authorized institutional portal
  access_status: needs-verification
  direct_url: https://www.stats.gov.cn/sj/tjgb/gypcgb.html
  requirements:
  - Formal research project and institutional sponsorship.
  - Confirmation that the 1985 Second Industrial Survey is in the current catalogue.
  - Confidentiality or controlled-use agreement and approved analysis environment.
  steps:
  - Ask NBS or the authorized institutional data centre for the 1985 survey codebook, sample, and geographic identifiers.
  - Submit the project, variables, matching plan, and output-control request.
  - Record the approved file version and restrictions before matching it to project or regional data.
  deliverable: Controlled 1985 firm-level records or approved aggregate output; no public micro-download is established.
  cost: by-application
  last_checked: '2026-08-11'
  caveat: The ReStud README describes formal NBS approval but does not provide a public application form, guaranteed fields, or processing time.

- route: ReStud Zenodo synthetic replication package
  access_status: available
  direct_url: https://zenodo.org/records/19175276
  requirements:
  - Download the 51.2MB package and read its README.
  - Python 3.9+ and Stata 16+ for the synthetic workflow.
  steps:
  - Use the synthetic scripts only to understand the paper's output and code structure.
  - Keep synthetic firm records separate from any real NBS survey observations.
  deliverable: Synthetic calibrated data and code; not the original Second Industrial Survey.
  cost: free
  last_checked: '2026-08-11'
  caveat: The package cannot answer a new empirical question about actual 1985 firms because the original survey is confidential.

access:
  url: https://zenodo.org/records/19175276
  cost: by-application for original data; free for synthetic package
  license: Original survey access is controlled by NBS; Zenodo package terms and source restrictions remain separate.
  format:
  - dta
  - do
  - py
  - csv
  api: false
  how_to_get: Treat the Zenodo package as a synthetic documentation route. For actual observations, begin with NBS or an authorized institutional application.

caveats:
- The 7,592-firm figure is the paper's reported extract, not a promise about a current release.
- The 139-project match is manually constructed and should not be reused without its matching rules and boundary checks.
- Survey definitions and identifiers may not be comparable to ASIF without a documented concordance.
- Synthetic data reproduce code and calibrated patterns, not the historical records.

production:
  raw_sources:
  - name: Second Industrial Survey (1985)
    source_type: dataset
    role: Firm output, sales, profits, fixed assets, and employment
    access_route: NBS formal application or authorized institutional portal
    url: https://www.stats.gov.cn/sj/tjgb/gypcgb.html
    coverage: 7,592 largest firms across 40 industries in the paper's extract
    last_checked: '2026-08-11'
  acquisition_methods:
  - records request
  - manual digitisation
  - manual matching
  sample_construction: The authors manually digitised the confidential survey and matched 139 projects using firm name, location, and province.
  pipeline_stages:
  - stage: collect
    inputs:
    - 1985 survey records
    method: Obtain approved survey files and codebook from NBS or an authorized centre.
    output: Controlled firm cross-section
    evidence: ReStud Section 3.3 and Zenodo README
  - stage: match
    inputs:
    - Survey firms
    - 156 Project list
    method: Match by firm name, location, and province with manual uniqueness checks.
    output: 139-project firm benchmark
    evidence: ReStud Section 3.3
  - stage: validate
    inputs:
    - Matched survey
    - Paper tables and diagnostics
    method: Reproduce approved aggregates and compare the project match counts; exact code and original files remain restricted.
    output: Paper-compatible firm benchmark
    evidence: ReStud Section 3.3 and Zenodo README
  validation:
  - Verify the approved universe, year, industry coverage, and identifier fields.
  - Preserve unmatched firms and document any boundary or name normalization.
  output:
    unit_of_observation: Firm
    structure: 1985 cross-section
    geography: Chinese industrial firms in the approved survey
    time_span: '1985'
    key_variables:
    - Output
    - Sales
    - Profits
    - Fixed assets
    - Employees
    formats:
    - controlled files
    - paper-specific Stata data
  reproducibility:
    level: not-reproducible
    starting_point: NBS application and ReStud README
    code_available: true
    code_url: https://zenodo.org/records/19175276
    requirements:
    - Approved NBS access
    - Secure analysis environment
    - Manual matching if the paper's prepared file is not supplied
    blockers:
    - Original survey and matched file are not publicly released
    - No public codebook or stable microdata download was verified
  compliance:
    terms_or_license: Follow NBS confidentiality and output-control rules
    robots_or_rate_limits: Not applicable to controlled access
    personal_or_sensitive_data: Firm records may be confidential
    redistribution: No redistribution without explicit permission
    review_needed: true

quality:
  profile_status: verified
  access_status: restricted
  paper_use_status: verified
  last_audited: '2026-08-11'

used_by:
- cite: 'Giorcelli & Li (2026), Technology Transfer and Early Industrial Development: Evidence from the Sino-Soviet Alliance'
  doi: https://doi.org/10.1093/restud/rdag047
  journal: ReStud
  year: 2026
  dataset_role: 1985 firm-level baseline matched to 139 final 156-Project projects
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845
  data_note: The article reports confidential 1985 Second Industrial Survey data for 7,592 largest firms across 40 industries, with output, sales, profits, fixed assets, and employees, and says the authors manually matched 139 projects by name, location, and province. The Zenodo package releases only synthetic data and code.

provenance:
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845
  field_scope:
  - survey identity, 1985 coverage, 7,592 firms, and 139-project match
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/19175276
  field_scope:
  - synthetic replication boundary
  - original survey access limitation
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/api/records/19175276/files/Replication_Package_260506.zip/content
  field_scope:
  - README-described NBS access route and synthetic workflow
  added: '2026-08-11'
  confidence: high
  verified: true

related_datasets:
- id: asif
  relation: complement
- id: china-steel-plant-performance-reports
  relation: complement
- id: china-million-rouble-plant-register
  relation: complement
---

## Positioning in one sentence

The 1985 Second Industrial Survey is a restricted historical firm cross-section that fills a gap before ASIF's commonly used panel years. The paper's synthetic Zenodo package helps understand the workflow but does not make the 7,592 real firms downloadable.

## Select rules

- Use it for a 1985 firm baseline when the project-compatible match and historical industrial coverage matter.
- Use ASIF for annual 1998-2013 firm outcomes, and the Steel Association Reports for plant-level steel physical outputs and technology.
- Do not infer a public NBS release from the paper's synthetic package.

## Get recipe

Start with the NBS/authorized-institution route and request the 1985 survey codebook, identifiers, and output permissions. Use the ReStud README and synthetic code only as a specification of the desired fields and matching logic.

## Connections and limitations

The useful join keys are name, location, province, and industry, but these are not stable universal identifiers. Preserve a manual match log and treat the 139-project linkage as a paper-specific research product, not a general firm registry.
