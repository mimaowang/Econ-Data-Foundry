---
schema_version: 3
catalog_status: ready
id: china-domestic-trade-statistical-yearbook
name: China Domestic Trade Yearbook source family, 1991-1994 (中国国内贸易年鉴及其前身)
aka:
- 中国国内贸易年鉴
- Almanac of China's Domestic Trade
- China Domestic Trade Statistical Yearbook
- 中国商业年鉴 (possible pre-1994 title in the same bibliographic family)
- CDTSY
provider: Ministry of Domestic Trade of the People's Republic of China (中华人民共和国国内贸易部) and China Domestic Trade Yearbook Society (中国国内贸易年鉴社) for the 1994-2002 series; the exact issuing body and title of the 1991-1993 volumes still require title-page verification
china_related: true
domains:
- regional
- rural
- trade
- development
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed annual domestic-trade yearbook volumes or licensed page images for the paper-era source family; Jin and Qian use selected market-transaction tables as inputs rather than a released copy of their final provincial panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: "Current CiNii records now close the paper-era source-family route: 中国商业年鉴 covers 1988-1993 (including the needed 1991-1993 predecessor issues) and 中国国内贸易年鉴 begins in 1994. The latter record explicitly describes the title transition. Both live catalogues show multiple holdings, including holdings spanning all required predecessor years and the 1994 volume. A researcher can therefore select a holding for each issue and transcribe the rural free-market transaction table with issue and page provenance. No open machine-readable release or reuse licence for the exact paper-era tables is verified."
  barrier: "This remains a source family with a title and sponsoring-body transition, not a guaranteed homogeneous panel. The current catalogues identify and locate the 1991-1994 issues, but table layout, publication/reference-year convention, exact provincial coverage and definition comparability still have to be checked on the physical or permitted page copy. A third-party scan or spreadsheet would not by itself establish provenance or redistribution rights."

# Identity and Coverage
unit_of_observation: National, provincial or other regional domestic-trade statistical entry; exact grain varies by issue and table
structure: Annual historical aggregate tables and narrative sections on domestic commerce, markets and trade administration
geo_granularity:
- national aggregate
- province/autonomous region/municipality where reported
- table-specific local market aggregates where present
geography: Mainland Chinese domestic-trade and market activity represented in the historical issues; province and indicator coverage must be checked table by table
time_span:
  start: '1991'
  end: '1994'
  last_confirmed_release: '1994'
  coverage_note: The QJE bibliography and Appendix Table I identify CDTSY annual issues for 1991-1994. Current CiNii records identify 中国商业年鉴 as the 1988-1993 predecessor (therefore covering 1991-1993) and 中国国内贸易年鉴 as the 1994-2002 successor. This closes the volume-identity and library-location route, but not the publication/reference-year lag or table-level comparability.
  last_checked: '2026-09-28'
frequency:
- annual issue
- table-specific annual series
sample_size: Not a microdata sample; regional coverage and table availability vary by issue
key_variables:
- Rural free-market transaction volume used as a market-development input in Jin and Qian's provincial panel
- Domestic-market, wholesale/retail or local-trade aggregates where the relevant historical table reports them
- Province/region labels, units, table notes and reference-year metadata needed to reconstruct comparable cells
- Other trade and market indicators in the volumes, kept separate from the specific paper-used transaction measure

# Research routing
research_fit:
  best_for:
  - Historical provincial or regional market-development measures based on rural free-market transaction activity
  - Reconstructing the CDTSY component behind Jin and Qian's 1998 QJE rural-enterprise panel
  - Checking whether a historical market statistic is a domestic-trade administrative aggregate rather than a modern retail-sales or firm-level database
  choose_over:
  - Choose this source family over current retail-sales databases when the question needs the paper-era rural free-market transaction concept and historical provincial coverage
  - Use the 1994-2002 domestic-trade catalogue as an acquisition lead, but inspect the pre-1994 predecessor title before treating it as the 1991-1993 source
  - Use a modern commercial database only when current product, firm, transaction or identifier detail is required; it cannot silently replace the historical aggregate
  not_good_for:
  - Household, merchant, firm or transaction-level microdata and identifiers
  - A guaranteed balanced province-year panel or a current measure of market integration
  - Treating all China domestic-trade yearbooks, China Commercial Yearbooks and current retail-sales tables as definition-identical
  - Treating a third-party digital listing as a rights-cleared download or proof of the paper's exact tables
  needs_join_for:
  - Township-enterprise employment/output categories from the China Township Enterprises Statistical Yearbook
  - Rural labor, population, land and responsibility-system measures from rural statistical sources
  - State-enterprise output, prices and broad macro controls from the China Statistical Yearbook
  - The earlier market-statistics component cited as CICAS, which is a separate historical compilation and must not be folded into CDTSY
  variation_available:
  - Annual and regional dimensions only; this record makes no policy-treatment or causal-variation claim
  topics:
  - domestic trade
  - rural markets
  - market development
  - regional development

good_for:
- Manual reconstruction or validation of historical regional rural-market transaction aggregates
- Documenting the market-development source boundary in the Jin and Qian QJE panel
- Comparing historical market indicators while preserving title, issue, table and reference-year changes
identification:
- This historical aggregate source is descriptive and does not itself encode a causal design or a verified treatment-assignment rule.
- Differences across provinces, issues and years require separate design evidence; they are not classified here as exogenous variation.
linkable_keys:
- Province or historical region label
- Year, issue year and reference year
- Market or trade category
- Indicator, unit and table/page number
- Historical regional-label concordance where necessary

joins:
  - target: china-township-enterprises-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year/reference year
    - Indicator and unit
    method: Join the market-transaction measure to township-enterprise employment/output only after aligning issue/reference years and preserving each source's category definitions.
    evidence_status: literature-used
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Indicator and unit
    method: Use the general Statistical Yearbook for population, prices and broad macro controls; do not substitute its retail or output aggregates for the paper's rural free-market measure without a table-level comparison.
    evidence_status: literature-used

access_routes:
  - route: CiNii Books journal/series catalogue and library holdings
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/AN10491143
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Verification of the requested historical volume and title
    steps:
    - Search NCID AN10491143 and the related book record BA37451907
    - Ask a holding library for the 1994 volume and, if needed, the predecessor 1991-1993 issues under the China Commercial Yearbook title
    - Confirm title page, sponsor, publisher, issue year, reference year and table of contents before requesting pages
    - Transcribe only the needed province/region cells with table, unit, footnote and page provenance
    deliverable: Physical volume, permitted scan or researcher-transcribed aggregate tables; no open machine-readable panel was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The current catalogue lists 17 holdings for the 1994-2002 series, but a catalogue entry does not guarantee a scan, interlibrary loan or permission to redistribute extracted pages.
  - route: CiNii Books detailed record for the 1994-2002 domestic-trade series
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/BA37451907
    requirements:
    - Library or document-delivery access
    - Careful comparison of the title-transition note and the requested year
    steps:
    - Use the record's holdings to locate 1994 and overlapping editions
    - Record the note that editions before 1993 and after 2003 use the China Commercial Yearbook title
    - Request the exact issue and inspect the rural free-market table before treating it as CDTSY
    deliverable: Physical or permitted scanned yearbook pages; not a public bulk download
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The record confirms the source-family chronology, not the exact table or provincial coverage used by Jin and Qian.
  - route: CiNii Books predecessor series for the 1991-1993 paper-era volumes
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/AN1023065X
    requirements:
    - Library membership or interlibrary-loan/document-delivery access
    - Confirmation of the requested 1991, 1992 or 1993 issue and the table's reference year
    steps:
    - Search NCID AN1023065X for 中国商业年鉴, the predecessor series published 1988-1993
    - Select a holding that lists all needed 1991-1993 volumes; the current catalogue displays several such runs
    - Inspect title page, sponsor/editor, issue year, reference year and the rural free-market table before transcribing
    - Record table, page, unit, footnotes and the holding's permitted-copy conditions
    deliverable: Physical volume, permitted scan or researcher-transcribed aggregate tables; not an open machine-readable panel
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The catalogue proves a practical route to the predecessor volumes, not the exact table content, a digital file or broad reuse permission.
  - route: Institutional Chinese bibliography and yearbook-library route
    access_status: needs-verification
    direct_url: https://iie.uibe.edu.cn/zlk/zwtsml/3947.htm
    requirements:
    - Library or institutional access to the listed 1994 Chinese domestic-trade yearbook
    - Verification of the volume's pages, tables and current delivery terms
    steps:
    - Use the catalogue entry as a second acquisition lead for the 1994 volume
    - Ask the library whether the pre-1994 predecessor title is also held
    - Do not infer digital access or reuse rights from a bibliography listing
    deliverable: Library-held volume or permitted copy if available; no open licence established
    cost: mixed
    last_checked: '2026-08-12'
    caveat: The page is a catalogue/listing, not proof that a machine-readable file or the exact paper-era tables can be downloaded.

access:
  url: https://ci.nii.ac.jp/ncid/AN10491143
  cost: mixed
  license: Printed-volume copyright, library/document-delivery terms or institutional database terms; no open-data licence for the exact paper-era tables was identified
  format:
  - printed Chinese volume
  - licensed page images
  - researcher-transcribed aggregate table
  api: false
  how_to_get: Start with the CiNii series and book records, verify the exact 1991-1994 title and issue mapping, and transcribe only the needed rural-market tables with page-level provenance. Keep any reconstructed panel separate from the source volumes.

caveats:
- The paper's English citation calls the source CDTSY 1991-1994; the directly catalogued Chinese domestic-trade series begins in 1994 and has a documented title transition, so 1991-1993 must not be silently inferred.
- Publication year, reference year, market category and provincial reporting coverage may change across issues.
- The yearbook is an aggregate domestic-trade source, not merchant microdata, firm registry data or a causal-treatment file.
- CICAS is a separate historical source named alongside CDTSY in the QJE appendix; do not merge its earlier market statistic into this record.
- A later domestic-trade or retail-sales database may have broader access but is not automatically comparable to the rural free-market transaction measure.

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
    dataset_role: Rural free-market transaction-volume component of a provincial market-development measure
    evidence_type: data_appendix
    evidence_url: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    data_note: The paper's Appendix Table I and bibliography identify CDTSY 1991-1994 annual issues, used together with the separate CICAS source to construct rural free-market transaction volume. The yearbook volumes are not the paper's final cleaned provincial panel.

provenance:
  - source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
    field_scope:
    - QJE article identity and provincial rural-enterprise study
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    field_scope:
    - CDTSY English source name, 1991-1994 citation and its distinction from CICAS
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - Appendix Table I rural free-market transaction-volume role
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://ci.nii.ac.jp/ncid/AN10491143
    field_scope:
    - Chinese domestic-trade series identity, sponsor, 1994-2002 annual range and library holdings
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BA37451907
    field_scope:
    - Detailed book record, 1994-2002 holdings and title-transition note
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/AN1023065X
    field_scope:
    - Current predecessor-series identity, 1988-1993 run and 1991-1993 paper-era issue route
    - Editorial/publisher transition notes and current library holdings
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://iie.uibe.edu.cn/zlk/zwtsml/3947.htm
    field_scope:
    - Institutional 1994 bibliography/acquisition lead
    added: '2026-08-12'
    confidence: med
    verified: true

related_datasets:
  - id: china-stat-yearbook
    relation: complement
  - id: china-township-enterprises-statistical-yearbook
    relation: complement
---

## Positioning in one sentence

This is the historical domestic-trade source family behind Jin and Qian's rural free-market transaction measure: its value is the paper-era regional market aggregate, while the main acquisition risk is the 1991-1994 title and edition transition that must be checked before any table is treated as comparable.

## Select rules

- Prioritize it when a historical regional-development question needs the rural free-market transaction concept cited in the QJE paper.
- Pair it with CTESY for township-enterprise activity and the China Statistical Yearbook for population, prices and broad controls; retain each source's table and definition.
- Treat CICAS as a separate earlier market-statistics compilation, not a missing year of CDTSY.
- Do not claim exact reproduction until the requested volumes, tables, reference-year convention and lawful copy route are verified.

## Get recipe

1. Start with CiNii records AN10491143 and BA37451907 and identify a library holding for 1994.
2. Ask the library to locate the 1991-1993 predecessor title and verify the title page, sponsor, publisher, issue year and reference year.
3. Locate the rural free-market transaction table and record province, unit, table/page and footnote information before transcription.
4. Compare overlaps with CICAS, CTESY and the China Statistical Yearbook without silently replacing the paper's source.
5. Keep the transcribed table or reconstructed panel separate from the printed/licensed volumes and document missing years or definition changes.

## Connections and Limitations

The safest join is province or historical region by reference year, with market category, issue and table retained. CTESY supplies rural-enterprise activity; the general Statistical Yearbook supplies denominators and macro controls. The record does not provide merchants, firms, transactions or a causal treatment date. If the predecessor issue cannot be obtained or the market definition cannot be aligned, preserve the gap or switch to a clearly labeled alternative rather than infer the missing series.

## Decision sufficiency check

For a researcher studying whether historical market development was associated with rural-enterprise organization, this record selects the CDTSY source family for the paper's rural free-market transaction input and gives a concrete library-first route to the predecessor 1991-1993 issues and 1994 successor volume. It is ready for page-provenanced consultation and extraction, not for claiming a downloadable panel, table-level uniformity, unrestricted copying or Jin and Qian's final cleaned provincial panel.
