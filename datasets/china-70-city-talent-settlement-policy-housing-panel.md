---
schema_version: 3
catalog_status: ready
id: china-70-city-talent-settlement-policy-housing-panel
name: 'Zhang et al. (2023 PLoS ONE) 70-city talent-settlement-policy housing-price panel (Supporting Information S1 Data)'
aka:
- 10.1371/journal.pone.0280317.s001
- journal.pone.0280317.s001.dta
- Impact of new talent settlement policy on housing prices data
- 人才新政对房价影响的70城面板数据
provider: PLOS (publisher, open access); authors Zhang L, Li Y, Kung C-C, Wu B, Zhang C (depositors)
china_related: true
domains:
- housing
- urban
- regional
- labor
- migration
- public

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: "Supporting Information S1 Data of Zhang et al. (2023) PLoS ONE 18(3): e0280317: a Stata-format file (served as journal.pone.0280317.s001.dta, 214,404 bytes, 2026-08-14 verified Content-Disposition) containing the paper's estimation panel: 490 rows = 70 cities x 7 years (2013-2019), 84 variables, including per-city talent-settlement-policy implementation year (Lyear), a treat indicator, event-time dummies, seven policy-tool dummies, housing prices (hp), population, region dummies, controls, PSM and IV variables."
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: The paper's full estimation dataset is released as the article's S1 Data file, freely downloadable from journals.plos.org without registration under the article's CC-BY license. It provides the hand-collected city-level NTSP (new talent settlement policy) implementation year for all 70 sample cities (2013-2019), housing prices, policy-tool indicators and controls. Timing is at YEAR granularity only; no month-level effective dates, no administrative codes, and no analysis code (do-files) are released.
  barrier: The released file starts with a <stata_dta> XML envelope; it was verified readable via pandas read_stata (pandas 3.0.3, 2026-08-14). Native Stata compatibility was not verified in this environment; check with the reader/version you plan to use. Automated fetch of the SI worked with a plain python requests client (no Cloudflare/login), so no barrier for retrieval itself.

unit_of_observation: City-year (70 large and medium-sized Chinese cities, 2013-2019)
structure: balanced annual panel (70 cities x 7 years = 490 rows)
geo_granularity:
- city
geography: "70 large and medium-sized cities from the NBS 2005 75-city housing-statistics list (based on economic strength, residential transaction volume, city size, and regional spread); cities identified by Chinese names only (e.g., 杭州市, 深圳市), no administrative codes in the file"
time_span:
  start: '2013'
  end: '2019'
  last_confirmed_release: '2023-03-24'
  coverage_note: 'Paper data section (read 2026-08-14): sample frame is the NBS 2005 list of 75 large/medium cities; the analysis uses 70 cities; 2017 set as the first policy-implementation year, sample period 2013-2019. File check (read 2026-08-14): 490 rows, 70 unique cities, 7 years each.'
  last_checked: '2026-09-27'
frequency:
- annual
sample_size: 490 city-year observations (70 cities x 7 years); 46 cities coded treated (Lyear 2015-2018), 24 cities control (Lyear 2013 or 2019)
key_variables:
- 'City (Chinese city name), year'
- 'hp: average annual housing price (RMB) - ln(hp) equals the paper''s outcome lnhou_price'
- 'Lyear: policy implementation year per city (2013: 7 cities, 2015: 1, 2016: 1, 2017: 14, 2018: 26, 2019: 21)'
- 'treat: 1 for 46 cities with Lyear in 2015-2018, 0 for 24 cities with Lyear 2013 or 2019 (paper''s own coding)'
- 'FT, FFT, F1T, F2T: policy-period interaction dummies; Dyear = year - Lyear; event-time dummies Before5..After4'
- 'Policy-tool dummies: ft (人才新政), Fm (高端人才引进计划), Uns (全面放开落户), Govs (政府提供补贴), Rs (租房补贴), Es (创业支持), Govsh (保障性住房)'
- 'Region dummies: East/Cen/West/NE (东中西部/东北), onetier/newonetier/Rest (一线/新一线/其他), Yz/Pr/Bj/RestM (长三角/珠三角/京津冀/其他都市圈), 北上广'
- 'Popu (population, 万人), lngdp, hou_inv, fin, hum_inv, city_size and other city controls'
- 'PSM variables (_pscore, _treated, _support, _weight) and IV variables (IV1/IV2, lnIV1/lnIV2) used in the paper''s robustness analyses'

research_fit:
  best_for:
  - Replicating or extending Zhang et al. (2023) DID/event-study estimates of the effect of new talent settlement policies (NTSP) on housing prices in China's 70 large/medium cities, 2013-2019
  - A released, machine-readable city-year panel with per-city talent-policy implementation YEAR (not month), housing prices, and seven policy-tool indicators, directly downloadable without registration
  - Studying policy-tool heterogeneity (cash subsidies, settlement liberalization, rental subsidies, entrepreneurship support, subsidized housing) in the 70-city sample
  choose_over:
  - Choose this released panel over resale "人才引进政策强度" indices (acadcn.cn/CSDN work-report keyword-frequency products) when policy definition, implementation timing and provenance matter: those indices lack policy definition, effective dates and provenance and cannot support event-study timing
  - Choose this over the 科学学研究 3308-policy corpus when a RELEASED file is required: the 3308 corpus (293 prefecture cities, 2002-2021) is not publicly released as of 2026-08-14
  - Choose this over PKULaw when a ready-coded city-year policy panel is needed rather than raw document text; use PKULaw for month-level timing reconstruction
  not_good_for:
  - Month-level or effective-date policy timing (the file records implementation YEAR only)
  - Cities outside the 70 NBS-2005-list cities (no county level, no 293-prefecture coverage)
  - Reproducing the paper's analysis pipeline (no do-files/code released; only the final estimation panel)
  - The 3308-policy / 293-city corpus of 叶杨/陈强远 et al. (科学学研究 2025/2026) - a different, unreleased asset
  - Causal identification claims about the talent war (assignment/design questions belong to the Econ-Variation repository)
  needs_join_for:
  - Administrative codes: the file has Chinese city names only; match to a city-code concordance (e.g., NBS codes) for joins
  - Month-level policy dates: reconstruct from PKULaw or city government websites (the paper collected them manually)
  - Other outcomes (migration, innovation, housing transactions): join by city-year (e.g., cmds, china-patents, china-land-transaction)
  variation_available:
  - Implementation-year variation across 70 cities (2013-2019) and policy-tool variation (7 dummy dimensions) are data dimensions in the released file; the paper's treatment coding (treat = Lyear 2015-2018) is the authors' own and is not a variation record
  topics:
  - talent policy
  - housing prices
  - urban development
  - migration
  - place-based policy

good_for:
- DID and event-study analysis of talent settlement policies on city housing prices, 2013-2019, 70 cities
- Policy-tool heterogeneity analysis (subsidies vs settlement liberalization vs subsidized housing)
identification:
- The released panel supplies the authors' city-year policy timing, outcomes, controls, and event-time variables; it can reproduce or extend their published specifications, but the file alone does not establish policy assignment or causal validity.
linkable_keys:
- City name (Chinese)
- Year
- Lyear (policy implementation year)

joins:
- target: pkulaw
  relation: complement
  keys:
  - City
  - Policy document date
  method: Use PKULaw raw policy texts to recover month-level announcement/effective dates per city for the 70-city sample; the released panel only codes implementation year
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - City
  - Year
  method: The paper states housing prices and economic controls come from the China City Statistical Yearbook and China Regional Economic Statistical Yearbook; use the yearbook record for extending variables or validating hp
  evidence_status: literature-used
- target: china-jrs-sweating-assets-housing-transactions-2026
  relation: often-confused-with
  keys:
  - City
  method: 'Keep the two housing products separate: this record is a 70-city city-year average-price panel; that record is transaction-level second-hand housing in 26 cities for an extreme-heat study'
  evidence_status: verified

access_routes:
- route: PLoS ONE article page - Supporting Information direct download
  access_status: available
  direct_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317
  requirements:
  - No registration; open access (CC-BY)
  - python requests or any HTTPS client worked (verified 2026-08-14); no Cloudflare/login challenge
  steps:
  - Open the article page (or the DOI https://doi.org/10.1371/journal.pone.0280317).
  - Click "Supporting information S1 Data" (link https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0280317.s001&type=supplementary).
  - Download the file (served as journal.pone.0280317.s001.dta, 214,404 bytes).
  - Read with a Stata-compatible reader; verified readable with pandas read_stata (3.0.3) - the file begins with a <stata_dta> XML envelope, so confirm your reader/version handles it.
  deliverable: One Stata-format file (490 rows x 84 variables) - the paper's full estimation panel
  cost: free
  last_checked: '2026-09-27'
  caveat: Only the estimation panel is released; no do-files, no raw policy documents, no month-level dates, no codebook (variable definitions are in the paper's Table 1).
- route: Article full text (open access) for variable definitions and data description
  access_status: available
  direct_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317
  requirements:
  - Public web access
  steps:
  - Read the Data description section (sample frame NBS 2005 75-city list; housing prices from China City Statistical Yearbook and China Regional Economic Statistical Yearbook; NTSP info gathered manually from local government websites; 2017 as first policy-implementation year; sample period 2013-2019).
  - Read Table 1 for explanatory variable definitions and the Data Availability statement ("All relevant data are within the manuscript and its Supporting Information files").
  deliverable: Full article text, tables, DAS
  cost: free
  last_checked: '2026-09-27'
  caveat: The HTML full text was read directly this pass (2026-08-14); the article body contains no city x month policy-date appendix table.

access:
  url: https://doi.org/10.1371/journal.pone.0280317
  cost: free
  license: CC-BY 4.0 (PLoS ONE open access; applies to the article and its Supporting Information)
  format:
  - dta
  api: false
  how_to_get: Open the article DOI, download the Supporting Information S1 Data file, and read with a Stata-compatible reader (pandas read_stata 3.0.3 verified 2026-08-14).
caveats:
- Timing granularity is YEAR-level (Lyear = implementation year per city); the file does not contain month-level effective dates, and the article body has no city x date appendix table. Month-level dates require reconstruction from raw policy documents (PKULaw / city government websites).
- No administrative codes: cities are identified by Chinese names; a name-to-code concordance is researcher work.
- The file is the paper's final estimation panel (includes analysis-specific PSM/IV/event-time columns), not raw policy documents; no analysis code is released.
- "treat coding is the authors' own (46 treated: Lyear 2015-2018; 24 control: Lyear 2013 or 2019); verify against the paper's design before reuse. Design/identification questions belong to the Econ-Variation repository."
- The file format: served bytes begin with a <stata_dta> XML envelope; pandas 3.0.3 read_stata parses it (verified 2026-08-14), native Stata compatibility not verified in this environment.

production:
  raw_sources:
  - name: Local government websites / government work reports (NTSP policy information)
    source_type: webpage
    role: 'Manual collection of per-city talent settlement policy implementation timing (the paper: "We gathered the NTSP information for all prefecture-level cities manually from the websites that host the local government reports")'
    access_route: Public web; exact collection protocol not released
    url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317
    coverage: 75-city frame, timing coded to year level
    last_checked: '2026-08-14'
  - name: China City Statistical Yearbook and China Regional Economic Statistical Yearbook
    source_type: dataset
    role: Housing prices and city economic data (per-capita GDP, education expenditure, real estate investment, loan balance, city size)
    access_route: See china-stat-yearbook record
    url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317
    coverage: 70 cities, 2013-2019
    last_checked: '2026-08-14'
  - name: NBS 2005 75-city list (sample frame)
    source_type: document
    role: Sample frame - large and medium cities defined by the National Bureau of Statistics in 2005 by economic strength, residential transaction volume, city size, and regional spread; 70 of 75 enter the analysis
    access_route: Public NBS list; not included in the SI file
    url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317
    coverage: 75 cities
    last_checked: '2026-08-14'
  acquisition_methods:
  - manual coding
  - yearbook collection
  sample_construction: 'Paper data section (read 2026-08-14): 75 NBS-2005 large/medium cities as the frame; 70 cities with complete data enter the analysis; sample period 2013-2019 with 2017 as the first policy-implementation year; treated cities are those implementing NTSP within the window. File check: Lyear present for all 70 cities; 46 treated (2015-2018), 24 control (2013 or 2019).'
  pipeline_stages:
  - stage: collect
    inputs:
    - Local government websites
    - City statistical yearbooks
    method: Manually gather NTSP policy information from local government report websites; collect housing prices and economic data from the yearbooks.
    tools: []
    output: City-level policy timing and city-year prices/controls
    evidence: Paper data description section (read 2026-08-14)
  - stage: clean
    inputs:
    - Collected city-year data
    method: Code policy timing into year-level treatment variables (FT, Lyear, event-time dummies); build controls; construct PSM/IV variables for robustness analyses.
    tools:
    - Stata (inferred from the .dta output; not stated in the paper)
    output: Final estimation panel (490 x 84) released as S1 Data
    evidence: File inspection 2026-08-14; paper Table 1 variable definitions
  constructed_variables:
  - name: Lyear / FT / treat
    concept: City-level new talent settlement policy implementation timing (year granularity)
    source_fields:
    - Manually collected policy information from local government websites
    method: FT = 1 if the city implemented the policy in that year; Lyear = implementation year per city; treat = the paper's analysis coding (46 cities Lyear 2015-2018)
    validation: Internal consistency with Dyear = year - Lyear and event-time dummies verified 2026-08-14; ln(hp) equals the released lnhou_price variable
    limitations: Year granularity only; no month-level dates; no raw collection logs released
  - name: Policy-tool dummies (ft, Fm, Uns, Govs, Rs, Es, Govsh)
    concept: Which NTSP tools a city adopted in a given year (人才新政, high-end talent introduction plan, full settlement liberalization, government subsidies, rental subsidies, entrepreneurship support, subsidized housing)
    source_fields:
    - Policy text coding by the authors
    method: Binary indicators per city-year
    validation: Used in the paper's Table 10 heterogeneity analysis
    limitations: Coding protocol not released beyond Table 1 definitions
  validation: []
  output:
    unit_of_observation: City-year
    structure: Balanced panel 70 x 7 = 490 rows
    geography: 70 large/medium Chinese cities (NBS 2005 list), Chinese city names, no admin codes
    time_span: 2013-2019
    key_variables:
    - City, year, hp, Popu
    - Lyear, Dyear, treat, FT, FFT, F1T, F2T
    - Event-time dummies Before5..After4
    - Policy-tool dummies (7)
    - Region dummies (12)
    - Controls (lngdp, hou_inv, fin, hum_inv, city_size, etc.)
    - PSM and IV variables
    formats:
    - dta
  reproducibility:
    level: low
    starting_point: https://doi.org/10.1371/journal.pone.0280317 (S1 Data download)
    code_available: false
    code_url: ''
    requirements:
    - A Stata-compatible reader (pandas read_stata 3.0.3 verified 2026-08-14)
    - City-name-to-code concordance for external joins
    blockers:
    - No do-files or code released - the analysis pipeline itself is not reproducible from the SI
    - Month-level policy dates not released - exact NTSP dates require re-collection from government sources
  compliance:
    terms_or_license: CC-BY 4.0
    robots_or_rate_limits: None observed; direct download worked with a plain python requests client (2026-08-14)
    personal_or_sensitive_data: None - city-year aggregates only
    redistribution: Permitted with attribution under CC-BY
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

used_by:
- cite: 'Zhang L, Li Y, Kung C-C, Wu B, Zhang C (2023), Impact of new talent settlement policy on housing prices: Evidence from 70 large and medium-sized Chinese cities, PLoS ONE 18(3): e0280317'
  doi: https://doi.org/10.1371/journal.pone.0280317
  journal: PLoS ONE
  year: 2023
  dataset_role: Main estimation panel - housing prices (outcome), NTSP implementation timing (treatment), policy-tool indicators, controls, PSM and IV variables for the DID analysis
  evidence_type: replication
  evidence_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0280317.s001&type=supplementary
  data_note: >-
    Article full text and S1 Data read 2026-08-14. DAS: "All relevant data are within the manuscript and its Supporting
    Information files." Data section: sample = 75 large/medium cities defined by NBS in 2005, 70 in analysis, 2013-2019,
    2017 as first policy-implementation year; housing prices from China City Statistical Yearbook and China Regional
    Economic Statistical Yearbook; NTSP information gathered manually from local government websites. S1 Data
    (journal.pone.0280317.s001.dta, 214,404 bytes): 490 rows = 70 cities x 7 years, 84 variables; per-city Lyear
    (implementation year) for all 70 cities; treat = 1 for 46 cities (Lyear 2015-2018), 0 for 24 (Lyear 2013 or 2019);
    ln(hp) equals lnhou_price. No month-level dates, no admin codes, no code released.

provenance:
- source: PLoS ONE article page and full HTML body (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317, fetched and read 2026-08-14)
  field_scope:
  - paper identity and citation
  - data availability statement
  - data description section (sample frame, sources, manual collection)
  - supporting information listing (S1 Data, DTA)
  - absence of a city x month policy-date appendix table
  added: '2026-08-14'
  confidence: high
  verified: true
- source: S1 Data file downloaded from journals.plos.org (journal.pone.0280317.s001.dta; Content-Disposition and size verified 2026-08-14) and parsed with pandas read_stata 3.0.3
  field_scope:
  - file identity (490 x 84, 70 cities x 7 years 2013-2019)
  - variables (hp, Popu, Lyear, Dyear, treat, FT, event-time dummies, policy-tool dummies, region dummies, controls, PSM/IV)
  - per-city Lyear distribution and treat coding
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Paper data section (read 2026-08-14) for production origin
  field_scope:
  - NBS 2005 75-city sample frame
  - yearbook sources for prices/controls
  - manual collection of NTSP timing from local government websites
  added: '2026-08-14'
  confidence: high
  verified: true
- source: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0280317
  field_scope:
  - current_public_access
  - paper_identity
  - paper_use
  - data_availability_statement
  - coverage_and_production_summary
  added: '2026-09-27'
  confidence: high
  verified: true

related_datasets:
- id: pkulaw
  relation: complement
- id: china-stat-yearbook
  relation: complement
- id: china-jrs-sweating-assets-housing-transactions-2026
  relation: often-confused-with
- id: cmds
  relation: complement
---

## Positioning in one sentence

The Supporting Information of Zhang et al. (2023 PLoS ONE) is a freely downloadable, machine-readable Stata file containing the paper's full estimation panel: 70 large/medium Chinese cities x 2013-2019 with per-city talent-settlement-policy implementation YEAR, housing prices, seven policy-tool dummies and controls (CC-BY, no registration) - but timing is year-level only, there are no administrative codes, and no analysis code is released.

## Select rules

- Prioritize it when the research needs a released city-year panel with talent-settlement-policy timing for the 70 NBS-2005-list cities, 2013-2019, especially for DID/event-study housing-price work.
- Switch to PKULaw plus city government pages when month-level policy effective dates are essential (reconstruction route; the released panel cannot supply them).
- Do not use it for the 293-city / 3308-policy corpus of 叶杨/陈强远 et al. (科学学研究 2025/2026) - that corpus is a different, unreleased asset; do not substitute resale work-report keyword-intensity indices (no policy definition/timing/provenance).
- Do not treat the paper's treat coding or the talent-war assignment as a variation record; that belongs to the Econ-Variation repository.

## Get recipe

1. Open https://doi.org/10.1371/journal.pone.0280317 (no login; CC-BY).
2. Download the Supporting Information "S1 Data" file (journal.pone.0280317.s001.dta, 214,404 bytes).
3. Read with a Stata-compatible reader; pandas read_stata 3.0.3 was verified to parse the file (2026-08-14); confirm your reader/version handles the <stata_dta> envelope if needed.
4. Read the paper's Data description and Table 1 for variable definitions; note the year-level timing and the authors' treat coding.
5. For month-level dates or administrative codes, match Chinese city names to a code concordance and reconstruct policy dates from PKULaw or city government websites.

## Connections and Limitations

The natural unit is city-year; the file's Chinese city names are the join keys, requiring a name-to-NBS-code concordance for external merges. Housing prices and controls trace to the China City Statistical Yearbook and China Regional Economic Statistical Yearbook (see china-stat-yearbook). The released panel covers only 70 cities of the NBS 2005 75-city list, 2013-2019, at year granularity: it cannot answer month-level policy-timing questions, county/prefecture-universe coverage, or the 293-city corpus questions. The paper's treatment coding (treat = Lyear 2015-2018) and any identification design belong to the Econ-Variation repository, not to this data record.
