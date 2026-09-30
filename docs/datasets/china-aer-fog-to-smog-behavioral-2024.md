---
schema_version: 3
catalog_status: ready
id: china-aer-fog-to-smog-behavioral-2024
name: China air-quality-disclosure behavioral-response data (avoidance, defensive spending, mortality; Barwick, Li, Lin & Zou 2024 AER)
aka:
- From Fog to Smog replication data
- openICPSR project 193441
- China pollution-information program evaluation data (2011-2016 city-weekly)
provider: >-
  Multiple providers: UnionPay (bank-card transactions); Baidu (search indices);
  People's Daily (digital archive); Apple App Store (app release info); CFPS
  (public opinion); Growth from Knowledge/GfK (air purifier sales); China CDC
  Disease Surveillance Points (mortality); NASA MODIS (AOD); replication deposit
  at ICPSR/openICPSR
china_related: true
domains:
- environment
- health
- consumer-behavior
- urban
- public-information

data_pathway:
  mode: hybrid
  origin: researcher-collected
  target_artifact: >-
    A city-weekly (Jan 2011 - Apr 2016; mortality through Dec 2016) multi-outcome
    dataset measuring the behavioral and health response to China's 2013 real-time
    PM2.5 monitoring and disclosure program: Baidu "smog" search intensity, People's
    Daily coverage, mobile pollution-app availability, CFPS environmental-concern
    measures, UnionPay offline purchase frequency per active card, GfK monthly air
    purifier sales in 50 cities, CDC DSP city-week-age-cause mortality in 131 cities,
    and MODIS AOD city-week air quality. Published as openICPSR replication package
    10.3886/E193441V1.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The paper's full text documents a comprehensive multi-source database around
    the 2013 monitoring program (three staggered waves of cities): media and search
    awareness (People's Daily, App Store, Baidu), public opinion (CFPS 2012-2018,
    83,237 respondents in 126 cities), consumption behavior (UnionPay 1% card
    sample, ~18.3M active cards, 59% of national consumption), defensive spending
    (GfK air purifier sales, 50 cities, 2012-2016), mortality (CDC DSP, 73M persons
    in 131 cities, 5% representative sample), and pollution (MODIS AOD). The AER
    article page links the replication package to openICPSR (10.3886/E193441V1);
    The current DataCite record confirms an active, findable ICPSR v1 Data and Code
    deposit for this paper and points to the same openICPSR project. The deposit's
    file manifest has not been opened
    (openICPSR blocks automated clients), and several raw inputs (UnionPay
    transactions, DSP mortality, GfK sales) are restricted or commercial.
  barrier: >-
    openICPSR project pages return 403 to automated clients; the file manifest and
    formats are unverified. The most valuable raw inputs - UnionPay card
    transactions, CDC DSP mortality microdata, GfK sales data - are confidential or
    commercial; the replication package (if it includes them) is the only practical
    route, and its contents are unverified.

unit_of_observation: City-week outcome panel (multiple outcome datasets at city-week level); CFPS at individual respondent level; UnionPay at card-transaction level (1% sample)
structure: City-week panel of awareness, behavior, health, and pollution outcomes (2011-2016) plus survey and app-level components
geo_granularity:
- city (prefecture or higher)
- county/city district (DSP raw units, aggregated to city)
- national (media series)
geography: National; air purifier sales in 50 cities (~28% of population); mortality in 131 DSP cities (5% representative sample); CFPS in 126 cities
time_span:
  start: '2011-01'
  end: '2016-12'
  last_confirmed_release: '2024-04-01'
  coverage_note: >-
    City-weekly data January 2011 - April 2016; mortality through December 2016;
    CFPS waves 2012, 2014, 2016, 2018; GfK air purifier sales monthly 2012-2016.
    Replication deposit registered 2024-04-01 (DataCite).
  last_checked: '2026-08-15'
frequency:
- city-week (main)
- monthly (air purifier sales)
- survey wave (CFPS 2012/2014/2016/2018)
sample_size: Baidu index city-day; UnionPay ~18.3M active cards (1% sample) with all transactions; GfK 50 cities monthly; DSP 73M individuals in 131 cities; CFPS 83,237 respondents in 126 cities
key_variables:
- Baidu "smog" search index (city-day, 2011 onward)
- People's Daily articles containing "smog"/"air pollution"/"atmospheric pollution" with mentioned cities
- Mobile app release info (Apple App Store, scraped December 2015) for pollution and control categories
- CFPS perceived seriousness of environment (and other issues) on 1-10 scale, 2012-2018
- UnionPay offline purchase frequency per active card (city-week), merchant category (300+ categories), transaction amount and time; online transactions dropped
- Air purifier unit sales (residential and institutional), monthly, 50 cities (GfK)
- DSP mortality: total deaths by city-week-age group and by cause (2011-2016, 131 cities)
- MODIS AOD city-week (10x10 km grid, 30-min scans averaged; NASA Terra)
- Monitoring-program wave/timing (staggered rollout; field rollout dates manually collected from news media)
- Weather-station-based daily visibility (used in robustness)

research_fit:
  best_for:
  - Estimating the value of pollution information and the behavioral response to real-time air-quality disclosure (avoidance, defensive purchases)
  - City-week event-study designs exploiting staggered monitoring-program rollout across three waves
  - Joint analysis of awareness (searches/media), behavior (transactions), defensive spending, and health (mortality) responses to information
  - Cost-benefit evaluation of pollution monitoring and disclosure programs
  choose_over:
  - Choose this over china-air-quality-monitoring (monitoring-station PM2.5) when the question is the information/disclosure margin and behavioral response, not station coverage itself.
  - Choose this over china-pollution/china-satellite-pm25 when behavioral and health outcomes tied to disclosure timing are the core need.
  - The paper's own MODIS AOD measure serves pollution exposure for the pre-program period; china-satellite-pm25 may complement for other periods/products but is a different construction.
  not_good_for:
  - Monitoring-station network coverage or station-level data quality questions (use china-air-quality-monitoring)
  - Post-2016 outcomes (all main series end 2016)
  - Firm-level emissions or compliance analysis (use china-firm-pollution or china-environmental-enforcement)
  - Reconstructing the raw UnionPay, DSP, or GfK datasets: they are confidential/commercial and not publicly downloadable
  needs_join_for:
  - Ground-station PM2.5 after 2013 (china-air-quality-monitoring) for exposure validation or post-program periods
  - Household-level outcomes beyond CFPS public-opinion items (e.g., cfps for consumption/health modules)
  - Weather data (visibility used in robustness; temperature/humidity for controls)
  variation_available:
  - Three-wave staggered city rollout of the monitoring program (city-level event times; field dates manually collected from news media)
  - Weekly variation in MODIS AOD pollution exposure within cities
  - Data-side variation dimensions only; the identification design belongs to the Econ-Variation repository.
  topics:
  - air pollution
  - pollution information
  - avoidance behavior
  - mortality
  - defensive spending
  - air purifiers
  - environmental policy

good_for:
- Staggered-DiD/event-study evaluation of information disclosure programs
- Revealed-preference valuation of pollution information (search, trips, purifier purchases)
- Health benefits (mortality elasticity) of monitoring and disclosure
identification:
- This is a paper-specific city-week, survey, and code asset, not a stand-alone causal-variation record. It supports reproducing the documented pollution-information study and inspecting released fields; any new identification claim requires its own design assessment.
linkable_keys:
- City (prefecture-level codes/names)
- City-week time key
- CFPS individual/household identifiers (for survey components)
- Card identifiers (UnionPay 1% sample, restricted)

joins:
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - City
  - Week/date
  method: Ground-station PM2.5 (post-2013) validates or extends the MODIS AOD exposure measure; the fog paper itself uses monitoring data after rollout.
  evidence_status: literature-used
- target: china-satellite-pm25
  relation: often-confused-with
  keys:
  - City and week (different constructions: MODIS AOD direct retrieval vs modeled PM2.5)
  method: Do not equate AOD with modeled PM2.5; the paper deliberately uses AOD to avoid measurement contamination by the policy.
  evidence_status: plausible
- target: cfps
  relation: complement
  keys:
  - CFPS individual identifiers
  - City and year
  method: The paper uses CFPS 2012-2018 environmental-concern items; deeper CFPS modules can extend household-level analysis.
  evidence_status: literature-used

access_routes:
- route: openICPSR replication deposit (AEA Data and Code policy)
  access_status: available-with-conditions
  direct_url: https://doi.org/10.3886/E193441V1
  requirements:
  - Free ICPSR/openICPSR account; download terms per the deposit
  steps:
  - Open the AER article page (doi.org/10.1257/aer.20200956) and follow the Additional Materials > Replication Package link (https://doi.org/10.3886/E193441V1).
  - Alternatively go directly to https://www.openicpsr.org/openicpsr/project/193441/version/V1/view.
  - Download and read the README/manifest to confirm which datasets are included (the raw UnionPay/DSP/GfK inputs may be absent).
  deliverable: Data and code for the paper (per DataCite title); exact manifest unverified (openICPSR 403 to automated clients).
  cost: free
  last_checked: '2026-09-28'
  caveat: Current DataCite metadata verifies the active, findable v1 DOI and matching openICPSR route, but not a file manifest, license, or download terms. The deposit may contain derived/aggregated data only; UnionPay, DSP, and GfK raw inputs are separately restricted or commercial.
- route: Component public data sources (reconstructing awareness and pollution series)
  access_status: available-with-conditions
  direct_url: needs-verification
  requirements:
  - Baidu index (Baidu Index platform, account); People's Daily digital archive (public); MODIS AOD (NASA, public); CFPS (application route, see cfps)
  steps:
  - Rebuild the awareness series (Baidu "smog" index, People's Daily articles, App Store scrape) and the MODIS AOD city-week exposure from public sources.
  - Apply the paper's construction rules (keyword set, city-week aggregation, 1% card sample definition if applicable).
  deliverable: "A partial reconstruction: awareness, exposure, and CFPS components; not the UnionPay, GfK, or DSP components."
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Reconstruction reproduces inputs, not the paper's exact analysis file; the transaction, sales, and mortality components remain out of reach publicly.
- route: Restricted component routes (UnionPay, CDC DSP, GfK)
  access_status: blocked
  direct_url: needs-verification
  requirements:
  - UnionPay: not a public product; bank/clearinghouse cooperation needed
  - CDC DSP: restricted health data; application to Chinese CDC per their rules
  - GfK: commercial purchase from the market-research firm
  steps:
  - Pursue each component through its own access authority; expect long application or purchase processes.
  deliverable: Individual components at best; full paper replication still needs the author deposit.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: No public route was identified for these components this round; application/purchase terms are unverified.

access:
  url: https://doi.org/10.3886/E193441V1
  cost: free
  license: ICPSR deposit terms; component data have separate terms (UnionPay/CDC/GfK restricted or commercial)
  format:
  - replication package (data + code), formats unverified
  api: false
  how_to_get: Start from the AER article page Replication Package link (openICPSR 193441 V1, human browser); inspect the manifest for which components are released; rebuild public components (Baidu, People's Daily, MODIS, CFPS) only if the deposit is insufficient.

caveats:
- The paper's main series end April 2016 (mortality December 2016); no post-2016 coverage.
- UnionPay data: 1% random card sample (~18.3M active cards), offline transactions only (online dropped, ~5.1% of volume), merchant categories only (no item-level purchase detail).
- DSP mortality: 131 cities, 5% representative sample, city-week-age-cause counts (not individual records in the paper's use).
- GfK air purifier sales: 50 cities, ~28% of population, residential and institutional units.
- MODIS AOD is the paper's deliberate exposure choice (avoids measurement contamination by the policy); do not substitute modeled PM2.5 without checking comparability.
- The openICPSR deposit manifest is unverified (403 to automated clients); whether restricted components are included is unknown.

production:
  raw_sources:
  - name: UnionPay bank-card transaction database
    source_type: dataset
    role: Purchase trips/consumption behavior (offline transactions, merchant category, amount, time)
    access_route: Author access via UnionPay cooperation; 1% card sample used
    url: needs-verification
    coverage: 59% of national consumption; 22% of GDP (2015); city-week panel Jan 2011 - Apr 2016
    last_checked: '2026-08-15'
  - name: Baidu search index
    source_type: dataset
    role: Pollution awareness (keyword "smog", city-day search intensity)
    access_route: Baidu Index platform
    url: https://index.baidu.com/
    coverage: City-day since 2011; Jan 2011 - Apr 2016 used
    last_checked: '2026-08-15'
  - name: People's Daily digital archive
    source_type: archive
    role: Media coverage of "smog"/"air pollution" with mentioned cities
    access_route: Public digital archive
    url: needs-verification
    coverage: 2011-2016 article series
    last_checked: '2026-08-15'
  - name: Apple App Store (scraped December 2015)
    source_type: webpage
    role: Pollution-app availability vs control categories
    access_route: Scraped by the authors
    url: needs-verification
    coverage: Top 200 apps per pollution keyword plus control categories, December 2015
    last_checked: '2026-08-15'
  - name: China Family Panel Studies (CFPS)
    source_type: dataset
    role: Public opinion (perceived seriousness of environment and other issues)
    access_route: Application route (see cfps record)
    url: https://www.isss.pku.edu.cn/cfps/
    coverage: Waves 2012, 2014, 2016, 2018; 83,237 respondents in 126 cities
    last_checked: '2026-08-15'
  - name: Growth from Knowledge (GfK) air purifier sales
    source_type: dataset
    role: Defensive spending (units sold, residential and institutional)
    access_route: Commercial market-research data
    url: needs-verification
    coverage: Monthly 2012-2016, 50 cities (~28% of population)
    last_checked: '2026-08-15'
  - name: China CDC Disease Surveillance Points (DSP)
    source_type: dataset
    role: Mortality by city-week-age group and cause
    access_route: Restricted; Chinese CDC system
    url: needs-verification
    coverage: 73M persons in 131 cities (5% representative sample), 2011-2016; raw units 161 counties/city districts aggregated to city
    last_checked: '2026-08-15'
  - name: NASA MODIS AOD (Terra)
    source_type: dataset
    role: Ambient air quality (proxy for PM) at city-week
    access_route: Public NASA data
    url: https://modis.gsfc.nasa.gov/
    coverage: 10x10 km, 30-min scans, averaged to city-week 2011-2016
    last_checked: '2026-08-15'
  acquisition_methods:
  - institutional/commercial access (UnionPay, GfK)
  - restricted-data application (DSP)
  - public retrieval (People's Daily, MODIS)
  - scraping (App Store)
  - platform account (Baidu Index)
  - survey data application (CFPS)
  sample_construction: >-
    UnionPay: 1% random sample of cards with all associated transactions; online
    transactions dropped (~5.1% of volume); outcome = purchase frequency per active
    card (city-week). Mortality: DSP county/city-district units aggregated to city
    level. Air purifier sales: 50 cities, residential and institutional units,
    monthly. All series aligned to city-week (or wave) with monitoring-program
    rollout timing (three waves; field dates manually collected from news media).
  pipeline_stages:
  - stage: collect
    inputs:
    - All component sources listed above
    method: Author-assembled multi-source database; scraping, archive retrieval, platform accounts, restricted-data access
    output: City-week outcome panel plus survey/app components
    evidence: Paper section 2 and Table 1
  - stage: aggregate
    inputs:
    - UnionPay transactions
    - DSP county-level mortality
    - MODIS AOD grids
    method: Aggregate to city-week; 1% card sample; city-level mortality aggregation
    output: City-week series for behavior, mortality, pollution
    evidence: Paper section 2 (footnote on DSP aggregation; UnionPay outcome definition)
  - stage: match
    inputs:
    - City-week outcomes
    - Monitoring-program rollout timing (field dates)
    method: Event-time alignment; staggered program timing
    output: Event-study-ready city-week panel
    evidence: Paper sections 2-4
  constructed_variables:
  - name: Purchase frequency per card
    concept: Number of offline transactions in a city-week per active card (active = positive transactions in the city-year)
    source_fields:
    - UnionPay transactions and card sample
    method: Transactions / active cards per city-week
    validation: Paper section 2 (Bank Card Transactions)
    limitations: Item-level purchases unobserved; merchant categories only
  - name: City-week AOD
    concept: Average aerosol optical depth as pollution proxy
    source_fields:
    - MODIS AOD (10x10 km, 30-min)
    method: Average to city-week 2011-2016
    validation: Appendix Figure E.5 (AOD vs PM2.5 correspondence after program)
    limitations: Cloud-clear condition only; proxy, not PM2.5
  validation:
  - AOD-PM2.5 correspondence check (Appendix E.5)
  - Event-study balance and placebo-style robustness (weather visibility, hospital counts, etc.)
  - CFPS 126-city sample mapped to program waves (34/39/49 cities in waves 1/2/3)
  output:
    unit_of_observation: City-week (main); CFPS respondent; card (UnionPay 1% sample)
    structure: City-week panel of awareness, behavior, spending, mortality, and pollution outcomes
    geography: National cities; GfK 50 cities; DSP 131 cities; CFPS 126 cities
    time_span: Jan 2011 - Apr 2016 (mortality to Dec 2016); CFPS 2012-2018
    key_variables:
    - Baidu smog search index
    - Purchase frequency per active card
    - Air purifier sales (units, monthly)
    - Deaths by cause/age (city-week)
    - MODIS AOD
    - Program wave/rollout timing
    formats:
    - deposit formats unverified
  reproducibility:
    level: medium
    starting_point: https://doi.org/10.3886/E193441V1
    code_available: true
    code_url: https://doi.org/10.3886/E193441V1
    requirements:
    - openICPSR account and download
    - Deposit contents (manifest unverified)
    - For full reconstruction: UnionPay/GfK/DSP access (restricted/commercial)
    blockers:
    - openICPSR 403 for automated clients
    - Restricted components (UnionPay, DSP, GfK) have no public route
    - Manifest may contain only derived series
  compliance:
    terms_or_license: ICPSR deposit terms; component data licensed separately (UnionPay/GfK commercial; DSP restricted)
    robots_or_rate_limits: Respect Baidu Index terms; App Store scraping requires compliance with Apple terms
    personal_or_sensitive_data: UnionPay transactions and DSP mortality involve personal/health data; handle only under the access agreement
    redistribution: Do not redistribute restricted components or derived personal/health fields
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Barwick, Panle Jia; Li, Shanjun; Lin, Liguo; Zou, Eric Yongchen (2024), From Fog to Smog: The Value of Pollution Information, American Economic Review 114(5): 1338-1381'
  doi: https://doi.org/10.1257/aer.20200956
  journal: American Economic Review
  year: 2024
  dataset_role: Main multi-source dataset (awareness, behavior, defensive spending, mortality, pollution) for monitoring-program evaluation
  evidence_type: data-section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257%2Faer.20200956
  data_note: >-
    Paper section 2 documents the data sources: People's Daily archive, Apple App
    Store scrape (Dec 2015), Baidu search index ("smog"), CFPS 2012-2018 (83,237
    respondents, 126 cities), UnionPay card transactions (1% sample, ~18.3M active
    cards; 59% of national consumption), GfK air purifier sales (50 cities,
    2012-2016 monthly), CDC DSP mortality (131 cities, 73M persons, 5% sample,
    2011-2016), MODIS AOD city-week. AER page links the replication package to
    openICPSR 10.3886/E193441V1 (DataCite: "Data and Code for: From Fog to Smog:
    The Value of Pollution Information", ICPSR, 2024).

provenance:
- source: Working-paper full text (cached nber_fog.txt), section 2 and Table 1
  field_scope:
  - data sources, coverage (periods, cities), and construction of each series
  - UnionPay 1% card sample and outcome definition
  - DSP aggregation and coverage
  - MODIS AOD choice and validation
  - monitoring-program wave timing (field dates from news media)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: AER article page (cached aea_fog.html) Additional Materials section
  field_scope:
  - Replication Package link to https://doi.org/10.3886/E193441V1
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite record 10.3886/E193441V1
  field_scope:
  - deposit existence, title, publisher (ICPSR), year (2024)
  - does not prove file contents or automated downloadability
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite API record 10.3886/E193441V1, queried 2026-09-28
  field_scope:
  - current active, findable v1 ICPSR data-and-code deposit identity and openICPSR project route
  - title and 2024 publication year
  - does not establish a file manifest, deposit license, current download terms, or public access to UnionPay, DSP, GfK, or other component inputs
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-air-quality-monitoring
  relation: complement
- id: china-satellite-pm25
  relation: often-confused-with
- id: cfps
  relation: complement
- id: china-pollution
  relation: often-confused-with
---

## Positioning in one sentence

A city-week multi-outcome panel (2011-2016) measuring awareness, consumption, defensive spending, and mortality responses to China's 2013 real-time PM2.5 disclosure program, assembled from seven sources (UnionPay, Baidu, People's Daily, App Store, CFPS, GfK, CDC DSP, MODIS); the openICPSR replication package (10.3886/E193441V1) is the current route while most raw inputs remain restricted or commercial.

## Select rules

- Prioritize it when the question is the value of pollution information and disclosure-driven behavior (avoidance, defensive purchases, mortality), exploiting the staggered monitoring-program rollout.
- Choose china-air-quality-monitoring for station-level PM2.5 coverage questions; choose china-firm-pollution/china-environmental-enforcement for firm compliance; choose china-satellite-pm25 for modeled PM2.5 exposure surfaces.
- It cannot support post-2016 outcomes, item-level consumption detail, or reconstruction of the restricted components (UnionPay/DSP/GfK) from public inputs.

## Get recipe

1. Download the openICPSR replication package (10.3886/E193441V1) via a human browser (automated clients get 403) and inspect the manifest to see which of the seven components are included.
2. For public components missing from the deposit: Baidu Index (account), People's Daily archive, NASA MODIS AOD (public), CFPS (application route per the cfps record).
3. For restricted components (UnionPay, DSP, GfK), pursue each authority's own application/purchase process or rely on the deposit if released.
4. Align everything to the paper's city-week grid and program-wave timing (field rollout dates from news media) before analysis.

## Connections and Limitations

Ground-station PM2.5 (china-air-quality-monitoring) validates and extends the MODIS AOD exposure measure; CFPS (cfps) carries the survey components; china-satellite-pm25 is a different construction (modeled PM2.5) and should not be equated with the paper's AOD. All main series end April 2016 (mortality December 2016). The deposit manifest is the decisive open item: it may contain only derived series, leaving the raw UnionPay/DSP/GfK components unobtainable publicly.
