---
schema_version: 3
catalog_status: grounding
id: china-truck-driver-telematics
name: Guangdong heavy-duty truck driver telematics and labor panel 2023-2025 (Ding, Wang, Wang & Wang 2026 JEEM "Too hot to haul?")
aka:
- 货车司机遥测数据
- truck driver GPS labor data
- Too hot to haul dataset
- JEEM 103338 truck data
provider: >-
  UNNAMED in the paper. Proprietary fleet telematics/vehicle-monitoring data
  covering approximately 10,000 heavy-duty trucks and 130 freight companies in
  Guangdong province, made available to the authors "under a data usage
  agreement" (DAS). The telematics provider and the freight companies are not
  identified anywhere in the readable text. Authors: Wenzhi Dave Ding (PolyU,
  corresponding), Xincheng Wang (PolyU), Yucheng Wang (University of Sydney),
  Zhenxuan Wang (NC State).
china_related: true
domains:
- labor
- environment
- transportation
- climate

data_pathway:
  mode: inaccessible
  origin: researcher-collected
  target_artifact: >-
    Driver-day panel of labor supply and on-duty safety outcomes for heavy-duty
    truck drivers in Guangdong, March 2023 - June 2025, constructed from
    vehicle GPS/sensor records: working-day indicator, maximum consecutive
    driving hours, completed trips, start-late indicator, accident-risk
    warnings per 100 km, yawning per 100 km; joined to hourly ERA5-Land weather
    along GPS trajectories, Guangdong air-quality station data, ASTER GDEM v3
    terrain, and OSM road/waterway features; firm-level heat-subsidy status
    from a phone survey; driver demographics from an online survey of 190
    drivers.
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: >-
    Grounding-b16 (2026-08-15): JEEM 138 (2026) 103338 full text read via the
    PolyU Institutional Repository (hdl.handle.net/10397/118478; hybrid open
    access, CC BY 4.0). Data section 2 read in full: sample = March 2023 to
    June 2025, approximately 10,000 trucks and 130 freight companies in
    Guangdong; GPS logged every 20 s in motion and every two minutes when
    stationary (battery-powered, records even with engine off); three states
    (off-duty rest, on-duty idle, actively driving) aggregated to driver-day;
    AI-enhanced driver-monitoring systems generate sensor-based accident-risk
    warnings (unsafe lane departures, collision warnings, tailgating, speeding);
    in-cab cameras with computer vision detect yawning; weather = hourly
    ERA5-Land (0.1-degree grid, ~9 km); air pollution = hourly records from all
    Guangdong monitoring stations (AQI and major pollutants, IDW interpolation);
    terrain = ASTER GDEM v3 at 30 m; road/waterway = OpenStreetMap; driver
    characteristics = online survey of 190 randomly selected drivers; heat
    subsidies = phone survey of transportation companies. DAS: "The data used
    in this study are proprietary and were made available under a data usage
    agreement. Authors will provide information on data access upon request."
    Provider unnamed. Companion WP exists (Ding, Wang, Wang & Wang 2025,
    "Steering Adaptation: Firm, Labor Contracts, and Driver Responses to Heat
    in the Trucking Industry") - no PDF found. NOTE: not merged with
    china-city-to-city-truck-flows (G7): different observation unit
    (driver-day vs city-pair flows), geography (Guangdong vs national),
    window (2023-2025 vs 2019-2022), and provider identity (unnamed vs G7).
  barrier: >-
    Proprietary telematics data with a data-usage agreement; the DAS offers
    "information on data access upon request" - not the data, and no public or
    application route exists. Rebuilding the panel is impossible without the
    fleet records (GPS/sensor feeds, camera footage) that only the unnamed
    provider and freight companies hold.

unit_of_observation: driver-day (constructed from vehicle-level GPS and sensor records; about 10,000 heavy-duty trucks)
structure: panel (driver-day over March 2023 - June 2025)
geo_granularity:
- GPS trajectory level (route-level weather/pollution/terrain exposure)
- Guangdong province (fleet operating region)
geography: Guangdong province, China; ~10,000 heavy-duty trucks across ~130 freight companies
time_span:
  start: '2023-03'
  end: '2025-06'
  last_confirmed_release: 'No release; DAS states proprietary data under a data usage agreement'
  coverage_note: >-
    Sample window March 2023 - June 2025 per the published JEEM 2026 data
    section. Driver-day aggregation; weather/pollution matched to trajectories.
  last_checked: '2026-08-15'
frequency:
- high-frequency GPS (20 s moving / 2 min stationary); daily aggregation for outcomes
sample_size: ~10,000 trucks; ~130 freight companies; 190 drivers in the online survey; 28 months (Mar 2023 - Jun 2025)
key_variables:
- Labor supply: working-day indicator, maximum consecutive driving hours, completed trips, start-late indicator (driver-day)
- Safety: accident-risk warnings per 100 km (AI sensor-based), yawning per 100 km (in-cab camera + computer vision)
- Exposure: hourly temperature/precipitation/wind (ERA5-Land) along trajectory; AQI and pollutants (Guangdong stations, IDW); slope/elevation (ASTER GDEM v3); road/waterway (OSM)
- Firm-level: heat-subsidy provision (phone survey)
- Driver-level: age, gender, prior driving experience (online survey, 190 drivers)

research_fit:
  best_for:
  - Heat (or weather) effects on labor supply and on-the-job safety at the driver-day level for heavy-duty trucking in Guangdong 2023-2025
  - Occupational heat-exposure mechanisms (fatigue via yawning, rest disruption, schedule reallocation)
  - Heterogeneity by firm heat-subsidy provision and by driver characteristics
  choose_over:
  - Choose this over china-city-to-city-truck-flows (G7) for driver-level labor questions: that asset is city-pair flow counts, not individual telematics; the two are NOT the same product and must not be merged
  - Choose this over household/labor surveys for within-day driving behavior, fatigue, and safety-warning outcomes
  not_good_for:
  - Anything outside Guangdong or outside March 2023 - June 2025
  - Aggregate freight-flow or trade-network analysis (that is china-city-to-city-truck-flows' role)
  - Obtaining the actual microdata: proprietary, no evidenced route
  - Driver demographics beyond the 190-driver survey subsample (administrative records contain no demographics)
  needs_join_for:
  - Firm outcomes, market conditions, or supply-chain context outside the fleet records
  - Realized accidents (warnings are proxies for unsafe episodes, not accident occurrences)
  variation_available:
  - Daily temperature variation along routes (hourly ERA5-Land matched to trajectories)
  - Cross-firm heat-subsidy variation (phone survey)
  - Driver-level heterogeneity from the 190-driver survey
  topics:
  - extreme heat
  - labor supply
  - occupational safety
  - trucking
  - telematics
  - climate adaptation

good_for:
- climate and labor
- occupational health
- driver behavior
identification:
- high-dimensional fixed effects / event-study temperature bins
- heterogeneity by heat-subsidy firms
linkable_keys:
- Driver (anonymized)
- Date
- GPS trajectory (location-time)

joins:
- target: china-city-to-city-truck-flows
  relation: often-confused-with
  keys: []
  method: >-
    Different product: G7 city-pair truck flows (national, 2019-2022) vs
    Guangdong driver-day telematics (2023-2025). Do not merge; no shared
    observation unit evidenced.
  evidence_status: verified
- target: era5-land
  relation: complement
  keys:
  - location
  - time
  method: Hourly ERA5-Land weather along GPS trajectories (the paper's own exposure source)
  evidence_status: literature-used

access_routes:
- route: polyu-ir-full-text
  access_status: available
  direct_url: http://hdl.handle.net/10397/118478
  requirements: None (hybrid open access under CC BY 4.0; fetched 2026-08-15)
  steps:
  - Open the PolyU Institutional Repository record (hdl.handle.net/10397/118478).
  - Download the published PDF (bitstream 10397/118478/1/1-s2.0-S0095069626000586-main.pdf) and read section 2 (Data and variable construction) plus the Data availability statement.
  deliverable: Published article full text incl. DAS; NOT the data.
  cost: free
  last_checked: '2026-08-15'
  caveat: The DAS only promises information on data access upon request; no data file is attached.
- route: data-usage-agreement-request
  access_status: needs-verification
  direct_url: https://doi.org/10.1016/j.jeem.2026.103338
  requirements: Request to the authors per the DAS ("Authors will provide information on data access upon request"); outcome unknown
  steps:
  - Contact the corresponding author (Wenzhi Dave Ding, PolyU) per the DAS for information on data access.
  - Expect a proprietary data-usage agreement if access is granted at all.
  deliverable: Possibly information on data access terms; not guaranteed data delivery.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: The DAS wording provides information, not data; treat any grant as uncertain.
- route: companion-working-paper
  access_status: blocked
  direct_url: needs-verification
  requirements: 'Companion WP (Ding, Wang, Wang & Wang 2025, "Steering Adaptation: Firm, Labor Contracts, and Driver Responses to Heat in the Trucking Industry") exists per the article references and the author personal site; no PDF found in this environment'
  steps:
  - Locate the companion WP PDF (author site/SSRN; not fetched 2026-08-15).
  - Use it for additional variable-construction detail (the JEEM paper refers readers to Ding et al. 2025 for context/data details).
  deliverable: Working-paper text; still not the data.
  cost: free
  last_checked: '2026-08-15'
  caveat: No PDF was found this session; the reference is to the paper's own citation.

access:
  url: http://hdl.handle.net/10397/118478
  cost: by-application
  license: Article CC BY 4.0 (hybrid OA); underlying data proprietary per DAS
  format: []
  api: false
  how_to_get: >-
    The telematics microdata are proprietary and obtainable only (if at all)
    through a data-usage agreement via the authors; the public route is the
    open-access article text, which documents construction and the DAS.
caveats: >-
  Provider and freight companies are unnamed - do not infer a vendor. GPS
  states (off-duty rest / on-duty idle / actively driving) are classification
  constructions with fixed thresholds (6 h, 10 min); accident-risk warnings are
  proxies for unsafe episodes, not realized accidents. Administrative records
  contain no driver demographics; heterogeneity evidence rests on the
  190-driver survey. Distinct asset from china-city-to-city-truck-flows (G7) -
  do not merge.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Ding, Wenzhi Dave; Xincheng Wang; Yucheng Wang & Zhenxuan Wang (2026), Too hot to haul? The impact of temperature on labor supply and performance of truck drivers'
  doi: https://doi.org/10.1016/j.jeem.2026.103338
  journal: Journal of Environmental Economics and Management
  year: 2026
  dataset_role: Main analysis dataset - driver-day labor supply and safety panel from Guangdong truck telematics, with weather/pollution/terrain exposure
  evidence_type: article-full-text
  evidence_url: http://hdl.handle.net/10397/118478
  data_note: >-
    Full text read 2026-08-15 via PolyU IR (hybrid OA, CC BY): ~10,000 trucks /
    ~130 freight companies, Guangdong, Mar 2023 - Jun 2025; GPS 20 s moving /
    2 min stationary; AI accident-risk warnings; in-cab cameras (yawning);
    ERA5-Land hourly; Guangdong AQ stations; ASTER GDEM v3; OSM; phone survey
    on heat subsidies; online survey of 190 drivers. DAS: proprietary data
    under a data usage agreement; authors provide information on data access
    upon request. Provider unnamed. Companion WP: Ding et al. 2025 "Steering
    Adaptation..." (no PDF found).

provenance:
- source: http://hdl.handle.net/10397/118478
  field_scope:
  - data_identity
  - sample
  - variables
  - construction
  - access
  - paper_use
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://doi.org/10.1016/j.jeem.2026.103338 (OpenAlex JEEM 138:103338)
  field_scope:
  - published_metadata
  - paper_identity
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Author personal website (Wenzhi Ding, PolyU; fetched 2026-08-15) - companion WP listing
  field_scope:
  - companion_paper
  added: '2026-08-15'
  confidence: med
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-truck-driver-telematics, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-city-to-city-truck-flows
  relation: often-confused-with
- id: era5-land
  relation: complement
---

## Positioning in one sentence

The Ding, Wang, Wang & Wang (2026 JEEM) asset is a proprietary driver-day telematics panel for about 10,000 Guangdong heavy-duty trucks (Mar 2023 - Jun 2025: GPS, AI safety warnings, in-cab camera fatigue, matched ERA5-Land/air-quality/terrain exposure) - fully documented in the CC BY open-access article but obtainable only, if at all, through the authors' data-usage agreement, and it is a different product from the G7 city-pair truck-flow panel.

## Select rules

- Use this identity for driver-level heat/labor/safety questions in Guangdong trucking 2023-2025; the open-access article documents construction completely even though the data are restricted.
- Do not merge with china-city-to-city-truck-flows (G7): different unit (driver-day vs city-pair flows), region, window, and provider.
- For weather exposure layers, era5-land is the public component a researcher can obtain independently; the fleet records cannot be rebuilt from it.

## Get recipe

1. Download the open-access JEEM article from the PolyU IR (hdl.handle.net/10397/118478, CC BY) and read section 2 for the full construction recipe and the DAS.
2. If the research design requires the actual driver-day panel, the only evidenced route is requesting information on data access from the authors (DAS); expect a proprietary data-usage agreement and uncertain outcome.
3. For weather/pollution/terrain layers, the public sources (ERA5-Land, Guangdong AQ stations, ASTER GDEM v3, OSM) are obtainable independently, but they cannot reproduce the fleet-side panel.

## Connections and Limitations

- The GPS state classification (off-duty rest >6 h; idle >10 min) is a construction choice; any rebuild must replicate these thresholds.
- Accident-risk warnings are proxies for unsafe driving episodes, not realized accidents; camera-based yawning is the fatigue mechanism measure.
- Administrative records lack demographics; all driver-heterogeneity evidence comes from the 190-driver online survey.
- Provider and companies are unnamed; no vendor inference is supported.
