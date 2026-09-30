---
schema_version: 3
catalog_status: ready
id: china-restud-melon-market-labels-2025
name: Shijiazhuang watermelon retail-market experiment data (sellers, transactions, household purchases; Bai 2025 ReStud)
aka:
- Melons as Lemons replication package
- Bai watermelon branding experiment data
- Zenodo 10.5281/zenodo.13909671
- 石家庄西瓜市场品牌标签实验数据
provider: Jie Bai (author); field experiment conducted in Shijiazhuang, Hebei, China (2014); replication package on Zenodo (CC-BY-4.0)
china_related: true
domains:
- development
- agriculture
- retail-markets
- information-economics
- field-experiment

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: >-
    The author's field-experiment dataset: 60 sellers in 60 Shijiazhuang watermelon
    markets randomized into 3 branding treatments (laser-cut label, sticker label,
    no label) crossed with an incentive treatment (6 groups); daily seller sales
    records (60,806 transactions, 19 Jul - 6 Sep 2014), biweekly sweetness quality
    checks, daily pricing/wholesale-price observations, and household purchasing
    diaries (675 households in 27 communities; 15,292 records; final analysis
    sample 4,309 watermelon purchases from 573 households in 26 communities).
    Published as a Zenodo replication package (10.5281/zenodo.13909671) under
    CC-BY-4.0 explicitly containing "all the STATA and Matlab codes as well as the
    original and intermediary data inputs".
  availability: reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The paper's full text (working-paper version) documents the experiment and
    data collection in detail, and the Zenodo DataCite record states the package
    contains the STATA/Matlab code and the original and intermediary data inputs
    for all tables and figures, under CC-BY-4.0. This is the strongest acquisition
    route among the current batch: a direct, free, license-clear download. The
    public record currently exposes a separate _readme.docx and two downloadable
    ZIP archives, including the later "Replication Package REStud 25751_v2.zip"
    (9,728,123 bytes). Its complete 270-member archive manifest was inspected on
    2026-09-28: it contains Stata seller transactions, quality sampling, surveys,
    household diaries and baseline/follow-up files; Matlab inputs; survey forms;
    Stata and Matlab code; and rendered results. Column-level content remains a
    separate inspection step.
  barrier: >-
    The archive is directly usable, but its public manifest alone does not document every variable label or confirm any difference between the cached working-paper text and the final ReStud version.

unit_of_observation: Seller-day records (sales transactions); seller-week (quality checks); household purchase records; households (panel)
structure: >-
  Multi-component: transaction-level seller sales (60,806 records), biweekly
  seller quality checks, daily pricing observations, household purchase diaries
  (panel), baseline/endline/follow-up surveys
geo_granularity:
- market (60 local markets; average distance between markets ~3 km)
- community (27 communities for household sample)
geography: Shijiazhuang, Hebei province, China (urban; over 800 gated communities and 200+ local markets in the city)
time_span:
  start: '2014-07'
  end: '2015'
  last_confirmed_release: '2024-11-25'
  coverage_note: >-
    Intervention 13-19 July 2014 (rolling-in excluded; day 1 = 19 July); phasing
    out 6-12 September 2014; sales records 19 July - 6 September 2014 (8 weeks);
    endline survey at final visit; two follow-up surveys after the intervention
    (including one year later). Replication package issued 2024-11-25 (DataCite).
  last_checked: '2026-09-27'
frequency:
- daily (seller sales, pricing observations)
- biweekly (quality checks, twice per week)
- purchase-record level (household diaries)
- survey wave (baseline/endline/follow-ups)
sample_size: 60 sellers in 60 markets; 60,806 transaction records (81% watermelon, 19% peach); 675 households in 27 communities, 15,292 purchase records; final household analysis sample 4,309 watermelon purchases, 573 households, 26 communities
key_variables:
- Seller: daily sales records (fruit type, quantity in Jin, sales value in RMB, quality category premium/normal), daily wholesale price, branding treatment (laser/sticker/label-less), incentive treatment, quality-check sweetness (center and side, averaged), pricing and differentiation behavior
- Household: purchase date, place, quantity, amount paid, satisfaction rating 1-5, whether bought from sample seller, whether fruit branded
- Baseline/endline/follow-up survey responses (sellers' future differentiation plans, consumer perceptions)
- Stratification: baseline average housing price in surrounding gated communities (above/below median)

research_fit:
  best_for:
  - Field-experimental evidence on quality signaling, seller reputation, and consumer learning in developing-country retail markets
  - Estimating how branding technologies (costly signaling) affect seller quality provision, prices, sales, and profits
  - Structural estimation of consumer learning and seller reputation (the paper estimates an empirical model on the experimental variation)
  - Welfare analysis of information frictions and market fragmentation in agricultural retail
  choose_over:
  - Choose this over china-weekly-provincial-hog-prices when the question is quality signaling and seller behavior at transaction level, not a price panel.
  - Choose this over survey-based market studies when randomized branding treatments and both seller-side and household-side records are needed.
  - For other crops or other cities, the experiment must be re-run; the data are specific to Shijiazhuang watermelons, summer 2014.
  not_good_for:
  - National or provincial agricultural market statistics (60 markets in one city, one season)
  - Post-2015 market behavior (follow-ups cover longer-term seller behavior, but the main panel is 2014)
  - Questions needing large-N seller or market samples (60 sellers; one per market by design)
  - Reconstructing the experiment's raw context (e.g., city-wide sales) beyond the recorded fields
  needs_join_for:
  - City-level context or controls (e.g., weather during the season) if needed for robustness
  - Other retail-market data for generalizing beyond watermelons
  variation_available:
  - Market-level randomization into 6 treatment cells (3 branding x 2 incentive)
  - Temporal variation: mandatory differentiation (first 2 weeks) vs free choice; incentive removal at week 6 (unanticipated)
  - Data-side variation dimensions only; the identification design belongs to the Econ-Variation repository.
  topics:
  - quality signaling
  - seller reputation
  - consumer learning
  - field experiment
  - agricultural markets
  - branding

good_for:
- Signaling and reputation experiments in retail markets
- Structural models of consumer learning estimated on experimental data
- Household purchase-diary analysis of demand responses to quality signals
identification:
- This is a released experimental-data asset: it supports reproducing the paper's randomized-branding analysis, but the public files themselves do not establish external validity beyond the 60 Shijiazhuang markets and the documented 2014 study window.
linkable_keys:
- Seller identifier (60 sample sellers)
- Market identifier (60 markets) and community identifier (27 communities)
- Date (day-level records)
- Household identifier (household diaries)

joins:
- target: china-weekly-provincial-hog-prices
  relation: often-confused-with
  keys:
  - None (different commodity, unit, and geography)
  method: Keep the Shijiazhuang experiment separate from the provincial hog-price panel; they answer different questions.
  evidence_status: verified

access_routes:
- route: Zenodo replication package (ReStud)
  access_status: available
  direct_url: https://zenodo.org/doi/10.5281/zenodo.13909671
  requirements:
  - None; CC-BY-4.0 license
  steps:
  - Open the Zenodo record 10.5281/zenodo.13909671 (latest version) or the concept DOI 10.5281/zenodo.13909670.
  - Download _readme.docx and the latest named archive, "Replication Package REStud 25751_v2.zip" (9,728,123 bytes in the record checked 2026-09-27).
  - Read the README and select the needed data path: data/stata/ contains seller_transactions.dta, seller_transactions_collapsed.dta, qualitysampling.dta, household_diary.dta, baseline/follow-up and surveyor files; data/matlab/ contains the structural-estimation inputs.
  - Use code/stata do files/ and code/matlab m files/ for replication, then check the paper's final ReStud version for any data-section differences.
  deliverable: A directly downloadable v2 archive with named Stata data, Matlab inputs, survey instruments, Stata/Matlab code, and rendered tables/figures; table columns and the published-version comparison remain to be checked for a new analysis.
  cost: free
  last_checked: '2026-09-27'
  caveat: Zenodo API and the complete v2 ZIP manifest confirm the practical file-level route. The archive listing does not itself establish every variable label or all researcher-side privacy decisions.
- route: Paper full text (working-paper version)
  access_status: available
  direct_url: needs-verification
  requirements: None
  steps:
  - Read the working-paper full text (cached copy) sections 4-5 for the experimental design and data-collection details.
  - Cross-check with the published ReStud version (92(6): 3574-3610) for any changes.
  deliverable: Design and data documentation; not the data.
  cost: free
  last_checked: '2026-08-15'
  caveat: The cached text is the job-market-paper version; the published version's data section was not read this round.

access:
  url: https://zenodo.org/doi/10.5281/zenodo.13909671
  cost: free
  license: CC-BY-4.0
  format:
  - STATA files
  - Matlab files
  - CSV and MAT inputs
  - DOCX survey instruments and README
  api: true
  how_to_get: Download the public v2 Zenodo ZIP, read its README, select the Stata or Matlab data path, and run the supplied code after checking local dependencies.

caveats:
- The complete public v2 ZIP manifest is verified: it includes Stata seller transactions, quality sampling, household diary/baseline/follow-up and surveyor files; Matlab inputs; survey forms; Stata/Matlab code; and results. Inspect table labels before using any field beyond its filename-level description.
- The cached full text is the working-paper version; the ReStud-published version (2025, vol 92) may differ in data details.
- Sample is one city (Shijiazhuang), one season (summer 2014), 60 sellers (one per market by design) - no national generalization.
- Only the "Jingxin" watermelon breed is used in the analysis (other breeds <2% of recorded sales).
- Sellers' self-recorded sales have known recording noise; the paper validates with surveyor-counted branded-watermelon records and self-recalled totals.
- Household analysis sample drops households with 3+ missing weekly records (final: 573 households, 26 communities, 4,309 watermelon purchases).

production:
  raw_sources:
  - name: Author field experiment (Shijiazhuang, 2014)
    source_type: dataset
    role: All experimental data (sales, quality, pricing, household diaries, surveys)
    access_route: Released as the Zenodo replication package
    url: https://zenodo.org/doi/10.5281/zenodo.13909671
    coverage: 60 sellers, 60 markets; 19 Jul - 6 Sep 2014; 675 households, 27 communities
    last_checked: '2026-08-15'
  acquisition_methods:
  - in-person survey (baseline/endline/follow-ups)
  - seller daily record sheets (sales)
  - surveyor daily market visits (pricing, branding service, counts)
  - biweekly unannounced quality checks (sweetness meter)
  - household purchase diaries
  sample_construction: >-
    60 sellers recruited from 60 different markets (one per market; 3-5 fruit
    sellers per market typically) following initial screening and sequential
    selection (Appendix C.1 of the paper); sellers randomized into 6 groups (3
    branding x 2 incentive), stratified on baseline housing prices of surrounding
    gated communities; 675 households in 27 communities recruited for purchase
    diaries, evenly distributed across treatment groups; households with 3+ missing
    weekly records dropped (final 573 households, 26 communities).
  pipeline_stages:
  - stage: collect
    inputs:
    - Seller daily sales records
    - Quality checks (twice weekly, sweetness meter)
    - Surveyor daily pricing visits and branding service
    - Household diaries
    - Surveys
    method: Field experiment with daily/biweekly data collection over 8 weeks
    output: Transaction records (60,806), quality checks, pricing series, household panel
    evidence: Paper sections 4.1 and 4.3
  - stage: clean
    inputs:
    - Seller records (omissions, lumped sales)
    - Household diaries (missing place/branding/satisfaction)
    method: Exclude rolling-in period (pre-19 July); validate with surveyor counts and recalled totals; match household-seller data for missing info; drop households with 3+ missing weekly records
    output: Analysis samples (sellers full; households 573/26 communities; 4,309 watermelon records)
    evidence: Paper section 4.3 and Appendix C.2
  constructed_variables:
  - name: Sales profit
    concept: Daily sales profit computed from sales quantity and prices
    source_fields:
    - Seller sales records
    - Prices
    method: Sales quantity x price-based computation (paper section 4.3 footnote 34)
    validation: Paper text
    limitations: Recording noise; validated against surveyor counts
  - name: Watermelon quality (sweetness)
    concept: Average sweetness measured at center and side
    source_fields:
    - Biweekly quality checks
    method: Sweetness meter; average of center and side readings
    validation: Maps to consumer ratings (sweetness >10.5 roughly maps to subjective ratings)
    limitations: Quality checks are periodic, not continuous
  validation:
  - Recording-noise checks: self-recalled vs recorded totals; surveyor-counted branded melons sold vs seller records
  - Final sample characteristics compared to full sample (Appendix C.2)
  output:
    unit_of_observation: Seller transaction; seller-week (quality); household purchase record
    structure: Multi-component experimental dataset
    geography: Shijiazhuang urban markets and communities
    time_span: July-September 2014 (main); follow-ups to ~1 year after
    key_variables:
    - Sales (quantity Jin, value RMB, quality category)
    - Quality (sweetness)
    - Prices (retail and wholesale)
    - Treatment (branding x incentive)
    - Household purchases (date, place, quantity, amount, satisfaction, branding)
    formats:
    - STATA
    - Matlab
  reproducibility:
    level: high
    starting_point: https://zenodo.org/doi/10.5281/zenodo.13909671
    code_available: true
    code_url: https://zenodo.org/doi/10.5281/zenodo.13909671
    requirements:
    - STATA and Matlab (versions per README)
    - The downloaded package (code + original and intermediary data inputs)
    blockers:
    - Published ReStud version's data section not read (working-paper version cached)
  compliance:
    terms_or_license: CC-BY-4.0 (replication package)
    robots_or_rate_limits: Zenodo public download; no scraping needed
    personal_or_sensitive_data: Household diaries may contain personal consumption records; follow CC-BY-4.0 attribution and reasonable privacy handling
    redistribution: CC-BY-4.0 permits sharing with attribution
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Bai, Jie (2025), Melons as Lemons: Asymmetric Information, Consumer Learning and Seller Reputation, Review of Economic Studies 92(6): 3574-3610'
  doi: https://doi.org/10.1093/restud/rdaf006
  journal: Review of Economic Studies
  year: 2025
  dataset_role: Main dataset (field experiment on 60 sellers and 675 households) for signaling, reputation, and consumer-learning analyses
  evidence_type: data-section
  evidence_url: https://zenodo.org/doi/10.5281/zenodo.13909671
  data_note: >-
    Paper (working-paper version, cached) sections 4.1-4.3 document the design and
    data: 60 sellers in 60 Shijiazhuang markets; 6 treatment cells (3 branding x 2
    incentive); 60,806 transaction records (19 Jul - 6 Sep 2014); biweekly
    sweetness checks; daily pricing visits; 675 households / 15,292 purchase
    records (final analysis sample 4,309 watermelon purchases from 573 households
    in 26 communities). Zenodo replication package 10.5281/zenodo.13909671
    (CC-BY-4.0) contains STATA/Matlab code and original and intermediary data
    inputs per the DataCite description.

provenance:
- source: Working-paper full text (cached melon_nfe_pdf.txt), sections 1, 4.1-4.3, and appendix notes
  field_scope:
  - experiment design (treatments, timeline, stratification)
  - data collection (sales records, quality checks, pricing, household diaries, surveys)
  - sample construction and cleaning (rolling-in exclusion, household drops)
  - key figures (60,806 transactions; 675 households; final 4,309 records)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite records 10.5281/zenodo.13909670 (concept) and 10.5281/zenodo.13909671 (version)
  field_scope:
  - package existence, title, creator, year (2024-11-25), license (CC-BY-4.0)
  - description: "all the STATA and Matlab codes as well as the original and intermediary data inputs"
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Zenodo record API https://zenodo.org/api/records/13909671 and public v2 archive response
  field_scope:
  - current_public_access
  - top_level_file_inventory
  - archive_names_and_sizes
  - open_access_and_license
  added: '2026-09-27'
  confidence: high
  verified: true
- source: Complete public v2 ZIP archive manifest (downloaded and inspected 2026-09-28)
  field_scope:
  - exact code, results, Stata-data, Matlab-input and survey-instrument paths
  - practical archive structure and uncompressed size (18,911,698 bytes across 270 members)
  added: '2026-09-28'
  confidence: high
  verified: true
- source: ReStud page (via cached Crossref/abstract evidence)
  field_scope:
  - publication identity (ReStud 92(6), DOI 10.1093/restud/rdaf006)
  added: '2026-08-15'
  confidence: high
  verified: true
related_datasets:
- id: china-weekly-provincial-hog-prices
  relation: often-confused-with
---

## Positioning in one sentence

A complete field-experiment asset: 60 Shijiazhuang watermelon sellers (6 randomized branding x incentive cells) with 60,806 transaction records, biweekly quality checks, daily pricing, and household purchase diaries (675 households), released as a CC-BY-4.0 Zenodo replication package (10.5281/zenodo.13909671) that per its metadata includes the original and intermediary data inputs - the most directly reproducible asset in this batch.

## Select rules

- Prioritize it when the question is quality signaling, seller reputation, or consumer learning in a developing-country retail market with randomized branding treatments.
- Switch to china-weekly-provincial-hog-prices for a long price panel; switch to other survey assets for household welfare questions beyond the purchase diaries.
- It cannot support national agricultural statistics, other crops/cities, or post-2015 market behavior beyond the follow-up surveys.

## Get recipe

1. Download the Zenodo package (10.5281/zenodo.13909671; CC-BY-4.0, no account needed for public files).
2. Read the README and select data/stata/ for the seller, quality, household and survey layers, or data/matlab/ for structural-estimation inputs; use code/stata do files/ and code/matlab m files/ for replication.
3. Cross-check the data section of the published ReStud version (92(6)) against the cached working-paper text for any differences.
4. Run the code to regenerate tables/figures; extend only with the paper's cleaning rules (rolling-in exclusion, Jingxin breed, household completeness filters).

## Connections and Limitations

The dataset is self-contained (seller-market-household links with daily dates); joins to outside sources are limited by the single-city, single-season scope. The public v2 archive contains the named Stata, Matlab, survey, code and result paths, while column-level interpretation and any difference between the working-paper and published data sections remain separate checks. Quality (sweetness) is measured periodically, and seller records have known recording noise validated by surveyor counts.
