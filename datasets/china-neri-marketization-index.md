---
schema_version: 3
catalog_status: ready
id: china-neri-marketization-index
name: NERI Marketization Index of China's Provinces (中国分省份市场化指数)
aka:
- Fan-Wang marketization index
- 樊纲市场化指数
- 中国分省份市场化指数
- 中国市场化指数
- 中国分省份市场化指数报告
- 分省份市场化指数数据库
- China Marketization Index
provider: 国民经济研究所 (National Economic Research Institute, NERI; Beijing), long-running project led by Fan Gang (樊纲) and Wang Xiaolu (王小鲁); report volumes published by 社会科学文献出版社 (2021 edition) and 中国经济出版社 (2024 edition); machine-readable database hosted by 社会科学文献出版社 (SSAP) at cmi.ssap.com.cn
china_related: true
domains:
- institutional
- regional
- development
- macro
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Province-year marketization index scores for China's 31 province-level units:
    a total index plus five aspect indices and their sub-indices (first-level and
    basic indices), with scores and rankings per edition. Delivered as printed
    report volumes or as read-only tables in the SSAP subscription database; no
    free public data file was found.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The NERI marketization index is the standard Chinese province-level institutional
    environment measure: an index system created in 2000 by the National Economic
    Research Institute (Fan Gang, Wang Xiaolu et al.), covering 31 provinces with
    annual data 1997-2023 (as of the 2024 report). A researcher obtains values from
    the printed reports or the read-only cmi.ssap.com.cn database through a library
    subscription; there is no public free download of the underlying tables.
  barrier: >-
    The current database (cmi.ssap.com.cn) is read-only for subscribers (no download
    permission per a 2026 library trial notice), and the exact edition/revision used
    by a given paper must be checked because the index structure was revised between
    editions (e.g., 17 vs 18 basic indices).

unit_of_observation: 'Province-year (31 provincial-level units: provinces, autonomous regions, municipalities)'
structure: Panel of annual index scores, issued in irregular report editions with occasional structural revisions
geo_granularity:
- province
geography: 31 province-level units of mainland China (provinces, autonomous regions, municipalities)
time_span:
  start: 1997
  end: 2023
  last_confirmed_release: '2025'
  coverage_note: >-
    Index system created in 2000; 27 years of annual data accumulated as of the 2024
    report, whose annual data extend through 2023. The 2021 report volume covers
    earlier years; the cmi.ssap.com.cn database is described (2026 library trial
    notice) as covering 1997-2023.
  last_checked: '2026-09-28'
frequency:
- annual
sample_size: '31 provinces x 27 annual observations (1997-2023) per index component; exact matrix size per edition not verified'
key_variables:
- Total marketization index (市场化总指数)
- Five aspect indices: government-market relations; development of non-state economy; development of product markets; development of factor markets; development of market intermediaries and legal environment (政府与市场的关系; 非国有经济的发展; 产品市场的发育程度; 要素市场的发育程度; 市场中介组织的发育和法治环境)
- First-level and basic sub-indices below each aspect index (14 first-level / 18 basic indices per the 2026 database notice; 15 first-level / 17 basic indices per the 2021 report revision - structure changed between editions, exact current composition unverified)
- Province rankings per year

research_fit:
  best_for:
  - Provincial-level institutional environment controls or marketization-growth analyses where a widely recognized, ready-made composite index is needed
  - Stylized facts on China's market-oriented reform progress by province and year
  choose_over:
  - Choose NERI over ad-hoc institutional proxies (e.g., share of SOE output) when comparability across provinces and years matters and a published, citable index is preferred.
  - Compare with the NERI 分省企业经营环境指数 (business environment index, also Wang Xiaolu et al.) when the research question is about the firm-operating environment rather than general marketization.
  not_good_for:
  - Sub-provincial geography: no official county/city-level NERI marketization scores exist.
  - Firm-level institutional measurement; the index is province-level only.
  - A continuous long panel without vintage care: editions revise earlier years' scores, so mixing editions without checking the vintage breaks comparability.
  needs_join_for:
  - City/county-level institutional variation: requires other constructed measures (e.g., 营商环境 indices) because NERI stops at province level.
  - Macro policy treatments: join provincial policy timing and other province-year controls.
  variation_available:
  - Panel variation across 31 provinces and 27 years of scores; revisions across editions are a known vintage issue, not an identification device.
  topics:
  - marketization
  - institutions
  - provincial index
  - economic reform
  - institutional environment

good_for:
- Province-year institutional controls in provincial panels (e.g., system GMM growth regressions)
- Describing the relative speed of market-oriented reform across provinces over 1997-2023
identification:
- >-
  Data-side variation is observed across province-years in the total score and the
  five reported marketization areas. The open 2019 use case directly verifies this
  structure for 31 mainland province-level regions in 2008-2014; it is a measurement
  dimension, not a policy treatment or a causal-design claim.
- >-
  A paper may form an analytic transformation from the delivered areas (for example,
  the 2019 study excludes the ownership-structure area). That transformation belongs
  to the paper, whereas the released report/database supplies the original total and
  component scores. Index-vintage revisions are a comparability limitation, not an
  additional source of usable within-panel variation.
linkable_keys:
- Province name / administrative code (province level)

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province code
  - Year
  method: Merge province-year index scores onto province-year macro data by standard province codes; confirm the index edition's year alignment before merging.
  evidence_status: plausible

access_routes:
- route: cmi.ssap.com.cn database (SSAP subscription)
  access_status: available-with-conditions
  direct_url: https://cmi.ssap.com.cn/
  requirements:
  - Institutional subscription (library trial model documented 2026-05-19 to 2026-08-31 at one university library)
  - On-campus IP or institutional authentication; account-based
  steps:
  - Check whether the institution subscribes to 中国分省份市场化指数数据库 (cmi.ssap.com.cn).
  - Open the database and navigate to the province-year score tables.
  - Note that the platform is read-only: no download permission (per the 2026 library trial notice), so values must be transcribed or used in-platform.
  deliverable: Online read-only tables of total index, aspect indices, and sub-indices with rankings, 1997-2023
  cost: by-application
  last_checked: '2026-09-28'
  caveat: The current public endpoint returned HTTP 200 on 2026-09-28 and identifies itself as 中国分省份市场化指数数据库, but it remains a JavaScript application shell rather than public table content. A human browser with institutional access is still needed to verify the delivered tables and current download/export terms.
- route: printed report volumes
  access_status: available
  direct_url: https://www.pishu.com.cn/skwx_ps/ps/bookdetail?SiteID=14&ID=12896275
  requirements: Purchase or library holdings of the report volumes
  steps:
  - Obtain 《中国分省份市场化指数报告（2021）》(王小鲁, 胡李鹏, 樊纲; 社会科学文献出版社 2021-09) for the pre-2020 era, or
  - Obtain 《中国分省份市场化指数报告（2024）》(王小鲁, 樊纲, 李爱莉; 中国经济出版社, annual data through 2023) for the latest available values.
  - Use the appendix chapter (构造和计算方法) to confirm the index structure of the edition being used.
  deliverable: Printed tables and methodology chapters per edition
  cost: paid
  last_checked: '2026-08-15'
  caveat: Editions revise the index structure and historical values; always record which report edition and data vintage a study used.
- route: CNKI 心可书馆 online reading of the 2021 volume
  access_status: available-with-conditions
  direct_url: https://thinker.cnki.net/bookStore/Book/bookdetail?bookcode=9787520188913000&type=book
  requirements: CNKI institutional account
  steps:
  - Search the book by ISBN 9787520188913000 (2021 report) on 心可书馆.
  - Read chapters online; export restrictions apply per CNKI terms.
  deliverable: Online reading access to the 2021 volume
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Online reading only; no dataset download implied.

access:
  url: https://cmi.ssap.com.cn/
  cost: by-application
  license: Database access per SSAP subscription terms; printed reports under publisher copyright; academic citation expected
  format:
  - printed tables
  - online tables (read-only)
  api: false
  how_to_get: Check institutional subscription to cmi.ssap.com.cn, or purchase the latest report volume (2024 edition for data through 2023); no free public data file was found.
caveats:
- 'The index is a constructed composite; editions revise the structure (2021 revision: 15 first-level / 17 basic indices; 2026 database notice: 14 first-level / 18 basic indices) and historical scores, so the edition-vintage used by a paper must be verified.'
- Province-level only; do not use as a county/city institutional measure.
- The motivating CER paper (Nonlinearities in the institutions-growth relationship, 10.1016/j.chieco.2025.102583) is ScienceDirect-blocked here; the exact edition it used is unverified.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: "Zhou & Hall (2019), The Impact of Marketization on Entrepreneurship in China: Recent Evidence"
  journal: American Journal of Entrepreneurship
  year: 2019
  dataset_role: >-
    Province-year total marketization index and five NERI area indices; the authors
    also construct a paper-specific modified index that omits the ownership-structure
    area.
  evidence_type: full-text
  evidence_url: https://americanjournalentrepreneurship.org/wp-content/uploads/2020/07/Zhou-Hall-2019.pdf
  data_note: >-
    The open article's data section identifies Fan et al.'s 2016 NERI report as the
    source of annual scores for 31 mainland province-level regions in 2008-2014
    (217 province-years). It says that the report supplies the total index and five
    areas, and that comparability across older report vintages is not assumed. Its
    modified four-area index is the authors' own analytic transformation, not a
    separate NERI delivery.
- cite: "CER 2025 (China Economic Review 94, 10.1016/j.chieco.2025.102583), Nonlinearities in the institutions-growth relationship in a dynamic panel data framework: Evidence from China's provinces"
  doi: https://doi.org/10.1016/j.chieco.2025.102583
  journal: China Economic Review
  year: 2025
  dataset_role: Main explanatory institutional variable (Fan et al. NERI marketization index) in provincial system-GMM growth regressions
  evidence_type: abstract-only
  evidence_url: https://econpapers.repec.org/article/eeechieco/v_3a94_3ay_3a2025_3ai_3ac_3as1043951x25000607.htm
  data_note: >-
    The abstract names 'Fan et al.'s NERI marketization index' as the institutional
    measure; the exact report edition and years used are unverified because the full
    text is ScienceDirect-gated for automated clients.

provenance:
- source: pishu.com.cn 皮书数据库 chapter page 市场化指数的构造和计算方法（2021年修订） (contentId 12896292)
  field_scope:
  - index system created 2000
  - 31 provinces measured
  - structure: total index + 5 aspect indices + 15 first-level + 17 basic indices in the 2021 revision
  - authors Wang Xiaolu, Hu Lipeng, Fan Gang; NERI affiliations
  added: '2026-08-15'
  confidence: high
  verified: true
- source: neri.org.cn official homepage (National Economic Research Institute) publications list
  field_scope:
  - producer identity (NERI; Fan Gang director, Wang Xiaolu deputy director)
  - report series including 2018, 2021, 2024 editions
  added: '2026-08-15'
  confidence: high
  verified: true
- source: 163.com 财经智库 article 市场化在路上——中国分省份市场化指数新报告 (2025-05-30)
  field_scope:
  - 2024 report by Wang Xiaolu, Fan Gang, Li Aili published by 中国经济出版社
  - annual data through 2023; 27 years of annual data; 10 reports published; project since 2000
  - five aspect indices named; objective data-based construction, no expert subjective scoring
  added: '2026-08-15'
  confidence: med
  verified: false
- source: Zhejiang Gongshang University Library trial notice 中国分省份市场化指数数据库 (lib.zjgsu.edu.cn 2026-05-21)
  field_scope:
  - cmi.ssap.com.cn platform identity and trial period 2026-05-19 to 2026-08-31
  - database coverage 1997-2023, 31 provinces, scores and rankings
  - current structure: 5 aspect indices, 14 first-level sub-indices, 18 basic indices
  - read-only access, no download permission
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://cmi.ssap.com.cn/ (HTTP 200 public application shell, checked 2026-09-28)
  field_scope:
  - current database endpoint remains live
  - public site identity as 中国分省份市场化指数数据库
  - JavaScript-shell boundary; no public table or export claim
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Zhou & Hall (2019), open full text at American Journal of Entrepreneurship
  field_scope:
  - actual use of 2016 NERI report total index and five area indices
  - 31 mainland province-level regions, annual 2008-2014, 217 province-years
  - report-vintage comparability boundary and paper-specific four-area transformation
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-stat-yearbook
  relation: complement
- id: china-io-table
  relation: complement
---

## Positioning in one sentence

The NERI marketization index is China's standard province-level institutional-environment measure: a composite index system created in 2000 by the National Economic Research Institute (Fan Gang, Wang Xiaolu et al.), covering 31 provinces with annual data 1997-2023 across five aspect indices. A researcher obtains values from printed report volumes (latest: 2024 edition, data through 2023) or the read-only cmi.ssap.com.cn database via library subscription; there is no free public data file.

## Select rules

- Prioritize it as a ready-made, citable province-level marketization control in provincial panels.
- Switch to 分省企业经营环境指数 when the question concerns the firm-operating environment, and to sub-provincial constructed measures when province-level is too coarse.
- Do not use it for county/city institutional variation, and always record which report edition (vintage) the values come from, because editions revise structure and historical scores.

## Get recipe

1. Identify the target years; if 1997-2019 values suffice, the 2021 report (社科文献出版社) covers them; for data through 2023 use the 2024 report (中国经济出版社).
2. Check institutional access to cmi.ssap.com.cn (中国分省份市场化指数数据库) — the database is read-only per the 2026 library trial notice, so plan to transcribe or use in-platform values.
3. Record the edition and revision used; verify the current structure claims (5 aspects; 14 first-level / 18 basic indices per the 2026 database notice vs 15 first-level / 17 basic indices per the 2021 report) against the edition's own 构造和计算方法 chapter.

## Connections and Limitations

Province-year index scores merge cleanly onto province-year macro data via province codes. The key limitations are the province-only granularity, the absence of a free downloadable file, and edition-to-edition revisions of historical scores, so the exact vintage a paper used must always be verified before reusing its reported values.
