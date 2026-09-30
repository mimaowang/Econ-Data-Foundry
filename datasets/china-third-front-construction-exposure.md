---
schema_version: 3
catalog_status: grounding
id: china-third-front-construction-exposure
name: Third Front (三线建设) industrialization exposure and human-capital outcomes (JCE 2026)
aka:
- Construction of Third Front exposure
- 三线建设
- TF campaign exposure
- 1985 industrial census employment share measure
provider: >-
  Paper authors (Guanghua Fang 方光华, Yinhe Liang 梁银河, Fan Qin 秦帆,
  Tsinghua University School of Economics and Management per the Chinese
  abstract republication) - constructed from public inputs; no release
  identified as of 2026-08-15.
china_related: true
domains:
- regional
- human-capital
- education
- economic-history
- industrial

data_pathway:
  mode: constructed
  origin: researcher-constructed
  target_artifact: >-
    Prefecture-level Third Front (TF) manufacturing exposure measure
    built from the 1985 industrial census (employment share of large and
    medium-sized manufacturing enterprises) joined to 1990 population-census
    microdata for individual human-capital outcomes (schooling, labor-market
    outcomes). Construction per the paper's introduction (Chinese
    translation republication, news.ebiotrade.com 2026-02-02): the TF
    exposure follows Fan & Zou (2021), "the manufacturing capacity built
    during the Third Front era defined as the employment share of large and
    medium-sized manufacturing enterprises listed in the 1985 industrial
    census".
  availability: partially-reproducible
  ordinary_researcher_feasible: false
  summary: >-
    Grounding repair (2026-09-28): the publisher's exposed Data and empirical
    strategy section confirms that the authors follow Fan and Zou (2021), use
    the 1985 Industrial Census to construct prefecture-level TF-built
    manufacturing capacity, and match it to several micro-level survey sources,
    with the 1990 Population Census as the main outcome source. A Chinese
    republication supplies only a secondary description of the
    large/medium-manufacturing-employment-share implementation. The census and
    survey inputs are separately restricted, and the paper's exact sample,
    coding, and regression files remain unavailable.
  barrier: >-
    Closed access (Unpaywall is_oa=false, 2026-08-15); no WP found; the
    exposure-measure details (firm list, county coding, exclusions) are
    only at abstract/intro level via a secondary translation, not the
    paper's own full text. The cited method source is identifiable as Fan and
    Zou (2021, JDE, DOI 10.1016/j.jdeveco.2021.102698), but its indexed Penn
    State repository download currently stops at bot detection rather than
    supplying readable text (2026-09-28); do not treat the repository metadata
    as verification of its construction details.

unit_of_observation: >-
  Individual (census microdata) x local TF exposure; prefecture-level
  exposure measure
structure: individual-level census extract with local exposure measures
geo_granularity:
- prefecture (exposure)
- individual (outcomes)
geography: >-
  China, inland "Third Front" regions vs others; province-level and group
  variation per the paper
time_span:
  start: '1964'
  end: '1990'
  last_confirmed_release: 'No public release identified (2026-08-15)'
  coverage_note: >-
    Campaign started 1964, investment stopped ~1972 (Nixon visit, per the
    translated introduction); outcomes from 1990 census microdata; exposure
    from 1985 industrial census.
  last_checked: '2026-08-15'
frequency:
- cross-section (1990 census) with historical exposure
sample_size: >-
  Unverified (census-microdata based; exact sample in the unread data
  section).
key_variables:
- TF exposure: 1985 industrial-census large/medium manufacturing employment share (Fan & Zou 2021 method)
- Years of schooling (1990 census)
- Labor-market outcomes: employment, non-agricultural occupation, lifetime income, fertility/marriage timing (1990 census based)
- Robustness: Cultural Revolution exposure, selective migration, resource endowments, alternative TF measures

research_fit:
  best_for:
  - Understanding the paper's prefecture-level Third Front exposure measure before seeking separately authorized underlying inputs
  - Historical industrialization and human-capital research when the required census and survey inputs are independently authorized
  choose_over:
  - Choose this constructed route over china-senddown-county-exposure when the campaign of interest is the Third Front (distinct campaign, distinct construction).
  - Use the raw censuses (china-census, china-second-industrial-survey-1985) when only inputs are needed; this record documents the paper-specific exposure recipe.
  not_good_for:
  - Claiming the paper's exact files are reproducible without the unread data section.
  - Campaign-assignment/treatment classification (belongs to Econ-Variation side).
  needs_join_for:
  - Authorized access to the 1990 census microdata and any additional micro-level survey sources used in the paper
  - Authorized access to the 1985 industrial census inputs
  variation_available:
  - Cross-county/cross-province variation in TF-era manufacturing capacity (the paper's identifying variation)
  topics:
  - third front
  - industrialization
  - human capital
  - historical regional development

good_for:
- Third Front exposure construction
- industrialization and education outcomes
- long-run regional development
identification: []
linkable_keys:
- Prefecture identifiers (exposure side; exact coding remains unavailable)
- Individual records (1990 census; restricted)

joins:
- target: china-census
  relation: complement
  keys:
  - individual records (1990 census microdata)
  method: access the 1990 census microdata under its own restricted route; join county exposure by code
  evidence_status: plausible
- target: china-second-industrial-survey-1985
  relation: complement
  keys:
  - prefecture/industry employment
  method: Construct the published prefecture-level capacity measure only after recovering the exact Fan-and-Zou implementation and authorized census inputs.
  evidence_status: plausible

access_routes:
- route: paper-full-text
  access_status: needs-verification
  direct_url: https://www.sciencedirect.com/science/article/pii/S0147596726000016
  requirements: Subscription or library access (closed access)
  steps:
  - Read the data section and appendix for the exact exposure coding, sample, and validation.
  - Recover the fan-out of census extracts and the exposure construction code if available.
  deliverable: Construction recipe; no public data file.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Elsevier 403 for automated clients; no WP found (search 2026-08-15).
- route: Fan--Zou method-source text
  access_status: blocked
  direct_url: https://doi.org/10.1016/j.jdeveco.2021.102698
  requirements: A legitimate session or library route that exposes the method paper's body or appendix.
  steps:
  - >-
    Confirm the source identity: Fan and Zou (2021), “Industrialization from
    scratch: The Construction of Third Front and local economic development in
    China's hinterland,” Journal of Development Economics 152, article 102698.
  - Read its construction and appendix before importing any formula, geography, or firm-selection rule into this record.
  - The indexed ScholarSphere submitted-version route must be checked for actual text delivery; the 2026-09-28 browser visit reached only bot detection.
  deliverable: Primary description of the referenced Third Front construction method, if text is actually delivered.
  cost: mixed
  last_checked: '2026-09-28'
  caveat: Crossref establishes the work identity and OpenAlex indexes a ScholarSphere submitted-version landing URL, but neither proves readable text or the cited method details.
- route: reconstruction-from-public-inputs
  access_status: needs-verification
  direct_url: https://www.stats.gov.cn/
  requirements: 1985 industrial census publications; 1990 census microdata access (restricted route)
  steps:
  - Obtain authorized 1985 industrial-census inputs and the 1990 census microdata route.
  - Recover the exact Fan & Zou (2021) implementation and all other micro-level survey inputs used by the paper.
  - Reconstruct only after the geographic code vintage, sample restrictions, and validation rule are documented from the full text or authors.
  deliverable: At most, a separately documented reconstruction; the current record does not establish a reproducible paper panel.
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Exact coding, prefecture-code vintage, firm inclusion, extra survey inputs, and sample restrictions remain unverified; read the full text or obtain author clarification before reconstruction.

access:
  url: https://doi.org/10.1016/j.jce.2026.01.001
  cost: paid
  license: No public data license identified
  format:
  - paper full text (subscription)
  api: false
  how_to_get: >-
    Read the full paper via library; recover the exact capacity construction,
    all micro-level outcome sources, and sample restrictions before considering a reconstruction.
caveats: >-
  The construction summary comes from a Chinese republication of the
  paper's introduction (news.ebiotrade.com 2026-02-02, 来源: Journal of
  Comparative Economics) - secondary, translated evidence; the paper's own
  full text and appendix are unread. Fan & Zou (2021) is cited as the
  method source for the exposure definition but was not re-verified this
  round.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Fang, Liang & Qin (2026), The long-term impact of industrialization campaigns on human capital accumulation: Evidence from the "Construction of Third Front" in China'
  doi: https://doi.org/10.1016/j.jce.2026.01.001
  journal: JCE
  year: 2026
  dataset_role: Prefecture-level TF-built manufacturing-capacity measure constructed from the 1985 Industrial Census, matched to several micro-level sources with the 1990 Population Census as the main outcome source
  evidence_type: publisher data-section snippet
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0147596726000016
  data_note: >-
    The publisher's exposed Data and empirical strategy snippet (checked
    2026-09-28) says the authors follow Fan and Zou (2021), construct
    prefecture-level TF-built manufacturing capacity using the 1985 Industrial
    Census, and match it to several micro-level survey data, with the 1990
    Population Census as the main outcome source. The exact construction code,
    other survey identities, and analytical sample remain unavailable.

provenance:
- source: Crossref API 10.1016/j.jce.2026.01.001 (read 2026-08-15)
  field_scope:
  - author list (Guanghua Fang, Yinhe Liang, Fan Qin)
  - journal/volume/pages/date
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://news.ebiotrade.com/2026-2/20260202181539648.htm (read 2026-08-15)
  field_scope:
  - construction method (1985 industrial census + 1990 census)
  - exposure definition (Fan & Zou 2021 method)
  - results and robustness
  - author affiliation (Tsinghua SEM)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: Unpaywall 10.1016/j.jce.2026.01.001 (read 2026-08-15)
  field_scope:
  - access status (closed)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.sciencedirect.com/science/article/pii/S0147596726000016 (publisher search result data-section snippet, checked 2026-09-28)
  field_scope:
  - paper use of 1985 Industrial Census
  - prefecture-level TF-built manufacturing-capacity construct
  - use of several micro-level survey sources
  - 1990 Population Census as main outcome source
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Crossref API DOI 10.1016/j.jdeveco.2021.102698; OpenAlex work W3171604543; rendered ScholarSphere download route https://scholarsphere.psu.edu/resources/601f8cc3-d6ce-4610-9527-ec4a2e547663/downloads/53695 (checked 2026-09-28)
  field_scope:
  - Identity of the Fan and Zou (2021) method source: Journal of Development Economics 152, article 102698
  - Indexed submitted-version route at ScholarSphere
  - Boundary that the live browser visit reached repository bot detection, not the paper body or appendix
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-senddown-county-exposure
  relation: often-confused-with
- id: china-second-industrial-survey-1985
  relation: complement

production:
  raw_sources:
  - name: 1985 industrial census (第二次全国工业普查) input to TF-built manufacturing capacity
    source_type: dataset
    role: Exposure input to the paper's prefecture-level TF-built manufacturing-capacity construct; the detailed Fan-and-Zou implementation remains unavailable
    access_route: Official NBS publications; see china-second-industrial-survey-1985
    url: https://www.stats.gov.cn/
    coverage: China, 1985 (prefecture-level construction per publisher snippet; detailed coding unavailable)
    last_checked: '2026-09-28'
  - name: 1990 population census microdata
    source_type: dataset
    role: Outcome input - individual schooling and labor-market outcomes
    access_route: Restricted census microdata route (see china-census)
    url: https://www.stats.gov.cn/
    coverage: China, 1990 (main outcome source; paper's analytical sample unavailable)
    last_checked: '2026-09-28'
  acquisition_methods:
  - census-table extraction
  - restricted microdata application
  sample_construction: >-
    The publisher confirms the broad design: follow Fan and Zou (2021), use
    the 1985 Industrial Census for prefecture-level TF-built manufacturing
    capacity, and match that measure to several micro-level survey sources,
    chiefly the 1990 Population Census. The secondary translation describes a
    large/medium-enterprise employment-share implementation, but the exact
    geographic coding, inclusion rules, survey list, and exclusions remain
    unavailable.
  pipeline_stages:
  - stage: collect
    inputs:
    - 1985 industrial census tables
    - 1990 census microdata
    method: Assemble the separately authorized census and survey inputs; the complete input list remains unavailable
    tools: []
    output: Exposure and outcome inputs
    evidence: Publisher Data and empirical strategy snippet; Fan--Zou method source identified but its detailed text unavailable in the checked session
  - stage: aggregate
    inputs:
    - 1985 Industrial Census input
    method: Construct prefecture-level TF-built manufacturing capacity following Fan and Zou (2021); detailed formula unavailable
    tools: []
    output: Prefecture-level TF exposure measure
    evidence: Publisher Data and empirical strategy snippet; exact implementation unavailable
  - stage: match
    inputs:
    - TF exposure
    - 1990 census microdata
    method: Match local exposure to micro-level records; the precise geographic key and sample restrictions remain unavailable
    tools: []
    output: Individual-level analysis sample
    evidence: Publisher Data and empirical strategy snippet; exact matching unavailable
  output:
    unit_of_observation: Individual (1990 census) with local TF exposure
    structure: Individual-level extract
    geography: China (inland Third Front regions vs others)
    time_span: Campaign 1964-~1972; outcomes 1990
    key_variables:
    - TF exposure (prefecture-level capacity construct)
    - Schooling years
    - Labor-market and fertility outcomes
    formats:
    - Unreleased (paper analysis files)
  reproducibility:
    level: low
    starting_point: Separately authorized 1985 Industrial Census and 1990 Population Census inputs, plus the paper's other unidentified micro-level sources
    code_available: false
    requirements:
    - Authorized 1985 Industrial Census input
    - Authorized 1990 census microdata access
    - The full paper or author clarification for exact coding, sample, and other source identities
    blockers:
    - Exact exposure coding, sample, geographic key, and additional micro-level sources unavailable
    - Underlying census and survey access is separately restricted
  compliance:
    terms_or_license: Census microdata terms apply (restricted)
    robots_or_rate_limits: Use official NBS routes
    personal_or_sensitive_data: Census microdata contains personal information; restricted use
    redistribution: No redistribution without census terms
    review_needed: true
---

## Positioning in one sentence

The Third Front paper's exposure measure is a researcher-constructed prefecture-level capacity variable from the 1985 Industrial Census, matched to several micro-level sources with the 1990 Population Census as its main outcome source. The publisher confirms this broad design, but the inputs are separately restricted and the exact coding and sample remain unavailable.

## Select rules

- Choose this route for Third Front exposure designs; the campaign differs from the send-down movement (china-senddown-county-exposure).
- Read the full paper's data section before coding the exposure: the publisher confirms the broad data design, but not the code-level construction or sample rules.
- Do not treat treatment assignment/policy timing as data knowledge; that side belongs to Econ-Variation.

## Get recipe

1. Read the closed-access paper (or obtain author clarification) for the exact capacity construction, survey inputs, codes, and sample.
2. Obtain each required census or survey input through its own authorized route.
3. Build and document a distinct reconstruction only if the definition and sample can be evidenced; do not validate a guessed build against a headline result.

## Connections and Limitations

- The publisher confirms the broad input roles, but neither the available snippets nor the secondary republication establishes every input, code, or restriction needed to reproduce the analysis.
- The 1985 industrial-census and 1990 census routes are separately restricted; a title or a paper snippet does not create ordinary access.
