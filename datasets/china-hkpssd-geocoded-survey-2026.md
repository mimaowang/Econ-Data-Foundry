---
schema_version: 3
catalog_status: grounding
id: china-hkpssd-geocoded-survey-2026
name: Hong Kong Panel Study of Social Dynamics (HKPSSD) linked to LSBG-level census neighborhood statistics (Zhang & Zhang 2026 Urban Studies)
aka:
- HKPSSD
- 香港社会动态追踪调查
- 香港社會動態追蹤調查
- Geospatial relative income and subjective well-being in Hong Kong
provider: HKPSSD executed by the Center for Applied Social and Economic Research (CASER), Hong Kong University of Science and Technology (now CAESER - Center for AI in Economic Social and Environmental Research, HKUST), with funding from the RGC-CPU Strategic Public Policy Research scheme and the RGC Collaborative Research Fund; the 2026 paper adds census/by-census LSBG aggregates from the Hong Kong Census and Statistics Department and WorldPop gridded population
china_related: true
domains:
- housing
- urban
- household
- inequality
- well-being
- hong-kong
- neighborhood

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: "The paper's analysis file: pooled HKPSSD W1 (2011) + W4 (2017-2018) individual-level records (8,703 obs) and a balanced panel (1,797 respondents / 3,594 person-year) geocoded to large street block groups (LSBG) and matched to 2011 Population Census / 2016 Population By-Census LSBG income statistics. The HKPSSD microdata are a restricted survey; the paper's exact linked analysis file is not released (no data-availability statement, no replication package found)."
  availability: restricted
  ordinary_researcher_feasible: false
  summary: The paper uses geocoded individual-level HKPSSD survey data (W1 2011 and W4 2017-2018) matched to quinquennial Hong Kong census/by-census statistics at the large street block group (LSBG) level to construct neighborhood and adjacent-neighborhood income contexts. HKPSSD is a restricted academic panel survey run by HKUST CASER/CAESER; access was granted to the authors by CASER, and a documented institutional application route exists at SYSU (internal use only). No general public download or application channel is documented in the sources read this round.
  barrier: HKPSSD microdata are shared by institutional agreement (paper acknowledgments thank HKUST CASER for granting access; SYSU 粤港澳发展研究院 shares waves W1-W4 to its own researchers via an internal application form). A general public application route from HKUST is not documented in the read sources.

unit_of_observation: Individual respondent (aged 15+ in W1) in the HKPSSD household panel; paper analysis at person level with residential LSBG context
structure: Repeated panel waves (W1 2011, W2 2013, W3 2015, W4 2017-2018; refreshment samples in W2B 2014 and later); paper uses pooled W1+W4 and a balanced two-wave panel
geo_granularity:
- large street block group (LSBG) of residence (median residential population ~2,200 per the paper)
- Hong Kong SAR
geography: Hong Kong Special Administrative Region; LSBG-level residential location linkage to census statistical units
time_span:
  start: '2011'
  end: '2018'
  last_confirmed_release: null
  coverage_note: "HKPSSD waves: W1 2011 (7,218 respondents aged 15+ from 3,214 households per the paper; 958 children additionally per CASER page), W2 2013 (2,165 households re-interviewed per SYSU notice), W2B refreshment 2014 (1,007 households), W3 2015 (2,404 households re-interviewed per SYSU notice), W4 Aug 2017-Sep 2018 (3,407 respondents from 2,000 households per the paper). The 2026 paper uses W1 and W4 only. Later waves (2019+ refreshment, 2021 follow-up per CASER) not used in this paper."
  last_checked: '2026-08-15'
frequency:
- wave-based (2011, 2013, 2015, 2017-2018)
sample_size: "Paper analysis sample: 8,703 pooled observations (5,652 W1 + 3,051 W4) and 1,797 balanced-panel respondents (3,594 person-year). Survey: W1 7,218 adults / 3,214 households."
key_variables:
- Life satisfaction (Satisfaction with Life Scale, 5 items, 7-point scale, averaged)
- Average monthly household income for the previous year (earnings, bonuses, commissions, housing/other cash allowances; bracketed responses converted via midpoints per Cheung & Lucas 2016)
- Residential LSBG of the household (linkage unit to census statistics)
- LSBG median monthly domestic household income (from quinquennial census/by-census)
- Relative household income (RHI) and relative neighborhood income (RNI) with asymmetric richer/poorer decompositions
- Temporal changes in RHI/RNI between 2011 and 2016 census vintages
- WorldPop 100-m gridded population for population-weighted LSBG centroids; queen-contiguity adjacency and distance weights (P_j/d_ij^2)

research_fit:
  best_for:
  - "Hong Kong household and neighborhood contextual research: geocoded individual outcomes (well-being, attitudes, health) linked to LSBG-level census income/neighborhood statistics"
  - "Relative-income and comparison-context studies in HK: RHI within neighborhood and RNI vs adjacent neighborhoods, with asymmetric (richer/poorer, positive/negative change) decompositions"
  - "Neighborhood-effects research exploiting quinquennial census vintages (2011 Census, 2016 By-Census) for time-varying LSBG context"
  choose_over:
  - Choose over mainland household surveys (cfps, chfs) when the population of interest is Hong Kong SAR residents and the neighborhood context must come from HK census LSBG units.
  - Choose over one-off HK cross-section surveys when panel structure (W1-W4 with refreshment) and longitudinal neighborhood context are needed.
  not_good_for:
  - "Research on movers' outcomes: the paper documents that follow-up waves did not record new addresses of movers, so movers are excluded from the matched analysis (self-selection into neighborhoods unobserved)"
  - "Fine-grained geocoding below LSBG (no street/block-level addresses or coordinates released in the paper)"
  - "Mainland China populations or neighborhoods (HK SAR only)"
  - "Recent (post-2018) HK household data: the paper's matched window ends at W4 (2017-2018); later waves exist per CASER but are not documented by the paper"
  needs_join_for:
  - Treatment/policy timing (e.g., HOS, political shocks) must come from external sources; this record supplies survey outcomes and census-based neighborhood context
  - Activity-space or daily-mobility exposures (the paper flags these as unobserved limitations)
  variation_available:
  - Temporal variation in neighborhood income context across census vintages (2011 vs 2016) for non-movers; cross-sectional variation in RHI/RNI; panel variation in life satisfaction
  topics:
  - subjective well-being
  - relative income
  - neighborhood effects
  - Hong Kong
  - panel survey
  - geocoded survey
  - census small-area statistics
  - spatial inequality

good_for:
- Neighborhood-relative-income and well-being analysis in Hong Kong with census-based spatial context
identification:
- Comparison of richer vs poorer relative positions and positive vs negative temporal changes (asymmetric effects); not a causal-design record
linkable_keys:
- Residential LSBG (linkage to 2011 Census / 2016 By-Census small-area statistics)
- Household and individual panel identifiers within HKPSSD (internal; not public)
- Hong Kong Census and Statistics Department statistical geography (LSBG boundaries)

joins:
- target: china-census
  relation: complement
  keys:
  - LSBG (large street block group)
  method: HKPSSD residential LSBG to quinquennial census/by-census small-area aggregates (2011 Census for W1, 2016 By-Census for W4); queen contiguity and WorldPop-population-weighted centroids for adjacent-neighborhood construction
  evidence_status: literature-used
- target: china-nighttime-lights
  relation: complement
  keys:
  - Geography
  - Time
  method: Possible for spatial-context extension, not used in the 2026 paper
  evidence_status: plausible

access_routes:
- route: "Institutional application (documented example: SYSU 粤港澳发展研究院 internal sharing)"
  access_status: restricted
  direct_url: https://ygafz.sysu.edu.cn/article/104
  requirements:
  - "Affiliation with an institution holding an HKPSSD data agreement (SYSU example: internal to SYSU researchers only; application form + signed commitment submitted to liuyj75@mail.sysu.edu.cn)"
  - "Research-use agreement; data delivered by email (Stata .dta format per the SYSU notice)"
  steps:
  - Check whether your institution holds an HKPSSD sharing agreement (HKUST CAESER is the executing center; paper acknowledgments show CASER grants access).
  - If affiliated with SYSU 粤港澳发展研究院, download the application form from the notice page, sign the commitment, and submit per the page instructions.
  deliverable: HKPSSD wave data (W1-W4 and refreshment samples; Stata .dta); the notice lists W1 (2011), W2 (2013), W2B (2014), W3 (2015), W4 (2017)
  cost: by-application
  last_checked: '2026-08-15'
  caveat: "SYSU route is internal to that institution; a general public application channel from HKUST CAESER is not documented in the sources read this round. The 2026 paper itself confirms only that CASER granted the authors access."
- route: Read the paper's full text (open access, documents data construction)
  access_status: available
  direct_url: https://sage.cnpereading.com/doi/10.1177/00420980251409955
  requirements:
  - None (hybrid open access per OpenAlex; served in full by the CNPeReading SAGE mirror on 2026-08-15)
  steps:
  - Read the Data and Method sections for sampling (Frame of Quarters, stratified random), waves, LSBG definitions, and variable construction.
  deliverable: Full methodological documentation; NOT the data
  cost: free
  last_checked: '2026-08-15'
  caveat: journals.sagepub.com resets automated connections (2026-08-15); the CNPeReading mirror worked. OpenAlex's oa_url pointing at a statistics.gov.hk CPI PDF is a misparse - the article is OA at the publisher.
- route: HKPSSD questionnaire and survey documentation (caser.ust.hk hkpssd_data pages)
  access_status: needs-verification
  direct_url: http://caser.ust.hk/?act=hkpssd_data
  requirements:
  - None (questionnaire pages per the SYSU notice; automated fetch failed 2026-08-15 - connection aborted)
  steps:
  - Open in a human browser; the old caser.ust.hk domain may redirect to the current CAESER site (caeser.hkust.edu.hk, which confirms the survey on its homepage).
  deliverable: Questionnaires (Chinese and English) and survey documentation
  cost: free
  last_checked: '2026-08-15'
  caveat: Domain redirect behavior unverified this session.

access:
  url: https://caeser.hkust.edu.hk
  cost: by-application
  license: research-use agreement (per-institution)
  format:
  - dta (per SYSU notice)
  api: false
  how_to_get: Institutional data-sharing agreement with HKUST CAESER or an institution holding HKPSSD data rights (SYSU internal route documented; general public route not found)
caveats:
- "No public download; the SYSU notice (2017-11 update) is the only concrete application form found and it is internal to SYSU."
- "The paper's analysis file (W1+W4 linked to LSBG census statistics) is not released; no replication package found."
- "Movers excluded: follow-up waves did not record new addresses, so any reconstruction inherits the non-mover sample."

production:
  raw_sources:
  - name: HKPSSD survey microdata (W1-W4)
    source_type: dataset
    role: Individual/household outcomes (life satisfaction, income, sociodemographics) and residential LSBG
    access_route: Institutional agreement (CASER/CAESER)
    url: https://caeser.hkust.edu.hk
    coverage: W1 2011 - W4 2017/2018, HK-wide representative household panel; refreshment samples
    last_checked: '2026-08-15'
  - name: Hong Kong Population Census / By-Census small-area statistics (LSBG)
    source_type: dataset
    role: Neighborhood income context (LSBG median monthly domestic household income) and LSBG geography
    access_route: Official publications of the Census and Statistics Department
    url: https://www.censtatd.gov.hk
    coverage: Quinquennial (2011 Census for W1; 2016 By-Census for W4); LSBG units, median residential population ~2,200
    last_checked: '2026-08-15'
  - name: WorldPop 100-m gridded population estimates
    source_type: dataset
    role: Population-weighted LSBG centroids for inter-neighborhood distance weighting
    access_route: Public download
    url: https://www.worldpop.org
    coverage: 100-m resolution grid, HK
    last_checked: '2026-08-15'
  acquisition_methods:
  - records request (institutional application for HKPSSD)
  - download (census/by-census LSBG tables; WorldPop grids)
  sample_construction: "Paper-level: pooled W1+W4 after dropping missing values (8,703 obs) and balanced panel of respondents observed in both waves (1,797); movers excluded because W4 addresses were not recorded."
  pipeline_stages:
  - stage: match
    inputs:
    - HKPSSD residential LSBG
    - 2011 Census / 2016 By-Census LSBG statistics
    - WorldPop 100-m population grid
    method: "Link households' residential LSBG to census vintage corresponding to wave; compute population-weighted LSBG centroids; queen-contiguity adjacency; adjacent-neighborhood income weighted by P_j/d_ij^2"
    tools: []
    parameters:
    - "CPI adjustment (Oct 2014-Sep 2015 = 100): 81.6 for 2011 respondents, 104.5 (2017), 107.0 (2018)"
    output: Person-level file with LSBG income context, RHI, RNI, and temporal-change variables
    evidence: Paper data section and equations (1)-(5)
  constructed_variables:
  - name: RNI (relative neighborhood income)
    concept: Weighted average of adjacent LSBGs' median household income vs own LSBG
    source_fields:
    - LSBG median household income (census/by-census)
    - LSBG geography (queen contiguity)
    - WorldPop population (centroids and weights)
    method: Equation (1) with weights P_j/d_ij^2
    validation: None stated beyond census official statistics
    limitations: Modifiable areal unit problem and fuzzy boundaries acknowledged by the paper
  - name: RHI (relative household income)
    concept: Household income relative to its LSBG income context
    source_fields:
    - Household monthly income (survey)
    - LSBG median income (census)
    method: Distance between household income and neighborhood income context; asymmetric richer/poorer decomposition
    validation: None stated
    limitations: Bracketed income responses approximated by midpoints
  validation: []
  output:
    unit_of_observation: Person (HKPSSD respondent) with residential LSBG context
    structure: Pooled two-wave + balanced panel
    geography: Hong Kong SAR, LSBG level
    time_span: W1 2011 and W4 2017-2018 matched to 2011 Census / 2016 By-Census
    key_variables:
    - Life satisfaction (SWLS)
    - Household income
    - RHI, RNI and their richer/poorer and change decompositions
    formats: []
  reproducibility:
    level: low
    starting_point: HKPSSD microdata (restricted) + census LSBG statistics + WorldPop grid
    code_available: false
    code_url: null
    requirements:
    - Institutional HKPSSD access
    - Census/by-census LSBG tables
    - WorldPop grids and GIS processing
    blockers:
    - HKPSSD restricted access
    - No replication code or package found
  compliance:
    terms_or_license: Institutional research-use agreement (SYSU example requires signed commitment form)
    robots_or_rate_limits: null
    personal_or_sensitive_data: Survey microdata with household addresses (LSBG linkage); restricted distribution
    redistribution: Not permitted without agreement terms
    review_needed: true

quality:
  profile_status: grounded
  access_status: needs-verification
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: "Zhang C, Zhang Z (2026) Geospatial relative income and subjective well-being in Hong Kong: A spatiotemporal perspective concerning adjacent neighborhoods. Urban Studies 63(9):1957-1978"
  doi: 10.1177/00420980251409955
  journal: Urban Studies
  year: 2026
  dataset_role: Main result
  evidence_type: data-section
  evidence_url: https://sage.cnpereading.com/doi/10.1177/00420980251409955
  data_note: "Full text read via CNPeReading SAGE mirror 2026-08-15. Data section: HKPSSD W1 (2011, 7,218 respondents/3,214 households) and W4 (Aug 2017-Sep 2018, 3,407 respondents/2,000 households); stratified random sample on the Census and Statistics Department Frame of Quarters; CAPI face-to-face; W1/W4 linked to 2011 Population Census / 2016 Population By-Census at LSBG level; WorldPop 100-m grid for centroids; pooled n=8,703, balanced panel n=1,797; movers excluded (addresses not recorded in follow-ups); no data-availability statement; acknowledgments thank HKUST CASER for granting data access."

provenance:
- source: "Paper full text (open access, CNPeReading SAGE mirror, cached .b4-scratch-20260815/cnpe_hkpssd.html)"
  field_scope:
  - paper use
  - waves and sample
  - LSBG linkage
  - variable construction
  - access acknowledgment
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "SYSU 粤港澳发展研究院 notice (2017-11 update), https://ygafz.sysu.edu.cn/article/104"
  field_scope:
  - provider (HKUST CASER execution)
  - wave structure (W1 2011 / W2 2013 / W2B 2014 / W3 2015 / W4 2017)
  - institutional application route and deliverable format (dta)
  added: '2026-08-15'
  confidence: med
  verified: true
- source: "CASER NYU Shanghai project page https://caser.shanghai.nyu.edu/caser-projects/hkpssd/ and CAESER HKUST homepage https://caeser.hkust.edu.hk/"
  field_scope:
  - provider identity
  - funding (RGC SPPR and CRF)
  - sample counts (7,218 adults + 958 children; refreshment samples)
  added: '2026-08-15'
  confidence: med
  verified: true
- source: "Crossref and OpenAlex records for 10.1177/00420980251409955"
  field_scope:
  - bibliographic identity
  - open-access status (hybrid OA)
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: cfps
  relation: complement
- id: china-jrs-sweating-assets-housing-transactions-2026
  relation: complement
- id: china-ziroom-shared-housing-listings-2026
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

HKPSSD is Hong Kong's first city-wide representative household panel (HKUST CASER/CAESER, waves 2011-2018 and later), and the 2026 Urban Studies paper shows how its geocoded residential LSBG codes can be matched to quinquennial census/by-census neighborhood statistics; the survey itself is restricted (institutional agreement), the paper's linked analysis file is not released, and no general public application channel is documented yet.

## Select rules

- Choose this asset when the population is Hong Kong SAR residents and the design needs both individual panel outcomes (e.g., life satisfaction, income) and time-varying LSBG-level neighborhood context from official census small-area statistics.
- Choose over mainland household surveys (CFPS/CHFS) for HK questions; choose over one-off HK surveys when panel linkage across waves matters.
- Not suitable for mover trajectories (addresses of movers were not recorded in follow-ups), sub-LSBG geocoding, or questions requiring post-2018 matched data.

## Get recipe

1. Confirm whether your institution holds an HKPSSD data-sharing agreement; the executing center is HKUST CASER (now CAESER, caeser.hkust.edu.hk).
2. Documented example route: SYSU 粤港澳发展研究院 shares HKPSSD waves W1-W4 (Stata .dta) to its internal researchers via an application form and signed commitment (https://ygafz.sysu.edu.cn/article/104, contact liuyj75@mail.sysu.edu.cn); internal to SYSU only.
3. For the neighborhood layer, obtain quinquennial census/by-census LSBG statistics from the HK Census and Statistics Department (2011 Census for W1, 2016 By-Census for W4) and WorldPop 100-m population grids; reproduce the paper's adjacency weighting (queen contiguity, P_j/d_ij^2) and CPI adjustment.
4. Expect that the paper's exact analysis file is NOT downloadable: no data-availability statement, no replication package found (2026-08-15).

## Connections and Limitations

- Join key: residential LSBG (HK Census statistical unit, median residential population ~2,200). Census vintage must match wave (2011 vs 2016 by-census) - the paper links W1 to the 2011 Census and W4 to the 2016 By-Census.
- Restricted-key condition: HKPSSD microdata access is by institutional agreement; LSBG codes are released inside the survey but the analysis-level linkage requires the survey plus the census tables.
- Coverage break: movers are excluded (no new-address recording), so panel estimates identify effects of neighborhood change among non-movers only; attrition bias is acknowledged by the paper.
- The RNI measure changes meaning with LSBG boundary vintages; WorldPop population distribution is used for within-neighborhood centroid placement.

## Decision sufficiency check

An agent reading only this record can choose HKPSSD for HK household-neighborhood research, reject mainland surveys for HK questions, describe the restricted access (institutional agreement; SYSU internal application documented), name the census LSBG + WorldPop inputs for the neighborhood layer, and state that the paper's final linked file is unreleased and the general public application route from HKUST is still unknown.
