---
schema_version: 3
catalog_status: ready
id: china-fishing-vessel-detection
name: Global Fishing Watch (GFW) public AIS-based vessel and fishing activity data
aka:
- GFW
- Global Fishing Watch data portal
- GFW API v3
- AIS vessel presence
- fishing effort
provider: >-
  Global Fishing Watch, Inc., a Delaware 501(c)(3) non-profit (per the
  official Terms of Use page, last modified 2021-05-21, read 2026-08-15).
  Data arm: public data download portal and API gateway
  (gateway.api.globalfishingwatch.org, API v3).
china_related: true
domains:
- environment
- marine
- regional
- satellite

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    GFW public datasets and dynamic API products, including fishing effort,
    AIS vessel presence, vessel identity/search and fishing events. The
    provider's current route is an account plus an individually requested API
    key; access is then through the v3 API gateway, portal, or documented R
    and Python clients. The public download-portal shell is not itself an
    evidence-backed dataset inventory.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider-first recheck (2026-09-28): the rendered official "Our APIs"
    page gives a current, executable academic route—register for a GFW
    account, request an API key, agree to terms/attribution, and state the
    intended impact of the work. It identifies fishing effort (nearly 70,000
    AIS-broadcasting vessels, global space/time), vessel search/identity,
    fishing events, AIS vessel presence and related functions; it also links
    the gfwr R package and official Python client. This makes the public GFW
    data family directly recommendable for its stated AIS-based roles. Terms
    retain CC BY-NC 4.0 for data products and Apache 2.0 for code; do not
    scrape the public site or represent an API key as anonymous access.
  barrier: >-
    GFW data require an account and requested API key rather than anonymous
    gateway calls. The JEEM 2025 Yuan paper's separate AIS component remains
    unverified: its abstract does not name GFW, and its nighttime-detection
    layer is a different satellite-data family.

unit_of_observation: >-
  Vessel activity/presence observations (AIS-based) and fishing-effort
  aggregates, global waters; dataset-specific units per portal records
structure: geospatial activity datasets (gridded/track-level per dataset)
geo_granularity:
- global ocean grid/cells (dataset-specific)
- vessel-level tracks (dataset-specific)
geography: Global oceans, including Chinese waters (EEZ-level coverage per GFW global products)
time_span:
  start: '2012'
  end: '2025'
  last_confirmed_release: 'GFW global AIS products span 2012-present (per GFW documentation pages; exact per-dataset coverage unverified this round)'
  coverage_note: >-
    GFW's AIS-derived products start around 2012 when AIS coverage became
    systematic. The JEEM 2025 anchor paper's study window and detection
    product are unread. Exact per-dataset time coverage must be read from
    the portal/dataset pages.
  last_checked: '2026-08-15'
frequency:
- daily-to-annual activity summaries (dataset-specific)
sample_size: >-
  Not verified this round; portal dataset pages list per-dataset sizes
  (unread - SPA requires token flow).
key_variables:
- Vessel presence (AIS-based), flag, vessel type, speed
- Fishing effort hours and gear type (dataset-specific)
- Spatial grid cells and timestamps (dataset-specific)

research_fit:
  best_for:
  - AIS-based vessel activity and fishing-effort research in Chinese and global waters with a free, documented API and non-commercial license
  - Building fishing-activity exposure measures (e.g., seasonal ban compliance, spillover) from a public source
  choose_over:
  - Choose GFW over commercial AIS resellers when non-commercial academic use, free API access, and documented methodology matter.
  - For nighttime-lights-based vessel detection (VIIRS-DNB type), use NOAA/NASA products - GFW is AIS-based, not a nighttime detection product.
  not_good_for:
  - Claiming the JEEM 2025 anchor paper used GFW (unverified - the paper's AIS provider is unnamed in the abstract).
  - Vessels without AIS (dark fleet detection requires satellite imagery products, not GFW AIS data).
  - Commercial redistribution (CC BY-NC 4.0 restricts commercial use).
  needs_join_for:
  - Nighttime vessel detection (satellite VIIRS-type) - separate product family from GFW AIS
  - Fleet registry/subsidy data (see candidate china-distant-water-fishing-fleet)
  variation_available:
  - Global spatial and temporal variation in AIS vessel presence and fishing activity (2012-present)
  topics:
  - fishing activity
  - marine policy
  - vessel detection
  - AIS data

good_for:
- fishing-ban compliance and spillover analysis (outcome layer)
- vessel activity exposure construction
- marine spatial analysis
identification:
- >-
  AIS-based activity observations describe vessel presence and behavior across
  space and time; the data product itself does not supply a causal assignment.
linkable_keys:
- Vessel identifier (MMSI, dataset-specific)
- Spatial cell coordinates and timestamps

joins: []

access_routes:
- route: data-portal
  access_status: available-with-registration
  direct_url: https://globalfishingwatch.org/data-download/
  requirements: >-
    Portal is a JavaScript SPA; bulk download via API requires registration
    (GFW registration form per Terms of Use) and a token
  steps:
  - Open https://globalfishingwatch.org/our-apis/ and choose Register for a GFW account.
  - Request an API key at the provider's API-key route, describe the intended research impact, and accept the terms/attribution conditions.
  - Use the documented API, portal, gfwr R package, or Python client to select the needed product (for example, fishing effort or AIS vessel presence).
  - Preserve the API query, product version, filters, time window, and attribution; keep use non-commercial under CC BY-NC 4.0.
  deliverable: API/portal responses for the selected GFW AIS-based product (fishing effort, presence, events or identity), subject to the approved key and product-specific query settings.
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    Anonymous /v3/datasets returned 401 (2026-08-15). The current provider
    page confirms account registration and a requested API key, but not an
    anonymous bulk-download route. Each API request still needs product- and
    query-specific documentation.
- route: api-r-python
  access_status: available-with-registration
  direct_url: https://globalfishingwatch.github.io/gfwr/
  requirements: GFW API token; R or Python environment
  steps:
  - Install the gfwr R package (or use the documented Python package).
  - Supply the API token and query the target dataset.
  - Follow the official examples for data filtering and formats.
  deliverable: Tidy data frames from GFW APIs for analysis workflows.
  cost: free
  last_checked: '2026-08-15'
  caveat: API v3 gateway requires token auth; rate limits per GFW documentation (unread this round).

access:
  url: https://globalfishingwatch.org/data-download/
  cost: free
  license: >-
    CC BY-NC 4.0 for data products (non-commercial, attribution); Apache 2.0
    for code; commercial use requires contacting GFW (official Terms of Use,
    read 2026-08-15)
  format:
  - CSV/geospatial downloads via portal
  - API (JSON) via gateway
  api: true
  how_to_get: Register on the GFW data portal, obtain a token, and download datasets via the portal or the v3 API (R/Python helpers documented).
caveats: >-
  GFW products are AIS-based; vessels not transmitting AIS are not covered.
  The JEEM 2025 anchor paper's detection data (nighttime vessel detections +
  AIS) is unread - do not assume GFW identity. Exact dataset list, per-
  dataset coverage, and rate limits require the logged-in portal.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Yuan (2025), seasonal fishing bans in China''s EEZ: novel nighttime vessel detections plus AIS-equipped vessel data'
  doi: https://doi.org/10.1016/j.jeem.2025.103202
  journal: JEEM
  year: 2025
  dataset_role: AIS-equipped vessel data component (provider unverified)
  evidence_type: abstract-only
  evidence_url: https://doi.org/10.1016/j.jeem.2025.103202
  data_note: >-
    Abstract read (Layer-2b sweep): "a novel dataset of nighttime vessel
    detections" + AIS-equipped vessel data, seasonal fishing bans in China's
    EEZ, RDiT, spillovers to neighboring EEZs. The abstract does not name
    the AIS provider; GFW is a plausible public source but identity is
    UNVERIFIED (data section unread).
- cite: 'Englander, Zhang, Villasenor-Derbez, Jiang, Hu, Deschenes & Costello (2025), Input subsidies and the depletion of natural capital: Chinese distant water fishing'
  doi: https://doi.org/10.1016/j.jeem.2025.103127
  journal: JEEM
  year: 2025
  dataset_role: >-
    Main outcome: vessel-level hours of fishing (fishing effort) for
    China-flagged distant water vessels, 2015-2020, from GFW AIS-based
    data (machine-learning-predicted fishing activity, Kroodsma et al.
    2018), matched to an RFMO/Rongcheng registry panel
  evidence_type: data-section
  evidence_url: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content
  data_note: >-
    Verified at data-section level 2026-08-15 from the World Bank Policy
    Research Working Paper 10412 (same authors/title; full text read): "We
    measure fishing behavior using real-time data from Global Fishing Watch
    (GFW)... fishing effort data from GFW are derived from AIS transponder
    signals"; extracted all China-flagged vessels 2015-2020 (hours of
    fishing); matched ~70% of the 2,216-vessel registry panel on
    registry name/MMSI (SSVID)/call sign/IMO (priority name+MMSI >
    name+call sign > name+IMO). The JEEM 130 (2025) 103127 published
    version is closed access; the WP is the same paper.

provenance:
- source: https://globalfishingwatch.org/our-apis/ (read 2026-08-15)
  field_scope:
  - portal and API identity
  - free download claim
  - AIS vessel presence product
  - R (gfwr) and Python packages
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://globalfishingwatch.org/terms-of-use/ (read 2026-08-15)
  field_scope:
  - non-commercial CC BY-NC 4.0 license
  - Apache 2.0 for code
  - registration requirement for bulk download/API
  - scraping prohibition
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://gateway.api.globalfishingwatch.org/v3/datasets (401, 2026-08-15)
  field_scope:
  - token auth requirement for API
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://globalfishingwatch.org/our-apis/ (rendered official page read 2026-09-28)
  field_scope:
  - current account-registration and requested-API-key route
  - required intended-impact description and terms/attribution agreement
  - current API functions: fishing effort, AIS presence, vessel identity/search, fishing events and related products
  - provider statement that fishing effort covers nearly 70,000 AIS-broadcasting vessels globally across space and time
  - current gfwr R and Python-client links
  added: '2026-09-28'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-fishing-vessel-detection, Layer-2b sweep)
  field_scope:
  - paper anchor (abstract-level)
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: gfw-static-apparent-fishing-effort-v3-2012-2024
  relation: often-confused-with
---

## Positioning in one sentence

Global Fishing Watch is a free-for-non-commercial-use, API-key-gated AIS vessel-activity platform with a documented route for fishing effort, AIS presence, vessel identity and events. It is the verified fishing-effort source in the Englander et al. JEEM 2025 study; it is only a possible, unverified AIS source for the separate Yuan fishing-ban paper.

## Select rules

- Prioritize GFW for AIS-based vessel activity and fishing effort in Chinese/global waters under non-commercial academic terms.
- For nighttime light-based vessel detection (the other component named in the JEEM abstract), use satellite products (NOAA VIIRS-type), not GFW.
- Confirm the target paper's AIS provider from its data section before claiming GFW identity.

## Get recipe

1. Visit https://globalfishingwatch.org/our-apis/, create a GFW account and request an API key; the provider asks users to describe their intended impact and agree to terms/attribution.
2. Choose the named API product matching the question—fishing effort, AIS vessel presence, vessel identity/search or fishing events—then make a documented token-authenticated query through the API, portal, gfwr R package or Python client.
3. Save the product selection, filters, time window and API version with the returned data; observe CC BY-NC 4.0 attribution and non-commercial-use terms.

## Connections and Limitations

- GFW data start around 2012 (AIS coverage); exact per-dataset coverage is on the portal (token-gated).
- Vessels without AIS are invisible to GFW products - combine with satellite detection products for dark-fleet questions.
- The candidate china-distant-water-fishing-fleet (fleet registry/subsidy) is a distinct layer; join by vessel identifier where available.
