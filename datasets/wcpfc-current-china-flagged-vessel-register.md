---
schema_version: 3
catalog_status: deprecated
id: wcpfc-current-china-flagged-vessel-register
superseded_by:
- wcpfc-current-vessel-registry
name: Deprecated duplicate of WCPFC current public vessel registry
aka: []
provider: Western and Central Pacific Fisheries Commission (WCPFC), Record of Fishing Vessels (RFV).
china_related: true
domains:
- marine
- fisheries
- firm
- spatial
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Superseded duplicate: a dated CSV export of WCPFC's current public RFV, filtered locally on its
    displayed Flag field for China. It is one live registry input for Chinese
    distant-water-fleet research, not the seven-RFMO historical panel or the
    paper-constructed 2015--2020 fleet dataset.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    This duplicate is retained solely as an audit trail. WCPFC's public RFV browse interface required no account in the checked
    route. Its unfiltered current view displayed 3,033 records on 2026-09-28
    and completed a server-side CSV export. The resulting current file exposes
    vessel name, flag, registration number, authorization period, vessel type,
    IRCS, WIN and VID; filtering its Flag field yields a reproducible current
    China-flagged extract when the retrieval date and filter are retained.
  barrier: >-
    This is a current, single-RFMO register. It does not establish historical
    snapshots, vessels outside WCPFC, a complete China fleet, activity, owner
    identity, subsidy receipt, or permission to redistribute a compiled panel.

unit_of_observation: One current WCPFC RFV vessel-registration record.
structure: Dated current register cross-section; filterable by flag.
geo_granularity:
- vessel
- WCPFC convention area / authorization record
geography: WCPFC public register; China-related subset is records whose displayed Flag field is China. This is not a national fleet universe.
time_span:
  start: null
  end: ongoing current register
  last_confirmed_release: Unfiltered public view displayed 3,033 records and exported on 2026-09-28.
  coverage_note: A retrieval is a dated current snapshot. The public check did not establish archival depth, past authorizations, or a stable China-record count.
  last_checked: '2026-09-28'
frequency:
- current register snapshot
sample_size: 3,033 records in the observed unfiltered public view; China-filtered count must be calculated from each dated export.
key_variables:
- Vessel name
- Flag
- Registration number
- Authorization period
- Vessel type
- IRCS
- WIN
- VID

research_fit:
  best_for:
  - Current China-flagged WCPFC vessel-register snapshots and vessel-identifier matching
  - A documented public starting layer for a bounded Chinese distant-water-fleet collection
  choose_over:
  - Choose this over the broader china-distant-water-fishing-fleet record when the task needs an obtainable present WCPFC register rather than the paper's 2015--2020 seven-RFMO reconstruction.
  - Use china-fishing-vessel-detection for AIS-derived fishing activity; this register supplies identity and authorization fields, not effort.
  not_good_for:
  - Historical fleet panels, complete Chinese distant-water-fleet counts, subsidy outcomes, fishing effort, or firm ownership analysis
  - Treating absence from WCPFC as evidence a vessel is not part of China's fleet
  needs_join_for:
  - Other RFMO registers and the Rongcheng dataset for a wider fleet reconstruction
  - GFW/AIS data for fishing activity, using identifiers with documented entity resolution
  variation_available:
  - Cross-sectional differences among currently registered vessels; changes across separately retained snapshots only after matching records and checking register revisions
  topics:
  - fishing vessels
  - distant-water fleet
  - vessel registry
  - China-flagged vessels

good_for:
- Current China-flagged vessel identity and authorization records within WCPFC
identification:
- Preserve vessel name together with registration number, IRCS, WIN and VID where present; do not rely on a name alone for longitudinal matching.
linkable_keys:
- Vessel name
- Registration number
- IRCS
- WIN
- VID

joins:
- target: china-distant-water-fishing-fleet
  relation: component
  keys:
  - vessel name
  - registration number
  - IRCS
  - WIN
  - VID
  method: This is the checked current WCPFC input layer. The broader record requires six additional RFMO sources, Rongcheng records and documented deduplication before it becomes the paper-like fleet panel.
  evidence_status: verified
- target: china-fishing-vessel-detection
  relation: complement
  keys:
  - vessel name
  - MMSI/SSVID where separately resolved
  method: Match only after recording identifier provenance and resolving aliases; the present WCPFC export does not itself prove an AIS match.
  evidence_status: plausible

access_routes:
- route: WCPFC RFV public browse-and-export
  access_status: available
  direct_url: https://vessels.wcpfc.int/browse-rfv?page=0
  requirements: A normal browser; no account was required for the observed current export.
  steps:
  - Open the public RFV browse page and retain the retrieval date.
  - Export the current CSV through the page's server-side CSV action and wait for its completion link.
  - Filter the exported Flag field for China, retaining the exact filter and unmodified source file.
  - Inspect authorization periods and identifiers before any cross-source match; stop if a historical, whole-fleet, activity or redistribution claim is required.
  deliverable: A dated current CSV register, locally filterable to China-flagged records.
  cost: free
  last_checked: '2026-09-28'
  caveat: The route was verified on an unfiltered view. The current China subset must be created and counted from the dated export; it is not a provider-certified national fleet file.

access:
  url: https://vessels.wcpfc.int/browse-rfv?page=0
  cost: free
  license: Provider terms for downstream reuse were not separately read; preserve attribution and do not assume redistribution permission for a compiled derivative.
  format:
  - CSV export
  api: false
  how_to_get: Export the dated public RFV CSV in a browser, then filter the displayed Flag field for China while retaining retrieval and filter metadata.
caveats:
- The observed 3,033 count belongs to the unfiltered current view, not to China.
- This register is a single RFMO input and cannot reproduce the 2,216-vessel historical seven-RFMO-plus-Rongcheng panel in the associated JEEM study.
- A current registration or authorization field is not observed fishing activity, subsidy receipt, ownership, or a historical status.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'
used_by: []
provenance:
- source: WCPFC Record of Fishing Vessels public browse page (https://vessels.wcpfc.int/browse-rfv?page=0, browser read 2026-09-28)
  field_scope:
  - Public no-login browse-and-export route
  - Unfiltered current display count of 3,033 records
  - Successful current CSV export and visible vessel-name, flag, registration-number, authorization-period, vessel-type, IRCS, WIN and VID fields
  - Boundary against historical, seven-RFMO, China-universe and redistribution claims
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-distant-water-fishing-fleet
  relation: component
- id: china-fishing-vessel-detection
  relation: complement
---

## Positioning in one sentence

This is a deprecated duplicate of `wcpfc-current-vessel-registry`. Use that canonical record for the genuinely obtainable current WCPFC registry snapshot and its China-flagged filter.

## Select rules

- Do not choose this deprecated duplicate; use `wcpfc-current-vessel-registry`.
- Choose the broader seven-RFMO reconstruction only when its additional inputs and historical matching work are actually required.
- Do not use it for fleet activity, complete national coverage, a historical panel, or subsidy measurement.

## Get recipe

1. Export the public current RFV CSV in a browser and preserve the retrieval date.
2. Filter the `Flag` field for China and retain both the original export and the exact filtering step.
3. Use the supplied identifiers for cautious matching, and obtain another source if history, activity, ownership or whole-fleet coverage matters.

## Connections and Limitations

The China-filtered extract is a current slice of one RFMO register. Its value is that it gives an ordinary researcher a real start point without pretending that the paper's seven-RFMO-plus-Rongcheng panel is downloadable. A vessel missing from this file may still be elsewhere in the Chinese distant-water fleet.

## Decision sufficiency check

The identity and route were independently valid but already represented by `wcpfc-current-vessel-registry`; keeping both as active records would split one decision across two names. This deprecated file is retained without deleting history, and future routing must use the existing canonical record.
