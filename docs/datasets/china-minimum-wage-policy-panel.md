---
schema_version: 3
catalog_status: ready
id: china-minimum-wage-policy-panel
name: China minimum wage standards (province/tier/county standards panel, reconstructable from official notices)
aka:
- 最低工资标准
- China Minimum Wage Policy Panel
- 全国各地区最低工资标准情况
- 区县最低工资数据
provider: >-
  Official system: Ministry of Human Resources and Social Security (MOHRSS
  人力资源社会保障部) national snapshots plus provincial government / provincial
  human-resources-and-social-security (人社厅) adjustment notices. Ready-made
  commercial/academic products: CnOpenData 中国各区县最低工资数据; HNU EDRC
  县级最低工资标准数据库 (Wang Haicheng).
china_related: true
domains:
- labor
- policy
- regional
- county

data_pathway:
  mode: collected
  origin: mixed
  target_artifact: >-
    A researcher-built panel of minimum wage standards: for each province,
    the intra-province tiers, the tier-to-county/district mapping (适用区域),
    the monthly and hourly RMB standards, and each adjustment's effective
    date. Raw source: provincial HRSS/government adjustment notices
    (scattered HTML/PDF, no central historical machine-readable index);
    ready-made partial products exist (MOHRSS national snapshots; CnOpenData
    county product; HNU county database).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Grounding pass 2026-08-15: the official announcement system is verified
    at national and provincial level. MOHRSS publishes periodic national
    snapshots 全国各地区最低工资标准情况 (editions 2016-12 through 2026-01,
    verified 2026-08-14; province-level rows, up to 4 tiers per province,
    monthly + hourly, machine-readable HTML). Provincial notices are the
    reconstructable raw source for a full panel with effective dates and
    tier-to-county mapping - verified this round on three official pages:
    Guangdong notice 粤府函〔2025〕23号 (published 2025-02-14, effective
    2025-03-01, 4 tiers with city mapping) plus its official interpretation;
    Guizhou provincial HRSS notice (effective 2025-02-01, 3 tiers with a
    county/district-level 区域划分表) forwarded by Xingyi city HRSS
    (2026-08-12); Guangxi HRSS interpretation (2018-01-19) documenting the
    adjustment-frequency rule (最低工资规定 Art.10: at least every 2 years;
    人社部发〔2015〕114号: relaxed to every 2-3 years). All three pages are
    machine-readable HTML.
  barrier: >-
    No single official ready-made historical panel exists: effective dates
    and tier-to-county mappings live only in scattered per-province notices,
    so a full county-month panel is per-province collection work. Ready-made
    commercial/academic products (CnOpenData 1999-2023 county product; HNU
    EDRC 2005-2010 county database) have unverified terms/prices (CnOpenData
    price not shown on public page; HNU application terms unverified).
    The paper-use evidence presently visible to this catalog is abstract-level
    only: the official Journal of World Economy page identifies the 2005-2010,
    2,855-county manual data and its ASIF/customs match, while the paper's
    methods/data section has not been read. That is not enough to establish
    its detailed construction or to treat the paper-built file as obtainable.

unit_of_observation: >-
  Province-tier or county/district-tier minimum wage standard per adjustment
  period (monthly RMB for full-time; hourly RMB for part-time)
structure: panel (reconstructable) plus point-in-time snapshots
geo_granularity:
- province
- city
- county/district
geography: All 31 mainland provinces/regions (Shenzhen is a separate row inside Guangdong in MOHRSS snapshots)
time_span:
  start: '1999'
  end: ongoing
  last_confirmed_release: >-
    MOHRSS snapshot edition 截至2026-01-01 (published 2026-01-12); CnOpenData
    county product 1999-2023; provincial notices verified 2025 (Guangdong,
    Guizhou) and 2018 (Guangxi)
  coverage_note: >-
    MOHRSS snapshots cover 2016-12 onward (indexed editions); earlier
    history must come from provincial notices or commercial/academic
    compilations (CnOpenData claims 1999.06/07 start; HNU database
    2005-2010). Point-in-time snapshots carry no effective dates.
  last_checked: '2026-08-15'
frequency:
- event (per adjustment, typically every 2-3 years per province)
- snapshot (MOHRSS national tables)
sample_size: >-
  31 provinces in MOHRSS snapshots; up to 4 tiers per province; CnOpenData
  claims county-level coverage 1999-2023 (row counts not shown on public
  page); HNU county database: 2,855 counties/districts, 17,130 records,
  2005-2010 (HNU EDRC page, verified 2026-08-14)
key_variables:
- Monthly minimum wage (RMB) per tier
- Hourly minimum wage (RMB) for part-time workers per tier
- Tier scope: applicable cities/counties/districts (适用区域)
- Effective date of each adjustment (provincial notices; commercial products include adjustment date)
- Legal basis and repeals (e.g., Guizhou 2025 notice repeals 黔人社发〔2022〕31号)

research_fit:
  best_for:
  - Minimum-wage exposure/outcome research needing effective dates and tier-to-county mappings, which only the provincial-notice reconstruction (or commercial county products) can provide
  - Province-level current standards with machine-readable official snapshots (MOHRSS 2016-12 onward)
  choose_over:
  - Choose the official MOHRSS snapshots when province-level current standards suffice and an official free source is required.
  - Choose provincial-notice collection when effective dates and county-tier mappings matter (the only official route to a full panel).
  - Choose CnOpenData 区县最低工资 (1999-2023, county level, adjustment date) as a paid shortcut when reconstruction cost is prohibitive - terms unverified on the public page.
  - Choose the HNU EDRC county database (2005-2010) for that exact window - application terms unverified.
  not_good_for:
  - Treating the Xu--Wang paper's abstract-level description as proof of its
    full construction, cleaning choices, or a released analysis file
  - County-to-county mapping before 1999 without verifying the commercial product's vintage and fields
  - Imputing effective dates from MOHRSS snapshots (they are point-in-time only)
  needs_join_for:
  - Firm or worker outcomes (ASIF, customs, surveys) - join by county/district and period
  - Policy assignment/identification design (see Econ-Variation)
  variation_available:
  - Cross-province, cross-tier and over-time variation in standards; adjustment timing varies by province (2-3 year cycles)
topics:
- minimum wage
- labor regulation
- wage standards
- county policy data

good_for:
- Building minimum-wage exposure panels with official effective dates
- Province-level current standards from an official free source
- Wage-floor research across Chinese regions
identification:
- >-
  The ready official snapshot product is titled 全国各地区最低工资标准情况 on the
  MOHRSS 服务园地 column: it is a dated province-by-tier table of monthly and
  hourly RMB standards, not a county-month panel and not evidence of an
  adjustment's effective date.
- >-
  The ready reconstruction input is a province's formal minimum-wage
  adjustment notice and any attached 适用区域 table. Identify each source by
  issuing authority, formal notice number, effective date (not merely web
  publication date), tier amount/unit, and the cities/counties assigned to
  that tier. The resulting researcher-built panel is distinct from the paid
  CnOpenData product and the HNU 2005-2010 academic database.
linkable_keys:
- Province
- City/county/district name (tier mapping)
- Effective date
- Standard amount (monthly/hourly)

joins:
- target: asif
  relation: complement
  keys:
  - County/district
  - Year (effective-date matching)
  method: Match firm county to tier by the adjustment in force in the firm-year; watch mid-year adjustments
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province
  - Year
  method: Join province-year controls; do not confuse yearbook wage levels with minimum standards
  evidence_status: plausible

access_routes:
- route: official-snapshot
  access_status: available
  direct_url: https://www.mohrss.gov.cn/SYrlzyhshbzb/laodongguanxi/fwyd/ (服务园地 column index)
  requirements: None; public gov.cn pages
  steps:
  - Open the MOHRSS 服务园地 column index; locate 全国各地区最低工资标准情况 editions (2016-12 through 2026-01 indexed; verified editions 截至2026-01-01 and 截至2024-07-01).
  - Read the machine-readable HTML table: 31 provinces, tiers, monthly + hourly standards.
  deliverable: Province-level point-in-time standard tables; no effective dates, no tier-to-county mapping, no pre-2016-12 history
  cost: free
  last_checked: '2026-08-15'
  caveat: Snapshot only - do not derive effective dates or county mappings from these tables.
- route: official-notice-collection
  access_status: available
  direct_url: http://www.gd.gov.cn/zwgk/wjk/qbwj/yfh/content/post_4668031.html
  requirements: None; per-province collection work (HTML pages + DOCX/PDF attachments; no central historical machine-readable index)
  steps:
  - For each province, find the latest adjustment notice on the provincial government portal or provincial HRSS site (verified examples: Guangdong 粤府函〔2025〕23号 2025-02-14; Guizhou provincial HRSS notice effective 2025-02-01 forwarded by county HRSS 2026-08-12; Guangxi interpretation 2018-01-19).
  - Extract standards, tier-to-county mapping (适用区域), effective date, and repeals; normalize names to current admin codes.
  deliverable: Reconstructed province-tier/county-tier panel with effective dates; manual per-province collection
  cost: free
  last_checked: '2026-08-15'
  caveat: Update cadence ~every 2-3 years per province (人社部发〔2015〕114号); interpretation pages often accompany notices and state the tier mapping.
- route: commercial-county-product
  access_status: available-with-account
  direct_url: https://www.cnopendata.com/data/m/covid19/minimum-wage-by-region.html
  requirements: CnOpenData account/purchase; price and license not shown on the public product page
  steps:
  - Open the CnOpenData product page 中国各区县最低工资数据 (read 2026-08-15: two tables - 各区县最低工资划分标准 and 各区县最低工资金额; time ranges 1999.06.01-2023.03.01 (division) and 1999.07.01-2023.03.01 (amount); adjustment date among fields; annual update).
  - Purchase/download per CnOpenData terms (unread on public page).
  deliverable: County-level minimum wage tables 1999-2023 with division standards, amounts and adjustment dates
  cost: paid
  last_checked: '2026-08-15'
  caveat: Terms, price, and field-level detail require the account-based route; update-on-request claim unverified.
- route: academic-county-database
  access_status: needs-verification
  direct_url: needs-verification
  requirements: HNU EDRC (Hunan University) application terms unverified
  steps:
  - Contact HNU EDRC for 县级最低工资标准数据库 (Wang Haicheng; 2005-2010, 2,855 counties/districts, 17,130 records, 96.35% coverage per the official HNU EDRC page read 2026-08-14).
  deliverable: County-level monthly standards 2005-2010 with annual weighted averages for mid-year adjustments (per the methods paper)
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Application terms and deliverable unverified; verify before relying on it.

access:
  url: https://www.mohrss.gov.cn/SYrlzyhshbzb/laodongguanxi/fwyd/
  cost: free
  license: Public official government data; redistribution per government data policies (not separately reviewed)
  format:
  - html
  - pdf
  - docx
  api: false
  how_to_get: >-
    Free official route: MOHRSS snapshots (province level, 2016-12 onward)
    and per-province adjustment notices (full panel reconstruction).
    Paid shortcut: CnOpenData county product 1999-2023. Academic route: HNU
    EDRC county database 2005-2010.
caveats:
- MOHRSS snapshots carry no effective dates and no tier-to-county mapping; do not treat them as a full panel.
- Provincial notices are scattered with no central machine-readable historical index; reconstruction is per-province collection.
- Update frequency is 2-3 years per province since 人社部发〔2015〕114号 (before that every 2 years per 最低工资规定 Art.10) - verified via the official Guangxi HRSS interpretation (2018-01-19).
- Ready-made product terms (CnOpenData price/license; HNU application) are unverified.
- The Xu--Wang (2016) official journal page and HNU EDRC catalogue identify a 2005-2010, 2,855-county hand-collected asset, but the paper's methods/data section remains unread. This is deliberately kept as abstract-only evidence, not proof of the paper's detailed construction or an obtainable author file.

production:
  raw_sources:
  - name: MOHRSS 全国各地区最低工资标准情况 snapshots
    source_type: webpage
    role: Province-level point-in-time standards, 2016-12 onward
    access_route: https://www.mohrss.gov.cn/SYrlzyhshbzb/laodongguanxi/fwyd/
    url: https://www.mohrss.gov.cn/SYrlzyhshbzb/laodongguanxi/fwyd/
    coverage: 31 provinces, editions 2016-12 to 2026-01 (verified editions 截至2024-07-01, 截至2026-01-01)
    last_checked: '2026-08-15'
  - name: Provincial minimum wage adjustment notices (人社厅/省政府)
    source_type: webpage
    role: Standards, tier-to-county mapping, effective dates, repeals; the raw source for a full panel
    access_route: 'Per-province government portals (verified examples: Guangdong 粤府函〔2025〕23号; Guizhou 2025 notice via Xingyi forwarding; Guangxi 2018 notice/interpretation)'
    url: http://www.gd.gov.cn/zwgk/wjk/qbwj/yfh/content/post_4668031.html
    coverage: All 31 provinces over time; scattered HTML/PDF
    last_checked: '2026-08-15'
  - name: CnOpenData 中国各区县最低工资数据
    source_type: dataset
    role: Ready-made county-level product (division standards + amounts + adjustment dates)
    access_route: https://www.cnopendata.com/data/m/covid19/minimum-wage-by-region.html (account/purchase)
    url: https://www.cnopendata.com/data/m/covid19/minimum-wage-by-region.html
    coverage: 1999.06/07-2023.03, county level, annual update
    last_checked: '2026-08-15'
  acquisition_methods:
  - direct download
  - manual coding
  - purchase
  sample_construction: >-
    Official system: standards are set per province in tiers with explicit
    county/district scope; a full panel requires collecting each provincial
    notice (2-3 year cycles per province). Commercial/academic products
    provide ready-made compilations with their own unverified vintages.
  pipeline_stages:
  - stage: collect
    inputs:
    - Provincial adjustment notices (HTML/PDF)
    method: Per-province collection of notices, attachments, and interpretations; extract standards, 适用区域, effective dates, repeals
    tools:
    - browser/parser
    output: Province-tier and county-tier standard records with effective dates
    evidence: Guangdong notice + interpretation (2025-02), Guizhou notice + Xingyi forwarding (2025/2026), Guangxi interpretation (2018)
  - stage: clean
    inputs:
    - Collected records
    method: Normalize place names to current administrative codes; handle tier reclassifications (e.g., Guangxi 4-tier to 3-tier in 2018); handle mid-year adjustments (HNU uses annual weighted averages)
    tools: []
    output: Cleaned county-month standard panel
    evidence: Guangxi interpretation documents tier consolidation; HNU methods paper documents weighted-average approach
  constructed_variables:
  - name: Effective standard at county-month
    concept: The minimum wage in force for a county in a given month, from the applicable tier of the latest notice
    source_fields:
    - Tier mapping
    - Effective date
    - Standard amount
    method: Match county to tier; apply the notice in force at the date
    validation: Cross-check against MOHRSS snapshots where available
    limitations: Pre-1999 county mapping must come from earlier notices (unverified); some provinces' historical notices may be missing from the web
  validation:
  - Cross-check reconstructed province-tier standards against MOHRSS snapshot editions.
  - Verify effective dates against the notice text (not the publication date).
  - Watch intra-province tier reclassifications across adjustments.
  output:
    unit_of_observation: Province-tier or county-tier standard per adjustment period
    structure: Panel with effective dates (reconstruction) or point-in-time snapshots
    geography: 31 provinces; county/district tier mapping
    time_span: 1999-present (reconstruction); 2016-12 onward (official snapshots)
    key_variables:
    - Monthly standard
    - Hourly standard
    - Tier and tier scope
    - Effective date
    formats:
    - html
    - csv
  reproducibility:
    level: medium
    starting_point: MOHRSS 服务园地 index + provincial government portals
    code_available: false
    code_url:
    requirements:
    - Per-province collection (manual parsing of notices and attachments)
    - Name-to-admin-code normalization
    blockers:
    - No central machine-readable historical index
    - Some historical notices may be missing or attachment-only (PDF/DOCX)
  compliance:
    terms_or_license: Official government data, public; commercial product terms unverified
    robots_or_rate_limits: Official pages fetched cleanly via python HTTPS on 2026-08-15 (gd.gov.cn, rst.gxzf.gov.cn, gzxy.gov.cn)
    personal_or_sensitive_data: None
    redistribution: Official standards are public; check commercial product license before redistribution
    review_needed: true

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-09-28'

used_by:
- cite: 'Xu Helian & Wang Haicheng (2016), hand-collected county minimum wage data 2005-2010 matched to ASIF and customs (世界经济 2016 issue 7)'
  journal: 世界经济
  year: 2016
  dataset_role: County minimum wage standards 2005-2010 (hand-collected)
  evidence_type: abstract-only
  evidence_url: https://sjjj.magtech.com.cn/CN/Y2016/V39/I7/73
  data_note: >-
    The official Journal of World Economy page and the HNU EDRC catalogue
    identify a manually collected 2005-2010 county-standard dataset (2,855
    counties; HNU reports 17,130 records) matched to the industrial-enterprise
    and customs databases. The visible journal statement is abstract-level and
    the paper's methods/data section was not read; this does not establish its
    detailed collection, cleaning, matching rules, or an obtainable author file.

provenance:
- source: http://www.gd.gov.cn/zwgk/wjk/qbwj/yfh/content/post_4668031.html (read 2026-08-15)
  field_scope:
  - Guangdong notice 粤府函〔2025〕23号 (成文 2025-02-08, published 2025-02-14, effective 2025-03-01)
  - notice structure, attachment 广东省最低工资标准表, legal basis
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://www.gd.gov.cn/zzzq/zcjd/content/mpost_4668242.html (read 2026-08-15)
  field_scope:
  - Guangdong 2025 tiers and city mapping (Guangzhou 2500/23.7, Shenzhen 2520/23.7, tier 2 2080/19.8, tier 3 1850/18.3, tier 4 1750/17.4)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://www.gzxy.gov.cn/gzxysite/xysrsj/1342/202608/t20260812_90724419.html (read 2026-08-15)
  field_scope:
  - Guizhou 2025 notice (effective 2025-02-01; tiers 2130/22.4, 1980/20.8, 1890/19.8) with county/district-level 区域划分表
  - county HRSS forwarding chain; repeal of 黔人社发〔2022〕31号; legal basis 最低工资规定 + 人社部发〔2015〕114号
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://rst.gxzf.gov.cn/zwgk/xxgkzcfg/xxgkwjjd/tw/t3254177.shtml (read 2026-08-15)
  field_scope:
  - 最低工资规定 Art.10 (at least every 2 years) and 人社部发〔2015〕114号 (every 2-3 years)
  - Guangxi 2018 adjustment tiers (1680/1450/1300; 16/14/12.5) and 4-to-3 tier consolidation
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.cnopendata.com/data/m/covid19/minimum-wage-by-region.html and /article/minimum-wage-by-region/minimum-wage-amount (read 2026-08-15)
  field_scope:
  - CnOpenData county product: two tables, 1999.06/07-2023.03, adjustment date field, annual update
  added: '2026-08-15'
  confidence: high
  verified: true
- source: MOHRSS snapshot editions and 服务园地 index (verified 2026-08-14; cited in candidate ledger)
  field_scope:
  - national snapshot family 2016-12 to 2026-01, province-level rows
  added: '2026-08-14'
  confidence: high
  verified: true
- source: https://sjjj.magtech.com.cn/CN/Y2016/V39/I7/73 and https://edrc.hnu.edu.cn/sjzy.htm (read 2026-09-28)
  field_scope:
  - official journal identity and abstract-level statement that the paper matched manually collected 2005-2010 standards for 2,855 counties to industrial-enterprise and customs data
  - HNU EDRC catalogue statement that Wang Haicheng's county dataset contains 17,130 records for those 2,855 counties
  - boundary that the paper's methods/data section and dataset-delivery terms were not read
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-neri-marketization-index
  relation: complement
- id: asif
  relation: complement
---

## Positioning in one sentence

China's minimum wage standards are set per province in tiers mapped to cities/counties, published in MOHRSS national snapshots (province level, 2016-12 onward, free) and in scattered provincial adjustment notices that carry the effective dates and tier-to-county mappings needed to build a real panel; ready-made county products exist commercially (CnOpenData 1999-2023) and academically (HNU 2005-2010), with unverified terms. The official Journal of World Economy page confirms that the HNU-linked 2005-2010 asset was matched with industrial-enterprise and customs data, but only at abstract level.

## Select rules

- Use the official MOHRSS snapshots for province-level current standards; use provincial notices for effective dates and county-tier mappings (the only official route to a full panel).
- Take the paid shortcut (CnOpenData county product) only after checking its terms; verify the HNU application terms for the 2005-2010 window.
- Do not derive effective dates from snapshots. The verified Xu--Wang use is still abstract-level: do not treat it as evidence for hidden construction choices or as a download route.

## Get recipe

1. Free official: open the MOHRSS 服务园地 index, download 全国各地区最低工资标准情况 editions (2016-12 to 2026-01); for a full panel, collect each province's adjustment notice from its government portal (verified examples: Guangdong 粤府函〔2025〕23号; Guizhou 2025; Guangxi 2018), extracting standards, 适用区域, effective dates and repeals.
2. Paid shortcut: CnOpenData 中国各区县最低工资数据 (1999-2023, county level, adjustment dates).
3. Academic route: HNU EDRC 县级最低工资标准数据库 (2005-2010) - application terms unverified.

## Connections and Limitations

Join to firm or worker outcomes by county/district and effective-date matching (ASIF), and to province-year controls from yearbooks. Update frequency is 2-3 years per province since 人社部发〔2015〕114号 (before: every 2 years per 最低工资规定 Art.10). Known limits: no central machine-readable historical index; snapshots lack effective dates; tier reclassifications (e.g., Guangxi 2018) require care; commercial/academic product terms unverified; and the Xu--Wang paper's accessible evidence is abstract-level rather than a read methods/data section.
