---
schema_version: 3
catalog_status: ready
id: css-chinese-social-survey
name: Chinese Social Survey (CSS 中国社会状况综合调查)
aka:
- CSS
- 中国社会状况综合调查
- Chinese Social Survey, CASS
- 社科院CSS调查
provider: >-
  中国社会科学院社会学研究所 (Institute of Sociology, Chinese Academy of Social
  Sciences, CASS). Verified from the official survey site css.cssn.cn
  (fetched 2026-08-15): CSS is a national large continuous sampling survey
  initiated in 2005 by the CASS Institute of Sociology, measuring public
  labor employment, family and social life, and social attitudes. Data
  application is run through 中国社会质量基础数据库 (csqr.cass.cn) and the
  CSS data-application portal; the site is funded by the 国家社科重大项目
  "中国社会质量基础数据库建设" and CASS programs (footer, read 2026-08-15).
china_related: true
domains:
- sociology
- public
- labor
- development
- governance
- demography

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    CSS wave microdata files (individual-level records with household
    context) delivered after an approved application. Verified waves with
    released data: 2006, 2008, 2011, 2013, 2015, 2017, 2019 (via 中国社会
    质量基础数据库 csqr.cass.cn) and CSS2021 (released 2023-02-03, via the
    CSS data-application portal). Application procedure verified from the
    official 历年数据申请方式说明 page (read 2026-08-15): register on the
    platform, complete 实名认证 (name, gender, contact, ID, unit, title),
    apply for the CSS data stating the research purpose, download and upload
    the signed 数据使用协议; processed within 3 working days; free of charge.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider-first grounding (2026-08-15): css.cssn.cn home, 历年数据 list and
    历年数据申请方式说明 were all fetched over HTTP(S) and read. Identity:
    biennial (双年度) national probability household survey since 2005 by the
    CASS Institute of Sociology. Released waves 2006-2021 with an explicit,
    free application protocol. A public 2023 paper independently verifies
    actual CSS2019 use, its csqr.cass.cn application entry, 10,283 valid
    questionnaires from urban and rural households in 596 villages/communities
    and 149 cities/counties/districts, and the paper's 6,689-person rural-hukou
    analytic subset. Variable sets and geography fields still vary by wave and
    must be checked in the approved delivery.
  barrier: >-
    Application-gated (实名认证 + research-purpose statement + signed data-use
    agreement); fine geography and variable details per wave must be checked
    in the approved delivery.

unit_of_observation: >-
  Individual respondent (adult) with household context; repeated cross-section
  per wave (biennial)
structure: repeated-cross-section (biennial waves; panel linkage across waves not claimed)
geo_granularity:
- region/province-level identifiers (exact geography fields per wave unread)
geography: >-
  China. The open CSS2019 paper documents urban and rural households in 596
  villages/communities and 149 cities/counties/districts nationwide; its
  paper-specific rural-hukou subset is not a general CSS coverage definition.
time_span:
  start: '2005'
  end: '2021'
  last_confirmed_release: 'CSS2021 data released 2023-02-03 (official 历年数据 page, read 2026-08-15)'
  coverage_note: >-
    Survey initiated 2005; released data waves verified on the official page:
    2006, 2008, 2011, 2013, 2015, 2017, 2019, 2021. Later waves beyond 2021
    not verified.
  last_checked: '2026-09-28'
frequency:
- biennial
sample_size: >-
  CSS2019: 10,283 valid questionnaires in the open paper's source description;
  that paper retains 6,689 rural-hukou respondents after its own exclusions.
  Do not project either count onto other waves.
key_variables:
- Labor employment and work status
- Family and social life
- Social attitudes and values
- Income/consumption related modules (exact variable sets per wave unread)
- Subjective well-being and social quality measures
  - CSS2019 social-justice evaluations, political participation/participation
    intentions, hukou, income, education and regional controls (paper-specific
    use; inspect the approved 2019 questionnaire/codebook for exact fields)

research_fit:
  best_for:
  - Chinese adult social attitudes, subjective well-being, social quality and employment-family conditions measured by the CASS national biennial survey
  - Public-opinion and governance-attitude research where the CASS survey family (and its 2006-2021 wave coverage) is the natural instrument
  choose_over:
  - Choose CSS alongside CGSS (RUC) when the research needs the CASS wave coverage (incl. 2019 and 2021 releases) or CASS module contents; verify both before choosing one for a specific module.
  - For income/consumption microdata with long panels prefer cfps/chip/chfs; CSS is a social-attitudes-and-conditions survey, not a balance-sheet survey.
  not_good_for:
  - Detailed household balance sheets or financial asset measurement (use chfs/cfps)
  - Longitudinal tracking of the same individuals (repeated cross-sections; linkage unclaimed)
  - Aging-health biomarkers (use charls/china-clhls)
  needs_join_for:
  - Fine geographic context (county-level) if the design needs it - geography fields per wave unread, verify in the delivered files
  - Treatment/policy timing (belongs to Econ-Variation side of the design)
  variation_available:
  - Wave-to-wave (biennial) cross-sectional variation in attitudes/conditions
  - Geographic variation within waves (subject to released geography fields)
  topics:
  - social attitudes
  - public opinion
  - subjective well-being
  - labor
  - social quality
  - CASS survey

good_for:
- social attitudes research
- subjective well-being
- employment conditions
- governance attitudes
identification:
- repeated cross-section comparisons
- cohort/wave designs
linkable_keys:
- Wave
- Individual respondent (no public cross-wave ID claimed)
- Region identifiers (per wave, unread)

joins:
- target: cgss
  relation: complement
  keys:
  - wave/individual
  method: compare module coverage and waves across the two national social surveys before choosing
  evidence_status: plausible

access_routes:
- route: csqr-application
  access_status: by-application
  direct_url: http://csqr.cass.cn/
  requirements: Registration + 实名认证 (name, gender, contact, ID, unit, title) + research-purpose statement + signed 数据使用协议
  steps:
  - Open 中国社会质量基础数据库 (csqr.cass.cn) and register/log in.
  - Complete 实名认证 in the personal center.
  - Apply for CSS data (choose the target wave, state the research purpose).
  - Download and upload the signed 数据使用协议.
  - Wait for processing (official note: within 3 working days).
  deliverable: CSS wave microdata files for approved purposes; free of charge.
  cost: free
  last_checked: '2026-08-15'
  caveat: 'Official note: CSS2019 data are only released via csqr.cass.cn. Exact deliverable format and variables per wave unread.'
- route: css-portal-2021
  access_status: by-application
  direct_url: http://skycss.haoboyihai.com:8099/skyuser/user_center/
  requirements: Account on the CSS data-application portal (linked from the official site navigation)
  steps:
  - Open the CSS data-application portal from css.cssn.cn navigation (数据申请).
  - Register and follow the same purpose-statement/agreement flow for CSS2021.
  deliverable: CSS2021 microdata files (released 2023-02-03).
  cost: free
  last_checked: '2026-08-15'
  caveat: The portal domain is a third-party-hosted application system linked from the official site; verify the current entry point on css.cssn.cn.

access:
  url: http://css.cssn.cn/
  cost: free
  license: Data-use agreement (数据使用协议) per application; academic use expected
  format:
  - dta-like microdata formats (exact formats unread)
  api: false
  how_to_get: Apply via 中国社会质量基础数据库 (csqr.cass.cn) for waves 2006-2019, or the CSS data-application portal for CSS2021; free, purpose-stated, agreement-signed.
caveats: >-
  The 2023 public paper grounds CSS2019 only: its 6,689 rural-hukou analysis
  subset, variables and regional controls are not a released all-purpose CSS
  file or a guarantee that the same fields occur in another wave. Verify the
  chosen wave's questionnaire, codebook, geography and weights in the approved
  delivery. Waves beyond 2021 are unverified. The application portal
  (skycss.haoboyihai.com:8099) is third-party-hosted; use the official
  navigation entry point.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: >-
    He (2023), How Does Perceptions of Social Justice Affect Farmers'
    Political Participation? Evidence from China
  doi: https://doi.org/10.1371/journal.pone.0295792
  journal: PLOS ONE
  year: 2023
  dataset_role: >-
    CSS2019 microdata supply social-justice evaluations, political-participation
    measures and individual controls for a rural-hukou analytic subset.
  evidence_type: publisher_full_text
  evidence_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0295792&type=printable
  data_note: >-
    The open full text identifies CSS2019, the CASS Institute of Sociology and
    csqr.cass.cn as the application route. It reports 10,283 valid questionnaires
    from urban and rural households in 596 villages/communities and 149
    cities/counties/districts, then restricts its own study to 6,689 rural-hukou
    respondents after missing-value exclusions. This verifies actual 2019 use,
    not release of the authors' cleaned rural subset or their exact analysis file.

provenance:
- source: http://css.cssn.cn/ (official survey site, fetched 2026-08-15)
  field_scope:
  - provider
  - identity
  - design
  - application_links
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://css.cssn.cn/css_sy/zlysj/lnsj/ (历年数据 list, fetched 2026-08-15)
  field_scope:
  - released_waves
  - release_dates
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://css.cssn.cn/css_sy/zlysj/lnsj/202209/t20220926_5541891.html (历年数据申请方式说明, fetched 2026-08-15)
  field_scope:
  - access_procedure
  - waves_via_csqr
  - contact
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0295792&type=printable (publisher full text, read 2026-09-28)
  field_scope:
  - actual CSS2019 use by He (2023)
  - CSS2019 application route through csqr.cass.cn
  - 10,283 valid questionnaires, 596 villages/communities and 149 cities/counties/districts in that paper's source description
  - paper-specific 6,689 rural-hukou analytic subset and named 2019 analysis measures
  - boundary between the released CSS2019 file and the authors' cleaned subset
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: cgss
  relation: complement
- id: cfps
  relation: complement
---

## Positioning in one sentence

CSS is the CASS Institute of Sociology's biennial national household survey (since 2005) covering labor, family and social attitudes, obtainable free of charge through a documented application route (csqr.cass.cn / CSS portal) for released waves 2006-2021; a public paper confirms the 2019 route and a concrete national urban/rural use case.

## Select rules

- Prioritize when the design needs CASS-wave coverage (incl. 2019/2021) or CASS module contents on social attitudes, employment and family conditions.
- Compare module coverage and waves with cgss before committing to either; they are distinct products from distinct institutes with similar names.
- For household balance-sheet or financial-asset measurement, switch to chfs/cfps; for aging health, switch to charls/china-clhls.

## Get recipe

1. Open css.cssn.cn and the 历年数据 page to confirm the target wave and its release status.
2. Apply via 中国社会质量基础数据库 (csqr.cass.cn) for waves 2006-2019 (CSS2019 only there) or the CSS portal for CSS2021.
3. Complete 实名认证, state the research purpose, sign and upload the 数据使用协议.
4. Expect processing within about 3 working days; download the delivered microdata.

## Connections and Limitations

- The documented 2019 coverage and sample count do not prove identical design or modules in other waves; verify the selected delivery's questionnaire, codebook, geography and weights.
- Repeated cross-sections; no cross-wave individual linkage is claimed - do not treat it as a panel.
- The application portal is third-party-hosted but linked from the official site; confirm the current entry point.
- Policy/treatment timing belongs to the variation side of the design (Econ-Variation), not to this data record.

## Decision sufficiency check

A researcher can select a released CSS wave, submit a concrete free application, and knows that CSS2019 has supported a nationwide urban/rural social-attitudes study. The study's rural-hukou subset is not what the researcher receives: obtain the approved wave first, then reproduce any subgroup and confirm its variables, weights and permitted geography from the associated materials.
