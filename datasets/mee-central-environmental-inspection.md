---
schema_version: 3
catalog_status: grounding
id: mee-central-environmental-inspection
name: MEE Central Environmental Inspection public records (中央生态环境保护督察 进驻/整改/管理)
aka:
- 中央生态环境保护督察
- central environmental inspection
- central eco-environmental protection inspection
- MEE inspection columns
provider: >-
  生态环境部 (Ministry of Ecology and Environment, MEE), 中央生态环境保护
  督察 columns on mee.gov.cn (verified: /ywgz/zysthjbhdc/ and its sub-columns
  督察进驻/督察整改/督察管理, all fetched 200, 2026-08-15).
china_related: true
domains:
- environment
- regulation
- governance
- public
- policy

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A researcher-built text corpus of central environmental inspection
    announcements: 进驻 (inspection entry) notices, 督察报告/反馈 (report and
    feedback), and 整改 (rectification) plans and progress reports published
    on the MEE columns. The provider publishes text records, not a structured
    dataset; any research table (inspection batch x province x date, or
    rectification outcomes) must be collected and parsed by the researcher.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Official MEE columns publish the full public record family of central
    environmental inspections. Verified on 2026-08-15: the 督察进驻 column
    documents third-round batches through 第三轮第六批 (fully entered
    2026-05-09, entry stage completed 2026-06-10; earlier batches: 第五批
    2025-11-19/2025-12-22, 第四批 completed 2025-07-01); the 督察整改 column
    publishes rectification-progress narratives (e.g. 2025-06 黄河韩城龙门段
    case); the 督察管理 column lists the regional inspection bureaus. No
    structured bulk product or machine-readable export was found.
  barrier: >-
    Collection burden: text-only announcements require per-announcement
    parsing and completeness auditing; batch/coverage metadata are not
    provided as a table.
  last_checked: '2026-08-15'

unit_of_observation: >-
  Inspection-related announcement/notice (进驻通知, 督察反馈, 整改方案/落实情况);
  a researcher-built panel would aggregate to inspection-batch x province x
  stage/date
structure: collection of text records organized by column and date
geo_granularity:
- province (inspection entry batches target provinces; verified via batch news titles)
- prefecture/county within rectification narratives (case-level)
geography: China (provinces covered by each inspection batch; batch coverage lists not read this round)
time_span:
  start: null
  end: null
  last_confirmed_release: '2026-06-10 (第三轮第六批 entry stage completed)'
  coverage_note: >-
    Third-round batches documented through 第六批 (2026). First/second-round
    archives and the full batch list were not read this round; earliest
    archive years unverified.
  last_checked: '2026-08-15'
frequency:
- irregular (per inspection batch and per rectification reporting cycle)
sample_size: null
key_variables:
- Inspection batch number and entry/completion dates (第三轮第四/五/六批 verified)
- Inspection entry notices (进驻公告) and feedback/report texts
- Rectification plans and progress narratives (整改方案/落实情况)
- Provincial/prefecture names in titles and texts

research_fit:
  best_for:
  - Constructing an inspection-exposure or rectification-outcome text panel
    from official public announcements (batch x province x date)
  - Verifying which provinces entered which third-round batches (via 进驻
    news) and reading rectification progress narratives
  choose_over:
  - Choose the MEE columns over secondary news coverage when authoritative
    announcement texts and official dates are required.
  - For treatment/timing classification (which province treated when), the
    variation-side record in Econ-Variation should carry the assignment
    design; this record documents only the public record family.
  not_good_for:
  - A ready-made structured dataset (none published)
  - Firm-level or prefecture-level enforcement data (use
    china-environmental-enforcement / china-firm-pollution for those layers)
  - Any claim about which provinces were inspected in which batch without
    reading the batch announcement lists
  needs_join_for:
  - Firm/plant outcomes (china-firm-pollution, asif)
  - Local environmental outcomes (china-air-quality-monitoring,
    china-water-quality-monitoring, china-satellite-pm25)
  - Treatment timing and assignment design (Econ-Variation side)
  variation_available:
  - Batch timing variation across provinces (subject to reading each batch's
    coverage list)
  - Pre/post rectification comparisons from rectification records
  topics:
  - central environmental inspection
  - environmental regulation
  - policy enforcement
  - governance records

good_for:
- inspection exposure construction
- rectification process research
identification: []
linkable_keys:
- Province
- Inspection batch
- Announcement date

joins:
- target: china-environmental-enforcement
  relation: complement
  keys:
  - province/prefecture + year
  method: compare official inspection records with firm-level enforcement data; normalize geography codes
  evidence_status: plausible
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - prefecture + date
  method: link inspection timing to environmental outcome series
  evidence_status: plausible

access_routes:
- route: MEE 中央生态环境保护督察 columns
  access_status: available
  direct_url: https://www.mee.gov.cn/ywgz/zysthjbhdc/
  requirements: none (public pages; automated clients fetched 200)
  steps:
  - Open the 中央生态环境保护督察 column; browse 督察进驻 (entry notices and batch news), 督察整改 (rectification plans/progress), 督察管理 (bureaus).
  - Collect announcement pages for the batches/years of interest; parse titles, dates and body text.
  - Build the research table (batch x province x stage/date) with completeness auditing against the batch news series.
  deliverable: collected text records; researcher-built panel
  cost: free
  last_checked: '2026-08-15'
  caveat: batch coverage lists (which provinces per batch) were not read this round; verify per batch before constructing exposure

access:
  url: https://www.mee.gov.cn/ywgz/zysthjbhdc/
  cost: free
  license: Public government announcements; reuse subject to official rules
  format:
  - HTML announcement pages
  api: false
  how_to_get: Browse the official columns and collect announcement texts; no bulk export exists.
caveats:
- Only text records; no structured product, API or bulk download found.
- Third-round batches verified through 第六批 (2026); first/second-round archives and earliest years unread.
- This record documents the public record family only; treatment/assignment design belongs to the variation repository.

production:
  raw_sources:
  - name: MEE 中央生态环境保护督察 columns (进驻/整改/管理)
    source_type: webpage
    role: official announcement texts and batch news
    access_route: public pages
    url: https://www.mee.gov.cn/ywgz/zysthjbhdc/
    coverage: third-round batches verified through 第六批 (2026); earlier archives unread
    last_checked: '2026-08-15'
  acquisition_methods:
  - crawl
  - manual coding
  sample_construction: >-
    Batch/province universe must be defined from the 进驻 news series and
    each batch's coverage list (batch province lists NOT read this round).
    Rectification records selected by column and date.
  pipeline_stages:
  - stage: collect
    inputs:
    - target batches/years
    method: collect announcement pages from the three columns
    tools: []
    parameters: {}
    output: announcement text corpus
    evidence: official columns (read 2026-08-15)
  - stage: parse
    inputs:
    - announcement corpus
    method: parse titles, dates, batch numbers, province/prefecture names
    tools: []
    parameters: {}
    output: batch x province x stage/date table
    evidence: researcher-side work (no provider template)
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: announcement / batch x province x stage
    structure: text corpus + researcher-built table
    geography: China (provinces per batch)
    time_span: third-round batches 2024-2026 (verified examples)
    key_variables:
    - batch number, entry/completion dates, province, announcement type
    formats:
    - HTML -> text/table
  reproducibility:
    level: medium
    starting_point: official MEE columns
    code_available: false
    code_url: null
    requirements:
    - collection script + completeness audit against batch news series
    blockers:
    - batch province lists unread this round
    - first/second-round archives unread
  compliance:
    terms_or_license: public government announcements
    robots_or_rate_limits: unknown; fetched fine from automated clients
    personal_or_sensitive_data: none expected (public announcements)
    redistribution: reuse under official rules
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://www.mee.gov.cn/ywgz/zysthjbhdc/ (中央生态环境保护督察 column, fetched 200, 2026-08-15)
  field_scope:
  - column identity and sub-columns (进驻/整改/管理)
  - third-round batch news (第四/五/六批 with dates)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/ywgz/zysthjbhdc/dczg/ (督察整改 column, fetched 200, 2026-08-15)
  field_scope:
  - rectification narratives published (2024-2025 dated examples)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/ywgz/zysthjbhdc/dcjg/ (督察管理/机构 page, fetched 200, 2026-08-15)
  field_scope:
  - regional inspection bureaus listed
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: china-environmental-enforcement
  relation: complement
- id: china-air-quality-monitoring
  relation: complement
---

## Positioning in one sentence

The MEE central environmental inspection columns publish the official announcement record family (进驻/整改/管理) with third-round batches documented through 2026-06; researchers must collect and parse the text themselves - no structured product exists.

## Select rules

- Use these columns as the authoritative public record family for constructing inspection exposure or rectification panels.
- For firm-level enforcement use china-environmental-enforcement / china-firm-pollution instead.
- Do not use this record for treatment classification without reading each batch's province list.

## Get recipe

1. Open the MEE inspection columns and identify the target batches (进驻 news series pins batch dates).
2. Collect the announcement pages (进驻公告, 反馈, 整改方案/落实情况).
3. Parse into a batch x province x date table with a completeness audit.

## Connections and Limitations

The record family is text-only; batch coverage lists were not read this round. First/second-round archives and earliest years unverified. Assignment/treatment design belongs to Econ-Variation, not to this data record.

## Decision sufficiency check

A researcher can start a collection of official inspection records, knows the columns, the verified batch chronology (第三轮第四-六批), and the parsing burden; batch province lists and the pre-third-round archive are the remaining unknowns - grounding is appropriate.
