---
schema_version: 3
catalog_status: ready
id: ceps
name: China Education Panel Survey (CEPS)
aka:
- CEPS
- 中国教育追踪调查
- China Education Panel Survey
provider: National Survey Research Center (NSRC), Renmin University of China
china_related: true
domains:
- education
- labor
- development
- public
- migration
- urban-rural
data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Multi-respondent school-based survey files for students, parents, teachers, and school administrators; baseline and follow-up files are released as separate respondent products.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The current CNSDA catalog identifies the survey and lists its questionnaires, data-use manual, cross-wave variable table, and Stata respondent files. The catalog says it will no longer add data but will continue daily maintenance, and directs requests for additional data to RUC's newer social-science data platform. A public PKU Dataverse deposit provides a 2014 baseline mirror, but it is a separate deposit and should not be assumed to contain every official file or geography field.
  barrier: Registration/login and the current data-use terms are required; county/school identifiers and fine geography may be restricted or absent from a public download.

unit_of_observation: Student-year, parent-year, teacher-year, school-administrator-year, with class and school context files
structure: Longitudinal school-based panel with multiple respondent types
geo_granularity:
- student
- family
- class
- school
- county/district (sample PSU; exact public identifiers require checking the release)
geography: National mainland China sample drawn from 28 county-level units (counties, districts, or county-level cities), 112 schools, and 438 classes at baseline
time_span:
  start: 2013-09
  end: 2015-07
  last_confirmed_release: 2015
  coverage_note: Baseline is the 2013-2014 school year; the CNSDA catalog confirms a 2014-2015 follow-up with respondent files. Later CEPS follow-ups or additional cohorts are not silently included in this record.
  last_checked: '2026-08-12'
frequency:
- annual follow-up
sample_size: Baseline approximately 19,487 students in 438 classrooms and 112 schools; the CNSDA 2014-2015 release lists 10,750 student and parent records, 791 teacher records, and 304 school-administrator records for that release.
key_variables:
- Student cognitive and noncognitive assessments
- Student demographics, family background, hukou and migration-related measures
- Parent education, occupation, household resources, and parent-child relationships
- Class composition, friendship and peer relationships, teacher-student interaction, and school context
- Teacher characteristics, evaluations, workload and attitudes
- School facilities, enrollment, staffing and administration

research_fit:
  best_for:
  - Peer composition, classroom interaction, school resources, and adolescent human-capital outcomes
  - Urban-rural, migrant-status, and local school-context comparisons when the approved geography and weights support them
  - Linking individual education outcomes to school, class, and county/district context rather than treating the survey as a county economic panel
  choose_over:
  - Prefer CEPS over a general household survey when the question needs students, parents, teachers, classmates, and school administrators observed around the same classrooms.
  - Prefer CFPS or CHFS when the question needs broader household or financial coverage, annual local economic outcomes, or a longer adult panel.
  not_good_for:
  - A dense city-year or county-year economic panel; only 28 county-level sample units are selected at baseline.
  - National administrative school outcomes, complete school rosters, or unrestricted fine-grained spatial exposure.
  - Treating classroom-derived peer shares as a ready-made national statistic; those variables must be reconstructed from respondent files and paper-specific inclusion rules.
  needs_join_for:
  - Local labor markets, housing, weather, land, or policy exposure require a separately sourced geography-year dataset and an approved, stable CEPS geography key.
  - Cross-wave comparisons require the survey's identifier and attrition documentation; do not assume every respondent file is a balanced panel.
  variation_available:
  - Classroom peer composition and school-context differences observed in the survey
  - Urban-rural and migrant-status heterogeneity in education and family outcomes
  topics:
  - education
  - peer effects
  - school quality
  - human capital
  - urban-rural inequality
  - migrant children
  - social capital
  - local public services

good_for:
- School and classroom peer effects
- Student cognitive and noncognitive development
- Family, school, and community channels of education inequality
- Urban-rural and migrant-background comparisons in lower-secondary education
identification:
- Multilevel or fixed-effects comparisons within school/class context
- Paper-specific random classroom assignment or peer-composition designs where assignment and sample restrictions are documented
- Panel comparisons across the confirmed baseline and follow-up waves
linkable_keys:
- Respondent identifiers within each wave and respondent type
- Student-parent, student-teacher, class, and school identifiers where supplied
- Wave/cohort and documented county/district identifiers when approved

joins:
  - target: cfps
    relation: complement
    keys:
    - Age/cohort and documented region, with no assumption of person-level matching
    - Survey year and urban-rural or hukou definitions
    method: Use CEPS for school and peer context and CFPS for broader household or adult outcomes; compare harmonized definitions rather than attempting individual linkage.
    evidence_status: plausible
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Approved county/district code or documented sample-PSU crosswalk
    - Reference year
    method: Add province/city or other public local context only after verifying that the released CEPS geography key is stable and permitted. The official CEPS pages establish the 28-PSU design but do not release a universal public crosswalk in the checked materials; a coarser join may be the only lawful option.
    evidence_status: plausible

access_routes:
  - route: CNSDA official CEPS catalog
    access_status: available-with-login
    direct_url: https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
    requirements: Free registration/login; follow the catalog's data-use and citation terms.
    steps:
    - Register or log in to CNSDA.
    - Open the CEPS 2014-2015 follow-up project and read the data-use notes and documentation.
    - Download the permitted questionnaire, codebook, and respondent files; record the exact release and language before analysis.
    deliverable: CNSDA lists Chinese and English questionnaires, a data-use manual, a two-wave variable crosswalk, and Stata respondent files for students, parents, teachers, and school administrators.
    cost: free
    last_checked: '2026-09-27'
    caveat: The catalog confirms project-level files and sample counts, but not every fine geography or identifier in the public download. It now directs requests for additional data to RUC's newer social-science data platform; verify that platform's current terms before treating it as an equivalent route.
  - route: RUC CEPS project documentation
    access_status: documentation-only
    direct_url: https://ceps.ruc.edu.cn/xmjs/xmgk.htm
    requirements: Use the project documentation to confirm design and current release links.
    steps:
    - Read the project overview and sampling documentation.
    - Follow the current data-release instructions to the authorized archive.
    deliverable: Survey design, baseline scope, questionnaires, and release notices.
    cost: free
    last_checked: '2026-08-12'
    caveat: The project site is the producer's documentation layer; it is not by itself evidence that every microdata file can be downloaded without an archive account.
  - route: PKU Open Research Data Platform 2014 baseline mirror
    access_status: available-with-login
    direct_url: https://doi.org/10.18170/DVN/KURJUU
    requirements: Dataverse account/login; cite the deposit and inspect its file-level metadata.
    steps:
    - Open the DOI deposit and review version, file list, and terms.
    - Download the questionnaire and files labelled as 2014 CEPS baseline data.
    - Treat the deposit as a mirror/subset unless it is independently shown to equal the official release.
    deliverable: The checked deposit lists a student questionnaire, SPSS student file, and a processed tabular student file; it does not establish complete multi-respondent or unrestricted geographic coverage.
    cost: free
    last_checked: '2026-08-12'
    caveat: This is a public research-data deposit by a named depositor, not proof that all official CEPS waves, identifiers, weights, or geographies are present.

access:
  url: https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
  cost: free
  license: Use the current CNSDA/RUC and file-level terms; academic citation is required, and sensitive geography or identifiers may be restricted.
  format:
  - dta
  - sav
  - pdf
  - xlsx
  api: false
  how_to_get: Register/login to CNSDA, open the relevant CEPS release, read the documentation and variable crosswalk, then download the permitted respondent files. Use the PKU DOI deposit only as a separately cited baseline mirror.
caveats: CEPS is school-based rather than a general local-economy panel. The baseline design is nationally representative at its stated sampling level, but the 28 county-level PSUs are not a census of Chinese counties. Student, parent, teacher and administrator files have different units and identifiers. A paper's classroom-level peer share, civil-servant-family indicator, or other constructed measure is a derived variable, not a raw CEPS field. Fine geography, weights, attrition, and the availability of later waves must be checked in the exact release used.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

used_by:
  - cite: 'Li & Wu (2026), Parental Social Capital Spillovers in Children''s Noncognitive Skills Formation: Evidence from Random Classroom Assignment in China'
    doi: https://doi.org/10.1016/j.chieco.2026.102748
    journal: CER
    year: 2026
    dataset_role: Main student, family, class, teacher and school-context evidence for peer-parent social-capital spillovers
    evidence_type: publisher_page_and_crossref
    evidence_url: https://www.sciencedirect.com/science/article/pii/S1043951X26000982
    data_note: The publisher page identifies the 2013-2014 CEPS baseline and its random classroom-assignment setting. The paper studies class exposure to children of civil-servant families, noncognitive skills, friendship networks and teacher-student relationships. The paper use supports the baseline CEPS role; it does not imply that its classroom-derived exposure variable or analysis file is a separate downloadable dataset.

provenance:
  - source: RUC CEPS project overview https://ceps.ruc.edu.cn/xmjs/xmgk.htm
    field_scope:
    - producer
    - baseline design
    - national scope
    - project identity
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: CNSDA CEPS 2014-2015 catalog https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
    field_scope:
    - follow-up wave
    - respondent files
    - variable counts
    - sample counts
    - access route
    - questionnaires and documentation
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: Current CNSDA CEPS 2014-2015 catalog recheck https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
    field_scope:
    - current catalog availability and registration entry point
    - 28-PSU, 112-school, 438-class sampling description
    - current 20-item catalog inventory, including questionnaires, manual, cross-wave table, and four respondent-file types
    - notice that additional-data requests are directed to RUC's newer social-science data platform
    added: '2026-09-27'
    confidence: high
    verified: true
  - source: PKU Open Research Data Platform deposit https://doi.org/10.18170/DVN/KURJUU
    field_scope:
    - public baseline mirror
    - file formats
    - deposit metadata
    - file-level terms
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: China Economic Review article page https://www.sciencedirect.com/science/article/pii/S1043951X26000982 and Crossref DOI metadata https://doi.org/10.1016/j.chieco.2026.102748
    field_scope:
    - Li and Wu authorship
    - 2026 publication
    - actual CEPS baseline use
    - classroom and outcome roles
    added: '2026-08-12'
    confidence: high
    verified: true

related_datasets:
  - id: cfps
    relation: complement
  - id: cgss
    relation: complement
---

## Positioning in one sentence

CEPS is a nationally sampled, school-based longitudinal survey that places students, parents, teachers, and school administrators around the same lower-secondary classrooms. It is especially useful when a research question needs peer composition and school context together; it is not a substitute for a dense county-year economic panel, and the public route must be distinguished from each paper's derived classroom file.

## Select rules

- Prioritize CEPS when the outcome is adolescent learning or noncognitive development and the mechanism runs through classmates, families, teachers, or school resources.
- Use the CNSDA release as the primary acquisition route and the PKU DOI deposit as a separately cited baseline mirror. Check the exact wave, file language, weights, attrition documentation, and geography fields before constructing a panel.
- Switch to CFPS or CHFS when the question needs broad household, adult, asset, labor-market, or annual local-economic coverage. Do not infer a county-level policy effect merely because CEPS sampled counties.

## Get recipe

1. Start at the CNSDA CEPS catalog and register/login.
2. Read the data-use manual and two-wave variable crosswalk before downloading respondent files.
3. Download only the permitted student, parent, teacher, and administrator files for the target wave, preserving their original file names and identifiers.
4. Build classroom or peer variables from the respondent files only after documenting inclusion rules. A paper's cleaned peer share is a constructed analysis variable, not an official CEPS download.
5. For local joins, confirm the approved county/district key and the reference year; if fine geography is absent, use a documented coarser match or stop.

## Connections and Limitations

The survey's strength is its nested school/class/respondent structure. The practical risk is assuming that a student file alone contains the parent, teacher, school, weights, or geography components needed for a paper. The 28 baseline PSUs support national survey inference at the design's stated level but do not support arbitrary county rankings. The 2014-2015 CNSDA release and the PKU baseline mirror have different samples and file inventories; never merge them without checking identifiers and attrition.

## Decision sufficiency check

For a question about how classmates' family background affects student outcomes, choose CEPS, obtain the relevant student/parent/class/teacher files through CNSDA, reconstruct the classroom measure, and treat any local policy or weather variable as a separately sourced join. For a question about annual city housing prices or county economic growth, choose CHFS/CFPS or an official local panel instead. This is a `ready` route for the documented CEPS files, not a claim of unrestricted geographic access or paper-file reproducibility: the catalog is sufficient to select the survey and start lawful acquisition, but not to assume every requested geography field or a paper's cleaned analysis file is available.
