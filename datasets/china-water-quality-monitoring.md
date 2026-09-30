---
schema_version: 3
catalog_status: grounding
id: china-water-quality-monitoring
name: China National Surface-Water Quality Monitoring Data (MEE 国控断面 network)
aka:
- 国家地表水水质监测数据
- 国控断面水质
- 全国地表水水质
- 地表水水质自动监测
- China surface water quality monitoring
provider: >-
  Ministry of Ecology and Environment (MEE, 生态环境部) and China National
  Environmental Monitoring Centre (CNEMC, 中国环境监测总站). The national
  surface-water quality monitoring network (国家地表水环境质量监测网) consists of
  national assessment sections (国控断面, 3641 in the "14th Five-Year Plan"
  period per the MEE 2025 annual release) plus automatic monitoring stations
  under CNEMC operation.
china_related: true
domains:
- environment
- water
- public
- urban
- health

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The underlying national surface-water monitoring-reading family: national
    assessment sections (国控断面) and automatic monitoring stations whose
    observations would support section- or station-level analysis. Public MEE
    bulletins are a separate canonical asset
    (china-mee-surface-water-quality-bulletins), not an acquisition route for
    this research panel.
  availability: partially-reproducible
  ordinary_researcher_feasible: false
  summary: >-
    MEE's public monthly, quarterly and annual bulletin series is now recorded
    separately as china-mee-surface-water-quality-bulletins. For the underlying
    section/station readings, the real-time automatic-monitoring publication
    system (szzdjc.cnemc.cn:8070) timed out for automated clients and browser
    historical access remains unverified. The two anchor papers' data sections
    are unread (Elsevier 403), so their exact monitoring product and geographic
    grain remain unestablished.
  barrier: >-
    Station/section-level historical microdata is not a one-click public
    download: the official route yields aggregate releases (monthly/quarterly/
    annual) plus the automatic-station real-time platform (technical
    friction). The exact station-level product used by the anchor papers
    (MEE national network vs local monitoring) is unread.

unit_of_observation: >-
  Monitoring section (断面) of rivers/lakes/reservoirs at sampling events.
  Section-level series are not part of the verified public bulletin releases;
  the separately catalogued bulletin asset supplies only national/basin aggregate
  summaries, not observations in this record.
structure: repeated-spatiotemporal
geo_granularity:
- monitoring section (national assessment section, 国控断面)
- river basin / water system
- lake and reservoir
- city (sections located in prefecture/county)
geography: >-
  National: 3641 national assessment sections (2025 releases) covering major
  rivers (七大流域: 长江、黄河、珠江、松花江、淮河、海河、辽河), 西北诸河、西南诸河、
  浙闽片河流, and 145 重点湖（库）(2026 Q2 release). Section count evolves with
  each Five-Year Plan.
time_span:
  start: unknown
  end: ongoing
  coverage_note: >-
    The national network operates in the 十四五 period with 3,641 assessment
    sections, but no complete historic section-level delivery, first measurement
    date or continuous roster has been verified for this asset. Dated public MEE
    bulletins are recorded separately and cannot fill those gaps.
  last_checked: '2026-08-15'
frequency:
- real-time (automatic monitoring stations)
- monthly (地表水水质月报)
- quarterly (全国地表水质量状况)
- annual (全国地表水质量状况)
sample_size: >-
  3641 national assessment sections (2025 releases); 145 重点湖（库） in the
  2026 Q2 release; automatic monitoring stations under CNEMC (count
  unverified this round).
key_variables:
- Water-quality class proportions: Ⅰ—Ⅲ类 (优良) share and 劣Ⅴ类 share of sections
- Main exceeding indicators (化学需氧量、高锰酸盐指数、总磷、五日生化需氧量)
- 重点湖（库） water quality and trophic status (中营养/轻度富营养/中度富营养)
- Section-level concentrations of standard indicators under MEE monitoring standards (network-measured; NOT part of the verified official aggregate releases — see unit_of_observation / access_routes)
- Basin-level aggregates for 七大流域 and 西北/西南诸河、浙闽片河流

research_fit:
  best_for:
  - Evaluating a separately verified source of section- or station-level surface-water readings for local exposure research
  - Understanding the monitoring family behind the cited research before seeking a provider-specific delivery route
  choose_over:
  - Choose this over china-air-quality-monitoring when the medium of interest is surface water, not ambient air; the two records are parallel products of the same MEE monitoring system family.
  - Choose this over china-firm-pollution for ambient water quality at monitoring sections; china-firm-pollution covers firm-level discharge/emissions reporting, a different unit.
  not_good_for:
  - Firm-level effluent or discharge amounts (use china-firm-pollution / enforcement records)
  - Groundwater quality and drinking-water source monitoring (separate MEE networks, not verified here)
  - Station-level hourly historical panels without a separately verified provider or compilation route
  needs_join_for:
  - Housing prices, firm outcomes, or health outcomes require location/time matching to the section network and to microdata (e.g., china-census for population controls)
  - Air pollution exposure studies should use china-air-quality-monitoring rather than water series
  variation_available:
  - Measured water-quality conditions differ across monitoring sections, basins and release periods; network composition, reporting frequency and available indicators can also change over time. These are data-coverage dimensions, not a treatment assignment or causal-design record.
  topics:
  - surface water quality
  - water pollution
  - river basin governance
  - environmental regulation
  - housing and environment

good_for:
- surface water quality exposure
- water governance policy evaluation
- environmental amenity and housing
- bureaucratic incentive and environmental assessment
identification: []
linkable_keys:
- Monitoring section name/code
- City (prefecture/county) where the section is located
- River basin
- Time (month/quarter/year)

joins:
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - city
  - time
  method: city-year/month matching of parallel MEE monitoring products
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - city code
  - year
  method: aggregate-level controls
  evidence_status: plausible
- target: china-firm-pollution
  relation: complement
  keys:
  - city
  - year
  method: firm-level discharge vs ambient section quality (different units; do not merge)
  evidence_status: plausible

access_routes:
- route: boundary-reference-separate-MEE-bulletin-series
  access_status: documentation-only
  direct_url: https://www.mee.gov.cn/hjzl/shj/qgdbszlzk/
  requirements: None; this is a route for a separate aggregate-bulletin asset, not for the readings in this record.
  steps:
  - If aggregate publication-level water-quality conditions are enough, switch to china-mee-surface-water-quality-bulletins and use its acquisition route.
  - Do not infer a section/station observation, a concentration value, a historical roster or a local panel from a bulletin's aggregate statements.
  deliverable: Documentation boundary only; it points to the distinct ready bulletin asset and does not deliver this monitoring asset.
  cost: free
  last_checked: '2026-09-28'
  caveat: Aggregate shares and indicator lists are not section-level concentration time series.
- route: realtime-automatic-station-platform
  access_status: needs-verification
  direct_url: http://szzdjc.cnemc.cn:8070/GJZ/Business/Publish/Main.html
  requirements: Browser session; automated clients time out (recorded in failed_tasks 2026-08-15); platform behavior unverified in this environment.
  steps:
  - Open the national surface-water automatic monitoring real-time publishing system.
  - Browse sections/stations for current quality.
  - Confirm historical download permissions and measurement definitions before batch use.
  deliverable: Real-time or recent automatic-station quality; historical batch access unverified.
  cost: free
  last_checked: '2026-08-15'
  caveat: Timeout for automated clients; human-browser availability unverified this round.
- route: third-party-compiled-panel
  access_status: needs-verification
  direct_url: https://data.epmap.org/product/water
  requirements: Third-party service terms unverified
  steps:
  - Review the third-party compiled station-level water-quality panel (青悦数据/IPE family) and its terms before use.
  deliverable: Compiled station-level panel (third-party); coverage and terms unverified.
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Secondary compilation; not the official MEE route; terms, coverage and update lag unverified.

access:
  url: http://szzdjc.cnemc.cn:8070/GJZ/Business/Publish/Main.html
  cost: unknown
  license: Historical batch access and reuse terms remain to be verified from a provider or compilation route.
  format:
  - html
  - pdf
  - xls
  api: false
  how_to_get: >-
    For section/station readings, first establish an actual provider or
    documented compilation route, then verify its historical coverage, section
    identifiers, measurement definitions and terms before collection. The MEE
    bulletin column belongs to the separate aggregate-publication asset and
    cannot establish access to this one.
caveats: >-
  The 3641-section network is the 十四五 assessment network; section counts
  changed across Five-Year Plans (unverified for earlier plans this round).
  The two anchor papers' exact water-quality product (MEE national network vs
  local stations; station-level vs section-level) is unread (Elsevier 403).
  Quality-class statistics are not concentration series.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: partial
  last_audited: '2026-09-28'

used_by:
- cite: 'Ge, Huang & Shi (2025), Cleaner water and higher housing prices: Evidence from China'
  doi: https://doi.org/10.1016/j.jpubeco.2025.105374
  journal: JPubE
  year: 2025
  dataset_role: Water quality monitoring + housing prices (anchor paper; exact product unread)
  evidence_type: title-level
  evidence_url: https://doi.org/10.1016/j.jpubeco.2025.105374
  data_note: Abstract channels empty (Layer-2b); ScienceDirect 403 for automated clients; registered as the water-quality anchor from the Layer-2b sweep (2026-08-15).
- cite: 'Lin, Sun & Zhao (2024), Environmental protection for bureaucratic promotion: Water quality performance review of provincial governors in China'
  doi: https://doi.org/10.1016/j.jeem.2024.103060
  journal: JEEM
  year: 2024
  dataset_role: Water quality performance outcomes for provincial governors (anchor paper; exact product unread)
  evidence_type: title-level
  evidence_url: https://doi.org/10.1016/j.jeem.2024.103060
  data_note: >-
    Abstract channels empty; ScienceDirect 403; registered from the Layer-2b
    sweep. Related water-quality user family screened in the same sweep
    (JEEM 2025.103200, JEEM 2026.103380, JPubE 2025.105495) - none read at
    data-section level.

provenance:
- source: https://www.mee.gov.cn/ywdt/xwfb/202601/t20260128_1142768.shtml
  field_scope:
  - provider
  - section_count
  - coverage
  - indicators
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/ywdt/xwfb/202607/t20260730_1163186.shtml
  field_scope:
  - frequency
  - indicators
  - lakes
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/hjzl/shj/
  field_scope:
  - access_route
  - product_family
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Rendered CNEMC homepage https://www.cnemc.cn/ (browser read 2026-09-28)
  field_scope:
  - visible current nationwide monitoring-section list with its three displayed fields
  - boundary that current display visibility does not establish historic panel, concentration, coordinates, archive or bulk access
  added: '2026-09-28'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-water-quality-monitoring, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: cnemc-current-national-surface-water-quality-dashboard
  relation: component
- id: china-mee-surface-water-quality-bulletins
  relation: successor
- id: china-air-quality-monitoring
  relation: complement
- id: china-firm-pollution
  relation: often-confused-with
---

## Positioning in one sentence

This record is the underlying MEE/CNEMC surface-water monitoring-reading family, not the separately obtainable MEE bulletin series. A historical section- or station-level panel requires an independently verified route, current automatic-platform conditions or a separately documented compilation.

## Select rules

- Prioritize when the research question needs surface-water quality at section/basin/city level, e.g., water-governance policy evaluation or water quality as an amenity.
- Switch to china-air-quality-monitoring for ambient air exposure; both are MEE monitoring-family products but different media and networks.
- For firm-level discharges use china-firm-pollution; do not equate ambient section quality with firm emissions.
- Before using a third-party compiled panel, verify its section coverage, measurement definition, and terms against the official releases.

## Get recipe

1. Start at the MEE water quality column (https://www.mee.gov.cn/hjzl/shj/) and collect 全国地表水质量状况 releases (quarterly/annual; verified back to 2025 Q1, latest 2026 Q2) and 地表水水质月报 (monthly).
2. For station-level work, evaluate the automatic-station real-time platform (szzdjc.cnemc.cn:8070; timed out for automated clients - human browser needed) or a third-party compilation with verified terms.
3. Expect class-proportion statistics (Ⅰ—Ⅲ类 / 劣Ⅴ类 shares) and exceeding-indicator lists, not raw concentration time series, from the official route.

## Connections and Limitations

- The 3641-section count is the 十四五 network; section definitions change across plans, so long panels must handle network changes.
- The anchor papers (JPubE 2025.105374; JEEM 2024.103060) use water-quality data in ways that remain unread at data-section level - do not assume they use the same product or granularity as this record's official route.
- The real-time platform's historical batch access is unverified; treat "official real-time page exists" as distinct from "historical station-level data obtainable".
