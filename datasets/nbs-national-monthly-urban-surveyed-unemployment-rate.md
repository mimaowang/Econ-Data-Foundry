---
schema_version: 3
catalog_status: ready
id: nbs-national-monthly-urban-surveyed-unemployment-rate
name: NBS national monthly urban surveyed unemployment rate (全国城镇调查失业率)
aka:
- 全国城镇调查失业率
- 城镇调查失业率
- National urban surveyed unemployment rate
provider: National Bureau of Statistics of China (NBS, 国家统计局).
china_related: true
domains:
- labor
- urban
- macro
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Monthly national aggregate urban surveyed unemployment-rate observations published in NBS national-economy releases.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    NBS has published the national urban surveyed unemployment rate monthly
    since 2018. The current monthly national-economy release route remains
    public: the 2026 August release reports a national rate of 5.3%, its
    year-to-date average of 5.2%, and a separate 31-large-city rate. A
    researcher can construct a documented national monthly series by
    transcribing the release table or text with release dates and URLs.
  barrier: >-
    The release is an aggregate indicator embedded in monthly pages, not a
    downloadable household file or a documented province-month panel.

unit_of_observation: National urban surveyed unemployment rate for one calendar month, reported as a percentage.
structure: Monthly national aggregate time series assembled from official release pages.
geo_granularity:
- national
geography: China national urban aggregate; the separately reported 31-large-city aggregate is not a province/city panel.
time_span:
  start: '2018-01'
  end: ongoing
  last_confirmed_release: 2026-08, released 2026-09-15
  coverage_note: NBS documentation states monthly national publication since 2018. The current route confirms 2026-08; archive completeness and exact release-page patterns should be recorded when constructing a full historical series.
  last_checked: '2026-09-28'
frequency:
- monthly
sample_size: One national aggregate per month; some releases also report a separate 31-large-city aggregate and selected subgroup rates.
key_variables:
- National urban surveyed unemployment rate (%)
- Year-to-date average national urban surveyed unemployment rate (%) where reported
- 31-large-city urban surveyed unemployment rate (%) where reported, as a separate aggregate

research_fit:
  best_for:
  - National monthly labor-market monitoring and macro controls in China
  - Time-series descriptions of the official survey-based urban unemployment measure
  choose_over:
  - Choose this over registered-unemployment measures when the needed indicator is NBS's survey-based, ILO-comparable urban unemployment rate.
  - Use the separate nbs-monthly-labor-force-survey record only when assessing the survey's restricted household microdata route.
  not_good_for:
  - Household, individual, city or province-month unemployment analysis
  - A causal-design or local labor-market outcome without another source
  needs_join_for:
  - National monthly macro indicators when modelling aggregate labor conditions
  - A separately verified subnational labor source for local empirical work
  variation_available:
  - Monthly national time variation since 2018
  topics:
  - unemployment
  - labor market
  - urban employment
  - macroeconomic indicators

good_for:
- A documented public national monthly unemployment series
identification:
- Aggregate monthly time-series variation only; it does not encode treatment assignment or individual labor outcomes.
linkable_keys:
- Calendar month
- Release date

joins:
- target: nbs-monthly-labor-force-survey
  relation: component
  keys:
  - month
  method: This is the public aggregate output of the survey family; it does not establish access to the survey microdata.
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - year
  method: Combine national annual or macro context cautiously; frequency conversion must be explicit.
  evidence_status: plausible

access_routes:
- route: NBS monthly national-economy releases
  access_status: available
  direct_url: https://www.stats.gov.cn/sj/zxfb/
  requirements: None.
  steps:
  - Open the NBS 数据发布 column and select the relevant monthly national-economy release.
  - Find the 全国城镇调查失业率 table row or employment section.
  - Transcribe the monthly rate with the observation month, release date, URL and any stated revisions or notes.
  - Keep the national rate separate from the 31-large-city aggregate and subgroup rates.
  deliverable: Official release-page observations for a researcher-built national monthly series.
  cost: free
  last_checked: '2026-09-28'
  caveat: The pages provide aggregate observations, not a bulk API, a household file or a verified province-month series.

access:
  url: https://www.stats.gov.cn/sj/zxfb/
  cost: free
  license: Government statistical releases; use subject to NBS publication rules.
  format:
  - HTML release pages and tables
  api: false
  how_to_get: Retrieve each relevant NBS monthly release and preserve source metadata while transcribing the national rate.
caveats:
- The indicator is national urban aggregate data, not microdata and not a city/province panel.
- Releases may contain year-to-date averages, 31-large-city or subgroup measures; do not substitute these for the monthly national rate.
- The household-survey microdata route remains unverified and is outside this record.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'
used_by: []
provenance:
- source: https://www.stats.gov.cn/zs/tjws/tjzb/202301/t20230101_1903672.html
  field_scope:
  - national monthly series published since 2018
  - survey-based ILO-comparable indicator definition
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/sj/zxfb/202609/t20260915_1965307.html
  field_scope:
  - current release route and 2026-08 national monthly rate, year-to-date average and separate 31-large-city aggregate
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: nbs-monthly-labor-force-survey
  relation: component
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is the directly obtainable national monthly output of the NBS labor-force survey, suitable for aggregate labor-market time series but not for local or household empirical analysis.

## Select rules

- Choose it for a national monthly survey-based unemployment control or descriptive series.
- Do not use it for city, province or household outcomes.
- Keep the national monthly rate distinct from the 31-large-city aggregate reported beside it.

## Get recipe

1. Find the relevant NBS monthly national-economy release.
2. Record the national monthly rate, observation month, release date and URL.
3. Preserve any table notes and never fill missing months with a year-to-date average.

## Connections and Limitations

The series is a public aggregate output. The survey's large household sample explains its measurement basis but does not make respondent-level data available. Local empirical work needs a different outcome source.

## Decision sufficiency check

A future agent can identify the correct public rate, acquire it from a current official release, construct a traceable monthly series and know that the product fails as soon as the question needs a local or individual observation.
