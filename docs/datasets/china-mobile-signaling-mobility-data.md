---
schema_version: 3
catalog_status: grounding
id: china-mobile-signaling-mobility-data
name: China mobile-phone signaling datasets for urban mobility and tourism flows (research-partnership products; three paper-specific layers, no public product)
aka:
- 手机信令数据
- mobile cellular signaling data
- mobile phone signaling data
- China Unicom tourist flow data
- 联通旅游大数据
provider: "Per-paper operator research partnerships, NOT one shared product: (1) Inner Mongolia tourism flows - China Unicom (中国联通) aggregated signaling data delivered through 'a collaborative framework with China Unicom's technical team'; (2) Qingdao activity spaces - China Mobile (中国移动) subscriber signaling per the same-team predecessor paper (JTLU 2023); provider for the Urban Studies 2026 paper itself unverified; (3) Beijing transit trajectories - an unnamed telecommunications service provider (abstract anonymizes; a same-first-author preprint uses data 'from a telecommunications service provider')."
china_related: true
domains:
- urban
- transport
- tourism
- spatial
- mobility
- environment

data_pathway:
  mode: inaccessible
  origin: mixed
  target_artifact: "Aggregated mobility/tourism flow datasets constructed from operator signaling records: (1) weekly origin-city to destination-county tourist flows for Inner Mongolia, May-October 2020 (China Unicom); (2) five-day activity data of 600,000+ Qingdao residents (Urban Studies 2026; provider unnamed, China Mobile per the team's 2023 JTLU predecessor); (3) segment-by-segment transit trajectories of 8.3 million Beijing users (Urban Studies 2026; provider unnamed). All are paper-specific operator collaborations; no public download or application route is documented in any of the papers."
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: Three 2025-2026 papers use Chinese telecom mobile signaling data for mobility research. The only fully readable data section (Land Economics 2026, Inner Mongolia) documents an operator collaboration with China Unicom that delivered only aggregated weekly tourist flows (privacy rules bar raw individual records), with no public access. The two Urban Studies papers (Qingdao, Beijing) name no provider in their abstracts; the Qingdao team's predecessor paper used China Mobile data. The family-level conclusion is routing knowledge - these are relationship/partnership data with no ordinary acquisition path, and each paper negotiated its own arrangement - this is NOT a downloadable product family, and it must not be confused with the released Baidu-Maps-derived commuting delineations (china-commuting-based-metropolitan-areas).
  barrier: Operator agreements, privacy/compliance constraints (aggregated output only), no application channel documented in any paper.

unit_of_observation: "Layer-specific: (1) Inner Mongolia - origin city (333) x destination county (103) x week x transport-mode x demographic-group tourist-flow cell (aggregated counts of China Unicom subscribers); (2) Qingdao - individual resident activity/location traces aggregated to activity spaces and third places (600,000+ residents, 5 days); (3) Beijing - user-level transit trajectory segments (8.3 million users) aggregated to route/corridor-level ridership composition"
structure: Aggregated flow panels (IM); individual-level derived activity spaces (Qingdao); trajectory-derived corridor-level cross-sections (Beijing)
geo_granularity:
- county (103 Inner Mongolia destination counties)
- city (333 Chinese origin cities; Beijing; Qingdao)
- base-station catchment (~500 m typical radius; base-station-level location inference)
geography: Inner Mongolia (all 103 counties, May-October 2020); Qingdao (2026 paper window unread; predecessor used July-September 2019); Beijing (2026 paper window unread)
time_span:
  start: '2020-05'
  end: '2020-10'
  last_confirmed_release: null
  coverage_note: "Only the Inner Mongolia layer has a confirmed window from the full text: May 1-October 31, 2020 (weekly flows). Qingdao: five days (window unspecified in abstract; the team's 2023 JTLU predecessor used July-September 2019 - different sample). Beijing: window unspecified in abstract."
  last_checked: '2026-08-14'
frequency:
- weekly (Inner Mongolia flows)
- other layers unread (abstract-level)
sample_size: "Inner Mongolia: flows from all 333 Chinese cities to all 103 Inner Mongolia counties, weekly, 6 months (China Unicom ~319M users in 2021, ~20% national market share); Qingdao: 600,000+ residents over five days; Beijing: 8.3 million users"
key_variables:
- "Origin city, destination county, week, tourist count (Inner Mongolia; also gender and age groups and transport mode: airplane, train, bus, private vehicle - per abstract and data section)"
- "Traveler residence/workplace identification from base-station patterns (Inner Mongolia: >10 km from primary residence and >=6 hours = tourist, per MOT definition; destination = registered residence/workplace excluded; scenic-area base-station verification)"
- Activity space, third places, familiar-stranger encounters (Qingdao)
- Segment-by-segment transit trajectories, destination-based and in-transit ridership diversity (Beijing)

research_fit:
  best_for:
  - Intra-city activity-space and mobility research where a research partnership with a Chinese telecom operator already exists or can be negotiated (Qingdao, Beijing layers)
  - Tourism-flow demand and travel-cost valuation at county/city level when an operator collaboration is feasible (Inner Mongolia layer; zonal travel cost method)
  - "Understanding what Chinese signaling-data papers actually contain: aggregated, operator-vetted outputs, not raw records"
  choose_over:
  - Choose china-commuting-based-metropolitan-areas (Baidu Maps location data, township-pair commuting matrix, 2017) when the need is a released, downloadable delineation of Chinese local labor markets - the only mobility-layer asset in this catalog with a public download
  - Choose china-city-to-city-truck-flows (G7 GPS telematics, openICPSR CC BY) for freight/city-pair flows
  - "Do not route researchers to any public Chinese mobile-signaling product: none is evidenced by these papers"
  not_good_for:
  - Any research design needing individual-level or raw signaling records (privacy rules; papers received aggregated data only)
  - Replication or extension without operator access (no release, no DAS in the read paper; no packages found)
  - Cross-operator or multi-city harmonized panels (each layer is a separate arrangement, different operator/period/unit)
  - Pre-2020 or post-2020 tourism flows (Inner Mongolia layer is pinned to the May-October 2020 window)
  needs_join_for:
  - Travel costs (flight data from VariFlight, road/rail routing and tolls from Amap, wage data) for travel-cost valuation - the Inner Mongolia paper compiles these separately
  - Land-use/NDVI/environmental controls (TPDC NDVI, NESDC data, MCT scenic-spot and hotel lists) used as correlates
  - Population denominators (2020 census) for per-capita scaling and operator market-share adjustment (Unicom share ~20% nationally; paper annualizes the 6-month window by 0.5353)
  variation_available:
  - "Inner Mongolia: weekly temporal variation within 2020 (May-October), origin-city and destination-county spatial variation, transport-mode and demographic splits"
  - "Qingdao/Beijing: variation across residents/routes/corridors (details unread)"
  topics:
  - mobile phone signaling data
  - human mobility
  - tourism flows
  - activity space
  - transit ridership diversity
  - travel cost method
  - China Unicom
  - China Mobile
  - operator data collaboration

good_for:
- Routing researchers away from false 'public Chinese signaling data' expectations and toward partnership reality or the released Baidu-derived alternative
identification: []
linkable_keys:
- County (103 Inner Mongolia counties; origin 333 cities) - joinable to county-level administrative codes by name/geography
- Base-station catchments (~500 m) - the spatial inference unit; no public station registry documented in the papers

joins:
- target: china-commuting-based-metropolitan-areas
  relation: often-confused-with
  keys:
  - City
  - Township
  method: Both are location/mobility-derived assets but from different provider families (telecom operator signaling vs Baidu Maps location data) and different units (aggregated operator flows vs township commuting matrix); do not treat as interchangeable
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - County
  - City
  method: Inner Mongolia paper scales flows with 2020 census population and adjusts for operator penetration; census provides denominators
  evidence_status: literature-used

access_routes:
- route: Operator research partnership (the route the papers actually used)
  access_status: by-application
  direct_url: needs-verification
  requirements:
  - Institutional relationship or formal collaboration with the operator (China Unicom technical team in the Inner Mongolia paper) and a privacy-compliant aggregation design
  - No generic application form or public channel is documented in any of the three papers
  steps:
  - Approach the operator (China Unicom for tourism flows; China Mobile for Qingdao-type data) through institutional channels; expect that only aggregated outputs will be provided under privacy constraints.
  - Design the aggregation (temporal/spatial screening, tourist definition, mode inference) jointly with the operator technical team as the Inner Mongolia paper did.
  deliverable: Aggregated flow/activity tables, not raw signaling records
  cost: by-application
  last_checked: '2026-08-14'
  caveat: No evidence of any public product; commercial operator big-data platforms (e.g. operator tourism big-data products) exist in the market but are NOT verified by these papers and were not checked this session.
- route: Published papers (documentation only)
  access_status: available
  direct_url: https://le.uwpress.org/content/wple/early/2026/02/13/le.102.3.012726-0016.full.pdf
  requirements:
  - "None for the Inner Mongolia paper (bronze OA PDF; fetched 2026-08-14); Urban Studies papers: Qingdao and Beijing closed (Beijing bronze OA at SAGE, blocked for automated clients this session)"
  steps:
  - Read the Inner Mongolia data section (Section 2) for the full China Unicom collaboration protocol, tourist definition, and mode inference.
  - "For Qingdao: read the same-team JTLU 2023 paper (open access, doi 10.5198/jtlu.2023.2159) for China Mobile data details (42,991 sampled subscribers, July-September 2019)."
  deliverable: Methodological documentation; no data
  cost: free
  last_checked: '2026-08-14'
  caveat: The Qingdao 2026 and Beijing 2026 data sections remain unread (closed/blocked); the JTLU predecessor documents a DIFFERENT sample than the 2026 paper (42,991 subs x 3 months vs 600,000+ residents x 5 days).

production:
  raw_sources:
  - name: China Unicom mobile signaling records (Inner Mongolia layer)
    source_type: dataset
    role: Raw input - base-station connection records (signal strength, location, timestamps; ~500 m typical base-station radius); aggregated by the operator into weekly origin-destination flows under a research collaboration
    access_route: Operator collaboration ('collaborative framework with China Unicom's technical team'); no public route
    url: https://doi.org/10.3368/le.102.3.012726-0016
    coverage: China Unicom subscribers whose devices appeared in Inner Mongolia 2020-05-01..2020-10-31; ~319M Unicom users in 2021 (~20% national share); all 333 origin cities, all 103 destination counties
    last_checked: '2026-08-14'
  - name: China Mobile cellular signaling data (Qingdao layer - predecessor paper)
    source_type: dataset
    role: Raw input for the same team's 2023 JTLU study (42,991 randomly sampled subscribers from 1,240 TAZs; July-September 2019; MSIN, cell-tower coordinates, arrival/leaving timestamps, ~1-minute recording; activity = stay >10 minutes)
    access_route: Not documented in JTLU 2023 (institute-level access; Qingdao Urban Planning and Design Research Institute co-authors)
    url: https://doi.org/10.5198/jtlu.2023.2159
    coverage: Qingdao, July-September 2019; China Mobile ~65% market share in Qingdao
    last_checked: '2026-08-14'
  acquisition_methods:
  - provided-by-operator (aggregated, under collaboration agreement)
  sample_construction: "Inner Mongolia: multi-stage filtering - (1) devices in Inner Mongolia in the study window; (2) tourism defined as travel >10 km from primary residence for >=6 hours (Ministry of Culture and Tourism definition); (3) exclude trips where destination = registered residence/workplace; (4) scenic-area verification via Unicom scenic-area base-station interface data; multi-destination trips recorded as separate origin-destination flows; transport mode from spatial intersection of connecting base stations with airport/railway/bus-station base stations (else private vehicle). Qingdao (JTLU predecessor): random sample of China Mobile subscribers from residential TAZs; home/work from frequency-duration clustering (home 12am-8am; work 9am-6pm weekdays); activity spaces as 95% standard deviational ellipses."
  pipeline_stages:
  - stage: collect
    inputs:
    - Operator signaling records
    method: Operator-side aggregation under collaboration (Inner Mongolia); institute-side sample extraction (Qingdao predecessor)
    tools: []
    parameters:
    - study window 2020-05-01 to 2020-10-31 (IM)
    output: Aggregated weekly origin-destination tourist flow tables (IM)
    evidence: Land Economics 2026 data section (read in full 2026-08-14)
  - stage: clean
    inputs:
    - Aggregated flows
    method: Annualization of the 6-month window by 0.5353 (share of annual tourists in the window); adjustment for Unicom market penetration by region
    tools: []
    parameters:
    - annualization factor 0.5353
    output: Annualized flow estimates
    evidence: Land Economics 2026 data section
  - stage: model
    inputs:
    - Annualized flows; travel costs (VariFlight airfares, Amap road/rail time and tolls, provincial wages)
    method: Zonal travel cost method with parametric and non-parametric (KNN) estimators; regression on grassland NDVI, scenic/hotel counts, GDP, population
    tools: []
    parameters: []
    output: Grassland tourism value estimates
    evidence: Land Economics 2026
  constructed_variables:
  - name: Weekly tourist flow (origin city i -> destination county j)
    concept: Number of China Unicom subscribers traveling from city i to county j in a week, meeting the tourist definition, by transport mode, gender, and age group
    source_fields:
    - Aggregated operator signaling tables
    method: Operator-side aggregation + multi-stage filtering (see sample_construction)
    validation: Scenic-area base-station verification step
    limitations: China Unicom subscribers only (adjusted by market share); COVID-19 year 2020; no individual-level verification possible
  validation:
  - Scenic-area base-station interface verification (IM)
  - Comparison with official tourism statistics is NOT documented in the paper's data section (robustness uses annual vs time-period aggregation)
  output:
    unit_of_observation: Origin-city x destination-county x week x mode x demographic flow cells (IM); resident activity traces (Qingdao); route/corridor ridership composition (Beijing)
    structure: Aggregated flow panels; activity-space cross-sections; corridor-level diversity measures
    geography: Inner Mongolia (103 counties); Qingdao; Beijing
    time_span: 2020-05-01 to 2020-10-31 (IM, weekly); others unread
    key_variables:
    - Tourist counts by origin/destination/week/mode/gender/age (IM)
    formats:
    - Unreleased (no packages found for any of the three papers on 2026-08-14)
  reproducibility:
    level: not-reproducible
    starting_point: Operator collaboration required; no public raw source
    code_available: false
    code_url: null
    requirements:
    - Operator agreement and privacy-compliant aggregation design
    blockers:
    - Raw signaling records not accessible per privacy rules (stated in the Inner Mongolia paper)
    - No releases or replication packages found (DataCite/OpenAlex/Semantic Scholar negative 2026-08-14)
  compliance:
    terms_or_license: Operator agreements not visible; privacy regulations cited as the reason for aggregated-only delivery (IM paper)
    robots_or_rate_limits: N/A
    personal_or_sensitive_data: Personal location data; papers state raw individual-level data cannot be accessed; only aggregates leave the operator
    redistribution: Not permitted (no data released)
    review_needed: Any new operator collaboration needs institutional ethics and data-governance review

quality:
  profile_status: partial
  access_status: unavailable
  paper_use_status: partial
  last_audited: '2026-08-14'

used_by:
- cite: 'Liu, Na, Xinxin Lv, Pengfei Liu and Lingling Hou (2026), Estimating the Economic Value of Grassland Tourism Services Based on Mobile Phone Data'
  doi: https://doi.org/10.3368/le.102.3.012726-0016
  journal: Land Economics
  year: 2026
  dataset_role: Main data - China Unicom aggregated mobile signaling data; weekly tourist flows from all 333 Chinese cities to all 103 Inner Mongolia counties, May 1-October 31 2020, with transport mode, gender and age groups; basis for zonal travel-cost valuation of grassland tourism
  evidence_type: data-section
  evidence_url: https://le.uwpress.org/content/wple/early/2026/02/13/le.102.3.012726-0016.full.pdf
  data_note: "Full text read 2026-08-14 (bronze OA PDF fetched directly from le.uwpress.org). Data section (Section 2) documents: China Unicom as provider via 'a collaborative framework with China Unicom's technical team'; aggregated-only delivery because confidentiality/privacy regulations bar raw individual data; tourist definition (>10 km from primary residence, >=6 hours, per MOT definition; residence/workplace trips excluded; scenic-area base-station verification); transport mode assignment by base-station intersection with airport/railway/bus stations else private vehicle; annualization by 0.5353 and Unicom market-share adjustment; travel costs from VariFlight, Amap, and wage data. No data-availability statement; acknowledgements only NSFC grants."
- cite: 'Lin, Lin, Tianyi Chen, Zhen Liu and Zhulin Shao (2026), Daily routines, activity space, and third places: A big data approach to understand encounters'
  doi: https://doi.org/10.1177/00420980261452161
  journal: Urban Studies
  year: 2026
  dataset_role: Main data - mobile cellular signaling data of 600,000+ Qingdao residents over five days, used to analyze activity spaces, third places and encounters (non-commute behaviors)
  evidence_type: abstract-only
  evidence_url: https://journals.sagepub.com/doi/10.1177/00420980261452161
  data_note: "Abstract-level only (closed access; SAGE and mirror pages served abstract+references on 2026-08-14; no OA copy in OpenAlex/Semantic Scholar). Provider and exact window NOT named in the abstract. Same-team predecessor: Lin & Chen (2023) JTLU 15(1), doi 10.5198/jtlu.2023.2159 (open access, read in full) used China Mobile signaling data (42,991 randomly sampled subscribers, July-September 2019, ~65% Qingdao market share) - a DIFFERENT sample from the 2026 paper (600,000+ residents, five days); whether the 2026 paper uses the same China Mobile channel is unverified."
- cite: 'Yang, Yitao, Erjian Liu, Shifen Cheng, Hui Wang and Junxi Chen (2026), Public transport and the paradox of socioeconomic segregation and diversity'
  doi: https://doi.org/10.1177/00420980261460340
  journal: Urban Studies
  year: 2026
  dataset_role: Main data - mobile phone data of 8.3 million users in Beijing used to reconstruct segment-by-segment transit trajectories and corridor-level socioeconomic diversity metrics
  evidence_type: abstract-only
  evidence_url: https://journals.sagepub.com/doi/10.1177/00420980261460340
  data_note: "Abstract-level only (bronze OA at SAGE; PDF fetch blocked for automated clients on 2026-08-14 - connection reset; mirror abstract-only; Wayback down). Provider unnamed in abstract. Related context: same-first-author preprint (Manley, Yang, Liu & Jia, Research Square rs-6716648/v1, 2025, read 2026-08-14) uses a DIFFERENT Beijing dataset - 'mobile phone data from 11 million users' from 'a telecommunications service provider' (anonymized) with property data from Lianjia and a GitHub data-availability statement - not evidence for the 8.3M-user sample of this paper."

provenance:
- source: Land Economics 2026 full text (PDF fetched from le.uwpress.org and read in full 2026-08-14)
  field_scope:
  - provider identity (China Unicom)
  - aggregation/collaboration mode
  - window, geography, flows, transport modes, demographics
  - annualization and penetration adjustments
  - absence of DAS/release
  added: '2026-08-14'
  confidence: high
  verified: true
- source: JTLU 2023 predecessor full text (open access, fetched and read 2026-08-14)
  field_scope:
  - China Mobile provider identity, sample, window for the Qingdao team's earlier data product
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Crossref/OpenAlex/Semantic Scholar + CNPeReading mirror abstracts for the two Urban Studies papers; Research Square preprint rs-6716648/v1 (full text read 2026-08-14)
  field_scope:
  - paper identity and OA status
  - abstract-level data description
  - related-preprint context (11M-user Beijing dataset, different study)
  added: '2026-08-14'
  confidence: med
  verified: false
- source: Negative checks (no replication packages for any of the three DOIs in DataCite/OpenAlex/Semantic Scholar, 2026-08-14)
  field_scope:
  - absence of released data
  added: '2026-08-14'
  confidence: med
  verified: false

related_datasets:
- id: china-commuting-based-metropolitan-areas
  relation: often-confused-with
- id: china-city-to-city-truck-flows
  relation: complement
---

## Positioning in one sentence

Three 2025-2026 papers use Chinese telecom mobile signaling data - Inner Mongolia tourism flows (China Unicom, aggregated, weekly, May-October 2020), Qingdao activity spaces (600,000+ residents, five days), and Beijing transit trajectories (8.3 million users) - but each is a separate operator research partnership with no public product: the one fully readable data section (Land Economics) states raw records are barred by privacy rules and only aggregates were delivered. The record's value is routing knowledge: do not expect to download Chinese mobile-signaling data; the only released mobility-layer asset in this catalog is the Baidu-derived commuting-MA delineation (china-commuting-based-metropolitan-areas).

## Select rules

- For released, downloadable Chinese mobility assets, use china-commuting-based-metropolitan-areas (Baidu Maps location data, 2017 township commuting matrix, Mendeley CC BY) or china-city-to-city-truck-flows (G7 GPS, openICPSR CC BY).
- For research designs that genuinely need operator signaling (activity spaces, tourist flows, ridership composition), expect to negotiate an operator collaboration per city - the Inner Mongolia paper is the model protocol (aggregated-only, tourist definition, mode inference, penetration adjustment).
- Do not use these papers as evidence that any Chinese signaling product is publicly obtainable; do not merge the three layers into one dataset identity.

## Get recipe

1. Read the Inner Mongolia paper's Section 2 (free bronze-OA PDF at le.uwpress.org, or via its DOI) for the full China Unicom collaboration protocol.
2. Read the same-team JTLU 2023 paper (open access, doi 10.5198/jtlu.2023.2159) for China Mobile Qingdao details - noting its sample differs from the 2026 Qingdao paper.
3. There is nothing to download: no releases, no replication packages for any of the three DOIs (checked 2026-08-14).
4. If an operator partnership is feasible for your institution, replicate the Inner Mongolia design: temporal/spatial screening, tourist definition (>10 km, >=6 hours), mode inference from hub base stations, annualization and market-share adjustment.

## Connections and Limitations

- The three layers are NOT one product: different operators (China Unicom confirmed for Inner Mongolia; China Mobile only for the Qingdao team's predecessor; unnamed for Beijing), different units (flow cells vs resident activity vs trajectory segments), and different windows.
- Boundary vs china-commuting-based-metropolitan-areas: provider family (telecom operator signaling vs Baidu Maps location services), unit (operator flow aggregates vs township-pair commuting matrix), and release status (none vs Mendeley CC BY download) all differ.
- Inner Mongolia layer limits: China Unicom subscribers only (~20% national share, adjusted), COVID-affected 2020, six-month window annualized by 0.5353, aggregate-level only, no official-statistics validation documented.
- Qingdao and Beijing layers: data sections unread (closed/blocked on 2026-08-14); provider identities for those papers remain unverified; the JTLU and Research Square documents describe different samples and must not be conflated.
