---
schema_version: 3
catalog_status: ready
id: class-china-longitudinal-aging-social-survey
name: China Longitudinal Aging Social Survey (CLASS 中国老年社会追踪调查)
aka:
- CLASS
- 中国老年社会追踪调查
- 中国老年社会追踪调查评估
- RUC CLASS
provider: >-
  中国人民大学老年学研究所 (Institute of Gerontology, Renmin University of
  China) designs and implements CLASS; data distributed via RUC's 健康中国
  研究院 CLASS数据申请 route and the CNSDA archive (中国社会调查数据资料库,
  cnsda.ruc.edu.cn / cnsda.org). Verified from the official project site
  class.ruc.edu.cn (fetched 2026-08-15) and the official RUC application
  note (jkzgyjy.ruc.edu.cn, fetched+read 2026-08-15).
china_related: true
domains:
- aging
- health
- demography
- household
- social welfare
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    CLASS individual (and community) questionnaire microdata. Per the
    official RUC application note (read 2026-08-15), RUC freely opens the
    2014, 2016, 2018 and 2020 individual questionnaire data to academia;
    applicants send a purpose statement plus a signed data-use agreement to
    class_ruc@163.com and receive the data by email within about 7 working
    days after review. The class.ruc.edu.cn FAQ additionally states that
    project data can be downloaded free after registration at the CNSDA
    archive (中国国家调查数据库).
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CLASS is a national longitudinal survey of older Chinese adults
    (baseline 2014) run by RUC's Institute of Gerontology. Baseline: 28
    provinces (excluding Hainan, Tibet, Xinjiang), 134 counties/districts,
    462 communities, 11,511 valid individual questionnaires plus 462
    community questionnaires; follow-ups in 2016-17, 2018-19 and 2020-21
    maintained about 12,000 surviving elderly respondents. Free
    application-based access for academia to 2014/2016/2018/2020 individual
    data, plus a free registration-download route via CNSDA per the official
    FAQ.
  barrier: >-
    Application-gated (purpose statement + signed agreement via email).
    The delivered-file geography fields and the complete variable inventory
    still need checking against the selected wave's questionnaire/codebook.
  last_checked: '2026-09-28'

unit_of_observation: Individual older adult respondent with household context; community questionnaire per sampled community
structure: panel (longitudinal follow-up of surviving elderly; baseline 2014, follow-ups 2016-17/2018-19/2020-21)
geo_granularity:
- '134 counties/districts, 462 communities (baseline); exact geographic
  identifiers in delivered files not read'
geography: >-
  China, 28 provinces/municipalities/autonomous regions at baseline (all
  except Hainan, Tibet, Xinjiang)
time_span:
  start: '2014'
  end: '2020'
  last_confirmed_release: '2020 wave data among the freely opened waves (official RUC note)'
  coverage_note: >-
    Baseline 2014; follow-ups 2016-17, 2018-19, 2020-21. Waves freely
    opened to academia: 2014, 2016, 2018, 2020 individual questionnaire
    data (official RUC application note, read 2026-08-15).
  last_checked: '2026-08-15'
frequency:
- biennial (approximate; fieldwork windows 2016-17/2018-19/2020-21)
sample_size: >-
  Baseline: 11,511 valid individual questionnaires; 462 community
  questionnaires. Follow-ups maintain ~12,000 surviving elderly in the
  sample (official RUC note).
key_variables:
- Personal and family background of older adults
- Health status, cognition and mental health
- Economic status (income/assets) and labor/social participation
- Care resources, care needs, old-age support and retirement planning
- Intergenerational relations, social network and social isolation
- Technology use (research topics listed in the official note; exact
  variable sets per wave not read)
- 2018 internet-use frequency and loneliness, family support, friend support
  and social-participation measures used in an urban/non-urban study (not a
  substitute for checking the selected-wave questionnaire/codebook)

research_fit:
  best_for:
  - Chinese older-adult (60+) health, family support, care, cognition and
    social participation research with a longitudinal follow-up design
  - Aging-policy-related outcomes where the RUC CLASS survey family and its
    free application route matter
  choose_over:
  - Choose CLASS over charls when the RUC survey design, the 2014-2020 wave
    set, or the free email application route is preferable; compare module
    coverage before committing (CLASS is aging-social; CHARLS has biomarkers
    and health modules - verify per design).
  - Choose china-clhls for the oldest-old (80+) focused samples.
  not_good_for:
  - Adults below the older-age sample (no working-age population)
  - Biomarker/physical-measurement panels unless verified in the delivered
    files (not read this round)
  - Full-population household panels (use cfps)
  needs_join_for:
  - Community/neighborhood context (community questionnaire exists; joining
    to external administrative data requires geography fields in the
    delivered files - unread)
  variation_available:
  - Longitudinal within-person variation across follow-ups (2014-2020)
  - Geographic variation across 28 provinces at baseline
  topics:
  - aging
  - elderly health
  - care and social support
  - intergenerational relations
  - longitudinal survey

good_for:
- older-adult health and social research
- aging policy evaluation
identification:
- longitudinal follow-up comparisons
- cohort designs
linkable_keys:
- Individual respondent ID (cross-wave linkage designed as a panel)
- Community ID

joins:
- target: charls
  relation: substitute
  keys: []
  method: compare wave years, sample (older adults), modules and access before choosing; both are national aging surveys but distinct products
  evidence_status: plausible

access_routes:
- route: RUC CLASS数据申请 (email application)
  access_status: by-application
  direct_url: http://jkzgyjy.ruc.edu.cn/sjzy/CLASSsjsq/index.htm
  requirements:
  - Purpose statement (research aim, plan, data needed)
  - Signed data-use agreement provided by the data publisher (scanned with
    signature/seal)
  steps:
  - Read the official 项目简介及数据申请说明 (jkzgyjy.ruc.edu.cn/sjzy/CLASSsjsq/).
  - Send the research plan plus the signed agreement scan to class_ruc@163.com.
  - Expect the data by email within about 7 working days after approval.
  deliverable: CLASS individual questionnaire microdata for approved waves (2014/2016/2018/2020)
  cost: free
  last_checked: '2026-08-15'
  caveat: contact 010-82507289 / sphoffice@ruc.edu.cn listed on the page; the 健康中国研究院 is the current host of the CLASS data page
- route: CNSDA archive (中国社会调查数据资料库)
  access_status: by-application
  direct_url: http://cnsda.ruc.edu.cn/
  requirements: registration at CNSDA (中国国家调查数据库); per the official FAQ, register, log in, download free
  steps:
  - Register on CNSDA; locate the CLASS project pages (pilot waves 2011/2012 and main waves listed in the archive).
  - Follow the archive's download procedure (login required; formal waves and files not verified this round - the archive domain intermittently fails DNS from this environment).
  deliverable: CLASS data files via the archive (exact per-wave inventory unread)
  cost: free
  last_checked: '2026-08-15'
  caveat: cnsda.ruc.edu.cn DNS failed from this environment on 2026-08-15 (blocked, not absence); cnsda.org project pages fetched OK

access:
  url: http://jkzgyjy.ruc.edu.cn/sjzy/CLASSsjsq/index.htm
  cost: free
  license: Data-use agreement per application; academic use expected
  format:
  - microdata files (exact formats unread)
  api: false
  how_to_get: Email application route (purpose + signed agreement to class_ruc@163.com) or CNSDA registration-download route; free of charge.
caveats:
- Exact per-wave variable sets, geography fields and file formats not read this round; verify in the delivered files.
- The class.ruc.edu.cn site is a small project/evaluation subsite (2014 materials, news to 2016); the data pages moved to the 健康中国研究院 and CNSDA.
- Waves beyond 2020 not verified.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: >-
    Zhang, Burr, Mutchler & Lu (2024), Internet Use and Loneliness Among
    Urban and Non-Urban Chinese Older Adults: The Roles of Family Support,
    Friend Support, and Social Participation
  doi: https://doi.org/10.1093/geronb/gbae081
  journal: 'The Journals of Gerontology: Series B'
  year: 2024
  dataset_role: >-
    2018 CLASS cross-section used to compare urban and non-urban older adults;
    internet use, loneliness, family support, friend support and social
    participation are analysis variables.
  evidence_type: data-section
  evidence_url: https://academic.oup.com/psychsocgerontology/article/79/7/gbae081/7671273
  data_note: >-
    The public article states that it uses the 2018 CLASS wave and analyses
    10,126 older adults separately in urban (3,917) and non-urban (6,209)
    samples. This verifies use of the named 2018 measures for a
    place-differentiated aging question. It does not release the authors'
    analysis subset or establish that its urban/non-urban grouping is a
    universal field definition in every CLASS delivery.

provenance:
- source: http://class.ruc.edu.cn/ (official project site, fetched 2026-08-15)
  field_scope:
  - project identity (RUC)
  - 2014 baseline questionnaire/manual
  - 调查数据 link to CNSDA
  - 2016 press conference news
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://class.ruc.edu.cn/lxwm/FAQ.htm (official FAQ, fetched+read 2026-08-15)
  field_scope:
  - free download after CNSDA registration
  - annual data release timing questions
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://jkzgyjy.ruc.edu.cn/sjzy/CLASSsjsq/ade1ba3977354553a798c8f10221c2ad.htm (RUC 健康中国研究院 项目简介及数据申请说明, fetched+read 2026-08-15)
  field_scope:
  - RUC Institute of Gerontology design/implementation
  - baseline 2014: 28 provinces, 134 counties, 462 communities, 11,511 individual + 462 community questionnaires
  - follow-ups 2016-17/2018-19/2020-21, ~12,000 elderly maintained
  - free 2014/2016/2018/2020 individual data for academia
  - application procedure (purpose + signed agreement -> class_ruc@163.com, ~7 working days)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.cnsda.org/index.php?r=projects/view&id=41895984 (CNSDA CLASS pilot project page, fetched 2026-08-15)
  field_scope:
  - CNSDA hosts CLASS project records (2011 pilot)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://academic.oup.com/psychsocgerontology/article/79/7/gbae081/7671273 (public article page, read 2026-09-28)
  field_scope:
  - actual 2018 CLASS use in Zhang, Burr, Mutchler & Lu (2024)
  - 10,126 analytic respondents split into 3,917 urban and 6,209 non-urban older adults
  - internet use, loneliness, family support, friend support and social participation as analysis measures
  - separate boundary between a paper's analysis subset/grouping and released CLASS files
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: charls
  relation: substitute
- id: china-clhls
  relation: substitute
- id: cfps
  relation: complement
---

## Positioning in one sentence

CLASS is RUC's national longitudinal survey of older adults (baseline 2014, 11,511 respondents across 28 provinces, follow-ups through 2020-21) with a verified free application route (purpose statement + signed agreement by email) for the 2014/2016/2018/2020 individual data; an open 2024 article confirms a usable 2018 urban/non-urban analysis.

## Select rules

- Prioritize CLASS for older-adult health/social/care research where the RUC survey family and free email application route fit.
- Compare with charls (biomarkers/health modules) before choosing; compare with china-clhls for oldest-old samples.
- Not for working-age populations or biomarker designs unless verified in the delivered files.

## Get recipe

1. Read the official application note on jkzgyjy.ruc.edu.cn.
2. Send research plan + signed data-use agreement to class_ruc@163.com.
3. Expect data within ~7 working days; alternatively register at CNSDA for the download route (browser check needed - DNS flaky from some networks).

## Connections and Limitations

Panel linkage is designed across waves; geography fields per wave need checking in the delivered file before an external spatial merge. The official CLASS site itself hosts only 2014-era materials - use the 健康中国研究院 page for data. Waves beyond 2020 are unverified. The 2024 paper verifies an urban/non-urban 2018 use case, but its cleaned subset and grouping implementation are not a released CLASS deliverable.

## Decision sufficiency check

A researcher can choose the released CLASS survey family for older-adult work, request the 2014/2016/2018/2020 microdata through the verified free route, and know a concrete 2018 urban/non-urban use case. Before a fine spatial merge or a different module, inspect the approved wave's questionnaire/codebook and delivered geography fields; do not treat the paper's analysis subset as a downloadable panel.
