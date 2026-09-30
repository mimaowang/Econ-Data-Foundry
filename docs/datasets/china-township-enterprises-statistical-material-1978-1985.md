---
schema_version: 3
catalog_status: grounding
id: china-township-enterprises-statistical-material-1978-1985
name: Township Enterprises Statistical Material 1978-1985 (TESM, 1986 issue)
aka:
- 乡镇企业统计资料
- Township Enterprises Statistical Material 1978-1985
- (全国)乡镇企业简明统计史料汇编 1978-1985 (related/reprinted title)
- TESM
provider: Ministry of Agriculture of the People's Republic of China (中华人民共和国农业部) as cited by Jin and Qian; the historical bureau/editor title and original imprint require title-page verification
china_related: true
domains:
- rural
- regional
- development
- firm
- labor

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed historical statistical material for 1978-1985, issued as a 1986 volume, containing aggregate township-enterprise indicators; Jin and Qian use selected 1986 and 1980 inputs rather than a released copy of their final provincial panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: "The QJE appendix identifies TESM 1986 as the source for 1986 TVE employment/output figures and collective fixed assets in 1980. A Google Books record identifies a 2022 reprint under the related title 乡镇企业系列之一: 1978-1985年, edited by the Ministry of Agriculture and Animal Husbandry Township Enterprises Bureau; the National Diet Library catalogs a separate 1978-2002 compilation by the Ministry's Township Enterprises Bureau. A researcher can use library or reprint leads to locate the historical tables and transcribe them with page-level provenance, but no open machine-readable copy of the exact 1986 source was verified."
  barrier: "The paper's English citation gives TESM 1978-1985, Beijing: Ministry of Agriculture, 1986, while the accessible Google Books item is a 2022 reprint with a different Chinese title and compiler/publisher. The original title page, exact table contents, regional coverage, units and whether the reprint is lossless remain to be checked. The later 1978-2002 compilation is a fallback, not proof that it reproduces the paper's source tables."

# Identity and Coverage
unit_of_observation: National, provincial or other regional township-enterprise aggregate; exact grain varies by historical table
structure: Historical aggregate statistical tables and source notes for township/rural enterprises
geo_granularity:
- national aggregate where reported
- province or region where reported
- table-specific local aggregates if present
geography: Mainland Chinese township and rural enterprises represented in the 1978-1985 historical material; exact province coverage must be checked from the source tables
time_span:
  start: '1978'
  end: '1985'
  last_confirmed_release: '1986'
  coverage_note: The paper cites TESM 1978-1985 (1986) and separately TESM 1986 (1987). Its Appendix Table I uses the TESM 1986 issue for 1986 employment/output shares and 1980 collective fixed assets; this record covers the 1978-1985 source volume and does not silently include the separate 1986 issue.
  last_checked: '2026-08-12'
frequency:
- historical compilation
- table-specific annual series
sample_size: Not a microdata sample; counts and regional coverage vary by table
key_variables:
- Collective fixed assets in 1980, used as the initial collective-assets measure
- TVE employment and output figures for 1986 as reported in the TESM 1986 issue
- Enterprise-category, employment, output and asset aggregates where the historical tables report them
- Table units, province/region labels and reference-year notes needed to compare TESM with later CTESY issues

# Research routing
research_fit:
  best_for:
  - Early-reform baseline measures of township-enterprise collective assets and 1986 TVE employment/output
  - Reconstructing the historical TESM component behind Jin and Qian's 1998 QJE provincial analysis
  - Establishing an initial rural-industrialization level before using later annual CTESY data
  choose_over:
  - Choose TESM over CTESY when the research needs the paper's 1980 initial collective-assets measure or 1986 baseline figures
  - Use CTESY for later annual TVE/private-enterprise employment and output, after checking category definitions and issue years
  - Use the 1978-2002 statistical compilation only as a fallback when its tables and units match; it is not the exact paper-era volume
  not_good_for:
  - A complete annual 1978-1994 province-year panel without additional sources
  - Firm, household or worker microdata, identifiers or longitudinal tracking
  - Assuming that the 2022 reprint or 2003 compilation has the same tables, corrections or definitions as TESM 1986
  - Treating initial collective assets as a policy treatment or causal-variation record
  needs_join_for:
  - Later TVE/private-enterprise employment and output from the China Township Enterprises Statistical Yearbook
  - Rural population denominators from the China Agricultural Yearbook or rural statistical sources
  - Rural labor, land and non-farm indicators from the China Rural Statistical Yearbook
  - Prices, state-industry output and broad controls from the China Statistical Yearbook
  variation_available:
  - Historical baseline and regional dimensions only; this record makes no policy-treatment or causal-variation claim
  topics:
  - township and village enterprises
  - rural industrialization
  - collective assets
  - regional development

good_for:
- Manual reconstruction or validation of the early collective-assets baseline used in the QJE paper
- Checking the handoff from TESM 1986 to CTESY 1987-1994
- Preserving the difference between a historical source volume and the paper's derived province-year variables
identification: []
linkable_keys:
- Province or historical region label
- Reference year and source/issue year
- Enterprise category and ownership label
- Indicator, unit and table/page number
- Historical region concordance where labels changed

joins:
  - target: china-township-enterprises-statistical-yearbook
    relation: successor/complement
    keys:
    - Province or region
    - Year
    - Enterprise category, indicator and unit
    method: Use TESM for the 1980/1986 baseline and CTESY for later annual measures only after comparing category definitions, issue/reference years and province coverage. Keep the source edition visible in every derived panel.
    evidence_status: literature-used
  - target: china-agricultural-yearbook
    relation: complement
    keys:
    - Province or region
    - Year/reference year
    - Rural population and asset indicator
    method: Use the agricultural yearbook or another explicitly verified source for rural-population denominators; do not infer denominators from the TESM title or reprint metadata.
    evidence_status: literature-used

access_routes:
  - route: Google Books related reprint and library-finder route
    access_status: needs-verification
    direct_url: https://books.google.com/books/about/%E4%B9%A1%E9%95%87%E4%BC%81%E4%B8%9A%E7%B3%BB%E5%88%97%E4%B9%8B%E4%B8%80.html?id=3kdrzwEACAAJ
    requirements:
    - Locate a holding or seller for the 2022 reprint
    - Compare its title page, editor, table of contents and pagination with TESM 1986
    - Confirm copying and reuse terms before extracting or redistributing pages
    steps:
    - Search the record for 乡镇企业系列之一: 1978-1985年 and use Find in a library or seller links
    - Inspect the reprint's source statement and identify whether it reproduces the 1986 Ministry of Agriculture material
    - Extract only after matching the needed collective-assets and 1986 employment/output tables
    deliverable: Possible reprint volume or permitted scan; not accepted as an exact original or open machine-readable dataset
    cost: mixed
    last_checked: '2026-08-12'
    caveat: Google Books identifies the item as a 2022 reprint compiled by the Chinese Publications Service Center; it does not prove lossless reproduction, public access or reuse permission.
  - route: National Diet Library 1978-2002 statistical-compilation fallback
    access_status: available-with-conditions
    direct_url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia1000045529
    requirements:
    - Library membership or document-delivery access
    - Table-level comparison with the original TESM citation before use
    steps:
    - Request 中国乡镇企业统计资料: 1978-2002年, DT363-C3, from a library or the listed holding
    - Inspect whether the 1978-1985 and 1980 collective-assets tables reproduce the required categories and units
    - Record that the copy is a 2003 compilation by the Ministry's Township Enterprises Bureau, not TESM 1986
    deliverable: Physical 2003 compilation or permitted scan; a related fallback table set, not the paper's exact source volume
    cost: mixed
    last_checked: '2026-08-12'
    caveat: The NDL record identifies a 416-page 2003 compilation priced at 180 yuan and does not establish that every TESM table or the paper's derived variables are reproduced.
  - route: Historical source citation in the QJE appendix
    access_status: needs-verification
    direct_url: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    requirements:
    - Use the citation to identify the original 1986 volume, not as evidence of a downloadable file
    steps:
    - Confirm the TESM 1978-1985 and TESM 1986 bibliography entries and Appendix Table I roles
    - Use the title, issuing body and year to query library catalogues or archive services
    - Keep paper-derived province-year variables separate from the source volume
    deliverable: Bibliographic and paper-use evidence only
    cost: mixed
    last_checked: '2026-08-12'
    caveat: The hosted appendix establishes paper use and source identity but does not itself provide the historical data file or rights to reproduce it.

access:
  url: https://books.google.com/books/about/%E4%B9%A1%E9%95%87%E4%BC%81%E4%B8%9A%E7%B3%BB%E5%88%97%E4%B9%8B%E4%B8%80.html?id=3kdrzwEACAAJ
  cost: mixed
  license: Printed/reprint copyright, library/document-delivery terms or seller terms; no open-data licence for the original 1986 tables was identified
  format:
  - printed historical volume
  - permitted library scan
  - researcher-transcribed aggregate table
  api: false
  how_to_get: Start with the reprint and NDL fallback records, verify the exact original/reprint relationship and table definitions, then transcribe only the 1980 and 1986 inputs needed for the intended research. Keep any derived panel separate from the source volume.

caveats:
- The paper cites TESM 1978-1985 (Beijing: Ministry of Agriculture, 1986) and a separate TESM 1986 (1987); do not combine these volumes or treat CTESY 1987 as an automatic replacement.
- The QJE Appendix Table I explicitly uses TESM 1986 for 1986 employment/output shares and for collective fixed assets in 1980; it does not prove that every table in TESM 1978-1985 is used.
- The 2022 reprint and 2003 compilation are acquisition leads or fallbacks, not evidence of an identical original table set.
- Historical enterprise categories, province labels, units and reference-year conventions require page-level checks.
- Initial collective assets are a baseline variable in the paper, not a policy or causal-variation record.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-12'

used_by:
  - cite: 'Jin & Qian (1998), Public Versus Private Ownership of Firms: Evidence from Rural China'
    doi: https://doi.org/10.1162/003355398555748
    journal: QJE
    year: 1998
    dataset_role: Initial collective-assets and 1986 TVE employment/output component of a provincial rural-enterprise panel
    evidence_type: data_appendix
    evidence_url: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    data_note: The Appendix Table I states that 1986 TVE employment/output figures come from TESM 1986 and that collective fixed assets in 1980 come from TESM 1986; later annual figures come from CTESY. The source volume is not the paper's final cleaned panel.

provenance:
  - source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
    field_scope:
    - QJE article identity and provincial rural-enterprise study
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - TESM 1978-1985 and TESM 1986 bibliography entries
    - Appendix Table I 1980 collective-assets and 1986 employment/output roles
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://books.google.com/books/about/%E4%B9%A1%E9%95%87%E4%BC%81%E4%B8%9A%E7%B3%BB%E5%88%97%E4%B9%8B%E4%B8%80.html?id=3kdrzwEACAAJ
    field_scope:
    - 2022 reprint title, Ministry of Agriculture and Animal Husbandry Township Enterprises Bureau editor and reprint publisher
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia1000045529
    field_scope:
    - 2003 1978-2002 related compilation, Ministry Township Enterprises Bureau compiler, physical-library route and price
    added: '2026-08-12'
    confidence: high
    verified: true

related_datasets:
  - id: china-township-enterprises-statistical-yearbook
    relation: successor/complement
  - id: china-agricultural-yearbook
    relation: complement
---

## Positioning in one sentence

This is the early township-enterprise source behind the initial-assets and 1986 TVE measures in Jin and Qian's QJE panel: its value is the historical baseline before the later CTESY series, while the practical barrier is proving that a reprint or later compilation reproduces the exact 1986 tables.

## Select rules

- Prioritize TESM when a study needs the 1980 collective-assets baseline or 1986 TVE employment/output figures used in the QJE paper.
- Switch to CTESY for later annual TVE/private-enterprise measures only after comparing definitions and source years.
- Use the 2003 1978-2002 compilation or 2022 reprint as a fallback/lead, not as an exact substitute without table-level comparison.
- Do not treat the baseline asset measure as a policy shock or variation record.

## Get recipe

1. Start with the 2022 reprint record and the NDL 2003 compilation to locate a physical or permitted copy.
2. Compare the title page, issuing body, edition, table of contents and source notes with the TESM 1986 citation.
3. Locate the collective-fixed-assets-in-1980 and 1986 TVE employment/output tables, recording units, province labels and pages.
4. Join to CTESY only after checking categories and reference years; keep each source edition visible.
5. Keep the resulting province-year variables in a separate reconstruction file and document any reprint or compilation differences.

## Connections and Limitations

The safest join is province or region plus reference year, enterprise category, indicator and source edition. CAY or another verified rural-population source supplies denominators; CTESY supplies later annual activity. TESM provides no firm identifiers, worker microdata or causal treatment timing. If the exact 1986 tables cannot be obtained or the reprint is not demonstrably equivalent, preserve the gap instead of silently substituting a later yearbook.

## Decision sufficiency check

For a researcher studying how early collective capacity relates to later rural industrialization, this record selects TESM for the initial 1980/1986 measures and CTESY for later years, gives two realistic library/reprint starting points, and identifies the reprint-equivalence test that can invalidate the recommendation. It remains grounding rather than ready because the exact original volume and table-level equivalence are not yet verified.
