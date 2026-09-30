---
schema_version: 3
catalog_status: ready
id: china-5a-scenic-area-list
name: China National 5A Scenic Area designation list (国家5A级旅游景区名单/名录)
aka:
- 国家5A级旅游景区
- 5A级旅游景区名单
- 5A景区名录
- China 5A tourist attractions
- National AAAAA scenic areas
provider: 文化和旅游部 (Ministry of Culture and Tourism), 资源开发司 (Department of Resource Development); predecessor 国家旅游局 (China National Tourism Administration) before the 2018 institutional reform; designations follow GB/T 17775 旅游景区质量等级的划分与评定 and 旅游景区质量等级管理办法, published as 公示 (publicity) + 公告 (final determination) pairs
china_related: true
domains:
- tourism
- regional
- human-capital
- policy
- urban

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The Ministry's current official 5A roster: one row per scenic area with its official
    name, province, designation year and service UUID. The public query returned 358 rows
    across 24 pages on 2026-09-28, covering designation years 2007-2024.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: "The Ministry's public 5A query page supplies the current complete roster directly, rather than merely an interface for isolated lookups. A read-only check on 2026-09-28 followed the page's own public SM4 request flow: the first page reported 358 rows and 24 pages at 15 rows per page, while the final page returned 13 rows. Returned fields are province, scenic-area name, designation year and a service UUID. This closes the current official name–province–year roster route. The separate announcement archive remains useful for documentary batch dates and cross-checks, but is not required to obtain the roster."
  barrier: The service exposes a browser-oriented, encrypted request flow rather than a documented CSV download or stable public API. It is sufficient to retrieve the current 358-row roster, but a researcher should retain the retrieval date and raw page responses because the roster can change and no historical service snapshot is promised.

unit_of_observation: Scenic area (景区) — one row per 5A-designated area, identified by its official name (province + prefecture/city + area name as printed in the announcement) and its designation batch
structure: Repeated cross-section of irregular batches (2007 first batch; batches of ~9-22 areas in later years; none in 2023)
geo_granularity:
- scenic area (with province and prefecture/city in the name)
- City/prefecture (inferable from the name prefix)
geography: "China, all provinces/regions; the 2024-02-06 announcement lists 21 areas in 21 distinct province-level units: Beijing, Hebei, Inner Mongolia, Liaoning, Jilin, Shanghai, Jiangsu, Zhejiang, Anhui, Fujian, Shandong, Henan, Hubei, Hunan, Guangxi, Hainan, Chongqing, Sichuan, Yunnan, Shaanxi, Ningxia."
time_span:
  start: '2007'
  end: ongoing
  last_confirmed_release: '2026-09-28 query check (358 current rows; designation years 2007-2024)'
  coverage_note: "The official query's unfiltered 2026-09-28 response reports 358 rows in 24 pages (page size 15), with fields for province, area name and designation year. Its first page begins with 2007 entries and its final page contains 2013-2024 entries. Official announcement anchors independently confirm the 2024-02 batch (21 areas) and 2024-12 batch (19 areas). Treat the roster as a current service snapshot, not a versioned historical release."
  last_checked: '2026-09-28'
frequency:
- irregular batches (multiple per year in some years; none in 2023)
sample_size: '358 rows in the unfiltered official service response checked 2026-09-28 (24 pages at 15 rows, final page 13 rows); recent announcement batches: 21 (2024-02-06), 19 (2024-12-27)'
key_variables:
- Official area name with province + prefecture/city prefix (e.g. 河北省衡水市衡水湖旅游景区)
- Designation year (ssYear) and service UUID; announcement dates and document numbers remain obtainable separately from the archive
- No administrative codes, no coordinates, no visitor/revenue data, no upgrade history per area beyond the 5A designation

research_fit:
  best_for:
  - Constructing scenic-area-level or city-level exposure rosters for China's 5A program 2007-2024 (which area/city, which designation year), e.g. tourism-growth exposure designs
  - Joining to household surveys or city panels by city name for tourism and human-capital research
  choose_over:
  - Choose this roster over commercial tourism databases when the research needs the official designation timing (batch year) and the complete public list
  - Choose it over china-mofcom-rural-ecommerce-demo-counties when the exposure is the national tourism rating program rather than e-commerce subsidies
  not_good_for:
  - Visitor flows, ticket revenue, or tourism intensity (the list carries no flows)
  - Non-5A A-level areas (the 4A and below rosters are published by provincial tourism departments, not this national series)
  - Point-level location analysis without external geocoding (the list prints names only)
  - The treatment-assignment/identification side of the 5A expansion: that belongs to the Econ-Variation repository
  needs_join_for:
  - Admin codes (NBS 行政区划代码) and coordinates (geocode from names)
  - Area or city characteristics and outcomes (statistical yearbooks, surveys)
  - Household-level outcomes (CFPS, census, gaokao data) for human-capital analysis
  variation_available:
  - Staggered designation across batches 2007-2024 is a data dimension of the list; the list itself is a data record — the designation mechanism and identification threats belong to Econ-Variation
  topics:
  - tourism
  - 5A scenic areas
  - scenic area rating
  - tourism and education
  - regional policy
  - local development

good_for:
- 5A designation timing roster (area-year) for tourism-exposure research
- City-level tourism-policy coverage variables
identification:
- This record supplies an administrative designation roster, not a treatment-assignment or causal design; any causal use requires separate evidence on assignment, comparison and timing.
linkable_keys:
- Area name (Chinese, as printed)
- Province + prefecture/city (in the name)
- Designation year (batch)

joins:
- target: cfps
  relation: complement
  keys:
  - City or county name
  - Survey year
  method: Normalize city/county names to the survey geography; verify codes; the roster itself carries no codes
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - County/city code or name
  - Census year
  method: Match on normalized names/codes for local controls; beware boundary changes across census vintages
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - City name
  - Year
  method: Join city-level outcomes by normalized name/code
  evidence_status: plausible

access_routes:
- route: 文旅部 政务公开 (zwgk.mct.gov.cn) 公告 archive
  access_status: available
  direct_url: https://zwgk.mct.gov.cn/zfxxgkml/zykf/202402/t20240206_951222.html
  requirements:
  - Public web access; no account
  steps:
  - Open the 公告 pages in the 资源开发 (zykf) column of zwgk.mct.gov.cn; example verified: 关于确定21家旅游景区为国家5A级旅游景区的公告 (2024-02-06, 索引号 357A10-15-2024-0115)
  - Extract the numbered area names (with province+city prefixes) and the announcement date for each batch
  - Reconstruct the full roster across batches 2007-2024
  deliverable: Official HTML lists of newly designated 5A areas per batch
  cost: free
  last_checked: '2026-08-14'
  caveat: The 2024-12 公告 (19 areas, 文旅资源发〔2024〕100号) was verified via the 安宁市政府 republication (kman.gov.cn, 2025-01-06) — its zwgk.mct.gov.cn origin page was not located this pass; older batches (2007-2023) not individually verified
- route: 文旅部 政务服务门户 '我要查询' → 5A级旅游景区
  access_status: available
  direct_url: https://zwfw.mct.gov.cn/wycx/5ajlyjq/
  requirements:
  - Public web access; no account
  steps:
  - Open the query page; it requests a temporary public SM4 key from /portal/getsm4key and loads /images/sm4.js as part of its own browser flow.
  - Submit the page's empty name/province/year filters to /portal/scenicspot, beginning with pageNum=1 and pageSize=15; follow pagination through the reported final page.
  - Decrypt the returned page payload with the page-supplied key and script, then retain the retrieval timestamp, reported total and page responses as the dated source snapshot.
  - For a manual route, use the rendered filters and pagination in an ordinary browser; no custom endpoint or credential is required.
  deliverable: Complete current official roster with province, scenic-area name, designation year and UUID (358 rows / 24 pages checked 2026-09-28)
  cost: free
  last_checked: '2026-09-28'
  caveat: This is the page's browser-oriented service flow, not a documented bulk-download API. The 358-row total is a dated snapshot; save results before building a fixed historical panel and check site terms before automated collection.
- route: 中国政府网 republications of 文旅部 公示/公告
  access_status: available
  direct_url: https://www.gov.cn/lianbo/bumen/202401/content_6928758.htm
  requirements:
  - Public web access; no account
  steps:
  - Open the gov.cn republication of the 文旅部 公示 (example verified: 拟确定21家旅游景区为国家5A级旅游景区的公示, 2024-01-25, 公示期至 2024-02-01)
  - Use as an official cross-check of batch content and dates
  deliverable: Official republication of the 公示 text with the full area list
  cost: free
  last_checked: '2026-08-14'
  caveat: Republications are copies of the 文旅部 text; the origin is zwgk.mct.gov.cn
- route: Provincial government republications (e.g. 黑龙江文旅厅, 安宁市政府) for individual batches
  access_status: available
  direct_url: https://wlt.hlj.gov.cn/wlt/c114167/202412/c00_31793036.shtml
  requirements:
  - Public web access; no account
  steps:
  - Open the provincial republication of the 文旅部 公示/公告 (example verified: 拟确定19家旅游景区为国家5A级旅游景区的公示, 2024-12-13; and the 公告 text with 文号 文旅资源发〔2024〕100号 on kman.gov.cn)
  - Extract the area list
  deliverable: Official text of the batch announcement
  cost: free
  last_checked: '2026-08-14'
  caveat: Use as official copies when the zwgk origin page is not located; treat name spellings as the government's official text

access:
  url: https://zwfw.mct.gov.cn/wycx/5ajlyjq/
  cost: free
  license: Public government announcements; no redistribution restriction observed beyond citing the source
  format:
  - encrypted JSON page payload (decoded by the query page's public script)
  - html
  api: false
  how_to_get: Use the public 5A query page and follow all reported pages to retrieve the current complete name–province–designation-year roster; keep a dated snapshot. Use 公示/公告 pages for batch-document verification. Geocoding and admin-code matching remain researcher work.
caveats:
- The announcements print names only: no admin codes, no coordinates, no visitor/revenue data.
- The query service supplies a current, paginated name–province–year roster, but not a static historical download, direct CSV export, coordinates, or announcement-level dates. Preserve a dated retrieval snapshot.
- The roster's individual years are provider fields. If a study requires an exact announcement date, an intermediate historical vintage, or the designation-document number, verify it against the relevant 公示/公告 rather than inferring it from the current roster.
- The roster is data; the 5A designation mechanism and identification threats belong to Econ-Variation.

production:
  raw_sources:
  - name: 文旅部 关于确定21家旅游景区为国家5A级旅游景区的公告 (zwgk.mct.gov.cn origin)
    source_type: webpage
    role: Official 2024-02-06 batch (21 areas), full text with numbered list
    access_route: Fetched and read 2026-08-14
    url: https://zwgk.mct.gov.cn/zfxxgkml/zykf/202402/t20240206_951222.html
    coverage: 21 areas across 21 distinct province-level units, counted from the official announcement
    last_checked: '2026-09-29'
  - name: 文旅部 拟确定19家旅游景区为国家5A级旅游景区的公示 (2024-12-13) — 黑龙江文旅厅 republication
    source_type: webpage
    role: Official 2024-12 公示 (19 areas), full text with numbered list
    access_route: Fetched and read 2026-08-14
    url: https://wlt.hlj.gov.cn/wlt/c114167/202412/c00_31793036.shtml
    coverage: 19 areas; 公示期 2024-12-13..2024-12-19
    last_checked: '2026-08-14'
  - name: 文旅部 关于确定19家旅游景区为国家5A级旅游景区的公告 (文旅资源发〔2024〕100号, 2024-12-27) — 安宁市政府 republication
    source_type: webpage
    role: Official 2024-12-27 公告 (19 areas), 文号 and issuing unit (资源开发司)
    access_route: Fetched and read 2026-08-14
    url: http://www.kman.gov.cn/c/2025-01-06/6955078.shtml
    coverage: 19 areas; 发布日期 2024-12-27
    last_checked: '2026-08-14'
  - name: 中国政府网 republication of 文旅部 拟确定21家...公示 (2024-01-25)
    source_type: webpage
    role: Official 2024-01 公示 (21 areas), full text
    access_route: Fetched and read 2026-08-14
    url: https://www.gov.cn/lianbo/bumen/202401/content_6928758.htm
    coverage: 21 areas; 公示期 2024-01-25..2024-02-01
    last_checked: '2026-08-14'
  - name: 人民日报官方微博 full-list item (via chinadaily.com.cn repost, 2025-05-19)
    source_type: webpage
    role: Official-media anchor for the current total (358家)
    access_route: Fetched and read 2026-08-14
    url: http://ex.chinadaily.com.cn/exchange/partners/82/rss/channel/cn/columns/80x78w/stories/WS682ac531a310205377033bd9.html
    coverage: 358 areas as of 2025-05-19
    last_checked: '2026-08-14'
  - name: 2007 first-batch coverage (CCTV/中新网 2007-05-22) and 2022 counts (media lists 306/318)
    source_type: webpage
    role: Media-level anchors for the 2007 first batch (66 areas) and the 2022 count sequence
    access_route: Search-index verified 2026-08-14 (pages not fetched)
    url: http://news.cctv.com/china/20070522/103666.shtml
    coverage: First batch 66 areas (2007-05-22); 306 (2022-07-11), 318 (2022-07-15)
    last_checked: '2026-08-14'
  acquisition_methods:
  - page fetch
  - manual coding
  - document parsing
  sample_construction: "No sampling: the roster includes every area printed in each official batch announcement; rows are (area name, batch year)."
  pipeline_stages:
  - stage: collect
    inputs:
    - zwgk.mct.gov.cn 公告 archive
    - Official republications
    method: Fetch each batch 公示/公告 page; verify issuing unit and date before parsing
    tools:
    - HTTPS fetch
    - text extraction
    output: One HTML/text file per batch with the numbered area list
    evidence: Batch pages listed in raw_sources (verified 2026-08-14)
  - stage: parse
    inputs:
    - Batch HTML files
    method: Extract the numbered area names (province + city + area) and announcement dates; reconcile with printed totals
    tools:
    - HTML parsing
    - manual review
    output: Structured (area name, batch year) rows
    evidence: Official lists; 21 and 19 counts reconciled with printed lists
  - stage: clean
    inputs:
    - Structured rows
    method: Normalize name variants, dedupe (a single area is designated once), flag name changes after designation (景区更名)
    tools:
    - Manual coding
    output: Cleaned area-batch records
    evidence: Name normalization is researcher work; the announcements print official names
  - stage: match
    inputs:
    - Cleaned area-batch records
    - NBS admin codes / gazetteer or geocoding source
    method: Assign admin codes/coordinates from area names (city prefix gives prefecture; geocoding for point locations)
    tools:
    - Manual coding
    - Geocoding service
    output: Area-batch roster with codes/coordinates
    evidence: Coding/geocoding step is researcher work; the official lists carry no codes
  constructed_variables:
  - name: 5A designation indicator / exposure timing
    concept: Whether and when a scenic area (or its city) received 5A designation
    source_fields:
    - Batch year
    - Area name
    method: Indicator = 1 for each area in the batch announcement; city-level exposure aggregates areas to cities by name prefix
    validation: Compare totals with official anchors (358 as of 2025-05-19; batch counts)
    limitations: Batch year (announcement date) is the timing; no per-area preparation/upgrade history; city aggregation depends on name parsing
  output:
    unit_of_observation: Scenic area (and city, after aggregation)
    structure: Repeated cross-section of batches 2007-2024
    geography: China
    time_span: 2007-2024 (ongoing)
    key_variables:
    - Area name (Chinese)
    - Province / prefecture (from name)
    - Designation batch year
    - Admin code / coordinates (researcher-matched)
    formats:
    - csv
  reproducibility:
    level: medium
    starting_point: 文旅部 public 5A query page; retrieve all 24 reported pages and retain a dated snapshot
    code_available: false
    code_url: ''
    requirements:
    - Public web access
    - Following the page's public encrypted request flow or its rendered pagination
    - Geocoding/admin-code resources for the location step
    blockers:
    - No stable CSV download or provider-maintained historical snapshots
    - Exact announcement dates and document numbers require a separate archive check
  compliance:
    terms_or_license: Public government announcements; no observed redistribution restriction
    robots_or_rate_limits: Normal page access; no bulk scraping observed as needed
    personal_or_sensitive_data: None
    redistribution: Cite the 文旅部 source when republishing extracted lists
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-08-14'

used_by:
- cite: 'Author (2025), Tourism growth, education decline: Evidence from China''s 5A attraction expansion, JUE 150'
  doi: https://doi.org/10.1016/j.jue.2025.103811
  journal: JUE
  year: 2025
  dataset_role: Exposure source — establishment/timing of 5A attractions driving tourism growth exposure
  evidence_type: abstract-only
  evidence_url: https://ideas.repec.org/a/eee/juecon/v150y2025ics0094119025000762.html
  data_note: >-
    IDEAS abstract (cached 2026-08-14) confirms the paper studies exposure to tourism growth driven by
    establishment of China's top-tier (5A) tourist attractions and effects on high school enrollment
    (mechanisms — opportunity cost, parental expectations, academic performance). The roster itself is
    inferable from the title/abstract but not verified from the paper; the outcome survey is unnamed in
    the abstract; ScienceDirect full text is blocked in this environment. The exact designation-year
    construction and any released exposure file remain unverified.

provenance:
- source: https://zwgk.mct.gov.cn/zfxxgkml/zykf/202402/t20240206_951222.html (official announcement re-read 2026-09-29)
  field_scope:
  - Counted the 21 listed areas and their 21 distinct province-level prefixes; corrected the earlier 18-province statement in geography and raw-source coverage.
  - This batch-level correction does not reverify the current 358-row query snapshot or historical batches.
  added: '2026-09-29'
  confidence: high
  verified: true
- source: zwgk.mct.gov.cn/zfxxgkml/zykf/202402/t20240206_951222.html (fetched and read 2026-08-14)
  field_scope:
  - 2024-02-06 公告 (21 areas)
  - announcement metadata (索引号, 发布机构 资源开发司)
  added: '2026-08-14'
  confidence: high
  verified: true
- source: wlt.hlj.gov.cn republication of the 2024-12-13 公示 (fetched and read 2026-08-14)
  field_scope:
  - 2024-12 公示 (19 areas)
  - 公示期 dates
  added: '2026-08-14'
  confidence: high
  verified: true
- source: kman.gov.cn republication of the 2024-12-27 公告 (fetched and read 2026-08-14)
  field_scope:
  - 2024-12-27 公告 (19 areas)
  - 文号 文旅资源发〔2024〕100号
  added: '2026-08-14'
  confidence: high
  verified: true
- source: gov.cn republication of the 2024-01-25 公示 (fetched and read 2026-08-14)
  field_scope:
  - 2024-01 公示 (21 areas)
  - 公示期 dates
  added: '2026-08-14'
  confidence: high
  verified: true
- source: 人民日报微博 via chinadaily repost (fetched and read 2026-08-14)
  field_scope:
  - current total 358 (2025-05-19)
  added: '2026-08-14'
  confidence: med
  verified: true
- source: 2007 first batch and 2022 counts (CCTV/中新网 2007-05-22; voc/gz-cmc 2022-07 lists) — search-index level only
  field_scope:
  - 2007 first batch (66)
  - 2022 counts (306, 318)
  added: '2026-08-14'
  confidence: low
  verified: false
- source: IDEAS abstract for 10.1016/j.jue.2025.103811 (cached 2026-08-14)
  field_scope:
  - paper identity
  - abstract-level 5A exposure use
  added: '2026-08-14'
  confidence: med
  verified: true
- source: 文旅部政务服务门户 5A级旅游景区 query page (checked 2026-09-28)
  field_scope:
  - official complete roster identity and public name, region, and designation-year filters
  - page-supported request flow: temporary public SM4 key, encrypted pagination request, and browser-side decoding
  - unfiltered response pagination (358 total rows, 24 pages at size 15; final page 13 rows)
  - returned roster fields (province, scenic-area name, designation year, UUID) and 2007-2024 designation-year coverage
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-mofcom-rural-ecommerce-demo-counties
  relation: often-confused-with
- id: cfps
  relation: complement
- id: china-census
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is the official, public current roster of China's national 5A scenic-area designations: the Ministry's query service returned 358 scenic areas across 24 pages on 2026-09-28, each with a province, name and designation year (2007-2024). It is the direct starting point for a scenic-area or city designation-timing roster, while announcement pages remain the right source for exact batch dates and documents. It contains neither codes, coordinates nor tourism flows.

## Select rules

- Prioritize it when the research needs the 5A program's designation timing (which area/city, which year) for tourism-exposure designs.
- Switch to provincial tourism-department lists for non-5A (4A and below) rosters; switch to commercial tourism databases only when flow/revenue data are the object.
- Do not use this record for the designation mechanism or identification design: that is Econ-Variation territory.

## Get recipe

1. Open the Ministry's 5A query page (zwfw.mct.gov.cn/wycx/5ajlyjq/) and retrieve every reported page using its ordinary browser pagination; at the check date there were 24 pages and 358 rows.
2. Preserve the date, total, pages and returned province/name/year/UUID fields as the current roster snapshot. A scripted retrieval can follow the page's public `/portal/getsm4key` and `/portal/scenicspot` flow; it is not necessary to invent a different endpoint.
3. For an exact designation announcement date or document number, cross-check the relevant row against the 资源开发 公告 archive rather than treating a year field as an exact date.
4. Match names to admin codes/coordinates externally; record the vintage and any renamed areas.

## Connections and Limitations

The join unit is the scenic area or its city, keyed by normalized Chinese names; the official roster carries no codes or coordinates, so every join to surveys, censuses or yearbooks requires an external geocoding/admin-code step. The Ministry service is a confirmed current complete-roster route, but not a static historical download: preserve a snapshot, and use announcements when exact batch dates matter. The triggering paper's particular exposure construction and outcome-survey evidence remain abstract-level.
