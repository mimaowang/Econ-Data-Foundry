---
schema_version: 3
catalog_status: ready
id: clds
name: China Labor-force Dynamics Survey
aka:
- CLDS
- China Labour-force Dynamics Survey
- 中国劳动力动态调查
provider: Center for Social Survey, Sun Yat-sen University
china_related: true
domains:
- labor
- development
- migration
- health
- education
- urban-rural
- public
- sociology
data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Individual, household, and community survey files from the CLDS rotating panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    CLDS is a ready-made longitudinal survey produced by Sun Yat-sen University.
    It is not a public-download corpus: the CNSDA catalog contains no files, but
    the provider's official 2017 notice documents registration and free academic
    applications for specified early waves, while recent public articles direct
    requesters to the provider website and cssdata@mail.sysu.edu.cn. A researcher
    can begin an approval-dependent request, then must verify the exact wave,
    modules, files and terms actually granted.
  barrier: >-
    Access is provider-controlled rather than a public download. The evidence does
    not establish a current general release inventory, automatic approval, later
    wave availability, identifiers, weights, or fine geography; do not substitute
    a historical registration announcement for confirmation of the requested file.
unit_of_observation: Individual-year, household-year, and community-year survey records
structure: Biennial rotating-panel survey with linked labor-force, household, and community layers
geo_granularity:
- individual
- family
- village/community
- county or city when the approved release supplies a usable key
geography: Mainland China sample covering 29 provinces or province-level units in the checked design descriptions; Tibet and Hainan are excluded, and exact public geography fields require the release used.
time_span:
  start: 2012
  end: 2016
  last_confirmed_release: 2016
  coverage_note: The checked design article describes three waves by 2017, and public descriptions identify the 2012, 2014, and 2016 waves. The CNSDA project execution field says 2012-, but later waves were not confirmed in the checked materials.
  last_checked: '2026-08-12'
frequency:
- biennial
sample_size: Not established in the checked official catalog or the 2025 paper; do not infer a wave sample size from secondary summaries.
key_variables:
- Labor-force participation, employment, occupation, work history, and earnings
- Education, migration, hukou, and demographic characteristics
- Health, mental or emotional status, and social attitudes where present in the release
- Household economic activity and family structure
- Community social structure, public services, and grassroots organization context
research_fit:
  best_for:
  - Individual and household labor-market outcomes linked to community context
  - Urban-rural, migration, hukou, employment, and social-attitude comparisons across confirmed waves
  - Mechanism or heterogeneity analyses that need labor-force and psychosocial measures rather than a firm panel
  choose_over:
  - Prefer CLDS over a general household-finance survey when the question needs working-age labor, migration, and community modules together.
  - Prefer CFPS when the question needs all-age family tracking or child-development measures; prefer CHFS when detailed assets, debt, and housing finance are central.
  not_good_for:
  - A dense annual city or county economic panel, firm-level production, or unrestricted local exposure at fine geography
  - School-age outcomes outside the labor-force sample or claims about later waves not confirmed in the release
  needs_join_for:
  - City, county, environmental, weather, or policy exposure requires an approved geography key, a reference year, and a separately sourced local panel.
  - Cross-wave work requires the actual identifiers, attrition documentation, weights, and harmonized questionnaires for each released wave.
  variation_available:
  - Observed labor, household, and community differences across survey waves; this record does not classify policies or causal treatment assignment.
  topics:
  - labor markets
  - migration
  - urban-rural inequality
  - community development
  - health and well-being
  - education and skills
  - social attitudes
good_for:
- Labor-force and employment transitions in China
- Household and community correlates of migration, hukou, and work outcomes
- Regional or urban-rural comparisons when the geography and weights in the approved release support them
identification:
- Rotating-panel or repeated-wave comparisons with documented sample and attrition rules
- Individual, household, and community-level comparisons; causal design must be established by the paper rather than inferred from the survey
linkable_keys:
- Wave and respondent or household identifiers as supplied by the release
- Community, county, or city code only when the approved file provides it and its meaning is documented
- Survey year and harmonized geography labels
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Approved province, county, or city code
  - Survey year
  method: Add local economic context only after verifying the release's geography key and boundary vintage; do not assume person-level matching.
  evidence_status: plausible
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - Approved community, county, or city geography
  - Survey year or interview period
  method: Aggregate exposure to the survey geography and interview window only after the permitted spatial key and timing are known.
  evidence_status: plausible
access_routes:
- route: CNSDA CLDS project catalog
  access_status: documentation-only
  direct_url: https://www.cnsda.org/index.php?id=75023529&r=projects%2Fview
  requirements: Use the catalog to confirm the project identity and follow the linked producer route; registration, application, and current data-use terms must be checked on the live route.
  steps:
  - Open the CLDS project page and record the current project metadata and external data URL.
  - Follow the producer's current data-release instructions rather than relying on the catalog's historical description.
  - Record the exact wave, files, permissions, identifiers, weights, geography fields, and terms before analysis.
  deliverable: Current project documentation or a confirmed handoff to an authorized CLDS release; the checked page itself listed zero documents/data.
  cost: by-application
  last_checked: '2026-08-12'
  caveat: CNSDA confirms the project but is not evidence that a current microdata file can be downloaded from that page.
- route: Sun Yat-sen University Center for Social Survey request route
  access_status: available-with-conditions
  direct_url: https://css.sysu.edu.cn/Data
  requirements: >-
    State the academic research purpose and personal information to the provider;
    access remains subject to the provider's response and current data-use terms.
  steps:
  - Start at the producer page or email cssdata@mail.sysu.edu.cn with the research purpose and personal information.
  - Request only the needed wave and modules, and obtain the provider's current approval or instructions before data transfer.
  - Preserve the release name, questionnaire, codebook, weights, geography restrictions, and access agreement.
  deliverable: Provider-approved CLDS wave files and accompanying documentation, if the request is accepted.
  cost: by-application
  last_checked: '2026-09-28'
  caveat: >-
    Recent articles confirm this request starting point, not a public download or
    automatic approval. Confirm the exact data release, wave, format, identifiers,
    weights and permitted geography in the provider's response.
access:
  url: https://www.cnsda.org/index.php?id=75023529&r=projects%2Fview
  cost: by-application
  license: Use only under the current Sun Yat-sen University or archive terms; the checked materials do not establish a general redistribution right.
  format:
  - dta
  - sav
  - csv
  api: false
  how_to_get: Begin a provider request via css.sysu.edu.cn or cssdata@mail.sysu.edu.cn, state the research purpose and personal information, then use only the specifically approved wave and fields. This is an approval-dependent route, not a public download.
caveats: CLDS is a labor-force and community survey, not a city-year statistics database or a firm census. The checked official catalog gives the project identity and design but no current files. The 2012/2014/2016 wave boundary is the last one confirmed as released here; sample sizes, weights, identifiers, attrition, later waves, fine geography, and the paper's cleaned mechanism file all require release-level confirmation. A request route is documented, but approval and the delivered material are not guaranteed.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'
used_by:
- cite: 'Zhang, Shen & Zhu (2025), Unintended Negative Impact of Environmental Regulation on Public Safety: Evidence from China'
  doi: https://doi.org/10.1016/j.chieco.2025.102562
  journal: CER
  year: 2025
  dataset_role: CLDS labor-force microdata used for the job-displacement, emotional-distress, and psychological-distress mechanism evidence
  evidence_type: publisher_full_text
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25002202
  data_note: The paper's full article text explicitly states that it uses CLDS data to examine job displacement in high-pollution industries and the emotional and psychological mechanisms connected to public-safety outcomes. The paper's main crime outcome is a separate city-level panel; CLDS is not treated as the source of that city panel or as a downloadable paper-specific mechanism file.
provenance:
- source: CNSDA CLDS project catalog https://www.cnsda.org/index.php?id=75023529&r=projects%2Fview
  field_scope:
  - project identity
  - Sun Yat-sen University responsibility
  - 2012- execution field
  - individual/family analysis units
  - biennial design
  - external producer data URL
  - zero listed documents/data in the checked catalog view
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Wang, Zhou & Liu (2017), CLDS design and practice https://doi.org/10.1177/2397200917735796
  field_scope:
  - rotating-panel design
  - biennial frequency
  - national labor-force survey identity
  - three waves described by 2017
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Zhang, Shen & Zhu (2025) ScienceDirect full article https://www.sciencedirect.com/science/article/abs/pii/S1043951X25002202
  field_scope:
  - actual CLDS use
  - job-displacement mechanism role
  - emotional and psychological distress role
  - distinction from city-level crime panel
  added: '2026-08-12'
  confidence: high
  verified: true
- source: CLDS 2016 method description https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0272199
  field_scope:
  - 2016 third-wave reference
  - 15-64 labor-force target
  - 29-province scope
  - application route historically described by a data user
  added: '2026-08-12'
  confidence: medium
  verified: true
- source: Sun Yat-sen University official notice, CLDS 2016 data opening https://isg.sysu.edu.cn/article/210
  field_scope:
  - 2012 and 2014 waves opened to the public through centre registration/application
  - 2016 wave offered to Sun Yat-sen University academic users through registration/application
  - provider described SPSS and Stata files plus questionnaires and technical manuals
  - rotating-panel design and the provider's CSS website contact
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Xiong & Sui (2024), Humanities and Social Sciences Communications, data-availability statement https://doi.org/10.1057/s41599-024-04326-1
  field_scope:
  - recent paper directs raw-data requests to the official CLDS website and cssdata@mail.sysu.edu.cn
  - paper-specific raw files were provider-authorized, not publicly redistributed
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Wang et al. (2025), PMC data-availability statement https://pmc.ncbi.nlm.nih.gov/articles/PMC12522228/
  field_scope:
  - provider-controlled/confidential status
  - request email asks for purpose and personal information
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- cfps
- cgss
- chfs
---

## Positioning in one sentence

CLDS is a biennial, multi-level labor-force survey from Sun Yat-sen University that links working-age individuals and households to village/community context. It is valuable for labor, migration, and urban-rural questions, but the current checked archive page lists no files, so a researcher must verify the live producer route and exact release before treating any wave as obtainable.

## Decision sufficiency check

For a question about how a local environmental change affects employment or distress, CLDS can supply the labor-force mechanism outcomes only after the approved wave and geography are obtained; a separate city or environmental dataset is still needed. For detailed household balance sheets choose CHFS, and for all-age family or child outcomes choose CFPS. Do not use the CLDS record as evidence that the 2025 paper's city crime panel, policy treatment, or cleaned analysis file is public.
