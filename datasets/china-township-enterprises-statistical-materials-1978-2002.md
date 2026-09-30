---
schema_version: 3
catalog_status: ready
id: china-township-enterprises-statistical-materials-1978-2002
name: China Township Enterprises Statistical Materials, 1978-2002 (中国乡镇企业统计资料)
aka:
- 中国乡镇企业统计资料 1978-2002年
- China Township Enterprises Statistical Materials 1978-2002
- DT363-C3
provider: 农业部乡镇企业局组编 (Township Enterprises Bureau of the Ministry of Agriculture, compiler); 中国农业出版社 (China Agricultural Press, publisher)
china_related: true
domains:
- rural
- regional
- development
- township and village enterprises
- historical statistics

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: A 2003 printed historical statistical compilation covering 1978-2002, with national and regional township-enterprise tables; the researcher receives a library copy or permitted pages, not Jin and Qian's constructed provincial panel.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The National Diet Library (NDL) live catalogue identifies the 2003 physical book as
    中国乡镇企业统计资料 : 1978-2002年, compiled by 农业部乡镇企业局, published by
    中国农业出版社, ISBN 7109083071, 416 pages, NDL call number DT363-C3. NDL's
    China long-statistics guide describes its national and regional sections as covering
    enterprise counts, employees, gross output, revenue and foreign-funded enterprises
    by enterprise type. This is a usable historical table source through a library or
    permitted document delivery, not an open machine-readable panel.
  barrier: >-
    Table layout, regional coverage, units and definitions must be checked on the requested
    pages. The NDL record proves physical/library access, not unrestricted digital copying,
    universal availability at every library, or equivalence to a paper's earlier annual issues.

unit_of_observation: Published statistical table cell, typically a national or province/region x year x township-enterprise category/indicator observation; exact grain is table-specific.
structure: One printed historical compilation with national and regional statistical table sections
geo_granularity:
- national
- province or region where the selected table reports it
geography: China; geographic coverage and category definitions must be retained table by table.
time_span:
  start: '1978'
  end: '2002'
  last_confirmed_release: 2003 printed edition
  coverage_note: The title establishes the 1978-2002 compilation span. NDL describes national and regional sections, but does not establish every indicator's annual continuity or a uniform geographic breakdown.
  last_checked: '2026-09-28'
frequency:
- annual series where the selected table supplies annual values
sample_size: 416-page printed compilation; the number of usable region-year-indicator cells depends on the chosen tables.
key_variables:
- Township-enterprise counts
- Employees
- Gross output
- Revenue
- Foreign-funded enterprise indicators
- Enterprise-type categories and national/regional breakdowns where reported

research_fit:
  best_for:
  - Historical rural-industrialization research needing published township-enterprise aggregate statistics across the reform-era 1978-2002 span
  - Building a transparently transcribed national or province/region series after preserving table, unit, category and page provenance
  choose_over:
  - Choose this compilation when a documented long historical table source is sufficient and a library route is feasible.
  - Choose china-township-enterprises-statistical-yearbook only when the question specifically requires the earlier annual CTESY issues cited by Jin and Qian; the two sources are not interchangeable.
  - Choose ASIF or a firm registry for firm-level identifiers and micro outcomes, which this aggregate compilation cannot provide.
  not_good_for:
  - Firm, household or worker microdata
  - Assuming every table is a balanced province-year series without page-level inspection
  - Reproducing Jin and Qian's 1987-1994 annual-issue inputs or their derived provincial panel without separately obtaining and verifying those issues
  needs_join_for:
  - Province/region concordances and population or price denominators from independently documented historical statistical sources
  - A table-specific definition and unit check before combining the series with another source
  variation_available:
  - Historical annual and regional differences in published township-enterprise aggregates
  topics:
  - township enterprises
  - rural industrialization
  - regional development
  - historical aggregate statistics

good_for:
- Historical township-enterprise aggregate data acquisition through a documented library source
- Source-labeled national or regional TVE series reconstruction
identification:
- >-
  Identify the asset by its full Chinese title 中国乡镇企业统计资料 : 1978-2002年,
  compiler 农业部乡镇企业局组编, publisher 中国农业出版社, 2003.8 publication date,
  ISBN 7109083071 and NDL catalogue identifier a1000045529 / call number DT363-C3.
- >-
  It is a 2003 retrospective compilation, distinct from the earlier annual China
  Township Enterprises Statistical Yearbook / CTESY issue family and from any
  researcher-built panel that uses either source.
linkable_keys:
- Year
- Province or region label where reported
- Enterprise category
- Indicator, unit, table and page number

joins:
- target: china-township-enterprises-statistical-yearbook
  relation: complement
  keys:
  - year
  - region
  - enterprise category and unit
  method: Compare definition, reference year and table notes before using an overlapping value; the compilation is a later source and does not prove equivalence to the annual CTESY issue.
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - province or region
  - year
  method: Join only after documenting units and historical region labels; retain source provenance rather than silently replacing TVE-specific measures.
  evidence_status: plausible

access_routes:
- route: National Diet Library catalogue and document-delivery route
  access_status: available-with-conditions
  direct_url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia1000045529
  requirements:
  - NDL reading access or a library/document-delivery route that can supply the physical volume or permitted pages
  - Compliance with the holding library's copying and copyright rules
  steps:
  - Open the NDL catalogue record and request 中国乡镇企业统计资料 : 1978-2002年 using call number DT363-C3 or ISBN 7109083071.
  - Inspect the needed table's table of contents, page, reference year, geographic scope, category and unit before transcription.
  - Retain page-level provenance and any footnotes with the transcribed series.
  deliverable: Physical library volume or permitted page copy/transcription of the 2003 statistical compilation.
  cost: paid
  last_checked: '2026-09-28'
  caveat: NDL's catalogue shows a physical 416-page book and a listed price of 180 yuan; local access, delivery fees and copy permissions vary by holding library.

access:
  url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia1000045529
  cost: paid
  license: Printed-volume copyright and holding-library/document-delivery conditions; no open-data licence is established.
  format:
  - printed book
  - permitted page scan or transcription
  api: false
  how_to_get: Request the exact NDL-held book or an equivalent library copy, inspect table identity and notes, then transcribe only the needed source-labeled values under the library's conditions.
caveats: >-
  This is a historical aggregate compilation, not a digital microdata release. It must not
  be conflated with the annual CTESY issues used by Jin and Qian, a firm panel, or a
  rights-cleared PDF download. Definitions, reference years and regional coverage may vary
  by table.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia1000045529 (live catalogue page read 2026-09-28)
  field_scope:
  - exact title, compiler, publisher, publication date, ISBN, physical form, page count and NDL call number
  - library acquisition route and listed price
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://ndlsearch.ndl.go.jp/rnavi/asia/post_97 (live NDL China long-statistics guide read 2026-09-28)
  field_scope:
  - national and regional table sections
  - described enterprise count, employee, gross-output, revenue and foreign-funded-enterprise subject coverage
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-township-enterprises-statistical-yearbook
  relation: complement
- id: china-stat-yearbook
  relation: complement

---

## Positioning in one sentence

This is a library-obtainable 2003 compilation of 1978-2002 Chinese township-enterprise aggregate statistics, useful for documented historical series construction but not a substitute for an annual CTESY issue, a firm dataset, or an open download.

## Select rules

- Use it when reform-era national or region-level TVE aggregates are needed and a physical/library source is acceptable.
- Switch to the annual CTESY record only when the question requires the exact issue family cited by the QJE paper.
- Preserve each table's unit, definition, page and reference year before joining to another source.

## Get recipe

1. Request DT363-C3 / ISBN 7109083071 through NDL or a compatible library.
2. Identify the exact table and inspect its definitions and coverage.
3. Transcribe needed values with page-level provenance under the library's permitted-copy conditions.

## Connections and Limitations

The useful join is a carefully normalized region-year indicator series. The principal risk is treating a later compilation as identical to an earlier annual yearbook, or treating a table-specific regional series as a balanced panel without inspecting the book.
