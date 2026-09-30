---
schema_version: 3
catalog_status: grounding
id: china-city-official-vacancy-panel
name: Hand-collected municipal party-secretary vacancy panel, China 2003-2019
aka:
- Leadership vacuum data
- 市委书记空缺数据
- unfilled municipal party secretary positions
provider: >-
  Paper authors (Maoyong Cheng, Yutong Yao, Justin Y. Jin, Khalid Nainar, Yu
  Meng) - hand-collected data, no public distribution identified as of
  2026-08-15. Cheng is at Xi'an Jiaotong University School of Economics and
  Finance (per scholar.xjtu.edu.cn); Jin and Nainar at McMaster University
  (per experts.mcmaster.ca record read 2026-08-15).
china_related: true
domains:
- urban
- political-economy
- public-economics
- regional

data_pathway:
  mode: inaccessible
  origin: researcher-collected
  target_artifact: >-
    Paper-specific hand-collected city-fiscal-year panel of municipal
    party-secretary vacancy duration. The authors manually obtained vacancy
    information through hotelaah.com and Baidu, then matched it to city data
    by province, city and fiscal year for 2003-2019. No replication package
    or public panel file is identified.
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: >-
    Grounding pass (2026-09-28): the public published text documents a
    2003-2019 hand-collected vacancy input and its matching to city data.
    Vacancy information was manually obtained from hotelaah.com and Baidu;
    separate city-level variables came from the China Statistical Yearbook,
    China Urban Statistical Yearbook and CSMAR. The main matched sample is
    1,224 city-fiscal-year observations, restricted to city-years with
    political turnover and available model inputs. That is not the universe
    of Chinese city-years and does not make the author panel downloadable.
  barrier: >-
    No public data file or code. The paper names a historical manual-search
    route, but does not release the search queries, event-level source
    captures, reconciliation decisions, underlying coverage universe or the
    final panel; the current or historical bulk availability of those sources
    is not established.

unit_of_observation: City-fiscal-year observation with a manually determined municipal party-secretary vacancy duration (month-level source timing)
structure: matched city-fiscal-year panel; the reported main analysis sample is restricted rather than a complete city universe
geo_granularity:
- city (municipality)
geography: Chinese cities (municipalities with party secretaries), 2003-2019
time_span:
  start: '2003'
  end: '2019'
  last_confirmed_release: 'No public release identified (2026-09-28)'
  coverage_note: >-
    The public paper text gives 2003-2019, 4,917 initial city-year
    observations and 1,224 final main-sample city-years after missing-input
    and no-turnover exclusions. It does not release the city roster or a
    machine-readable vacancy-event file.
  last_checked: '2026-09-28'
frequency:
- city-fiscal-year
sample_size: >-
  1,224 city-fiscal-year observations in the paper's final main sample;
  4,917 initial 2003-2019 observations before reported exclusions. Neither
  is a public data delivery.
key_variables:
- SV: duration in months for which a municipal party-secretary post was vacant
- Vacancy assignment year: departure before June 30 is recorded in that year; after June 30 in the following year
- Province, city and fiscal year used to match the hand-collected vacancy data to separate city statistics

research_fit:
  best_for:
  - Studying effects of temporary executive vacancy at the Chinese city level (government efficiency, policy uncertainty channels)
  - Political-uncertainty measures for city-year panel designs (family: Cheng, Duan & Li 2026 JIFMIM 106:102247 uses a related "temporary absences of SMPCs and Mayors" measure)
  choose_over:
  - Choose this family over china-city-leader-rotation-microdata-2026 (candidate, JEG) when the research question is vacancy/absence rather than rotation/tenure.
  - Treat the documented website-and-search-engine route as a starting point for historical research, not as evidence of a supported bulk archive or a reproducible copy of this panel.
  not_good_for:
  - Assuming a public download exists (none found).
  - Treating access to city statistical controls as access to the authors' vacancy panel.
  needs_join_for:
  - City outcomes and covariates (china-stat-yearbook family)
  - Leader identity/rotation detail (candidate china-city-leader-rotation-microdata-2026)
  variation_available:
  - City-period vacancy variation 2003-2019 (data dimension; the paper's causal claims are its own)
  topics:
  - leadership vacancy
  - political uncertainty
  - city government

good_for:
- political-uncertainty outcome designs
- vacancy/leadership-gap analysis
identification: []
linkable_keys:
- Province
- City (municipality) name/code
- Fiscal year

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - city
  - year
  method: city-year outcome matching
  evidence_status: verified

access_routes:
- route: open-access-full-text
  access_status: available
  direct_url: https://www.sciencedirect.com/science/article/pii/S0147596723000707
  requirements: Human browser (ScienceDirect 403 for automated clients); no subscription needed (hybrid OA, CC BY-NC-ND, CRKN sponsor)
  steps:
  - Open the article page (PII S0147596723000707) in a human browser.
  - Read the data section and appendix for the vacancy definition, sources, and city coverage.
  - Decide whether rebuilding the panel from the stated sources is feasible.
  deliverable: Full text incl. data construction details; no data file.
  cost: free
  last_checked: '2026-08-15'
  caveat: Delivers construction documentation, not the vacancy panel or code.
- route: public-published-text
  access_status: available
  direct_url: https://www.researchgate.net/publication/373472307_Leadership_vacuum_and_urban_economic_development_Evidence_from_a_transition_country
  requirements: Public web access; treat the hosted article text as documentation rather than a data source.
  steps:
  - Read Section 4.1 for the named vacancy-search and city-data inputs.
  - Read Section 4.3 for the monthly-duration definition and fiscal-year assignment convention.
  - Request the authors' materials if the exact panel or source captures are needed.
  deliverable: Public article text documenting construction and matching; no data file.
  cost: free
  last_checked: '2026-09-28'
  caveat: The page does not establish that hotelaah.com or Baidu provide a complete historical export, nor does it supply the authors' search results.
- route: author-contact
  access_status: needs-verification
  direct_url: https://experts.mcmaster.ca/scholarly-works/3288257
  requirements: Email request (corresponding author per journal page)
  steps:
  - Contact the authors for the vacancy panel or construction files.
  - Confirm terms before any use.
  deliverable: Unverified; no public commitment.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: No public evidence that the authors share the data.

access:
  url: https://doi.org/10.1016/j.jce.2023.08.004
  cost: free
  license: >-
    Paper: CC BY-NC-ND 4.0 (hybrid OA). Data: no public file/license
    identified.
  format:
  - paper full text (HTML/PDF via publisher)
  api: false
  how_to_get: >-
    Read the public paper text for construction documentation; obtain the
    separate city-statistics inputs from their providers where appropriate.
    The exact hand-collected vacancy panel requires an author request or a
    newly documented reconstruction.
caveats: >-
  The data is hand-collected and unpublished. The public article documents
  the broad manual sources and a month-accurate timing convention, but not
  the search queries, captured pages, event reconciliation, city roster,
  source retention or code. Its main 1,224-observation sample is a selected
  analysis sample, not a public master panel. A search result or a city
  statistical series must never be represented as the original vacancy data.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Cheng, Yao, Jin, Nainar & Meng (2024), Leadership vacuum and urban economic development: Evidence from a transition country'
  doi: https://doi.org/10.1016/j.jce.2023.08.004
  journal: JCE
  year: 2024
  dataset_role: Manually collected municipal party-secretary vacancy panel 2003-2019 (main explanatory variable)
  evidence_type: published-paper-full-text
  evidence_url: https://www.researchgate.net/publication/373472307_Leadership_vacuum_and_urban_economic_development_Evidence_from_a_transition_country
  data_note: >-
    Public article text, Section 4.1-4.3, read 2026-09-28: authors manually
    obtained vacancy data through hotelaah.com and Baidu; city variables came
    separately from the China Statistical Yearbook, China Urban Statistical
    Yearbook and CSMAR. They matched by province, city and fiscal year; the
    final restricted main sample has 1,224 city-year observations. SV is
    vacancy duration; source timing is accurate only to month. No panel or
    code is supplied.

provenance:
- source: https://experts.mcmaster.ca/scholarly-works/3288257 (read 2026-08-15)
  field_scope:
  - paper identity
  - abstract (data definition, period, channels)
  - author affiliations
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Crossref API 10.1016/j.jce.2023.08.004 (read 2026-08-15)
  field_scope:
  - author list
  - journal/volume/pages
  - publication date
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Elsevier core-data API (PII S0147596723000707, read 2026-08-15)
  field_scope:
  - open access status (hybrid, CC BY-NC-ND, CRKN sponsor)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://scholar.xjtu.edu.cn (Cheng profile, read 2026-08-15)
  field_scope:
  - author affiliation
  - related vacancy-data research program
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.researchgate.net/publication/373472307_Leadership_vacuum_and_urban_economic_development_Evidence_from_a_transition_country (public article text, read 2026-09-28)
  field_scope:
  - actual vacancy-data collection sources
  - city-statistics inputs distinct from vacancy data
  - 2003-2019 coverage, matching keys and main-sample count
  - vacancy-duration definition and timing precision
  - paper use
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets: []
---

## Positioning in one sentence

This is an unpublished, hand-collected city-fiscal-year vacancy panel for 2003-2019: the paper documents manual collection from hotelaah.com and Baidu and matching to separate city statistics, but it does not release the panel, source captures or code.

## Select rules

- Choose this asset family when the design needs vacancy/absence timing of city party secretaries, not rotation or tenure.
- Use the public paper text to understand the limited reconstruction recipe, then decide whether a fresh, fully documented historical collection is feasible.
- Do not treat the JEG rotation candidate or the XJTU equity-market paper as the same product until their constructions are compared.

## Get recipe

1. Read Section 4 of the public article text for the named manual sources, province-city-fiscal-year matching and monthly timing convention.
2. Obtain city outcomes/controls separately from the stated statistical sources if needed; these are not substitutes for the vacancy data.
3. For the exact vacancy panel, request materials from the authors; otherwise treat any new reconstruction as a distinct dataset with its own documented collection trail.

## Connections and Limitations

- No public file or replication package is identified; the public text is a useful construction boundary, not a reproducible event-level recipe.
- The paper is CC BY-NC-ND: reuse of text needs attribution and non-commercial compliance.
- Cheng, Duan & Li (2026, JIFMIM) use a related absence measure (SMPCs and Mayors) - evidence of an ongoing data program, not of a public release.
