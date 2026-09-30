---
schema_version: 3
catalog_status: ready
id: china-mee-surface-water-quality-bulletins
name: MEE National Surface-Water Quality Bulletins (全国地表水质量状况 and 地表水水质月报)
aka:
- 全国地表水质量状况
- 地表水水质月报
- MEE surface-water quality bulletins
- national surface-water quality releases
provider: Ministry of Ecology and Environment (生态环境部, MEE), with monitoring information from the China National Environmental Monitoring Centre network
china_related: true
domains:
- environment
- water quality
- public
- urban

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Dated official MEE monthly, quarterly and annual publication pages or bulletins reporting national/basin aggregate surface-water quality conditions; not a station- or section-level historical concentration panel.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    MEE's water-environment-quality column and its 全国地表水质量状况 and 地表水水质月报
    subcolumns were live and publicly reachable on 2026-09-28. The 2026 Q2 release page
    also returned 200. The verified product is a dated bulletin: it reports aggregate
    quality-class shares, main exceeding indicators, basin or key-lake summaries and
    report-specific network coverage, rather than a downloadable record for each section.
  barrier: >-
    The bulletin series does not establish a complete machine-readable section/station
    concentration archive, an API, or a stable historical network roster.

unit_of_observation: One dated monthly, quarterly or annual official bulletin; values are publication-level national, basin or report-specific aggregate summaries.
structure: Recurring official HTML/PDF-style bulletin and press-release series
geo_granularity:
- national aggregate
- river basin or water-system aggregate
- key lake or reservoir aggregate
geography: China; the covered network, basins and lakes are stated in each release and change by report/vintage.
time_span:
  start: unknown
  end: ongoing
  last_confirmed_release: 2026 Q2 and January-June national surface-water quality release, 2026-07-30
  coverage_note: MEE pages verify current monthly and quarterly/annual publication channels. The 2026 Q2 page reports 145 key lakes/reservoirs; it does not prove a complete historical archive or an unchanged network.
  last_checked: '2026-09-28'
frequency:
- monthly
- quarterly
- annual
sample_size: Report-specific. The 2026 Q2 release includes 145 key lakes/reservoirs; 2025 annual reporting refers to 3,641 national assessment sections, but aggregate bulletin values are not a section-level dataset.
key_variables:
- Share of national assessment sections in quality classes I-III and inferior to V
- Main exceeding indicators, such as COD, permanganate index and total phosphorus where reported
- Basin or water-system quality summaries
- Key lake/reservoir quality and trophic-status summaries where reported

research_fit:
  best_for:
  - Official current or recent national/basin surface-water quality conditions when aggregate bulletin evidence is sufficient
  - Descriptive environmental reporting and documented policy context using the report's own stated coverage
  choose_over:
  - Choose these MEE bulletins over secondary media summaries when a dated official source and stated aggregate definition are required.
  - Choose china-water-quality-monitoring only after separately verifying a section/station data route for high-granularity exposure or panel research.
  not_good_for:
  - Section-level or station-level concentration panels
  - A complete city-year or city-month water-quality panel inferred from national shares
  - Firm discharge measurement, which belongs to firm-pollution data rather than ambient water bulletins
  needs_join_for:
  - A separately documented geographic/concentration dataset for local exposure analysis
  - Report-month and basin definitions when combining bulletins with macro or policy context
  variation_available:
  - Published aggregate changes across report periods and the report's stated water systems or lakes
  topics:
  - surface-water quality
  - environmental reporting
  - river basins
  - water governance

good_for:
- Official aggregate surface-water-quality bulletin acquisition
- National and basin-level environmental-condition context
identification:
- >-
  Identify the product by the MEE 水环境质量 column and either the 全国地表水质量状况
  or 地表水水质月报 subcolumn, retaining the exact dated release title and URL.
- >-
  This is a bulletin/publication series. It is distinct from the underlying MEE/CNEMC
  monitoring readings recorded in china-water-quality-monitoring and must not be
  treated as a hidden section-level historical data download.
linkable_keys:
- Bulletin period
- River basin or water-system label where reported
- Report-specific indicator

joins:
- target: china-water-quality-monitoring
  relation: often-confused-with
  keys:
  - period
  - basin or geography where applicable
  method: Use this record only for published aggregate conditions; verify a distinct route before linking micro outcomes to section/station readings.
  evidence_status: verified
- target: china-firm-pollution
  relation: often-confused-with
  keys:
  - year
  - geography
  method: Ambient surface-water aggregate bulletins and firm discharges are different measurement layers.
  evidence_status: verified

access_routes:
- route: MEE water-environment-quality bulletin columns
  access_status: available
  direct_url: https://www.mee.gov.cn/hjzl/shj/
  requirements: None for the checked public pages.
  steps:
  - Open MEE's 水环境质量 column.
  - Select 全国地表水质量状况 for quarterly/annual releases or 地表水水质月报 for monthly bulletins.
  - Retain the release title, period, publication date, URL, stated network/geographic scope and table notes with any extracted value.
  deliverable: Free official monthly, quarterly and annual aggregate surface-water-quality bulletins.
  cost: free
  last_checked: '2026-09-28'
  caveat: Current column accessibility does not establish a complete historical archive or section-level raw-data delivery.

access:
  url: https://www.mee.gov.cn/hjzl/shj/
  cost: free
  license: Government disclosure information; retain attribution and respect release-specific conditions.
  format:
  - HTML bulletin page
  - linked report material where supplied
  api: false
  how_to_get: Use the MEE water-quality column, choose the relevant monthly or quarterly/annual subcolumn, open a dated release and preserve its stated coverage before extracting aggregate values.
caveats: >-
  Bulletins report aggregate class shares and summary conditions. They do not provide a
  complete public station/section concentration panel, a bulk API, a stable geographic
  roster or evidence of the exact water-quality product used by a particular paper.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://www.mee.gov.cn/hjzl/shj/ (live page read 2026-09-28)
  field_scope:
  - MEE water-environment-quality publication column
  - current public publication route
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/hjzl/shj/qgdbszlzk/ and https://www.mee.gov.cn/hjzl/shj/dbsszyb/ (live subcolumns read 2026-09-28)
  field_scope:
  - quarterly/annual and monthly bulletin-series identities
  - public access routes
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/ywdt/xwfb/202607/t20260730_1163186.shtml (2026 Q2 release read 2026-09-28)
  field_scope:
  - current dated official release
  - report-level aggregate scope and key-lake summary
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-water-quality-monitoring
  relation: complement
- id: china-firm-pollution
  relation: often-confused-with

---

## Positioning in one sentence

This is MEE's public bulletin series for national and basin-level surface-water conditions: it is directly obtainable and useful for aggregate context, but is not a section-level monitoring panel.

## Select rules

- Choose it when official report-level water-quality conditions are sufficient.
- Switch to a separately verified monitoring dataset when local concentrations or a longitudinal section/station panel are required.
- Preserve the exact report period, network scope and definition with every extracted value.

## Get recipe

1. Open the MEE water-quality column and the appropriate monthly or quarterly/annual subcolumn.
2. Retrieve a dated release and record its metadata.
3. Extract only the report's stated aggregate measures.

## Connections and Limitations

The record can provide environmental context by period or basin but cannot validly stand in for local exposure measurements. Network counts and coverage are report/vintage-dependent.
