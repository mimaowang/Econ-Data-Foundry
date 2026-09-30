---
schema_version: 3
catalog_status: ready
id: cnemc-current-national-surface-water-quality-dashboard
name: CNEMC public current national surface-water quality dashboard (全国水质自动监测展示)
aka:
- 全国水质自动监测
- CNEMC current water-quality dashboard
- 中国环境监测总站断面水质实时展示
provider: China National Environmental Monitoring Centre (CNEMC, 中国环境监测总站)
china_related: true
domains:
- environment
- water
- urban
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The browser-visible current national water-monitoring list on CNEMC's
    public homepage: a timestamped set of displayed monitoring-section names
    and water-quality classes. A researcher may manually preserve this bounded
    display; it is not the underlying national historical monitoring panel.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CNEMC's homepage visibly labelled this layer 全国水质自动监测 and displayed
    a list headed 监测断面、测量时间、水质类别. On 2026-09-28 it showed 1,178
    list entries, with a visible 2026-09-28 12:00 timestamp for the observed
    rows and water-quality classes such as Ⅰ--Ⅴ and 劣Ⅴ. This supports a
    traceable current snapshot recorded from the public page. It does not
    establish concentration fields, coordinates, a complete or stable station
    roster, historical look-back, download, API or reuse permission.
  barrier: >-
    The public screen exposes only its current list and class label. It cannot
    reproduce the section/station history used by research papers, establish a
    balanced panel, or support bulk collection merely because the display is
    publicly visible.

unit_of_observation: One displayed monitoring-section row at the page's shown measurement time, with section name and water-quality class.
structure: Timestamped browser-visible current-section cross-section; retain each captured page time separately.
geo_granularity:
- monitoring section
geography: National public CNEMC display; the observed list includes river, lake and reservoir-related section names, but no fixed geographic universe or coordinates are established.
time_span:
  start: '2026-09-28'
  end: ongoing current display
  last_confirmed_release: 1,178 displayed rows at 2026-09-28 12:00
  coverage_note: >-
    This proves one current display only. It does not prove complete same-day
    coverage, a historical archive, continuous measurement, a first available
    date, or that 1,178 is a fixed network count.
  last_checked: '2026-09-28'
frequency:
- current timestamped display
sample_size: 1,178 displayed rows on the observed 2026-09-28 page; not a claimed network universe.
key_variables:
- Monitoring-section name as displayed
- Displayed measurement time
- Water-quality class (Ⅰ--Ⅴ, 劣Ⅴ, or displayed missing marker)

research_fit:
  best_for:
  - A documented snapshot of the water-quality class CNEMC visibly showed for named sections at a specific time
  - Small descriptive work that retains its page time and accepts the displayed-name-only geographic boundary
  choose_over:
  - Choose this record when the empirical object is the current public display itself.
  - Choose china-mee-surface-water-quality-bulletins for official aggregate monthly, quarterly or annual publication summaries.
  - Use china-water-quality-monitoring only after establishing a suitable historical section/station route for research-panel work.
  not_good_for:
  - Historical section or station panels, concentration analysis, pollution exposure construction, or a balanced network
  - Geocoding from this page alone, since it supplies no coordinates or administrative location fields
  - Automated bulk extraction, redistribution, or inference that omitted entries have a particular water-quality class
  needs_join_for:
  - An independently verified section-location crosswalk before linking a snapshot to locations or outcomes
  - A separately verified historical route for repeated-time empirical analysis
  variation_available:
  - Cross-section differences among classes shown at one documented time
  - Differences across separately preserved snapshots, conditional on the unverified roster and historical-availability boundary
  topics:
  - surface-water quality
  - environmental monitoring
  - descriptive local environmental conditions

good_for:
- Manually preserved, time-stamped observations from CNEMC's public water-quality display
identification:
- >-
  Identify each observation by page URL, display type, section name, shown
  measurement time, water-quality class and retrieval time. Do not infer a
  pollutant concentration, basin, city or section code from the name alone.
linkable_keys:
- Displayed monitoring-section name
- Displayed measurement time

joins:
- target: china-water-quality-monitoring
  relation: component
  keys:
  - monitoring-section name
  - time
  method: >-
    This is a visible public slice of the broader monitoring family. It does
    not provide access to that family's historical readings, section roster or
    paper-specific products.
  evidence_status: verified
- target: china-mee-surface-water-quality-bulletins
  relation: complement
  keys:
  - reporting time
  method: >-
    A current section-class display and an aggregate MEE bulletin are different
    products with different units; neither substitutes for the other.
  evidence_status: plausible

access_routes:
- route: CNEMC public homepage water-monitoring display
  access_status: available
  direct_url: https://www.cnemc.cn/
  requirements: A normal browser; no account was required for the observed list.
  steps:
  - Open CNEMC's homepage and locate 全国水质自动监测.
  - Confirm the displayed header and the page's measurement time before recording rows.
  - Preserve the section name, displayed time, water-quality class, page URL and retrieval time.
  - Stop at the visible snapshot boundary; establish another documented route if location, concentration, history or bulk access is required.
  deliverable: Manually recordable current monitoring-section names, timestamps and water-quality classes.
  cost: free
  last_checked: '2026-09-28'
  caveat: The observed page establishes a current display only, not a download, API, historical archive, fixed roster or reuse right.

access:
  url: https://www.cnemc.cn/
  cost: free
  license: Provider terms were not separately read; do not assume permission for bulk reuse or redistribution.
  format:
  - browser-visible section list
  api: false
  how_to_get: Manually preserve the visible rows with their page-supplied time and water-quality class, keeping retrieval metadata.
caveats:
- A water-quality class is not a concentration value and the public row does not expose the underlying indicators.
- Section names are not safe geographic identifiers without a separately verified crosswalk.
- The observed 1,178 rows are a dated display count, not a claim about the full national network.
- The public current display cannot reproduce a paper's historical section/station panel or demonstrate bulk-use permission.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'
used_by: []
provenance:
- source: Rendered CNEMC homepage https://www.cnemc.cn/ (browser read 2026-09-28)
  field_scope:
  - public layer label 全国水质自动监测 and its link to the national water-monitoring page
  - table header 监测断面、测量时间、水质类别
  - 1,178 observed list entries, including named rows at 2026-09-28 12:00 with classes Ⅰ--Ⅴ, 劣Ⅴ or a displayed missing marker
  - boundary against concentration, coordinate, roster, archive, download, API and reuse claims
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-water-quality-monitoring
  relation: component
- id: china-mee-surface-water-quality-bulletins
  relation: complement
---

## Positioning in one sentence

This is CNEMC's genuinely accessible public current water-quality display: a dated list of named monitoring sections and water-quality classes, not a hidden release of the historical monitoring data used in empirical research.

## Select rules

- Choose it only when a documented current snapshot of displayed section classes is the desired object.
- Choose official aggregate bulletins for report-level water-quality summaries.
- Do not choose it for historic exposure construction, concentrations, geocoded analysis, a balanced panel or paper replication.

## Get recipe

1. Open the CNEMC homepage and locate 全国水质自动监测.
2. Verify the visible headers and measurement time.
3. Preserve the displayed section name and class alongside the page URL and retrieval time.
4. Use a separately verified route for any history, coordinates, concentrations or bulk analysis.

## Connections and limitations

The natural key is the displayed section name plus the shown time, but the name alone is not a geographic code. The essential limitation is that the page shows a current public snapshot; it does not reveal the historical research dataset that a future agent might otherwise mistakenly assume is available.
