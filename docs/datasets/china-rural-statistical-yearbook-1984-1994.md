---
schema_version: 3
catalog_status: ready
id: china-rural-statistical-yearbook-1984-1994
name: China Rural Statistical Yearbook, 1984-1994 (中国农村统计年鉴)
aka:
- 中国农村统计年鉴
- China Rural Statistical Yearbook
- Rural Statistical Yearbook of China
- CRSY
provider: National Bureau of Statistics rural-statistics offices (issue-level compiler changed over time); China Statistical Press (中国统计出版社)
china_related: true
domains:
- rural
- regional
- development
- labor
- agriculture
- urban

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed annual China Rural Statistical Yearbook volumes and their issue-specific tables for the 1984-1994 source family cited by Jin and Qian; the paper-built provincial panel is not a released copy of the yearbook
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The QJE appendix identifies CRSY as the source for rural gross social product, rural labor, cultivated land, non-farm employment, a 1983 Household Responsibility System measure, and related rural-population denominators. The current National Diet Library catalogue confirms the annual printed series, China Statistical Press publication from 1985 onward, and issue-level compiler changes covering the paper period. A library copy or permitted scan is a concrete starting route for page-provenanced extraction.
  barrier: The paper's 1984-1994 labels may refer to reference years rather than publication years. Exact issue-to-table mapping, provincial table layout, machine-readable delivery, and reuse rights still require inspection of a physical or licensed copy. A third-party PDF/Excel listing is only an unverified lead and is not evidence of an open or lawful download.

# Identity and Coverage
unit_of_observation: National, provincial or other regional rural-statistical entry; the exact grain depends on the issue and table
structure: Annual historical aggregate tables with table-dependent rural economic, labor, land and social indicators
geo_granularity:
- national aggregate where reported
- province or region where reported
- table-specific local aggregates where present
geography: Mainland Chinese rural economy represented in the historical volumes; province coverage and boundary labels must be checked table by table
time_span:
  start: '1984'
  end: '1994'
  last_confirmed_release: '1994 volume in the series (issue/reference-year mapping unresolved)'
  coverage_note: Jin and Qian cite annual CRSY issues for 1984-1994. The National Diet Library catalogue records the series from the 1985 volume (published 1986.2) onward and records compiler changes through 1994; Google Books identifies a 1992 volume that reports 1991 rural conditions. Keep publication year, issue label and reference year separate until the title page and table notes are checked.
  last_checked: '2026-09-28'
frequency:
- annual issue
- table-specific annual series
sample_size: Not a microdata sample; province, indicator and year coverage vary by table
key_variables:
- Rural gross social product used as a denominator for private financial assets and product-market development
- Total rural labor force and agricultural labor force for the non-farm-employment share
- Total cultivated land and rural population for per-capita cultivated land
- Rural household adoption of the Dabaogan form of the Household Responsibility System at the end of 1983
- Rural population and other rural basic-condition denominators where reported

# Research routing
research_fit:
  best_for:
  - Historical provincial or regional rural-economy measures when the question needs rural production, labor, land or household-responsibility-system context in the 1980s and early 1990s
  - Reconstructing the CRSY component of Jin and Qian's 1998 QJE provincial rural-enterprise panel
  - Building a source-audited aggregate rural panel when table, page, unit and issue provenance can be preserved
  choose_over:
  - Choose CRSY over the general China Statistical Yearbook when the needed measure is specifically rural gross social product, rural labor, cultivated land, non-farm employment or the historical HRS-adoption table
  - Use the 1949-1986 rural-economic compilation for earlier historical coverage only; it is a different book and does not silently extend this 1984-1994 source family
  - Use a current NBS release for current definitions, not as proof that the paper-era tables or definitions are unchanged
  not_good_for:
  - Household, farm, worker, village or firm microdata and individual identifiers
  - A guaranteed balanced province-year panel, county-level data, or a current rural series
  - Treating the yearbook as Jin and Qian's final cleaned panel or as a policy-treatment dataset
  - Assuming that every table covers every province or that a later digital copy has the same definitions as the paper-era issue
  needs_join_for:
  - Township-enterprise and private-enterprise employment/output from the CTESY and TESM source families
  - Rural income, taxes, government revenue and rural price measures from the China Agricultural Yearbook
  - Rural-enterprise loans and household savings from the China Rural Finance Statistical Yearbook
  - State-industry output and rural CPI inputs from the China Statistical Yearbook
  - Urban-population shares from the China Population Yearbook or a compatible census product
  variation_available:
  - Provincial and annual differences in reported rural aggregates; this describes the data dimensions only and is not a policy treatment or causal-variation record
  topics:
  - rural development
  - rural industrialization
  - non-farm employment
  - land and labor allocation
  - regional growth
  - household responsibility system

good_for:
- Manual reconstruction or validation of historical provincial rural aggregates
- Documenting the CRSY source boundary behind Jin and Qian (1998 QJE)
- Joining rural labor, land and production denominators to separate enterprise, finance and income yearbooks
identification:
- This annual statistical source is descriptive and does not itself encode a causal design or a verified treatment-assignment rule.
- Provincial and annual differences require separate design evidence; they are not classified here as exogenous variation.
linkable_keys:
- Province or historical region label
- Year, issue label and reference-year convention
- Indicator, unit, table and page number
- Rural population denominator and rural/total labor definition
- Researcher-built province concordance when historical labels or boundaries changed

joins:
  - target: china-township-enterprises-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year and reference-year convention
    - Rural labor or enterprise indicator
    method: Use CRSY for rural labor, land and gross-social-product denominators and CTESY for township/private-enterprise employment and output. Preserve each issue, table, unit and missing-value note instead of copying the paper's derived ratios as raw columns.
    evidence_status: literature-used
  - target: china-township-enterprises-statistical-material-1978-1985
    relation: complement
    keys:
    - Province or region
    - Year
    - Rural population or rural-enterprise context
    method: Use TESM only for the separate 1980/1986 baseline inputs documented in the QJE appendix; do not use it as a substitute for CRSY's 1987-1994 rural labor and land tables.
    evidence_status: literature-used
  - target: china-agricultural-yearbook
    relation: complement
    keys:
    - Province or region
    - Year and issue/reference-year convention
    - Rural income, revenue or price indicator
    method: Join only after checking the two books' reference years and province labels. CRSY supplies rural production/labor/land context; CAY supplies the separate income, taxes, revenue and price roles in the QJE construction.
    evidence_status: literature-used
  - target: china-rural-finance-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Rural financial indicator
    method: Keep CRSY's rural gross-social-product denominator separate from CRFSY's loan and savings numerators; preserve the previous-year timing used in the paper.
    evidence_status: literature-used
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Indicator and unit
    method: Use the general Statistical Yearbook for state-industry output or rural CPI inputs and for cross-checking, not as a silent replacement for CRSY rural tables.
    evidence_status: literature-used
  - target: china-rural-economic-statistics-1949-1986
    relation: predecessor
    keys:
    - Province or region
    - Year
    - Rural/agricultural indicator and unit
    method: Use the 1949-1986 compilation only for earlier historical context and overlapping-definition checks; it is not evidence for the paper's later CRSY tables.
    evidence_status: plausible

access_routes:
  - route: National Diet Library catalogue and holding-library/document-delivery route
    access_status: available-with-conditions
    direct_url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053636
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Chinese-language table reading and manual transcription
    steps:
    - Search the NDL record Z41-AC72 and its holdings, beginning with the paper-era 1985-1994 volumes
    - Ask the holding library to verify the title page, issue label, publisher, compiler, publication date and table of contents
    - Match the requested table and reference year to the QJE Appendix Table I before copying any values
    - Request only needed pages under the library's scan and copyright rules, then record table, page, unit, province coverage and missing-value codes
    deliverable: Physical volume, permitted scan or researcher-transcribed tables; no open machine-readable CRSY file was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The NDL record confirms the series and holdings, not that every requested volume is immediately scanable or that a scan may be redistributed.
  - route: Google Books bibliographic record for the 1992 volume
    access_status: discovery-only
    direct_url: https://books.google.com/books/about/%E4%B8%AD%E5%9B%BD%E5%86%9C%E6%9D%91%E7%BB%9F%E8%AE%A1%E5%B9%B4%E9%89%B4.html?id=hUNauAAACAAJ
    requirements:
    - Use the metadata to identify a library or licensed seller; Google Books does not establish a downloadable copy
    steps:
    - Confirm that the volume is 中国农村统计年鉴: 1992, compiled by the NBS rural social-economic statistics office
    - Note that the record says it reports 1991 rural conditions and contains rural output, labor, income, finance and social tables
    - Locate a lawful physical or licensed copy and compare the title page/table notes before using it
    deliverable: Bibliographic identification and a route lead, not the paper's data file
    cost: mixed
    last_checked: '2026-08-12'
    caveat: Metadata and page count do not prove the exact table used by Jin and Qian or any reuse permission.
  - route: Third-party yearbook listing (unverified digital lead)
    access_status: needs-verification
    direct_url: https://www.tjnj.net/navibooklist-N2006010438-2.html
    requirements:
    - Verify file provenance, exact issue, payment terms and reuse permission
    - Compare any delivered file with a library title page and the QJE source citation
    steps:
    - Treat the listing as a discovery lead only
    - Do not download, redistribute or cite a file as the paper's source until its edition and rights are checked
    deliverable: Possible third-party PDF/Excel subject to provider terms; not accepted as an open or rights-cleared route
    cost: mixed
    last_checked: '2026-08-12'
    caveat: A listing is not evidence of official provenance, complete coverage or permission to reuse.

access:
  url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053636
  cost: mixed
  license: Printed-volume copyright and library/document-delivery terms; no open-data licence for the paper-era issues was identified
  format:
  - printed Chinese annual volume
  - permitted library scan
  - researcher-transcribed table
  api: false
  how_to_get: Start with the NDL catalogue and a holding library, verify the issue/reference-year/table boundary against the QJE appendix, and transcribe only the required provincial cells with page, unit, footnote and missing-value provenance. Treat Google Books and third-party listings as metadata or unverified leads, not as automatic downloads.

caveats:
- The paper cites CRSY 1984-1994 annual issues, while the NDL series record starts with the 1985 volume published in 1986.2; do not assume the year labels mean the same thing without checking title pages and table notes.
- Compiler responsibility changes across the paper period; preserve the issue-level editor and publisher rather than collapsing all volumes into a timeless provider.
- The QJE variables are ratios or derived measures built from source tables. CRSY does not by itself provide Jin and Qian's final provincial regression panel.
- The source is aggregate and table-dependent; it does not establish county, household, worker or firm identifiers.
- The current NBS series and a later digital yearbook may revise definitions, province names or units; preserve the historical issue and compare before splicing.
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
    dataset_role: Rural production, labor, land and household-responsibility-system inputs and denominators in a provincial rural-enterprise panel
    evidence_type: data_appendix
    evidence_url: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    data_note: Appendix Table I identifies CRSY 1985 for the share of rural households not adopting Dabaogan at the end of 1983 and CRSY 1987-1994 for rural gross social product, total/agricultural labor, cultivated land and rural population inputs. The paper uses these source tables to construct ratios and controls; it does not release CRSY or claim that the yearbooks are its final cleaned panel.

provenance:
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - paper actually uses CRSY
    - source-specific variable roles and year labels
    - provincial aggregate panel and derived-variable boundary
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000053636
    field_scope:
    - Chinese title and annual-series identity
    - China Statistical Press publisher
    - 1985-onward holdings and issue-level compiler changes through the paper period
    - library/document-delivery route
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://books.google.com/books/about/%E4%B8%AD%E5%9B%BD%E5%86%9C%E6%9D%91%E7%BB%9F%E8%AE%A1%E5%B9%B4%E9%89%B4.html?id=hUNauAAACAAJ
    field_scope:
    - 1992 volume metadata
    - compiler and publisher corroboration
    - 1991 reference-year description
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://www.stats.gov.cn/zs/tjwh/tjkw/tjzl/index_5.html
    field_scope:
    - official NBS publication-catalogue context for the yearbook series
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://www.tjnj.net/navibooklist-N2006010438-2.html
    field_scope:
    - unverified digital-access lead only
    added: '2026-08-12'
    confidence: low
    verified: false

related_datasets:
  - id: china-township-enterprises-statistical-yearbook
    relation: complement
  - id: china-township-enterprises-statistical-material-1978-1985
    relation: complement
  - id: china-agricultural-yearbook
    relation: complement
  - id: china-rural-finance-statistical-yearbook
    relation: complement
  - id: china-stat-yearbook
    relation: complement
  - id: china-rural-economic-statistics-1949-1986
    relation: predecessor
---

## Positioning in one sentence

This is the historical printed rural-statistics source family behind several provincial inputs in Jin and Qian (1998 QJE), not their final regression file: its value is the rural production/labor/land detail for the 1980s and early 1990s, while the main cost is library-mediated access and manual table verification.

## Select rules

- Prioritize it when a research idea needs historical provincial rural gross product, labor, cultivated land, non-farm employment or the 1983 HRS-adoption measure.
- Pair it with CTESY/TESM for township-enterprise measures, CAY for rural income and government revenue, CRFSY for loans and savings, and CSY for state-industry or CPI inputs; keep the table-level provenance of each source.
- Use the 1949-1986 rural compilation for earlier historical context, not as an automatic replacement for 1987-1994 CRSY observations. Use current NBS releases for current questions only after checking definition changes.
- Do not use this record for microdata, firm identifiers, a guaranteed county panel, or policy-treatment claims.

## Get recipe

1. Search the NDL record `Z41-AC72` and the Chinese title for a holding library with the needed 1985-1994 volumes.
2. Obtain a physical copy, permitted scan or other lawful document delivery. Record the title page, issue label, compiler, publication date and publisher.
3. Use the QJE Appendix Table I to specify the needed indicators before transcribing. Capture table/page, unit, province labels, reference year and missing-value notes for every cell.
4. Compare overlapping values and definitions with the companion yearbooks before joining by province and year. Keep publication year and reference year separate.
5. Store any derived panel or ratios in a separate reproducible project; this record identifies the source tables and their route, not a redistributed copy of the paper's analysis file.

## Connections and Limitations

The safest join is province-by-reference-year with an explicit historical province concordance, indicator label, unit and table/page provenance. CRSY supplies rural production, labor and land context, while the companion yearbooks supply enterprise, finance, income, price and state-sector components. Because no open machine-readable release was verified, a researcher should not promise a bulk download or redistribute a third-party file until a specific library/provider confirms the issue and terms. A recommendation fails if the needed issue/table is absent, if the issue/reference-year convention cannot be reconciled, or if a changed definition makes the intended join invalid.

## Decision sufficiency check

For a researcher studying historical regional rural industrialization, this record selects CRSY for rural denominators and labor/land context, tells the researcher to start with a library issue check, and explains why CTESY, CAY and the general Statistical Yearbook must remain separate complements. If the exact table or lawful copy cannot be obtained, the agent should retain the uncertainty and switch to a verified later/earlier source rather than fill the gap from a title, abstract or third-party listing.
