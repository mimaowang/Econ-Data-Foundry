---
schema_version: 3
catalog_status: ready
id: china-mee-monthly-city-air-quality-reports
name: MEE National City Air Quality Monthly Reports (全国城市空气质量月报)
aka:
- 城市空气质量状况月报
- 全国城市空气质量报告
- 全国城市空气质量月报
- MEE city air-quality monthly reports
provider: 生态环境部监测司 and 中国环境监测总站 (China National Environmental Monitoring Centre), through the Ministry of Ecology and Environment report archive
china_related: true
domains:
- environment
- air quality
- urban
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Dated official PDF reports containing report-level, city-oriented monthly air-quality summaries; a report is a publication product, not the underlying station-hour or full city-day monitoring feed.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The MEE archive exposes a dated sequence of city-air-quality report pages with direct
    PDF delivery. On 2026-09-28, the archive, its July 2026 report page and the linked
    10.9 MB PDF all returned 200. The PDF is titled "2026年7月全国城市空气质量月报"
    and names MEE's monitoring department and CNEMC as producers.
  barrier: >-
    These reports are individual monthly publications. They do not establish a complete,
    machine-readable historical city-day or station-hour panel, an API, or a stable station roster.

unit_of_observation: One dated official monthly-report PDF; any city or regional values are report-specific published summaries, not a declared universal panel.
structure: Recurring monthly PDF publication series with narrative and tabular city/regional summaries
geo_granularity:
- city
- region
- national summary
geography: China; the city universe and regional groupings must be read from each report rather than assumed constant.
time_span:
  start: unknown
  end: ongoing
  last_confirmed_release: 2026-07 monthly report, posted 2026-08-31
  coverage_note: The live archive visibly listed dated 2025-2026 reports when checked. This proves a current report-publication sequence, not its first issue or a complete historical archive.
  last_checked: '2026-09-28'
frequency:
- monthly
sample_size: Report-specific; the July 2026 PDF describes national-city summaries and a 168-city section, but researchers must retain the stated universe for each report.
key_variables:
- Report-specific city air-quality rate or level summaries
- PM2.5, PM10, SO2, NO2, CO and O3 summary measures where reported
- AQI-related and primary-pollutant summaries where reported
- Regional and national comparison summaries

research_fit:
  best_for:
  - Obtaining official current or recent city-oriented monthly air-quality publications when report-level summary evidence is sufficient
  - Documenting published monthly air-quality conditions, stated city coverage and pollutant summaries without claiming access to raw monitoring observations
  choose_over:
  - Choose this series over secondary news summaries when an official dated PDF and its stated universe are needed.
  - Choose china-air-quality-monitoring only after separately verifying a high-frequency monitoring-data route; the report PDFs are not a substitute for station-hour or complete city-day readings.
  not_good_for:
  - Building a complete historical city-day, station-hour or station-panel dataset
  - Treating a report-specific city list as a balanced or unchanged national panel
  - Firm emissions, which require china-firm-pollution rather than ambient-air publications
  needs_join_for:
  - City identifiers and boundaries when a report table must be joined to other city-level data
  - A separately verified high-frequency provider route for daily exposure, event studies or station-level analysis
  variation_available:
  - Published month-to-month differences in report-specific city and regional summaries
  topics:
  - city air quality
  - monthly environmental reporting
  - ambient pollution summaries

good_for:
- Official monthly city-air-quality report acquisition
- Current/recent report-level pollution summaries
identification:
- >-
  Identify the asset by the MEE "城市空气质量状况月报" archive and a dated report page,
  then retain the linked PDF title, report month, publication date, URL and retrieval date.
  The checked July 2026 instance is page "2026年7月全国城市空气质量报告" and PDF
  "2026年7月全国城市空气质量月报".
- >-
  This is a report-PDF series produced by 生态环境部监测司 and 中国环境监测总站.
  It is distinct from the CNEMC/MEE underlying monitoring-reading family recorded in
  china-air-quality-monitoring, whose historical bulk station-hour/city-day delivery is not verified.
linkable_keys:
- Report month
- Report-specific city name
- Pollutant or summary indicator

joins:
- target: china-air-quality-monitoring
  relation: often-confused-with
  keys:
  - city
  - date or month
  method: Use this record only for published monthly summaries. Verify a separate provider route before attempting a high-frequency match to monitoring readings.
  evidence_status: verified
- target: china-firm-pollution
  relation: often-confused-with
  keys:
  - city
  - year
  method: Ambient report summaries and firm-emission data answer different questions; do not substitute one for the other.
  evidence_status: verified

access_routes:
- route: MEE city-air-quality monthly-report archive
  access_status: available
  direct_url: https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/
  requirements: None for the checked public report pages and PDFs.
  steps:
  - Open the archive and select the required dated report page.
  - Follow the page's PDF link; save the report month, page URL, PDF URL, publication date and retrieval date.
  - Read the PDF's stated city universe, indicators and table notes before extracting any values.
  deliverable: Free official monthly PDF report(s), not a verified full-history machine-readable monitoring panel.
  cost: free
  last_checked: '2026-09-28'
  caveat: The archive and July 2026 report/PDF were directly checked; historical completeness and table comparability remain report-specific.

access:
  url: https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/
  cost: free
  license: Government disclosure information; retain source attribution and report-specific conditions.
  format:
  - PDF
  - HTML report page
  api: false
  how_to_get: Start at the archive, choose a dated report page, download its linked PDF, and preserve the report-specific coverage and definitions with any extracted values.
caveats: >-
  A downloadable monthly report does not prove public access to raw station-hour readings,
  complete city-day history, a bulk API, unchanged city coverage or comparability across all report vintages.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/ (archive read 2026-09-28) and https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/202608/t20260831_1164765.shtml (report page read 2026-09-28)
  field_scope:
  - archive identity and dated report pages
  - July 2026 report-page identity
  - public HTML-to-PDF delivery
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.mee.gov.cn/hjzl/dqhj/cskqzlzkyb/202608/W020260831608340693618.pdf (downloaded 2026-09-28; 10,887,555 bytes)
  field_scope:
  - PDF title and producer bodies
  - report-level city and pollutant-summary scope
  - July 2026 report-specific 168-city section
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-air-quality-monitoring
  relation: complement
- id: china-firm-pollution
  relation: often-confused-with

---

## Positioning in one sentence

This is the public MEE series of dated monthly city-air-quality report PDFs: it is a usable official publication layer for report-level summaries, but not a hidden substitute for the underlying high-frequency monitoring data.

## Select rules

- Choose it when an official month-specific city-air-quality report is enough for the empirical task.
- Switch to a separately verified high-frequency product when daily, hourly, station-level or complete historical observations are required.
- Keep each report's city universe and table definitions with the extracted values.

## Get recipe

1. Open the archive and select the relevant monthly report page.
2. Download its linked PDF and record its month, URLs and retrieval date.
3. Read table notes before transcription; use only the report's stated coverage.

## Connections and Limitations

City names may need normalization before a city-level join. The report series has no verified bulk or station-level pathway, so it cannot support an event-study panel simply by concatenating visible PDFs.
