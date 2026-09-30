---
schema_version: 3
catalog_status: grounding
id: china-local-government-work-report-texts
name: Chinese local government work reports text corpus (政府工作报告文本语料)
aka:
- 政府工作报告文本
- Government Work Report corpus
- 地方政府工作报告数据库
- GWR texts
provider: >-
  Reports are produced by central, provincial and prefecture-level governments and are
  publicly posted on gov.cn and local government websites (e.g., prefecture 政府工作报告
  disclosure columns). Ready-made corpus providers: CnOpenData '中国各地区政府工作报告数据库'
  (commercial; 2000-2025, 9,595 documents: 26 central + 1,097 provincial + 8,472
  prefecture-city; 129 PDF + 8,343 TXT) and a dataset listed on the National Basic Science
  Data Center (NBSDC, dataset page 643fa54c87c4324301f65fe2; content unread, JS-loaded).
china_related: true
domains:
- governance
- urban
- regional
- public

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A text corpus of Chinese government work reports (government x year), with the
    paper-specific asset being tone measures of forward-looking content used in event-study
    designs (Gong, Cao, Zhao & Zeng CWE 2025: forward-looking-content tone -> CARs of local
    listed firms). The separately catalogued CnOpenData commercial corpus is a ready-made
    acquisition product, not evidence of the paper-specific corpus or its tone construction.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Provider side verified 2026-08-15: work reports are public official documents posted
    annually on government websites (example disclosure columns read: Ordos 政府工作报告
    column; Liuzhou; Sichuan Pidu district), and ready-made corpora exist - CnOpenData's
    commercial database (2000-2025, 9,595 reports, coverage read from its product page) and
    an NBSDC dataset (metadata JS-loaded, unread this round). The paper use is abstract-level
    (CWE 12620: positive tone in forward-looking content raises CARs of local listed firms,
    stronger under policy uncertainty). The paper's own corpus construction (period, levels,
    source, sentiment dictionary) is unread (Wiley 403).
  barrier: >-
    A national machine-readable corpus requires either the commercial product (paid) or
    self-collection from thousands of government pages; the paper's exact corpus period and
    construction are unread.

unit_of_observation: One government work report (government x year)
structure: corpus of annual reports (central/provincial/prefecture levels)
geo_granularity:
- central
- province
- prefecture/city
geography: Mainland China (central + provincial + prefecture levels; CnOpenData corpus claims all three levels)
time_span:
  start: '2000'
  end: '2025'
  last_confirmed_release: '2025 (CnOpenData corpus coverage claim, product page read 2026-08-15)'
  coverage_note: >-
    CnOpenData product page (read 2026-08-15): 2000-2025, 9,595 documents (26 central, 1,097
    provincial, 8,472 prefecture-city; 129 PDF + 8,343 TXT). The CWE 2025 paper's corpus
    period and levels are unread. NBSDC dataset existence noted (id 643fa54c87c4324301f65fe2,
    content unread).
  last_checked: '2026-08-15'
frequency:
- annual (per government)
sample_size: 'CnOpenData corpus: 9,595 documents (provider claim). Paper corpus size unread.'
key_variables:
- Report full text (per government-year)
- Forward-looking content tone (paper-constructed)
- Government level and jurisdiction
- Report year

research_fit:
  best_for:
  - Text-based measures of local policy tone/focus (e.g., forward-looking content, policy
    targets) for event-study or panel designs on local listed firms or local policy
  - Cross-city comparisons of annual policy language
  choose_over:
  - Choose the work-report corpus over china-gov-procurement when the research question is
    about policy language/tone, not procurement transactions.
  - For a ready-made national corpus, buy/access CnOpenData; for small samples, collect
    directly from government sites.
  not_good_for:
  - Claiming the paper's exact sentiment/tone measures without its dictionary and construction
    (unread).
  - Verifying the NBSDC dataset's content without loading its JS metadata (human browser).
  needs_join_for:
  - Firm valuation outcomes (e.g., stock returns around report disclosures; paper uses CARs)
  - City-level covariates (china-stat-yearbook family)
  variation_available:
  - Cross-government and cross-year variation in report content
  topics:
  - government work report
  - text analysis
  - policy tone
  - local government disclosure

good_for:
- policy-tone text measures
- local disclosure event studies
identification:
- Event-study around report release dates (design-dependent)
linkable_keys:
- Government level + jurisdiction (city/province names)
- Year

joins:
- target: china-gov-procurement
  relation: often-confused-with
  keys:
  - city/province
  method: distinct assets (text corpus vs transaction records); join only by jurisdiction
  evidence_status: plausible

access_routes:
- route: official government websites (raw source)
  access_status: available
  direct_url: https://wsq.gov.cn/zwgk/fdzdgknr/zfgzbg/
  requirements: none
  steps:
  - Reports are posted in 政府工作报告 disclosure columns of gov.cn and local government sites (example read: Ordos 鄂尔多斯市政府 column)
  - Collect/parse per government-year (collection is the reusable work)
  deliverable: Per-report full texts (official source)
  cost: free
  last_checked: '2026-08-15'
  caveat: Collection across thousands of government sites is the main cost; no single official national text portal evidenced this round.
- route: boundary-reference-CnOpenData-commercial-corpus
  access_status: documentation-only
  direct_url: https://www.cnopendata.com/data/m/government-corpus/chinese-government-work-report.html
  requirements: This is a distinct ready-made asset; see cnopendata-local-government-work-report-corpus for its purchase route.
  steps:
  - Switch to cnopendata-local-government-work-report-corpus when the provider corpus is the desired asset.
  - Do not equate that provider corpus with a paper's author-built text sample or tone construction.
  deliverable: Documentation boundary only; the distinct ready-made provider corpus is not delivered by this grounding record.
  cost: paid
  last_checked: '2026-08-15'
  caveat: Provider corpus identity and delivery route are now recorded separately; this record retains the unresolved self-built and paper-specific paths.
- route: NBSDC dataset (public science data center)
  access_status: needs-verification
  direct_url: https://www.nbsdc.cn/general/dataDetail?id=643fa54c87c4324301f65fe2&type=1
  requirements: Human browser (metadata is JS-loaded; automated clients get an empty shell)
  steps:
  - Open the NBSDC dataset page in a browser to read the metadata and files
  deliverable: Unverified (dataset content not read this round)
  cost: free
  last_checked: '2026-08-15'
  caveat: Found via search index for government work report data; name/content unverified.
- route: paper-full-text (paper-use verification)
  access_status: needs-verification
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/cwe.12620
  requirements: Subscription or library access (Wiley; automated clients 403)
  steps:
  - Read the CWE 2025 data section for the corpus source, period, levels and tone construction
  deliverable: Paper data-section detail; no data file
  cost: paid
  last_checked: '2026-08-15'
  caveat: Not read this round (Wiley blocked); paper use currently abstract-level.

access:
  url: https://www.cnopendata.com/data/m/government/chinese-government-work-report.html
  cost: paid (commercial corpus) / free (official sites, per report)
  license: commercial product terms (unreviewed); official reports are public documents
  format:
  - txt
  - pdf
  api: false
  how_to_get: Collect from government sites (free) or buy a ready-made corpus (CnOpenData); NBSDC route unverified.
caveats: >-
  Corpus construction (deduplication, OCR, text cleaning) is the reusable work; the paper's
  tone measure is paper-specific. The NBSDC dataset's content is unread (JS-loaded metadata).

production:
  raw_sources:
    - name: Government websites (政府工作报告 columns)
      source_type: webpage
      role: original reports
      access_route: 'official sites (example: Ordos column)'
      url: https://wsq.gov.cn/zwgk/fdzdgknr/zfgzbg/
      coverage: annual reports per government; all levels
      last_checked: '2026-08-15'
    - name: CnOpenData corpus
      source_type: dataset
      role: ready-made compiled corpus (commercial)
      access_route: product purchase
      url: https://www.cnopendata.com/data/m/government/chinese-government-work-report.html
      coverage: 2000-2025; 9,595 docs (26 central/1,097 provincial/8,472 prefecture-city)
      last_checked: '2026-08-15'
  acquisition_methods:
  - download (commercial corpus)
  - crawl (self-collection from government sites)
  sample_construction: >-
    CnOpenData: hand-compiled from official platforms (provider claim); coverage 2000-2025,
    three levels.
  pipeline_stages:
    - stage: collect
      inputs:
      - government websites / commercial corpus
      method: per-government annual collection; parse/clean texts
      tools: []
      parameters:
      output: report-level text corpus
      evidence: CnOpenData product page; official disclosure columns (2026-08-15)
    - stage: classify
      inputs:
      - report texts
      method: sentiment/tone construction (paper-specific; dictionary unread)
      tools: []
      parameters:
      output: tone measures (e.g., forward-looking content tone)
      evidence: CWE 12620 abstract (paper-specific construction unread)
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: government-year report
    structure: text corpus + paper-specific tone measures
    geography: central/provincial/prefecture
    time_span: 2000-2025 (commercial corpus claim)
    key_variables: full text; tone
    formats:
    - txt
    - pdf
  reproducibility:
    level: medium
    starting_point: official government sites (free) or CnOpenData (paid)
    code_available: false
    code_url: ''
    requirements:
    - collection/parsing effort for self-built corpus
    blockers:
    - paper's exact corpus and dictionary unread
  compliance:
    terms_or_license: reports are public official documents; commercial corpus terms unreviewed
    robots_or_rate_limits: not documented on read pages
    personal_or_sensitive_data: none
    redistribution: official texts are public; compiled corpus redistribution subject to product terms
    review_needed: false

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: abstract-only
  last_audited: '2026-08-15'

used_by:
- cite: 'Gong, Cao, Zhao & Zeng (2025), Do Local Government Disclosures Affect Firm Valuation? Evidence from Government Work Reports'
  doi: https://doi.org/10.1111/cwe.12620
  journal: China & World Economy
  year: 2025
  dataset_role: Local government work reports corpus; forward-looking content tone -> CARs of local listed firms
  evidence_type: abstract-only
  evidence_url: https://api.crossref.org/works/10.1111/cwe.12620
  data_note: >-
    Crossref abstract (read 2026-08-15): 'Using local government work reports from China...
    a positive tone in the forward-looking content increased the cumulative abnormal returns
    of local listed firms significantly'; stronger under economic policy uncertainty,
    especially private firms and firms whose executives lacked government background. Corpus
    period/levels/source and tone construction unread (Wiley 403).

provenance:
- source: https://www.cnopendata.com/data/m/government/chinese-government-work-report.html
  field_scope:
  - CnOpenData corpus coverage (2000-2025; 26 central + 1,097 provincial + 8,472 prefecture-city; 129 PDF + 8,343 TXT)
  - provider claim of hand-compilation from official platforms; commercial availability
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://wsq.gov.cn/zwgk/fdzdgknr/zfgzbg/
  field_scope:
  - work reports are publicly posted in local government disclosure columns (example page read 2026-08-15)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.nbsdc.cn/general/dataDetail?id=643fa54c87c4324301f65fe2&type=1
  field_scope:
  - existence of an NBSDC dataset page (search-index lead for government work report data; metadata JS-loaded and unread)
  added: '2026-08-15'
  confidence: low
  verified: false
- source: https://api.crossref.org/works/10.1111/cwe.12620
  field_scope:
  - paper identity and abstract (work reports, forward-looking tone, CARs)
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: cnopendata-local-government-work-report-corpus
  relation: successor
- id: china-gov-procurement
  relation: often-confused-with
---

## Positioning in one sentence

政府工作报告是各级政府每年公开发布的政策文件（政府官网信息公开栏目可见），全国性机器可读语料可通过官方站点自建（免费、收集成本高）或购买商业语料（CnOpenData 2000-2025 三层级 9,595 份）；论文（CWE 12620）用前瞻性内容语气做事件研究，其语料构造未读。

## Select rules

- 研究地方政策语气/前瞻性内容时选工作报告文本；研究采购交易时用 china-gov-procurement。
- 要现成全国语料买 CnOpenData；样本小就直接从政府站收集。
- 不要在没有读到论文词典/构造方法前声称能复现其语气指标。

## Get recipe

1. 免费路线：从 gov.cn 与各地方政府"政府工作报告"信息公开栏目逐份收集（示例：鄂尔多斯市政府栏目页）。
2. 付费路线：购买 CnOpenData 中国各地区政府工作报告数据库（2000-2025，8,343 TXT + 129 PDF）。
3. 自建语料需做去重、清洗、OCR（如遇扫描件）；NBSDC 数据集（id 643fa54c87c4324301f65fe2）内容未读，需人类浏览器核验。

## Connections and Limitations

- 连接：按政府层级+辖区+年份与上市公司事件/城市变量连接。
- 限制：论文语料周期与构造未读；NBSDC 数据集未核验；商业语料条款未审查。
- 未验证：任何语料与论文所用语料的重合度。
