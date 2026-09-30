---
schema_version: 3
catalog_status: grounding
id: china-gaokao-ncee-universe-1999-2003
name: National College Entrance Exam (NCEE/gaokao) participant administrative microdata, universe 1999-2003 (China; Li, Meng, Mu & Wang 2024 JDE)
aka:
- 高考考生数据
- NCEE administrative data
- gaokao universe 1999-2003
- 22,608,392 test takers
provider: >-
  Administrative dataset maintained by China's Ministry of Education (MOE),
  per the BFI WP 2024-20 data section ("a novel administrative dataset
  maintained by the MOE"). The exact MOE unit or access agreement that supplied
  the authors is not named in the WP. No public distribution channel exists.
china_related: true
domains:
- education
- labor
- urban-rural
- inequality

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    Student-level administrative microdata for the universe of NCEE (gaokao)
    test takers 1999-2003: 22,608,392 participants (48.5% urban Hukou), with
    basic demographics, per-subject exam performance, college admission
    outcomes, and urban/rural classification from Hukou status. English-listening
    rollout years per province are compiled separately from the China Education
    and Examination Yearbooks cross-validated with news archives.
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: >-
    Grounding-b16 (2026-08-15): BFI Working Paper No. 2024-20 ("English Language
    Requirement and Educational Inequality: Evidence from 16 Million College
    Applicants in China", Li, Meng, Mu & Wang, Feb 2024) downloaded from
    bfi.uchicago.edu and data section 3 read in full: "The main data used in
    this paper come from a novel administrative dataset maintained by the MOE
    and covering more than 22 million NCEE test takers between 1999 and 2003.
    For each exam taker, we have detailed information on basic demographics,
    exam performance in each subject, and college admission outcomes...
    categorize each student as 'urban' or 'rural' based on the Hukou status."
    Universe: 22,608,392 participants; 48.5% urban; ~54% of urban and ~63% of
    rural test takers male; mean age ~19; 94% ethnic Han; ~0.5% Party members;
    repeaters ~21% urban / ~29% rural. English-listening rollout (1999-2003)
    compiled from the China Education and Examination Yearbooks, cross-validated
    with news archives (section 3.1). NO data availability statement in the WP;
    no replication deposit found; published JDE version (10.1016/j.jdeveco.2024.
    103271) data section unread (Elsevier 403). The WP title's "16 million"
    versus the 22.6 million universe is the paper's own framing - the analysis
    sample restricts to English-choosing, Han Chinese first-time takers
    (footnotes 11-12), but the exact mapping is not spelled out in the read text.
  barrier: >-
    MOE administrative microdata; no application route, no public release, and
    no replication package evidenced. Not reconstructable from public inputs
    (per-student scores, Hukou, and admission outcomes are not public). The
    obtainable evidence is the WP text (construction and sample description),
    not the data.

unit_of_observation: individual NCEE (gaokao) test taker, per exam year 1999-2003
structure: repeated cross-section of students across exam years (some repeaters take the exam in multiple years)
geo_granularity:
- province (students take the NCEE in their home province per Hukou); county appears in regressions per appendix references
geography: China, all provinces; students take the exam in their home province as determined by Hukou
time_span:
  start: '1999'
  end: '2003'
  last_confirmed_release: 'No release; evidence is BFI WP 2024-20 (Feb 2024) data section'
  coverage_note: >-
    Universe 22,608,392 NCEE participants 1999-2003 (48.5% urban Hukou).
    English-listening adoption varies across provinces 1999-2003. Published JDE
    2024 version coverage unverified against the WP.
  last_checked: '2026-08-15'
frequency:
- annual (exam years)
sample_size: 22,608,392 NCEE participants 1999-2003 (universe; analysis sample smaller - English-choosing, Han first-time takers)
key_variables:
- Basic demographics (gender, age, ethnicity, Party membership)
- Exam performance in each subject (score percentile ranks within province-year-track)
- College admission outcomes (any college, 4-year regular, Project 211, Project 985)
- Hukou status (urban vs rural)
- Repeater indicator (multiple-year takers)
- Province-year English-listening adoption (from China Education and Examination Yearbooks)

research_fit:
  best_for:
  - Urban-rural gaps in college access and exam performance in China 1999-2003 at the individual level
  - Describing differences in scores and admission outcomes by province, exam year, track, and Hukou group when access is approved
  - Population-scale descriptive work on the gaokao (admission rates, demographics of takers) for 1999-2003
  choose_over:
  - Choose this over census- or survey-based education measures (china-census) when individual exam scores, per-subject performance, or admission outcomes are required
  - Choose this over aggregate admission statistics when within-province-track score distributions are needed
  not_good_for:
  - Post-2003 cohorts (data end at 2003)
  - Students who took foreign languages other than English (excluded from the English-choosing sample)
  - Any question requiring the actual microdata: it is not obtainable
  - College outcomes after admission (no post-admission records in the described fields)
  needs_join_for:
  - Post-education outcomes (earnings, careers) - not in this asset
  - Provincial context (education inputs, quotas) from yearbooks/statistical data
  variation_available:
  - Exam-year, province, track, score, admission, and Hukou fields are observed dimensions of the described administrative file.
  - English-listening rollout years are separately compiled from yearbooks and news archives; this record does not document a causal assignment design.
  topics:
  - college entrance exam
  - education inequality
  - urban-rural gap
  - English language requirement
  - administrative microdata

good_for:
- education economics
- gaokao analysis
- urban-rural inequality
identification: []
linkable_keys:
- Province
- Year
- (Student identifiers exist in the raw data but are not releasable/evidenced)

joins:
- target: china-census
  relation: complement
  keys:
  - province
  - year
  method: Census education and urban-rural population measures as context or alternative education outcomes
  evidence_status: plausible

access_routes:
- route: bfi-wp-full-text
  access_status: available
  direct_url: https://bfi.uchicago.edu/working-paper/english-language-requirement-and-educational-inequality-evidence-from-16-million-college-applicants-in-china/
  requirements: None (publicly downloadable BFI WP PDF; fetched 2026-08-15)
  steps:
  - Download BFI Working Paper No. 2024-20 (Li, Meng, Mu & Wang, Feb 2024).
  - Read section 3 (Data) for the MOE administrative dataset description, sample restrictions, and English-listening rollout construction.
  deliverable: Full working-paper text with the data section; NOT the microdata.
  cost: free
  last_checked: '2026-08-15'
  caveat: The WP contains no data availability statement and no data files.
- route: jde-published
  access_status: blocked
  direct_url: https://doi.org/10.1016/j.jdeveco.2024.103271
  requirements: Subscription or institutional access (Elsevier 403 for automated clients)
  steps:
  - Read the published JDE 2024 version (vol 168, article 103271) data section and any data availability statement.
  deliverable: Published data section / DAS; expected to confirm the same restricted boundary.
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Published version data section unread in this environment.
- route: data-itself
  access_status: blocked
  direct_url: needs-verification
  requirements: MOE administrative data access; no application route evidenced
  steps:
  - No public or institutional route evidenced for the raw microdata.
  deliverable: None public.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Do not assume author contact implies data sharing; the WP is silent on access terms.

access:
  url: https://bfi.uchicago.edu/working-paper/english-language-requirement-and-educational-inequality-evidence-from-16-million-college-applicants-in-china/
  cost: by-application
  license: MOE administrative microdata - restricted; WP text freely downloadable
  format: []
  api: false
  how_to_get: >-
    The microdata are unobtainable through any evidenced route. The BFI WP full
    text documents the universe, fields, and sample restrictions and is the
    evidence base for any research design referencing this asset.
caveats: >-
  The WP title says "16 million college applicants" while the data section
  reports 22,608,392 participants - the analysis sample (English-choosing, Han
  first-time takers, per footnotes 11-12) is smaller than the universe, but the
  exact mapping of "16 million" is not spelled out in the read text; retain the
  discrepancy. No DAS in the WP; published JDE DAS unread.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Li, Hongbin; Lingsheng Meng; Kai Mu & Shaoda Wang (2024), English language requirement and educational inequality: Evidence from 16 million college applicants in China'
  doi: https://doi.org/10.1016/j.jdeveco.2024.103271
  journal: Journal of Development Economics
  year: 2024
  dataset_role: Main analysis dataset - universe of NCEE participants 1999-2003 (scores, admission outcomes, Hukou)
  evidence_type: working_paper_data_section
  evidence_url: https://bfi.uchicago.edu/working-paper/english-language-requirement-and-educational-inequality-evidence-from-16-million-college-applicants-in-china/
  data_note: >-
    BFI WP 2024-20 (Feb 2024) data section 3 read in full (2026-08-15):
    "novel administrative dataset maintained by the MOE"; 22,608,392 NCEE test
    takers 1999-2003; fields = basic demographics, per-subject exam performance,
    college admission outcomes, Hukou urban/rural; 48.5% urban; rollout years
    from China Education and Examination Yearbooks cross-validated with news
    archives. No DAS in WP; no replication found; JDE published version data
    section unread (Elsevier 403).

provenance:
- source: https://bfi.uchicago.edu/working-paper/english-language-requirement-and-educational-inequality-evidence-from-16-million-college-applicants-in-china/
  field_scope:
  - data_identity
  - sample
  - variables
  - construction
  - paper_use
  added: '2026-08-15'
  confidence: high
  verified: true
- source: 'https://doi.org/10.1016/j.jdeveco.2024.103271 (OpenAlex: JDE vol 168, article 103271, 2024)'
  field_scope:
  - published_metadata
  - paper_identity
  added: '2026-08-15'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-gaokao-ncee-universe-1999-2003, JDE 2024 sweep 2026-08-16)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-census
  relation: complement
---

## Positioning in one sentence

The Li, Meng, Mu & Wang (2024 JDE) asset is the MOE-maintained administrative microdata for the universe of NCEE (gaokao) test takers 1999-2003 - 22,608,392 individuals with demographics, per-subject scores, admission outcomes, and Hukou - fully documented in the free BFI WP 2024-20 data section but with no evidenced access route or release, making it an inaccessible paper-specific asset.

## Select rules

- Use this identity for research questions on urban-rural college-access gaps and exam outcomes at the population scale for 1999-2003; the WP documents the asset precisely even though the data are unobtainable.
- For obtainable alternatives, use china-census education measures, public admission statistics, or survey data - they cannot reproduce per-student scores or admission outcomes.
- Do not treat the WP as a data release; do not route researchers to an application channel that no source evidences.

## Get recipe

1. Download BFI WP 2024-20 (free) and read section 3 for the universe, fields, sample restrictions, and rollout construction - this is the evidence base for any design.
2. For the actual microdata, no route exists: MOE administrative access is not described anywhere readable; assume inaccessible and design around obtainable alternatives.
3. If a design truly needs the data, the only open action is author contact (no evidence of past sharing) or a human-browser check of the published JDE DAS.

## Connections and Limitations

- Universe (22,608,392) vs the title's "16 million": analysis sample restrictions (English-choosing, Han first-time takers, repeaters excluded) shrink the universe; the exact mapping is not explicit in the read text.
- English-listening rollout (1999-2003) comes from China Education and Examination Yearbooks cross-validated with news archives - a separate, reproducible component.
- Students take the exam in their home province per Hukou; admission quotas are province-track level; these institutional features structure all joins.
- No post-admission outcomes exist in the described asset; career-earnings questions need other data.
