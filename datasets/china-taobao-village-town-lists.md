---
schema_version: 3
catalog_status: ready
id: china-taobao-village-town-lists
name: Taobao Village and Taobao Town lists (淘宝村淘宝镇名单; AliResearch platform-identified e-commerce villages/towns, official series 2009-2022; CnOpenData structured module 2017-2022 excl 2018)
aka:
- 淘宝村淘宝镇名单数据
- Taobao village list
- Taobao town list
- 淘宝村名单信息表
- 淘宝镇名单信息表
- AliResearch Taobao village/town list series
provider: >-
  Official series: 阿里研究院 (AliResearch, Alibaba Group) compiles and publishes
  annual Taobao village/town lists with published selection criteria (village:
  rural administrative village, >=10M RMB annual Alibaba-platform sales, >=100
  active shops or >=10% of households; town: >=3 Taobao villages or >=30M RMB
  annual sales + >=300 active shops). Structured delivery module: CnOpenData
  (浙江天池科技有限公司 platform) resells a structured 淘宝村淘宝镇名单数据 module
  (two tables, 2017-2022 excluding 2018) on an account-based commercial route;
  the module page references NBS 《2021年统计用区划代码和城乡划分代码》 for the
  urban/rural classification.
china_related: true
domains:
- rural
- e-commerce
- platform-economy
- digital-economy
- regional
- village-economy

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Year-level rosters of Taobao villages and Taobao towns: official series is
    annual name lists (2009-2022; 3 villages in 2009, 20 in 2013, 7,780 villages
    and 2,429 towns in 2022 across 28 provinces); the CnOpenData module delivers
    two structured tables (淘宝村名单信息表 / 淘宝镇名单信息表) with fields
    省/市/区县/村/经纬度 (province, city, county, village name, lat/lon) for the
    years 2017-2022 excluding 2018, updated annually.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    A distinct, reusable asset layer for village-level platform e-commerce
    research: the official AliResearch Taobao village/town series (2009-2022)
    and its structured delivery via the CnOpenData module (2017-2022 excl
    2018). The current actionable route is the account-based CnOpenData module,
    not a claim that an official full-series download is available. The 2022
    Journal of World Economy paper independently confirms actual use of the
    official 2013-2017 AliResearch reports to construct a township-year
    Taobao-village indicator; its report-derived file is distinct from the
    vendor's later, limited-coverage delivery. Price and download terms are
    confirmed only after the vendor account/request step.
  barrier: >-
    No machine-readable official download confirmed (aliresearch.com pages are
    JS-rendered shells); the structured module goes through a CnOpenData account
    with unpublished price/terms; the module omits 2018 and does not cover the
    official series' 2009-2016 years.

unit_of_observation: >-
  Taobao village (行政村-level; rural administrative village) and Taobao town
  (乡镇-level) per list year, with province/city/county names and (in the
  CnOpenData module) lat/lon
structure: Repeated cross-section of annual lists (a village/town can appear in multiple years)
geo_granularity:
- village
- township
- county (as a name field)
- province (as a name field)
geography: China; 2022 lists cover 28 provinces/自治区/直辖市 (7,780 villages, 2,429 towns)
time_span:
  start: '2009'
  end: '2022'
  last_confirmed_release: '2022'
  coverage_note: >-
    Official series runs 2009-2022 (3 villages 2009; 20 villages 2013; 2022
    counts 7,780 villages / 2,429 towns across 28 provinces - read from the
    CnOpenData module page and consistent with the 贾铖 & 易红梅 2023 review).
    The CnOpenData module covers 2017-2022 EXCLUDING 2018 (page states
    时间区间 2017-2022年（不包含2018年）); the 2018 roster is absent from the
    module and its official list page was not verified.
  last_checked: '2026-08-15'
frequency:
- annual
sample_size: '2022 official counts: 7,780 Taobao villages, 2,429 Taobao towns, 28 provinces; earlier years smaller (3 in 2009, 20 in 2013); module row counts not shown on the public page'
key_variables:
- List year
- Province (省)
- City (市)
- County/district (区县)
- Village/town name (村/镇; module table split by 淘宝村名单信息表 / 淘宝镇名单信息表)
- Latitude/longitude (经纬度, per the CnOpenData module)
- 'Selection-criteria flags implied by the official definition (sales >=10M RMB, >=100 active shops or >=10% of households; town: >=3 villages or >=30M RMB + >=300 shops) - not confirmed as released fields'
- No sales volumes, no shop counts, no firm identifiers in the module description

research_fit:
  best_for:
  - Village/town-level identification of platform e-commerce activity in China (which rural villages were recognized as Taobao villages, in which years)
  - Constructing village-level e-commerce exposure variables for rural digital-economy research (e.g. distance-to-nearest-Taobao-village, village-in-list indicators)
  - Panel-style coverage analysis of the AliResearch village/town lists 2017-2022 (module years) or 2009-2022 (official series)
  choose_over:
  - Choose these lists over china-mofcom-rural-ecommerce-demo-counties when the research needs PLATFORM-identified e-commerce villages/towns (Alibaba ecosystem) rather than the MOFCOM government demonstration-program counties - the two programs and rosters are different
  - Choose these lists over china-rural-ecommerce-couture-2021-replication when the need is a nationwide village roster for exposure construction rather than the 100-village RCT microdata
  - Choose the CnOpenData structured module over hand-collecting official announcement pages when 2017-2022 (excl 2018) coverage with lat/lon suffices and an account is acceptable
  not_good_for:
  - Village-level sales volumes, shop counts, or transaction data (the lists are rosters with selection thresholds, not measures)
  - The MOFCOM demonstration-program counties or Alibaba's Rural Taobao RCT data (distinct programs/assets; see related_datasets)
  - Years before 2017 via the CnOpenData module (official announcements remain the only route for 2009-2016)
  - The 2018 roster via the CnOpenData module (explicitly excluded from the module's time range)
  needs_join_for:
  - Administrative codes: the module references NBS 2021 statistical division codes for classification, but the public page lists name fields only - a name-to-code concordance is researcher work
  - Outcomes: household/firm surveys (cfps etc.), fiscal or consumption data by county/village for effect estimation
  - Village lat/lon (module) for distance-based designs; official announcement rosters may lack coordinates
  variation_available:
  - Year-over-year entry into the lists (village/town appears in some years, not others) is a data dimension of the rosters; treatment-assignment interpretations belong to the Econ-Variation repository
  topics:
  - taobao village
  - e-commerce villages
  - rural e-commerce
  - platform economy
  - digital economy
  - village-level exposure

good_for:
- Village/town-level platform e-commerce roster and coverage research
- Constructing e-commerce exposure measures for rural China
identification:
- >-
  A row is a listed Taobao village or Taobao town in a particular list year,
  not a village's sales or shop-count observation. The current CnOpenData
  delivery is a separate, later access product with 2017-2022 coverage except
  2018; it must not be called the 2013-2017 township-year file constructed by
  Wu, Yang and Zhou from AliResearch reports.
linkable_keys:
- Village/town name (Chinese, as printed in the list)
- Province/city/county name
- Lat/lon (module field; precision and coding unverified)

joins:
- target: china-mofcom-rural-ecommerce-demo-counties
  relation: often-confused-with
  keys:
  - County name (normalized)
  method: 'Keep the two programs separate: Alibaba/AliResearch Taobao village/town lists vs MOFCOM demonstration-county batches; both are county/village rosters but different selection authorities and purposes.'
  evidence_status: verified
- target: china-rural-ecommerce-couture-2021-replication
  relation: often-confused-with
  keys: []
  method: The Couture et al. RCT studies Alibaba's Rural Taobao terminals in 100 villages; the village/town lists are a national roster - do not merge.
  evidence_status: verified

access_routes:
- route: CnOpenData 淘宝村淘宝镇名单数据 module (structured download)
  access_status: available-with-registration
  direct_url: https://www.cnopendata.com/data/m/Platform_Eco/taobao-township.html
  requirements:
  - CnOpenData account (registration/login); price and download terms are NOT shown on the public module page
  steps:
  - Open the module page and confirm the current tables (淘宝村名单信息表 / 淘宝镇名单信息表), time range (2017-2022 excl 2018), and fields (省/市/区县/村/经纬度).
  - Register/log in on cnopendata.com and request the module (price/terms to be confirmed in the account flow or by contacting the vendor).
  - Download the two tables; verify the lat/lon field format and the NBS-code vintage referenced (2021 统计用区划代码).
  deliverable: Two structured tables (village list, town list) with 省/市/区县/村/经纬度 for 2017-2022 excluding 2018
  cost: registration
  last_checked: '2026-08-15'
  caveat: Price, license, and exact row counts are unverified (account-gated); the module omits 2018 and years before 2017.
- route: Official AliResearch annual lists and query page (raw official series)
  access_status: partial
  direct_url: http://www.aliresearch.com/cn/activity/taobaoVillageResearchList
  requirements:
  - Human browser with JavaScript: the official pages (annual 名单公示 notices and the taobaoVillageResearchList query page exposing adcode/villageCode/villageYear/item parameters) are React SPA shells to automated clients (re-verified blocked 2026-08-14)
  steps:
  - Open the AliResearch query page or the annual 淘宝村/淘宝镇名单 notice in a JS-capable browser.
  - Export or transcribe the village/town rosters by year (download/export options unverified).
  deliverable: Official annual rosters (2009-2022); exact export format unverified
  cost: free
  last_checked: '2026-08-15'
  caveat: No machine-readable official download confirmed; page contents and terms require a human browser.

access:
  url: https://www.cnopendata.com/data/m/Platform_Eco/taobao-township.html
  cost: registration
  license: CnOpenData account terms (unverified on the public page)
  format:
  - structured tables (vendor format; likely xlsx/csv - unverified)
  api: false
  how_to_get: Register on cnopendata.com and request the 淘宝村淘宝镇名单数据 module; confirm price/terms in the account flow. For the official series, browse aliresearch.com in a JS-capable browser.
caveats:
- 'The module page (fetched 2026-08-14, parsed 2026-08-15) grounds: two tables, time range 2017-2022 excluding 2018, fields 省/市/区县/村/经纬度, annual update, selection criteria (village: >=10M RMB annual sales, >=100 active shops or >=10% of households; town: >=3 villages or >=30M RMB + >=300 shops), 2022 counts 7,780/2,429 across 28 provinces, NBS 2021 division-code reference.'
- Price, license, row counts, and the lat/lon format of the module are unverified (account-gated); the official AliResearch pages remain JS shells with no machine-readable download confirmed.
- Paper use is NOT verified from any paper's data section this pass: the module page lists four related papers (崔丽丽 et al. 2014 中国农村经济; 吴一平、杨芳、周彩 2022 世界经济; 曾亿武 et al. 2020 农业经济问题; 刘俊杰 et al. 2020 中国农村经济) as a secondary literature list - leads only, not evidence of their data construction.

production:
  raw_sources:
  - name: AliResearch annual Taobao village/town lists (official series)
    source_type: webpage
    role: Underlying official roster series 2009-2022 with published selection criteria
    access_route: aliresearch.com pages (JS shells; human browser); no machine-readable download confirmed
    url: http://www.aliresearch.com/cn/activity/taobaoVillageResearchList
    coverage: 2009-2022; 2022 counts 7,780 villages / 2,429 towns / 28 provinces
    last_checked: '2026-08-15'
  - name: CnOpenData 淘宝村淘宝镇名单数据 module
    source_type: dataset
    role: Structured vendor delivery of the lists (2017-2022 excl 2018; 省/市/区县/村/经纬度)
    access_route: Account-based module on cnopendata.com; price/terms unverified
    url: https://www.cnopendata.com/data/m/Platform_Eco/taobao-township.html
    coverage: 2017-2022 excluding 2018
    last_checked: '2026-08-15'
  acquisition_methods:
  - account-based download (CnOpenData module)
  - page transcription (official series; human browser)
  sample_construction: >-
    No sampling on the researcher side: the module claims the full official
    rosters for its covered years; the official series itself applies the
    AliResearch selection criteria (sales/shop thresholds above). Module-side
    coverage gaps (2018, pre-2017) are the vendor's stated time range.
  pipeline_stages:
  - stage: collect
    inputs:
    - CnOpenData module tables or official announcement pages
    method: Download the module tables (account) or transcribe official annual lists from aliresearch.com in a browser.
    tools:
    - Human browser
    - CnOpenData account
    output: Year-level village/town rosters
    evidence: Module page (fetched 2026-08-14); official pages JS-shell status (prior passes)
  - stage: clean
    inputs:
    - Year-level rosters
    method: Normalize Chinese name variants across years; the module references NBS 2021 division codes for urban/rural classification - a name-to-code concordance is researcher work.
    tools: []
    parameters: {}
    output: Cleaned village-year / town-year panel
    evidence: Module page field list; coding step is researcher work
  constructed_variables: []
  validation:
  - Cross-check module counts against official 2022 totals (7,780 / 2,429) when the download is available
  output:
    unit_of_observation: Village-year and town-year rows
    structure: Repeated cross-section by year
    geography: China (28 provinces in 2022)
    time_span: 2017-2022 excl 2018 (module); 2009-2022 (official series)
    key_variables:
    - 省/市/区县/村/经纬度
    - list year
    formats:
    - vendor tables (unverified format)
  reproducibility:
    level: medium
    starting_point: CnOpenData module page (structured route) or aliresearch.com (official route)
    code_available: false
    code_url: ''
    requirements:
    - CnOpenData account (price unverified) or a JS-capable browser for the official pages
    - Name normalization and code-matching work
    blockers:
    - No machine-readable official download confirmed
    - Module price/terms unverified; 2018 and pre-2017 years absent from the module
  compliance:
    terms_or_license: CnOpenData account terms (unverified on the public page)
    robots_or_rate_limits: Official aliresearch.com pages are JS-rendered; bulk scraping terms unverified
    personal_or_sensitive_data: Village/town names and coordinates only; no individuals
    redistribution: Unverified; follow the vendor terms
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 贾铖 & 易红梅 (2023) 电子商务进农村综合示范政策研究综述, 农业大数据学报 5(4):95-102
  doi: ''
  journal: 农业大数据学报
  year: 2023
  dataset_role: Series-scope evidence for the Taobao village/town list series (2009-2022, selection criteria, 2022 counts)
  evidence_type: data-review
  evidence_url: https://nyxsj.cbpt.cnki.net/
  data_note: >-
    The review (fetched 2026-08-14 in an earlier pass) documents the Taobao
    village/town list series 2009-2022; its statements were re-checked against
    the CnOpenData module page (fetched 2026-08-14, parsed 2026-08-15) which
    prints the same criteria and counts. This is series-level evidence, not a
    paper's data-section verification.
- cite: '吴一平、杨芳、周彩 (2022) 电子商务与财政能力: 来自中国淘宝村的证据, 世界经济 第3期'
  doi: ''
  journal: 世界经济
  year: 2022
  dataset_role: Main source for the township-year indicator of whether a township contains a Taobao village
  evidence_type: paper-data-section
  evidence_url: https://sjjj.magtech.com.cn/CN/PDF/769
  data_note: >-
    Full paper read from the journal's official PDF on 2026-09-28. Its data
    section says the authors construct a 2013-2017 panel of 20,793 townships;
    Taobao-village data come from AliResearch's published 淘宝村报告, giving
    spatial distribution and counts, and are matched to township-year fiscal
    data to create the town-year whether-a-Taobao-village indicator. The paper
    notes that its 2013 value primarily uses the end-2013 微报告 2.0 because
    微报告 1.0 was not a full-year survey. This proves official-report use, not
    delivery of the authors' merged analysis file or equivalence to the
    CnOpenData module.

provenance:
- source: CnOpenData module page https://www.cnopendata.com/data/m/Platform_Eco/taobao-township.html (fetched 2026-08-14, parsed 2026-08-15; cached .grounding-b17-20260815/cache/cnopendata_taobao.html)
  field_scope:
  - module tables and time range (2017-2022 excl 2018)
  - fields (省/市/区县/村/经纬度)
  - selection criteria and 2022 counts
  - NBS 2021 division-code reference and annual update
  - related-literature list (leads only)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: 贾铖 & 易红梅 (2023) review (fetched 2026-08-14, earlier pass)
  field_scope:
  - series-level scope 2009-2022 and criteria consistency
  added: '2026-08-15'
  confidence: med
  verified: false
- source: aliresearch.com official pages (2022 draft-list notice, 2020 report/list, taobaoVillageResearchList query page)
  field_scope:
  - official series existence; JS-shell status (blocked for automated clients; no machine-readable download confirmed)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://sjjj.magtech.com.cn/CN/PDF/769
  field_scope:
  - 2022 Journal of World Economy paper's actual use of AliResearch 淘宝村报告
  - paper construction of a 2013-2017, 20,793-township panel
  - township-year Taobao-village indicator and the 2013 微报告 2.0 boundary
  - distinction between the report-derived paper file and the CnOpenData delivery
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-mofcom-rural-ecommerce-demo-counties
  relation: often-confused-with
- id: china-rural-ecommerce-couture-2021-replication
  relation: often-confused-with
---

## Positioning in one sentence

The Taobao village/town lists are the platform-identified e-commerce roster layer for rural China. A researcher who can work within a commercial account can obtain the bounded CnOpenData structured module (2017-2022 excluding 2018, with place names and coordinates); this is not the full official 2009-2022 series and not the 2013-2017 township-year file that a verified Journal of World Economy study reconstructed from AliResearch reports.

## Select rules

- Prioritize these lists when the research needs which rural villages/towns Alibaba's ecosystem recognized as Taobao villages (exposure construction, coverage analysis, distance-based designs with the module's lat/lon).
- Switch to china-mofcom-rural-ecommerce-demo-counties when the question is the government demonstration-program counties (different selection authority and roster); switch to china-rural-ecommerce-couture-2021-replication when the question needs the RCT household microdata.
- Do not use this record for village sales volumes, shop counts, the MOFCOM program, or the Rural Taobao RCT data - those are separate assets.

## Get recipe

1. For the current structured route: open the CnOpenData module page (cnopendata.com/data/m/Platform_Eco/taobao-township.html), register an account, and request the 淘宝村淘宝镇名单数据 module; confirm price/terms in the account flow (not public).
2. Verify the delivered tables against the page description: two tables (village/town), 2017-2022 excluding 2018, fields 省/市/区县/村/经纬度; cross-check 2022 counts (7,780 villages / 2,429 towns).
3. For the full official series (2009-2022), browse aliresearch.com in a JS-capable browser (annual notices, taobaoVillageResearchList query page) and transcribe/export the rosters; no machine-readable official download is confirmed.
4. Normalize village/town names across years and match administrative codes (the module references NBS 2021 division codes) before joining to outcomes.

## Connections and Limitations

The natural unit is village-year / town-year with province/city/county name fields; the module adds lat/lon, enabling distance-based designs, but the field format and precision are unverified. The module omits 2018 and pre-2017 years, so a full 2009-2022 panel requires the official announcement route. The lists are rosters built on selection thresholds (>=10M RMB sales etc.), not sales measures. The verified 2022 paper used AliResearch reports for a 2013-2017 township-year indicator, not the later CnOpenData module; other papers still require vintage- and field-specific checking.
