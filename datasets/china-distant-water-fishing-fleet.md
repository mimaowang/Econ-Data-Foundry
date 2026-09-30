---
schema_version: 3
catalog_status: grounding
id: china-distant-water-fishing-fleet
name: Chinese distant water fishing fleet registry and fuel-subsidy panel (RFMO + Rongcheng, 2015-2020)
aka:
- 中国远洋渔业船队
- distant water fishing fleet registry
- 远洋渔船名录
provider: >-
  Paper-constructed by Englander (World Bank), Zhang (Ocean University of
  China), Villasenor-Derbez (U Miami), Jiang (HKU), Hu (Mayo Clinic),
  Deschenes (UCSB) and Costello (UCSB Bren), from public inputs: vessel
  registries of seven Regional Fishery Management Organizations (RFMOs) for
  vessels flagged to mainland China, the Rongcheng (荣成) municipal distant
  water vessel dataset on the Shandong Provincial Open Data Platform
  (developed 2018), and Ministry of Agriculture fuel-subsidy policy
  documents (2016-2020 formula).
china_related: true
domains:
- environment
- marine
- firm
- policy

data_pathway:
  mode: constructed
  origin: researcher-constructed
  target_artifact: >-
    A vessel-level panel of the Chinese distant water fishing fleet (2,216
    vessels after deduplication) with registry characteristics (gear, length,
    gross tonnage, engine power, build year, MMSI, call sign, IMO, previous
    name, target species, authorized fishing area, freezer type, firm, RFMO
    membership) and the fuel-subsidy schedule implied by the 2016-2020
    subsidy formula (25 engine-power thresholds). Fishing-activity outcomes
    come from GFW (see china-fishing-vessel-detection); this record covers
    the registry/subsidy layer only.
  availability: reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Grounding pass (2026-08-15): the World Bank Policy Research Working
    Paper 10412 (same paper as JEEM 130 (2025) 103127, full text read)
    documents the construction first-hand. Vessel characteristics: compiled
    from RFMO registration databases (7 RFMOs; registry name, gear, length,
    gross tonnage, engine power, build year, MMSI, call sign, IMO) plus the
    Rongcheng municipal dataset on the Shandong Provincial Open Data
    Platform (318 vessels + 104 additional), standardized units, deduplicated
    to 2,216 Chinese distant water vessels (vs 2,705 legally authorized at
    end-2020 per the Chinese Fisheries Statistical Yearbook). Subsidy layer:
    fuel subsidy formula Subsidy = Standard x GearFactor (10 gears) x
    SubsidizedEnginePower x SubsidyDays under the 2016 reform, with 25
    engine-power thresholds creating the RD discontinuities; policy window
    studied 2016-2020 (2021+ replaced by compliance awards). Fishing effort
    is the GFW layer (see china-fishing-vessel-detection used_by).
  barrier: >-
    The paper's compiled vessel panel and matching code are not released.
    RFMO registries and the Rongcheng open-data dataset are public inputs
    but scattered across seven RFMO systems; subsidy thresholds require the
    MOA policy documents (formula documented in the WP). The published JEEM
    version is closed access (WP is open).

unit_of_observation: Chinese distant water fishing vessel (vessel-RFMO records; analysis at vessel-year)
structure: vessel-level panel (constructed), cross-referenced to GFW fishing hours
geo_granularity:
- vessel
- RFMO region
geography: Chinese distant water fleet operating in EEZs of 40+ countries and high seas (Pacific, Indian, Atlantic, Southern Ocean); registry sources global (RFMOs) + Rongcheng (Shandong)
time_span:
  start: '2015'
  end: '2020'
  last_confirmed_release: 'GFW extraction window 2015-2020; subsidy analysis window 2016-2020; registry built to end-2020 universe'
  coverage_note: >-
    Vessels present in the seven RFMO registries plus Rongcheng; vessels
    authorized outside RFMO regions (e.g., bilateral EEZ access) are missing
    (paper footnote 11).
  last_checked: '2026-08-15'
frequency:
- annual
sample_size: >-
  2,216 Chinese distant water fishing vessels (paper; after dedup across
  RFMOs and Rongcheng); ~70% matched to GFW AIS fishing hours; 2,705 legally
  authorized distant water vessels at end-2020 (Chinese Fisheries Statistical
  Yearbook, cited in paper)
key_variables:
- Registry name (Chinese pinyin), gear, length, gross tonnage, engine power, build year
- MMSI, call sign, IMO, previous name (matching identifiers)
- Target species, authorized fishing area, freezer type, owning firm, RFMO membership
- Fuel subsidy formula inputs: subsidy standard (year), gear factor, subsidized engine power, subsidy days
- Vessel-level fuel subsidy amount (deterministic function of characteristics and activity)

research_fit:
  best_for:
  - Research on China's distant water fishing fleet composition and the 2016-2020 fuel subsidy program's structure (thresholds, formula)
  - Rebuilding a vessel-registry panel from public inputs (RFMOs + Rongcheng open data) for marine/fishery policy studies
  choose_over:
  - Choose this registry/subsidy layer over GFW alone when vessel characteristics and subsidy eligibility matter; GFW supplies the fishing-effort outcome layer (china-fishing-vessel-detection).
  - Choose it over MARA aggregate yearbook counts when vessel-level variation is needed (the yearbook gives legal-authorization counts, e.g., 2,705 vessels).
  not_good_for:
  - Fishing-effort outcomes (use GFW - china-fishing-vessel-detection)
  - Vessels not in RFMO/Rongcheng sources (bilateral-access vessels are missing)
  - Claiming the paper's compiled panel is downloadable (not released)
  needs_join_for:
  - Fishing activity (GFW AIS-based) - see china-fishing-vessel-detection
  - Fish stock / overfishing simulations (Costello et al. 2016 data, paper-level)
  variation_available:
  - Vessel-level variation in subsidy amount at 25 engine-power thresholds (RD design; design details belong to Econ-Variation)
topics:
- distant water fishing
- fisheries subsidies
- vessel registry
- marine policy
- RFMO

good_for:
- Fleet composition and subsidy-structure research for Chinese distant water fishing
- Rebuilding the registry panel from public RFMO/Rongcheng inputs
- Understanding the 2016-2020 fuel subsidy formula and thresholds
identification: []
linkable_keys:
- Vessel registry name
- MMSI (SSVID in GFW)
- Call sign
- IMO
- Engine power (subsidy threshold variable)

joins:
- target: china-fishing-vessel-detection
  relation: complement
  keys:
  - Vessel registry name
  - MMSI (SSVID)
  - Call sign
  - IMO
  method: Match registry panel to GFW fishing hours with priority name+MMSI > name+call sign > name+IMO (paper); ~70% match rate
  evidence_status: literature-used

access_routes:
- route: WCPFC current Record of Fishing Vessels (one RFMO input)
  access_status: available
  direct_url: https://vessels.wcpfc.int/browse-rfv?page=0
  requirements:
  - No account was required for the checked public current-register export.
  - Preserve the retrieval date and query/filter state; current authorization fields are not a historical snapshot.
  steps:
  - Open the public WCPFC RFV browse page and set Flag = China if a China-only current view is wanted; an unfiltered export can instead be filtered locally on the Flag field.
  - Click CSV, wait for WCPFC's server-side export job to complete, then download the time-stamped CSV link shown by the completion message.
  - Save the retrieval date and query/filter state with the file; record the visible identity and authorization fields before entity matching.
  deliverable: A no-login, current WCPFC RFV CSV export for the selected public view. The unfiltered view displayed 3,033 records on 2026-09-28 and exported successfully; it includes the visible vessel-name, flag, registration-number, authorization-period, vessel-type, IRCS, WIN and VID fields. It is neither a complete seven-RFMO panel nor a historical WCPFC snapshot.
  cost: free
  last_checked: '2026-09-28'
  caveat: WCPFC is only one of the seven RFMO inputs. The checked route delivers a current public CSV, but does not establish a complete historical series, the paper's 2015-2020 version, cross-RFMO completeness, or rights to redistribute a compiled derivative.
- route: public-inputs-reconstruction
  access_status: available
  direct_url: needs-verification
  requirements: >-
    Seven RFMO vessel-registration databases named in the paper appendix
    (CCAMLR, IATTC, ICCAT, IOTC, NPFC, SPRFMO and WCPFC); Rongcheng distant water vessel dataset on the Shandong
    Provincial Open Data Platform (developed 2018; 318+104 vessels); MOA
    fuel subsidy policy documents (2016-2020 formula, 25 thresholds)
  steps:
  - Start from the seven registry routes named in Appendix B: CCAMLR authorised vessels (ccamlr.org/en/compliance/authorised-vessels-0), IATTC Vessel Register (iattc.org/VesselRegister/VesselList.aspx?Lang=en), ICCAT Record of Vessels (iccat.int/en/VesselsRecord.asp), IOTC authorised vessels (iotc.org/vessels), NPFC flagged-vessels register (npfc.int/compliance/vessels), SPRFMO vessel records (sprfmo.org/web/public/vessel), and WCPFC Record of Fishing Vessels (wcpfc.int/record-fishing-vessel-database).
  - Collect China-flagged vessel records from each accessible registry, preserving retrieval date and the registry's own identifiers before standardization.
  - Add the Rongcheng municipal dataset from the Shandong Open Data Platform (318 vessels + 104 not in RFMOs).
  - Standardize units (length to meters, engine power to kW), deduplicate to the vessel level (paper: 2,216 vessels).
  - Encode the subsidy formula and thresholds from the MOA 2016 policy (Subsidy = Standard x GearFactor x SubsidizedEnginePower x SubsidyDays).
  - Match to GFW fishing hours for outcomes (china-fishing-vessel-detection).
  deliverable: Rebuilt vessel-registry and subsidy panel; paper's exact cleaning rules are documented in the WP
  cost: free
  last_checked: '2026-08-15'
  caveat: >-
    The seven RFMO registry entry points are now pinned from the paper's
    Appendix B, but their live export formats, historical snapshots and
    present-day terms still require route-by-route checking. The Rongcheng
    dataset URL is an archived 2021 source and may require a replacement
    current open-data route.
- route: paper-panel
  access_status: unavailable
  direct_url: needs-verification
  requirements: Not released; no DAS or replication package found (WP has none; JEEM closed)
  steps:
  - No public route evidenced; the compiled panel must be rebuilt from the public inputs (route above).
  - Contact the authors (Englander, World Bank) only if a data-sharing agreement is being negotiated.
  deliverable: None - the compiled panel must be rebuilt
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Author contact possible (Englander, World Bank) but no release evidenced.

access:
  url: needs-verification
  cost: free
  license: Public registry/open-data inputs; compiled panel not released
  format:
  - web tables (RFMO registries)
  - open-data platform records
  api: false
  how_to_get: >-
    Rebuild from the seven RFMO vessel registries + Rongcheng open-data
    dataset per the WP's documented rules; subsidy formula and thresholds
    from MOA 2016 policy documents.
caveats:
- The compiled panel and code are not released; reconstruction follows the WP's documented cleaning.
- Coverage excludes distant water vessels authorized outside RFMO regions (bilateral EEZ access).
- GFW vessel characteristics are machine-learning-predicted and less reliable than RFMO data (paper); use RFMO characteristics.
- The 2016-2020 subsidy formula ended in 2021 (replaced by compliance awards) - do not apply the formula to later years.

production:
  raw_sources:
  - name: RFMO vessel registration databases (7 RFMOs)
    source_type: dataset
    role: China-flagged vessel records with characteristics and identifiers
    access_route: >-
      Appendix-B routes: CCAMLR, IATTC, ICCAT, IOTC, NPFC, SPRFMO and WCPFC
      public vessel registries; preserve each registry's retrieval date and
      export format.
    url: https://vessels.wcpfc.int/browse-rfv?page=0
    coverage: Vessels registered with RFMOs; characteristics vary by RFMO. WCPFC currently exposes a public current-register CSV with vessel name, flag, registration number, authorization period, vessel type, IRCS, WIN and VID; this is one current RFMO input, not a historic combined panel.
    last_checked: '2026-09-28'
  - name: Rongcheng distant water vessel dataset (Shandong Provincial Open Data Platform)
    source_type: dataset
    role: Additional vessel records (318 + 104 not in RFMOs); hub of Chinese distant water fisheries
    access_route: Shandong Provincial Open Data Platform (developed 2018; cited as Rongcheng Municipal Government 2021)
    url: needs-verification
    coverage: 318 vessels registered in Rongcheng (+104 additional)
    last_checked: '2026-08-15'
  - name: MOA fuel subsidy policy documents (2016-2020 formula)
    source_type: document
    role: Subsidy formula, gear factors, engine-power thresholds
    access_route: Ministry of Agriculture policy documents (2016); formula documented in WP
    url: needs-verification
    coverage: 2016-2020 (25 thresholds); 2021+ compliance-award regime
    last_checked: '2026-08-15'
  - name: GFW fishing hours (outcome layer)
    source_type: dataset
    role: Vessel-level hours of fishing (AIS-based, ML-predicted)
    access_route: https://globalfishingwatch.org/data-download/ (see china-fishing-vessel-detection)
    url: https://globalfishingwatch.org/data-download/
    coverage: China-flagged vessels 2015-2020
    last_checked: '2026-08-15'
  acquisition_methods:
  - direct download
  - manual coding
  sample_construction: >-
    Paper (WB WP 10412, read in full): combine RFMO registrations for
    mainland-China-flagged vessels with the Rongcheng dataset; treat same
    pinyin name + different Chinese characters/characteristics as different
    vessels; standardize units; deduplicate to 2,216 vessels; match ~70% to
    GFW on name/MMSI/call sign/IMO with the documented priority rule.
  pipeline_stages:
  - stage: collect
    inputs:
    - RFMO registries
    - Rongcheng dataset
    method: Record registry name and characteristics (gear, length, GT, engine power, build year) plus identifiers (previous name, MMSI, call sign, IMO); gather species/area/freezer/firm/RFMO membership from RFMO websites
    tools: []
    output: Vessel-RFMO records
    evidence: WB WP 10412 (Section on vessel data; Appendix B)
  - stage: clean
    inputs:
    - Vessel-RFMO records
    method: Standardize length (m) and engine power (kW); deduplicate vessels; combine RFMO + Rongcheng (adds 104 vessels)
    tools: []
    output: 2,216-vessel registry panel
    evidence: WB WP 10412
  - stage: match
    inputs:
    - Registry panel
    - GFW China-flagged fishing hours 2015-2020
    method: Match on name+MMSI, then name+call sign, then name+IMO; ignore GFW-predicted characteristics, keep RFMO ones
    tools: []
    output: Vessel-year panel with fishing hours (~70% matched)
    evidence: WB WP 10412 (Figure B1 matching flow)
  constructed_variables:
  - name: Vessel-level fuel subsidy
    concept: Subsidy received under the 2016-2020 formula
    source_fields:
    - Subsidy standard (year)
    - Gear factor (10 gears)
    - Subsidized engine power
    - Subsidy days
    method: Subsidy = Standard x GearFactor x SubsidizedEnginePower x SubsidyDays (paper Eq. 1)
    validation: 25 discontinuous thresholds; RD diagnostics in paper
    limitations: Formula applies 2016-2020 only
  validation:
  - Paper compares with Chinese Fisheries Statistical Yearbook legal-authorization counts (2,705 vs 2,216 collected).
  - RD validity checks (threshold-based assignment) in paper.
  output:
    unit_of_observation: Vessel (registry); vessel-year (analysis)
    structure: Vessel-level panel with subsidy schedule and matched fishing hours
    geography: Global distant water fleet of China (7 RFMOs + Rongcheng)
    time_span: 2015-2020 (GFW); 2016-2020 (subsidy analysis)
    key_variables:
    - Vessel characteristics and identifiers
    - Subsidy amount (formula-based)
    - Fishing hours (GFW)
    formats:
    - not released
  reproducibility:
    level: medium
    starting_point: RFMO registries + Rongcheng open-data platform (public); WP 10412 documents all rules
    code_available: false
    code_url:
    requirements:
    - Collection from 7 RFMO systems + Rongcheng open data
    - MOA 2016 subsidy policy documents for formula/thresholds
    - GFW access for outcomes (china-fishing-vessel-detection)
    blockers:
    - Paper panel/code not released
    - Registry pages are now identified, but their live export formats and historical snapshots are not yet verified
  compliance:
    terms_or_license: Public registries; GFW CC BY-NC 4.0 (non-commercial) per china-fishing-vessel-detection
    robots_or_rate_limits: Respect RFMO site terms; open-data platform terms unread
    personal_or_sensitive_data: Vessel records, not personal data
    redistribution: Compiled panel is paper's intellectual output; distribute only rebuilt versions with attribution
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Englander, Zhang, Villasenor-Derbez, Jiang, Hu, Deschenes & Costello (2025), Input subsidies and the depletion of natural capital: Chinese distant water fishing'
  doi: https://doi.org/10.1016/j.jeem.2025.103127
  journal: JEEM
  year: 2025
  dataset_role: >-
    Treatment and registry layer: vessel-level panel of the Chinese distant
    water fishing fleet (2,216 vessels from 7 RFMOs + Rongcheng) with
    characteristics and the 2016-2020 fuel-subsidy schedule (25 thresholds);
    outcomes from GFW fishing hours
  evidence_type: data-section
  evidence_url: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content
  data_note: >-
    World Bank Policy Research WP 10412 (full text read 2026-08-15) - same
    paper as JEEM 130 (2025) 103127 (Crossref: vol 130, article 103127,
    March 2025; closed access). Data construction: RFMO registries (7) +
    Rongcheng municipal dataset (Shandong Open Data Platform, 318+104
    vessels); dedup to 2,216 vessels; ~70% matched to GFW (name/MMSI/call
    sign/IMO, priority name+MMSI > name+call sign > name+IMO); subsidy
    formula Subsidy = Standard x GearFactor x SubsidizedEnginePower x
    SubsidyDays (2016-2020, 25 thresholds; 2021+ compliance awards).
    Results: 1% fuel-subsidy increase -> +2.2% fishing hours; vessels just
    above a threshold receive $10,000/month more and fish 170 more
    hours/month; distance elasticity 1.7%; total distant water fuel
    subsidies $520M (2018).

provenance:
- source: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content (WB PRWP 10412, read in full 2026-08-15)
  field_scope:
  - vessel data construction (RFMOs + Rongcheng), dedup count 2,216
  - subsidy formula, gear factors, thresholds, policy windows
  - GFW matching rule and ~70% match rate
  - results (elasticities, subsidy totals)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.crossref.org/works/10.1016/j.jeem.2025.103127 (read 2026-08-15)
  field_scope:
  - published identity: JEEM vol 130, article 103127, March 2025
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.openalex.org/works/https://doi.org/10.1016/j.jeem.2025.103127 (read 2026-08-15)
  field_scope:
  - author affiliations (Englander World Bank; Zhang OUC; Villasenor-Derbez U Miami; Jiang HKU; Hu Mayo; Deschenes/Costello UCSB)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: WCPFC Record of Fishing Vessels public browse page (https://vessels.wcpfc.int/browse-rfv?page=0, checked 2026-09-28)
  field_scope:
  - current public WCPFC RFV route
  - Flag = China filter availability
  - visible fields: vessel name, flag, registration number, authorization period, vessel type, IRCS, WIN and VID
  - visible CSV control, without a claim of successful complete/historical export
  added: '2026-09-28'
  confidence: high
  verified: true
- source: WCPFC Record of Fishing Vessels public CSV export workflow (https://vessels.wcpfc.int/browse-rfv, browser checked 2026-09-28)
  field_scope:
  - no-login server-side CSV export completion and generated download link
  - unfiltered current-view count of 3,033 records
  - boundary that the exported result is a current WCPFC snapshot, not a historical or seven-RFMO reconstruction
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: wcpfc-current-vessel-registry
  relation: component
- id: china-fishing-vessel-detection
  relation: complement
---

## Positioning in one sentence

The Chinese distant water fishing fleet layer behind Englander et al. (JEEM 2025) is a researcher-constructed 2,216-vessel registry/subsidy panel built from public inputs (seven RFMO registries + the Rongcheng open-data dataset + MOA 2016-2020 fuel-subsidy formula); it complements the GFW fishing-effort layer (china-fishing-vessel-detection) and is reconstructable from public sources per the fully documented World Bank WP 10412.

## Select rules

- Use this layer for fleet composition and fuel-subsidy-structure research; use GFW (china-fishing-vessel-detection) for fishing-effort outcomes.
- Rebuild from RFMO registries + Rongcheng open data per the WP's rules; do not promise the paper's compiled panel.
- Do not apply the 2016-2020 subsidy formula to 2021+ (compliance-award regime).

## Get recipe

1. Collect China-flagged vessel records from the seven RFMO registries (WP Appendix B) and the Rongcheng dataset (Shandong Open Data Platform).
2. Standardize units and deduplicate to the vessel level (paper: 2,216 vessels).
3. Encode the subsidy formula and 25 thresholds from MOA 2016 policy; match to GFW fishing hours (name/MMSI/call sign/IMO priority rule).

## Connections and Limitations

The registry layer joins to GFW fishing hours by vessel identifiers (~70% match). Coverage excludes vessels authorized outside RFMO regions (bilateral EEZ access). GFW-predicted vessel characteristics are less reliable than RFMO data. The paper panel/code are not released. The seven RFMO registry starting points are now recorded, while live export formats, historical snapshots and the current Rongcheng route still need verification.
