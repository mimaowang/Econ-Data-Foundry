---
schema_version: 3
catalog_status: ready
id: china-rural-finance-statistical-yearbook
name: China Rural Finance Statistical Yearbook, 1989-1994 (中国农村金融统计年鉴)
aka:
- 中国农村金融统计年鉴
- China Rural Finance Statistical Yearbook
- Zhongguo nongcun jinrong tongji nianjian
- CRFSY
provider: Agricultural Bank of China (中国农业银行) as the listed compiler; China Statistical Press (中国统计出版社) as publisher
china_related: true
domains:
- rural
- regional
- finance
- development
- firm

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed or licensed annual statistical yearbook volumes covering Agricultural Bank of China and Rural Credit Cooperative rural-finance aggregates; Jin and Qian use the source tables rather than a released copy of their final provincial panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The title, compiler, publisher and historical volumes are grounded by current
    library records, and an institutional Fangzheng yearbook page lists this title
    for 1979-1996 under authenticated access. A researcher can select the
    Agricultural Bank/Rural Credit Cooperative source family, request or open a
    permitted volume, locate the province/reference-year table, and transcribe the
    needed rural-enterprise-loan or household-savings cells with page provenance.
    This is a ready route to the source tables, not a release of Jin and Qian's
    cleaned provincial panel.
  barrier: >-
    Library membership, interlibrary loan, document delivery, or an institutional
    database entitlement is required. The exact table/page and issue-year versus
    reference-year mapping must be checked in the authorized copy; the unresolved
    1994 extension and the paper's final cleaned panel are not represented as
    delivered data.

# Identity and Coverage
unit_of_observation: National, provincial, autonomous-region, planned-city or institution-level rural-finance statistical entry; exact grain varies by table and volume
structure: Annual historical aggregate tables for agricultural-bank and rural-credit-cooperative finance
geo_granularity:
- national aggregate
- province/autonomous region/municipality where reported
- planned city or branch-level aggregate where reported
geography: Mainland Chinese Agricultural Bank of China and Rural Credit Cooperative system represented in the annual volumes; provincial coverage and table definitions must be checked volume by volume
time_span:
  start: '1989'
  end: '1994'
  last_confirmed_release: '1996'
  coverage_note: >-
    The QJE bibliography identifies CRFSY annual issues for 1989-1994, while the
    paper's Appendix Table I uses 1989-1993 for rural-enterprise loans and rural
    household savings. A catalogued 1995 issue is described as containing 1994
    data, so the apparent 1994 gap is a publication-year/reference-year mismatch,
    not evidence that a 1994-reference-year volume was absent. Table/page contents
    still require an authorized volume check.
  last_checked: '2026-09-28'
frequency:
- annual issue
- table-specific annual series
sample_size: Not a microdata sample; coverage is the set of reporting institutions and regions in each volume/table
key_variables:
- Rural-enterprise loan balances or loan totals from the Agricultural Bank of China and Rural Credit Cooperatives
- Rural household savings/deposit measures
- Rural-finance branch, institution, personnel, cash and interest tables where present
- National and regional rural-economic benchmark indicators included in the yearbook, which should remain source-labeled

# Research routing
research_fit:
  best_for:
  - Historical provincial or regional rural-credit supply and rural-enterprise finance measures
  - Reconstructing the CRFSY component behind Jin and Qian's 1998 QJE rural-enterprise panel
  - Checking whether a rural-finance series is bank/credit-cooperative specific rather than a general macro aggregate
  choose_over:
  - Choose CRFSY over the general China Statistical Yearbook when the research needs Agricultural Bank/Rural Credit Cooperative loans, deposits or branch statistics
  - Pair it with the Township Enterprises Statistical Yearbook when the question links rural-enterprise finance to employment/output, keeping both source identities visible
  - Use a current banking database or micro loan records only when current identifiers, account-level outcomes or institution-level panels are required
  not_good_for:
  - Household, farm, firm or loan-account microdata and borrower identifiers
  - A guaranteed balanced province-year panel or a current rural-finance series
  - Treating the yearbook's benchmark macro tables as a substitute for the China Statistical Yearbook or rural survey source
  - Assuming a later China Rural Finance Almanac/Yearbook has identical historical definitions without checking the volume
  needs_join_for:
  - Township-enterprise employment/output categories from CTESY
  - Population, rural labor and land denominators from CRSY or census/yearbook sources
  - General state-enterprise output, CPI and macro controls from the China Statistical Yearbook
  - Household or firm outcomes from a separate microdata asset
  variation_available:
  - Annual and regional dimensions only; this record makes no policy-treatment or causal-variation claim
  topics:
  - rural finance
  - agricultural banking
  - rural credit cooperatives
  - township-enterprise finance
  - regional development

good_for:
- Manual reconstruction or validation of historical rural-enterprise loan and household-savings aggregates
- Documenting the finance-source boundary in the Jin and Qian QJE panel
- Comparing rural-credit indicators across provinces while preserving bank/credit-cooperative and yearbook definitions
identification:
- >-
  Identify the source volume by its Chinese title 中国农村金融统计年鉴, China
  Agricultural Bank compiler, China Statistical Press publisher, and the intended
  issue/reference year. Within a permitted volume, identify the needed table by
  its Agricultural Bank or Rural Credit Cooperative institution label, indicator,
  unit, province/region headings, table title and page. This source-table route
  is not the same artifact as Jin and Qian's cleaned provincial analysis panel,
  a later rural-finance yearbook, or a general macro-finance table with a similar
  label.
linkable_keys:
- Province/autonomous-region/municipality or planned-city label
- Year, issue year and reference year
- Institution type (Agricultural Bank or Rural Credit Cooperative)
- Indicator, unit and table/page number
- Historical regional-label concordance where necessary

joins:
  - target: china-township-enterprises-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year/reference year
    - Rural-enterprise category
    method: Join CRFSY loan/savings measures to CTESY employment/output categories only after aligning issue/reference years and preserving each source's enterprise and institution definitions.
    evidence_status: literature-used
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Indicator and unit
    method: Use the general Statistical Yearbook for population, prices and broad macro controls; do not replace CRFSY bank-specific measures with a similar-sounding aggregate finance table.
    evidence_status: literature-used

access_routes:
  - route: CiNii Books library and interlibrary-loan route
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/BA3743840X
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Verification of the requested volume and reference year
    steps:
    - Search NCID BA3743840X and ISBNs listed for the 1991-1996 volumes
    - Ask a holding library for the 1989-1994 reference-year source family, including the 1995 issue that is described as containing 1994 data
    - Confirm title page, compiler, publisher, issue year and tables before requesting pages
    - Transcribe only the needed provincial/region cells with table, unit and footnote provenance
    deliverable: Physical volume, permitted scan or researcher-transcribed tables; no open machine-readable panel was verified
    cost: mixed
    last_checked: '2026-08-12'
    caveat: CiNii currently identifies the title/compiler/publisher, lists 1991, 1992, 1993, 1995 and 1996 issues, and shows multiple university holdings. It does not guarantee a scan, interlibrary loan or redistribution permission.
  - route: Institutional Fangzheng Yearbook and Reference Library
    access_status: available-with-conditions
    direct_url: https://lib.uibe.edu.cn/zy/sjk/dzs/33820.htm
    requirements:
    - University or library subscription and permitted on-campus/VPN access
    - Apabi/Fangzheng reader or the provider's current access method
    steps:
    - Confirm that the subscribed China Yearbook Full-text Database exposes 中国农村金融统计年鉴 and the 1979-1996 range advertised by the library
    - Search the relevant volume and export or transcribe only within the subscription terms
    - Record volume, table, page/image and any export restrictions; do not treat the database listing as an open licence
    deliverable: On-platform book images or permitted table extraction, not a public bulk download
    cost: paid
    last_checked: '2026-09-28'
    caveat: The current library page lists 中国农村金融统计年鉴 for 1979-1996 and states that the database is authenticated by campus IP or remote access. It documents a licensed reading route, not unrestricted export or a right to redistribute extracted pages.
  - route: Google Books digitized bibliographic/snippet record
    access_status: needs-verification
    direct_url: https://books.google.com/books/about/%E4%B8%AD%E5%9B%BD%E5%86%9C%E6%9D%91%E9%87%91%E8%9E%8D%E7%BB%9F%E8%AE%A1%E5%B9%B4%E9%89%B4.html?id=X4gwAAAAMAAJ
    requirements:
    - Check whether the needed pages are available in the current snippet view or through a holding library
    steps:
    - Use the 1991 record to corroborate title, Agricultural Bank contributor, publisher and table vocabulary
    - Follow the listed 1993/1995 editions or library links where available
    - Do not infer full-text access or reuse rights from the digitization metadata
    deliverable: Bibliographic metadata and limited snippets; not accepted as the paper's downloadable panel
    cost: registration
    last_checked: '2026-08-12'
    caveat: Google Books states the item was digitized from the University of Michigan but provides no open-data licence and may show only snippets.

access:
  url: https://ci.nii.ac.jp/ncid/BA3743840X
  cost: mixed
  license: Printed-volume copyright, library/document-delivery terms or institutional database terms; no open-data licence for the exact paper-era tables was identified
  format:
  - printed Chinese volume
  - licensed page images
  - researcher-transcribed aggregate table
  api: false
  how_to_get: Start with the CiNii record or an institutional yearbook database, verify the exact issue and reference year, and transcribe only the bank/credit-cooperative tables needed with page-level provenance. Keep any reconstructed panel separate from the source volumes.

caveats:
- The paper names CRFSY annual issues 1989-1994, but the Appendix Table I reports 1989-1993 for the loan and savings inputs; do not fill the final year from a later publication without recording the source.
- The 1995 issue is described as covering 1994 data; still verify the exact table and whether the QJE bibliography's year denotes reference year or volume label before extraction.
- The yearbook is an aggregate financial source, not borrower-level microdata, a firm registry or a causal treatment file.
- Rural-enterprise loans, rural household savings, Agricultural Bank figures and Rural Credit Cooperative figures must remain distinguishable; similar labels in general financial yearbooks are not automatic substitutes.
- Publication year, reference year, accounting definitions and reporting coverage may change across volumes and require table-note checks.

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
    dataset_role: Rural-enterprise loan and rural-household-savings component of a provincial rural-enterprise panel
    evidence_type: data_appendix
    evidence_url: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    data_note: The paper's Appendix Table I and bibliography identify CRFSY 1989-1994 annual issues; the reported loan and savings inputs cover 1989-1993 and distinguish Agricultural Bank/Rural Credit Cooperative rural-enterprise loans from rural household savings. The source volumes are not the paper's final cleaned panel.

provenance:
  - source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
    field_scope:
    - QJE article identity and provincial rural-enterprise study
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    field_scope:
    - CRFSY exact source name and 1989-1994 annual issue range
    - bibliography publisher and source-family identity
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - Appendix Table I rural-enterprise loan and household-savings roles
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BA3743840X
    field_scope:
    - Chinese title, Agricultural Bank compiler, China Statistical Press, historical volumes, ISBNs and library holdings
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://books.google.com/books/about/%E4%B8%AD%E5%9B%BD%E5%86%9C%E6%9D%91%E9%87%91%E8%9E%8D%E7%BB%9F%E8%AE%A1%E5%B9%B4%E9%89%B4.html?id=X4gwAAAAMAAJ
    field_scope:
    - 1991 bibliographic metadata, contributor/publisher and snippet vocabulary for loans, deposits and rural-enterprise finance
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://lib.uibe.edu.cn/zy/sjk/dzs/33820.htm
    field_scope:
    - Institutional Fangzheng yearbook database route and advertised 1979-1996 collection range
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://www.nianjiandata.com/books-zhongguo-nongcunjinrong-tongjinianjian.html
    field_scope:
    - bibliographic/content-year mapping: 1995 issue described as containing 1994 data
    - 1991, 1992, 1993 and 1995 issue labels shown with their corresponding content years
    - boundary: third-party page is not used as an authorized download, licensing, or table-content source
    added: '2026-09-28'
    confidence: medium
    verified: true
  - source: CiNii Books NCID BA3743840X and UIBE Fangzheng Yearbook Library page (read 2026-09-28)
    field_scope:
    - CiNii title, China Agricultural Bank compiler, China Statistical Press publisher, issue labels and multiple holdings
    - authenticated library route and advertised 1979-1996 coverage for this exact title
    - boundary: this supports source-volume acquisition, not a public machine-readable panel or the paper's final file
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

This is the historical aggregate rural-finance source behind Jin and Qian's loan and savings inputs: its distinctive value is the separation of Agricultural Bank/Rural Credit Cooperative and rural-enterprise finance measures, while the practical barrier is locating the exact annual volumes and preserving their reference-year and reporting definitions.

## Select rules

- Prioritize it when a regional rural-development question needs historical rural-enterprise loans, deposits or credit-cooperative coverage rather than a generic fiscal or macro-finance total.
- Pair it with CTESY for rural-enterprise employment/output and with the China Statistical Yearbook for population, price and broad macro denominators; do not collapse these products.
- Use a current banking database or micro survey when the research needs account-level, borrower-level or institution-identifier data.
- Do not claim exact reproduction until the 1989-1994 issue/table mapping and any 1994 gap are resolved.

## Get recipe

1. Search CiNii by NCID `BA3743840X` and the listed ISBNs, or use an institutional Fangzheng yearbook subscription.
2. Request the relevant 1989-1994 reference-year volumes and verify title page, compiler, publisher, issue year and reference year; specifically inspect the 1995 issue for the 1994 tables.
3. Identify the rural-enterprise loan and household-savings tables before extraction, recording bank/cooperative category, province, unit, table and page.
4. Cross-check overlapping totals with the paper appendix and general yearbooks without silently replacing the source.
5. Keep the transcribed or reconstructed panel separate from the printed/licensed volumes and document any missing years or definition changes.

## Connections and Limitations

The safest join is province or region by reference year, with institution type and indicator retained. CTESY supplies the rural-enterprise activity side; the general Statistical Yearbook supplies denominators and macro controls. The record does not provide borrowers, firms, loan accounts or causal treatment dates. If the exact volume/table cannot be obtained or the reference-year definitions cannot be reconciled, the researcher should preserve the gap or switch to a clearly labeled alternative rather than infer the missing series.

## Decision sufficiency check

For a researcher studying whether historical rural credit tracked township-enterprise expansion, this record selects CRFSY for the bank/cooperative loan and savings measures, CTESY for enterprise activity and the Statistical Yearbook for denominators. It gives a concrete library or authenticated-database start, requires table/page/reference-year provenance, and keeps the 1994 extension and paper-cleaned panel outside the delivered route; this bounded source-table route is ready.
