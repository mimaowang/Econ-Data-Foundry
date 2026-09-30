---
schema_version: 3
catalog_status: grounding
id: china-township-enterprises-statistical-yearbook
name: China Township Enterprises Statistical Yearbook, 1987-1994 (中国乡镇企业统计年鉴)
aka:
- 中国乡镇企业统计年鉴
- China Township Enterprises Statistical Yearbook
- 中国乡镇企业年鉴
- China Township and Village Enterprises Yearbook
- CTESY
provider: China Township Enterprises Yearbook Editorial Committee (中国乡镇企业年鉴编辑委员会); the current National Diet Library parent catalogue lists China Agricultural Press (中国农业出版社) for its related 1990-2006 series, while the paper's exact 1987-1989 source volumes and title-page publisher still need verification
china_related: true
domains:
- rural
- regional
- development
- firm
- labor
- urban

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed annual statistical yearbook issues for 1987-1994 containing aggregate township/rural-enterprise employment, output and related indicators; Jin and Qian use source tables rather than a released copy of their final provincial panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: "The QJE bibliography and appendix identify CTESY as the source family for its township-enterprise inputs. The current National Diet Library parent catalogue establishes a related China Township Enterprises Yearbook sequence, edited by the China Township Enterprises Yearbook Editorial Committee, whose documented holdings begin with 1990 (published 1991.2) and continue to 2006. A researcher can begin a library request for the documented 1990-1994 part of that sequence, then verify title page and tables before transcription. The 1978-2002 NDL compilation remains a distinct fallback. No stable public machine-readable release or open reuse licence for the paper's full 1987-1994 source sequence was verified."
  barrier: The current catalogue closes neither the paper's 1987-1989 source boundary nor the equivalence between its English CTESY citation and the related Chinese-title series. The NDL parent record supports a documented 1990-1994 library starting point, not complete replication of all paper-era inputs. Digital listings and later compilations must not be treated as the paper's source without title-page and table-level confirmation.

# Identity and Coverage
unit_of_observation: National, provincial or other regional aggregate township/rural-enterprise statistical entry; exact grain varies by issue and table
structure: Annual historical aggregate tables with table-dependent enterprise, employment, output and finance measures
geo_granularity:
- national aggregate where reported
- province or region where reported
- table-specific local aggregates if an issue includes them
geography: Mainland Chinese township and rural enterprises represented in the historical issues; province and regional coverage must be checked table by table
time_span:
  start: '1987'
  end: '1994'
  last_confirmed_release: '1995'
  coverage_note: The QJE bibliography identifies CTESY inputs for 1987-1994. The current NDL parent catalogue for the related Chinese-title series documents holdings from 1990 (published 1991.2) through 2006. This gives a concrete 1990-1994 library starting point; it does not establish the paper's 1987-1989 source volumes, whether publication and reference years align, or the exact issue/table mapping.
  last_checked: '2026-09-28'
frequency:
- annual issue
- table-specific annual series
sample_size: Not a microdata sample; counts and coverage vary by table and issue
key_variables:
- Township/rural-enterprise employment and the rural-enterprise employment denominator
- Township-enterprise and private-enterprise employment/output shares
- TVE output-price deflator inputs
- Enterprise counts, gross output and revenue where reported in the statistical tables
- National or regional enterprise indicators in the 1978-2002 statistical compilation, which is a related fallback rather than the annual CTESY asset

# Research routing
research_fit:
  best_for:
  - Historical provincial or regional rural-industrialization measures when the question needs township-enterprise employment, output or ownership categories
  - Reconstructing the CTESY source boundary behind Jin and Qian's 1998 QJE rural-enterprise panel
  - Cross-checking the nonfarm/rural-enterprise component of a regional development series before building a derived panel
  choose_over:
  - Choose this source family over the general China Statistical Yearbook when the indicator is specifically a township-enterprise employment/output or price-deflator measure
  - Use the National Diet Library 1978-2002 statistical compilation as a practical fallback only when its table definitions and years match the research need; it is not the same artifact as the annual issues
  - Use a current firm registry or ASIF when firm-level identifiers and micro outcomes are needed; those products cannot substitute for historical aggregate TVE categories
  not_good_for:
  - Firm, household or worker microdata, firm identifiers, or longitudinal firm tracking
  - A guaranteed balanced province-year panel or a current post-1994 enterprise series
  - Assuming that the later China Township Enterprises Yearbook has identical ownership definitions, table labels or reference-year timing
  - Treating a third-party PDF listing as a rights-cleared download or as proof of the exact paper-used tables
  needs_join_for:
  - Rural labor, cultivated land, population and responsibility-system measures from the China Rural Statistical Yearbook
  - State-enterprise output and rural-price deflators from the China Statistical Yearbook component
  - Population denominators and urban shares from the China Population Yearbook or census products
  - Household or firm outcomes from a separate microdata source
  variation_available:
  - Annual and regional dimensions only; this record does not classify any policy treatment or causal variation
  topics:
  - township and village enterprises
  - rural industrialization
  - nonfarm employment
  - regional development
  - ownership structure

good_for:
- Manual reconstruction or validation of historical aggregate TVE employment/output series
- Documenting the source behind the CTESY component of Jin and Qian (1998 QJE)
- Comparing rural-enterprise measures with general statistical-yearbook aggregates while preserving source-specific definitions
identification: []
linkable_keys:
- Province or historical region label
- Year and issue/reference-year convention
- Enterprise category and ownership label
- Indicator, unit and table/page number
- Researcher-built province concordance when historical labels changed

joins:
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Indicator and unit
    method: Use CTESY for township-enterprise-specific measures and the China Statistical Yearbook for state-enterprise output, CPI or general population denominators. Preserve the issue, table and definition instead of silently blending series.
    evidence_status: literature-used
  - target: china-rural-economic-statistics-1949-1986
    relation: predecessor
    keys:
    - Province or region
    - Year
    - Rural/nonfarm enterprise indicator where present
    method: Use the 1949-1986 rural compilation only for earlier historical context and check overlapping definitions; it does not extend or replace the 1987-1994 CTESY issues.
    evidence_status: plausible

access_routes:
  - route: National Diet Library parent catalogue for the related China Township Enterprises Yearbook series, with documented holdings beginning 1990 (published 1991.2)
    access_status: available-with-conditions
    direct_url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053607
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Confirmation that the requested volume is the historical CTESY issue or a definition-compatible successor
    steps:
    - Open the parent catalogue record Z41-AC47 and request the desired documented 1990-1994 volume through its holding library
    - Ask the holding library to check title page, publisher, issue year and table of contents against the paper's CTESY citation
    - Request only the needed pages under the library's scan and copyright rules
    - Record issue, reference year, table, unit, province coverage and missing-value notes before transcription
    deliverable: Physical volume, permitted scan or researcher-transcribed tables; no open machine-readable CTESY file was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The current parent catalogue establishes a physical/library-held Chinese-title sequence from 1990 (published 1991.2) to 2006. It does not prove the 1987-1989 source volumes, the paper's exact English-title equivalence, table identity, a volume-by-volume publisher history, or a rights-cleared digital file.
  - route: National Diet Library research guide for China Township Enterprises Statistical Materials, 1978-2002
    access_status: available-with-conditions
    direct_url: https://ndlsearch.ndl.go.jp/rnavi/asia/post_97
    requirements:
    - A library or document-delivery service that can locate the DT363-C3 compilation
    - Table-level comparison with the annual CTESY source before use
    steps:
    - Search the guide entry for 中国乡镇企业统计资料: 1978-2002 (中国农业出版社, 2003, DT363-C3)
    - Obtain the compilation and inspect its national/region sections, enterprise categories and reference years
    - Use it only where its definitions and years match the research question, recording that it is a separate compilation
    deliverable: Library copy or permitted scan of a related 1978-2002 statistical compilation, not the paper's annual issue set
    cost: mixed
    last_checked: '2026-08-12'
    caveat: The guide describes enterprise counts, employees, gross output, revenue and foreign-funded enterprises, but it does not establish that the compilation reproduces every CTESY table or the paper's cleaned panel.
  - route: Third-party yearbook database/listing (unverified digital lead)
    access_status: needs-verification
    direct_url: https://www.nianjiandata.com/index.php/books-zhongguo-xiangzhenqiye-nongchanpinjiagongye-nianjian.html
    requirements:
    - Verify file provenance, exact issue title, payment terms and reuse permission
    - Compare a delivered volume with the paper bibliography and library title page
    steps:
    - Treat the listing of 1990-2006 and 1978-1987 files only as a discovery lead
    - Do not rely on a download or redistribute it until its rights and exact edition are documented
    deliverable: Possible PDF copy subject to provider terms; not accepted as a public or rights-cleared source in this record
    cost: mixed
    last_checked: '2026-08-12'
    caveat: The page itself says its files come from public information and shared resources for academic exchange; that statement is not an open-data licence and does not prove the paper-used annual issues.

access:
  url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053607
  cost: mixed
  license: Printed-volume copyright and library/document-delivery terms; no open-data licence for the exact annual CTESY issues was identified
  format:
  - printed Chinese volume
  - permitted library scan
  - researcher-transcribed table
  api: false
  how_to_get: Start with the NDL related-series record or the 1978-2002 statistical-materials guide, ask a holding library to verify the exact issue and title page, and transcribe only the tables needed with page, unit and issue provenance. Treat later annual volumes and third-party PDFs as separate routes until matched.

caveats:
- The paper calls the source CTESY and dates annual issues 1987-1994; the NDL catalogue uses the related title 中国乡镇企业年鉴 for 1990-2006. Do not silently merge the names.
- Issue year, publication year and reference year may differ; record all three when a volume is obtained.
- The paper's employment/output shares and deflator inputs are constructed from source tables; they are not evidence that the yearbook supplies Jin and Qian's final panel or derived variables.
- Ownership and enterprise-category definitions may change across historical issues; preserve table notes and do not splice a later series without a comparability decision.
- The source does not establish county, household, worker or firm-level identifiers and does not create a policy or causal-variation record.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
  - cite: 'Jin & Qian (1998), Public Versus Private Ownership of Firms: Evidence from Rural China'
    doi: https://doi.org/10.1162/003355398555748
    journal: QJE
    year: 1998
    dataset_role: Township-enterprise employment/output and price-deflator component of a provincial rural-enterprise panel
    evidence_type: data_appendix
    evidence_url: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    data_note: The paper's Appendix Table I and bibliography identify CTESY 1987-1994 annual issues as the source for TVE/private employment and output shares, the TVE output-price deflator, and the rural-enterprise employment denominator. The exact source tables and final paper panel remain distinct from the yearbook volumes.

provenance:
  - source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
    field_scope:
    - QJE article identity and provincial rural-enterprise study
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    field_scope:
    - CTESY exact source name, 1987-1994 annual issue range and China Agricultural Press bibliography
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - Appendix Table I employment/output and deflator roles
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053607
    field_scope:
    - Related China Township Enterprises Yearbook series identity, China Agricultural Press, 1990-2006 holdings and physical/library route
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053607
    field_scope:
    - Current parent-record identity, editorial committee, China Agricultural Press listing, and documented holdings beginning 1990 (published 1991.2) through 2006
    - Negative boundary: this parent record does not establish an 1989 issue or the paper's 1987-1989 source volumes
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://ndlsearch.ndl.go.jp/rnavi/asia/post_97
    field_scope:
    - 1978-2002 statistical-compilation identity, library call number and described national/regional fields
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://www.nianjiandata.com/index.php/books-zhongguo-xiangzhenqiye-nongchanpinjiagongye-nianjian.html
    field_scope:
    - Third-party digital-listing lead and its stated shared-resource caveat only
    added: '2026-08-12'
    confidence: med
    verified: true

related_datasets:
- id: china-township-enterprises-statistical-materials-1978-2002
  relation: complement
- id: china-stat-yearbook
  relation: complement
- id: china-rural-economic-statistics-1949-1986
  relation: predecessor
---

## Positioning in one sentence

This is the historical printed source family behind the township-enterprise component of Jin and Qian's rural China panel: its irreplaceable value is TVE-specific aggregate employment/output information, while the main acquisition cost is verifying the exact annual issue and manually preserving its table definitions rather than assuming that a later or digitized yearbook is identical.

## Select rules

- Prioritize it when a regional or rural-development question needs historical township-enterprise categories that the general China Statistical Yearbook does not identify separately.
- Pair it with the China Statistical Yearbook and the China Rural Statistical Yearbook; each supplies different denominators, deflators or rural indicators and should remain source-labeled.
- Use the 1978-2002 statistical compilation as a practical fallback only after checking table definitions and reference years; use a current registry or ASIF for micro firm questions instead.
- Do not claim exact reproduction until the requested annual issues, tables and page-level extraction are obtained.

## Get recipe

1. Start with the National Diet Library related-series record and the 1978-2002 statistical-materials guide.
2. Ask a holding library to verify the Chinese title, publisher, issue year, reference year and table of contents against CTESY 1987-1994.
3. Obtain a physical copy or permitted scan and define the required province-year-indicator cells before transcription.
4. Record table/page, unit, footnotes, issue/reference-year mapping and missing-value codes for every extracted cell.
5. Compare overlaps with the China Statistical Yearbook or Rural Statistical Yearbook, keeping every source edition and definition visible; keep any derived panel in a separate reproducible project.

## Connections and Limitations

The safest join is province-or-region by year plus enterprise category and indicator, with a historical label concordance and explicit issue/reference-year fields. The general Statistical Yearbook can provide state-enterprise output, prices and population denominators, but it cannot be assumed to reproduce TVE-specific tables. The record identifies no micro identifiers, no guaranteed balanced panel and no open digital licence; if a library cannot confirm the exact issue or its units cannot be reconciled, switch to a verified alternative rather than infer missing values.

## Decision sufficiency check

For a researcher studying historical rural industrialization, this record selects CTESY because it is the source family actually cited for the QJE paper's TVE employment/output and deflator inputs, provides a library-first route and names the closest but non-equivalent compilation. The recommendation fails if the needed issue/table is unavailable or if the yearbook's definitions cannot be aligned with the intended province-year series; the record therefore remains grounding rather than ready.
