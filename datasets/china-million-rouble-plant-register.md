---
schema_version: 3
catalog_status: ready
id: china-million-rouble-plant-register
name: China Million-Rouble Plant register and replication asset
aka:
- 156 Programme plant register
- Million-Rouble Plants (MRPs)
- 中国156项重点工程厂址数据
- 一五计划156项重点工程
provider: Heblich, Seror, Xu & Zylberberg; historical sources include Dong (1999), Dong & Wu (2004), and Chinese historical archives
china_related: true
domains:
- regional
- urban
- industrialization
- economic-history
- spatial

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: Public Zenodo replication package 20671189 containing the paper's plant register, location files, direct-descendant links, public raw inputs, code, and documentation
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The package provides a usable historical plant register and geospatial starting files, so a researcher can begin with the authors' coded plant locations rather than re-transcribing the historical books. Rebuilding the full county and establishment outputs still requires confidential NBS census and ASIF inputs, licensed patent data, and the documented GIS/Stata pipeline.
  barrier: The 1.05GB public package is a paper-specific replication bundle, not a neutral current factory census. Several upstream files are proprietary, confidential, manually collected, or subject to third-party rights; the current deposit is CC-BY-4.0, but that deposit-level licence does not settle rights in every upstream source.

unit_of_observation: Plant, direct descendant, plant location, and plant-to-county spatial record (separate files in the replication package)
structure: historical-register-plus-spatial-replication-bundle
geo_granularity:
- plant coordinates
- county
- prefecture-level city
- province
geography: Mainland China plant locations and host counties represented in the authors' register; exact file-level boundary vintage must be read from the package labels
time_span:
  start: '1950s'
  end: '2010'
  last_confirmed_release: '2026-07-08'
  coverage_note: The programme plants were built in the 1950s; the paper follows plant and host-county outcomes from 1953 through 2010. The register records location, construction timing, initial investment, original industry, and later evolution, while the exact year coverage of each file is package-specific.
  last_checked: '2026-08-11'
frequency:
- event-dated
- irregular historical panel
sample_size: 149 geolocated/operational Million-Rouble Plants in the paper's treatment register; 156 is the programme label and not the count of final operational plants
key_variables:
- Plant identity and name
- Location and host county
- Construction timing
- Initial investment
- Original industry
- Later production/evolution fields where available
- Direct-descendant links
- Spatial files and county joins used by the replication code

research_fit:
  best_for:
  - Joining the historically coded Million-Rouble Plant locations to county, city, firm, census, or spatial outcomes in studies of long-run industrialization and local production structure
  - Starting from a documented public register when the research needs the paper's plant identities and locations rather than a current industrial-firm directory
  choose_over:
  - Choose this register over a generic policy list when the exact paper-compatible plant identity, location, construction period, and descendant files are required.
  - Choose ASIF, census, or statistical yearbooks for outcomes and controls; this register does not substitute for those sources.
  - Use the separate variation repository for institutional assignment and causal-design interpretation; this record only describes the obtainable data artifact and its joins.
  not_good_for:
  - A current census of all Chinese factories or a complete production time series for every plant
  - Firm-level outcomes outside the listed plants and descendants
  - Treating the released register as proof of exogeneity, treatment assignment, or a causal estimate
  needs_join_for:
  - County population, urbanization, migration, and sector outcomes from the China Census
  - Establishment production, productivity, patent, and markup outcomes from ASIF and linked patent data
  - Annual regional controls from the China Statistical Yearbook
  variation_available:
  - Plant location, construction timing, and descendant relationships are data dimensions in the register; no causal or exogenous-shock classification is recorded here.
  topics:
  - Million-Rouble Plants
  - 156 Programme
  - industrial clusters
  - place-based industrialization
  - county development
  - historical economic geography

good_for:
- Reusing the paper's plant-level spatial inventory and direct-descendant files
- Building county or city joins for long-run industrial-cluster and local-production research
- Reproducing the plant-location starting point while preserving the distinction between public files and restricted outcomes
identification:
- This is a historical spatial register and replication asset, not a current factory census or a causal-shock record. Plant siting and its causal interpretation require separate design evidence and are outside this data record.
linkable_keys:
- Plant name or register identifier
- Plant coordinates
- Normalized county/city name and code
- Year or event date

joins:
- target: china-census
  relation: complement
  keys:
  - Host county or city
  - Census year
  method: Explicit geographic concordance; preserve the paper's county boundary vintage before aggregating outcomes
  evidence_status: literature-used
- target: asif
  relation: complement
  keys:
  - Plant or descendant name
  - Firm name/identifier
  - County and year
  method: Use the paper's documented establishment links and name/identifier cleaning; raw ASIF access remains separate
  evidence_status: literature-used
- target: china-patents
  relation: complement
  keys:
  - Establishment name or matched firm identifier
  - Patent application year
  method: Use the He et al. (2018) establishment-to-patent links or a separately licensed patent product; do not infer matches from names alone
  evidence_status: literature-used
- target: china-stat-yearbook
  relation: complement
  keys:
  - County/city identifier
  - Year
  method: Align administrative boundaries and measurement definitions before joining annual controls
  evidence_status: plausible

access_routes:
- route: Zenodo public replication package
  access_status: available-with-conditions
  direct_url: https://zenodo.org/records/20671189
  requirements:
  - Download PUBLIC_PACKAGE.zip (about 1.1GB) and README.pdf.
  - Check the current Zenodo version, checksum, and rights information before reuse; the current record is open and labels the deposit CC-BY-4.0.
  - Install Stata MP 17, Python 3.8.3, and ArcGIS Pro 2.9 only if rebuilding the full pipeline.
  steps:
  - Open the record and read the README before unpacking or running code.
  - Start with the provided Data/Public/Raw/Stata/Factories/Factories.txt, Factories/FactoryLocations.xlsx, and direct-descendant files; keep public and confidential folders separate.
  - If full reproduction is needed, obtain the licensed ASIF, patent, census, and other restricted inputs named in the README, then follow Code/Master.do and the GIS sequence.
  deliverable: Public plant-register spreadsheets/text files, selected public GIS and auxiliary inputs, Stata/Python/GIS code, documentation, and paper-specific derived outputs; not the confidential census, ASIF, or patent inputs.
  cost: mixed
  last_checked: '2026-09-28'
  caveat: >-
    The current Zenodo API lists two open files: README.pdf (497,835 bytes; MD5 60cb18117b302f86bcf05ad858bde630) and PUBLIC_PACKAGE.zip (1,052,415,593 bytes; MD5 4a946756aff3a3e277fc5bca221167aa). The package is directly downloadable but is not a general public release of every source used in the paper; third-party source and redistribution terms must still be checked before sharing derivatives.

access:
  url: https://zenodo.org/records/20671189
  cost: mixed
  license: CC-BY-4.0 for the current Zenodo deposit; follow the README and the rights of each upstream source.
  format:
  - zip
  - xlsx
  - txt
  - csv
  - shp
  - dta
  - do
  - py
  api: false
  how_to_get: Open the current Zenodo record, download README.pdf and PUBLIC_PACKAGE.zip, verify their listed checksums, inspect the public/confidential folder structure, and use the provided plant files first. Apply separately for or purchase each restricted input needed to reproduce county or establishment outcomes.

caveats:
- The 149-plant register and the 156 Programme label are different counts; do not silently replace one with the other.
- Plant locations, construction dates, descendants, and county joins are author-assembled research files. Administrative boundaries and names must be reconciled before a new join.
- The public package can reproduce the register and code starting point, but not the full analysis without restricted NBS census/ASIF data, licensed patent data, and the stated software/GIS workflow.
- The register records a historical industrial asset; it is not a current operating-status database and does not itself encode a causal design.

production:
  raw_sources:
  - name: Historical Million-Rouble Plant sources
    source_type: document
    role: Plant identity, location, construction, industry, and historical evolution
    access_route: Author-provided files in the Zenodo public package; cited sources include Dong (1999), Dong & Wu (2004), and historical archives
    url: https://zenodo.org/records/20671189
    coverage: The programme plants and direct descendants represented in the paper's register; source-level coverage remains file-specific
    last_checked: '2026-08-11'
  - name: NBS above-scale firm data (ASIF)
    source_type: dataset
    role: Recent plant activity and establishment outcomes linked to the register
    access_route: Licensed vendor or institutional route named in README.pdf
    url: https://zenodo.org/records/20671189
    coverage: 1998-2007 establishment data in the paper; raw files are not publicly redistributed
    last_checked: '2026-08-11'
  - name: NBS population censuses and 1% surveys
    source_type: dataset
    role: County-level population, urbanization, migration, and sector outcomes
    access_route: NBS application or secured university portal; the Zenodo package documents the required inputs
    url: https://microdata.stats.gov.cn/
    coverage: Historical census and 1% survey waves named in the paper; approved waves and variables are access-dependent
    last_checked: '2026-08-11'
  acquisition_methods:
  - download
  - manual coding
  - geocode
  - match
  - aggregate
  sample_construction: The authors combine manually coded historical plant information with spatial and establishment links; the released register should be treated as the paper's prepared starting point rather than as a neutral raw archive.
  pipeline_stages:
  - stage: collect
    inputs:
    - Historical plant books and archives
    tools:
    - Manual coding
    method: Manually transcribe and reconcile historical plant sources as documented by the authors; use the provided register as the released starting point.
    parameters: Plant identity, location, construction timing, investment, industry, and later evolution as documented in the README
    output: Factories.txt, FactoryLocations.xlsx, and related plant files
    evidence: Zenodo README.pdf, Data Availability and Raw Data Summary
  - stage: match
    inputs:
    - Plant register
    - Direct-descendant sources
    - NBS establishment input
    tools:
    - Stata
    method: Apply the paper's documented plant and descendant/establishment links; exact name and identifier rules remain package-specific.
    parameters: Paper-specific name and identifier links
    output: Direct-descendant files and establishment-linked plant measures
    evidence: Zenodo README.pdf and the paper's Section 3.1.1
  - stage: geocode
    inputs:
    - Factory location files
    - Administrative GIS files
    tools:
    - Python
    - ArcGIS Pro 2.9
    method: Run the documented GIS sequence to map plant locations and join administrative files.
    parameters: Package GIS sequence and paths
    output: Plant shapefiles and county/spatial intermediate files
    evidence: Zenodo README.pdf, Further instructions—GIS
  - stage: validate
    inputs:
    - Public register
    - Replication code and tables
    tools:
    - Stata MP 17
    - Python 3.8.3
    method: Re-run the documented cleaning and analysis programs and compare outputs with released exhibits where restricted inputs are available.
    output: Paper tables, figures, and documented intermediate files where restricted inputs are available
    evidence: Zenodo README.pdf, Computational Requirements and Instructions to Replicators
  constructed_variables:
  - name: Host-county plant exposure/join fields
    concept: Spatial linkage from plant locations to the paper's county units
    source_fields:
    - Plant coordinates
    - Administrative boundary files
    method: Package GIS and concordance code; do not infer a new boundary rule from the register alone
    validation: Compare the released plant maps and county files with the package documentation
    limitations: Boundary vintage, coordinate precision, and file-level exclusions must be checked before reuse
  validation:
  - Compare the plant count and register files with the README's 149-geolocated-plant description.
  - Preserve the public/confidential folder distinction and compare any rebuilt outputs with released paper exhibits.
  output:
    unit_of_observation: Plant, descendant, location, or host-county record depending on file
    structure: Historical register and spatial replication files
    geography: Mainland China locations represented by the authors
    time_span: 1950s-2010, with file-specific event and outcome windows
    key_variables:
    - Plant identity and location
    - Construction and industry fields
    - Direct descendants
    - County joins
    formats:
    - txt
    - xlsx
    - csv
    - shp
    - dta
  reproducibility:
    level: medium
    starting_point: Zenodo PUBLIC_PACKAGE.zip and README.pdf
    code_available: true
    code_url: https://zenodo.org/records/20671189
    requirements:
    - 1.1GB download plus working storage
    - Stata MP 17
    - Python 3.8.3
    - ArcGIS Pro 2.9 for GIS outputs
    - Licensed ASIF, census, patent, and other restricted inputs for full reproduction
    - Approximately 50-200 hours reported by the authors for the full run
    blockers:
    - Proprietary/confidential raw inputs are not included
    - Third-party source rights and current package licence are not fully displayed
  compliance:
    terms_or_license: The current Zenodo deposit is CC-BY-4.0; each upstream provider's terms still govern third-party source material.
    robots_or_rate_limits: Not applicable to the Zenodo download
    personal_or_sensitive_data: Restricted firm and census inputs may contain confidential information; do not redistribute them
    redistribution: Public plant files and derivatives remain subject to source-specific rights
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-11'

used_by:
- cite: 'Heblich, Seror, Xu & Zylberberg (2026), Industrial Clusters in the Long Run: Evidence from Million-Rouble Plants in China'
  doi: https://doi.org/10.1093/restud/rdag078
  journal: ReStud
  year: 2026
  dataset_role: Historical Million-Rouble Plant identity, location, construction, industry, and evolution inputs for county-level industrial-cluster analysis
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  data_note: The paper says plant information was extracted primarily from Bo (1991), Dong (1999), Dong & Wu (2004), and historical archives, with recent activity obtained from establishment-level data. The public Zenodo package supplies the coded register and direct-descendant/location files, while confidential firm and census inputs remain separate.

provenance:
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  field_scope:
  - ReStud paper identity and data-section description
  - plant source families and 149/156 count distinction
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/20671189
  field_scope:
  - public replication package identity and file availability
  - package size and public/confidential boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/api/records/20671189/files/README.pdf/content
  field_scope:
  - raw-source provenance
  - folder names, software requirements, and reproduction limits
  added: '2026-08-11'
  confidence: high
  verified: true
- source: Zenodo API record 20671189, queried 2026-09-28
  field_scope:
  - current open-record status and CC-BY-4.0 deposit licence
  - current package title and publication date
  - named README.pdf and PUBLIC_PACKAGE.zip files, sizes and MD5 checksums
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: asif
  relation: complement
- id: china-census
  relation: complement
- id: china-stat-yearbook
  relation: complement
- id: china-patents
  relation: complement
- id: china-steel-plant-performance-reports
  relation: complement
- id: china-second-industrial-survey-1985
  relation: complement
---

## Positioning in one sentence

This is a public, paper-specific historical register of the Million-Rouble Plants and their spatial/descendant files, not a live factory directory or a causal-variation record. It is useful because it preserves the authors' coded plant identities and locations; its main limitation is that the county and establishment outcomes still depend on restricted NBS/ASIF/census inputs.

## Select rules

- Use it when a regional or urban research idea needs the paper-compatible historical plant locations and direct descendants.
- Join it to the census, yearbooks, ASIF, or patent records for outcomes; do not ask the register to supply those outcomes.
- Keep any claim about assignment, exogeneity, or causal interpretation in the separate variation repository.

## Get recipe

Download the Zenodo package, read README.pdf, inspect the public Factories files, and record the exact version and rights before use. If the research requires the paper's county or establishment estimates, separately obtain the confidential inputs and reproduce only the documented Stata/GIS stages needed for the intended artifact.

## Connections and limitations

The plant register is most valuable as a stable spatial key. County names and boundaries changed over the long period, and the paper's code may use a particular administrative vintage; any merge to a modern panel should preserve the original key and document the concordance. A downloaded package is therefore a strong starting point, not a guarantee that a new researcher can recreate every result.
