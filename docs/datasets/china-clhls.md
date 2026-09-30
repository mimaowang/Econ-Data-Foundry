---
schema_version: 3
catalog_status: ready
id: china-clhls
name: Chinese Longitudinal Healthy Longevity Survey (CLHLS) / 中国老年健康影响因素跟踪调查 (now CLHLS-HF 中国老年健康与家庭幸福调查)
aka:
- CLHLS
- CLHLS-HF
- 中国老年健康调查
- 中国老年健康影响因素跟踪调查
- 中国老年健康与家庭幸福调查
- Chinese Longitudinal Healthy Longevity and Happy Family Study
provider: >-
  Joint project of Peking University Center for Healthy Aging and Development
  Studies (北京大学健康老龄与发展研究中心, CHADS) and Duke University (Duke
  Population Research Institute, DUPRI; long-time Duke PI Zeng Yi); data
  distributed free of charge via the PKU Open Research Data Platform and the
  ICPSR NACDA series
china_related: true
domains:
- health
- aging
- public
- labor
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Free downloadable CLHLS/CLHLS-HF microdata: longitudinal follow-up datasets of
    the 8 waves 1998-2018 (plus the 2021 9th-wave cross-section, released 2026-07-11),
    community data (1998-2014), biomedical indicators (2009/2012/2014), and
    parent-child paired samples (2002-2005), after signing a Data Use Agreement.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CLHLS is the world's largest survey of centenarians, nonagenarians and
    octogenarians with younger comparison groups: 113,000 face-to-face interviews
    across 8 waves (1998-2018) in 23 provinces, plus a separately released 2021 wave.
    Any researcher can register, sign
    a Data Use Agreement, and download datasets free of charge from the PKU Open
    Research Data Platform or ICPSR NACDA.
  barrier: >-
    A signed Data Use Agreement is required; released files and current terms should
    be checked at download time, and fine geographic identifiers may be restricted.

unit_of_observation: 'Elderly individual (oldest-old oversample: centenarians, nonagenarians, octogenarians) plus younger elderly (65-79) and adult comparison groups (35-64), and deceased participants'' surviving family members for end-of-life interviews'
structure: Longitudinal panel (8 waves 1998-2018); separately released 2021 wave data
geo_granularity:
- individual
- county/district (where retained in released files; fine codes may be restricted)
- province
geography: >-
  23 provinces/municipalities/autonomous regions in the released 1998-2018 tracking data.
  The current official 2021 dataset description also says that its selected counties/districts are in 23 provinces.
  Earlier project material described a 27-province 2021 field expansion; that difference is unresolved and must not be
  treated as coverage of the downloadable 2021 file without inspecting its documentation.
time_span:
  start: 1998
  end: 2021
  last_confirmed_release: 'PKU Dataverse API checked 2026-09-28: released v2.1 (1998-2018), v3.0 (2021), v1.0 (community), and v1.0 (biomarkers)'
  coverage_note: >-
    8 waves: baseline 1998 and follow-ups 2000, 2002, 2005, 2008-09, 2011-12, 2014,
    2017-18 (Duke page lists released wave years as 2000, 2002, 2005, 2008-2009,
    2011-2012, 2014, 2017-2018). The current PKU API lists a separate released 2021
    data file and questionnaire (9,720 elderly respondents in its description); its displayed
    dataset title conflicts with that description, so use the file-level metadata rather than title text alone for wave identification.
  last_checked: '2026-09-28'
frequency:
- irregular (2-3 year intervals between waves)
sample_size: >-
  113,000 face-to-face interviews across waves 1-8: 19,500 centenarians, 26,700
  nonagenarians, 29,700 octogenarians, 25,500 younger elders aged 65-79, 11,300
  adults aged 35-64; end-of-life interviews for 28,900 deceased participants;
  DNA samples for 25,000 participants (per Duke DUPRI page). The current official
  2021 release description reports 9,720 elderly respondents.
key_variables:
- Health status, physical and mental function, cognitive function (MMSE; CSI-D added in wave 8)
- Depression (CES-D scale adopted in wave 8) and emotional characteristics (PANAS components)
- Living arrangements, family structure, marital status, intergenerational support and care provision/costs
- Socioeconomic characteristics, behavior, diet/nutrition, lifestyle
- Mortality and degree/length of disability before death (deceased participants, family informant interviews)
- Biomedical indicators (2009, 2012, 2014 datasets); DNA samples (separate consent)
- Community-level data (1998-2014); parent-child paired samples (2002-2005); wave-9 family housing/finance and adult-children modules

research_fit:
  best_for:
  - Health, longevity, and cognitive research on the oldest old (80+), especially centenarians/nonagenarians
  - End-of-life health, disability, and care-cost trajectories using family-informant interviews of deceased participants
  - Intergenerational support, living arrangements, and filial-care questions for the elderly
  choose_over:
  - Choose CLHLS over CHARLS when the sample must oversample the oldest old (80+) or reach back to 1998; choose CHARLS when the target population is the general 45+ population with biomarkers and retirement modules, or when a 2011+ panel with 150 counties/28 provinces is preferred.
  - Choose CLHLS over CFPS for elderly-specific longevity/health-aging questions; CFPS remains the all-age household panel.
  not_good_for:
  - Working-age population analysis: the comparison groups (35-64) are not a representative working-age sample.
  - Nationally representative household economics for all ages (use CFPS/CHIP).
  - Recent waves after 2021: 2021 is the latest released wave confirmed in this record; no later wave was confirmed this round.
  needs_join_for:
  - Policy timing and macro context: join province/county policy dates and macro series; check which geographic identifiers the released files carry.
  - Biomarker-based clinical analysis: biomedical datasets cover 2009/2012/2014 only.
  variation_available:
  - Longitudinal follow-up of individuals across 8 waves with mortality capture between waves; age-heterogeneity comparisons across oldest-old vs younger groups.
  topics:
  - healthy longevity
  - oldest old
  - aging
  - centenarians
  - elderly health
  - intergenerational care
  - mortality

good_for:
- DiD/event studies of elderly-care policies on health outcomes using wave-to-wave follow-up (e.g., the CER 2026 medical-elderly-care integration pilot study)
- Longevity determinants and centenarian studies
- End-of-life care costs and disability trajectories
identification:
- Direct survey microdata: released CLHLS/CLHLS-HF respondent-level files, community contextual files, and separately scoped biomarker files; these are distinct deliverables rather than one interchangeable all-purpose panel.
linkable_keys:
- Individual ID (within CLHLS longitudinal files)
- Wave/survey year
- Province/county identifiers (subject to released-file permissions)

joins:
- target: charls
  relation: often-confused-with
  keys:
  - Province or county
  - Age group
  method: Compare samples and modules before any combined analysis; the two surveys have different age targets, waves, and sampling frames, so treat them as separate products.
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province code
  - Year
  method: Join province-year macro controls by province/year; check the geographic codes actually released in the CLHLS files.
  evidence_status: plausible

access_routes:
- route: pku-open-data (PKU Open Research Data Platform, CHADS dataverse)
  access_status: available-with-application
  direct_url: https://opendata.pku.edu.cn/dataverse/CHADS
  requirements:
  - Registration on the PKU Open Research Data Platform
  - Signed CLHLS Data Use Agreement (data use for research; personal privacy fields removed before release)
  steps:
  - Register at opendata.pku.edu.cn and open the 中国老年健康与家庭幸福调查（CLHLS-HF） dataverse (北京大学健康老龄与发展研究中心).
  - Open the released dataset pages for tracking data (1998-2018, DOI 10.18170/DVN/WBO7LK, v2.1, 7 files), 2021 data (DOI 10.18170/DVN/UNYEL1, v3.0, 2 files), community data (1998-2014, DOI 10.18170/DVN/UWS2LR, v1.0, 18 files), or biomarkers (2009/2012/2014, DOI 10.18170/DVN/FWVGN5, v1.0, 10 files).
  - Sign the Data Use Agreement and download the datasets free of charge.
  deliverable: Released wave datasets, questionnaires, user guides, and codebooks in platform formats
  cost: free
  last_checked: '2026-09-28'
  caveat: The current API reports released versions and file inventories, not that every field is unrestricted. The platform requires JavaScript for ordinary browsing; sensitive geographic fields may be restricted per agreement.
- route: icpsr-nacda (National Archive of Computerized Data on Aging, series 487)
  access_status: available-with-application
  direct_url: https://www.icpsr.umich.edu/icpsrweb/NACDA/series/487
  requirements:
  - ICPSR registration and signed Data Use Agreement (per the Duke CLHLS page)
  steps:
  - Open the NACDA CLHLS series page, register, and accept the data use terms.
  - Download the wave files available in the series.
  deliverable: CLHLS wave datasets as deposited in NACDA
  cost: free
  last_checked: '2026-08-15'
  caveat: ICPSR deposit contents were not enumerated this round; the Duke page names this route as an official distribution point.
- route: cpdrc-padis
  access_status: needs-verification
  direct_url: https://www.cpdrc.org.cn/
  requirements: China Population and Development Research Center platform access (PADIS), per the PKU dataverse description
  steps:
  - The PKU page states the data are also made available through the 中国人口与发展研究中心 PADIS and 全民健康保障信息化工程 database platforms.
  - The exact application flow was not verified this round (cpdrc.org.cn TLS-unreachable in this environment).
  deliverable: Same released CLHLS datasets via the alternative official channel (to be verified)
  cost: free
  last_checked: '2026-08-15'
  caveat: Unverified channel; do not rely on it without confirming the current procedure.

access:
  url: https://opendata.pku.edu.cn/dataverse/CHADS
  cost: free
  license: Data Use Agreement (academic research use; no redistribution of raw data)
  format:
  - dta
  - sav
  - csv
  - pdf (questionnaires and guides)
  api: false
  how_to_get: Register on the PKU Open Research Data Platform, sign the CLHLS Data Use Agreement, and download from the CHADS dataverse; ICPSR NACDA series 487 is the alternative official route.
caveats:
- Sample is elderly-focused with an oldest-old oversample (67.4% of interviews were 80+ per the PKU page); it is not a representative sample of the general adult population.
- Wave years and province coverage changed over time. The 2021 release's current official description says 23 provinces, while an earlier project source says 27; inspect the selected release before relying on either scope claim.
- Biomedical data exist only for 2009/2012/2014; DNA data require separate consent.
- The motivating CER paper (10.1016/j.chieco.2026.102641) is abstract-level evidence only; the exact waves and variables it used are unverified (ScienceDirect 403).

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: partial
  last_audited: '2026-09-28'

used_by:
- cite: 'CER 2026 (China Economic Review 96, 10.1016/j.chieco.2026.102641), Integration of medical care and elderly care: Chinese experience and outcomes of older adults'
  doi: https://doi.org/10.1016/j.chieco.2026.102641
  journal: China Economic Review
  year: 2026
  dataset_role: Main outcome microdata (panel data from CLHLS) in a DiD on the 2016 city-level medical-elderly-care integration pilot
  evidence_type: abstract-only
  evidence_url: https://econpapers.repec.org/article/eeechieco/v_3a96_3ay_3a2026_3ai_3ac_3as1043951x26000100.htm
  data_note: >-
    The abstract names 'panel data from CLHLS' as the outcome source in a DiD
    design around the 2016 integration pilot; the exact waves, sample, and
    geographic identifiers used are unverified (ScienceDirect full text blocked).

provenance:
- source: Duke University Population Research Institute (DUPRI) CLHLS-HF project page (www.dupri.duke.edu)
  field_scope:
  - survey identity (CLHLS-HF) and world's-largest-centenarian-survey claim
  - 8 waves 1998-2018 in 23 provinces; 113,000 interviews with age-composition breakdowns
  - 28,900 deceased participants' end-of-life interviews; DNA samples 25,000
  - wave-8 instrument additions (CSI-D, CES-D, PANAS); 9th wave 2021 extended to 27 provinces
  - free data access after DUA via opendata.pku.edu.cn and ICPSR NACDA series 487
  - birth years ~1890-1967; age range at last data collection 60-100+
  added: '2026-08-15'
  confidence: high
  verified: true
- source: PKU Open Research Data Platform CHADS dataverse (opendata.pku.edu.cn/dataverse/CHADS)
  field_scope:
  - Chinese names (中国老年健康与家庭幸福调查; 原中国老年健康调查)
  - baseline 1998; 8 surveys 1998-2018 in 23 provinces; 9th survey 2021 in 27 provinces
  - 113,000 interviews; 67.4% aged 80+; 28,900 deceased-interview figure; free to scholars; privacy-stripped release
  - dataset inventory with DOIs (tracking 1998-2018 WBO7LK; 2021 cross-section UNYEL1 released 2026-07-11; community UWS2LR; biomedical FWVGN5; parent-child 47EDYC)
  - 10,327 registered scholars as of 2021-10-15; distribution via PKU platform and CPDRC PADIS
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://opendata.pku.edu.cn/api/datasets/:persistentId/
  field_scope:
  - current released-version status and file inventories for WBO7LK, UNYEL1, UWS2LR, and FWVGN5
  - 1998-2018 tracking-data title and 7-file inventory
  - 2021 description, 9,720-respondent count, two released files, and 23-province wording
  - community-data 1998-2014 description and 18-file inventory
  - biomarker 2009/2012/2014 description and 10-file inventory
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: charls
  relation: often-confused-with
- id: cfps
  relation: complement
- id: chns
  relation: complement
---

## Positioning in one sentence

CLHLS is the world's largest survey of centenarians, nonagenarians and octogenarians with younger comparison groups — 113,000 interviews across 8 waves (1998-2018) in 23 provinces, plus a separately released 2021 wave — jointly run by Peking University (CHADS) and Duke University, and obtainable after a signed Data Use Agreement from the PKU Open Research Data Platform or ICPSR NACDA. Its irreplaceable value is oldest-old health, longevity, and end-of-life research since 1998; the main acquisition step is registration plus agreement signing.

## Select rules

- Prioritize CLHLS for oldest-old (80+) health, longevity, cognition, and end-of-life care questions, and for intergenerational support among the elderly.
- Switch to CHARLS when the design needs the general 45+ population, biomarker blood panels across waves, or a 2011+ county-based sample; keep the two products separate.
- Do not use it as a representative all-age household panel, and verify which geographic identifiers the released files carry before planning fine-grain joins.

## Get recipe

1. Register on the PKU Open Research Data Platform (opendata.pku.edu.cn) and open the 中国老年健康与家庭幸福调查（CLHLS-HF） dataverse.
2. Sign the CLHLS Data Use Agreement and download the needed datasets: 追踪数据（1998-2018） (DOI 10.18170/DVN/WBO7LK), the 2021 截面数据 (DOI 10.18170/DVN/UNYEL1), community (UWS2LR), biomedical (FWVGN5), and parent-child (47EDYC) files.
3. Alternatively use ICPSR NACDA series 487 after signing the agreement; confirm the deposited file inventory.
4. Before analysis, map the released geographic identifiers and confirm which waves the research question needs (wave years: 1998, 2000, 2002, 2005, 2008-09, 2011-12, 2014, 2017-18, 2021). For the 2021 file, inspect its release documentation: current official metadata says 23 provinces, not the 27 claimed in older project material.

## Connections and Limitations

CLHLS and CHARLS are often confused but are different products: different age targets (oldest-old oversample vs 45+ general elderly), different start years (1998 vs 2011), and different sampling frames. Fine county identifiers may be restricted under the agreement, and biomedical data exist only for 2009/2012/2014, so long-run biomarker trajectories must respect those gaps. The published 2021 dataset's geography must be read from its own documentation because older 27-province wording conflicts with the current official metadata's 23-province description.
