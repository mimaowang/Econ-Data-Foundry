---
schema_version: 3
catalog_status: ready
id: china-rural-economic-statistics-1949-1986
name: Compilation of China's Rural Economic Statistics, 1949-1986 (中国农村经济统计大全：1949-1986)
aka:
- '中国农村经济统计大全：1949-1986'
- '中国农村经济统计大全: 1949-1986'
- China Rural Economic Statistics Encyclopedia, 1949-1986
- "Compilation of China's Rural Economic Statistics: 1949-86"
provider: Ministry of Agriculture Planning Division (中华人民共和国农业部计划司); Agricultural Press (农业出版社), Beijing, 1989
china_related: true
domains:
- regional
- rural
- agriculture
- development
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: A Chinese-language printed statistical compilation of historical rural and agricultural statistics for 1949-1986; the paper-used object is the relevant provincial tables, not a released copy of Li and Yang's cleaned panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The title, edition, ISBN, library identifiers, and paper use are documented. The current CiNii catalogue identifies the May 1989 Agricultural Press volume, its Ministry of Agriculture Planning Division compiler, 2 preliminary pages plus 9 pages plus 707 pages, and 38 university-library holdings. A researcher can select a holding or request permitted document delivery, then manually transcribe and validate the needed tables with page provenance. No stable public machine-readable download or open reuse licence was verified.
  barrier: The route is library-mediated and table extraction is manual. The volume's exact table inventory, scan availability, and copyright/reuse conditions must be checked with the holding institution; a citation does not imply access to the final analysis file.

# Identity and Coverage
unit_of_observation: Provincial or other aggregate rural/agricultural statistical entry; the exact grain varies by chapter and table
structure: Historical aggregate tables, with annual series where a table reports them
geo_granularity:
- province
- national or regional aggregate where supplied by a table
geography: Mainland Chinese provinces and aggregate regions represented in the compilation; the presence of a province, indicator, and year must be checked table by table
time_span:
  start: '1949'
  end: '1986'
  last_confirmed_release: '1989-05'
  coverage_note: The book title and bibliographic records cover 1949-1986. Li and Yang's final provincial panel runs from 1954 to 1989 because they supplement the book with the China Statistical Yearbook, provincial agricultural statistical yearbooks, and other paper-specific sources. Do not treat the book as evidence for the post-1986 years.
  last_checked: '2026-09-28'
frequency:
- annual historical series where reported
- table-dependent aggregate observations
sample_size: Not stated as a single machine-readable count; province and indicator coverage varies by table
key_variables:
- Provincial agricultural input and output series
- Grain and crop output; Li and Yang define grain as the sum of eight crops in their derived panel
- Sown area and related agricultural production measures
- Draft animals and farm capital inputs, including the paper's equivalent-horsepower construction
- Agricultural population/labor and related regional controls where reported
- Procurement, retention, or grain-allocation tables where reported

# Research routing
research_fit:
  best_for:
  - Historical provincial agricultural production and input comparisons, especially for the pre-1986 planning-era baseline
  - Recovering source tables behind Li and Yang's 1954-1986 provincial agricultural series
  - Building a documented historical aggregate panel when the researcher can preserve table/page/unit provenance
  choose_over:
  - Choose it over a modern China Statistical Yearbook when the question requires the 1949-1986 historical compilation or its pre-reform agricultural tables
  - Use the China Statistical Yearbook and provincial agricultural yearbooks alongside it when the target period extends beyond 1986 or when missing years/definitions need cross-checking
  - Prefer a machine-readable released replication file when the goal is to reproduce Li and Yang's final regression sample rather than inspect the underlying historical source
  not_good_for:
  - Household, farm, village, firm, or individual microdata
  - A guaranteed balanced province-year panel, county-level observations, or a current agricultural series
  - Treating every indicator in the book as available for every province and year
  - Inferring causal treatment, exogenous exposure, or the paper's retrospective survey from the book
  needs_join_for:
  - 1987-1989 agricultural outcomes and missing values from the China Statistical Yearbook or provincial Agricultural Statistical Yearbooks
  - Population, mortality, and other controls not present or not continuous in the selected tables
  - Li and Yang's weather, collective-unit scale, and exit-rights variables, which came from a separate 1999 retrospective province survey
  variation_available:
  - Provincial cross-sectional and historical-year dimensions only; this record makes no causal or exogenous-variation claim
  topics:
  - agricultural production
  - rural development
  - central planning
  - historical regional growth
  - provincial input-output comparisons

good_for:
- Manual reconstruction or cross-checking of historical provincial agricultural aggregates
- Establishing the source boundary for the agricultural component of Li and Yang's Great Leap Forward panel
identification:
- This descriptive historical statistical compilation does not itself encode a causal design or a verified treatment-assignment rule.
- Its provincial and historical dimensions require separate design evidence; they are not classified here as exogenous variation.
linkable_keys:
- Province name and historical province label
- Year
- Table title, indicator label, unit, and page number
- Researcher-built province concordance if administrative labels changed

joins:
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province name/code
    - Year
    - Indicator and unit
    method: Use the later Yearbook and provincial Agricultural Statistical Yearbooks to extend 1987-1989 and cross-check missing or conflicting entries. Preserve the book edition and source page instead of silently merging revisions.
    evidence_status: literature-used

access_routes:
  - route: Library catalogue and interlibrary loan
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/BN10983973
    requirements:
    - Library membership or interlibrary-loan/scan request
    - Chinese-language table reading and manual transcription
    steps:
    - Search by the Chinese title, ISBN 7109009300, or NCID BN10983973
    - Confirm the title page, edition, publisher imprint, table of contents, and relevant province tables
    - Request only the needed pages under the holding library's scan and copyright rules
    - Transcribe values with page, table, unit, footnote, and missing-value codes; validate against a later Yearbook where possible
    deliverable: Physical consultation, permitted library scan, or researcher-transcribed table; no public machine-readable file was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: CiNii and WorldCat establish catalogue identity and holdings, not that every holding library offers a scan or permits redistribution.
  - route: WorldCat holding-library search
    access_status: available-with-conditions
    direct_url: https://search.worldcat.org/pt/title/%3A-%281949-1986%29/oclc/22378850
    requirements:
    - A participating library or document-delivery service
    steps:
    - Search OCLC 22378850 or ISBN 9787109009301
    - Ask the library to verify the 1989 first-edition Chinese volume and the requested chapter/table
    - Record the institution, edition, page range, and permission terms in the extraction log
    deliverable: Library copy or permitted document delivery, not an open data download
    cost: mixed
    last_checked: '2026-08-11'
    caveat: WorldCat is a discovery and holding route; access, fees, and scan rights depend on the institution.

access:
  url: https://ci.nii.ac.jp/ncid/BN10983973
  cost: mixed
  license: Printed-volume copyright and library scan/document-delivery terms; no open-data licence was identified
  format:
  - printed Chinese volume
  - permitted library scan
  - researcher-transcribed table
  api: false
  how_to_get: Locate the CiNii or WorldCat record by title/ISBN/NCID/OCLC, obtain a library copy or permitted scan, verify the title page and table definitions, and transcribe only the needed tables with page-level provenance. Google Books confirms bibliographic metadata and reports no eBook availability; it is not a download route.
caveats:
- CiNii records 707 pages while Google Books records 718 pages; retain this discrepancy until a physical title page and pagination are checked.
- The source ends in 1986, whereas Li and Yang's final panel extends to 1989 through other yearbooks and sources.
- Li and Yang's paper-derived variables (for example, eight-crop grain output and equivalent horsepower) are transformations of source tables, not a claim that the book contains those exact final columns.
- The source does not prove that Li and Yang's final cleaned panel, retrospective province survey, or code is publicly reproducible.
- Rojas databank tables and third-party commercial PDF claims may help locate related historical series, but they are not accepted as a direct substitute for this volume or evidence of its licensing.
- Province labels, units, footnotes, and missing-value conventions must be preserved; historical aggregate definitions may change across the 1949-1986 span.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
  - cite: 'Li & Yang (2005), The Great Leap Forward: Anatomy of a Central Planning Disaster'
    doi: https://doi.org/10.1086/430804
    journal: JPE
    year: 2005
    dataset_role: Main historical source for provincial agricultural input and output series in the 1954-1989 panel
    evidence_type: data_appendix
    evidence_url: https://www3.nd.edu/~nmark/ChinaCourse/TheWeeks/Li_Yang_GLF_JPE.pdf
    data_note: Appendix B says provincial agricultural inputs and outputs came mainly from this Ministry of Agriculture compilation. The paper cross-checked or filled missing observations with the China Statistical Yearbook and provincial Agricultural Statistical Yearbooks; its weather, collective-unit, and exit-rights measures came from a separate retrospective province survey.

provenance:
  - source: https://www3.nd.edu/~nmark/ChinaCourse/TheWeeks/Li_Yang_GLF_JPE.pdf
    field_scope:
    - paper actually uses the compilation
    - provincial agricultural input/output role
    - 1954-1989 final-panel boundary and later-yearbook supplementation
    - paper-derived variable definitions and separate retrospective survey boundary
    added: '2026-08-11'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BN10983973
    field_scope:
    - exact Chinese title and editor
    - 1989 publication metadata
    - ISBN, NCID, language, pagination, and catalogue holdings
    added: '2026-08-11'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BN10983973
    field_scope:
    - Current May 1989 bibliographic metadata, 2 preliminary pages plus 9 pages plus 707-page extent, and 38 university-library holdings
    - Current library-mediated acquisition route for the printed volume
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://search.worldcat.org/pt/title/%3A-%281949-1986%29/oclc/22378850
    field_scope:
    - printed first-edition identity
    - publisher, ISBN, OCLC, and holding-library discovery route
    added: '2026-08-11'
    confidence: high
    verified: true
  - source: https://books.google.com/books/about/%E4%B8%AD%E5%9B%BD%E5%农村经济统计大全_1949_1986.html?id=gS0yAAAAMAAJ
    field_scope:
    - corroborating bibliographic metadata
    - no eBook availability statement
    added: '2026-08-11'
    confidence: med
    verified: true

related_datasets:
  - id: china-stat-yearbook
    relation: complement
---

## Positioning in one sentence

This is a paper-used printed source for historical provincial agricultural statistics, not Li and Yang's final regression file: its irreplaceable value is the 1949-1986 source boundary, while its main cost is finding a library copy and manually preserving table definitions, units, and pages.

## Select rules

- Prioritize it when a question needs the planning-era provincial agricultural tables or when the researcher must audit the source behind Li and Yang's 1954-1986 observations.
- Pair it with the China Statistical Yearbook and provincial agricultural yearbooks for 1987-1989, missing values, and definition checks; do not silently treat the combined panel as one ready-made release.
- Switch to a verified replication file if the goal is exact reproduction of Li and Yang's cleaned regressions rather than source-table inspection. Switch to modern yearbooks for current or annual post-1986 coverage.
- Do not use this record for household/farm microdata or for claims about policy assignment and causal identification.

## Get recipe

1. Search CiNii using `BN10983973`, ISBN `7109009300`, or the Chinese title; use WorldCat OCLC `22378850` if the local catalogue has no result.
2. Obtain a physical copy, interlibrary-loan scan, or other permitted document delivery. Confirm the 1989 title page and the relevant table's edition.
3. Define the province-year-indicator cells needed for the research question before transcribing. Record table/page, unit, footnotes, and missing-value codes for every cell.
4. Cross-check overlaps against the China Statistical Yearbook or provincial Agricultural Statistical Yearbooks, especially when extending beyond 1986 or filling gaps.
5. Keep any derived panel and transformations (such as eight-crop grain totals or equivalent horsepower) in a separate reproducible project; this record identifies the source asset only.

## Connections and Limitations

The safest join is province-by-year with an explicit historical label/code concordance and the source table's indicator/unit. A later Yearbook can extend the period and cross-check values, but revisions and changing definitions must remain visible. The book itself does not establish county, household, or farm microdata, and it does not contain the retrospective survey variables that Li and Yang collected separately. Because no open digital release was verified, a future agent should not promise a bulk download or redistribution permission until a specific holding institution confirms it.

## Decision sufficiency check

For a researcher studying historical provincial agricultural production, this record selects the volume because it is the source actually used for the relevant pre-1986 tables, and its current CiNii route lets the researcher choose among identified holdings for page-provenanced consultation or extraction. It is ready for that bounded source-table use, not for a downloadable panel or exact paper replication: the book ends in 1986, table-specific province/unit coverage and reuse terms still need inspection, and Li and Yang's later years and derived variables remain separate work. If a physical copy is unavailable, if the needed indicator is absent, or if the unit definition cannot be reconciled, the recommendation fails and the researcher should switch to a verified yearbook or replication asset rather than infer the missing values.
