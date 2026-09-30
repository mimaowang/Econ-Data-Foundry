---
schema_version: 3
catalog_status: grounding
id: cec-electricity-statistics
name: CEC China electricity industry statistics (中国电力企业联合会 电力统计/供需报告)
aka:
- 中电联
- CEC
- CECI (中国电煤采购价格指数)
- 中国电力统计年鉴
- China Electricity Council statistics
provider: >-
  中国电力企业联合会 (China Electricity Council, CEC), official site
  cec.org.cn (fetched 200, 2026-08-15). CECI (China Coal-Purchase Price
  Index, 中国电煤采购价格指数) pages and the 电力市场/供需报告/年度报告 tabs
  are official; detail pages are JavaScript-rendered.
china_related: true
domains:
- energy
- electricity
- macro
- industry
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Industry-wide electricity statistics: installed capacity, generation and
    electricity-consumption aggregates (e.g. annual 电力统计基本数据/公报 and
    中国电力统计年鉴) plus CEC analysis reports (年度发展报告, 供需形势分析).
    The separately recorded cec-national-electricity-market-transaction-bulletins
    product covers browser-readable published market-transaction releases.
    The public web layer (cec.org.cn columns) is JS-rendered and was not
    readable in detail from an automated client; the 中国电力统计年鉴 is a
    paid publication; an exact 2022 publisher listing is verified below.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    CEC is the industry association publishing China-wide electricity
    statistics (capacity/generation/consumption aggregates). Verified
    2026-08-15: cec.org.cn home (200, columns 电力市场/供需报告/年度报告 and
    official CECI pages), while menu/detail pages return JavaScript shells to
    automated clients; cec.org.cn hosts official PDF reports (reachable,
    application/pdf). The annual 中国电力统计年鉴 and 中国电力行业年度发展报告
    exist (secondary sources for the 2024 leads). The 2022 statistical
    yearbook now has a verified official publisher listing.
    No machine-readable bulk export was found.
  barrier: >-
    Statistics tables are JS-gated on the web (human browser needed); the
    yearbook is a paid book; a researcher-built time series requires
    transcription from reports/tables.
  last_checked: '2026-09-28'

unit_of_observation: >-
  Industry/national aggregate series (e.g. annual or monthly installed
  capacity, generation, consumption) and CECI index series
structure: time series of aggregates
geo_granularity:
- national (industry aggregates)
- province breakdowns where published in yearbooks/reports (unverified this round)
geography: China national aggregates and region-labelled yearbook tables; the exact regional units must be confirmed from the selected edition
time_span:
  start: null
  end: null
  last_confirmed_release: null
  coverage_note: >-
    Annual yearbook series exists (中国电力统计年鉴, latest 2024 edition per
    secondary sources). The official 2022 edition's contents include tables
    explicitly labelled 2021; inspect each table for its actual year range.
    Web column coverage years remain unverified.
  last_checked: '2026-08-15'
frequency:
- annual (yearbook/公报)
- monthly or daily for some series (CECI index; 用电量 series - unverified)
sample_size: null
key_variables:
- Installed power generation capacity (装机容量)
- Power generation (发电量) by source
- Electricity consumption (用电量/全社会用电量)
- CECI coal-purchase price index series (official CECI pages verified)

research_fit:
  best_for:
  - National China electricity industry aggregates (capacity/generation/
    consumption) from the industry association
  - Coal-price pressure index (CECI) series and CEC annual development reports
  choose_over:
  - Choose cec-national-electricity-market-transaction-bulletins for the distinct public CEC bulletins reporting national and selected grid-region electricity-market transaction volumes; do not treat an unverified yearbook route as necessary for that narrower product.
  - For city/prefecture-level electricity consumption, the china-stat-yearbook
    family (or CEIC) covers more granular series; CEC is the industry-level
    aggregate source.
  - For firm- or plant-level electricity data use china-coal-power-plant-panel
    or grid/enterprise datasets.
  not_good_for:
  - City-level or county-level electricity series (not verified here)
  - Machine-readable bulk downloads (none found)
  - Firm/plant-level records
  needs_join_for:
  - Macro context (GDP, industry output) from china-stat-yearbook / WDI
  - Subnational series from the yearbook family
  variation_available:
  - Time-series variation in national electricity aggregates and the CECI index
  topics:
  - electricity
  - energy statistics
  - coal prices
  - power industry

good_for:
- national electricity aggregates
- energy industry analysis
identification: []
linkable_keys:
- Year/month

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - year
  method: combine national electricity aggregates with macro yearbook series; subnational needs the yearbook family
  evidence_status: plausible
- target: china-coal-power-plant-panel
  relation: complement
  keys: []
  method: plant-level vs industry-aggregate layers are different assets; do not merge
  evidence_status: plausible

access_routes:
- route: CEC official site columns
  access_status: partial
  direct_url: https://www.cec.org.cn/
  requirements: human browser for the JS-rendered statistics columns and report pages
  steps:
  - Open cec.org.cn; browse 电力市场/供需报告/年度报告 tabs and the official CECI pages.
  - Read/download report PDFs hosted on cec.org.cn (reachable from automated clients as application/pdf).
  deliverable: report PDFs and web tables (researcher must transcribe/parse)
  cost: free
  last_checked: '2026-08-15'
  caveat: >-
    Menu/detail pages need a normal browser. The official home page still returned 200 on
    2026-09-28, but its static HTML exposed no directly actionable PDF link; this is not
    evidence that reports do not exist, only that the home page alone does not close a
    report-acquisition route.
- route: 中国电力统计年鉴2022 (official publisher listing)
  access_status: paid
  direct_url: https://www.zgtjcbs.com/quanbutushu/5458
  requirements: Purchase or library access; confirm stock and fulfilment with the publisher
  steps:
  - Identify the 2022 edition by ISBN 978-7-5037-9844-3.
  - Use the publisher ordering/contact option or ask a library for that edition.
  - Inspect table years, region names, definitions and notes before transcription.
  deliverable: Listed hardback statistical yearbook; no digital export established
  cost: paid
  last_checked: '2026-09-28'
  caveat: Publisher lists RMB 498 and publication date 2022-07-08; current stock, delivery price and digital rights need confirmation. The 2024 edition remains a separate unverified lead.

access:
  url: https://www.cec.org.cn/
  cost: mixed
  license: Provider terms (unread); yearbook under publisher terms
  format:
  - HTML/JS web tables
  - PDF reports
  - printed/PDF yearbook
  api: false
  how_to_get: Browse the official site in a browser for report PDFs; purchase the yearbook for full tabulations.
caveats:
- Web statistics content is JS-gated; the exact 电力统计公报/基本数据 tables and their free availability were NOT verified this round (candidate-level unknown retained).
- The 2022 publisher listing closes edition identity and the listed book price, but not current stock, digital delivery or table-level coverage. The 2024 edition remains unverified.
- CECI index is a price index for coal purchases, not an electricity flow series.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-08-15'

used_by: []

provenance:
- source: https://www.cec.org.cn/ (official home, fetched 200, 2026-08-15)
  field_scope:
  - provider identity
  - 电力市场/供需报告/年度报告 tabs
  - CECI official pages and independence statement
  added: '2026-08-15'
  confidence: high
  verified: true
- source: cec.org.cn menu/detail probes (JS shells, 2026-08-15) and hosted PDF probe (206 application/pdf)
  field_scope:
  - detail content JS-gated
  - official PDF hosting reachable
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://www.cec.org.cn/ (official home fetched 200, static HTML inspected 2026-09-28)
  field_scope:
  - current homepage reachability
  - negative boundary: no directly actionable PDF href in the inspected static homepage HTML
  added: '2026-09-28'
  confidence: high
  verified: true
- source: 中国电力统计年鉴2024 / 中国电力行业年度发展报告2024 (web search leads - fxbaogao/sdyanbao news pages)
  field_scope:
  - yearbook and annual development report exist (secondary)
  added: '2026-08-15'
  confidence: low
  verified: false
- source: https://www.zgtjcbs.com/quanbutushu/5458 (official publisher page read 2026-09-28)
  field_scope:
  - 2022 edition, CEC authorship, ISBN, binding, publication date and listed price
  - Regional capacity, generation and consumption table headings; selected tables explicitly labelled 2021
  - Book acquisition lead, not stock confirmation or digital access
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: cec-national-electricity-market-transaction-bulletins
  relation: component
- id: china-stat-yearbook
  relation: complement
- id: china-coal-power-plant-panel
  relation: complement
---

## Positioning in one sentence

CEC publishes electricity industry aggregates and regional yearbook tables alongside a separate coal-price index. The official 2022 yearbook listing supplies a concrete book-acquisition start; the web-table set, exact regional units and digital delivery remain unverified.

## Select rules

- Use CEC for national electricity aggregates and CEC analysis reports.
- For city-level electricity consumption use the china-stat-yearbook family; for plant-level use china-coal-power-plant-panel.
- Do not promise machine-readable bulk access - none was found.

## Get recipe

1. Browse cec.org.cn in a human browser for the statistics columns and report PDFs.
2. Transcribe/parse the needed series into a researcher-built table.
3. For yearbook coverage, purchase or use a library copy.

## Connections and Limitations

The public web-table set remains unverified. The 2022 yearbook is now identified at its official publisher, but its actual table contents and delivery conditions still require inspection. CECI is a coal-price index, not an electricity-flow series.

## Decision sufficiency check

A researcher now knows where the industry aggregates live, that the web layer is browser-only, and that the yearbook is the paid fallback; the exact free table set remains unknown - grounding status is appropriate.
