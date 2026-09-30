---
schema_version: 3
catalog_status: grounding
id: nbs-time-use-survey
name: NBS Time Use Survey (全国时间利用调查) - diary microdata with a documented 2018 laboratory route
aka:
- 全国时间利用调查
- 时间利用调查
- NBS National Time Use Survey (NTUS)
- 全国时间利用调查公报
provider: >-
  国家统计局 (National Bureau of Statistics of China, NBS). Third survey
  (2024) bulletin published on stats.gov.cn (第三次全国时间利用调查公报,
  read 2026-08-15); first survey 2008 with an official 2008年时间利用调查
  资料汇编 special section (verified 2026-08-15); second survey 2018
  (公报 published 2019-01-27 per news reports - secondary evidence).
china_related: true
domains:
- time use
- labor
- welfare
- household
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Household/individual diary microdata from the national time-use survey
    rounds. The 2018 round has a documented institution-based application
    route for controlled laboratory use, not a public microdata download.
    Access for 2008 and 2024 is not established here. The separately
    catalogued 2024 public bulletin tables are a different aggregate product.
  availability: restricted
  ordinary_researcher_feasible: true
  summary: >-
    A national time-use survey run three times (2008, 2018, 2024). The 2024
    third survey (bulletin read 2026-08-15): field work 2024-05-11..31; two
    diary days per respondent (one weekday + one weekend day, 24h diary with
    15-minute recording threshold); coverage extended to 31 provinces +
    Xinjiang Production and Construction Corps; ages 6+ included for the
    first time; 34 activity categories; app-based self-reporting. Public
    output is tabulations; the directly obtainable 2024 public tables now
    have their own ready record. NBS explicitly confirmed in February 2024
    that the 2018 microdata can be applied for through its laboratory. This
    route is feasible only for researchers in eligible, registered institutions
    whose projects are approved; onsite use and reviewed outputs are required.
    The October 2024 announcement describes planned opening of the third-round
    microdata, not proof that this later round is currently in the catalogue.
  barrier: >-
    The application portal remains JS-driven. The documented 2018 route does
    not establish a user's approval, current appointment availability, exact
    sanitized fields, geographic identifiers, fees or access to other rounds.
    The 2024 design also breaks comparability with earlier rounds.
  last_checked: '2026-09-28'

unit_of_observation: Individual respondent's daily time diary; two diary days per respondent. Age eligibility differs by round (2018 ages 15+; 2024 ages 6+).
structure: 'repeated-cross-section (three rounds: 2008, 2018, 2024)'
geo_granularity:
- individual / household within approved diary extracts
- province and urban/rural sampling frame (released geographic fields unverified)
geography: >-
  2024 round: 31 provinces (autonomous regions/municipalities) + Xinjiang
  Production and Construction Corps. The 2018 design names Beijing, Hebei,
  Heilongjiang, Shanghai, Zhejiang, Anhui, Henan, Guangdong, Sichuan, Yunnan
  and Gansu. Its published bulletin explicitly excludes Shanghai; do not
  assume a laboratory extract's province coverage from that bulletin alone.
time_span:
  start: '2008'
  end: '2024'
  last_confirmed_release: '2024-10-31 (third-survey bulletins)'
  coverage_note: >-
    First survey 2008 (资料汇编 special section verified on stats.gov.cn);
    second survey 2018 (official bulletin published 2019-01-25); third survey
    2024 (公报 read 2026-08-15). Field period of the third survey:
    2024-05-11 to 2024-05-31.
  last_checked: '2026-09-28'
frequency:
- irregular (three national rounds in 16 years)
sample_size: >-
  The official 2018 bulletin reports 20,226 households and 48,580 people;
  it separately cautions that its published results exclude Shanghai.
  NBS's 2024 Q&A reports 38,500 households and about 107,000 respondents
  for the third survey. These are reported survey counts, not a verified
  inventory of rows supplied to an approved laboratory project.
key_variables:
- Minutes/day spent on activities by 34 activity categories (2024 round),
  aggregated by population groups
- Two diary days per person (weekday + weekend day), 24h diary with
  15-minute recording threshold (activities <7 min not recorded; 7-15 min
  rounded up to 15)
- Coverage: all ages 6+ (first time in 2024); urban/rural; sex/age breakdowns
- 2018 diaries record activity in 15-minute slots, internet use during the activity and who the respondent is with; the sanitized laboratory field inventory is not yet read.

research_fit:
  best_for:
  - Approved 2018 projects on time allocation, unpaid care, labor, leisure or travel where controlled onsite analysis is practical
  choose_over:
  - Choose nbs-third-national-time-use-survey-2024-public-bulletins for public 2024 aggregates; use the conditional 2018 laboratory route when individual diaries are necessary.
  not_good_for:
  - Unrestricted offsite diary analysis or redistribution; laboratory access is not a raw-file download.
  - Treating 2008, 2018 and 2024 as a household panel or assuming all three rounds are offered together.
  - High-frequency time series (only three rounds)
  - Fine geography (subnational tabulations not verified in the bulletins)
  needs_join_for:
  - Local exposure or policy matching requires approved geographic fields and permission to introduce external inputs; both remain unverified.
  variation_available:
  - Cross-round (2008/2018/2024) comparisons with the caveat of method
    changes in 2024
  topics:
  - time use
  - time allocation
  - unpaid work
  - leisure
  - national statistics

good_for:
- national time-allocation benchmarking
- unpaid work measurement
identification: []
linkable_keys:
- Round/year; respondent and household identifiers only if exposed in the approved extract (codebook unread)

joins: []

access_routes:
- route: Public NBS time-use bulletins (documentation only)
  access_status: documentation-only
  direct_url: https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957216.html
  requirements: none
  steps:
  - Use the separately catalogued nbs-third-national-time-use-survey-2024-public-bulletins record if national 2024 public tabulations are enough.
  deliverable: Documentation and a separate national aggregate product; not diary microdata.
  cost: free
  last_checked: '2026-09-28'
  caveat: The public tables do not close this record's person-level microdata route.
- route: NBS laboratory application for the 2018 round
  access_status: available-with-conditions
  direct_url: https://microdata.stats.gov.cn/
  requirements: >-
    Eligible institution registration and project approval, followed by an
    onsite appointment. NBS's December 2024 explanation lists central-government
    research bodies, Double First-Class and Ministry-of-Education universities,
    specified national academies and other institutions approved by NBS.
    Eligibility alone does not grant access.
  steps:
  - Ask the institution's research/data office whether it is registered for NBS microdata use; if not, start institution registration before a personal project application.
  - Use the official portal to apply specifically for the 2018 time-use database; confirm the current codebook, geography, appointment location and any charges before committing to a design.
  - After approval, use the data onsite. Submit intermediate outputs for removal review, then final-output review and registration under the laboratory process.
  deliverable: Controlled analysis of the approved, sanitized 2018 diary extract and reviewed research outputs; no general raw-file export is established.
  cost: by-application
  last_checked: '2026-09-28'
  caveat: >-
    NBS's 2024 reply and dataset list explicitly confirm 2018. Its 2024
    third-survey Q&A announces opening plans for that later round only.
    Current portal forms, processing time, fees, exact fields and geography
    remain unread; verify them with the laboratory (official contact in the
    third-survey Q&A: wgsjsys@stats.gov.cn). No application was submitted here.

access:
  url: https://microdata.stats.gov.cn/
  cost: unknown
  license: Approved laboratory use and reviewed outputs; no public microdata redistribution license established.
  format:
  - controlled laboratory microdata (exact format unverified)
  api: false
  how_to_get: For 2018, establish institution eligibility/registration, apply for the named diary database and arrange approved onsite use. For public 2024 tables, use the separate bulletin record instead.
caveats:
- The 2024 round changed scope (31 provinces + XPCC), age range (6+ first time) and recording mode (app self-report) versus earlier rounds; cross-round comparability should be checked against each round's design.
- The 2018 bulletin excludes Shanghai although the design names 11 provinces; verify the laboratory extract's inclusion and weighting rather than importing bulletin coverage.
- The 2018 application route is documented, but its sanitized codebook, geographic fields, charges and present appointments remain unverified; 2008/2024 microdata access is not established here.
- CTUS is an ambiguous acronym also used for university-led time-use surveys. Identify the producer and wave; do not substitute a non-NBS survey for this official 2018 product.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://www.stats.gov.cn/sj/zxfb/202410/t20241031_1957216.html (第三次全国时间利用调查公报（第二号）, fetched+read 2026-08-15; public-tabulation route re-scoped 2026-09-28)
  field_scope:
  - third survey 2024
  - field period 2024-05-11..31
  - two diary days, 15-minute threshold
  - 31 provinces + XPCC
  - ages 6+ first time
  - 34 activity categories
  - app self-report
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/zt_18555/ztsj/2008sjly/ (2008年时间利用调查资料汇编 special section, fetched 2026-08-15)
  field_scope:
  - first survey 2008 exists with official 资料汇编
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1900224.html (ordinary GET 200 and survey-design notes read 2026-09-28)
  field_scope:
  - official 2018 bulletin date, diary timing and recording fields
  - named 11-province design; public results exclude Shanghai
  - reported 20,226 households and 48,580 people; not an approved-extract row count
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/hd/lyzx/zxgk/202405/t20240524_1954036.html (official reply dated 2024-02-23, read 2026-09-28)
  field_scope:
  - explicit confirmation that 2018 time-use data are open for laboratory application
  - boundary that this is not an Excel/raw-data public download
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/zs/tjws/jbtjzswd/tjzn/202412/t20241216_1957775.html (read 2026-09-28)
  field_scope:
  - 2018 time-use database among the offered microdata products
  - institutional eligibility, sanitization, physical laboratory use and application stages
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/zt_18555/zthd/lhfw/2022/rdwt/202302/t20230214_1903571.html (2021 explanation, read 2026-09-28)
  field_scope:
  - institution registration before project application and onsite appointment
  - intermediate-output removal review, final review and registration
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/zwfwck/sjfb/202410/t20241031_1957218.html (2024 Q&A, read 2026-09-28)
  field_scope:
  - reported third-survey household/respondent counts
  - announced future 2024 microdata opening, not proof of current availability
  - official microdata-laboratory contact
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://microdata.stats.gov.cn/ (probe, 200, JS app, 2026-08-15)
  field_scope:
  - microdata portal exists; terms unread
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: nbs-monthly-labor-force-survey
  relation: complement
---

## Positioning in one sentence

The official NBS diary-survey family has a documented conditional laboratory route for 2018, not a public download or a verified all-round archive. Public 2024 national tables remain a separate ready product.

## Select rules

- Use nbs-third-national-time-use-survey-2024-public-bulletins for the directly obtainable 2024 national figures.
- For individual diaries in 2018, check institution registration and apply for onsite use; for other rounds, first establish that the laboratory actually offers them.
- Cross-round comparisons must account for the 2024 method/coverage changes.

## Get recipe

1. If national 2024 aggregate figures suffice, use the separate ready public-bulletin record.
2. For 2018 diaries, establish institutional registration, submit the named-data project application and arrange an approved onsite appointment.
3. Verify the extract codebook, geography and external-data rules before designing joins. Export only outputs approved by the laboratory; do not assume raw files can leave.

## Connections and Limitations

The public tabulation layer remains distinct from controlled diary analysis. The 2018 route is now evidenced, but a fine-geography design still depends on its unread sanitized codebook and permissions. The 2024 opening announcement must not be treated as a present delivery; cross-wave comparisons must account for changes in population, geography and recording.

## Decision sufficiency check

A researcher can start a real 2018 application and distinguish onsite analysis from public 2024 tabulations. The record stays grounding because extract fields/geography and a fully read economics-paper use remain unresolved. A 2023 Statistical Research paper (DOI 10.19343/j.cnki.11-1302/c.2023.07.011) is a promising use lead, but its institutional PDF returned 502; its abstract/indexed excerpts have not been promoted into used_by evidence.
