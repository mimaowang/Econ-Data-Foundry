---
schema_version: 3
catalog_status: grounding
id: baidu-qianxi-2020-spring-festival-city-od-network
name: Baidu Qianxi 2020 Spring Festival 339-city daily origin-destination migration network (paper-specific extraction)
aka:
- 2020年春节前百度迁徙339城市OD网络
- 百度迁徙2020年1月6日至26日城市间OD迁徙数据
- Baidu Migration 2020 city OD network
provider: >-
  Baidu Maps Huiyan (百度地图慧眼) as the provider platform; the specific
  2020 339-city daily OD extraction is documented in Zhang et al. (2021), not
  released by the article or verified as a current provider download.
china_related: true
domains:
- migration
- urban
- regional
- spatial
- labor mobility

data_pathway:
  mode: inaccessible
  origin: unknown
  target_artifact: >-
    The paper-specific daily directed origin-destination migration matrices
    among 339 Chinese prefecture-level-and-above cities, covering 2020-01-06
    through 2020-01-26. The paper describes daily inflow, outflow and migration
    intensity and constructs separate 339 x 339 directed inbound and outbound
    OD matrices; it does not release the matrix, collection procedure, or code.
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: >-
    Zhang et al. (2021) genuinely used this Baidu Migration extraction to study
    China's urban network. The full paper fixes the dates, city universe, daily
    OD structure, three data types and their network transformation. It does
    not establish that the same 2020 historical OD data can be downloaded or
    reconstructed today. The currently browser-visible Baidu Qianxi product is
    a different, much narrower selected-day top-20 city ranking.
  barrier: >-
    No paper repository, matrix file, code, documented historical export, or
    current provider route for the 2020 339-city OD panel was found. The public
    page's selected-day top-20 ranking cannot reproduce the city universe,
    bilateral links or historical 2020 window.
  last_checked: '2026-09-28'

unit_of_observation: One directed origin-city x destination-city x day migration-intensity cell in the paper's 339-city 2020 Spring Festival extraction.
structure: Daily directed origin-destination network matrices; paper-described as separate inbound and outbound 339 x 339 matrices.
geo_granularity:
- prefecture-level city and above
- directed city pair
geography: 339 Chinese prefecture-level-and-above cities, excluding Hong Kong, Macao and Taiwan.
time_span:
  start: '2020-01-06'
  end: '2020-01-26'
  last_confirmed_release: null
  coverage_note: The 21-day window is the three weeks before the 2020 Spring Festival, as documented in the paper; it is not evidence of a publicly retrievable historical archive.
  last_checked: '2026-09-28'
frequency:
- daily
sample_size: 339 cities; the paper reports 23,847 OD city-pair links after its mean-intensity thresholding step.
key_variables:
- Daily inbound, outbound and migration-intensity measures between cities
- Directed inbound and outbound OD matrices
- Paper-derived mean migration intensity and net migration intensity

research_fit:
  best_for:
  - Understanding the exact empirical mobility input behind Zhang et al.'s China-wide urban-network analysis
  - Designing a related 2020-Spring-Festival city-network study only if the same historical OD delivery can be independently obtained
  choose_over:
  - Choose the current baidu-qianxi-migration record when a current browser-visible selected-day top-20 ranking is sufficient.
  - Do not choose this record when the task needs a reproducible current OD panel; no such route is verified here.
  not_good_for:
  - Direct download, replication or extension without a separately verified historical Baidu delivery
  - Complete current-city migration coverage, absolute migration counts, individual traces, or a policy-treatment database
  needs_join_for:
  - City outcomes and boundary concordances, if an independently obtained OD file exposes compatible city names or codes
  variation_available:
  - Paper-observed daily and bilateral-city variation within 2020-01-06 through 2020-01-26; current accessibility is unresolved
  topics:
  - urban networks
  - intercity migration
  - Spring Festival mobility
  - regional development

good_for:
- Paper-data lineage and feasibility assessment for a 2020 China urban-migration network study
identification:
- The record documents a mobility outcome/input; it supplies no treatment assignment or causal design.
linkable_keys:
- Origin city and destination city, if an independently obtained delivery exposes them
- Calendar day

joins:
- target: baidu-qianxi-migration
  relation: often-confused-with
  keys:
  - city
  - date
  method: The current public page offers only top-20 rankings; it cannot be substituted for this paper's 339-city bilateral network without changing the data object.
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - city name or code
  - year
  method: Add city economic controls only after verifying the historical city concordance in the acquired mobility file.
  evidence_status: plausible

access_routes:
- route: Open full paper as construction documentation
  access_status: documentation-only
  direct_url: https://www.dqxxkx.cn/CN/abstract/article/1560-8999/50521
  requirements: None for the article.
  steps:
  - Read section 2.1 to preserve the exact 2020 window, city universe and matrix description.
  - Treat the paper as evidence of use and construction only; it does not deliver its data or code.
  deliverable: Public documentation of the paper-specific OD extraction, not a matrix file.
  cost: free
  last_checked: '2026-09-28'
  caveat: The article cannot establish a current historical-data route.
- route: Baidu Maps Huiyan data request
  access_status: needs-verification
  direct_url: https://huiyan.baidu.com/contact
  requirements: A provider response confirming whether a 2020 historical city-OD product exists, its coverage, cost, licence and delivery terms.
  steps:
  - Ask specifically for the 2020-01-06 through 2020-01-26, prefecture-city OD product rather than a generic current ranking.
  - Record any provider response, product definition, city universe, fields, cost and redistribution conditions before treating it as obtainable.
  deliverable: Unverified; no general application or historical product is documented in the checked sources.
  cost: by-application
  last_checked: '2026-09-28'
  caveat: The public ranking page's “获取详情数据请点击联系我们” notice does not itself establish that this historical matrix is sold or delivered.

access:
  url: https://www.dqxxkx.cn/CN/abstract/article/1560-8999/50521
  cost: by-application
  license: Article access and a possible provider data licence are separate; no matrix redistribution permission is established.
  format:
  - unknown (paper reports matrices but no file is released)
  api: false
  how_to_get: Use the paper to formulate a precise provider or author request; do not substitute the current top-20 display for the 2020 OD matrices.
caveats:
- The paper's 339-city matrices prove actual research use, not public current availability.
- The paper's reported 23,847 links follow a paper-side mean-intensity threshold; that filtered network is not automatically the provider's raw delivery.
- “Migration intensity” is the paper's reported construct, not an absolute count or a documented population-representative flow measure.
- Current selected-day rankings and the historical bilateral matrix have different units and must not be merged or treated as interchangeable.

quality:
  profile_status: verified
  access_status: unavailable
  paper_use_status: verified
  last_audited: '2026-09-28'
used_by:
- cite: Zhang, Han, Tang & Luo (2021), Research on the Characteristics of Urban Network Structure in China based on Baidu Migration Data
  doi: https://doi.org/10.12082/dqxxkx.2021.210223
  journal: Journal of Geo-information Science
  year: 2021
  dataset_role: Main daily bilateral city-migration input for network centrality and net-migration analysis
  evidence_type: paper_data_section
  evidence_url: https://www.dqxxkx.cn/CN/abstract/article/1560-8999/50521
  data_note: >-
    Section 2.1 states that the study selected continuous directed OD migration
    data among 339 prefecture-level-and-above cities for 2020-01-06..26,
    distinguishes daily inflow, outflow and migration intensity, and formed
    directed 339 x 339 inbound/outbound matrices. It reports 23,847 city-pair
    links after the paper's mean-intensity threshold.
provenance:
- source: https://www.dqxxkx.cn/CN/abstract/article/1560-8999/50521
  field_scope:
  - paper identity, DOI and urban/regional research scope
  - actual Baidu Migration use and the 2020-01-06..26 window
  - 339-city universe excluding Hong Kong, Macao and Taiwan
  - daily inflow/outflow/migration-intensity variables, directed OD matrices and paper thresholding
  - absence of a released matrix, code or provider delivery route on the read article page
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://qianxi.baidu.com/ (browser-read 2026-09-28)
  field_scope:
  - current public page supplies selected-day city top-20 rankings and asks users to contact the provider for details
  - this is not evidence that the paper's historical 339-city OD matrices are currently retrievable
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: baidu-qianxi-migration
  relation: often-confused-with
- id: china-amap-migration-flow-indices
  relation: substitute
---

## Positioning in one sentence

This is the real 2020 Baidu-based 339-city daily OD network used in a China urban-network paper, but it is documented rather than delivered: the current public Baidu page cannot reproduce its bilateral historical matrix.

## Select rules

- Use this record to judge whether a proposed urban-network project truly needs the paper's bilateral 2020 OD object.
- Use the separate current Baidu ranking record only for its narrow, manually transcribable top-20 display.
- Do not call a current browser ranking a replication of this 339-city network.

## Get recipe

1. Read the paper's data section to retain the exact dates, city universe and matrix target.
2. Ask Baidu Huiyan or the authors for that specific historical OD delivery and its terms.
3. Inspect any delivered file's city universe, direction convention, dates, index definition and paper-side thresholding before analysis.

## Connections and Limitations

The decisive join is origin city × destination city × day. City names must be reconciled to any outcome source, and the paper's thresholding must not be silently treated as the provider's raw network. No policy or causal-design interpretation belongs here.

## Decision sufficiency check

A later agent can identify the paper-used 2020 network, distinguish it from the current public ranking, formulate the right data request and stop before claiming an unverified historical download exists.
