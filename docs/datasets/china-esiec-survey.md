---
schema_version: 3
catalog_status: ready
id: china-esiec-survey
name: PKU Enterprise Survey for Innovation and Entrepreneurship in China (ESIEC; 中国企业创新创业调查)
aka:
- ESIEC
- 中国企业创新创业调查
- Enterprise Survey for Innovation and Entrepreneurship in China
- 北大企业创新创业调查
provider: >-
  Peking University Institute of Social Science Survey (北京大学中国社会科学调查中心) core
  survey project, organized and implemented by the Center for Enterprise Research / Big Data
  Research Center of Peking University (北京大学企业大数据研究中心); general director Zhang
  Xiaobo (张晓波, NSD). Public data released through the PKU Open Research Data Platform
  (opendata.pku.edu.cn) under the China Survey Data Archive (CSDA), dataset DOI
  10.18170/DVN/DLBWAK (current API version 12.2, checked 2026-09-28).
china_related: true
domains:
- firm
- innovation
- entrepreneurship
- development
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Released ESIEC microdata files (tab/dta-style) plus questionnaires, codebooks, sampling
    plans and data-cleaning reports on the PKU Open Research Data Platform dataverse 'esiec',
    dataset 10.18170/DVN/DLBWAK. Current official API inventory (v12.2, 2026-09-28) contains 23 files:
    ESIEC2017 v0.5/v0.6 tab + codebook v0.6 + questionnaire; ESIEC2018 v0.1Beta tab +
    questionnaires v1.0/v2.0 + sampling plan; ESIEC202002/202005 (COVID rounds) sample-library
    and network versions v2.0-v3.0 + questionnaires; ESIEC2023 v1.0 tab + sampling design +
    database intro & cleaning report + questionnaire.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider identity, waves, released files and the application route are verified from the
    official PKU dataverse pages (2026-08-15/2026-09-28). ESIEC surveyed private/foreign enterprises
    registered 2010-2017 (2018 baseline in 117 counties/districts of 6 provinces, 58,500
    firms/individual businesses contacted), with 2019 topical follow-ups, two 2020 COVID
    rounds, and a 2023 wave. Files are downloadable after joining the 'ESIEC用户' user group
    (institutional email required, approval typically within one week). The public author-accepted
    manuscript of Cao, Tu & Williams (2024) verifies use of the 2018/2019 baseline plus
    ESIEC202005: after its stated restrictions and city-data merge, the paper has a balanced
    1,324-firm panel in 62 cities for 2018-2020.
  barrier: >-
    Institutional/work email (edu/org/gov.cn) required for the user-group application; CSDA
    member terms forbid redistribution, commercial use and third-party sharing; the paper's
    exact sample and variable selection are unread (Wiley paywall).

unit_of_observation: Firm (registered enterprise or individual household business) and its entrepreneur/founder
structure: repeated cross-sections with designed follow-ups (baseline 2018; 2019 topical; 2020 COVID rounds; 2023)
geo_granularity:
- firm
- county/district (sample design)
- province (6 provinces in 2018 baseline)
geography: >-
  Mainland China. 2018 baseline: Liaoning, Shanghai, Zhejiang, Henan, Guangdong, Gansu
  (6 provinces), 117 counties/districts. 2017 pre-survey: Henan (16 counties/districts).
  Not a national full-coverage sample.
time_span:
  start: '2017'
  end: '2023'
  last_confirmed_release: 'PKU Dataverse API checked 2026-09-28: released dataset version 12.2, 23 files'
  coverage_note: >-
    Publicly released data per the dataset description (2020-12-29 note): 2017 Henan
    pre-survey 1,410 completed firms; 2020 first COVID round 2,513 sample-library + 376
    network completions; 2020 follow-up 2,508 sample-library + 63 network. 2018 baseline
    contacted 58,500 (v0.1Beta released); 2023 wave v1.0 released with cleaning report.
  last_checked: '2026-09-28'
frequency:
- multi-wave (2017/2018/2019/2020/2023; not annual for all modules)
sample_size: >-
  2018 baseline: 58,500 contacted in 117 counties/districts (6 provinces); 2017 Henan
  pre-survey: 6,400 contacted / 1,410 completed; 2020 rounds: ~2,500-2,600 sample-library
  completions per round; released-file sample sizes not read from the data files themselves.
key_variables:
- Entrepreneur's entrepreneurial history
- Enterprise creation process and basic information
- Enterprise innovation
- Inter-firm relationships and business environment
- COVID shock: survival status, operations (2020 rounds)
- Firm/entrepreneur identifiers enabling follow-up linkage (subject to terms)

research_fit:
  best_for:
  - SME/entrepreneur-level research on innovation, entrepreneurship, business environment and
    COVID survival where a survey microdata file (not a registry) is the right unit
  - Comparing firm-side modules with the same cohort across the 2018 baseline and 2020 COVID waves
  choose_over:
  - Choose ESIEC over ASIF/china-firm-registry when the question needs entrepreneur history,
    innovation behavior and COVID survival outcomes rather than financial-statement/registration fields.
  - Choose over CFPS/CHFS when the unit is the firm/entrepreneur, not the household.
  not_good_for:
  - Nationally representative full-coverage firm census (only 6 provinces in the baseline).
  - Annual firm panel with full balance-sheet coverage (waves are survey rounds, not annual accounts).
  needs_join_for:
  - Firm registry or financial variables (china-firm-registry, china-tianyancha-firm-information, ASIF)
  - Local/regional controls (china-stat-yearbook family)
  variation_available:
  - Cross-province/county sample variation and multi-wave firm follow-up; the documented
    Cao, Tu & Williams paper combines 2018/2019 baseline responses with ESIEC202005
  topics:
  - entrepreneurship
  - SME
  - innovation
  - COVID shock
  - business environment

good_for:
- SME survival and e-commerce adoption (COVID)
- entrepreneurship and innovation microdata
identification:
- Direct survey microdata: released ESIEC firm/entrepreneur survey files and their wave-specific documentation; they are distinct from a firm registry, a national enterprise census, and the paper's restricted analysis subset.
linkable_keys:
- Firm identifiers (survey-defined; linkage to registries subject to terms)

joins:
- target: china-firm-registry
  relation: complement
  keys:
  - firm name / registration identifiers
  method: match released ESIEC firm identifiers to registry records under the CSDA terms; not verified on the files
  evidence_status: plausible

access_routes:
- route: PKU Open Research Data Platform dataverse (official)
  access_status: available-with-registration
  direct_url: https://opendata.pku.edu.cn/dataverse/esiec
  requirements:
  - Register an account on opendata.pku.edu.cn
  - Apply to join the 'ESIEC用户' user group; only institutional/work emails (edu/org/gov.cn) are accepted
  - Accept the CSDA member terms (no redistribution, no commercial use, citation required, no third-party sharing, destroy files after membership ends)
  steps:
  - Open the ESIEC dataverse (dataset 10.18170/DVN/DLBWAK)
  - Click 申请 (apply) on the ESIEC用户 user group row
  - Wait for approval (stated: generally within one week)
  - Download the released tab/questionnaire/codebook files
  deliverable: ESIEC released microdata (2017/2018/2020/2023 waves as listed on the dataset page), questionnaires, codebooks, sampling plans, cleaning report
  cost: registration
  last_checked: '2026-09-28'
  caveat: The official API confirms a released V12.2 inventory of 23 named files, but it does not replace the platform's user-group/CSDA terms. Group-level access remains the documented route; the paper-specific analysis sample is not identified by this inventory.
- route: paper-full-text (paper-use verification)
  access_status: needs-verification
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/cwe.12550
  requirements: Subscription or library access (Wiley; automated clients 403)
  steps:
  - Read the CWE 2024 data section for the exact ESIEC waves, sample restrictions and variables used
  deliverable: Paper data-section detail; no data file
  cost: paid
  last_checked: '2026-09-28'
  caveat: >-
    The publisher page was not used for this check, but an author-accepted manuscript is openly
    available through Sheffield Hallam University's repository. It verifies the 2018/2019 baseline
    and ESIEC202005 use and the paper's 1,324-firm analytic panel; it does not make that cleaned
    panel, its merge inputs, or the exact author code a released ESIEC deliverable.

access:
  url: https://opendata.pku.edu.cn/dataverse/esiec
  cost: by-application
  license: CSDA member terms (research use; no redistribution/commercial use)
  format:
  - tab
  - pdf
  - doc
  api: true
  how_to_get: >-
    Register at opendata.pku.edu.cn, apply to join the 'ESIEC用户' user group with an
    institutional email, accept the CSDA terms, then download the released files.
caveats: >-
  The 2018 baseline file is released as v0.1Beta; versions update frequently (dataset V12 as
  of 2026-05-13). Released files do not include the full 2019 topical survey (only 2017, 2018,
  2020 and 2023 files are listed on the dataset page). Sample-frame and completion numbers are
  from the provider description, not from the data files.

production:
  raw_sources:
    - name: ESIEC field surveys (PKU Center for Enterprise Research)
      source_type: other
      role: the survey itself; files released through the platform
      access_route: official dataverse (see access_routes)
      url: https://opendata.pku.edu.cn/dataverse/esiec
      coverage: 2017 Henan pre-survey; 2018 baseline (6 provinces, 117 counties); 2019 topical; 2020 COVID rounds; 2023
  last_checked: '2026-09-28'
  acquisition_methods:
  - download (approved user group)
  sample_construction: >-
    Provider-documented: 2018 baseline sampled private and foreign-owned enterprises
    registered 2010-2017 in 6 provinces (58,500 contacted in 117 counties/districts); 2019
    targeted non-completed 2018 firms plus hi-tech-park supplements
    (Beijing/Shanghai/Shenzhen); 2020 rounds followed 2017/2018/2019 completed samples
    (~8,750 firms) plus network questionnaires.
  pipeline_stages:
    - stage: collect
      inputs:
      - field survey
      method: provider-conducted sampling and field tracking
      tools: []
      parameters:
      output: released tab/questionnaire/codebook files
      evidence: PKU dataverse dataset description (2026-08-15)
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: firm/entrepreneur
    structure: multi-wave survey files
    geography: 6 provinces (2018 baseline) / Henan (2017) + supplements
    time_span: 2017-2023
    key_variables: innovation, entrepreneurship history, business environment, COVID survival
    formats:
    - tab
  reproducibility:
    level: needs-verification
    starting_point: approved download of released files
    code_available: false
    code_url: ''
    requirements:
    - approved user-group access (institutional email)
    blockers:
    - restricted files; paper's exact sample unread
  compliance:
    terms_or_license: CSDA member rules (platform page, read 2026-08-15)
    robots_or_rate_limits: not documented on the read pages
    personal_or_sensitive_data: firm-level; respondent privacy protected per terms (no re-identification)
    redistribution: prohibited
    review_needed: group approval

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Cao, Tu & Williams (2024), E-commerce, Pandemic Shock, and the Survival of Small and Medium Enterprises'
  doi: https://doi.org/10.1111/cwe.12550
  journal: China & World Economy
  year: 2024
  dataset_role: Combined ESIEC 2018-2020 dataset; DID on e-commerce adoption before/after COVID for SME survival
  evidence_type: author_accepted_manuscript
  evidence_url: https://shura.shu.ac.uk/34259/1/Williams-E-CommercePandemicShock%28AM%29.pdf
  data_note: >-
    The openly archived author-accepted manuscript identifies the 2018 ESIEC baseline (6,199
    firms) plus the 2019 survey of 429 firms missed in 2018, then two 2020 special surveys.
    It chooses the May 2020 ESIEC202005 wave (2,508 responses), matches it to baseline records,
    retains incorporated firms because only they were asked about e-commerce, merges city-level
    data by address, and reports a balanced 1,324-SME panel in 62 cities for 2018-2020. It also
    states that ESIEC202005 contains closure timing, orders, cash-flow and accounts-receivable
    questions. This verifies the paper's actual data use, not release of its cleaned analytic panel.

provenance:
- source: https://opendata.pku.edu.cn/dataverse/esiec
  field_scope:
  - ESIEC identity, organizer (Center for Enterprise Research, PKU), general director (Zhang Xiaobo)
  - pre-surveys 2016-2017, 2018 baseline sample frame, 2019 topical, 2020 COVID rounds, released-data note 2020-12-29
  - user-group application rules (institutional email, one-week approval)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://opendata.pku.edu.cn/dataset.xhtml?persistentId=doi:10.18170/DVN/DLBWAK
  field_scope:
  - dataset DOI, version 12, modification date 2026-05-13, download count
  - released file list (ESIEC2017/2018/2020/2023 files, questionnaires, codebooks, sampling plans)
  - CSDA terms text (download popup) and request-access flow
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.crossref.org/works/10.1111/cwe.12550
  field_scope:
  - paper identity and abstract (ESIEC 2018-2020 use, DID design, survival results)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://shura.shu.ac.uk/34259/1/Williams-E-CommercePandemicShock%28AM%29.pdf (author-accepted manuscript, read 2026-09-28)
  field_scope:
  - actual ESIEC 2018/2019 baseline and ESIEC202005 use
  - baseline and follow-up response counts stated by the paper
  - firm restriction, address-based city merge, and 1,324-firm/62-city/2018-2020 analytic-panel construction
  - ESIEC202005 survival, operations, orders, cash-flow and accounts-receivable measures stated by the paper
  - separate unreleased-author-panel boundary
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://opendata.pku.edu.cn/api/datasets/:persistentId/?persistentId=doi:10.18170/DVN/DLBWAK
  field_scope:
  - current released version 12.2 and 23-file inventory
  - 2017, 2018, 2020 February/May, and 2023 released file names
  - official baseline population, 2010-2017 registration frame, and six-province/117-county design description
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: cfps
  relation: often-confused-with
- id: china-firm-registry
  relation: complement
---

## Positioning in one sentence

ESIEC 是北京大学企业大数据研究中心实施的创新创业企业调查，公开数据经北大开放研究数据平台（CSDA 下，DOI 10.18170/DVN/DLBWAK）按用户组申请发放；它提供企业+创业者层面的创新、创业史、营商环境与疫情冲击微观数据，但基线仅覆盖 6 省 117 县（市、区），不是全国全覆盖企业普查。

## Select rules

- 当研究问题需要企业/创业者层面的创新行为、创业史、营商环境感知或疫情下 SME 生存状态时，选 ESIEC（2018 基线 + 2020 疫情两轮 + 2023 波次已发布）。
- 需要全量财务/注册信息时改用 ASIF 或 china-firm-registry；需要家庭单元时改用 CFPS/CHFS。
- 论文使用证据目前只有摘要级（CWE 12550 用 ESIEC 2018-2020 做电商采纳×疫情 DID）；论文确切样本与变量未读。

## Get recipe

1. 在 opendata.pku.edu.cn 注册，进入 ESIEC dataverse（数据集 10.18170/DVN/DLBWAK，当前 V12）。
2. 申请加入"ESIEC用户"用户组——平台明确只接受机构/工作邮箱（edu/org/gov.cn），一般一周内审批；不接受单文件申请。
3. 接受 CSDA 会员条款（不得再分发、不得商用、引用规范、退出后销毁数据）后下载已发布的 tab/问卷/编码手册/抽样方案/清理报告。
4. 使用前核对文件版本（如 ESIEC2018 为 v0.1Beta）与各波次样本定义；如需论文同款样本，读 Wiley 全文数据章节（需订阅）。

## Connections and Limitations

- 连接：企业层面标识可与 registry/天眼查类数据做名称/标识匹配，但受 CSDA 条款约束（不得分享给第三方）；匹配方法未在本轮验证。
- 限制：2018 基线只在辽宁、上海、浙江、河南、广东、甘肃 6 省；2019 专题调查未出现在公开文件列表；发布文件不含全部波次；论文用到的确切波次组合与样本限制未读（Wiley 403）。
- 未验证：数据文件内部字段与行数（本轮只读平台页面）；申请审批的实际流程时间。
