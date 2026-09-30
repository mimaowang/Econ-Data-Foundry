---
schema_version: 3
catalog_status: ready
id: china-township-census-population-2010-2020
name: Tabulation on China population census by township (中国人口普查分乡、镇、街道资料), 2010 and 2020 volumes
aka:
- 中国人口普查分乡、镇、街道资料
- 分乡镇街道人口普查资料
- Tabulation on 2010/2020 China population census by township
- 七普分乡、镇、街道资料
provider: >-
  National Bureau of Statistics / census offices, published by China Statistics Press
  (中国统计出版社). 2010 volume: compiled by 国务院人口普查办公室 (State Council Population
  Census Office), published 2012, ISBN 9787503766602. 2020 volume: compiled by
  国务院第七次全国人口普查领导小组办公室 (State Council 7th Population Census Leading Group
  Office), published 2022-11, ISBN 9787503797736, 968 pages.
china_related: true
domains:
- demography
- urban
- regional
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The published printed volumes (and commercial PDF reproductions) containing township-level
    (乡/镇/街道) population tables from the 6th (2010) and 7th (2020) National Population
    Censuses. The paper-specific research asset (Yang, Yang & Lei CWE 2026) is a township-year
    panel of 16,364 township units with population-shrinkage indicators, built by extracting
    and matching these volumes with expressway accessibility.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Both volumes exist as published China Statistics Press books (2010: 2012, ISBN
    9787503766602, compiler 国务院人口普查办公室; 2020: 2022-11, ISBN 9787503797736, 968 pp,
    compiler 国务院第七次全国人口普查领导小组办公室), confirmed via library/book records
    (las.ac.cn 2010 record read 2026-08-15; winxuan 2020 product page read 2026-08-15) and a
    republication of the book's own foreword (tjcn.org page read 2026-08-15). The 2020 volume
    is the 7th census' township tabulation: direct registration aggregates (excl. 0.05%
    undercount and 2 million active military), resident population at 2020-11-01 00:00, using
    7th-census statistical zoning. A current China Statistics Press catalogue exposes a useful
    practical boundary: its contents are 31 province-level tables, each titled "乡、镇、街道人口",
    with a listed price of 500 CNY and 960 pages. That establishes a population tabulation, not a
    general township microdata file or the paper's constructed panel. Acquisition is by book
    purchase; a paid commercial PDF route exists (tjcn.org, 20 coins, unofficial). No free official digital release of the
    township volumes was evidenced. The ready recommendation is the bounded route to these
    published source tables, not a claim that the paper's extracted panel is downloadable or
    that its unread data section identifies the exact tables used. Paper use is abstract-level
    (CWE 70036: 16,364 township units from the 2010 and 2020 censuses + expressway accessibility; shrinkage indicators).
  barrier: >-
    No free digital release evidenced; acquisition requires print purchase, library access, or
    an unofficial commercial PDF. The paper's exact extraction route (which tables, how
    digitized) is unread (Wiley 403), so it remains outside this ready source-table route.

unit_of_observation: Township-level administrative unit (乡/镇/街道) population aggregates per census
structure: two decennial cross-sections (2010, 2020) at township level
geo_granularity:
- Township/street (乡、镇、街道)
geography: >-
  All mainland China townships (乡级单位 per the 6th-census zoning for 2010; per 7th-census
  statistical zoning for 2020 - the 2020 volume explicitly warns to adjust for zoning changes
  in historical comparisons).
time_span:
  start: '2010'
  end: '2020'
  last_confirmed_release: '2022-11 (2020 volume publication, winxuan record)'
  coverage_note: >-
    2010 volume published 2012; 2020 volume published 2022-11. Population reference dates:
    2010-11-01 00:00 (6th census) and 2020-11-01 00:00 (7th census) resident population.
    The 2020 volume excludes undercounted population (post-enumeration undercount 0.05%) and
    2 million active military personnel.
  last_checked: '2026-08-15'
frequency:
- decennial census volumes
sample_size: >-
  ~16,364 township units used in the CWE 2026 paper (abstract); the volumes themselves cover
  all mainland townships (count not independently verified this round).
key_variables:
- Township resident population (2010, 2020)
- Township resident population by province table in the 2020 volume (31 tables: one for each mainland province-level unit; official catalogue contents read 2026-09-28)
- Other township-level demographic tables, if any (not verified from the accessible catalogue)
- Population-shrinkage indicators (paper-constructed from the two cross-sections)

research_fit:
  best_for:
  - Township-level population change / shrinkage research matching the 2010-2020 census
    cross-sections at 乡/镇/街道 granularity
  - Small-area population distribution and size research below the county level
  choose_over:
  - Choose the township volumes over china-census microdata routes when county-level
    aggregation is too coarse and the required output is the official printed township
    tabulations (IPUMS China samples stop at 2000; NBS microdata routes are application-based).
  - Use china-census (summary tables/microdata routes) when province/county-level or
    micro-level analysis suffices.
  not_good_for:
  - Individual/family-level microdata (the volumes are aggregate tables).
  - Direct machine-readable panels are not in the volumes (the books are aggregate tables;
    the paper's township panel is a paper-specific extraction and matching construction).
  needs_join_for:
  - Expressway/transport accessibility (paper-constructed in CWE 70036)
  - County-level controls (china-stat-yearbook family, china-county data)
  variation_available:
  - Township-level population change 2010 vs 2020 (the paper's shrinkage measure)
  topics:
  - population shrinkage
  - township
  - census
  - small-area population

good_for:
- township-level population change
- small-area demography
- urban shrinkage
identification:
- Cross-sectional/pseudo-panel comparisons of township population change
linkable_keys:
- Township name/statistical zoning code (7th-census zoning for 2020; 6th-census for 2010 - zoning differs across censuses)

joins:
- target: china-census
  relation: predecessor
  keys:
  - township/county statistical zoning codes
  method: china-census documents the family routes; the township volumes are the finer printed sub-product
  evidence_status: plausible

access_routes:
- route: print purchase (bookstores / online retailers)
  access_status: available
  direct_url: https://item.winxuan.com/1202885806
  requirements: none (paid book)
  steps:
  - Order the 2010 volume (中国统计出版社 2012, ISBN 9787503766602) and/or the 2020 volume
    (ISBN 9787503797736, 968 pp) from a bookstore/online retailer
  - Digitize/extract tables for analysis (OCR or manual), or rely on library copies
  deliverable: Printed volumes (township-level census tables)
  cost: paid
  last_checked: '2026-08-15'
  caveat: >-
    No free official digital edition was evidenced; library holdings exist (e.g., las.ac.cn record
    for the 2010 volume). A current China Statistics Press catalogue record for the 2020 volume lists
    a 500 CNY price and 960 pages, while the earlier retailer record lists 968 pages; treat the seller
    metadata discrepancy as non-substantive until a physical copy or publisher erratum resolves it.
- route: commercial PDF (unofficial)
  access_status: available
  direct_url: http://www.tjcn.org/tjnj/00zg/41518.html
  requirements: paid download (20 coins on tjcn.org)
  steps:
  - Purchase the PDF version of the 2020 volume on tjcn.org (a commercial statistics site,
    not an official NBS channel)
  deliverable: PDF of the 2020 volume
  cost: paid
  last_checked: '2026-08-15'
  caveat: Non-official channel; 2020 volume description on the page matches the book's own foreword (read 2026-08-15).
- route: paper-full-text (paper-use verification)
  access_status: needs-verification
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/cwe.70036
  requirements: Subscription or library access (Wiley; automated clients 403)
  steps:
  - Read the CWE 2026 data section for which census township volumes/tables were used and how they were obtained
  deliverable: Paper data-section detail; no data file
  cost: paid
  last_checked: '2026-08-15'
  caveat: Not read this round (Wiley blocked); paper use currently abstract-level.

access:
  url: https://item.winxuan.com/1202885806
  cost: paid
  license: commercial publication
  format:
  - print
  - pdf (commercial)
  api: false
  how_to_get: Buy the printed volumes (China Statistics Press) or a commercial PDF; no free official digital route evidenced.
caveats: >-
  The two censuses use different statistical zonings at township level (the 2020 volume warns
  explicitly); historical comparisons require zoning alignment. The 2020 volume excludes
  undercount and active military. The accessible 2020 catalogue confirms 31 province-level
  township-population tables, but it does not reveal a downloadable data file, complete column
  layout, or the paper's exact extraction and matching method.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: abstract-only
  last_audited: '2026-09-28'

used_by:
- cite: 'Yang, Yang & Lei (2026), China''s Expressways and Population Shrinkage in Township-level Administrative Units'
  doi: https://doi.org/10.1111/cwe.70036
  journal: China & World Economy
  year: 2026
  dataset_role: 16,364 township-level units from the 2010 and 2020 National Population Censuses; population-shrinkage indicators matched with expressway accessibility
  evidence_type: abstract-only
  evidence_url: https://api.crossref.org/works/10.1111/cwe.70036
  data_note: >-
    Crossref abstract (read 2026-08-15): 'constructed innovative indicators, using data for
    16,364 township-level administrative units from the National Population Census of 2010 and
    2020, to identify population shrinkage and assess the mitigating effect of expressway
    accessibility'. The paper's data section (which volumes, how obtained/digitized, matching)
    is unread (Wiley 403).

provenance:
- source: https://www.las.ac.cn/front/book/detail?id=decfe0aeb1c378e67fad3d68eb20a3a7
  field_scope:
  - 2010 volume existence, title, compiler (国务院人口普查办公室), publisher (中国统计出版社), year 2012, ISBN 9787503766602
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://item.winxuan.com/1202885806
  field_scope:
  - 2020 volume existence, title, compiler (国务院第七次全国人口普查领导小组办公室), publisher (中国统计出版社), publication date 2022-11-01, 968 pages, ISBN 9787503797736
  - 2020 volume foreword (7th census special publication; 'published for every census since 2000'; undercount 0.05%, 2M military excluded; 2020-11-01 resident population; 7th-census statistical zoning)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://www.tjcn.org/tjnj/00zg/41518.html
  field_scope:
  - 2020 volume description (same foreword text) and existence of a paid commercial PDF route (20 coins)
  added: '2026-08-15'
  confidence: med
  verified: true
- source: https://api.crossref.org/works/10.1111/cwe.70036
  field_scope:
  - paper identity and abstract (16,364 township units, 2010/2020 censuses, expressway accessibility)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.yuntaigo.com/book.action?recordid=bmxmYmJoa2M5Nzg3NTAzNzk3NzM2
  field_scope:
  - 2020 volume catalogue metadata: China Statistics Press, ISBN 9787503797736, 2022-11, listed price 500 CNY and 960 pages
  - table-of-contents boundary: 31 province-level tables, each labelled as township/town/street population
  - confirms that the accessible catalogue does not itself provide a downloadable dataset or paper-specific panel
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-census
  relation: predecessor
---

## Positioning in one sentence

《中国人口普查分乡、镇、街道资料》2010 与 2020 卷是国务院人口普查机构编辑、中国统计出版社出版的乡级人口汇总册。可读到的 2020 目录明确列出 31 个省级表、每表为乡镇街道人口；它是乡镇尺度人口分布与规模研究（如人口收缩）的官方纸面数据源。获取靠购书或商业 PDF，没有证据表明存在免费官方数字版或现成的论文面板。

## Select rules

- 需要乡/镇/街道级人口两期横截面时选这两卷；县级或更粗粒度用 china-census 汇总表/微数据路线即可。
- 需要 2010 年代以后的个人级微数据时不能用这两卷（它们是聚合表；IPUMS 中国样本只到 2000）。
- 论文（CWE 70036）用 16,364 个乡镇单元构建收缩指标——那是一个论文特定的抽取+匹配面板，不是卷内的现成表格。

## Get recipe

1. 购书：2010 卷（统计社 2012，ISBN 9787503766602）与 2020 卷（统计社 2022-11，ISBN 9787503797736）可从书店/电商购买，或查图书馆馆藏（如 las.ac.cn 有 2010 卷记录）。
2. 数字替代：tjcn.org 提供 2020 卷付费 PDF（20 金币，非官方渠道）。
3. 抽取表格（OCR/人工）并按统计用区划对齐两期（2010 用六普区划、2020 用七普区划——卷内明确警告跨期比较需调整）。
4. 论文同款收缩指数构造需读 Wiley 全文数据章节（未读）。

## Connections and Limitations

- 连接：以乡级单位名称/区划代码与高速可达性、县级控制变量连接；两期区划不同，连接前必须做区划对齐。
- 限制：免费官方数字版未证实；论文的抽取方式未读。2020 卷可见目录只确认 31 个省级乡镇人口表，不能证明每个表的完整字段或提供可下载的机器可读文件。
- 未验证：全部乡镇的单元总数（论文用 16,364，卷内实际乡级单元数未独立核对）。
