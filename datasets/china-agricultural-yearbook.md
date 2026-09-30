---
schema_version: 3
catalog_status: ready
id: china-agricultural-yearbook
name: China Agricultural Yearbook, 1981-1994 (中国农业年鉴)
aka:
- 中国农业年鉴
- China Agricultural Yearbook
- Zhongguo nongye nianjian
- CAY
provider: China Agricultural Yearbook Editorial Committee (中国农业年鉴编辑委员会); Agricultural Press (农业出版社) and later China Agriculture Press (中国农业出版社)
china_related: true
domains:
- agriculture
- rural
- regional
- development
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed annual agricultural statistical yearbook volumes for 1981-1994 containing national and regional agricultural/rural indicators; Jin and Qian use selected tables as inputs rather than a released copy of their final provincial panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: "The current CiNii series record identifies 中国农业年鉴 as an annual Agricultural Press series spanning 1980 through 2022, with the editorial committee noted in the colophon and 68 listed holdings. It specifically lists holdings covering all 1981-1994 paper-era volumes, so a researcher can select a complete holding, request the needed volumes, inspect rural-revenue, income, land and population tables, and transcribe them with page-level provenance. No open machine-readable release or licence for the exact 1981-1994 tables is verified."
  barrier: "The yearbook is a broad annual publication, not one stable panel: table contents, units and reference-year conventions vary by issue. Library access establishes a realistic consultation route, not scan or redistribution rights. Third-party Excel/PDF listings remain discovery leads only and do not prove exact paper-era tables or reuse rights."

# Identity and Coverage
unit_of_observation: National, provincial or other regional agricultural/rural statistical entry; exact grain varies by volume and table
structure: Annual historical aggregate tables and narrative/statistical sections
geo_granularity:
- national aggregate
- province/region where reported
- table-specific local aggregates where present
geography: Mainland Chinese agricultural and rural economy represented in the annual issues; province and indicator coverage must be checked table by table
time_span:
  start: '1981'
  end: '1994'
  last_confirmed_release: '1995'
  coverage_note: The QJE bibliography identifies CAY annual issues for 1981-1994. CiNii confirms the continuous annual series and holdings spanning the period; publication year and reference year may differ, and the exact issue-to-table mapping used by the paper remains to be inspected.
  last_checked: '2026-09-28'
frequency:
- annual issue
- table-specific annual series
sample_size: Not a microdata sample; reported national/regional aggregates vary by table
key_variables:
- Rural taxes and fees and rural net-income measures
- Community-government revenue and retained township-enterprise profits where reported
- Cultivated land and rural-population denominators
- Agricultural price or other deflator inputs where reported
- Broader agricultural production, investment and rural social indicators in the yearbook, subject to table-level verification

# Research routing
research_fit:
  best_for:
  - Historical provincial agricultural and rural-economy controls when the question needs an agriculture-specific source rather than a general macro yearbook
  - Reconstructing the CAY component behind Jin and Qian's rural-enterprise/income panel
  - Cross-checking rural revenue, land and population measures across annual agricultural publications
  choose_over:
  - Choose CAY over the general China Statistical Yearbook when the needed series is agriculture/rural-specific and the issue's table notes are the relevant source
  - Use the China Rural Statistical Yearbook alongside CAY when rural social-economic survey indicators and rural labor definitions are needed; neither silently replaces the other
  - Use the historical 1949-1986 rural compilation for its earlier source boundary, not as a substitute for CAY's 1987-1994 issues
  not_good_for:
  - Household, farm, worker or firm microdata and identifiers
  - A guaranteed balanced province-year panel or a current agricultural series
  - Treating all CAY issues as definition-compatible without comparing table notes and accounting revisions
  - Assuming a third-party spreadsheet or later English edition contains the paper's exact input tables
  needs_join_for:
  - Township-enterprise employment/output and deflators from CTESY
  - Rural labor, cultivated land and responsibility-system measures from CRSY
  - State output, CPI and broad macro controls from the China Statistical Yearbook
  - Household, firm or census outcomes from a separate data asset
  variation_available:
  - Annual and regional dimensions only; this record makes no policy-treatment or causal-variation claim
  topics:
  - agricultural production
  - rural income and fees
  - land and population
  - rural industrialization
  - regional development

good_for:
- Manual reconstruction or validation of historical provincial agricultural/rural aggregates
- Documenting the agriculture-source boundary in the Jin and Qian QJE panel
- Comparing agriculture-specific measures across regions while retaining issue and table definitions
identification:
- This annual statistical source is descriptive and does not itself encode a causal design or a verified treatment-assignment rule.
- Annual and regional differences in its tables require separate design evidence; they are not classified here as exogenous variation.
linkable_keys:
- Province or historical region label
- Year, issue year and reference year
- Indicator, unit and table/page number
- Rural-sector or revenue category
- Researcher-built historical province concordance where needed

joins:
  - target: china-township-enterprises-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year/reference year
    - Rural-enterprise or agricultural indicator
    method: Use CAY for agriculture/rural revenue, land and population inputs and CTESY for township-enterprise activity; preserve issue, table and unit definitions instead of blending similarly named aggregates.
    evidence_status: literature-used
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Indicator and unit
    method: Use the general Statistical Yearbook for broad macro, state-industry, price and population cross-checks, recording any revisions or definition breaks.
    evidence_status: literature-used
  - target: china-rural-economic-statistics-1949-1986
    relation: predecessor
    keys:
    - Province or region
    - Year
    - Agricultural/rural indicator
    method: Use the 1949-1986 compilation only for earlier historical context and overlapping table checks; it does not replace the 1981-1994 CAY issues.
    evidence_status: plausible

access_routes:
  - route: CiNii Books library and interlibrary-loan route
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/AN10188735
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Confirmation of the requested issue, publisher and reference year
    steps:
    - Search NCID AN10188735 and select a current listed holding that covers the needed 1981-1994 volumes
    - Confirm title page, editorial committee, publisher imprint, issue year and table of contents
    - Request only the needed rural/revenue/land/population pages under the holding library's rules
    - Transcribe values with issue, table, page, unit, footnotes and missing-value codes
    deliverable: Physical volume, permitted scan or researcher-transcribed tables; no public machine-readable CAY panel was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: Current CiNii metadata identifies 68 holdings and lists several full or near-full paper-era runs, but local access, scan permission and table-level coverage still depend on the institution.
  - route: Institutional Chinese yearbook full-text database
    access_status: needs-verification
    direct_url: https://lib.uibe.edu.cn/zy/sjk/dzs/33820.htm
    requirements:
    - University or library subscription and permitted on-campus/VPN access
    - Provider reader/export terms
    steps:
    - Check whether the subscribed yearbook collection includes 中国农业年鉴 for 1981-1994
    - Compare the digital volume's title page and table images with the paper-era issue needed
    - Record any export or copy restrictions before transcribing
    deliverable: Licensed page images or permitted table extraction, not an open data download
    cost: paid
    last_checked: '2026-08-12'
    caveat: The checked UIBE page documents a selected Chinese yearbook database but does not list CAY in the excerpted collection; verify current module coverage before relying on it.
  - route: Third-party spreadsheet/PDF listing (unverified digital lead)
    access_status: needs-verification
    direct_url: https://www.shujuku.org/china-agriculture-yearbook.html
    requirements:
    - Verify file provenance, exact issue, payment and reuse permission
    - Compare delivered tables with a library volume and the QJE source citation
    steps:
    - Use the listing of 1990 and 1994 Excel files only to locate a possible digital copy
    - Do not treat its fee or delivery as an open-data licence or as proof of the paper's exact source tables
    deliverable: Possible spreadsheet subject to provider terms; not accepted as a rights-cleared canonical route
    cost: mixed
    last_checked: '2026-08-12'
    caveat: The page says it charges for整理/data maintenance; its provenance and redistribution rights remain unverified.

access:
  url: https://ci.nii.ac.jp/ncid/AN10188735
  cost: mixed
  license: Printed-volume copyright, library/document-delivery terms or institutional database terms; no open-data licence for the exact paper-era tables was identified
  format:
  - printed Chinese volume
  - licensed page images
  - researcher-transcribed aggregate table
  api: false
  how_to_get: Start with the CiNii series record and a holding library, verify the exact 1981-1994 issue and reference year, then transcribe only the tables needed with page-level provenance. Keep any derived panel separate from the source volumes.

caveats:
- CAY is a broad annual agriculture publication; the QJE paper uses selected tables, not the entire book or a ready-made panel.
- Publication year and reference year, publisher imprint and accounting definitions may vary across issues; record the title page and table notes.
- Rural taxes/fees, community-government revenue, retained TVE profits, land and population must remain distinct variables with their source tables; similar labels in CRSY or CSY are not automatic substitutes.
- The source does not establish county, household, farm, worker or firm identifiers and does not create a policy or causal-variation record.
- Third-party Excel/PDF listings and the 1995 English bibliographic record are discovery aids, not evidence of a reproducible or redistributable paper-era dataset.

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
    dataset_role: Agriculture/rural-income, fees, land, population and deflator component of a provincial rural-enterprise panel
    evidence_type: data_appendix
    evidence_url: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    data_note: The paper's Appendix Table I and bibliography identify CAY 1981-1994 annual issues for rural taxes/fees, rural net income, community-government revenue and retained TVE profits, cultivated land/rural population and deflator inputs. These source tables remain distinct from the paper's final cleaned panel and from CRSY/CTESY.

provenance:
  - source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
    field_scope:
    - QJE article identity and provincial rural-enterprise study
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    field_scope:
    - CAY exact source name and 1981-1994 annual issue range
    - bibliography source-family identity
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - Appendix Table I rural taxes/fees, income, land, population and deflator roles
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://ci.nii.ac.jp/ncid/AN10188735
    field_scope:
    - Chinese title, editorial committee, annual series, publisher changes and historical library holdings
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/AN10188735
    field_scope:
    - Current annual-series identity, 1980-2022 run, editorial-colophon note, publisher transition and 68 listed holdings
    - Concrete library holdings covering the complete 1981-1994 paper-era run
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://openlibrary.org/books/OL22420251M/China_Agriculture_Yearbook
    field_scope:
    - Corroborating 1995 English-edition bibliographic metadata and library-discovery route only
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://www.shujuku.org/china-agriculture-yearbook.html
    field_scope:
    - Third-party 1990/1994 spreadsheet listing and stated paid-maintenance caveat only
    added: '2026-08-12'
    confidence: med
    verified: true

related_datasets:
  - id: china-township-enterprises-statistical-yearbook
    relation: complement
  - id: china-stat-yearbook
    relation: complement
  - id: china-rural-economic-statistics-1949-1986
    relation: predecessor
---

## Positioning in one sentence

This is the agriculture-specific annual source behind the CAY component of Jin and Qian's rural panel: its distinctive value is rural revenue, land, population and agricultural-accounting detail, while its practical route is manual, issue-by-issue extraction from a specifically identifiable library-held series rather than a stable downloadable panel.

## Select rules

- Prioritize it when a historical regional question needs agriculture/rural-specific tax, income, land or population tables and the issue's source notes matter.
- Pair it with CTESY for township-enterprise activity, CRSY for rural social-economic measures and the China Statistical Yearbook for broad macro cross-checks.
- Use the 1949-1986 rural compilation for the earlier historical source boundary; use modern agricultural databases for current series only after checking comparability.
- Do not promise exact reproduction until the needed 1981-1994 issue and table pages are obtained.

## Get recipe

1. Search CiNii NCID `AN10188735` and choose a listed holding with the needed 1981-1994 volume range.
2. Verify title page, editorial committee, publisher, issue year, reference year and table of contents.
3. Identify the rural revenue, income, land, population and deflator tables before extraction; record page, unit, footnotes and missing-value codes.
4. Cross-check overlaps with CRSY and the China Statistical Yearbook while preserving every source edition and definition.
5. Keep any derived province-year panel separate from the yearbook and document all transformations.

## Connections and Limitations

The safest join is province or historical region by reference year plus indicator and unit. CTESY supplies township-enterprise measures; CRSY and CSY supply complementary rural and macro denominators. The record does not provide micro identifiers, a guaranteed balanced panel or an open digital licence. If the table or definition cannot be reconciled, preserve the gap or switch to a clearly labeled alternative instead of inferring values.

## Decision sufficiency check

For a researcher studying 1990s rural industrialization and regional income, this record selects CAY for agriculture/rural revenue, land and population inputs, CTESY for enterprise activity and CRFSY for rural finance. It gives a concrete library-first acquisition route, identifies the closest substitutes, and states the issue/table and reuse conditions that would invalidate the recommendation. It is ready for page-provenanced consultation and extraction, not for claiming a digital panel, a complete machine-readable series, or unrestricted redistribution.
