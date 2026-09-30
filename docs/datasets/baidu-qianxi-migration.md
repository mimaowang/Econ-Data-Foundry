---
schema_version: 3
catalog_status: grounding
id: baidu-qianxi-migration
name: Baidu Migration Index (百度迁徙, 百度地图慧眼)
aka:
- 百度迁徙
- Baidu Qianxi
- 百度迁徙大数据
- Baidu Maps Huiyan migration index
- qianxi.baidu.com
provider: >-
  百度地图慧眼 (Baidu Maps Huiyan), the spatiotemporal big-data brand of
  Baidu Maps. Verified 2026-08-15: qianxi.baidu.com (200, JS app, title
  百度迁徙-百度地图慧眼, description 通过将定位可视化直观呈现国内人口迁徙情况) and
  huiyan.baidu.com (200, read: 基于百度地图时空特性数据推出的时空大数据服务
  品牌, with 数据平台/数据API/数据可视化大屏/数据报告 product forms for 政企
  客户).
china_related: true
domains:
- migration
- mobility
- urban
- spatial
- transport

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The public browser-visible layer of Baidu Qianxi: for a selected day, a
    national city-level ranking of the top 20 inbound destinations or top 20
    outbound origins, with city/province label and a provider-displayed
    “比例” value. The broader underlying mobility detail is not publicly
    delivered by this interface; it directs a user to contact Baidu for detail.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Browser verification on 2026-09-28 establishes a narrow public layer: the
    page displayed city-level inbound and outbound top-20 rankings with a
    “比例” column for selected dates, and its date selector visibly offered
    2026-01-01 through 2026-09-27. It is a DIFFERENT provider and product
    from Gaode/AMAP's migration indices (china-amap-migration-flow-indices):
    Baidu Maps Huiyan versus Gaode LBS, with separate index construction and
    platforms. The page says “获取详情数据请点击联系我们”, so it does not
    establish a downloadable full city panel, OD matrix, index definition,
    bulk history, or research API.
  barrier: >-
    The publicly visible product stops at a selected-day top-20 ranking. No
    documented researcher export/API, full city list, OD matrix, bulk history,
    index-definition documentation, or terms for retained research data were
    verified; any page-internal API use would be undocumented scraping.
  last_checked: '2026-09-28'

unit_of_observation: >-
  One row in a selected-day national top-20 city ranking: rank, city/province
  label, and the provider-displayed “比例” for either inbound destinations or
  outbound origins. The denominator and index construction are not explained
  in the observed interface.
structure: Selected-day national top-20 ranking table, separately viewable for inbound and outbound city lists.
geo_granularity:
- city (only the displayed top 20 for the selected national ranking)
geography: National China page; the observed public table does not establish a complete city universe.
time_span:
  start: '2026-01-01'
  end: '2026-09-27'
  last_confirmed_release: '2026-09-27'
  coverage_note: >-
    The browser-visible date selector offered every observed calendar date
    from 2026-01-01 to 2026-09-27 when checked. This confirms those selectable
    dates only; it does not establish availability before 2026-01-01, after
    2026-09-27, or a stable historical archive.
  last_checked: '2026-09-28'
frequency:
- daily
sample_size: null
key_variables:
- Rank, city name and province label in national inbound/outbound top-20 lists
- Provider-displayed “比例” for each displayed city and selected date

research_fit:
  best_for:
  - Describing selected-day national leading migration destinations or origins
    in the browser-visible 2026 date range
  - Small, manually transcribed exploratory comparisons of top-ranked cities,
    with each selected date and page retrieval retained
  choose_over:
  - Choose Baidu Qianxi or AMAP migration indices (china-amap-migration-
    flow-indices) as two separate provider products; decide on coverage,
    series availability and terms per project - do not treat them as one
    asset.
  - For commuting delineations use china-commuting-based-metropolitan-areas;
    for freight use china-city-to-city-truck-flows.
  not_good_for:
  - Absolute migration counts, complete city coverage or origin-destination flows
  - Individual-level data (aggregated)
  - Reproducing another paper's city panel without the paper's collection procedure and terms
  needs_join_for:
  - Outcomes at city level (Tianyancha/Qichacha firm data, yearbook series)
  - Treatment timing (Econ-Variation side)
  variation_available:
  - Day-to-day and top-ranked-city variation within the browser-visible dates;
    this is not a complete city panel
  topics:
  - human migration
  - mobility
  - Baidu big data
  - COVID-19 mobility

good_for:
- Descriptive top-city migration ranking checks
identification: []
linkable_keys:
- City name and province label
- Selected date

joins:
- target: china-amap-migration-flow-indices
  relation: substitute
  keys:
  - city + date
  method: distinct provider products (Baidu vs Gaode) with different index construction; compare series before combining, never merge blindly
  evidence_status: plausible
- target: china-commuting-based-metropolitan-areas
  relation: often-confused-with
  keys: []
  method: Baidu-derived but different product (2017 commuting delineations vs daily migration indices)
  evidence_status: plausible

access_routes:
- route: qianxi.baidu.com public page
  access_status: partial
  direct_url: https://qianxi.baidu.com/
  requirements: human browser (JS app; automated clients receive the HTML shell only)
  steps:
  - Open qianxi.baidu.com in a browser and choose 城市级别.
  - Select 热门迁入地 or 热门迁出地, then choose one available date.
  - Manually transcribe the 20 visible rank/city/province/“比例” rows with the selected date and retrieval date.
  - Treat the page's “获取详情数据请点击联系我们” notice as the stopping point; do not infer an export or scrape its internal API.
  deliverable: A researcher-transcribed selected-day national top-20 inbound or outbound city ranking; no export or full panel was verified.
  cost: free
  last_checked: '2026-09-28'
  caveat: The visible table is top 20 only. The observed date selector covered 2026-01-01..2026-09-27, but does not prove a permanent archive; “比例” is the provider's displayed label, whose denominator is not explained on the page.
- route: Baidu Maps Huiyan commercial products (数据API/数据平台)
  access_status: needs-verification
  direct_url: https://huiyan.baidu.com/
  requirements: commercial engagement (政企客户 per the official brand page); pricing and product terms unread
  steps:
  - Contact Baidu Maps Huiyan for commercial data-platform/API products (人口/客流/选址).
  deliverable: commercial spatiotemporal data services (pricing unread)
  cost: paid
  last_checked: '2026-08-15'
  caveat: commercial route documented only at brand level this round

access:
  url: https://qianxi.baidu.com/
  cost: free
  license: Provider terms (unread)
  format:
  - web visualization (JS)
  api: false
  how_to_get: Browser access to the public page for manual selected-day top-20 transcription; bulk, full-city and historical delivery remain unverified.
caveats:
- The browser-visible layer is a top-20 city ranking, not a complete city panel, OD matrix or direct download. “比例” is displayed but its denominator is not documented in the observed page.
- The verified selectable date interval is 2026-01-01..2026-09-27 only; do not treat it as a durable historical archive.
- Distinct from the AMAP migration product - different provider, different index family; record separately.
- No paper use verified this round (provider-first record).

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Li, Yang, Liu & Yao (2026), Assessing spatial transmission risk of respiratory infectious diseases across cities of different socioeconomic tiers in China: A modelling study'
  doi: https://doi.org/10.1371/journal.pmed.1005172
  journal: PLOS Medicine
  year: 2026
  dataset_role: >-
    Daily city-level outbound migration-scale index and destination-share inputs used to
    build intercity mobility transition matrices for 366 mainland-China cities, 2021-01-01
    through 2022-04-05.
  evidence_type: published-paper-full-text-and-data-availability-statement
  evidence_url: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1005172
  data_note: >-
    The read Methods section says the authors extracted Baidu Qianxi's daily migration index
    for 366 cities, obtaining each city's outbound scale index and the proportion directed to
    each destination; the paper's data-availability statement links processed analytical inputs
    and Baidu Migration data in Zenodo. This establishes historical paper use and a released
    research derivative, not a current public bulk-download or a guarantee that the present
    Qianxi interface exposes the same full panel.

provenance:
- source: https://qianxi.baidu.com/ (fetched 200, HTML shell, read 2026-08-15)
  field_scope:
  - product identity (百度迁徙-百度地图慧眼)
  - description (定位可视化呈现国内人口迁徙情况)
  - JS app (values not readable)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://huiyan.baidu.com/ (fetched 200, read 2026-08-15)
  field_scope:
  - Huiyan brand identity (时空大数据服务品牌)
  - product forms (数据平台/数据API/大屏/报告) and 政企客户 positioning
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://qianxi.baidu.com/ (browser-read 2026-09-28)
  field_scope:
  - city-level national 热门迁入地 and 热门迁出地 tables display 20 ranked rows with city/province labels and a “比例” column
  - selected dates 2026-01-01 and 2026-09-27 were each rendered with distinct table values
  - the date selector visibly listed 2026-01-01 through 2026-09-27
  - page notice “获取详情数据请点击联系我们” marks the boundary between public ranking display and unverified detail delivery
  - page note says the national migration scale is overall, while city level distinguishes inflow and outflow; it does not define the “比例” denominator
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1005172 (full text and data-availability statement read 2026-09-28)
  field_scope:
  - actual Baidu Qianxi use for 366 cities from 2021-01-01 through 2022-04-05
  - outbound migration-scale index and destination-share inputs
  - paper-side processed-data and code release notice
  - boundary that a historical research release does not establish present-interface bulk access
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: baidu-qianxi-2020-spring-festival-city-od-network
  relation: often-confused-with
- id: china-amap-migration-flow-indices
  relation: substitute
- id: china-commuting-based-metropolitan-areas
  relation: often-confused-with
---

## Positioning in one sentence

Baidu Qianxi visibly supplies a selected-day national top-20 city inbound/outbound ranking, with a provider-labelled “比例” value, but it does not thereby supply a complete city panel or OD matrix; it remains distinct from Gaode's AMAP migration product.

## Select rules

- Use Baidu Qianxi only when a selected-day national top-20 city ranking is sufficient; use AMAP or another source only after comparing their separately verified public products.
- Do not merge the two index families; they come from different providers with different construction.
- For absolute counts, individual data or commuting delineations, switch to other assets.

## Get recipe

1. Open qianxi.baidu.com, choose 城市级别 and select 热门迁入地 or 热门迁出地.
2. Select an available date and transcribe the 20 visible rows with their provider labels.
3. Stop at the public ranking unless Baidu documents a separate detail-delivery route; for commercial-grade series, contact Baidu Maps Huiyan (huiyan.baidu.com).

## Connections and Limitations

The verified public layer ends at 20 ranked cities for a selected date. It neither establishes a full city universe nor gives the meaning of the displayed “比例”, a bulk export, an OD matrix or terms for a retained research panel. The boundary against china-amap-migration-flow-indices (provider, construction, platform) remains essential.

## Decision sufficiency check

A researcher can now obtain a traceable, manually transcribed selected-day top-20 ranking and knows exactly where that current public route stops. The record also documents one separate historical paper-side derivative and its release, but that evidence does not establish a current Qianxi full-panel route, export terms, or the definition of the displayed “比例”. Grounding remains appropriate because those provider-side acquisition boundaries are still unresolved.
