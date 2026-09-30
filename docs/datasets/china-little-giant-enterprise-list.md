---
schema_version: 3
catalog_status: grounding
id: china-little-giant-enterprise-list
name: MIIT national-level 'Little Giant' (专精特新小巨人) enterprise designation lists
aka:
- 专精特新"小巨人"企业名单
- Little Giant enterprises list
- 国家级专精特新小巨人
- MIIT Little Giant designations
provider: >-
  Ministry of Industry and Information Technology (MIIT, 工业和信息化部) SME bureau
  (中小企业局): national designation batches with public 公示 (publicity) and 公布
  (announcement) rounds. Announcements are posted on miit.gov.cn and reposted on
  gov.cn/provincial government sites.
china_related: true
domains:
- firm
- industrial
- regional
- innovation

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    Firm-level list of MIIT-designated 'Little Giant' enterprises (firm names per batch),
    with locations added by the researcher (geocoding to prefecture/city), used for
    geographic-concentration analysis (Tang, Zheng, Yang & Ren, Ann Reg Sci 2025: five
    batches announced May 2019-July 2023, 12,950 enterprises).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The designation program and its batch structure are confirmed from MIIT news (fetched
    2026-08-15: 4th batch of 4,300+ completed 公示 by 2022-08; ~9,000 designated cumulatively
    by 2023-05), the ARS 2025 paper's abstract (read on Springer 2026-08-15: five batches
    announced by MIIT May 2019-July 2023, 12,950 enterprises, geocoded with ArcGIS 10.7),
    and a 2026-09-28 route check. MIIT's own 2021 explanation identifies the second national
    designation notice as 工信部企业函〔2020〕335号 and confirms that the first two designation
    batches together contained 1,832 enterprises. That is distinct from later "second-batch
    first/second/third-year" support or review lists. The same check pinned MIIT's direct PDF
    attachment for the third-batch publicity list: it is a national, 63-page table of sequence
    number and enterprise name, rather than a provincial subset. The lists are public
    announcements; compiling a firm-level list with locations is the reusable
    collection/geocoding work. For the fifth batch, MIIT's 2023 process notice
    makes clear that a public list of proposed fifth-batch designations precedes
    the final announcement. A Guangzhou SASAC official repost identifies that
    final announcement as 工信部企业函〔2023〕272号 and reports 3,654 fifth-batch
    firms; the same notice separately reports 1,078 firms passing a review of
    the *second* batch. This establishes the fifth-batch final-list identity and
    count, but is not itself the national list attachment.
    The directly obtainable third-batch publicity PDF is separately catalogued as
    miit-third-batch-little-giant-publicity-roster-2021. A complete, directly
    checked national attachment set for all five paper-era final-designation
    batches is still not pinned, so this broader multi-batch/geocoded asset is
    not yet a ready reproducible route.
  barrier: >-
    MIIT search is JS-driven and the direct national attachments for batches 1, 2, 4, and 5
    remain unpinned. For batch 5, 工信部企业函〔2023〕272号 is now pinned as the final
    designation-notice identity and 3,654 as its corroborated count, but the attachment
    containing the national firm names is still missing. The same notice's 1,078 is a
    second-batch *review* count, not fifth-batch membership. The official 1,832 figure is a
    combined first-two-batch total, not a second-batch count or a complete five-batch series.
    The paper's 12,950 total remains abstract-level.

unit_of_observation: Designated enterprise (firm) per batch; locations derived by the researcher
structure: batch lists (cross-sectional per batch, ~annual designations since 2019)
geo_granularity:
- firm
- prefecture/city (researcher-derived via geocoding)
- province
geography: Mainland China (national program; enterprises across provinces)
time_span:
  start: '2019'
  end: '2024'
  last_confirmed_release: '2024 (6th batch program launched 2024-04 per gov.cn repost)'
  coverage_note: >-
    First batch 2019-05. Fifth-batch final designation notice 工信部企业函〔2023〕272号
    reports 3,654 newly designated firms; its separately reported 1,078 firms are the
    reviewed second batch, not an additional fifth-batch list. Batches continue (6th batch cultivation launched 2024-04-17 per
    gov.cn repost of MIIT notice). The ARS 2025 paper uses batches 1-5 (May 2019 - July 2023,
    12,950 enterprises per its abstract). Later batches (6th 2024, 7th 2025) exist per
    program continuity and news coverage but their official lists were not pinned this round.
  last_checked: '2026-08-15'
frequency:
- irregular batch announcements (roughly annual)
sample_size: >-
  ARS 2025 paper: 12,950 enterprises across five batches (abstract-level). Cumulative
  ~9,000 by 2023-05 (MIIT news, before the 5th batch announcement). Per-batch official
  counts not independently verified this round.
key_variables:
- Designated enterprise name
- Batch (批次) and announcement date
- Firm location (researcher-derived; city/province)
- Designation attributes (e.g., specialization fields) per announcement attachments (unread)

research_fit:
  best_for:
  - Research using MIIT 'Little Giant' designations as a firm-level public list with
    location information (e.g., geographic concentration or matched-firm description)
  - Rebuilding a designated-firm panel for designated-firm analyses
  choose_over:
  - Choose this designation list over china-firm-registry / china-tianyancha-firm-information
    when the question is about the MIIT designation program itself (the registry families
    record all firms; the designation is the treatment/program signal).
  - Use the registry families for full registration data; this record is the designation list
    and its collection route.
  not_good_for:
  - Full firm-level financial or registration microdata (use registries/ASIF).
  - Claiming per-batch official counts without checking the announcement attachments.
  needs_join_for:
  - Firm characteristics (china-tianyancha-firm-information, china-firm-registry, ASIF)
  - City-level economic covariates (china-stat-yearbook family)
  variation_available:
  - The observable dimensions are firm name, designation batch/date, and any
    researcher-derived location. Whether a designation can be used as a
    treatment, comparison, or causal event is outside this data record.
  topics:
  - little giant
  - zhuanjingtexin
  - industrial policy
  - firm designation
  - geographic concentration

good_for:
- designated-firm geographic analysis
- descriptive or matched-firm research that needs the designation-list membership field
identification:
- >-
  This is a batch membership list: it identifies which named enterprises appear
  in a particular MIIT designation notice. It is not a firm registry, an outcome
  panel, or a causal-design record; any use of the batch date beyond data joining
  requires separate design evidence.
linkable_keys:
- Enterprise name (matching to registries requires name normalization)
- City/province (researcher-derived)

joins:
- target: china-tianyancha-firm-information
  relation: complement
  keys:
  - enterprise name
  method: name-based matching to registry/relationship data; normalization required
  evidence_status: plausible
- target: china-firm-registry
  relation: complement
  keys:
  - enterprise name / registration identifiers
  method: name-based matching; not verified this round
  evidence_status: plausible

access_routes:
  - route: miit.gov.cn announcement pages (primary)
    access_status: available-with-conditions
    direct_url: https://www.miit.gov.cn/
    requirements: Human browser (MIIT search is JS-driven; automated clients get the SPA shell)
    steps:
    - Navigate MIIT's 中小企业局 announcement columns for each batch's 公示 or 公布 notice, using the batch's formal citation as a search anchor
    - For batch 3, start from the directly retrievable national publicity-list PDF below; it is a 63-page table of sequence number and enterprise name
    - Preserve the dated notice/attachment URL alongside each parsed batch, because later review lists and renamed-firm notices are different products
    deliverable: Per-batch national firm lists (announcement attachments); only the batch-3 national PDF is directly pinned and checked
    cost: free
    last_checked: '2026-09-28'
    caveat: Do not substitute a publicity list, a later "second-batch first/second/third-year" support list, a three-year review list, or a provincial repost for the final national designation list without recording that distinction. MIIT identifies the 2020 second designation notice as 工信部企业函〔2020〕335号. Batch 5's final notice identity is 工信部企业函〔2023〕272号 (3,654 fifth-batch firms), but its direct national attachment is still not pinned; its 1,078 second-batch review firms are a different list. Primary direct URLs for batches 1, 2, 4, and 5 therefore remain incomplete, so provincial/government reposts remain cross-checks, not a verified complete route.
  - route: provincial government reposts
    access_status: available
    direct_url: https://gxj.guiyang.gov.cn/zfxxgk/fdzdgknr/zdlyxxgk/myjjgl/202307/t20230717_81002465.html
    requirements: none
    steps:
    - Provincial 公示 pages republish the batch lists (example: Guizhou 5th batch 公示 2023-07-17)
    deliverable: Batch list reposts (province-level subsets or full lists)
    cost: free
    last_checked: '2026-08-15'
    caveat: Reposts may be province-subset lists; the national full list is in the MIIT announcement.
  - route: paper-full-text (paper-use verification)
    access_status: needs-verification
    direct_url: https://link.springer.com/article/10.1007/s00168-025-01417-y
    requirements: Pay-per-view (39.95 EUR) or subscription (Springer; abstract and metadata are readable without payment)
    steps:
    - Read the ARS 2025 data section for the exact list versions and geocoding steps
    deliverable: Paper data-section detail; no data file
    cost: paid
    last_checked: '2026-08-15'
    caveat: Abstract read via Springer page (2026-08-15); full text paywalled.

access:
  url: https://www.miit.gov.cn/
  cost: free (public announcements)
  license: public government announcements
  format:
  - pdf/xlsx/doc attachments (per announcement)
  api: false
  how_to_get: Collect per-batch firm names from MIIT announcement attachments (or provincial reposts), then geocode.
caveats: >-
  The paper's 12,950 total (five batches) is from its abstract; per-batch official counts
  need the announcement attachments. Batch 6 (2024) and later exist per program continuity
  but their national lists were not pinned this round.

production:
  raw_sources:
    - name: MIIT 专精特新小巨人 batch announcements
      source_type: webpage
      role: designated-firm lists per batch
      access_route: miit.gov.cn (human browser) + provincial/gov.cn reposts
      url: https://www.miit.gov.cn/
      coverage: batches from 2019-05 onward (5 batches to 2023-07 used by the ARS paper)
      last_checked: '2026-08-15'
    - name: ARS 2025 paper (use evidence)
      source_type: other
      role: paper-use anchor (five batches, 12,950 firms, ArcGIS geocoding)
      access_route: Springer article page (abstract readable)
      url: https://link.springer.com/article/10.1007/s00168-025-01417-y
      coverage: batches May 2019 - July 2023
      last_checked: '2026-08-15'
  acquisition_methods:
  - download (announcement attachments)
  - crawl (if systematic per-batch collection)
  sample_construction: >-
    Per-batch announcement lists; the ARS paper's sample = five batches (May 2019 - July
    2023), 12,950 enterprises (abstract-level).
  pipeline_stages:
    - stage: collect
      inputs:
      - MIIT announcements
      method: download announcement attachments per batch; parse firm names
      tools: []
      parameters:
      output: firm-level batch list (names, batch, announcement date)
      evidence: ARS abstract; MIIT news; provincial reposts (2026-08-15)
    - stage: geocode
      inputs:
      - firm names/addresses in announcements
      method: geocoding to coordinates/city (paper used ArcGIS 10.7; exact geocoding source unread)
      tools:
      - ArcGIS
      parameters:
      output: firm spatial point data (paper-level)
      evidence: ARS abstract (paper-level; details unread)
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: designated enterprise
    structure: batch lists / spatial points
    geography: prefecture-level (paper-level aggregation)
    time_span: 2019-2023 (paper sample)
    key_variables: firm name, batch, location
    formats:
    - xlsx/pdf/doc (announcements)
  reproducibility:
    level: medium
    starting_point: MIIT announcement attachments per batch (primary URLs to pin via human browser)
    code_available: false
    code_url: ''
    requirements:
    - human browser for MIIT search/announcement pages
    - geocoding step (paper used ArcGIS; alternatives exist)
    blockers:
    - primary miit.gov.cn per-batch URLs not pinned this round
  compliance:
    terms_or_license: public government announcements
    robots_or_rate_limits: not documented on read pages
    personal_or_sensitive_data: none (firm names)
    redistribution: public data; redistribution per China's government information disclosure rules (not verified)
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: abstract-only
  last_audited: '2026-08-15'

used_by:
- cite: 'Tang, Zheng, Yang & Ren (2025), Examining the geographic concentration of China''s "Little Giant" enterprises'
  doi: https://doi.org/10.1007/s00168-025-01417-y
  journal: The Annals of Regional Science
  year: 2025
  dataset_role: Five MIIT 'Little Giant' batches (May 2019 - July 2023), 12,950 enterprises, geocoded for prefecture-level concentration analysis
  evidence_type: abstract-only
  evidence_url: https://link.springer.com/article/10.1007/s00168-025-01417-y
  data_note: >-
    Springer article page (read 2026-08-15): 'selects five batches of China's national-level
    specialized and sophisticated "Little Giant" Enterprises announced by the Ministry of
    Industry and Information Technology from May 2019 to July 2023, totalling 12,950 ...
    as the sample data. The study employed ArcGIS 10.7 ... to transform the enterprise
    coordinates into enterprise spatial point data files.' Full text paywalled (39.95 EUR);
    the data section (list versions, geocoding source) is unread.

provenance:
- source: https://www.miit.gov.cn/threestrategy/dtzx/zhzx/art/2022/art_c0434369e2a24d2faaf28d870f727775.html
  field_scope:
  - MIIT program news (repost of People's Daily 2023-05-13): 4th batch 4,300+ completed 公示; ~9,000 'Little Giant' enterprises cumulatively by then
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://link.springer.com/article/10.1007/s00168-025-01417-y
  field_scope:
  - ARS paper identity (74:90, 2025-09-29), authors, abstract (five batches May 2019-July 2023, 12,950 firms, ArcGIS geocoding)
  - paywall status (no-access; 39.95 EUR PPV)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.miit.gov.cn/cms_files/filemanager/1226211233/attach/20217/71bd4daebeb44632b672b7747a36b65f.pdf
  field_scope:
  - Direct MIIT attachment for the third-batch publicity list: national table, 63 pages, with sequence number and enterprise-name columns
  - Distinction between a directly obtainable national batch-list input and an unreleased paper geocoding/output file
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.miit.gov.cn/zwgk/zcjd/art/2021/art_456ef30df73345ccba8852dea5c016d0.html
  field_scope:
  - Official identification of the second national designation notice as 工信部企业函〔2020〕335号
  - Official combined first-and-second-batch total of 1,832 enterprises
  - Boundary between designation batches and later support/review lists
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2023/art_8b5db52eb1864c4da842a61543c9ecf7.html
  field_scope:
  - Official fifth-batch/second-batch-review process: MIIT publicizes proposed fifth-batch designations before issuing the final list
  - Boundary that fifth-batch designation and second-batch review are separate outputs of the same 2023 workflow
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://gzw.gz.gov.cn/qy/qydt/content/post_9317207.html
  field_scope:
  - Official Guangzhou SASAC repost identifying the final combined notice as 工信部企业函〔2023〕272号
  - Corroborated counts: 3,654 fifth-batch designated firms and 1,078 second-batch review-passing firms
  - Notice identity and counts only; this repost is not a national firm-list attachment
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.ncsti.gov.cn/kjdt/tzgg/201906/t20190613_3307.html
  field_scope:
  - Public reprint of MIIT's first-batch 2019 designation notice, including the stated 248 enterprises and an embedded enterprise-name/product table
  - First-batch citation and list identity only; this is not treated as a pinned MIIT-primary attachment
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://gxj.guiyang.gov.cn/zfxxgk/fdzdgknr/zdlyxxgk/myjjgl/202307/t20230717_81002465.html
  field_scope:
  - provincial 公示 page for the 5th batch (2023-07-17, search-result lead; not fetched this round)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://www.gov.cn/lianbo/bumen/202404/content_6946051.htm
  field_scope:
  - 6th batch cultivation launch (2024-04; gov.cn repost of MIIT notice; search-result lead)
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: miit-third-batch-little-giant-publicity-roster-2021
  relation: successor
- id: china-firm-registry
  relation: complement
- id: china-tianyancha-firm-information
  relation: complement
---

## Positioning in one sentence

工信部专精特新"小巨人"名单是国家批次认定名单（2019 年起公开公示/公布，2023 年中前累计约 9000 家；ARS 2025 论文用 2019-05 至 2023-07 五批共 12,950 家做地理集中度分析）。第五批最终通知现已锚定为工信部企业函〔2023〕272号，其中第五批为 3,654 家；同通知的 1,078 家是第二批复核通过企业，不能混入第五批。第三批全国公示名单已有工信部直链 PDF；其余论文期批次的完整直链集合尚未钉住。把这些名单变成带区位的分析数据仍需要逐批收集和地理编码。

## Select rules

- 研究"小巨人"认定本身（政策暴露、地理集中度）时用本名单；要全量注册/财务信息改用 registry/天眼查/ASIF。
- 名单是政策项目清单，不是企业注册库——不要把二者混为一谈（见 china-firm-registry 边界）。
- 论文确切的名单版本与地理编码细节未读（Springer 付费墙）。

## Get recipe

1. 人类浏览器访问 miit.gov.cn（站内搜索为 JS 驱动），逐批找"专精特新'小巨人'企业名单公示/公布"通知并下载附件名单；第三批可先用已钉住的全国公示 PDF 验证解析方式。
2. 用省级政府转载页交叉核对（例：贵阳市政府 2023-07-17 第五批公示页）。
3. 解析企业名称，做名称标准化与地理编码（论文用 ArcGIS 10.7；替代工具可行）。
4. 按研究需要聚合到地级市/省级。

## Connections and Limitations

- 连接：企业名称可与天眼查/registry 做名称匹配（需规范化，未验证）；与城市年鉴类变量按区位连接。
- 限制：五个论文期批次尚未形成完整的直接官方附件集合，且各批次最终认定与公示/复核名单不能混用；第五批已知最终通知和总数，但其全国企业名附件仍未钉住。论文 12,950 仍是摘要级数字。第 6/7 批名单未在本轮钉住。
- 已核验但仍不充分：工信部确认第二批的正式通知编号，并确认前两批合计 1,832 家；这不能替代第二批完整附件，也不能把后续“第二批第 X 年”支持/复核名单当作原始认定名单。
