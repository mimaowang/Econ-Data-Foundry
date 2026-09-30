---
schema_version: 3
catalog_status: grounding
id: samr-food-sampling-inspection
name: SAMR national food-safety sampling inspection announcements (食品安全抽检通告)
aka:
- 食品安全抽检通告
- 食品抽检不合格通告
- SAMR food sampling announcements
- 市场监管总局关于XX批次食品抽检情况的通告
provider: >-
  国家市场监督管理总局 (State Administration for Market Regulation, SAMR).
  Verified 2026-08-15: the 食品生产经营安全监督管理司 column
  (samr.gov.cn/spscs/, 200) and a representative national 通告 article
  (市场监管总局关于35批次食品抽检不合格情况的通告, 2025-07-25, column 食品抽检司,
  fetched 200, read). The former 食品安全抽检监测司 column URL
  (samr.gov.cn/spcjjg/) returns 404 (post-2023 restructuring).
china_related: true
domains:
- food safety
- regulation
- health
- public

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A researcher-built dataset of national food-sampling inspection
    announcements: the SAMR monthly 通告 series (e.g. 关于XX批次食品抽检
    不合格情况的通告) listing inspected samples and non-compliant items. The
    provider publishes announcement texts; the underlying 国家食品安全抽检
    监测信息系统 is internal. Collection = locating and parsing the 通告
    series (batch numbers, dates, product/enterprise and non-compliance
    fields).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    SAMR publishes national food-sampling inspection announcements with
    batch counts and non-compliant items (verified example: 35批次不合格,
    published 2025-07-25 under the 食品抽检司 column). The current
    announcement column and its full listing structure were not fully pinned
    this round (a column URL probe 404'd); the underlying sampling system is
    internal, so researchers must collect and parse announcement texts.
  barrier: >-
    Text-only announcements; current column/listing URL unverified; batch
    structure and completeness need auditing; no bulk export found.
  last_checked: '2026-08-15'

unit_of_observation: >-
  Food-sampling announcement (通告) at the national level, containing
  per-batch lists of inspected/non-compliant samples; a researcher-built
  table would go down to sample/item level
structure: series of announcement documents (text)
geo_granularity:
- national announcements
- product/enterprise locations within announcements (field-level unverified)
geography: China (national sampling program; sampling design unread)
time_span:
  start: null
  end: null
  last_confirmed_release: '2025-07-25 (35批次 example announcement)'
  coverage_note: >-
    Series history (earliest years, cadence) unverified; the example
    announcement is from 2025.
  last_checked: '2026-08-15'
frequency:
- regular announcement series (monthly-ish cadence per the 通告 naming; exact cadence unverified)
sample_size: null
key_variables:
- Announcement batch number and date
- Number of inspected/non-compliant batches (example: 35批次不合格)
- Product names, sampling units and non-compliance items (per announcement text; field structure unread)

research_fit:
  best_for:
  - Building a national food-sampling/quality-event dataset from official
    announcements (non-compliance batches over time)
  - Regulatory-enforcement research on food safety where official 通告 are
    the public record family
  choose_over:
  - Choose SAMR 通告 over secondary food-safety news when official batch
    counts and product-level detail are required.
  - For firm-level enforcement outcomes use china-environmental-enforcement
    analog families or firm platforms; this record is the food-sampling
    announcement layer.
  not_good_for:
  - Complete sampling-design data (the underlying system is internal)
  - Bulk structured exports (none found)
  - Province-level sampling databases (national announcements only verified;
    provincial bureaus publish separately)
  needs_join_for:
  - Enterprise outcomes (qichacha/china-tianyancha-firm-information) via
    named enterprises in announcements
  - Market context (china-stat-yearbook)
  variation_available:
  - Batch-level timing variation of announced non-compliance
  topics:
  - food safety
  - sampling inspection
  - regulatory enforcement
  - consumer protection

good_for:
- food safety announcement research
- non-compliance batch series
identification: []
linkable_keys:
- Announcement date/number
- Product/enterprise names

joins:
- target: china-tianyancha-firm-information
  relation: complement
  keys:
  - enterprise names in announcements
  method: entity resolution from announcement text to firm records
  evidence_status: plausible

access_routes:
- route: SAMR announcement pages (通告 series)
  access_status: available
  direct_url: https://www.samr.gov.cn/spscs/
  requirements: none (public pages)
  steps:
  - Locate the current 通告 listing (the 食品抽检司/食品生产经营安全监督管理司 columns; the exact listing URL was not pinned this round).
  - Collect announcements of interest (e.g. via site search for 食品抽检不合格情况的通告).
  - Parse batch counts, products, enterprises and non-compliance items into a research table.
  deliverable: collected announcement texts / researcher-built batch table
  cost: free
  last_checked: '2026-08-15'
  caveat: 'the listing column URL probed this round returned 404; use site search or the article URL pattern (zw/zfxxgk/fdzdgknr/spcjs/art/...)'

access:
  url: https://www.samr.gov.cn/spscs/
  cost: free
  license: Public government announcements; reuse under official rules
  format:
  - HTML announcement pages
  api: false
  how_to_get: Browse/search SAMR for the 通告 series; collect and parse announcements.
caveats:
- Current listing column URL unverified (404 on probe; the example article itself fetched 200).
- Sampling design and the underlying system are internal; only announcement texts are public.
- Series history (years, cadence, completeness) unverified.

production:
  raw_sources:
  - name: SAMR 通告 series (食品抽检司 column)
    source_type: webpage
    role: national food-sampling inspection announcements (批次不合格 lists)
    access_route: public announcement pages
    url: https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/spcjs/art/2025/art_4375a079d848481b8e16eeb1973a3bb3.html
    coverage: example 2025-07-25 (35批次); series history unverified
    last_checked: '2026-08-15'
  acquisition_methods:
  - crawl
  - manual coding
  sample_construction: >-
    Announcement universe must be located via site search (the listing
    column URL probed this round returned 404) and audited against
    announcement numbering. Underlying sampling design is internal.
  pipeline_stages:
  - stage: collect
    inputs:
    - target period
    method: locate and collect 通告 articles via site search/article URL pattern
    tools: []
    parameters: {}
    output: announcement corpus
    evidence: example article (read 2026-08-15)
  - stage: parse
    inputs:
    - announcement corpus
    method: parse batch counts, dates, products, enterprises, non-compliance items
    tools: []
    parameters: {}
    output: batch/sample-level table
    evidence: researcher-side work
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: announcement / sample batch
    structure: announcement series + researcher-built table
    geography: China (national announcements)
    time_span: 2025 example; history unverified
    key_variables:
    - announcement date/number, batch count, products, enterprises, non-compliance
    formats:
    - HTML -> text/table
  reproducibility:
    level: medium
    starting_point: SAMR announcement pages
    code_available: false
    code_url: null
    requirements:
    - collection script + completeness audit
    blockers:
    - current listing column URL unverified
    - series history unverified
  compliance:
    terms_or_license: public government announcements
    robots_or_rate_limits: unknown
    personal_or_sensitive_data: none expected (public announcements)
    redistribution: reuse under official rules
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://www.samr.gov.cn/spscs/ (食品生产经营安全监督管理司 column, fetched 200, 2026-08-15)
  field_scope:
  - current department column identity
  - news content (not the 通告 listing itself)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/spcjs/art/2025/art_4375a079d848481b8e16eeb1973a3bb3.html (市场监管总局关于35批次食品抽检不合格情况的通告, fetched 200, read 2026-08-15)
  field_scope:
  - announcement series exists (35批次 example, PubDate 2025-07-25)
  - column metadata 食品抽检司
  - article URL pattern
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.samr.gov.cn/spcjjg/ (probe 404, 2026-08-15)
  field_scope:
  - former 抽检监测司 column moved/merged (404, not absence)
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: nmpa-drug-approval-database
  relation: complement
- id: china-tianyancha-firm-information
  relation: complement
---

## Positioning in one sentence

SAMR's national food-sampling 通告 series (e.g. 35批次不合格, 2025-07-25) is the official public record family for food-sampling enforcement; the underlying system is internal, the current listing column is unpinned, and any research dataset must be collected from announcement texts.

## Select rules

- Use the 通告 series for national food-sampling enforcement research built from official announcements.
- Do not promise bulk exports or sampling-design data - neither is public.
- For enterprise-level outcomes, join named enterprises to firm platforms.

## Get recipe

1. Search SAMR for 食品抽检不合格情况的通告 to locate the series (the pinned example article works; the listing column URL is unverified).
2. Collect announcements for the target period; parse batches/products/non-compliance.
3. Audit series completeness against announcement numbering.

## Connections and Limitations

Only announcement texts are public; the sampling system is internal. Series history and listing structure unverified. Announcement-level joins to firms require text parsing and entity resolution.

## Decision sufficiency check

A researcher can find and parse the official 通告 series (one working article URL pinned), knows the internal-system boundary and the unverified listing column - grounding is appropriate.
