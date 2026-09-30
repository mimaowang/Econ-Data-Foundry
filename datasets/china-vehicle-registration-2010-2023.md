---
schema_version: 3
catalog_status: grounding
id: china-vehicle-registration-2010-2023
name: China city-month vehicle sales panel 2010-2023 (registration + compulsory-insurance records)
aka:
- 车辆注册数据
- 交强险上险数据
- vehicle registration data China
- Compulsory Traffic Accident Liability Insurance records
- 中国汽车销量数据
provider: >-
  Unnamed commercial/official compilation used by the paper (Fang, Li, Wang
  & Yang): per the NBER WP data section (w33489, read 2026-08-15), "data
  from 2010 to 2015 are derived from official vehicle registration records,
  while data from 2016 to 2023 are sourced from Compulsory Traffic Accident
  Liability Insurance records" (交强险-based vehicle sales/insurance data,
  the standard Chinese auto-market source family). The exact supplier
  (registration authority extract vs insurance-data vendor) is NOT named in
  the WP.
china_related: true
domains:
- transportation
- environment
- urban
- automobile

data_pathway:
  mode: inaccessible
  origin: researcher-collected
  target_artifact: >-
    City-month panel of vehicle sales (new and pre-owned) for 328 prefectural
    cities, January 2010 to December 2023, with sales volume and market share
    by powertrain type (pure battery EV / fuel / hybrid), constructed by the
    authors from two raw inputs: official vehicle registration records
    (2010-2015) and Compulsory Traffic Accident Liability Insurance (CTALI/
    交强险) records (2016-2023).
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    Route-B grounding (2026-08-15): NBER WP w33489 ("High-Speed Rail and
    China's Electric Vehicle Adoption Miracle", Feb 2025) fetched and data
    section 3.1 read in full: city-month panel, 328 prefectural cities,
    Jan 2010-Dec 2023, new + pre-owned; 2010-2015 from official vehicle
    registration records; 2016-2023 from CTALI records; three powertrain
    classes (pure BEV/FV/hybrid); outcomes sales volume and market share;
    national EV trajectory from CSMAR (footnote 5). Supplementary data:
    charging stations from Gaode Maps POIs (2010-2023), road networks from
    statistical yearbooks, SAIC firm registrations. IDEAS page confirms the
    published version (JPubE vol 260, 2026, DOI 10.1016/j.jpubeco.2026.
    105705; authors Fang, Hanming; Li, Ming; Wang, Long; Yang, Yang). The
    data supplier is unnamed in the WP; the published-version data
    availability statement is unread (Elsevier 403).
  barrier: >-
    Raw inputs (official registration records; CTALI records) are
    administrative/commercial, not publicly downloadable; the paper's exact
    supplier is unnamed; no replication data deposit found.

unit_of_observation: city-month (vehicle sales volume and market share by powertrain); raw inputs are vehicle-level records
structure: panel (city-month, 328 cities x 168 months)
geo_granularity:
- prefecture-level city (328 cities)
geography: 328 prefectural cities of China, Jan 2010 - Dec 2023
time_span:
  start: '2010-01'
  end: '2023-12'
  last_confirmed_release: 'NBER WP w33489 (Feb 2025) data section 3.1'
  coverage_note: >-
    City-month panel 2010.1-2023.12, 328 prefectural cities; 2010-2015 from
    official registration records, 2016-2023 from CTALI records. Published
    JPubE version (2026) coverage unverified against the WP.
  last_checked: '2026-08-15'
frequency:
- monthly
sample_size: >-
  328 prefectural cities x 168 months; sales volume and market share by
  powertrain type (pure BEV, fuel, hybrid), new + pre-owned.
key_variables:
- Vehicle sales volume (units) by powertrain (pure BEV / fuel / hybrid)
- Market share by powertrain within city-month
- New and pre-owned vehicles
- City and month identifiers
- (Raw inputs: vehicle registration records 2010-2015; CTALI insurance records 2016-2023)

research_fit:
  best_for:
  - City-month EV-adoption and vehicle-market measurement by powertrain, 2010-2023
  - City-level vehicle sales/market-share panels by powertrain 2010-2023
  - Transport-network and charging-infrastructure effects on vehicle adoption
  choose_over:
  - Choose this over csmar for city-month sales panels by powertrain; CSMAR carries the national EV trajectory used in the paper's Figure 1, not the city panel.
  - Pair with a separately sourced city-year transport-network measure only after harmonizing city names and time conventions; this record supplies the vehicle-market side, not a transport-network series.
  not_good_for:
  - Vehicle-level microdata (make/model/VIN-level fields): the paper's asset is a city-month panel; raw vehicle records are unnamed and restricted
  - Post-2023 or pre-2010 city panels
  - Provincial/national aggregates when city-level variation is needed
  - Reconstructing the exact panel without the two restricted raw inputs
  needs_join_for:
  - HSR network connectivity (china-high-speed-rail-network)
  - Charging infrastructure and road networks (paper constructs these from Gaode POIs and yearbooks)
  - Firm-registration controls (SAIC; china-firm-registry family)
  variation_available:
  - Observed city, month, new/pre-owned status and powertrain-class dimensions in the documented panel
  - This data record does not classify treatment assignment, comparison groups or causal designs
  topics:
  - electric vehicles
  - vehicle registration
  - automobile market

good_for:
- EV adoption
- city vehicle market panels
- transport policy effects
identification:
- City-month vehicle sales volume and market share by powertrain, constructed from two distinct raw record systems
- The 2010-2015 registration-record segment and 2016-2023 CTALI segment must remain separately labeled when assessing continuity or making a new panel
linkable_keys:
- City code
- Month/year

joins:
- target: china-high-speed-rail-network
  relation: complement
  keys:
  - city
  - year
  method: Match a separately sourced transport-network measure to the vehicle panel only by documented city and time keys; this record makes no treatment or causal-design claim.
  evidence_status: literature-used
- target: csmar
  relation: complement
  keys:
  - year
  method: 'national EV trajectory (paper Figure 1, footnote 5: https://data.csmar.com/)'
  evidence_status: verified
- target: china-firm-registry
  relation: complement
  keys:
  - city
  - year
  method: SAIC firm registrations as supply-side controls (paper section 3.2; same SAMR/SAIC registration family, extract vintage differs)
  evidence_status: literature-used

access_routes:
- route: nber-working-paper
  access_status: available
  direct_url: https://www.nber.org/papers/w33489
  requirements: None
  steps:
  - Download the NBER WP w33489 PDF (fetched 2026-08-15, 51 pages).
  - Read section 3.1 for the vehicle-sales panel construction and section 3.2 for the supplementary data (charging stations, roads, firm registrations).
  deliverable: Full working-paper text with data construction details; not the data itself.
  cost: free
  last_checked: '2026-08-15'
  caveat: WP (Feb 2025) may differ from the published JPubE 2026 version.
- route: published-journal
  access_status: blocked
  direct_url: https://doi.org/10.1016/j.jpubeco.2026.105705
  requirements: Institutional access or human browser (Elsevier 403 for automated clients)
  steps:
  - Read the published JPubE data section and data availability statement for the supplier identity (unnamed in the WP).
  deliverable: Published data section; supplier identity and any data availability statement.
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Elsevier 403 for automated clients (recorded in failed_tasks).
- route: raw-inputs
  access_status: blocked
  direct_url: needs-verification
  requirements: Not evidenced; official registration records and CTALI records are administrative/commercial
  steps:
  - No public route evidenced for the raw registration/insurance records.
  deliverable: None public.
  cost: paid
  last_checked: '2026-08-15'
  caveat: Commercial 交强险 data products exist in the market but no supplier or terms are evidenced for this paper.

access:
  url: https://www.nber.org/papers/w33489
  cost: by-application
  license: Restricted/commercial raw inputs; paper text free via NBER
  format: []
  api: false
  how_to_get: >-
    The paper's city-month panel is not publicly released. The NBER WP is
    the obtainable evidence of construction; raw inputs (official vehicle
    registration records, CTALI records) have no evidenced public route.
caveats: >-
  The supplier of the vehicle data is unnamed in the WP; do not infer a
  vendor. The 2010-2015 vs 2016-2023 split means the panel is built on two
  different record systems (registration vs insurance) - a measurement
  boundary the paper itself relies on. Published-version DAS unread.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Fang, Li, Wang & Yang (2026), High-Speed Rail and China''s Electric Vehicle Adoption Miracle'
  doi: https://doi.org/10.1016/j.jpubeco.2026.105705
  journal: JPubE
  year: 2026
  dataset_role: City-month vehicle sales and market-share panel by powertrain, 2010-2023
  evidence_type: working_paper_data_section
  evidence_url: https://www.nber.org/papers/w33489
  data_note: >-
    WP data section 3.1 read (2026-08-15): 328 prefectural cities, Jan
    2010-Dec 2023, new + pre-owned; 2010-2015 official vehicle registration
    records; 2016-2023 CTALI records; pure BEV/FV/hybrid classes; sales
    volume + market share. Supplier unnamed. The published JPubE data
    availability statement remains unread (Elsevier 403).

provenance:
- source: https://www.nber.org/system/files/working_papers/w33489/w33489.pdf
  field_scope:
  - data_identity
  - sample
  - variables
  - construction
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://ideas.repec.org/a/eee/pubeco/v260y2026ics0047272726001416.html
  field_scope:
  - published_metadata
  - abstract
  - authors
  added: '2026-08-15'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-vehicle-registration-2010-2023, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-high-speed-rail-network
  relation: complement
- id: csmar
  relation: complement
- id: china-firm-registry
  relation: often-confused-with
---

## Positioning in one sentence

The JPubE 2026 paper's asset is a city-month vehicle sales panel (328 prefectural cities, 2010-2023, by powertrain) built from official vehicle registration records (2010-2015) and Compulsory Traffic Accident Liability Insurance records (2016-2023) - restricted/commercial raw inputs with an unnamed supplier, documented from the readable NBER WP.

## Select rules

- Use for city-month EV-adoption and vehicle-market questions, 2010-2023; if a separate transport-network measure is needed, match it by documented city and time keys.
- Do not treat the paper's city-month panel as public vehicle-registration microdata; the raw records are unnamed and restricted.
- For national EV series use csmar (the paper's own Figure 1 source); for firm-registration controls note the SAIC family (china-firm-registry extract differs by vintage).

## Get recipe

1. Download NBER WP w33489 and read sections 3.1-3.2 for the construction recipe.
2. If the research design requires the actual panel, the route is the raw inputs (registration + CTALI records) - no supplier or public route evidenced; treat as restricted.
3. Check the published JPubE data availability statement via a human browser/library for the supplier identity.

## Connections and Limitations

- Two record systems (registration 2010-2015; insurance 2016-2023) are spliced in the panel; cross-system comparability is the paper's construction choice.
- Supplier identity and the published-version DAS are the key open items.
- Vehicle-level microdata (make/model) is not the paper's released asset; do not over-promise granularity.
