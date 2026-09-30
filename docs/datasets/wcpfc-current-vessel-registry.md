---
schema_version: 3
catalog_status: ready
id: wcpfc-current-vessel-registry
name: WCPFC Record of Fishing Vessels current public CSV export (China-filterable)
aka:
- WCPFC RFV
- WCPFC Record of Fishing Vessels
- WCPFC vessel registry CSV
provider: Western and Central Pacific Fisheries Commission (WCPFC), through its public Record of Fishing Vessels website.
china_related: true
domains:
- fisheries
- marine
- firm
- environment
- international trade

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    A current, point-in-time CSV export of WCPFC's public Record of Fishing
    Vessels. The researcher can retain all current records or filter the
    delivered Flag field to China. This is one regional-fishery-organization
    registry, not a historical China distant-water-fleet panel.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    On 2026-09-28, an unauthenticated browser session opened WCPFC's public
    RFV browse page, where the unfiltered view displayed 3,033 records. Its
    CSV control started a public server-side export job and, after completion,
    exposed a direct CSV download link. The visible register and the export
    route supply current vessel identity and authorization information,
    including China-flagged records. The generated file is time-stamped and
    should be treated as a dated snapshot rather than a stable historical
    product.
  barrier: >-
    The route closes current-file acquisition, not longitudinal history,
    cross-RFMO coverage, paper-specific cleaning, or a reuse licence beyond
    the provider's public site. Archive every acquired CSV and the exact
    filter state because the live register changes.

unit_of_observation: One current WCPFC vessel-register record (vessel identity and authorization record); China is a value of the Flag field, not a separate national registry.
structure: Current cross-sectional vessel-register snapshot; repeat downloads can form researcher-collected dated snapshots, but no provider historical panel was verified.
geo_granularity:
- vessel
- WCPFC convention-area registry
geography: WCPFC Record of Fishing Vessels, with a current China-flagged subset obtainable by filtering the public export; it does not represent all Chinese distant-water vessels worldwide.
time_span:
  start: unknown
  end: ongoing current register
  last_confirmed_release: Public current CSV export generated 2026-09-28
  coverage_note: >-
    The unfiltered public browse view showed 3,033 current records on
    2026-09-28. This is a live-register count, not a claim about a historical
    Chinese fleet universe, an annual sample, or the number of China-flagged
    vessels.
  last_checked: '2026-09-28'
frequency:
- current snapshot
sample_size: 3,033 records in the unfiltered public view observed on 2026-09-28; China-subset count is query- and retrieval-date-specific and was not inferred.
key_variables:
- Vessel name
- Flag
- Registration number
- Authorization period
- Vessel type
- IRCS
- WIN
- WCPFC vessel identifier (VID)

research_fit:
  best_for:
  - Building a dated current China-flagged WCPFC vessel-register extract with public vessel identifiers and authorization fields
  - Entity matching of current WCPFC vessels to another vessel-level source when identifiers and retrieval date are retained
  - A transparent starting input for a broader researcher-built fishing-fleet registry
  choose_over:
  - Choose this over manually transcribing a WCPFC results page when a reproducible current CSV snapshot is sufficient.
  - Choose china-distant-water-fishing-fleet when the question needs the JEEM paper's documented seven-RFMO plus Rongcheng reconstruction or its 2016-2020 subsidy layer; this file is only one of those inputs.
  - Choose china-fishing-vessel-detection when the research role is AIS-derived fishing effort rather than registry identity or authorization.
  not_good_for:
  - A complete Chinese distant-water-fleet census, including bilateral-EEZ vessels or vessels outside WCPFC coverage
  - Historical 2015-2020 vessel status without independently archived snapshots
  - Fishing location, catch, effort, ownership, engine power, subsidy eligibility, or a causal treatment measure
  - Assuming Chinese Taipei records are mainland-China records; retain the provider's Flag value.
  needs_join_for:
  - Other RFMO registries and the Rongcheng source for a wider China distant-water-fleet reconstruction
  - Global Fishing Watch or another separately authorised source for fishing activity
  - A documented vessel-identifier matching protocol when joining across registries or AIS data
  variation_available:
  - Cross-vessel differences in current register fields and authorization periods
  - Repeated researcher-retained snapshots may reveal changes, but change history is not provider-verified here
  topics:
  - fishing vessel registry
  - Chinese distant-water fishing
  - vessel identity matching
  - marine data

good_for:
- Public acquisition of a current WCPFC vessel-register CSV
- Identifying China-flagged WCPFC vessel records by the provider's Flag field
- Starting a documented, dated vessel-registry snapshot series
identification:
- >-
  Identify each extract by the WCPFC RFV browse URL, retrieval date, active
  filter state, and the provider-generated CSV filename. Do not identify a
  record as mainland Chinese merely from a vessel name; use the Flag field.
linkable_keys:
- WCPFC VID
- Vessel name
- Registration number
- IRCS
- WIN
- Flag

joins:
- target: china-distant-water-fishing-fleet
  relation: component
  keys:
  - Vessel name
  - IRCS
  - WIN
  - WCPFC VID
  - Flag
  method: >-
    Treat this CSV as one current WCPFC input. A wider Chinese fleet panel
    needs the paper-documented cross-RFMO standardisation and deduplication;
    do not append this snapshot to that panel without a dated entity-resolution
    protocol.
  evidence_status: literature-used
- target: china-fishing-vessel-detection
  relation: complement
  keys:
  - Vessel name
  - IRCS
  - WCPFC VID where crosswalked
  method: >-
    Match only after checking identifiers and date coverage. The WCPFC
    register provides identity/authorization information, while the other
    asset provides AIS-derived fishing activity.
  evidence_status: plausible

access_routes:
- route: WCPFC public RFV browser and generated CSV export
  access_status: available
  direct_url: https://vessels.wcpfc.int/browse-rfv
  requirements: No account was required for the observed public export; retain the provider's current terms and the retrieval state with any file.
  steps:
  - Open the RFV browse page and set any desired public filters, including Flag = China for a China-flagged view.
  - Click CSV and wait for the WCPFC server-side export job to finish.
  - Download the time-stamped CSV link shown in the completion message.
  - Store the file with its retrieval date, filter state and source URL; inspect the received columns before using it in a match.
  deliverable: A provider-generated, current-view CSV. The unfiltered route completed publicly on 2026-09-28.
  cost: free
  last_checked: '2026-09-28'
  caveat: The generated link is time-stamped and should be treated as a one-time current snapshot. No historical archive, stable API, China-subset count, or explicit data licence was verified in this task.

access:
  url: https://vessels.wcpfc.int/browse-rfv
  cost: free
  license: WCPFC public-site copyright is visible in the footer; no separate RFV CSV reuse licence was located in this bounded check. Preserve attribution and check current provider conditions before redistributing a derivative.
  format:
  - CSV
  - HTML table
  api: false
  how_to_get: Use the public browse page, set an optional filter, start its CSV export, wait for completion and download the generated link.
caveats:
- The export is a current WCPFC snapshot, not an annual or historical panel.
- The unfiltered 3,033-record count is a retrieval-date-specific interface count, not a China-fleet count.
- WCPFC coverage is geographically and institutionally narrower than a worldwide Chinese distant-water-fleet registry.
- The file does not establish vessel ownership, engine power, fishing activity, catch, subsidies or a paper's exact cleaned data.
- A public download does not by itself grant permission to redistribute a compiled dataset.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Englander, Zhang, Villasenor-Derbez, Jiang, Hu, Deschenes & Costello (2025), Input subsidies and the depletion of natural capital: Chinese distant water fishing'
  doi: https://doi.org/10.1016/j.jeem.2025.103127
  journal: Journal of Environmental Economics and Management
  year: 2025
  dataset_role: One of seven RFMO registry inputs to the authors' separately constructed Chinese distant-water-fleet registry
  evidence_type: data-section
  evidence_url: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content
  data_note: >-
    The open World Bank working-paper version documents seven RFMO registries
    as inputs to a 2,216-vessel reconstruction. It does not establish that
    this current WCPFC CSV has the same date, rows, fields or cleaning as the
    published paper's WCPFC input.

provenance:
- source: https://vessels.wcpfc.int/browse-rfv
  field_scope:
  - public RFV product identity
  - visible current fields, filters, pagination and CSV control
  - current public interface count of 3,033 unfiltered records
  added: '2026-09-28'
  confidence: high
  verified: true
- source: WCPFC RFV browser export completion page, generated from https://vessels.wcpfc.int/browse-rfv on 2026-09-28
  field_scope:
  - unauthenticated server-side export completion
  - generated time-stamped CSV download link
  - boundary that the delivered file is a current-view export
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://openknowledge.worldbank.org/server/api/core/bitstreams/b5100595-8420-4c58-bb03-354db2fda0bc/content
  field_scope:
  - WCPFC's role as one of seven RFMO inputs in the separate JEEM/WB reconstructed fleet panel
  - boundary against equating this current export with that paper's historical reconstruction
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

This is a genuinely downloadable current WCPFC vessel-register CSV, useful for a dated China-flagged subset or vessel matching; it is not the historical, seven-RFMO Chinese fishing-fleet panel assembled for the JEEM paper.

## Select rules

- Choose it for a documented current WCPFC snapshot or a China-flagged subset defined by the provider's `Flag` field.
- Switch to the reconstructed distant-water-fleet record when the question requires seven RFMO sources, Rongcheng additions, engine power or the 2016--2020 subsidy construction.
- Do not use it as fishing-effort data or a complete census of China's worldwide distant-water fleet.

## Get recipe

1. Open the public WCPFC browse page and set `Flag = China` if that is the intended subset.
2. Click CSV and wait for the server-side job to generate its download link.
3. Retain the downloaded file, exact filter, retrieval time and provider URL together.
4. Inspect fields and current terms before matching or sharing a derivative; compare identifiers rather than relying on vessel names alone.

## Connections and Limitations

The most useful connection is to vessel-activity data, but it requires an explicit crosswalk and date alignment. A current register cannot reconstruct a past fleet composition without archived snapshots, and WCPFC alone cannot cover Chinese vessels registered through the other RFMO or bilateral-access routes. The provider's `Flag` field is authoritative for this asset; do not collapse mainland China and Chinese Taipei records.
