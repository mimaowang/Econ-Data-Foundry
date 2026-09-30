---
schema_version: 3
catalog_status: grounding
id: china-steel-plant-performance-reports
name: China Steel Association plant annual performance reports
aka:
- Steel Association Reports
- 中国钢铁工业协会钢铁企业年度报表
- Chinese steel plant annual reports
provider: China Steel Association; current custodial/access route named by the authors is the Ministry of Industry and Information Technology (MIIT)
china_related: true
domains:
- industrialization
- regional
- urban
- firm
- economic-history
- productivity

data_pathway:
  mode: inaccessible
  origin: researcher-constructed
  target_artifact: Plant-year performance panel digitised from restricted Steel Association annual reports, with paper-specific matches to the 304 steel plants in 20 industrial clusters
  availability: restricted
  ordinary_researcher_feasible: false
  summary: This is the plant-level historical source behind the core steel outcomes in Giorcelli and Li (2026 ReStud). It contains physical production, product quality, inputs, machinery/technology, and worker categories for 1949-2000, but the original reports and the authors' digitised panel are not publicly downloadable.
  barrier: The authors state that the reports are restricted government data and the README directs researchers to formal approval from MIIT. The Zenodo package contains only synthetic data calibrated to the paper's results, not the original records.

unit_of_observation: Steel plant-year record; the paper's matched analysis sample has 304 plants in 20 steel industrial clusters
structure: historical-plant-panel
geo_granularity:
- plant
- county
- province
geography: Chinese steel plants represented in the Steel Association records and the paper's matched plant sample; exact national inclusion outside the paper sample is not established
time_span:
  start: '1949'
  end: '2000'
  last_confirmed_release: '2026-05-05'
  coverage_note: Annual reports were collected for 1949-2000. The paper manually matches plant name, location, county, and province to 304 plants; the underlying custodial series may have its own completeness and boundary limits.
  last_checked: '2026-08-11'
frequency:
- annual
sample_size: 304 matched steel plants in 20 industrial clusters in the paper; article describes reports for all plants operating in the steel industry, but a complete public inventory is not available
key_variables:
- Steel product quantity and quality
- Output in steel, crude steel, and pig iron
- Input usage
- Capital and labor inputs
- Machinery and technology in use
- Unskilled workers
- High-skilled workers
- Engineers
- Plant name and location fields used for matching

research_fit:
  best_for:
  - Historical plant-level steel production, productivity, technology adoption, and worker composition before and after China's industrialization period
  - Research that needs physical-output measures unavailable in the general ASIF firm panel
  choose_over:
  - Choose this source over ASIF when the question requires pre-2000 steel-plant physical output, product quality, machinery, or worker-type measures.
  - Choose ASIF or the Second Industrial Survey for broader firm coverage and financial variables, subject to their own access limits.
  - Use the public Zenodo package only for code/synthetic workflow checks; it cannot substitute for the original panel.
  not_good_for:
  - Current steel production monitoring or a public national firm census
  - General manufacturing or service firms outside the steel-plant records
  - Treating the source as a released causal-treatment dataset
  needs_join_for:
  - 156 Project identity and plant-transfer fields
  - County or city outcomes from census and statistical yearbooks
  - Firm-level post-1998 outcomes from ASIF
  variation_available:
  - Plant-year production, technology, and worker categories are data dimensions; no causal or transfer-assignment classification is recorded here.
  topics:
  - steel industry
  - historical industrialization
  - plant productivity
  - technology adoption
  - worker skills
  - regional development

good_for:
- Plant-level historical output and technology measures where the paper's restricted source is obtainable through an approved route
- Understanding why the paper's synthetic replication files cannot answer a new empirical question
identification: []
linkable_keys:
- Plant name
- Plant location
- County
- Province
- Year

joins:
- target: china-million-rouble-plant-register
  relation: complement
  keys:
  - Plant name
  - Location
  - Project or cluster identifier
  method: Use the paper's historical matching files and document any name or boundary normalization
  evidence_status: literature-used
- target: asif
  relation: complement
  keys:
  - Plant/firm name
  - County or province
  - Year
  method: Match only with documented identifiers or manual checks; the 1998-2000 overlap does not imply a common firm panel
  evidence_status: literature-used
- target: china-census
  relation: complement
  keys:
  - County
  - Year
  method: Administrative concordance; preserve the source boundary vintage
  evidence_status: plausible

access_routes:
- route: MIIT formal data-access request
  access_status: needs-verification
  direct_url: https://wap.miit.gov.cn/gxsj/index.html
  requirements:
  - Formal research project and institutional sponsorship.
  - Approval from the relevant MIIT data-access office and compliance with current Chinese data rules.
  - A precise request for years, plant fields, and permitted analysis environment.
  steps:
  - Contact the MIIT industrial-data access office named in the replication README.
  - Ask whether the Steel Association Reports for 1949-2000 and the required plant fields can be accessed, and record the approval scope.
  - Use the approved secure route; do not request or redistribute copies outside the agreement.
  deliverable: Controlled access to selected official reports or a secured analysis environment; no public download is established.
  cost: by-application
  last_checked: '2026-08-11'
  caveat: The README gives the formal-approval route but not a public application form, fee schedule, processing time, or guaranteed fields.

- route: ReStud Zenodo synthetic replication package
  access_status: available
  direct_url: https://zenodo.org/records/19175276
  requirements:
  - Download the 51.2MB package and read the README.
  - Python 3.9+ and Stata 16+ for the synthetic workflow.
  steps:
  - Run the synthetic data-generation scripts only to inspect code structure and output format.
  - Keep synthetic data clearly labeled and do not use it as an empirical substitute for the original records.
  deliverable: Synthetic calibrated plant panels, code, figures, and original do-files for reference; no original Steel Association Reports.
  cost: free
  last_checked: '2026-08-11'
  caveat: The package is useful for computational and documentation checks, not for estimating new effects or reproducing the underlying facts without the restricted inputs.

access:
  url: https://zenodo.org/records/19175276
  cost: by-application for original data; free for synthetic package
  license: Original reports are subject to government access rules; Zenodo package rights and upstream restrictions must be checked before reuse.
  format:
  - pdf
  - dta
  - do
  - py
  - csv
  - xls
  api: false
  how_to_get: Treat the Zenodo package as a synthetic workflow. For the actual panel, start with a formal MIIT request and obtain only the approved reports or secure output.

caveats:
- The public synthetic panel is calibrated to published coefficients and sample structure; it does not contain or reconstruct identifiable original plant records.
- The authors note possible measurement and reporting issues in historical official data; preserve this limitation when using an approved extract.
- Plant-to-project matching is author-built and uses name, location, county, and province; a new join must not rely on plant names alone.
- The article's 304-plant sample should not be generalized to all Chinese steel firms or all years without source-level verification.

production:
  raw_sources:
  - name: Steel Association annual reports
    source_type: document
    role: Plant-year performance, products, inputs, machinery, technology, and workers
    access_route: MIIT formal approval
    url: https://wap.miit.gov.cn/gxsj/index.html
    coverage: 1949-2000 annual plant reports; exact completeness and fields are access-dependent
    last_checked: '2026-08-11'
  acquisition_methods:
  - records request
  - digitisation
  - manual matching
  sample_construction: The authors manually collected and digitised the restricted reports, then uniquely matched 304 plants using plant name, location, county, and province.
  pipeline_stages:
  - stage: collect
    inputs:
    - Steel Association Reports
    tools:
    - Manual archive work
    method: Obtain approved reports and select the required annual plant records.
    parameters: 1949-2000 and paper-compatible steel-plant fields
    output: Digitised plant-year records
    evidence: ReStud Section 3.2 and Zenodo README
  - stage: extract
    inputs:
    - Annual reports
    tools:
    - Manual digitisation
    method: Transcribe product, input, technology, and worker fields from the reports; exact transcription protocol is not released.
    output: Researcher-built plant panel
    evidence: ReStud Section 3.2
  - stage: match
    inputs:
    - Digitised plant records
    - 156 Project and cluster files
    method: Match by plant name, location, county, and province and manually check uniqueness.
    output: 304-plant analysis sample
    evidence: ReStud Section 3.2
  - stage: validate
    inputs:
    - Plant panel
    - Historical technology/archive records
    method: Compare production and technology measures with complementary historical archives and paper diagnostics; exact validation files are restricted.
    output: Paper analysis files
    evidence: ReStud Section 3.2 and Appendix B
  validation:
  - Confirm the approved extract's years, plant universe, and field definitions before analysis.
  - Reproduce only approved aggregate outputs; do not attempt to reconstruct unapproved micro-records.
  output:
    unit_of_observation: Plant-year
    structure: Annual historical panel
    geography: Chinese steel plants in the approved source and paper sample
    time_span: 1949-2000
    key_variables:
    - Product quantity and quality
    - Inputs and capital
    - Technology and machinery
    - Worker categories
    formats:
    - controlled files
    - paper-specific Stata data
  reproducibility:
    level: not-reproducible
    starting_point: Zenodo README and formal MIIT access request
    code_available: true
    code_url: https://zenodo.org/records/19175276
    requirements:
    - Approved MIIT access
    - Institutional secure environment
    - Manual digitisation and matching if the original panel is not supplied
    blockers:
    - Original reports and digitised panel are restricted
    - No public field-level codebook or download was found
  compliance:
    terms_or_license: Follow MIIT/NBS access agreement and current Chinese data rules
    robots_or_rate_limits: Not applicable to the controlled records request
    personal_or_sensitive_data: Firm and plant records may be confidential
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
  dataset_role: Core plant-level output, productivity, technology, and worker outcomes
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845
  data_note: The article says it manually collected and digitised annual Steel Association Reports for 1949-2000, then matched 304 steel plants in 20 clusters. It lists physical output, product quality, inputs, machinery/technology, and worker categories; the Zenodo README confirms the original records are restricted and that only synthetic calibrated data are released.

provenance:
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845
  field_scope:
  - article identity and Steel Association data role
  - 1949-2000 coverage and 304-plant match
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/19175276
  field_scope:
  - synthetic package identity and size
  - original-data restriction boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/api/records/19175276/files/Replication_Package_260506.zip/content
  field_scope:
  - README-described access route and synthetic workflow
  - software requirements and data-generation boundary
  added: '2026-08-11'
  confidence: high
  verified: true

related_datasets:
- id: china-million-rouble-plant-register
  relation: complement
- id: asif
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

This is a restricted historical steel-plant panel source, not the freely downloadable synthetic files in the paper's Zenodo package. It is valuable for physical production and technology measures that ASIF does not provide, but a new researcher should plan around formal access uncertainty rather than assume that the replication package unlocks the original records.

## Select rules

- Choose it when the idea needs historical steel-plant output, product quality, machinery, or worker types.
- Choose ASIF for broader firm coverage, financial variables, and post-1998 industrial panels.
- Use the Zenodo package to understand code and output shape only; use approved original data for substantive estimates.

## Get recipe

First inspect the Zenodo README to identify fields and software. Then contact the MIIT industrial-data access office with a bounded request for the relevant Steel Association years and plant fields. If access is granted, preserve the approved plant key and reproduce only the paper-compatible transformations.

## Connections and limitations

The plant key can be joined to the paper's project/cluster files and to ASIF or census outcomes, but boundary and name changes matter. The source does not provide a public national panel, and the exact field-level access decision belongs to the custodial authority.
