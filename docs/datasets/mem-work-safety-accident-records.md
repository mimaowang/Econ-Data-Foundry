---
schema_version: 3
catalog_status: grounding
id: mem-work-safety-accident-records
name: MEM work-safety accident investigation and supervision records (生产安全事故查处/挂牌督办/调查报告)
aka:
- 事故及灾害查处
- 重大生产安全事故查处挂牌督办
- 事故调查报告
- MEM accident records
- 安委督
provider: >-
  应急管理部 (Ministry of Emergency Management, MEM), 事故及灾害查处 section
  mem.gov.cn/gk/sgcc/. Verified 2026-08-15: the section redirects to the
  挂牌督办 (supervision) and 调查报告 (investigation-report) sub-columns
  (sggpdbqk/ and tbzdsgdcbg/, both fetched 200 and read).
china_related: true
domains:
- work safety
- regulation
- public
- industrial accidents

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A researcher-built database of work-safety accident records: 挂牌督办
    通知书 (supervision notices, numbered 安委督〔year〕N号) and 事故调查报告
    (investigation reports), published as text pages on mem.gov.cn. No
    machine-readable bulk export found; collection = parsing announcement
    pages (dates, accident types, enterprises, casualties).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    MEM publishes work-safety accident supervision and investigation records.
    Verified 2026-08-15: the 挂牌督办 column lists 重大生产安全事故查处挂牌
    督办通知书 (安委督〔2026〕1号, 2026-01-19; 安委督〔2025〕7号, 2025-11-28;
    natural-disaster investigation supervision notices 2026-08-02) with
    yearly sub-columns (2024-2026); the 调查报告 column (特别重大事故调查
    报告 family) fetched 200. Text-only public records; completeness and
    fields unverified.
  barrier: >-
    Text pages; parsing and completeness auditing required; no bulk export;
    full report inventory and fields unverified.
  last_checked: '2026-08-15'

unit_of_observation: >-
  Accident supervision/investigation document (挂牌督办通知书 or 事故调查报告);
  a researcher-built table would aggregate to accident-level records
structure: document series organized by column and year
geo_granularity:
- accident location (province/city within document text; field-level unverified)
geography: China (major work-safety accidents; geographic field structure unverified)
time_span:
  start: null
  end: null
  last_confirmed_release: '2026-08-02 (natural-disaster supervision notice)'
  coverage_note: >-
    Yearly supervision sub-columns verified for 2024-2026; earlier years and
    the full investigation-report inventory unverified.
  last_checked: '2026-08-15'
frequency:
- irregular (per major accident and supervision decision)
sample_size: null
key_variables:
- Supervision notice number (安委督〔year〕N号) and date
- Accident type and location (in document text)
- Investigation report texts (特别重大事故调查报告 family)
- Related enterprise/unit names (in text)

research_fit:
  best_for:
  - Constructing major work-safety accident event records (supervision
    notices + investigation reports) from official MEM pages
  - Research on severe industrial accidents where official documents are the
    authoritative record family
  choose_over:
  - Choose MEM official columns over news compilations for authoritative
    accident documents and notice numbering.
  - For firm-level production/enforcement data use asif /
    china-environmental-enforcement; this record is the accident-document
    layer.
  not_good_for:
  - Complete casualty/incident statistics for all accidents (only major
    accidents are published this way; MEM statistics bulletins are separate)
  - Bulk structured exports (none found)
  - County-level completeness (coverage audit required)
  needs_join_for:
  - Firm outcomes (asif, qichacha/china-tianyancha-firm-information) via
    named units
  - Regional context (china-stat-yearbook)
  variation_available:
  - Timing variation of supervision notices (2024-2026 verified)
  topics:
  - work safety
  - industrial accidents
  - accident investigation
  - regulation

good_for:
- major accident event records
- work-safety enforcement research
identification: []
linkable_keys:
- Notice number/date
- Accident location/enterprise names

joins:
- target: china-tianyancha-firm-information
  relation: complement
  keys:
  - enterprise names in documents
  method: entity resolution from accident documents to firm records
  evidence_status: plausible

access_routes:
- route: MEM 事故及灾害查处 columns
  access_status: available
  direct_url: https://www.mem.gov.cn/gk/sgcc/sggpdbqk/
  requirements: none (public pages; fetched 200)
  steps:
  - Open the 挂牌督办 column (yearly lists) and the 调查报告 column (mem.gov.cn/gk/sgcc/tbzdsgdcbg/).
  - Collect notices/reports for the target years; parse notice numbers, dates, locations and enterprises.
  - Build the accident table with a completeness audit against the yearly lists.
  deliverable: collected document texts / researcher-built accident records
  cost: free
  last_checked: '2026-08-15'
  caveat: the parent section URL (mem.gov.cn/gk/sgcc/) is a JS redirect shell; use the sub-column URLs directly

access:
  url: https://www.mem.gov.cn/gk/sgcc/sggpdbqk/
  cost: free
  license: Public government documents; reuse under official rules
  format:
  - HTML document pages
  api: false
  how_to_get: Browse the sub-columns directly; collect and parse document pages.
caveats:
- Text-only records; completeness and field structure unverified.
- Only major accidents are published as supervision/report documents - not a full incident census.
- Earlier-year archives and the full report inventory unverified.

production:
  raw_sources:
  - name: MEM 挂牌督办 column
    source_type: webpage
    role: supervision notices (安委督 numbering), yearly lists
    access_route: public pages
    url: https://www.mem.gov.cn/gk/sgcc/sggpdbqk/
    coverage: yearly sub-columns verified 2024-2026; earlier years unread
    last_checked: '2026-08-15'
  - name: MEM 调查报告 column
    source_type: webpage
    role: investigation reports (特别重大事故调查报告 family)
    access_route: public pages
    url: https://www.mem.gov.cn/gk/sgcc/tbzdsgdcbg/
    coverage: column verified; full report inventory unread
    last_checked: '2026-08-15'
  acquisition_methods:
  - crawl
  - manual coding
  sample_construction: >-
    Universe = notices/reports listed in the yearly sub-columns; completeness
    must be audited against the yearly lists (2024-2026 verified). Only major
    accidents are published this way.
  pipeline_stages:
  - stage: collect
    inputs:
    - target years
    method: collect document pages from the two columns
    tools: []
    parameters: {}
    output: accident document corpus
    evidence: official columns (read 2026-08-15)
  - stage: parse
    inputs:
    - document corpus
    method: parse notice numbers (安委督〔year〕N号), dates, accident types, locations, enterprises
    tools: []
    parameters: {}
    output: accident-level table
    evidence: researcher-side work (no provider template)
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: accident document / accident record
    structure: document series + researcher-built table
    geography: China (major work-safety accidents)
    time_span: 2024-2026 verified; earlier unverified
    key_variables:
    - notice number, date, accident type/location, enterprises
    formats:
    - HTML -> text/table
  reproducibility:
    level: medium
    starting_point: MEM sub-columns
    code_available: false
    code_url: null
    requirements:
    - collection script + completeness audit
    blockers:
    - full report inventory and earlier archives unread
  compliance:
    terms_or_license: public government documents
    robots_or_rate_limits: unknown
    personal_or_sensitive_data: none expected (official documents)
    redistribution: reuse under official rules
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://www.mem.gov.cn/gk/sgcc/sggpdbqk/ (挂牌督办 column, fetched 200, decompressed+read 2026-08-15)
  field_scope:
  - column identity (挂牌督办)
  - yearly sub-columns 2024-2026
  - example notices (安委督〔2026〕1号 2026-01-19; 安委督〔2025〕7号 2025-11-28; 自然灾害调查评估挂牌督办通知书 2026-08-02)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.mem.gov.cn/gk/sgcc/tbzdsgdcbg/ (调查报告 column, fetched 200, read 2026-08-15)
  field_scope:
  - investigation-report column exists (特别重大事故调查报告 family)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.mem.gov.cn/gk/sgcc/ (fetched 200, 484B JS redirect shell, 2026-08-15)
  field_scope:
  - parent section is a redirect shell; use sub-columns
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: samr-food-sampling-inspection
  relation: complement
- id: china-tianyancha-firm-information
  relation: complement
---

## Positioning in one sentence

MEM's 挂牌督办 and 调查报告 columns publish official work-safety accident supervision notices (安委督 numbering) and investigation reports - verified as public text records (2024-2026 yearly lists), with any research table requiring collection and parsing.

## Select rules

- Use the MEM columns as the authoritative document family for major work-safety accidents.
- Not a full incident census - only major accidents appear as supervision/report documents.
- For firm-level outcomes, join named units to firm platforms.

## Get recipe

1. Open the 挂牌督办 column (yearly lists) and the 调查报告 column directly (the parent section is a redirect shell).
2. Collect documents for target years; parse notice numbers, dates, locations, enterprises.
3. Audit completeness against the yearly lists.

## Connections and Limitations

Only major accidents are covered; fields and full inventory unverified; text parsing is the researcher's burden. The record documents the public layer only.

## Decision sufficiency check

A researcher can reach both columns directly, knows the document types and numbering, and the coverage boundary (major accidents only) - grounding is appropriate.
