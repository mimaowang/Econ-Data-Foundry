---
schema_version: 3
catalog_status: ready
id: china-coal-power-plant-panel
name: Global Energy Monitor China coal-fired-unit status summary (GCPT)
aka:
- GCPT
- Global Coal Plant Tracker
- 全球燃煤电厂追踪
- Coal Plants in China (Units)
provider: >-
  Global Energy Monitor (GEM), a US-based non-profit (440 N Barranca Ave,
  Covina, CA 91723, per site footer 2026-08-15). GCPT project manager /
  contacts: Christine Shearer (Interim Director, Coal), Lucy Hummer (Interim
  Project Manager) per the official tracker page (fetched 2026-08-15).
china_related: true
domains:
- energy
- environment
- industrial
- regional

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The directly verified China-specific GCPT workbook, "Coal-fired Power
    Units in China.xlsx": a province/region-by-status summary of unit counts
    for Announced, Pre-permit, Permitted, Construction, Shelved, Cancelled,
    Operating, Mothballed, and Retired units. It is not an individual-unit
    roster.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Direct workbook inspection (2026-09-28) closes the public China route:
    GEM's July 2026 file has one sheet, titled "Coal-fired Power Units in
    China," and its usable table gives each province/region counts by unit
    status (for example, Announced through Retired). The broader GCPT project
    describes a unit-level tracker maintained twice yearly and licensed CC
    BY 4.0, but this China-specific export contains no individual plant/unit
    identifiers, owners, coordinates, capacity, or unit dates. It is therefore
    a ready-made province-status summary, not the plant roster previously
    implied by this record.
  barrier: >-
    The two JEEM anchor papers' plant rosters remain unverified. More
    fundamentally, the checked China-specific export is only a provincial
    status-count summary, so it cannot supply a plant-level exposure or
    closure panel. A separately verified global or China-level individual-unit
    download would be required before recommending GCPT for such work.

unit_of_observation: Province/region x coal-unit status category, with the value equal to the number of units in that status
structure: cross-sectional status-count table, release-vintage specific
geo_granularity:
- Chinese province/region
geography: China, summarized by province/region in the July 2026 China Units workbook
time_span:
  start: '2026'
  end: '2026'
  last_confirmed_release: 'July 2026 China Units workbook (read 2026-09-28)'
  coverage_note: >-
    This directly checked file is a July 2026 snapshot, not a 2000-2026
    panel. Its status labels count cancelled units since 2010 and retired
    units since 2000, but those label cutoffs do not provide dated historical
    observations. The two JEEM anchor papers cover closures 2004-2014 (JEEM
    2026.103302, abstract-level) and coal-regulated plants (JEEM 2025.103205,
    title-level); overlap with this product remains unverified.
  last_checked: '2026-09-28'
frequency:
- bi-annual database update (January and July)
sample_size: >-
  One row per Chinese province/region in the July 2026 workbook, with ten
  reported status-count columns; the provider's broader global unit count is
  not the row count or unit-level content of this China export.
key_variables:
- Province/Region
- Counts of units by status: Announced, Pre-permit, Permitted, Construction, Shelved, Cancelled (since 2010), Operating, Mothballed, and Retired (since 2000)
- Combined Announced + Pre-permit + Permitted count

research_fit:
  best_for:
  - Province-level descriptive comparison of Chinese coal-unit status counts in a documented GCPT release
  - A transparent aggregate cross-check when a research design only needs counts of operating, retired, or in-development units by province
  choose_over:
  - Choose this workbook over an unversioned web statistic when province-level unit-status counts suffice and a versioned, open-licensed source is needed.
  - Choose a separately verified plant-unit source over this workbook whenever plant identity, location, capacity, ownership, or closure date matters.
  not_good_for:
  - Plant-level exposure, closure, ownership, capacity, generation, utilization, or emissions analysis.
  - Claiming that either JEEM anchor used GCPT (paper data sections unread - identity unverified).
  - A time-series inference from one workbook vintage; the file is a release snapshot.
  needs_join_for:
  - Province-year outcome data, if comparing aggregate status counts with regional outcomes
  - A separately obtained plant-level roster for any spatial or ownership match
  variation_available:
  - Cross-province differences in counts by operating status within the downloaded release
  topics:
  - coal power
  - energy transition
  - power plants
  - industrial exposure

good_for:
- Provincial coal-unit-status descriptives
- Release-vintage comparisons after independently retaining later GCPT exports
identification:
- >-
  The workbook is an aggregate descriptive input. It contains no assignment,
  treatment, or unit-level event date from which to infer causal exposure.
linkable_keys:
- Province/Region
- GCPT release vintage
- Status category

joins:
- target: china-city-co2-emissions
  relation: complement
  keys:
  - Province/region
  - Release vintage
  method: Compare only at an aggregate province level; this workbook cannot be geocoded to prefectures or plants.
  evidence_status: plausible

access_routes:
- route: official-download
  access_status: available
  direct_url: https://globalenergymonitor.org/projects/global-coal-plant-tracker/
  requirements: No account; direct Google Sheets links on the official page
  steps:
  - Open the official tracker page and go to the "Download data" section.
  - Pick the needed table (e.g., "Coal Plants in China (Units)") and open its Google Sheets link.
  - Export the China Units table as XLSX and keep the release vintage (bi-annual).
  - Read the workbook before modelling: the checked July 2026 China file is a province/status-count table, not a list of units.
  - Cite as "Global Coal Plant Tracker, Global Energy Monitor, <release> release."
  deliverable: >-
    The checked China-specific XLSX is one province/region-by-status count
    table. It reports status categories and counts, not individual plants or
    units; CC BY 4.0 licensed (official license page).
  cost: free
  last_checked: '2026-08-15'
  caveat: >-
    On 2026-09-28, the China Units XLSX export returned HTTP 200 and was read:
    it has a single sheet with province/region rows and status-count columns.
    The /projects/global-coal-plant-tracker/download-data/ URL redirects to
    the main tracker page; use the page's own "Download data" section links.

access:
  url: https://globalenergymonitor.org/projects/global-coal-plant-tracker/
  cost: free
  license: >-
    Creative Commons Attribution 4.0 International (official GEM license
    page globalenergymonitor.org/creative-commons-license, read 2026-08-15);
    attribution required
  format:
  - xlsx
  api: false
  how_to_get: >-
    Open the official tracker page, scroll to "Download data", open the
    China Units Google Sheets link, and export the province/status summary
    workbook as XLSX.
caveats: >-
  The checked China Units file is an aggregate status-count table, not a
  status/capacity plant tracker: it has no names, coordinates, owners,
  capacity, or event dates. Paper identity to GCPT is unverified for both
  JEEM anchors. A different GCPT/global file may have another structure, but
  that is not established by this record and must be inspected separately.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: partial
  last_audited: '2026-09-28'

used_by:
- cite: 'Fan, Gao & Tang (2026), mass coal-plant closures 2004-2014 with geographic/operational information from more than 1500 power plants and monthly satellite SO2'
  doi: https://doi.org/10.1016/j.jeem.2026.103302
  journal: JEEM
  year: 2026
  dataset_role: Plant-level operational/closure information (explanatory/control layer; provider unverified)
  evidence_type: abstract-only
  evidence_url: https://doi.org/10.1016/j.jeem.2026.103302
  data_note: >-
    Abstract read (Layer-2b sweep): geographic and operational information
    from more than 1,500 power plants plus monthly satellite SO2. The
    abstract does not name the plant roster provider; GEM GCPT is a
    plausible family but identity is UNVERIFIED (data section unread).
- cite: 'Jia, Ma, Wang & Xie (2025), intra-firm pollution leakage, coal-regulated plants'
  doi: https://doi.org/10.1016/j.jeem.2025.103205
  journal: JEEM
  year: 2025
  dataset_role: Coal-regulated plant identification (provider unverified)
  evidence_type: abstract-only
  evidence_url: https://doi.org/10.1016/j.jeem.2025.103205
  data_note: >-
    Title-level anchor (abstract channels empty at Layer-2b sweep); no
    provider identity established.

provenance:
- source: https://globalenergymonitor.org/projects/global-coal-plant-tracker/ (read in full 2026-08-15)
  field_scope:
  - product identity
  - coverage (30+ MW, 2000-present)
  - unit counts
  - status categories
  - update frequency
  - download links (Google Sheets incl. China tables)
  - recommended citation
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://globalenergymonitor.org/creative-commons-license (read 2026-08-15)
  field_scope:
  - license (CC BY 4.0)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://globalenergymonitor.org/projects/global-coal-plant-tracker/ (re-read 2026-09-28); China Units XLSX export endpoint https://docs.google.com/spreadsheets/d/1yESp-dY3hHJpgZ5HS-9V8x70eiY0oDqLFJYup0AwkbY/export?format=xlsx (HTTP HEAD checked 2026-09-28)
  field_scope:
  - current July 2026 release and China-specific table identity
  - current China Units XLSX delivery route
  - delivered XLSX media type, filename, sheet title, and province/status-count columns
  added: '2026-09-28'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-coal-power-plant-panel, Layer-2b sweep)
  field_scope:
  - paper anchors (abstract-level)
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-city-co2-emissions
  relation: complement
---

## Positioning in one sentence

The directly verified China GCPT download is a free, CC BY 4.0-licensed, release-specific province-by-status count table—not a Chinese coal-plant or unit roster.

## Select rules

- Use this export when the question is about provincial counts of coal-unit statuses in a fixed GCPT release.
- Find and inspect a distinct plant-level source before any plant closure, ownership, capacity, or spatial analysis; do not assume this China file contains it.
- Do not use it for generation, utilization, emissions, or unit-level event-time analysis.

## Get recipe

1. Open the official tracker page and scroll to "Download data".
2. Open the "Coal Plants in China (Units)" Google Sheets link (ID 1yESp-dY3hHJpgZ5HS-9V8x70eiY0oDqLFJYup0AwkbY in the page HTML) and export the XLSX. The route was live at the 2026-09-28 check and returned "Coal-fired Power Units in China.xlsx."
3. Use row 8 as the column header and preserve the release vintage (July 2026 at last check). The rows are provinces/regions; the values are counts by status.
4. For a plant-level question, stop here and find another independently inspected source.

## Connections and Limitations

- The Chinese export contains status counts only; it cannot support a plant-to-place join or recover a unit's capacity, owner, coordinates, or closure date.
- The status labels themselves include Cancelled since 2010 and Retired since 2000. They are counts in a July 2026 snapshot, not a release of historical plant-level event data.
- Paper-to-product identity is still open: the JEEM 2026.103302 and JEEM 2025.103205 data sections may use GCPT, NEA lists, or another roster.
