---
schema_version: 3
catalog_status: grounding
id: china-2017-fertility-survey
name: 2017 China Fertility Survey (2017年全国生育状况抽样调查)
aka:
- 2017年全国生育状况抽样调查
- 2017 National Fertility Survey
- 2017 China Fertility Survey
- 全国生育状况抽样调查
provider: >-
  国家卫生计生委 (NHFPC, the predecessor of today's National Health Commission,
  NHC) with provincial health and family-planning commissions; official results
  and analyses released through the 中国人口与发展研究中心 (China Population and
  Development Research Center, CPDRC) and journal reports
china_related: true
domains:
- health
- demography
- fertility
- population
- regional

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    Restricted national survey microdata on ~250,000 women aged 15-60 (2017
    cross-section); no public microdata file or application channel was found -
    published outputs are official reports and journal analyses built from
    approved extracts.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    A one-off nationally representative survey of fertility behavior and
    intentions, fielded in July 2017 by the NHFPC (NHC) in all 31 mainland
    provinces plus the Xinjiang Production and Construction Corps, targeting
    about 250,000 Chinese women aged 15-60 with a stratified three-stage PPS
    design and CAPI face-to-face interviews. The microdata are not publicly
    released; researchers encounter the survey through official reports and
    journal papers that obtained extracts through approved channels.
  barrier: >-
    No public microdata release or application route was found in any checked
    source (official notice pages, provincial implementation plans, results
    pages, news reports, journal articles). Access appears to depend on a
    controlled NHC/CPDRC arrangement, which is not documented as a general
    public application.

unit_of_observation: Woman aged 15-60 (Chinese nationality, resident in mainland China or the Xinjiang Production and Construction Corps at 2017-07-01 00:00); village-committee questionnaire at sampled communities
structure: One-off national sample survey (cross-section), stratified three-stage PPS
geo_granularity:
- individual (woman)
- village/community (second stage)
- township/street (first stage)
- province
geography: All 31 mainland provinces, autonomous regions and municipalities plus the Xinjiang Production and Construction Corps; Heilongjiang plan states its own coverage as 16 prefecture units, 110 county units, 400 village sample points
time_span:
  start: 2017
  end: 2017
  last_confirmed_release: 2017
  coverage_note: >-
    Reference population defined at 2017-07-01; fieldwork July 2017 (first-stage
    sampling May 2017; training June 2017; data cleaning, weighting and report
    drafting August-December 2017 per the Heilongjiang implementation plan).
    Results released 2018-08 via CPDRC.
  last_checked: '2026-08-15'
frequency:
- one-off
sample_size: 'Nationally about 250,000 women (~25万); Heilongjiang province quota about 8,000. About 15,000 enumerators/supervisors trained nationally. An 8-province minority-area subsample used in a 人口研究 2019 analysis had 45,998 valid cases.'
key_variables:
- Personal information (age, hukou, education, marriage)
- Fertility behavior (births, timing, spacing)
- Fertility and child-rearing services (birth/rearing services and policies)
- Fertility intention
- Family information
- Village questionnaire: basic conditions and related service management
- Detailed retrospective pregnancy and live-birth dates for 2012-2017, desired fertility, and planned births for 2018 onward (confirmed in Fang, Liu & Yang's public JDE final paper)
- Demographic and socioeconomic fields including ethnicity, marital status, education, hukou, siblings, employment, occupation and 2016 income; comparable spouse/cohabitant characteristics except fertility desires (same source)

research_fit:
  best_for:
  - Nationally representative descriptive facts on Chinese fertility behavior and intentions circa 2017 (e.g., the 贺丹 2019 report on 2006-2016 fertility trends, 人口研究)
  - Analyses of the Universal Two-Child Policy's short-run birth response using the survey's retrospective birth histories (as in Fang & Liu 2026 JDE)
  - Fertility-intention research across all provinces (the plan notes intention is representative at national and provincial level)
  choose_over:
  - Choose this survey over CMDS when the question needs nationally representative fertility behavior/intentions of the general female population rather than migrants; CMDS remains the migrant-focused NHC survey.
  - Choose census or mini-census data when only fertility outcomes (not intentions/services) are needed with full national coverage.
  not_good_for:
  - Panel or longitudinal analysis: the survey is a single cross-section.
  - Microdata-level analysis by ordinary researchers: no public microdata route exists.
  - Post-2017 fertility: the survey measures the 2017 state of affairs (with retrospective history).
  needs_join_for:
  - County- or city-level outcomes require geographic identifiers that only exist in approved extracts (unverified).
  - Policy timing (e.g., Universal Two-Child Policy) must come from a separate policy record; this record only describes the data product.
  variation_available:
  - Cross-sectional comparisons across age cohorts, provinces, hukou and parity groups; the survey itself is not a panel.
  topics:
  - fertility
  - birth policy
  - fertility intention
  - population policy
  - women's health services

good_for:
- National fertility-level and intention benchmarks around 2016-2017
- Universal Two-Child Policy short-run response analysis (birth histories)
identification: []
linkable_keys:
- Province and sampling-unit identifiers only within approved extracts (unverified)
- No public record-level identifiers

joins:
- target: china-census
  relation: complement
  keys:
  - Province
  - Year
  method: Use census aggregates for population denominators and long-run fertility outcomes; the survey adds intentions and services not in the census.
  evidence_status: plausible
- target: cmds
  relation: complement
  keys:
  - Province
  - Year
  method: CMDS is the NHC migrant-focused survey; compare sampling frames before any combined use.
  evidence_status: plausible

access_routes:
- route: report-only
  access_status: documentation-only
  direct_url: https://www.cpdrc.org.cn/yjdt/yjbg/2017/201808/t20180810_2586.html
  requirements:
  - No public application form found; microdata are not released
  steps:
  - Read the official NHC notice 国卫指导函[2017]183号 (nhc.gov.cn, 412 anti-bot for automated clients) and the CPDRC results page (2018-08; TLS-unreachable in this environment) for the official framing.
  - Use published reports and journal analyses (e.g., 贺丹 2019 人口研究; 原新 et al. 2019 人口研究) as the public research outputs.
  - For microdata, contact the responsible institution (NHC population monitoring or CPDRC) only if a controlled research arrangement is plausible; this route is undocumented.
  deliverable: Official reports and journal analyses; no microdata file
  cost: free
  last_checked: '2026-08-15'
  caveat: All official pages (nhc.gov.cn notice, cpdrc.org.cn results, jkfpsj.org.cn copy) were blocked for automated clients in this environment; URL/title-level identity is grounded, page text was not read except through provincial reposts.
- route: journal-extract (documented paper use)
  access_status: documentation-only
  direct_url: https://doi.org/10.1016/j.jdeveco.2026.103796
  requirements:
  - Access to the paper's own data arrangement (how Fang & Liu obtained the survey is unverified; ScienceDirect 403 for automated clients, article is hybrid OA and browser-readable)
  steps:
  - Read the JDE 2026 article's data section in a human browser to learn the survey extract, sample, and access terms used by the authors.
  deliverable: Documentation of an approved-extract use; not a public route
  cost: by-application
  last_checked: '2026-09-28'
  caveat: >-
    The authors' public final JDE paper documents their survey extract and reports that they do
    not have permission to share the data. This closes paper use and confirms non-release, but it
    does not document a general NHC/CPDRC application channel.

access:
  url: https://www.nhc.gov.cn/jczds/s3582r/201706/33d71625e4874e1d9277ec3aeb26a949.shtml
  cost: unknown
  license: Not established; no public release terms found
  format:
  - unknown
  api: false
  how_to_get: No public route exists. Use published reports and journal analyses; treat microdata as restricted pending a documented NHC/CPDRC arrangement.
caveats:
- The total sample (~250,000) is confirmed by the provincial official implementation plan (which quotes the national notice) and the 中国人口报 launch report; the national notice page itself was not readable in this environment.
- No microdata release, application form, or data-use agreement is documented in any checked source; do not promise access.
- The survey is a 2017 cross-section; retrospective birth histories support short-run policy response analysis but not panel designs.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Fang, Hanming & Liu, Chang (2026), Desired fertility, realized fertility and the effects of China''s Universal Two-Child Policy, JDE 182, 10.1016/j.jdeveco.2026.103796'
  doi: https://doi.org/10.1016/j.jdeveco.2026.103796
  journal: Journal of Development Economics
  year: 2026
  dataset_role: Main outcome data (nationally representative 2017 China Fertility Survey)
  evidence_type: published-paper-full-text
  evidence_url: https://bpb-us-w2.wpmucdn.com/web.sas.upenn.edu/dist/3/517/files/2026/04/JDE-print-main.pdf
  data_note: >-
    Public final JDE paper read 2026-09-28: the CFS was conducted by the NHFPC
    in mid-2017, covers 249,946 women aged 15-60 in 2,737 counties of 31
    provinces through three-stage stratified sampling, and supplies demographics,
    fertility histories, desired fertility and planned births. The paper's data-
    availability statement says the authors do not have permission to share data.
- cite: '原新, 刘厚莲, 金牛 (2019), 2006~2016年少数民族省区生育水平研究, 人口研究 43(1)'
  doi: null
  journal: 人口研究 (Population Research)
  year: 2019
  dataset_role: Main outcome microdata (8 minority provinces subsample of the 2017 survey; 45,998 valid cases)
  evidence_type: data-section
  evidence_url: http://rkyj.ruc.edu.cn
  data_note: >-
    Full text read 2026-08-15 on a sohu republication (cached in scratch): the
    article uses the 2017 survey's minority-province subsample (8 provinces,
    45,998 valid cases) and confirms the survey design (implemented by 原国家卫生
    计生委, females aged 15-60, stratified three-stage PPS, 31 provinces).

provenance:
- source: 黑龙江省卫生计生委实施方案 (黑卫指导规发[2017]20号, 2017-06-13, full text via pharnexcloud.com repost)
  field_scope:
  - target population (15-60 Chinese women resident in 31 provinces + XPCC at 2017-07-01)
  - national sample size ~250,000; Heilongjiang ~8,000
  - stratified three-stage PPS sampling (township/street, village committee, woman)
  - questionnaire modules (personal + village) and CAPI fieldwork
  - data processing timeline (weighting, reports, August-December 2017)
  - reference to the national notice 国卫指导函[2017]183号
  added: '2026-08-15'
  confidence: high
  verified: true
- source: 中国人口报 report of the 2017-06-01 launch meeting (reposted by 福建省计划生育协会, fjfpa.org.cn, read directly)
  field_scope:
  - launch meeting 2017-06-01, 国家卫生计生委
  - sample scale ~250,000; ~15,000 enumerators/supervisors trained
  - survey objectives and questionnaire scope
  added: '2026-08-15'
  confidence: high
  verified: true
- source: NHC notice URL and launch-meeting URL (nhc.gov.cn; 412 anti-bot, page text unread)
  field_scope:
  - notice existence and title 关于开展2017年全国生育状况抽样调查的通知 (国卫指导函[2017]183号 per provincial plan)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: OpenAlex abstract for 10.1016/j.jdeveco.2026.103796
  field_scope:
  - JDE 2026 paper use of the survey (national representativeness)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://bpb-us-w2.wpmucdn.com/web.sas.upenn.edu/dist/3/517/files/2026/04/JDE-print-main.pdf (Fang, Liu & Yang, JDE final paper, read 2026-09-28)
  field_scope:
  - actual use of the 2017 China Fertility Survey in the published paper
  - 249,946 women aged 15-60, 2,737 counties, 31 provinces and three-stage stratified sample
  - documented demographic, socioeconomic, fertility-history, desired-fertility and planned-birth fields
  - data-availability statement: authors do not have permission to share data
  - boundary: no general application route stated
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: cmds
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

The 2017 China Fertility Survey is the NHFPC/NHC's one-off national sample survey of ~250,000 women aged 15-60 (stratified three-stage PPS, all 31 provinces plus the Xinjiang Production and Construction Corps) that anchors Chinese fertility-behavior and fertility-intention research around the Universal Two-Child Policy; its irreplaceable value is national fertility intentions and behavior circa 2017, and its main barrier is that the microdata are not publicly released - researchers get reports and approved-extract journal analyses only.

## Select rules

- Prioritize it when the question needs nationally representative fertility behavior/intentions for 2016-2017 or short-run birth responses to the 2016 Universal Two-Child Policy.
- Use census/mini-census data when full-coverage fertility outcomes suffice; use CMDS for migrant-focused dynamics; use later surveys (e.g., 2021 mini-census or post-2021 fertility data) for post-2017 fertility.
- Do not plan a microdata-level analysis assuming public access: no release or application channel is documented.

## Get recipe

1. Read the official framing: NHC notice 国卫指导函[2017]183号 (nhc.gov.cn; blocked for automated clients) and the CPDRC results page (2018-08; TLS-unreachable here). Provincial implementation plans (e.g., 黑卫指导规发[2017]20号) document the sampling design.
2. Use the public research outputs: 贺丹 2019 report (人口研究), 原新 et al. 2019 (8-province minority subsample, 45,998 cases), Fang & Liu 2026 JDE.
3. If the design requires the microdata, treat access as restricted: there is no documented public application route, and the evidence boundary must be stated rather than bridged by assuming author cooperation.

## Connections and Limitations

The survey is a single 2017 cross-section with retrospective birth histories; it supports short-run policy-response analysis but not panel designs. Its geographic identifiers exist only inside approved extracts (unverified). Policy timing (Universal Two-Child Policy) belongs to the variation repository, not this record.
