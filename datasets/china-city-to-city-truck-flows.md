---
schema_version: 3
catalog_status: ready
id: china-city-to-city-truck-flows
name: China city-to-city truck flow panel from real-time truck GPS (G7 telematics; Chen, Chen, Liu, Luo & Song 2025 JUE; replication package openICPSR 210761 V1)
aka:
- 城际卡车流量数据
- G7 卡车 GPS 流量数据
- The Economic Cost of Locking down like China replication data
- 10.3886/E210761V1
provider: G7 (private logistics/trucking service provider, real-time truck GPS data; named in Chen, He, Hsieh & Song 2020 CCE report, the same data family the JUE paper cites); compiled city-pair flow panel constructed by the paper's authors; ICPSR [distributor of the replication package]
china_related: true
domains:
- transport
- logistics
- urban
- regional
- trade-networks
- covid19
- digital-economy

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: "openICPSR project 210761 version V1 (DOI 10.3886/E210761V1): 'Replication package for The Economic Cost of Locking down like China: Evidence from City-to-City Truck Flows' - data-and-codes/data_raw/ with china_city_db.dta, full_pair_weekly.dta, data_esti_expenditure.mat plus Stata code (Step1_data_clean.do and related); the compiled city-pair truck-flow panel and lockdown-measure files"
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The paper's compiled city-to-city truck-flow panel (GPS-derived, city-pair weekly/monthly flow counts) plus the lockdown measures and estimation code are released on openICPSR under CC BY 4.0; the underlying raw asset - G7's real-time truck GPS records (about 1.8-2 million long-haul trucks) - is commercial telematics data, not publicly downloadable. The JUE paper's own working paper anonymizes the provider ('one of China's leading logistics service providers'), but the same team's CCE report (Chen, He, Hsieh & Song 2020, cited by the WP for aggregate statistics of the same data) names G7 explicitly.
  barrier: openICPSR serves a Cloudflare challenge to automated clients in this environment (recorded 2026-08-14), so the package download and README contents need a human browser or JS-capable client plus a free ICPSR/MyData account; G7 raw GPS microdata is not offered publicly (commercial product, terms unverified here).

unit_of_observation: City-pair (origin loading city -> destination discharge city) truck flow count per period (monthly per the working paper; the replication package contains a full_pair_weekly file, so the published version may use weekly pairs - unverified)
structure: Panel of directed (symmetric by construction) city-pair flows over time; round-trip trucks counted from loading-city to discharge-city
geo_granularity:
- city
- prefecture-level city
geography: "China, 336 of 342 prefecture-level cities covered by the GPS records (WP); analysis sample 315 cities, excluding Tibet and Xinjiang; the provider does not monitor within-city flows"
time_span:
  start: '2019-01'
  end: '2022-01'
  last_confirmed_release: '2024-11-11'
  coverage_note: "Working-paper data section (truck_flow_and_covid19_final.pdf, read in full 2026-08-14): flows Jan 2019 - Jan 2022, 315 cities, monthly; the openICPSR DDI record gives distribution date 2024-11-11 (biblCit) with V1 datestamp 2026-08-14/15. The published JUE version's exact sample window and frequency were not readable (ScienceDirect 403); the replication file name full_pair_weekly.dta suggests weekly pair data in the released package."
  last_checked: '2026-08-14'
frequency:
- monthly (per the author working paper)
- weekly (per replication file name full_pair_weekly.dta; unverified against contents)
sample_size: 1.8 million long-haul trucks (2020, about 20% of China's long-haul fleet) tracked in real time (WP); about 2 million trucks (about 10% of all trucks) per the CCE report (2020-03); flows regularly updated on 60% of the 315x314/2 = 49,455 city pairs (WP)
key_variables:
- City-to-city truck flow (number of round-trip trucks from loading city to discharge city; symmetric by construction; no freight tonnage/weight information)
- City-level lockdown dummies (full-scale / partial / minimum lockdown per city-pair and per city, compiled from government announcements; timing/duration)
- City-pair and city controls used in the paper (COVID case counts, GDP, night lights correlations)
- Estimation output files (data_esti_expenditure.mat) and Stata cleaning code (Step1_data_clean.do)

research_fit:
  best_for:
  - City-pair trade-network and intercity-transport-flow research for China (2020-2022 window), including COVID lockdown cost estimation and gravity-model trade analysis
  - Replicating or extending Chen, Chen, Liu, Luo & Song (2025 JUE) lockdown-cost estimates with the authors' released panel and code
  - Correlating truck flows with economic activity (the WP documents 0.9 correlation with 2019 city GDP, 0.86 with night lights)
  choose_over:
  - Choose this panel over official freight statistics when monthly/weekly city-pair granularity and network structure are required (official data are aggregate, lower-frequency, and not city-pair)
  - Choose the released openICPSR package over attempting to buy G7 raw data when the paper's compiled panel suffices
  not_good_for:
  - Within-city transport or traffic flows (the provider does not monitor within-city truck flows)
  - Freight tonnage or value (the data contain no freight information)
  - Periods before 2019 or after January 2022 (per the working-paper sample; the G7 data family itself extends beyond, e.g. Alder, Song & Zhu 2023 use 2018 data, but the released package covers the paper's sample)
  - All-city coverage: Tibet and Xinjiang are excluded from the analysis sample and pair coverage is about 60%
  needs_join_for:
  - City-level economic outcomes (GDP, employment) from official statistics or other panels for outcome analysis beyond flows
  - COVID case data and lockdown announcement details for treatment measurement
  - Night-lights or other activity proxies for validation
  variation_available:
  - Temporal variation in lockdown treatment (16 full-scale lockdowns in 16 cities, 18 partial, ~111 community-level per the WP) with event-study and TWFE designs; treatment assignment details belong to the Econ-Variation repository
  topics:
  - truck flows
  - transport networks
  - COVID-19 lockdown
  - city-pair trade
  - gravity model
  - China cities

good_for:
- City-pair transport-flow panel analysis for China 2019-2022
- Lockdown/policy cost estimation with a network structure
identification:
- This is a paper-specific compiled city-pair flow and code package, not a stand-alone causal-variation record. It supports reproducing the documented transport-flow analysis and inspecting released fields; any new identification claim requires separate design assessment.
linkable_keys:
- City (prefecture-level city; 315-city sample; exact city identifiers and codes per the released files)
- City pair (symmetric by construction)

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - City
  method: City-level GDP and controls are used in the paper for validation and structural estimation; join on city identifiers normalized to the paper's 315-city sample
  evidence_status: plausible
- target: china-nighttime-lights
  relation: complement
  keys:
  - City (aggregate)
  method: The WP validates truck outflows against night-light intensity (correlation 0.86); use for cross-validation of flow activity measures
  evidence_status: literature-used

access_routes:
- route: openICPSR replication package 210761 V1 (DOI 10.3886/E210761V1)
  access_status: available-with-registration
  direct_url: https://www.openicpsr.org/openicpsr/project/210761/version/V1/view
  requirements:
  - Free ICPSR/MyData account and acceptance of the current download terms
  - Human browser or JS-capable client: openICPSR serves a Cloudflare challenge to automated clients (403 'Just a moment...' in this environment, 2026-08-14)
  steps:
  - Open the DOI https://doi.org/10.3886/E210761V1 (resolves to the openICPSR project page).
  - Read the README and the data-and-codes/data_raw folder listing (files evidenced so far: china_city_db.dta, full_pair_weekly.dta, data_esti_expenditure.mat, Step1_data_clean.do).
  - Download the needed data and code files; record the version (V1) and citation (Chen, Chen, Liu & Song, 10.3886/E210761V1).
  deliverable: data-and-codes/data_raw/ files (city database, full pair weekly panel, expenditure .mat) plus Stata code; license CC BY 4.0 per the ICPSR DDI record
  cost: free
  last_checked: '2026-09-28'
  caveat: Current DataCite metadata verifies the active, findable V1 DOI and now resolves to an ICPSR study page; it does not expose a license, file manifest, current download terms, README contents, or exact row counts. The documented CC BY 4.0 claim remains sourced to the earlier ICPSR OAI/DDI metadata. Note the package credits four authors (Chen, Chen, Liu, Song) while the JUE article lists five (adding Jie Luo).
- route: Author working paper (open full text) - final preprint
  access_status: available
  direct_url: https://www.michael-song.org/uploads/4/8/1/4/48141215/truck_flow_and_covid19_final.pdf
  requirements:
  - Public web access
  steps:
  - Download the PDF (57 pp, fetched and read in full 2026-08-14); data section 2.3 'Truck Flows' describes construction and coverage; footnote 14 points to Alder, Song & Zhu (2023) for the GPS-data description; footnote 4 cites Chen, He, Hsieh & Song (2021a, CCE report) for aggregate statistics of the same data.
  - Earlier WP copies: CUHK-Tsinghua Joint Research Center research paper 0040 (2022, abstract page) and the retired michaelzsong.weebly.com URL (404 as of 2026-08-14).
  deliverable: Full working-paper text with the data section
  cost: free
  last_checked: '2026-08-14'
  caveat: The WP anonymizes the provider ('one of China's leading logistics service providers'); the published JUE version (ScienceDirect 403 here) may differ in sample window and frequency.
- route: CCE report naming the provider (Chen, He, Hsieh & Song, 'Economic Effects of Lockdown in China', April 2020)
  access_status: available
  direct_url: https://www.michael-song.org/uploads/4/8/1/4/48141215/cce_report_covid-19_thematic_report_no.2.pdf
  requirements:
  - Public web access
  steps:
  - Download and read the report (fetched and read 2026-08-14): it names the company as G7 ('this company, G7, has real-time GPS data from two million trucks, accounting for about 10 percent of all trucks operating in China').
  deliverable: Report text naming the data provider and describing the daily provincial-capital truck-flow aggregation
  cost: free
  last_checked: '2026-08-14'
  caveat: This is the same team's descriptive COVID report, not the JUE paper itself; it establishes provider identity for the data family, not the paper's own wording.

access:
  url: https://doi.org/10.3886/E210761V1
  cost: free
  license: CC BY 4.0 (per ICPSR DDI metadata record for 210761 V1)
  format:
  - dta
  - mat
  - do
  api: false
  how_to_get: Free ICPSR/MyData account; download data-and-codes from openICPSR project 210761 V1 in a human browser (Cloudflare challenge blocks automated clients)
caveats: Provider identity rests on the team's CCE report (named G7) plus the JUE working-paper description of the same data family; the JUE paper itself anonymizes the provider. The G7 raw GPS microdata (trucks, routes, timestamps) is a commercial product and is not publicly downloadable; only the authors' compiled panel is released.

production:
  raw_sources:
    - name: G7 real-time truck GPS records (telematics)
      source_type: dataset
      role: Raw flow measurement - loading/discharge city pairs derived from real-time GPS of about 1.8-2 million trucks
      access_route: Commercial (G7, Beijing-based logistics service provider); terms unverified in this environment
      url: https://www.g7.com.cn (not fetched this session; provider name grounded via the CCE report)
      coverage: 'About 1.8 million long-haul trucks in 2020 (WP), 20% of China''s long-haul fleet; about 2 million trucks / 10% of all trucks (CCE report, 2020-03); 336 of 342 prefecture-level cities'
      last_checked: '2026-08-14'
    - name: City-level lockdown announcement compilation (paper-constructed)
      source_type: document
      role: Treatment measurement - full-scale/partial/minimum lockdown timing and duration compiled from official local-government announcements and Baidu keyword searches (per WP section 2.2 and ABFER slides)
      access_route: Public announcements; compilation is the authors' manual work
      url: ''
      coverage: 16 full-scale lockdowns in 16 cities, 18 partial lockdowns in 18 cities, ~111 community-level lockdowns, April 2020 - January 2022 (WP)
      last_checked: '2026-08-14'
  acquisition_methods:
  - download (openICPSR replication package)
  - vendor data agreement (raw G7 GPS; unverified)
  sample_construction: "The authors aggregate real-time GPS records into city-pair monthly flows: number of round-trip trucks departing from the loading city and arriving at the discharge city; flows are symmetric by construction; route-specific trends are filtered and log changes are measured relative to the same period in 2019 (WP section 2.3)"
  pipeline_stages:
    - stage: collect
      inputs:
      - G7 real-time truck GPS records
      method: Logistics provider tracks trucks; authors receive aggregated city-to-city flows (provider does not monitor within-city flows)
      tools: []
      parameters: {}
      output: City-pair monthly truck flows (WP) / weekly panel (package file name)
      evidence: 'WP section 2.3; Alder, Song & Zhu (2023) for a detailed description of the real-time GPS data (WP footnote 14)'
    - stage: collect
      inputs:
      - Local government lockdown announcements
      - Baidu search results (year/month/city + COVID keywords)
      method: Manual collection of official announcements; classification into full-scale (citywide), partial (district) and minimum (community) lockdowns
      tools: []
      parameters: {}
      output: City-pair and city lockdown dummies with durations
      evidence: WP section 2.2; ABFER webinar slides (August 2022)
  constructed_variables:
    - name: d ln q_ni,t (log change in truck flows)
      concept: Detrended log truck flow difference between current period and the same period in 2019, weighted by 2019 pair flows
      source_fields:
      - city-pair truck flow
      method: Filter route-specific trend; take difference vs same period 2019 (WP section 2.3)
      validation: Correlations with COVID cases (-0.69 aggregate), 2019 city GDP (0.9) and night lights (0.86)
      limitations: No freight tonnage; 60% of pairs regularly updated; pairs with data are closer and richer (35% less distance, 55% more GDP)
    - name: Lockdown dummies (D_k_ni,t)
      concept: City-pair dummies for full-scale (k=h), partial (k=l) and minimum (k=m) lockdown in period t for at least one city in the pair
      source_fields:
      - lockdown announcements
      method: Manual compilation and classification
      validation: Event-study parallel trends
      limitations: Wording of announcements varies; classification is author judgment
  validation:
  - Correlation of city truck outflows with GDP (0.9) and night lights (0.86) in 2019 (WP, Figure A8)
  - Cross-checks against official statistics (73% of China's freight by highway, 2019)
  output:
    unit_of_observation: City pair x period
    structure: Panel of symmetric directed city-pair flows (N = 315 cities, 49,455 potential pairs, about 60% with regular updates)
    geography: 315 Chinese prefecture-level cities (excluding Tibet and Xinjiang) in the analysis sample
    time_span: 2019-01 to 2022-01 (WP); published/released versions may differ (weekly file name)
    key_variables:
    - truck flow
    - lockdown dummies
    - analysis/estimation files
    formats:
    - dta
    - mat
    - do
  reproducibility:
    level: medium
    starting_point: openICPSR 210761 V1 (compiled panel + code); WP PDF for method details
    code_available: true
    code_url: https://www.openicpsr.org/openicpsr/project/210761/version/V1/view
    requirements:
    - Free ICPSR account and human-browser download (Cloudflare challenge in this environment)
    - Stata (Step1_data_clean.do) and MATLAB/other tools for the .mat estimation files (unverified which package)
    blockers:
    - README contents and file-level manifest not read (Cloudflare); raw G7 GPS is not included - only the compiled flows
  compliance:
    terms_or_license: CC BY 4.0 (per ICPSR DDI metadata for 210761 V1)
    robots_or_rate_limits: openICPSR Cloudflare challenge blocks automated clients
    personal_or_sensitive_data: Aggregated city-pair flows; no truck- or driver-level identifiers in the released compiled panel (per file naming; README unverified)
    redistribution: CC BY 4.0 permits redistribution with attribution
    review_needed: false

quality:
  profile_status: grounded
  access_status: needs-verification
  paper_use_status: grounded
  last_audited: '2026-08-14'

used_by:
  - cite: "Chen, Jingjing; Chen, Wei; Liu, Ernest; Luo, Jie; Song, Zheng (2025). 'The economic cost of locking down like China: Evidence from city-to-city truck flows.' Journal of Urban Economics 145:103729."
    doi: 10.1016/j.jue.2024.103729
    journal: Journal of Urban Economics
    year: 2025
    dataset_role: Main data - high-frequency city-to-city truck flow panel used as the outcome and as the empirical counterpart of the gravity model of city-to-city trade
    evidence_type: data-section
    evidence_url: https://www.michael-song.org/uploads/4/8/1/4/48141215/truck_flow_and_covid19_final.pdf
    data_note: "Author working paper (57 pp, read in full 2026-08-14): data from real-time truck GPS of 1.8 million (20% of China's) long-haul trucks in 2020, flows in 336 of 342 prefecture-level cities, analysis sample 315 cities January 2019 - January 2022, symmetric city-pair round trips, no freight information; provider anonymized in the WP; replication package openICPSR 210761 V1 (DOI 10.3886/E210761V1) confirms release. Published JUE version (ScienceDirect 403) not read."
  - cite: "Alder, Simon; Song, Zheng; Zhu, Zhitao (2023). 'On (Un)Congested Roads: A Quantitative Analysis of Infrastructure Investment Efficiency using Truck GPS Data in China.' (working paper)"
    doi: ''
    journal: working paper
    year: 2023
    dataset_role: Same data family - real-time truck GPS from one of China's leading logistics service providers, 562,980 trucks in 2018 (7.9% of all trucks); cited by the JUE working paper (footnote 14) for the detailed GPS-data description
    evidence_type: data-section
    evidence_url: https://www.michael-song.org/uploads/4/8/1/4/48141215/road_230428.pdf
    data_note: 'Fetched and read 2026-08-14; provider anonymized as "one of China''s leading logistics services providers" in this paper too; establishes the data family''s use across years (2018 data)'
  - cite: Chen, Qi; He, Zhiguo; Hsieh, Chang-Tai; Song, Zheng (2020/2021). 'Economic Effects of Lockdown in China.' CCE COVID-19 Thematic Report No. 2 (April 2020).
    doi: ''
    journal: CCE report
    year: 2020
    dataset_role: Same data family - the report names the provider G7 ('this company, G7, has real-time GPS data from two million trucks, accounting for about 10 percent of all trucks operating in China')
    evidence_type: data-section
    evidence_url: https://www.michael-song.org/uploads/4/8/1/4/48141215/cce_report_covid-19_thematic_report_no.2.pdf
    data_note: Fetched and read 2026-08-14; the JUE working paper (footnote 4) cites this report's aggregate statistics of the same data; this is the direct evidence that the data family is G7's

provenance:
  - source: Author working paper truck_flow_and_covid19_final.pdf (michael-song.org), section 2.3 and footnotes 4/14-17
    field_scope:
    - data_pathway.target_artifact
    - unit_of_observation
    - time_span
    - sample_size
    - key_variables
    - production
    added: '2026-08-14'
    confidence: high
    verified: true
  - source: CCE report No. 2 (Chen, He, Hsieh & Song, michael-song.org) naming G7
    field_scope:
    - provider
    - production.raw_sources
    added: '2026-08-14'
    confidence: high
    verified: true
  - source: ICPSR OAI/DDI records for openICPSR 210761 V1 and DataCite 10.3886/E210761V1
    field_scope:
    - access_routes
    - access.license
    - target_artifact
    added: '2026-08-14'
    confidence: high
    verified: true
  - source: IDEAS article page for 10.1016/j.jue.2024.103729; Crossref; OpenAlex; Unpaywall
    field_scope:
    - used_by
    - bibliography
    added: '2026-08-14'
    confidence: high
    verified: true
  - source: CUHK-Tsinghua Joint Research Center research-paper page (paper 0040, 2022) and ABFER webinar slides (August 2022)
    field_scope:
    - access_routes (WP history)
    - production.sample_construction
    added: '2026-08-14'
    confidence: med
    verified: true
  - source: DataCite API record 10.3886/E210761V1, queried 2026-09-28
    field_scope:
    - current active, findable V1 ICPSR replication-package identity and current ICPSR study route
    - title, 2026 publication year, and abstract describing high-frequency China city-to-city truck-flow data
    - does not establish a license, file manifest, current download terms, README contents, or public access to raw G7 GPS data
    added: '2026-09-28'
    confidence: high
    verified: true

related_datasets:
  - id: china-county-population-agriculture-gis-1990
    relation: complement
  - id: china-nighttime-lights
    relation: complement
---

## Positioning in one sentence

The released research asset is the authors' compiled China city-pair truck-flow panel (openICPSR 210761 V1, CC BY 4.0) derived from real-time truck GPS of the commercial telematics provider G7 - usable for city-pair trade-network and lockdown-cost research 2019-2022 - while the raw G7 GPS microdata behind it is a commercial product with no public download.

## Select rules

- Prioritize this panel when the research needs monthly/weekly city-pair truck flows with a network structure (gravity/trade-spillover designs) rather than aggregate freight statistics.
- Use the openICPSR package for replication and extension of the JUE paper; do not assume the raw G7 GPS records (trucks, routes, timestamps) are obtainable - they are not part of the package and no public G7 data route was verified.
- Not suitable for within-city traffic, freight tonnage/value, or periods outside the released sample (working paper: Jan 2019 - Jan 2022; Tibet/Xinjiang excluded).
- The treatment-side lockdown timing/classification is the paper's own compilation (Econ-Variation territory); this record covers the flow data and the released panel.

## Get recipe

1. Open the openICPSR project page (DOI 10.3886/E210761V1) in a human browser; create a free ICPSR/MyData account if needed (openICPSR blocks automated clients with a Cloudflare challenge - verified 2026-08-14).
2. Read the README and the data-and-codes/data_raw folder listing; download china_city_db.dta, full_pair_weekly.dta, data_esti_expenditure.mat and the Stata code (Step1_data_clean.do and related).
3. For method details, download the author working paper from Zheng Song's site (truck_flow_and_covid19_final.pdf) and read section 2.3 (Truck Flows) plus footnotes 4, 14-17.
4. For provider identity, read the CCE report No. 2 (Chen, He, Hsieh & Song 2020) on the same site, which names G7.
5. If the compiled panel does not meet the research need, treat the raw G7 GPS data as a separate commercial acquisition (terms unverified) - do not assume public availability.

## Connections and Limitations

- City-pair flows are symmetric by construction (round trips from loading to discharge city); no within-city flows, no freight tonnage.
- Only about 60% of the 49,455 city pairs are regularly updated; pairs with data are closer and richer than those without (WP footnote 17) - sample-selection awareness is required when building networks.
- The JUE working paper's sample is 315 cities (excludes Tibet and Xinjiang), January 2019 - January 2022; the published JUE version (ScienceDirect 403 in this environment) and the released package may use a weekly panel - the file name full_pair_weekly.dta points that way, but contents were not readable.
- Provider identity: the JUE paper itself anonymizes the provider; the identification of G7 comes from the same team's CCE report, which the WP cites for aggregate statistics of the same data. Treat 'G7' as the documented provider of the data family, with the paper's own anonymized wording as the primary description.
- The replication package credits four authors (Chen, Chen, Liu, Song) while the JUE article lists five (adding Jie Luo) - a metadata-level discrepancy to note when citing.

## Decision sufficiency check

Using only this record, a future agent can: identify the asset (G7-GPS-derived city-pair truck flow panel), name the released deliverable (openICPSR 210761 V1, CC BY 4.0, with data_raw files and code), give the acquisition start (DOI -> openICPSR project page with a free account in a human browser), state coverage (315-city analysis sample, Jan 2019 - Jan 2022 in the WP, 336/342 cities in the raw records), state limitations (no within-city flows, no tonnage, ~60% pair coverage, Tibet/Xinjiang excluded, raw G7 data commercial), and name the key unknown (published-version data section and package README contents unread; weekly-vs-monthly frequency in the released files).
