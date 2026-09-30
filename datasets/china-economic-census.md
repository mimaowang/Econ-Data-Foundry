---
schema_version: 3
catalog_status: grounding
id: china-economic-census
name: China Economic Census / Industrial Census (中国经济普查/工业普查)
aka:
- 经济普查
- 工业普查
- 全国经济普查
- Chinese Industrial Census
- CIC
- 第三次工业普查
- 第一次经济普查
- 第二次经济普查
provider: National Bureau of Statistics (NBS, 国家统计局)
china_related: true
domains:
- firm
- macro
- development
- IO
- labor
- trade
data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: The wave- and variable-specific microdata extract, sample, or controlled-environment output actually approved by NBS; for the Brandt et al. paper, a constructed 1992/1995/2004/2008 firm file and main analysis file built from those inputs
  availability: restricted
  ordinary_researcher_feasible: false
  summary: Economic Census collection aims at broad enumeration, but a researcher's obtainable deliverable is defined by NBS approval and may be a sample, selected variables, controlled-environment access, or export-limited output. The ReStud replication package supplies code, concordances, selected derived files, and documentation, but not the confidential census inputs or the paper's complete main file. Public aggregate tables are a separate direct route.
  barrier: Microdata requires formal NBS application, institutional affiliation, and confidentiality agreement. Most researchers access it through university-NBS partnerships or designated data laboratories.
unit_of_observation: 'Census frame: legal entity, establishment unit, or self-employed business in a census year; researcher-obtainable deliverable: approval-specific extract, sample, or controlled-environment output'
structure: repeated-cross-section-census
geo_granularity:
- enterprise
- County
- city
- province
geography: All mainland China (all provinces, autonomous regions, and municipalities)
time_span:
  start: 1992
  end: 2023
  last_confirmed_release: 2024-12-26 public aggregate bulletins for the 2023 reference year
  coverage_note: The 1992 Industrial Census is an additional paper-used input; Brandt, Kambourov & Storesletten's README lists raw CIC inputs for 1992, 1995, 2004, and 2008, while the headline regional comparisons emphasize 1995/2004/2008. National Economic Census reference years are 2004, 2008, 2013, 2018, and 2023. NBS has published 2023 aggregate bulletins; this record does not confirm that 2023 microdata are available through the application route.
  last_checked: "2026-08-11"
frequency:
- quinquennial
sample_size: 'Paper-used industrial microdata: 1995 ~0.53M firms, 2004 ~1.37M, 2008 ~2.08M. Official 2023 aggregates report 33.270M legal entities, 36.360M establishment units, and 87.995M self-employed businesses in the second and third sectors; these aggregate counts do not imply that equivalent microdata are obtainable.'
key_variables:
- Gross output
- Value added
- Employment
- Gross capital stock
- Depreciation
- Total wage bill
- Year of establishment
- Ownership type (state/collective/private/foreign/JV/etc.)
- Main industry/sector classification
- Registered capital
- Revenue
research_fit:
  best_for:
  - Broad firm-size and establishment distributions when an approved microdata extract actually includes the required small entities
  - Regional comparisons of manufacturing productivity and barriers to entry
  - Structural estimation of entry costs, capital wedges, and output wedges across locations
  choose_over:
  - Choose an approved census extract over ASIF when the delivered wave and scope include the small firms or establishments needed for the design
  - Choose ASIF over CIC when you need annual panel data (1998–2013) rather than quinquennial cross-sections
  not_good_for:
  - Annual firm panels (use ASIF)
  - Annual or post-census firm dynamics; 2023 aggregate results are public, but this record does not confirm 2023 microdata access
  - Household or individual outcomes (use CFPS/CHNS/census microdata)
  needs_join_for:
  - Pollution, patent, trade, or policy outcomes — join by firm name/identifier, industry code, and location
  variation_available:
  - 1995 Industrial Census and 2004/2008/2013/2018 Economic Census waves used or discussed in research
  - 2023 Economic Census aggregate variation; microdata availability requires separate confirmation
  - Cross-prefecture and cross-industry variation
  - Before/after policy changes spanning census years
  - Ownership type comparisons
topics:
- firm entry and exit
- productivity dispersion
- industrial structure
- regional development
- ownership and privatization
good_for:
- Measuring firm entry barriers, productivity dispersion, and the full firm-size distribution across Chinese regions
- Structural models of industry dynamics requiring the universe of firms
- Benchmarking ASIF coverage against a broader census frame when the approved extract supports the comparison
identification:
- Cross-sectional variation across prefectures and industries
- Before/after comparisons across census waves
- Structural estimation (Hopenhayn model, etc.)
linkable_keys:
- Firm name
- Industry code (GB/T 4754)
- Prefecture/county code
- Ownership type
joins:
- target: asif
  relation: complement
  keys:
  - Firm name or identifier
  - Industry code
  - Year (census years overlap with ASIF)
  method: entity-resolution
  evidence_status: literature-used
- target: china-census
  relation: complement
  keys:
  - County/city/prefecture code
  - Industry code (aggregated)
  method: aggregation
  evidence_status: plausible
access_routes:
- route: NBS microdata application
  access_status: by-application
  direct_url: https://microdata.stats.gov.cn/
  requirements:
  - Institutional affiliation
  - Research project proposal
  - Confidentiality agreement
  - May require on-site use in NBS-designated laboratory
  steps:
  - Confirm target census wave and variable catalog
  - Submit application through institution
  - Sign data use and confidentiality agreement
  - Access desensitized microdata in approved environment
  deliverable: Approved census microdata sample; specific waves, variables, and export permissions depend on approval
  cost: by-application
  last_checked: "2026-08-11"
  caveat: Approval timing and the accessible fields are not guaranteed. Desensitization or controlled access may remove precise identifiers. Cross-wave comparisons require careful concordance work.
- route: Authors' Zenodo replication package
  access_status: available
  direct_url: https://zenodo.org/records/14872511
  requirements:
  - Free download of MS28536_data.zip (5.2 MB; MD5 a44784ba060006b105254a263368e442)
  - Stata/MP 18.0 for the authors' full scripts
  - Separate legitimate access to the NBS CIC and population-census inputs for complete reruns
  steps:
  - Download the version-1 package and read MS28536_readme_file_2025_BKS.pdf before using any file
  - Use the /1_data_CIC do-files and supplied concordances only after obtaining the confidential 1992/1995/2004/2008 raw CIC files through NBS or an approved secured portal
  - Use /2_data_main to build the paper-specific main file, then /3_figures_tables/Run_all_results.do for tables and figures
  deliverable: Public CC BY 4.0 package containing Stata code, README, concordances, deflators, selected derived DTA files, and result inputs; it does not contain the raw CIC files or the complete BKS_main_data_file_92_95_04_08.dta
  cost: mixed
  last_checked: "2026-08-11"
  caveat: Zenodo metadata marks the package open and licensed CC BY 4.0, but the README says the NBS CIC and population-census originals cannot be purchased from a vendor and must be obtained through formal NBS application or secured university portals. The raw files were obtained by the authors in November 2012, so current file structure may differ; a successful package download alone cannot reproduce the paper.
- route: Published aggregate tabulations
  access_status: available
  direct_url: https://data.stats.gov.cn/
  requirements:
  - None for public aggregate data
  steps:
  - Search NBS data portal by census year, geography, and industry
  - Download or record aggregate indicators
  deliverable: Publicly available aggregate statistics at province/city/county/industry levels
  cost: free
  last_checked: "2026-07-14"
access:
  url: https://microdata.stats.gov.cn/
  cost: by-application
  license: Public Zenodo replication files are CC BY 4.0; NBS microdata and population-census inputs cannot be redistributed and remain subject to approval-specific terms
  format:
  - dta
  - csv
  api: false
  how_to_get: Submit formal application to NBS Microdata Laboratory; aggregate tables available at data.stats.gov.cn
caveats: Microdata access requires uncertain lead time and approval-specific scope. Industry codes change across census waves — manual concordance is needed. Ownership classification also changed (especially around the SOE reform period). Unlike ASIF (annual panel), CIC is quinquennial and cannot track firms at annual frequency. Pre-2004 coverage is limited to the industrial sector; later census scope is broader, but the obtainable microdata deliverable must be confirmed in the approved environment.
quality:
  profile_status: partial
  access_status: partial
  paper_use_status: verified
  last_audited: "2026-08-11"
used_by:
- cite: 'Chen, Chen, Liu, Suárez Serrato & Xu (2025), Regulating Conglomerates: Evidence from an Energy Conservation Program in China'
  doi: https://doi.org/10.1257/aer.20211455
  journal: AER
  year: 2025
  dataset_role: 2004 Economic Census input for structural-estimation moments and firm-size/output benchmarks
  evidence_type: data_appendix
  evidence_url: https://assets.aeaweb.org/asset-server/files/22048.pdf
  data_note: Table A.36 identifies the 2004 Economic Census alongside ASIF and CARD as a source for the model moments. This
    confirms paper use of a census input, not a public release of the paper's matched file; obtain the needed wave and fields
    through the NBS route described above and keep it separate from the annual ASIF panel.
- cite: 'Brandt, Kambourov & Storesletten (2025), Barriers to Entry and Regional Economic Growth in China'
  doi: https://doi.org/10.1093/restud/rdaf029
  journal: ReStud
  year: 2025
  dataset_role: Main firm-level dataset — 1995/2004/2008 Industrial Census waves covering all manufacturing firms
  evidence_type: replication
  evidence_url: https://zenodo.org/records/14872511
  data_note: >-
    The paper's CIC inputs are the 1992, 1995, 2004, and 2008 NBS files; the three headline manufacturing waves contain about
    0.53M, 1.37M, and 2.08M firm records respectively. The public Zenodo package (5.2 MB, CC BY 4.0) includes the README,
    Stata construction/result code, industry and prefecture concordances, deflators, and selected derived DTA files. It lists
    the raw census filenames and the variables in the combined file but marks every raw CIC file and the constructed
    BKS_main_data_file_92_95_04_08.dta as not provided. It therefore supports reproducible transformations and result code
    conditional on legitimate access to the restricted census and population-census inputs, not a public release of the paper's
    complete microdata or final analysis file.
- cite: 'Tang, Gao & You (2025), Structural Transformation and the Urban Growth Shadows: County-Level Evidence from China, 1990-2020'
  doi: https://doi.org/10.1016/j.regsciurbeco.2025.104141
  journal: RSUE
  year: 2025
  dataset_role: Economic Census data providing county-level economic structure measures
  evidence_type: data-section
  evidence_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4765694
  data_note: Uses Economic Census data alongside Population Census and county statistical yearbooks to measure economic structure across 2,225 counties. Documents how structural transformation interacts with urban growth shadows — counties with initially higher agricultural employment shares experience greater population outflows to nearby cities, while counties with initial manufacturing/service advantages become shadow-casters rather than shadowed.
provenance:
- source: Brandt et al. (2025) paper and online appendix confirming CIC coverage, variables, and concordance methods
  added: "2026-07-12"
  confidence: high
  verified: true
- source: https://zenodo.org/records/14872511
  field_scope:
  - replication package
  - 1992/1995/2004/2008 raw-file boundary
  - derived files and Stata code
  - README variable list and build sequence
  - CC BY 4.0 package license and 5.2 MB MD5 manifest
  - restricted-source caveat
  added: '2026-08-11'
  confidence: high
  verified: true
- source: NBS microdata.stats.gov.cn confirming application channel for census microdata
  added: "2026-07-12"
  confidence: high
  verified: true
- source: NBS Fifth National Economic Census bulletin series confirming the 2023 reference year, covered unit types, completion, and public aggregate results
  url: https://www.stats.gov.cn/sj/tjgb/jjpcgb/
  field_scope:
  - 2023 reference year
  - official unit scope and aggregate counts
  - aggregate publication status
  added: "2026-07-14"
  confidence: high
  verified: true
- source: https://assets.aeaweb.org/asset-server/files/22048.pdf
  field_scope:
  - AER paper use of 2004 Economic Census
  - structural-moment source distinction
  added: "2026-08-11"
  confidence: high
  verified: true
related_datasets:
- id: asif
  relation: complement
- id: china-census
  relation: complement
---
## Positioning in one sentence
China's Economic Census is a quinquennial enumeration of legal entities, establishment units, and self-employed businesses in the second and third sectors; the related 1995 Industrial Census is also used in the research literature. It offers broader scope than ASIF, but the public aggregate bulletins, an approved microdata extract, and a paper's final analysis file are different deliverables. The 2023 aggregates are public; 2023 microdata availability is not confirmed by this record.

## Select rules
- When broad census-frame coverage, including smaller establishments, is essential and the approved extract confirms the needed unit scope
- When structural estimation of entry barriers or firm dynamics can be supported by the delivered census wave and identifiers
- Switch to ASIF when annual panel frequency is essential and above-scale coverage is sufficient
- Public 2023 aggregates can support aggregate analysis; do not promise 2023 microdata or sub-annual dynamics without route-specific evidence

## Get recipe
1. Download the authors' Zenodo package and read its README to distinguish supplied concordances/derived files from missing raw inputs
2. Confirm your institution has an existing NBS data partnership or is willing to sponsor an application
3. Contact NBS Microdata Laboratory (microdata.stats.gov.cn) with a proposal naming the 1992/1995/2004/2008 CIC files, or the other wave and variables actually needed
4. Sign the confidentiality agreement and use the approved data in its controlled environment; only then run the supplied /1_data_CIC and /2_data_main scripts
5. For aggregate statistics, use data.stats.gov.cn directly (free, no application)

## Connections and Limitations
- The Zenodo package supplies industry and prefecture concordances for the paper's 1992/1995/2004/2008 construction, but not a universal cross-dataset identifier
- Concordance with ASIF possible via firm name/identifier matching for census years (1995, 2004, 2008)
- Industry code concordances (GB/T 4754 versions) needed for cross-wave comparisons
- Prefecture/county boundary changes require geographic concordances
- Ownership classification schemes changed significantly across waves
- Desensitization removes precise addresses and firm identifiers — matching to other databases may require fuzzy methods
