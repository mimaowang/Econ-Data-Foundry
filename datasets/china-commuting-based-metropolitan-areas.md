---
schema_version: 3
catalog_status: ready
id: china-commuting-based-metropolitan-areas
name: China's commuting-based metropolitan areas (Chen, Gu & Zou 2024 JUE; delineation files on Mendeley Data 10.17632/9ng8663r8c.1)
aka:
- 基于通勤的中国都市区
- 中国通勤都市圈划分
- China's Commuting-Based Metropolitan Areas
- Delineating China's Metropolitan Areas Using Commuting Flow Data
- 10.17632/9ng8663r8c.1
provider: Data originally produced by a leading Chinese digital-map/navigation company (paper anonymizes the provider in the data section; acknowledgements thank the Baidu Maps Open Platform department); the paper's authors (Chen, Gu, Zou) compiled the township-level commuting matrix and delineations; Mendeley Data distributes the replication files
china_related: true
domains:
- urban
- regional
- labor
- transport
- spatial
- agglomeration

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: "Mendeley Data dataset 10.17632/9ng8663r8c.1 'China's Commuting-based Metropolitan Areas (Replication Files)' - a public 270-file replication deposit (9,538,905,568 bytes in API metadata), including _RunAll.do, README, township MA-membership files at seven thresholds (2%-30%), township-to-county intersection files, and named commuting-flow/sample files. It is a directly obtainable derived MA-boundary route; filenames alone do not establish that any one file is the complete provider matrix."
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The paper's MA delineation files and code are downloadable from Mendeley Data under CC BY 4.0. The underlying township-pair commuting matrix was produced by a Chinese digital-map/location company (Baidu Maps Open Platform per acknowledgements; anonymized in the data section) from three months of smartphone location data ending November 2017, covering all 39,764 townships of China. The raw company-side location data are not publicly available; only the derived commuting flows and delineations enter the research pipeline.
  barrier: The current public Mendeley API exposes the completed V1 file manifest and public-file download URLs, but the full 9.54 GB deposit requires substantial local storage and the API metadata does not reveal table columns or prove that a named commuting-flow file is the complete provider matrix. The paper full text itself is ScienceDirect subscriber-only, but the authors' October 2024 preprint was read in full from an author-hosted copy.

unit_of_observation: Township (乡镇; 39,764 townships of mainland China) - commuting flows between township pairs; MA = cluster of townships merged by iterative clustering
structure: Cross-sectional commuting matrix (township-pair flows) with derived cluster (MA) membership at multiple thresholds
geo_granularity:
- township (乡镇; lowest administrative rung)
- county (2,855; used for validation and coarsened delineations)
- MA (township clusters, also mapped to county boundaries)
geography: All mainland China - 39,764 townships (31 province-level units, 333 prefecture units, 2,855 county units, ~40,000 township units per 2017 administrative divisions)
time_span:
  start: '2017-09'
  end: '2017-11'
  last_confirmed_release: '2024-10-22'
  coverage_note: "Commuting matrix based on typical daytime (workplace) and nighttime (home) locations recorded over the three months ending November 2017; MA delineations derived from that single cross-section. Replication files published 2024-10-22 (DataCite Issued date). No later waves documented in the preprint."
  last_checked: '2026-09-28'
frequency:
- cross-sectional (single three-month observation window ending 2017-11)
sample_size: 39,764 townships; median township population 21,967 (paper Table 1), company app about 600 million active users in mainland China in 2017; threshold-2% clustering yields 9,261 clusters, preferred 10% threshold delineation reported for top MAs
key_variables:
- Township-level population, residence employment, workplace employment (company-inferred, validated against 2020 census and 2015 1% population survey)
- Commuting flows between township pairs (matrix; share of workers commuting between units)
- MA membership at thresholds 2%, 5%, 10%, 15%, 20%, 25%, 30% (iterative clustering following Duranton 2015)
- MA population, area, skill share (college share of adult population), wage premium, firm TFP, house price elasticities used in the paper's city-size analyses

research_fit:
  best_for:
  - Defining Chinese cities as local labor markets beyond administrative boundaries - any research idea needing a commuting-based city/MA definition (agglomeration, sorting, wage premia, local labor markets)
  - Comparing China's functional urban system with US/Brazil/Mexico delineations built with the same algorithm and threshold
  - Selecting threshold (2%-30%) and imposing population/density restrictions for researcher-specific city definitions
  choose_over:
  - Choose over administrative prefecture/county definitions when the question concerns the functional economic extent of cities (commuting-based MAs differ substantively; e.g. Beijing MA extends beyond the municipality; Chongqing MA is only ~40% of the municipality's population)
  - Choose over nightlight/built-up morphological delineations when actual labor-market connection matters (commuting flows reveal e.g. Guangzhou-Shenzhen as two clusters despite contiguous nightlight)
  not_good_for:
  - Time-series or panel analysis of city boundaries (single 2017 cross-section; no repeated waves documented)
  - Pre-2017 or post-2017 MA definitions from this asset (delineations are pinned to the 2017-11 commuting matrix)
  - Device-level or individual-level mobility research (only aggregated township flows; the company's demographics inference algorithm is not accessible)
  - Official/administrative city definitions where policy relevance requires gazetteer boundaries
  needs_join_for:
  - City-level outcomes (wages, skills, firm productivity, house prices) from census, firm, or transaction data to exploit MA definitions - the paper itself joins census, firm and housing data to document size premia
  - Population censuses (2020) and the 2015 1% survey for validation and demographic coarsening
  - GIS shapefiles (2010 census township boundaries updated to the flow data's townships) for mapping and coarsening to county boundaries
  variation_available:
  - Cross-sectional variation across MAs of different sizes and ranks; threshold choice (2%-30%) as a robustness dimension; MA-vs-administrative boundary misalignment correlated with local economic development
  topics:
  - metropolitan areas
  - local labor markets
  - commuting flows
  - city size distribution
  - agglomeration
  - China urbanization
  - smartphone location data

good_for:
- Commuting-based delineation of Chinese metropolitan areas as local labor markets
- City-size distribution (power law) and size premia analysis
identification:
- This is a spatial-definition asset, not an identification design: it supports defining functional local-labor-market units and joining outcomes to them, but neither the released boundary files nor the underlying smartphone flows alone establish a causal effect.
linkable_keys:
- Township name/ID (39,764 townships; matched to 2010 census GIS shapefiles; exact identifier scheme per replication files - unverified)
- County (2,855) for coarsened delineations
- MA membership at each threshold (2%-30%)

joins:
- target: china-census
  relation: complement
  keys:
  - Township
  - County
  method: Paper validates flow-data populations against the 2020 census and uses the 2015 1% survey (work/home townships) for commuting-flow validation; 2010 census township shapefiles are the GIS base for boundaries
  evidence_status: literature-used
- target: china-stat-yearbook
  relation: complement
  keys:
  - City
  - County
  method: Official population counts from censuses and statistical-yearbook estimates used to corroborate the cellphone-based flows
  evidence_status: literature-used

access_routes:
- route: Mendeley Data replication files (DOI 10.17632/9ng8663r8c.1)
  access_status: available
  direct_url: https://data.mendeley.com/datasets/9ng8663r8c/1
  requirements:
  - Download the selected public files or the full deposit; current V1 API metadata marks the deposit available and non-confidential, and exposes public-file URLs.
  - Allow up to 9,538,905,568 bytes if obtaining the whole deposit; individual named files can be selected from the manifest instead.
  steps:
  - Open https://doi.org/10.17632/9ng8663r8c.1 or the dataset landing page, then use the V1 manifest to select a threshold-specific boundary file.
  - For a township MA definition, obtain one of `town_2017_.02.dta`, `.05`, `.1`, `.15`, `.2`, `.25`, or `.3`; `.1` is the paper's preferred 10% threshold.
  - Obtain the matching `town_county_intersect_2017_*.dta` when a county crosswalk is needed. `_RunAll.do`, `README.pdf`, `README.docx`, `WithinCommShare_town_CN.dta`, `WithinCommShare_county_CN.dta`, and a file named `commuting_flow.dta` are also listed in the current manifest.
  - Cite as Chen, Gu & Zou, "China's Commuting-based Metropolitan Areas (Replication Files)", Mendeley Data, doi:10.17632/9ng8663r8c.1 (2024).
  deliverable: Public V1 replication deposit with code, README, threshold-specific township MA memberships, township-county intersection crosswalks and additional named analysis files; the manifest alone does not document every table's columns or prove that `commuting_flow.dta` is a complete raw matrix.
  cost: free
  last_checked: '2026-09-28'
  caveat: Mendeley public API V1 verified 270 completed files, 15 folders, CC BY 4.0, available=true and confidential=false on 2026-09-28. No account requirement was observed in the API route; future platform terms can change.
- route: Author preprint (full text, October 2024)
  access_status: available
  direct_url: https://www.dropbox.com/scl/fi/kgguv6o32h649iflaxpo2/ChinaMSA.pdf
  requirements:
  - None (public link surfaced via search; download worked with dl.dropboxusercontent.com raw link on 2026-08-14)
  steps:
  - Download the 57-page preprint "China's Commuting-based Metropolitan Areas" (Ting Chen, Yizhen Gu and Ben Zou, October 2024), which contains the data section, validation, and appendices.
  - SSRN version (abstract 4052749, 2022, 'Delineating China's Metropolitan Areas Using Commuting Flow Data') exists as an earlier WP version; SSRN itself blocks automated clients.
  deliverable: Full preprint text incl. Section 2 (Background and Data), Table 1 summary statistics, validation against census/survey data
  cost: free
  last_checked: '2026-08-14'
  caveat: The Dropbox URL was discovered through search results; link stability is not guaranteed. The published JUE version may differ slightly; ScienceDirect is subscriber-only.
- route: Original company location data
  access_status: no-public-route-found
  direct_url: needs-verification
  requirements:
  - The provider's raw smartphone location records and its demographics-inference algorithm are private; no application or purchase channel is documented in the paper
  steps:
  - Confirm with the data provider (Baidu Maps Open Platform per acknowledgements) whether any research collaboration or data agreement is possible
  - Do not expect access: the paper states the authors themselves lack access to the user composition of inferred demographics and the algorithm
  deliverable: Not available to researchers - only the derived township-level commuting matrix enters the research pipeline
  cost: by-application
  last_checked: '2026-08-14'
  caveat: Paper states the authors do not have access to the user composition of inferred demographics nor the algorithm; treat this route as closed unless the provider offers a new channel.

production:
  raw_sources:
  - name: Chinese digital-map/location company smartphone location data (Baidu Maps Open Platform per acknowledgements; anonymized in data section as 'a leading provider of digital maps and online navigation services')
    source_type: dataset
    role: Raw input - frequent smartphone location records from the company's map app and other apps using its location services, tagged as workplace/home over three months ending November 2017; aggregated township-pair commuting matrix
    access_route: Not public; provided to the authors directly (paper thanks Xiangan Kong and Tianqi Liu of the Baidu Maps Open Platform department)
    url: https://doi.org/10.1016/j.jue.2024.103715
    coverage: About 600 million active users of the company's app in mainland China (2017); devices using its location services in other popular apps; all townships
    last_checked: '2026-08-14'
  acquisition_methods:
  - provided-by-company (not public)
  - download of Mendeley replication files (derived asset)
  sample_construction: Company determines typical daytime (workplace) and nighttime (home) locations per device over three months; infers worker status and demographics from third-party data and its apps; the authors receive the aggregated township-level matrix, not device records.
  pipeline_stages:
  - stage: collect
    inputs:
    - Smartphone location records (company-side)
    method: Provider aggregates frequent location pins into typical daytime/nighttime locations over the three months ending November 2017, then into township-pair commuting flows (39,764 townships)
    tools: []
    parameters:
    - 3-month window ending 2017-11
    - township level aggregation
    output: Township-pair commuting matrix with township population and employment (residence/workplace)
    evidence: Preprint Section 2.2 (read in full 2026-08-14)
  - stage: validate
    inputs:
    - Township-pair commuting matrix
    method: Compare township/county population and employment with 2020 census and 2015 1% population survey; match township GIS boundaries against official shapefiles
    tools: []
    parameters: []
    output: Validated commuting matrix
    evidence: Preprint Section 2.3
  - stage: model
    inputs:
    - Validated commuting matrix
    method: Iterative clustering following Duranton (2015) at thresholds 2%, 5%, 10%, 15%, 20%, 25%, 30%; 10% preferred; delineations also mapped to county boundaries
    tools:
    - Duranton's clustering code (shared by Gilles Duranton, per acknowledgements)
    parameters:
    - threshold 10% preferred
    output: MA membership files at all thresholds
    evidence: Preprint Sections 3 and Appendix
  constructed_variables:
  - name: MA delineations at multiple thresholds
    concept: Township clusters whose internal commuting exceeds the threshold share, defining functional metropolitan areas
    source_fields:
    - Township-pair commuting flows
    method: Duranton (2015) iterative clustering
    validation: Power-law city size distribution, comparisons with US/Brazil/Mexico delineations, cross-checks against administrative and nightlight definitions
    limitations: Single 2017-11 cross-section; threshold choice is a judgment call (paper argues 10%)
  validation:
  - Population counts vs 2020 census (highly correlated, close in levels)
  - Employment by residence/workplace vs 2015 1% population survey (consistent in magnitude and distribution)
  - Township boundaries vs official GIS shapefiles
  output:
    unit_of_observation: Township clusters (MAs) and township-pair commuting flows
    structure: Cross-sectional; cluster membership at thresholds 2%-30%
    geography: Mainland China (39,764 townships)
    time_span: 2017-09 to 2017-11 (data window)
    key_variables:
    - MA membership, MA population/area, commuting flows, township population/employment
    formats:
    - Stata .dta data files
    - Stata .do code
    - README.pdf and README.docx
  reproducibility:
    level: medium
    starting_point: Mendeley Data 10.17632/9ng8663r8c.1 (replication data, code, results); author preprint for the full data section
    code_available: true
    code_url: https://data.mendeley.com/datasets/9ng8663r8c/1
    requirements:
    - Select the needed public V1 file rather than assuming the full 9.54 GB deposit is necessary
    - The raw company-side location data are NOT reproducible by third parties; the released deposit supports the derived boundary route, not recovery of provider device records or the proprietary inference algorithm
    blockers:
    - Raw smartphone location data not publicly obtainable
    - Single cross-section; no updates documented
  compliance:
    terms_or_license: Replication files CC BY 4.0 (DataCite rightsList); raw company data governed by provider agreements not visible to researchers
    robots_or_rate_limits: Current public Mendeley API returned V1 metadata and public-file download URLs; do not automate bulk retrieval without observing current platform limits
    personal_or_sensitive_data: Flow data are aggregated at township level; device-level records never leave the provider per the paper's description
    redistribution: CC BY 4.0 covers the replication files; company data redistribution is not authorized
    review_needed: Inspect the README and selected table columns before treating a named commuting file as the complete matrix or before redistributing a modified subset

access:
  url: https://data.mendeley.com/datasets/9ng8663r8c/1
  cost: free
  license: CC BY 4.0 (replication files)
  format:
  - Stata .dta
  - Stata .do
  - PDF/DOCX README
  api: true
  how_to_get: Open the Mendeley Data V1 landing page or public API metadata, choose a threshold-specific `town_2017_*.dta` plus any needed `town_county_intersect_2017_*.dta`, then download the selected file(s). Read the author preprint for construction and validation. The original company location data are not accessible.
caveats: "The paper's data section anonymizes the provider, but the acknowledgements name the Baidu Maps Open Platform department (people: Xiangan Kong and Tianqi Liu) as the data providers; the anonymous description ('leading provider of digital maps and online navigation services', ~600M active users in 2017) is consistent with that identification. The current V1 manifest establishes named code, README, threshold-membership and crosswalk files, but not their columns, row counts, or whether the 939,899-byte file named `commuting_flow.dta` is the complete township-pair matrix. The raw smartphone records and proprietary demographic inference remain unavailable."

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Chen, Ting, Yizhen Gu and Ben Zou (2024), China''s Commuting-based Metropolitan Areas'
  doi: https://doi.org/10.1016/j.jue.2024.103715
  journal: Journal of Urban Economics
  year: 2024
  dataset_role: Main data - commuting flows derived from smartphone location data used to delineate China's commuting-based metropolitan areas (39,764 townships; three months ending November 2017); MA delineations are the paper's core output
  evidence_type: working_paper_data_section
  evidence_url: https://www.dropbox.com/scl/fi/kgguv6o32h649iflaxpo2/ChinaMSA.pdf
  data_note: "Author preprint (October 2024, 57 pp) read in full on 2026-08-14: Section 2 documents the company-produced township-pair commuting matrix (39,764 townships, ~600M app users in 2017, workplace/home inference over 3 months ending 2017-11), validation against 2020 census and 2015 1% survey, Duranton (2015) iterative clustering at 2%-30% thresholds with 10% preferred, and comparison delineations (administrative, nightlight). Acknowledgements name the Baidu Maps Open Platform department as data providers. Replication files: Mendeley Data 10.17632/9ng8663r8c.1 (2024-10-22, CC BY 4.0, open access; DataCite + Wayback verified). Published JUE version subscriber-only."

provenance:
- source: Author preprint PDF (October 2024) - data section, Table 1, validation section, acknowledgements; read in full via author-hosted Dropbox copy 2026-08-14
  field_scope:
  - data source and construction
  - coverage (townships, window, users)
  - validation
  - MA algorithm and thresholds
  - replication-file citation
  added: '2026-08-14'
  confidence: high
  verified: true
- source: DataCite record for 10.17632/9ng8663r8c.1 (title, creators, issue date 2024-10-22, CC BY 4.0, open access) and Wayback snapshots of the Mendeley landing page (2025-12-06)
  field_scope:
  - replication package identity
  - license and issue date
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Mendeley Data public API, dataset 9ng8663r8c V1 (queried 2026-09-28)
  field_scope:
  - current availability and non-confidential status
  - CC BY 4.0 license
  - 270 completed files in 15 folders and aggregate size 9,538,905,568 bytes
  - file-level public download URLs and named code, README, threshold-membership, crosswalk and commuting-flow files
  added: '2026-09-28'
  confidence: high
  verified: true
- source: IDEAS/RePEc article page and OpenAlex (bibliographic identity; no open full text)
  field_scope:
  - journal, volume, DOI, authors
  added: '2026-08-14'
  confidence: high
  verified: true
- source: PHBS faculty news (2025-02-13) and Xiangzhang Economics blog post (secondary summaries, consistent with the preprint)
  field_scope:
  - corroboration of author affiliations and data description (secondary only)
  added: '2026-08-14'
  confidence: med
  verified: false

related_datasets:
- id: china-nighttime-lights
  relation: often-confused-with
- id: china-city-to-city-truck-flows
  relation: complement
---

## Positioning in one sentence

Chen, Gu & Zou (2024 JUE) provide the first commuting-based delineation of Chinese metropolitan areas, built on a township-pair commuting matrix produced by a Chinese digital-map company (Baidu Maps Open Platform per acknowledgements; anonymized in the data section) from three months of smartphone location data ending November 2017. The MA delineation files (thresholds 2%-30%, 10% preferred) and code are directly downloadable from Mendeley Data under CC BY 4.0; the raw company-side location data are not publicly available.

## Select rules

- Prioritize this asset when a research idea needs Chinese cities as functional local labor markets rather than administrative units - agglomeration, sorting, wage premia, firm productivity, or house-price analyses keyed to city size, or any design that must define cities beyond gazetteer boundaries.
- Switch to administrative delineations (statistical yearbook cities/counties) when the design requires official gazetteer boundaries or long time series; this asset is a single 2017 cross-section.
- Choose commuting-based MAs over nightlight or built-up morphological delineations when actual labor-market connection matters (e.g. PRD appears as one contiguous nightlight area but two commuting clusters, Guangzhou and Shenzhen).
- Not suitable for device-level mobility, panel analysis of boundary change, or any pre/post-2017 city definition.

## Get recipe

1. Open the V1 Mendeley Data record (DOI 10.17632/9ng8663r8c.1) or its public API manifest. Select the MA threshold first: the visible files are `town_2017_.02.dta`, `.05`, `.1`, `.15`, `.2`, `.25`, and `.3`; the paper prefers `.1` (10%).
2. Read the author preprint (Dropbox ChinaMSA.pdf, October 2024) for the full data section, validation, and appendices; the published JUE version is subscriber-only.
3. Select the threshold (2%-30%) appropriate to the question; the paper argues 10%; impose population/density restrictions as needed.
4. When crossing to counties, select the matching `town_county_intersect_2017_*.dta`; otherwise join MA membership to outcome data on the identifiers documented in the selected file. Use 2010 census township shapefiles as the GIS base where required.
5. For validation, compare flow-based population/employment with 2020 census and 2015 1% population survey figures as the paper does.

## Connections and Limitations

- The matrix covers all 39,764 townships of mainland China for the three months ending November 2017; there is no documented update, so the asset pins MA definitions to 2017.
- MA definitions differ substantively from administrative cities (Beijing MA extends beyond the municipality; Chongqing MA is only ~40% of municipal population); the misalignment correlates with local development.
- The provider is anonymized in the data section but identified in the acknowledgements (Baidu Maps Open Platform department); the anonymous description is consistent with Baidu (~600M app users, 2017).
- Raw smartphone location records and the company's demographics-inference algorithm are inaccessible; this record is ready for the released derived MA-definition route, not for recovering those inputs.
- The current public Mendeley API verifies a CC BY 4.0 V1 deposit with 270 completed files (9.54 GB total), including named Stata code, README, seven threshold-membership files and matching township-county intersections. Open the selected table/README before assuming its columns or that a named commuting-flow file is the complete matrix.
