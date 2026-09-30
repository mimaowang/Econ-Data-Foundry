---
schema_version: 3
catalog_status: ready
id: china-population-yearbook-1991
name: China Population Yearbook, 1991 (中国人口年鉴 1991)
aka:
- 中国人口年鉴 1991
- 中国人口年鉴
- China Population Yearbook
- Almanac of China's Population
- CPY 1991
provider: Chinese Academy of Social Sciences Institute of Population and its China Population Yearbook editorial office; Economic Management Press (经济管理出版社) published the series through the 1995 issue in the current NDL catalogue
china_related: true
domains:
- population
- regional
- urban
- labor
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed 1991 China Population Yearbook volume and its issue-specific population, urbanization and census tables; the provincial variables constructed by Jin and Qian are not a released copy of the yearbook
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: Jin and Qian's QJE appendix identifies CPY 1991 as the source for the 1990 census urban-population share and population denominators in their provincial panel. The current NDL catalogue identifies the continuing 中国人口年鉴 series, its CASS Institute of Population/China Population Yearbook editorial responsibility, its Economic Management Press run through 1995, and an NDL holding sequence that includes 1991. A library copy or permitted scan is therefore a concrete acquisition route; the cited 1991 issue remains distinct from a downloadable panel.
  barrier: "The paper bibliography says Beijing: China Population Press, 1991, while the current NDL series record documents Economic Management Press for the relevant publication period. This does not prevent locating the distinct series, but the title page, exact table numbers, reference-year convention, machine-readable delivery and reuse terms still need checking. 中国人口统计年鉴 must not be treated as the same product."

# Identity and Coverage
unit_of_observation: National, provincial, city or other population-statistical entry; exact grain depends on the table
structure: Annual population almanac with aggregate demographic, urban/rural, census and research tables
geo_granularity:
- national aggregate where reported
- province/autonomous-region/municipality where reported
- city or county entries for selected tables
geography: Mainland Chinese population and urban/rural statistics represented in the 1991 volume; table-specific geographic coverage must be checked from the issue
time_span:
  start: '1990'
  end: '1991'
  last_confirmed_release: '1991 volume, bibliographically dated 1992'
  coverage_note: The QJE appendix uses the 1990 census urban-population share and cites CPY 1991-1994 for population denominators; this record grounds only the 1991 component and does not imply that later CPY volumes or all tables are included. The current NDL series holding explicitly includes 1991, but table-level publication/reference-year mapping remains a volume check.
  last_checked: '2026-09-28'
frequency:
- annual issue
- table-specific census and population series
sample_size: Not a microdata sample; counts and geographic coverage vary by table
key_variables:
- Urban population and total population used to construct the 1990 census urban-population share
- Provincial population denominators used with state-industrial output in the QJE panel
- Urban/rural, city/town and agricultural/non-agricultural population tables where reported
- Population, area and density or other demographic indicators in the issue's aggregate tables

# Research routing
research_fit:
  best_for:
  - Historical provincial urbanization and population denominators when the question needs the population-almanac source used by Jin and Qian (1998 QJE)
  - Reconstructing the CPY 1991 component of a late-1980s/early-1990s provincial regional panel
  - Checking urban/rural and census-era population definitions before joining historical rural or industrial yearbooks
  choose_over:
  - Choose this record when the paper or source trail specifically names 中国人口年鉴/China Population Yearbook; do not replace it with 中国人口统计年鉴 merely because the names look similar
  - Use the China Statistical Yearbook for broad official macro tables and the China Census record for census products or microdata; neither silently proves the CPY 1991 table identity
  - Use current population releases for current questions only after checking that the urban/rural definition and boundary vintage are comparable
  not_good_for:
  - Individual or household microdata, person identifiers or a public-use census microfile
  - A guaranteed balanced city/county panel or every province-year combination
  - Treating the volume as Jin and Qian's final cleaned panel or as a policy-treatment dataset
  - Assuming that the paper's cited publisher, the series-level catalogue publisher and a third-party scan listing are interchangeable without title-page verification
  needs_join_for:
  - State-enterprise output and price controls from the China Statistical Yearbook
  - Rural labor, cultivated land and rural gross-social-product denominators from the China Rural Statistical Yearbook
  - Township-enterprise outcomes from CTESY/TESM and rural income/revenue from the China Agricultural Yearbook
  - Direct census or GIS products when the question needs boundary concordances, county detail or microdata
  variation_available:
  - Provincial, urban/rural and census-era population dimensions; this describes data coverage only and is not a policy-treatment or causal-variation record
  topics:
  - population geography
  - urbanization
  - rural-urban classification
  - regional development
  - demographic denominators

good_for:
- Manual reconstruction or validation of historical provincial urban-population shares and population denominators
- Documenting the CPY source boundary behind Jin and Qian (1998 QJE)
- Comparing population-almanac definitions with the general Statistical Yearbook and census products
identification:
- This historical population source is descriptive and does not itself encode a causal design or a verified treatment-assignment rule.
- Population differences across provinces, urban/rural categories and census-era tables require separate design evidence; they are not classified here as exogenous variation.
linkable_keys:
- Province/autonomous-region/municipality or historical city label
- Year, issue label and reference-year convention
- Population category (urban, rural, total, agricultural/non-agricultural)
- Indicator, unit, table and page number
- Researcher-built geographic concordance when historical boundaries changed

joins:
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province or region
    - Year and reference-year convention
    - Population category and unit
    method: Use CPY for the paper-specific urban-population share and population denominator role, and the China Statistical Yearbook for state-industry output or CPI inputs. Preserve the source table and do not substitute a general population table without comparing definitions.
    evidence_status: literature-used
  - target: china-rural-statistical-yearbook-1984-1994
    relation: complement
    keys:
    - Province or region
    - Year
    - Rural population and rural/total category
    method: Compare the CPY and CRSY population denominators by issue and definition before joining; the QJE appendix assigns them different source roles even when both contain population measures.
    evidence_status: literature-used
  - target: china-census
    relation: complement
    keys:
    - Province or region
    - 1990 census reference date
    - Urban/rural population category
    method: Use a census product when the research question needs the underlying census or finer geography. CPY records the paper's population-almanac route; it does not prove that a census microfile or GIS concordance is included.
    evidence_status: literature-used
  - target: china-agricultural-yearbook
    relation: complement
    keys:
    - Province or region
    - Year and issue/reference-year convention
    - Rural population or income indicator
    method: Keep CPY's urban-share/population-denominator role separate from CAY's rural income, government-revenue and agricultural-accounting tables; verify province labels and reference years before any join.
    evidence_status: plausible

access_routes:
  - route: CiNii Books and university-library holdings for the China Population Yearbook series
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/BN06246133
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Confirmation that the requested item is the 1991 volume of 中国人口年鉴, not 中国人口统计年鉴
    steps:
    - Search NCID BN06246133 and ask a holding library for the 1991 volume
    - Verify the title page, editorial office, publisher, publication date, ISBN 7800256111 and table of contents
    - Match the urban-population-share and denominator tables to the QJE Appendix Table I before copying values
    - Request only needed pages under the library's scan and copyright rules; record table, page, unit, geographic coverage and footnotes
    deliverable: Physical volume, permitted scan or researcher-transcribed tables; no open machine-readable CPY file was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The CiNii endpoint had a transient TLS body-retrieval failure in this check. The independent current NDL route below confirms the library-mediated acquisition decision; neither catalogue establishes scanning or redistribution permission.
  - route: National Diet Library series record and holding-library/document-delivery route
    access_status: available-with-conditions
    direct_url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053584
    requirements:
    - Library or document-delivery access
    - Title-page and table-level comparison with the paper citation
    steps:
    - Use the NDL series record to locate a 1991 issue and its holding institutions
    - Check the publisher discrepancy and publication/reference-year convention before extraction
    - Request only the pages needed for the research question and preserve issue provenance
    deliverable: Physical volume or permitted copy; not the paper's final panel
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The current NDL catalogue identifies the series and includes 1991 in its NDL holding sequence; it is a realistic volume route but does not itself establish the exact tables used by Jin and Qian, a scan or redistribution permission.
  - route: Third-party 1991 scan listing (unverified digital lead)
    access_status: needs-verification
    direct_url: https://www.nianjian.cc/post-4315.html
    requirements:
    - Verify file provenance, exact edition, payment terms and reuse permission
    - Compare the delivered scan with a library title page and the QJE source citation
    steps:
    - Use the listing only to corroborate ISBN/page/publisher metadata and to locate a possible copy
    - Do not treat its paid scan as an open-data release or redistribute it without permission
    deliverable: Possible PDF scan subject to provider terms; not accepted as a rights-cleared route
    cost: paid
    last_checked: '2026-08-12'
    caveat: The page advertises a scan and download service; it is not an official publisher or library licence.

access:
  url: https://ci.nii.ac.jp/ncid/BN06246133
  cost: mixed
  license: Printed-volume copyright and library/document-delivery terms; no open-data licence for the 1991 issue was identified
  format:
  - printed Chinese annual volume
  - permitted library scan
  - researcher-transcribed table
  api: false
  how_to_get: Start with CiNii or NDL holdings, request the 1991 volume, verify the title page and publisher against the QJE citation, and transcribe only the required provincial/census tables with page, unit, reference-year and footnote provenance. Treat third-party scan listings as unverified leads.

caveats:
- The paper bibliography says Beijing: China Population Press, 1991, while the 1991 volume metadata points to Economic Management Press and publication in 1992; preserve this discrepancy until the physical title page is checked.
- 中国人口年鉴 and 中国人口统计年鉴 are distinct series with different compilers and publication roles; never merge them by topic or year.
- The QJE paper uses CPY tables to build ratios and denominators; the yearbook is not the final cleaned provincial regression panel.
- Aggregate tables may use different urban/rural definitions, census reference dates and historical geographic boundaries; record table notes before joining.
- No county/household/individual identifiers, census microdata or GIS concordance are established by this record.
- No policy, treatment, causal-variation or identification record is created here.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
  - cite: 'Jin & Qian (1998), Public Versus Private Ownership of Firms: Evidence from Rural China'
    doi: https://doi.org/10.1162/003355398555748
    journal: QJE
    year: 1998
    dataset_role: Urban-population share and population-denominator component of a provincial rural-enterprise panel
    evidence_type: data_appendix
    evidence_url: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    data_note: Appendix Table I states that state-industry size divides CSY real state-enterprise output by population from CPY 1991-1994, and that the share of urban population uses 1990 census urban population divided by total population from CPY 1991. These are source-table roles used to construct paper variables; CPY does not equal the final panel.

provenance:
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - paper actually uses CPY
    - 1990 census urban-share role
    - population-denominator role and year labels
    - derived-variable boundary
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BN06246133
    field_scope:
    - Chinese and English series identity
    - Institute of Population editorial identity
    - annual volumes including 1991
    - library holdings and acquisition route
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053584
    field_scope:
    - Current continuing-series identity, editorial responsibility and Economic Management Press publication period through 1995
    - Current NDL holding sequence including the 1991 issue and library-mediated acquisition route
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://www.nianjian.cc/post-4315.html
    field_scope:
    - 1991 volume ISBN 7800256111
    - 753-page metadata
    - Economic Management Press and 1992 publication metadata
    - table-list and paid scan lead only
    added: '2026-08-12'
    confidence: med
    verified: false

related_datasets:
  - id: china-stat-yearbook
    relation: complement
  - id: china-rural-statistical-yearbook-1984-1994
    relation: complement
  - id: china-census
    relation: complement
  - id: china-agricultural-yearbook
    relation: complement
---

## Positioning in one sentence

This is the 1991 population-almanac volume behind Jin and Qian's historical urban-share and population-denominator inputs, not a census microfile or their final panel: its value is the paper-specific source identity and aggregate population detail, with a current NDL library route for lawful issue-by-issue consultation.

## Select rules

- Prioritize it when a historical regional question needs the CPY source named in Jin and Qian or a comparable population-almanac table for the 1990 census-era urban share.
- Keep it separate from 中国人口统计年鉴, the China Census microdata record and the general China Statistical Yearbook. Use those alternatives only when their product identity, definitions and access route fit the research question.
- Pair it with CRSY, CAY and CSY when reconstructing the full provincial rural-enterprise panel; preserve each source's table, year and denominator definition.
- Do not use it as household/individual microdata or infer county detail, GIS keys or policy treatment from a population table.

## Get recipe

1. Search CiNii NCID `BN06246133` or the NDL series record for a library holding the 1991 volume.
2. Obtain a physical copy, permitted scan or other lawful document delivery. Confirm the title page, editorial office, publisher, publication date and ISBN `7800256111`.
3. Locate the 1990 census urban-population and total-population tables, plus the denominator table needed for the research question. Record page, unit, category, reference date and footnotes.
4. Join by province or historical region only after checking urban/rural definitions and boundary concordances against the companion yearbooks or census source.
5. Keep any derived urban-share or provincial panel in a separate reproducible project; this record identifies the source asset and route, not a redistributed analysis file.

## Connections and Limitations

The safest join is province-by-reference-date plus population category, indicator, unit and table/page provenance. CPY supplies the paper-specific urban-share and population-denominator role; CSY, CRSY, CAY and census products supply distinct complements. A recommendation fails for a particular extraction if the title page reveals a different product, the required table is absent, the urban/rural definition cannot be reconciled, or only an unauthorized scan is available; those are issue-level stop conditions, not grounds to erase the verified library route.

## Decision sufficiency check

For a researcher studying historical provincial urbanization alongside rural industrialization, this record selects CPY for the paper-specific 1990 urban share and population denominator, starts with the current NDL library route for the 1991 issue, and warns against substituting the similarly named population-statistics yearbook. It is ready for page-provenanced consultation and extraction, not for claiming a downloadable panel, unrestricted copying, complete table compatibility or Jin and Qian's final cleaned provincial panel.
