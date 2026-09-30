---
schema_version: 3
catalog_status: ready
id: mnr-national-real-estate-registration-bulletins
name: MNR annual national real-estate registration statistics in the China Natural Resources Bulletin
aka:
- 中国自然资源公报 不动产统一登记统计
- 全国不动产统一登记年度统计
- MNR national real-estate registration bulletin statistics
provider: Ministry of Natural Resources of the People's Republic of China (MNR, 自然资源部), through the annual 中国自然资源公报.
china_related: true
domains:
- housing
- urban
- property rights
- public statistics

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The annual, national aggregate real-estate-registration statistics in the
    不动产统一登记 section of the China Natural Resources Bulletin, delivered
    as a public PDF. This is an aggregate publication, not the underlying
    property-registration register.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The MNR bulletin column and the 2024 bulletin PDF are currently reachable.
    The verified 2023 and 2024 bulletins contain national annual counts of
    real-estate ownership certificates and registration proofs, including
    right-type breakdowns and multi-year charts. The checked material supports
    a national annual series for 2019-2024, not a subnational or property-level
    data product.
  barrier: >-
    Values are reported in PDFs and may require manual transcription. The
    publication does not establish province/city/property microdata, a bulk
    registry extract, or a stable machine-readable series.

unit_of_observation: National annual aggregate count or rate for a registration-certificate/proof category.
structure: Annual national aggregate statistical tables, charts and narrative in PDF bulletins.
geo_granularity:
- national
geography: Mainland China, national aggregate only.
time_span:
  start: '2019'
  end: '2024'
  last_confirmed_release: 2024 China Natural Resources Bulletin, published 2025-03-14; PDF route reached on 2026-09-28
  coverage_note: The 2023 and 2024 bulletins together verify charts covering 2019-2024. Earlier bulletin sections and any future releases need year-by-year confirmation.
  last_checked: '2026-09-28'
frequency:
- annual
sample_size: One national annual observation per reported registration category; 2019-2024 chart coverage verified.
key_variables:
- Number of 不动产权证书 issued, with right-type breakdowns where reported
- Number of 不动产登记证明 issued, including mortgage, pre-registration and objection-proof categories where reported
- Year-over-year change and multi-year national chart values where reported
- Selected national programme outputs reported in the same registration section

research_fit:
  best_for:
  - Describing national annual trends in property-registration output and registration-proof issuance
  - National housing, property-rights or mortgage-registration context where aggregate administrative output is the appropriate measurement layer
  choose_over:
  - Choose this over mnr-real-estate-registration when the need is the directly obtainable national bulletin layer rather than the restricted underlying registry.
  - Switch to city-level housing, land or transaction products when the question needs local price, transaction or property-unit variation.
  not_good_for:
  - City, province, county, property or household registration data
  - Housing prices, transaction values, ownership links or mortgage microdata
  - A causal-design or policy-assignment record
  needs_join_for:
  - National macro or housing indicators if modelling a national annual series
  - A separately verified local housing or land data source for subnational research
  variation_available:
  - Annual national time-series changes from 2019 to 2024
  - Cross-category differences among reported certificate and registration-proof types
  topics:
  - real-estate registration
  - housing statistics
  - property rights
  - mortgage registration

good_for:
- A transparent national annual registration-output series transcribed from official PDFs
- Documenting the distinction between public aggregates and restricted property-register data
identification:
- National annual changes in reported registration output; no local treatment or property-level design is encoded.
linkable_keys:
- Year
- Certificate or proof category

joins:
- target: mnr-real-estate-registration
  relation: component
  keys:
  - year
  method: This is the public national aggregate layer of the broader registration system. It must not be used to infer access to the restricted property register.
  evidence_status: verified
- target: china-land-transaction
  relation: often-confused-with
  keys: []
  method: Registration-output totals and public plot-level land-transfer announcements are different institutions, units and research objects.
  evidence_status: verified

access_routes:
- route: MNR China Natural Resources Bulletin column and annual PDF
  access_status: available
  direct_url: https://www.mnr.gov.cn/sj/tjgb/
  requirements: A normal browser or PDF-capable client.
  steps:
  - Open the MNR 自然资源公报 column and select the required annual China Natural Resources Bulletin.
  - Download its linked PDF; for the 2024 bulletin the verified PDF is http://gi.mnr.gov.cn/202503/P020251209353094119242.pdf.
  - Read the 不动产统一登记 section and transcribe only the reported national annual values, retaining bulletin year, page/figure and category.
  - Stop at national aggregates; choose a different source if the research requires local or property-level data.
  deliverable: Public annual bulletin PDF containing national registration statistics.
  cost: free
  last_checked: '2026-09-28'
  caveat: The bulletin is a PDF publication and not a microdata or subnational statistical release; section names and coverage should be rechecked for each bulletin year.

access:
  url: https://www.mnr.gov.cn/sj/tjgb/
  cost: free
  license: Public government bulletin; no separate open-data licence was identified in the checked material.
  format:
  - PDF
  api: false
  how_to_get: Download the relevant annual bulletin PDF from the MNR bulletin column, then preserve page/figure references while transcribing national aggregate statistics.
caveats:
- The verified series is national-only and covers 2019-2024 through the checked 2023/2024 bulletin charts.
- No city/province/county breakdown, machine-readable bulk file or property-level register is established by these PDFs.
- The underlying registration record system has separate statutory access restrictions and is not supplied by this product.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://www.mnr.gov.cn/sj/tjgb/
  field_scope:
  - official annual-bulletin column identity
  - current public starting route
  added: '2026-09-28'
  confidence: high
  verified: true
- source: http://gi.mnr.gov.cn/202503/P020251209353094119242.pdf
  field_scope:
  - 2024 bulletin PDF delivery and registration section
  - national certificate/proof counts, type breakdowns and 2020-2024 chart
  added: '2026-09-28'
  confidence: high
  verified: true
- source: http://gi.mnr.gov.cn/202402/P020240312701247258838.pdf
  field_scope:
  - 2023 bulletin registration section and 2019-2023 chart
  - continuity needed to document the 2019-2024 public annual range
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: mnr-real-estate-registration
  relation: component
- id: china-land-transaction
  relation: often-confused-with
---

## Positioning in one sentence

This is the public, obtainable layer of China’s real-estate-registration system: annual national totals in official MNR PDFs. It is useful for national context, but it cannot answer a city, household or property-level question.

## Select rules

- Choose it when the needed observation is a reported national registration total by year and type.
- Switch to local land or housing data when the outcome must vary across places or properties.
- Do not infer access to a property register from the public bulletin.

## Get recipe

1. Open the MNR bulletin column and choose the required annual bulletin.
2. Download the PDF and locate the 不动产统一登记 section.
3. Transcribe values with year, category, page and chart reference.
4. Treat the result as a national annual series only.

## Connections and Limitations

The public bulletin records administrative output at the national level; the underlying registry records property rights one property unit at a time and follows different statutory rules. A national increase in certificates is not a local housing-market observation, a transaction count or evidence about individual owners.

## Decision sufficiency check

A future agent can obtain the exact PDF route, identify one observation correctly, construct a documented national annual series and know when the product fails: any local, property or household requirement requires another source.
