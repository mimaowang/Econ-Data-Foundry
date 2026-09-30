---
schema_version: 3
catalog_status: ready
id: china-sister-city-ties
name: China international sister/friendship city ties (中国国际友好城市/省州关系名录, CPAFFC)
aka:
- 友好城市
- Sister city ties
- 国际友好城市关系
- CPAFFC friendship cities
provider: >-
  Chinese People's Association for Friendship with Foreign Countries (中国人民对外友好协会,
  CPAFFC). Official query tool '友城查询' at cpaffc.org.cn, covering all China-foreign
  sister province/state and city ties since 1973.
china_related: true
domains:
- urban
- international
- trade
- political-economy

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Pair-level list of China-foreign sister city (and province/state) ties: each row is one
    结好 pair with Chinese province + city, foreign city + country, signing date and year,
    plus tags (region, membership tags such as neighboring/ASEAN/EU) and an event log
    (dashiji). Extractable in bulk from the CPAFFC query tool's JSON endpoint (rechecked
    2026-09-28: full list of 3,187 pairs, years 1973-2026).
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Ready as a bounded raw registry (2026-09-28): provider identity, coverage and a working
    public bulk-extraction route are verified from the official CPAFFC pages. The page's
    summary states: as of July 2026, 31
    provinces/autonomous regions/municipalities (excl. Taiwan and HK/Macau SARs) and 556
    cities have 3,181 sister ties with 619 foreign states/provinces and 1,920 foreign cities
    in 153 countries (first pair 1973). A later direct endpoint check on 2026-09-28 returned
    3,187 rows, from 1973-06-24 through 2026-07-07, so the rendered summary and live data
    are different dated snapshots rather than a fixed historical total. A POST to
    /index/friend_city/ajax with empty filters returns JSON fields including prov, city,
    w_city, w_country, qzsj signing date, jhsj year and sn, plus region/membership tags and
    dashiji events. Paper use is
    abstract-level (CWE 12521: country-level aggregation 2003-2016 for OFDI spatial
    econometrics). This status covers the official pair-level registry and its documented
    public JSON route, not the paper's unreleased country-level aggregation.
  barrier: >-
    The query tool is web-based; bulk extraction uses its undocumented JSON endpoint
    (observed this round, no auth). Public article front matter identifies CPAFFC as
    the source for its reported China sister-city count, but the paper's country-level
    aggregation (which pairs, de-duplication, period 2003-2016) remains unread.

unit_of_observation: 'Sister/friendship tie (one row per 结好 pair: Chinese city/province x foreign city/state)'
structure: pair-level list (with signing year; 3,187 rows in the 2026-09-28 live query)
geo_granularity:
- Chinese city (and province/region)
- foreign city
- foreign country
- foreign state/province (province-level ties)
geography: >-
  China (31 province-level units + 556 cities) x 153 foreign countries (619 foreign
  states/provinces + 1,920 foreign cities) per the CPAFFC summary as of 2026-07.
time_span:
  start: '1973'
  end: '2026'
  last_confirmed_release: '2026-09-28 live query (latest signing date in returned rows: 2026-07-07)'
  coverage_note: >-
    First tie 1973 (Tianjin-Kobe). The official rendered summary reports 3,181 pairs as
    of July 2026; the live empty-filter endpoint returned 3,187 rows on 2026-09-28, with
    signing dates through 2026-07-07. The CWE 2024 paper uses a 2003-2016 country-level
    aggregation (abstract).
  last_checked: '2026-09-28'
frequency:
- ongoing (ties added continuously)
sample_size: >-
  3,187 rows in the official empty-filter JSON query on 2026-09-28; the rendered CPAFFC
  summary reports 3,181 pairs as of 2026-07. Treat either as a dated live-registry snapshot.
key_variables:
- Chinese province (prov) and city (city)
- Foreign city (w_city) and country (w_country)
- Signing date (qzsj) and year (jhsj)
- Serial number (sn)
- Region/membership tags (e.g., dili/fagai regions; linguo neighboring, dongmeng ASEAN, oumeng EU etc.)
- Event log (dashiji) for many pairs

research_fit:
  best_for:
  - City/country-pair analyses using the full national sister-city network (e.g., OFDI
    location, international linkages, cultural diplomacy)
  - Building a researcher-defined country-level bilateral tie count by year from the pair-level registry; this supports a transparent new aggregation, not a claim to reproduce CWE 12521's unreleased rule
  choose_over:
  - Choose this official list over ad-hoc city-level compilations (e.g., 重庆/云南外办 lists)
    when national coverage and consistent fields are needed; the CPAFFC tool is the single
    national registry.
  not_good_for:
  - Claiming the paper's exact country-level aggregation without reading its data section.
  - Underlying 'why' of tie formation (the list has event logs but no causal structure).
  needs_join_for:
  - OFDI or trade outcomes (e.g., China Global Investment Tracker family, customs)
  - City-level covariates (china-stat-yearbook family)
  variation_available:
  - Pair and timing variation of tie formation since 1973
  topics:
  - sister cities
  - international relations
  - OFDI
  - city networks

good_for:
- sister-city network construction
- international-tie exposure measures
identification:
- Event-study timing of tie signing (design-dependent)
linkable_keys:
- Chinese city name (normalization to city codes needed for joins)
- Foreign city/country names

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Chinese city
  method: normalize Chinese city names to standard city codes; not verified this round
  evidence_status: plausible

access_routes:
- route: CPAFFC official query tool (web)
  access_status: available
  direct_url: https://www.cpaffc.org.cn/index/friend_city/index/lang/1.html
  requirements: none (public)
  steps:
  - Open the 友城查询 page
  - Use the filters (year, province, Chinese city, foreign city) or the bulk endpoint below
  deliverable: Pair-level query results (prov, city, w_city, w_country, qzsj, sn)
  cost: free
  last_checked: '2026-08-15'
  caveat: Web UI is filter-based; the bulk route below was observed this round but is undocumented.
- route: CPAFFC bulk JSON endpoint
  access_status: available
  direct_url: https://www.cpaffc.org.cn/index/friend_city/ajax
  requirements: POST with filter parameters (empty filter returns the full list; is_ajax=1)
  steps:
  - POST filter[prov]/filter[city]/filter[w_city]/filter[w_country]/filter[qzsj]/filter[qzsj_end] (empty) with is_ajax=1
  - Parse the JSON response data.lists (3,187 rows on 2026-09-28; live registry changes over time)
  deliverable: Full pair list with fields incl. dashiji event logs and membership tags
  cost: free
  last_checked: '2026-09-28'
  caveat: Undocumented endpoint; check the site's terms before bulk use (terms not reviewed this round).
- route: paper-full-text (paper-use verification)
  access_status: needs-verification
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/cwe.12521
  requirements: Subscription or library access (Wiley; automated clients 403)
  steps:
  - Read the CWE 2024 data section for the country-level aggregation recipe (2003-2016)
  deliverable: Paper data-section detail; no data file
  cost: paid
  last_checked: '2026-08-15'
  caveat: Not read this round (Wiley blocked); paper use currently abstract-level.

access:
  url: https://www.cpaffc.org.cn/index/friend_city/index/lang/1.html
  cost: free
  license: public official data (site terms not reviewed this round)
  format:
  - json (bulk endpoint)
  - html (query tool)
  api: true
  how_to_get: Query the CPAFFC tool online, or POST to the ajax endpoint for the full list.
caveats: >-
  Coverage note: '556 cities' in the rendered July 2026 summary includes county-level and district-level units in some cases
  (e.g., 泰安市肥城市, 盐城市大丰区 appear in the city lists) - normalize before city-level
  joins. The list updates continuously; the 3,187 row count is a 2026-09-28 snapshot.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: abstract-only
  last_audited: '2026-09-28'

used_by:
- cite: 'Huang, Dong & Zhao (2024), Sister-city Ties and Chinese Outward Foreign Direct Investment: A Spatial Econometric Analysis'
  doi: https://doi.org/10.1111/cwe.12521
  journal: China & World Economy
  year: 2024
  dataset_role: Country-level sister-city tie dataset 2003-2016 linked to OFDI; spatial econometrics
  evidence_type: abstract-only
  evidence_url: https://api.crossref.org/works/10.1111/cwe.12521
  data_note: >-
    The public Wiley article page gives the abstract's linked country-level
    2003-2016 sister-city/OFDI dataset and the accessible introductory page
    footnote attributes its reported China sister-city count to CPAFFC
    (read 2026-09-28). The publication's data section remains inaccessible,
    so this does not establish the exact city-pair-to-country aggregation,
    deduplication or country-year rule used in the analysis.

provenance:
- source: https://www.cpaffc.org.cn/index/friend_city/index/lang/1.html
  field_scope:
  - CPAFFC official query tool existence and filters (year, province, Chinese city, foreign city)
  - summary numbers as of 2026-07 (31 provinces + 556 cities; 153 countries; 619 foreign states; 1,920 foreign cities; 3,181 pairs; first tie 1973)
  - AJAX endpoint structure (POST /index/friend_city/ajax, filter fields, response fields incl. prov/city/w_city/w_country/qzsj/sn)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.cpaffc.org.cn/index/friend_city/ajax (tested POST)
  field_scope:
  - full JSON extraction without filters: 3,181 rows; fields verified on sample and last rows; year range 1973-2026; 153 countries; top countries (US 288, Japan 268, Korea 232, Russia 179...)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.cpaffc.org.cn/index/friend_city/ajax (empty-filter POST rechecked 2026-09-28)
  field_scope:
  - live response status (HTTP 200) and full-list row count (3,187)
  - row fields (id, sn, prov, city, w_city, w_country, qzsj, jhsj and tags)
  - returned signing-date range (1973-06-24 through 2026-07-07)
  - difference between live-row count and the rendered July 2026 summary count
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://api.crossref.org/works/10.1111/cwe.12521
  field_scope:
  - paper identity and abstract (country-level 2003-2016, OFDI spatial econometrics)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://onlinelibrary.wiley.com/doi/10.1111/cwe.12521 (public article front matter, read 2026-09-28)
  field_scope:
  - paper's explicit CPAFFC attribution for its reported sister-city count
  - boundary: accessible public page does not expose the data section or aggregation recipe
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-amap-migration-flow-indices
  relation: often-confused-with
---

## Positioning in one sentence

中国人民对外友好协会官网"友城查询"是全国国际友好城市（省州）关系的单一官方名录：其页面摘要给出 2026-07 的 3,181 对，而 2026-09-28 直接查询返回 3,187 对（最晚签字日 2026-07-07）。每行一对结好关系并带签字日期、年份与大事记；页面 JSON 接口可无鉴权取全量，因此这一对级原始名录本身可直接使用。论文中的国家层聚合则仍是另一项未公开的构造。

## Select rules

- 需要全国覆盖的友城对级数据时选 CPAFFC 名录，而不是单省外办清单（如重庆/云南外办一览表）。
- 城市级加入口：中方城市名需规范化（名录含县级市/区，如"泰安市肥城市"）。
- 论文（CWE 12521）公开前段明确把 CPAFFC 名录作为友城对数量来源，但其国家层 2003-2016 聚合仍是论文特定构造；未读数据章节前不要声称可精确复现。

## Get recipe

1. 打开 cpaffc.org.cn/index/friend_city/index/lang/1.html（友城查询）。
2. 批量：POST /index/friend_city/ajax（filter 参数留空、is_ajax=1），解析 JSON data.lists——2026-09-28 实测返回 3,187 行；把行数和日期记录为自己的下载快照。
3. 按需过滤（结好年份、省份、中方城市、外方城市/国家）。
4. 做中方城市名称规范化与城市代码匹配后用于城市层/国家层分析。

## Connections and Limitations

- 连接：按中方城市名与城市统计年鉴/OFDI 数据连接（需名称规范化）；国家层聚合需自行去重与周期定义。
- 限制：名录持续更新（数量为快照值）；城市清单包含县级单位；网站条款未审查（批量使用前应核对）。
- 未验证：论文的聚合方法与确切配对集合（Wiley 403）。
