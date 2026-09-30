---
schema_version: 3
catalog_status: ready
id: nbs-third-national-time-use-survey-2024-public-bulletins
name: Third National Time Use Survey (2024) public national bulletin tabulations
aka:
- 第三次全国时间利用调查公报
- 全国居民主要活动领域和主要活动大类时间利用情况
- 2024 China Time Use Survey public bulletins
provider: National Bureau of Statistics of China (NBS, 国家统计局).
china_related: true
domains:
- time use
- labor
- household
- welfare
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The public national aggregate time-use statistics in NBS's 2024 third
    National Time Use Survey bulletin pages: daily mean time, participant mean
    time and participation rates for the published activity domains and major
    activity classes.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The official second bulletin is a public HTML table and text release. It
    gives nationally aggregated, seven-day daily time-use measures for six
    activity domains, 13 major activity classes and internet use. A researcher
    can transcribe the published tables into a small, documented aggregate
    dataset while retaining the bulletin URL and release date.
  barrier: >-
    This is a 2024 national aggregate release, not person-level diaries,
    province/city estimates, a machine-readable bulk file, or a comparable
    multi-round panel.

unit_of_observation: >-
  One published national aggregate statistic for an activity domain or major
  activity class in the 2024 survey, reported as daily mean time, participant
  daily mean time, or participation rate.
structure: Cross-sectional national aggregate tabulations from the 2024 survey round.
geo_granularity:
- national
geography: China national aggregate; the survey fieldwork covered 31 provinces (autonomous regions and municipalities) plus the Xinjiang Production and Construction Corps, but this bulletin does not supply a subnational series.
time_span:
  start: '2024-05-11'
  end: '2024-05-31'
  last_confirmed_release: '2024-10-31'
  coverage_note: >-
    The bulletin reports results as daily measures calculated for a seven-day
    week. It is a single 2024 public release, not a historical panel.
  last_checked: '2026-09-28'
frequency:
- one 2024 cross-sectional release
sample_size: Not stated in the read bulletin.
key_variables:
- Resident daily mean time by published activity domain and major activity class
- Participant daily mean time by the same published classes
- Activity participation rate (%)
- Internet-use daily mean time, participant mean time and participation rate

research_fit:
  best_for:
  - A documented national 2024 descriptive benchmark for paid work, unpaid work, travel, care, leisure, study and internet use
  - National aggregate controls or descriptive context when an empirical design does not require local or individual variation
  choose_over:
  - Choose this rather than the broader nbs-time-use-survey record when the needed object is the directly obtainable 2024 public table rather than diary microdata or cross-round survey analysis.
  not_good_for:
  - Individual-, household-, province- or city-level empirical analysis
  - Estimating variation across places or population cells not explicitly published in this bulletin
  - A multi-year panel or causal design without another source of variation
  needs_join_for:
  - Any local, individual or longitudinal outcome must come from a separately obtainable source with compatible geography and timing.
  variation_available:
  - Published national activity-category variation within the single 2024 release only
  topics:
  - time allocation
  - paid work
  - unpaid work
  - care
  - travel
  - internet use

good_for:
- Public national time-use descriptive statistics
identification:
- Descriptive aggregate measures only; the bulletin supplies no treatment assignment or local comparison group.
linkable_keys:
- Survey round (2024)

joins:
- target: nbs-time-use-survey
  relation: component
  keys:
  - survey round
  method: This ready record is the publicly obtainable aggregate output of the broader survey family; it does not establish access to the survey diaries.
  evidence_status: verified

access_routes:
- route: NBS Third National Time Use Survey Bulletin No. 2
  access_status: available
  direct_url: https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957216.html
  requirements: None.
  steps:
  - Open the official NBS bulletin page.
  - Transcribe each required row from the two attached public tables, retaining the measure type, activity label, release date and URL.
  - Keep reported hours/minutes distinct from participation rates, and document any conversion to minutes.
  deliverable: A researcher-built machine-readable transcription of official national 2024 aggregate tabulations.
  cost: free
  last_checked: '2026-09-28'
  caveat: The page is an HTML publication, not an API or downloadable respondent-level file.

access:
  url: https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957216.html
  cost: free
  license: Government statistical release; use subject to NBS publication rules.
  format:
  - HTML text and tables
  api: false
  how_to_get: Retrieve the official bulletin and transcribe the published national aggregate tables with source metadata.
caveats:
- The bulletin's national totals cannot be converted into province, city, household or person observations.
- Fieldwork used two diary days per respondent, with weekday/weekend weighting; activities under seven minutes were not recorded and activities over seven but under 15 minutes were recorded as 15 minutes.
- The 2024 round expanded coverage, age range and recording mode relative to earlier rounds; do not infer comparability with 2008 or 2018 without round-specific documentation.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'
used_by: []
provenance:
- source: https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957216.html
  field_scope:
  - release date and public HTML access
  - national daily mean, participant mean and participation-rate tables
  - 2024 field dates and two-day diary weighting
  - 31 provinces plus Xinjiang Production and Construction Corps survey coverage
  - 34 activity categories and app-based self-reporting
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: nbs-time-use-survey
  relation: component
---

## Positioning in one sentence

This is the directly obtainable national aggregate output of the 2024 NBS time-use survey: useful for a transparent descriptive benchmark, but deliberately too coarse for local, household or person-level empirical analysis.

## Select rules

- Choose it when the question genuinely needs a published national 2024 time-use statistic.
- Use another data source when the outcome must vary across people, households, cities or years.
- Do not treat the public page as access to the survey's diary microdata.

## Get recipe

1. Open the official Bulletin No. 2 page.
2. Copy the required table cells into a tidy file, preserving activity labels and measure type.
3. Keep the source URL, release date and any time-unit conversion beside the resulting observation.

## Connections and Limitations

The underlying survey is broader than this public product. The public bulletin gives national aggregates only; its coverage of 31 provincial-level areas describes the survey frame, not a published regional panel. A project needing regional/urban or development-economics variation must pair this benchmark with a separate local data asset.

## Decision sufficiency check

A later agent can retrieve the exact official release, know what each published row represents, create a traceable national aggregate file, and stop before falsely claiming diary or local access.
