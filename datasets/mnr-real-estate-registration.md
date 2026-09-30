---
schema_version: 3
catalog_status: grounding
id: mnr-real-estate-registration
name: MNR Real-Estate Registration System Data (自然资源部不动产登记数据)
aka:
- 不动产登记
- 不动产统一登记
- 不动产权证书
- 不动产登记簿
- 不动产登记资料
- Real Estate Registration
- Unified Real Estate Registration
provider: "Ministry of Natural Resources of the People's Republic of China (自然资源部); policy and statistics layer under 自然资源确权登记局 (Department of Natural Resources Ownership Rights Registration); registration itself is administered by county/city-level 不动产登记机构 (real-estate registration agencies) under local governments"
china_related: true
domains:
- housing
- public
- macro
- finance
- urban
data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: "Property-level 不动产登记簿/登记资料 and their underlying registration records, administered by local registration agencies. These records are statute-restricted and are not obtainable in bulk. The separately catalogued MNR annual national bulletin statistics are a different, public aggregate product."
  availability: restricted
  ordinary_researcher_feasible: false
  summary: "The registration micro-layer (不动产登记簿 and 登记原始资料) is restricted by statute to per-property queries by rights holders and interested parties at the local registration agency where the property sits. No bulk, city-level, or machine-readable registration product was found on official MNR channels. The distinct ready bulletin product records the freely downloadable national annual certificate/proof statistics and must not be confused with this target artifact."
  barrier: "《不动产登记资料查询暂行办法》(国土资源部令第80号, 2018; amended 2019/2024/2025) limits querying to 权利人/利害关系人, requires on-site application at the 市县 real-estate registration agency where the property is located, allows only one 不动产单元 per application, and forbids use for other purposes or disclosure; no bulk or research access channel exists in the statute."
unit_of_observation: "One property-right registration unit (不动产单元), registered right (不动产权证书) or registration-proof matter (登记证明) in the restricted registry."
structure: Restricted registration records administered by local registration agencies.
geo_granularity:
- Property unit (restricted registry, local agencies)
geography: Mainland China, with records administered by local city/county registration agencies.
time_span:
  start: 2015
  end: ongoing
  last_confirmed_release: null
  coverage_note: The exact historical coverage of the restricted registry is not publicly established here. Its legal framework began with unified registration in the mid-2010s; this record does not claim a released time series.
  last_checked: "2026-08-15"
frequency:
- Event-level (restricted registry)
sample_size: Not publicly released as an obtainable research extract.
key_variables:
- Property-right registration fields and certificates in the statutory registry; public field-level schema is not established here
research_fit:
  best_for:
  - Documenting that property-level real-estate registration records are NOT obtainable in bulk, so designs must not assume such data
  - Understanding the property-level registry's local-administration and statutory-query boundary
  choose_over:
  - Choose this record to understand why property-level registration data are unavailable; use mnr-national-real-estate-registration-bulletins for the public national aggregate layer and china-land-transaction for plot-level land-transfer transactions.
  not_good_for:
  - Property-level or household-level registration records of any kind (statute-restricted; no bulk route exists)
  - City/county/province-level registration statistics or any bulk extract
  - Housing transaction prices or market activity at sub-national level (use china-land-transaction or housing-transaction records)
  - Assuming the annual bulletin numbers imply any microdata or sub-national breakdown availability
  needs_join_for:
  - A separately verified public product for any housing-market or credit-market analysis
  variation_available:
  - No public research-ready variation is supplied by this restricted registry record
  topics:
  - real estate registration
  - property rights
  - housing
  - mortgage registration
  - rural land rights
good_for:
- An honest assessment of the property-registration data access barrier
identification:
- Annual time-series variation at national level only; no credible sub-national identification from the verified public layer
linkable_keys:
- Year (public aggregate layer)
- Right type / certificate type (public aggregate layer)
access_routes:
- route: "Boundary reference: public national annual bulletin statistics"
  access_status: documentation-only
  direct_url: https://www.mnr.gov.cn/sj/tjgb/
  requirements: See mnr-national-real-estate-registration-bulletins for the public PDF route.
  steps:
  - Do not treat annual national statistics as a route to property-level registration data.
  deliverable: Documentation-only cross-reference to the distinct public aggregate product.
  cost: free
  last_checked: '2026-09-28'
  caveat: The bulletin contains national aggregates only and cannot close the access gap for this restricted registry record.
- route: "Former public-bulletin route (moved to distinct aggregate record)"
  access_status: documentation-only
  direct_url: https://www.mnr.gov.cn/sj/tjgb/
  requirements:
  - See mnr-national-real-estate-registration-bulletins for the separate public product.
  steps:
  - Do not use this route as access to the property-level register.
  deliverable: Documentation-only pointer; the annual bulletin is separately catalogued.
  cost: free
  last_checked: "2026-08-15"
  caveat: The public annual aggregate product has a separate canonical identity and must not be conflated with this restricted registry.
- route: Per-property statutory query at the local real-estate registration agency
  access_status: by-application
  direct_url: https://www.gov.cn/zhengce/2019-08/13/content_5711410.htm
  requirements:
  - Status as 权利人 or 利害关系人 (or authorized agent/lawyer)
  - Query application stating purpose, content and required results, plus identity materials
  - Application must be made at the 市/县 real-estate registration agency where the property is located
  steps:
  - Confirm the applicable current text (2018 original 国土资源部令第80号 as amended 2019/2024/2025)
  - Submit the query application with identity and interest materials at the local agency
  - Receive a per-property 查询结果证明 (immediately or within 5 working days)
  deliverable: A query-result certificate for ONE named property unit; no bulk records, no research use, no disclosure of the 登记簿 itself
  cost: by-application
  last_checked: "2026-08-15"
  caveat: This route exists for property rights verification, not for research data collection; reuse of obtained information for other purposes and disclosure are prohibited by the statute.
access:
  url: https://www.mnr.gov.cn/sj/tjgb/
  cost: free
  license: Public government publication (公报); registration records remain subject to the statute's restrictions and may not be redistributed
  format:
  - pdf
  api: false
  how_to_get: "The restricted micro layer is not obtainable in bulk. A per-property statutory query is available only at the local 市县不动产登记机构 for an eligible rights holder or interested party. The public annual bulletin route is separately documented in mnr-national-real-estate-registration-bulletins."
caveats: "The bulletin statistics are national annual totals; no city/province breakdown was found in the verified 2023/2024 bulletins or any other official channel checked. The unified-registration system is administered locally, so any 公示-type outputs (e.g., 首次登记/继承公告) would be local-level per-property notices, not an MNR product. rerc.com.cn (MNR 不动产登记中心 affiliated unit) was unreachable from this environment (DNS), so its own outputs remain unverified. Paper-use evidence is not yet recorded; no used_by entries."
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: "2026-08-15"
used_by: []
provenance:
- source: MNR portal home and column pages (mnr.gov.cn home 200; /sj/tjgb/, /sj/sjfw/, /dt/xwfb/, /gk/tzgg/, /fw/jggb/, /fw/fwzn/, gi.mnr.gov.cn all 200, fetched 2026-08-15)
  field_scope:
  - MNR site identity and real column structure
  - Existence of the 自然资源公报 column and other data/news columns
  - Absence of any separate registration-statistics product in those columns (as observed)
  added: "2026-08-15"
  confidence: high
  verified: true
- source: 2024年中国自然资源公报 PDF http://gi.mnr.gov.cn/202503/P020251209353094119242.pdf (article page http://gi.mnr.gov.cn/202503/t20250314_2881937.html)
  field_scope:
  - 2024 不动产统一登记 section content (certificate/proof counts and breakdowns, 2020-2024 chart, 专栏6 convenience programs)
  - National-level-only granularity of the verified section
  added: "2026-08-15"
  confidence: high
  verified: true
- source: 2023年中国自然资源公报 PDF http://gi.mnr.gov.cn/202402/P020240312701247258838.pdf (article page http://gi.mnr.gov.cn/202402/t20240229_2838490.html)
  field_scope:
  - 2023 不动产统一登记 section content (proof counts, 2019-2023 chart, rural registration 专栏)
  - Continuity of the annual series across 2023/2024 bulletins
  added: "2026-08-15"
  confidence: high
  verified: true
- source: 《不动产登记资料查询暂行办法》 official republication https://www.gov.cn/zhengce/2019-08/13/content_5711410.htm and 2025 amendment decree (自然资源部令第18号) in 国务院公报 2026年第4号 https://www.gov.cn/gongbao/2026/issue_12546/202602/content_7057456.html
  field_scope:
  - Statute identity (国土资源部令第80号, 2018-03-02 公布) and amendment history (2019, 2024, 2025)
  - Query-subject restrictions (第4条), location requirement (第7条), per-property limitation (第24条), purpose/disclosure prohibitions (第25-26条)
  added: "2026-08-15"
  confidence: high
  verified: true
- source: MNR 机构设置 page for 自然资源确权登记局 https://www.mnr.gov.cn/jg/jgsz/nsjg/201809/t20180912_2188293.html
  field_scope:
  - Responsible department identity and mandate (制度标准规范, 指导监督全国登记工作, 全国登记信息管理基础平台, 管理登记资料)
  added: "2026-08-15"
  confidence: high
  verified: true
- source: Press-conference/news pages (mnr.gov.cn/dt/zb/2026/lxxwfbh_5/ and lxxwfbh_6/, mnr.gov.cn/dt/ywbb/202607/t20260715_2934474.html, t20260715_2934558.html; mnr.gov.cn/sj/sjfw/, /fw/jggb/; search.mnr.gov.cn site search)
  field_scope:
  - No registration statistics in the checked May/June 2026 monthly press conferences
  - SCiO 2026-07-15 press conference and 确权登记 news provide policy narrative only (no statistics tables)
  - No registration 公示 outputs in the checked 结果公布/通知公告 columns
  added: "2026-08-15"
  confidence: med
  verified: true
related_datasets:
- id: mnr-national-real-estate-registration-bulletins
  relation: successor
- id: china-land-transaction
  relation: often-confused-with
---

## Positioning in one sentence

MNR 不动产登记 is China’s property-right registration system, but its register and source materials are statute-restricted to eligible, per-property local queries. It is not a research bulk-data route; the separate mnr-national-real-estate-registration-bulletins record covers the public national PDF statistics.

## Select rules

- Use this record to confirm that a design cannot assume bulk household- or property-level registration data.
- Use mnr-national-real-estate-registration-bulletins for the separately obtainable national annual bulletin series.
- Switch to china-land-transaction for plot-level land-transfer transactions (landchina 招拍挂 announcements) — a different system (land-supply market) and a different product family; do not merge the two.
- Not suitable for: any property-level or sub-national registration statistics (none verified in official channels), housing transaction prices, or designs that need registration identifiers (不动产单元号) outside a per-property statutory query.

## Get recipe

1. For a public national aggregate series, follow the separate mnr-national-real-estate-registration-bulletins record.
2. For a property-level query, first confirm that the requester is a 权利人 or 利害关系人 under the current legal framework, then apply at the relevant 市县 agency for one named property unit. This is a verification service, not a research-data route.

## Connections and Limitations

- Distinct from china-land-transaction: registration records property rights per 不动产单元 and are restricted; landchina records plot-level land-use-right transactions from public announcements and is collectible.
- The public national aggregate layer is separately catalogued; neither it nor this record establishes province/city/county, property or machine-readable registry data.
- 2022年中国自然资源统计公报 PDF is image-based (unreadable by standard text extraction this round) — its registration content is unknown, not absent. Older 国土资源公报 years (2001-2013) are listed in the column but unread.
- rerc.com.cn (MNR-affiliated 不动产登记中心) was DNS-unreachable from this environment; its outputs unverified.
- Paper-use evidence is not yet recorded: used_by is empty and paper_use_status needs-verification; no paper-to-product attribution is claimed here.
