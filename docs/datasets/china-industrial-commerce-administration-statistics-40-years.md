---
schema_version: 3
catalog_status: ready
id: china-industrial-commerce-administration-statistics-40-years
name: China Industrial and Commerce Administration Statistics 40 Years, 1950-1990 source family (中国工商行政管理统计四十年)
aka:
- 中国工商行政管理统计四十年
- Zhongguo gongshang xingzheng guanli tongji sishi nian
- China Industrial and Commerce Administration Statistics Forty Years
- CICAS
provider: Information Center of the State Administration for Industry and Commerce (国家工商行政管理局信息中心); China Statistical Press (中国统计出版社)
china_related: true
domains:
- regional
- rural
- trade
- firm
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Printed historical statistical compilation covering industry-and-commerce administration indicators through 1990; Jin and Qian use selected market-management tables as an input rather than a released copy of their final provincial panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: "The current National Diet Library catalogue and current CiNii record identify a Chinese-language 483-page volume compiled by the Information Center of the State Administration for Industry and Commerce and published by China Statistical Press in October 1992. NDL classifies its subject coverage as China industry-and-commerce administration statistics for 1950-1990, while CiNii currently lists eight university-library holdings. A researcher can use either catalogue to request the physical volume or permitted pages and transcribe the relevant regional market tables with page-level provenance. No open machine-readable release or reuse licence for the exact paper-era tables was verified."
  barrier: "The QJE paper bibliography cites CICAS as a 1990 Beijing volume, while the checked NDL/CiNii records describe a 1992 edition (published October 1992) with data through 1990. The exact edition used by the paper, the table that supplied its rural free-market transaction input, and any historical title-page or reference-year convention must therefore be checked directly. A commercial Excel/PDF listing is an access lead, not evidence of open rights."

# Identity and Coverage
unit_of_observation: National, provincial or other regional industry-and-commerce administration statistical entry; exact grain varies by table
structure: Historical aggregate tables and administrative-statistics sections covering registration, market management and related commerce indicators
geo_granularity:
- national aggregate
- province/region where reported
- table-specific local market aggregates where present
geography: Mainland Chinese industry-and-commerce administration and market activity represented in the compilation; regional coverage and labels must be checked table by table
time_span:
  start: '1950'
  end: '1990'
  last_confirmed_release: '1992'
  coverage_note: The NDL/CiNii subject and catalogue records describe statistics for 1950-1990 and a 1992 publication. The QJE bibliography calls the source CICAS and gives Beijing/China Statistical Press/1990; the paper-era edition relationship remains unresolved.
  last_checked: '2026-09-28'
frequency:
- historical compilation
- table-specific annual series
sample_size: Not a microdata sample; the compilation reports administrative counts, quantities and aggregates by table
key_variables:
- Regional rural/urban market-management and free-market transaction quantities where reported
- Market-management, enterprise-registration, private-enterprise, individual-business and contract-management aggregates
- Commodity quantities or market shares in regional market tables, with units and definitions preserved from each table
- Trademark, advertising and economic-inspection indicators that belong to the volume but are not automatically part of the paper-used market measure

# Research routing
research_fit:
  best_for:
  - Historical regional market-development measures when the research needs administrative market-management statistics through 1990
  - Reconstructing the earlier CICAS component behind Jin and Qian's 1998 QJE rural free-market transaction measure
  - Distinguishing historical market-administration aggregates from modern SAIC/SAMR firm registries or current retail-sales databases
  choose_over:
  - Choose CICAS over a modern firm registry when the research needs the historical aggregate market-statistics concept cited in the QJE paper
  - Pair CICAS with CDTSY only after checking their overlapping years and definitions; the paper treats them as separate source components, not interchangeable editions
  - Use a current registry or commercial database when firm identifiers, current entities or micro outcomes are required; those products cannot replace the 1950-1990 compilation
  not_good_for:
  - Firm-level identifiers, merchant records, transaction microdata or longitudinal business tracking
  - A guaranteed balanced province-year panel or a current measure of market integration
  - Assuming that every table in the volume is the rural free-market transaction measure used in the QJE paper
  - Treating a third-party Excel/PDF listing as a rights-cleared download or proof of the exact 1990 edition
  needs_join_for:
  - Later rural-market transaction measures from the separate China Domestic Trade Yearbook source family
  - Township-enterprise employment/output categories from the China Township Enterprises Statistical Yearbook
  - Rural labor, population and land denominators from rural statistical sources
  - State-enterprise output, prices and broad macro controls from the China Statistical Yearbook
  variation_available:
  - Historical annual and regional dimensions only; this record makes no policy-treatment or causal-variation claim
  topics:
  - market administration
  - rural markets
  - domestic trade
  - regional development
  - firm registration

good_for:
- Manual reconstruction or validation of historical regional market-administration aggregates
- Documenting the pre-1991 source boundary in the Jin and Qian QJE market-development input
- Comparing market indicators across regions while retaining source edition, table, unit and administrative definitions
identification:
- This descriptive statistical compilation does not itself encode a causal design or a verified treatment-assignment rule.
- Its regional and historical dimensions require separate design evidence; they are not classified here as exogenous variation.
linkable_keys:
- Province or historical region label
- Year and source/issue edition
- Market or administrative category
- Indicator, unit and table/page number
- Historical regional-label concordance where necessary

joins:
  - target: china-domestic-trade-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year/reference year
    - Market category and indicator
    method: Use CICAS for the earlier historical market-administration component and CDTSY for the later domestic-trade component only after checking overlapping concepts, units and source years. Keep each source and table visible in the reconstructed panel.
    evidence_status: literature-used
  - target: china-township-enterprises-statistical-yearbook
    relation: complement
    keys:
    - Province or region
    - Year
    - Indicator and unit
    method: Join market measures to township-enterprise activity only after preserving the different administrative and enterprise definitions and aligning the reference year.
    evidence_status: plausible

access_routes:
  - route: National Diet Library catalogue and document-delivery route
    access_status: available-with-conditions
    direct_url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000017642
    requirements:
    - Library membership or document-delivery/interlibrary-loan access
    - Verification of the physical 1992 volume and permission to copy needed pages
    steps:
    - Search NDL bibliographic ID a0000017642 and call number DT331-C5
    - Ask a library to obtain the 483-page Chinese volume and verify the title page, compiler, publisher and publication date
    - Inspect the market-management and regional-market sections before deciding which tables correspond to the QJE input
    - Transcribe only the needed cells with table, page, unit, region and footnote provenance
    deliverable: Physical volume, permitted scan or researcher-transcribed aggregate tables; no open machine-readable panel was verified
    cost: mixed
    last_checked: '2026-09-28'
    caveat: NDL notes that current holdings and copy/loan conditions must be confirmed with the holding library; a catalogue record is not a redistribution licence.
  - route: CiNii Books library holdings
    access_status: available-with-conditions
    direct_url: https://ci.nii.ac.jp/ncid/BN10718939
    requirements:
    - Library or document-delivery access
    - Verification of the requested edition and local copying terms
    steps:
    - Use NCID BN10718939 to locate holdings at specialist and university libraries
    - Request the volume and compare its title page and table of contents with the CICAS citation
    - Preserve the 1990-versus-1992 edition discrepancy in the extraction notes
    deliverable: Physical or permitted scanned pages; not a public bulk download
    cost: mixed
    last_checked: '2026-09-28'
    caveat: CiNii confirms the 1992.10 bibliographic record and holdings, but does not establish that the exact 1990 edition cited by the paper is held or that any digital file is reusable.
  - route: Third-party statistical-yearbook listing (unverified digital lead)
    access_status: needs-verification
    direct_url: https://www.tongjinianjian.com/forty-years-of-statistics-on-chinese-administration-for-industry-and-commerce.html
    requirements:
    - Verify the delivered file's provenance, edition, tables, payment terms and reuse permission
    - Compare it with the NDL/CiNii physical volume before using any cells
    steps:
    - Treat the listing's 1950-1990 Excel/PDF claims as a lead for locating table names only
    - Do not treat the site password, membership or purchase route as an open-data licence
    - Record any file's source edition and page images before transcription
    deliverable: Possible provider-supplied PDF/Excel subject to its terms; not accepted as a rights-cleared source in this record
    cost: paid
    last_checked: '2026-08-12'
    caveat: The listing explicitly distinguishes paid Excel from limited PDF access and does not establish official provenance or permission to redistribute the historical tables.

access:
  url: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000017642
  cost: mixed
  license: Printed-volume copyright, library/document-delivery terms or provider terms; no open-data licence for the exact paper-era tables was identified
  format:
  - printed Chinese compilation
  - permitted library scan
  - researcher-transcribed aggregate table
  api: false
  how_to_get: Start with the NDL or CiNii record, obtain the physical/approved copy, verify whether it is the 1990 or 1992 source edition, locate the relevant regional market table, and transcribe only the needed cells with page-level provenance. Keep any derived panel separate from the book.

caveats:
- The QJE bibliography cites CICAS as a 1990 source, while NDL/CiNii catalogue a 1992 edition containing data through 1990; this version discrepancy must be resolved before claiming exact paper reproduction.
- The volume contains many administrative sections; the presence of market-management tables does not prove that every table supplied the QJE rural free-market measure.
- Regional labels, units and reporting definitions may differ across tables and cannot be inferred from the title alone.
- CICAS and CDTSY are separate source components in the paper; do not merge them into one yearbook or fill one with the other.
- The compilation is aggregate and historical; it does not provide firm identifiers, merchants, transactions or causal treatment dates.

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
    dataset_role: Earlier historical component of the rural free-market transaction-volume measure in a provincial market-development panel
    evidence_type: data_appendix
    evidence_url: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    data_note: The paper's Appendix Table I and bibliography identify CICAS alongside the separate CDTSY source for rural free-market transaction volume. The compilation is not the paper's final cleaned provincial panel, and the paper's 1990 citation must be compared with the catalogued 1992 edition.

provenance:
  - source: https://academic.oup.com/qje/article-abstract/113/3/773/1851137
    field_scope:
    - QJE article identity and provincial rural-enterprise study
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://citeseerx.ist.psu.edu/document?doi=39ff6e496517307ca84bf5bb5343192b9278a4ba&repid=rep1&type=pdf
    field_scope:
    - CICAS source name, paper bibliography and distinction from CDTSY
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://paperzz.com/doc/7852221/forthcoming--quarterly-journal-of-economics-public-vs.-pr...
    field_scope:
    - Appendix Table I rural free-market transaction-volume role
    added: '2026-08-12'
    confidence: med
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000017642
    field_scope:
    - Compiler, publisher, 1992 publication, 483-page physical volume, 1950-1990 subject range and NDL route
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BN10718939
    field_scope:
    - Chinese title, 1992.10 bibliographic record, ISBN, 483-page volume and eight library holdings
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://ndlsearch.ndl.go.jp/books/R100000002-Ia0000017642
    field_scope:
    - Current NDL catalogue availability, compiler, publisher and 1950-1990 subject classification
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://ci.nii.ac.jp/ncid/BN10718939
    field_scope:
    - Current CiNii 1992.10 bibliographic metadata and eight-library holding route
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://www.tongjinianjian.com/forty-years-of-statistics-on-chinese-administration-for-industry-and-commerce.html
    field_scope:
    - Unverified digital listing and table-name lead only
    added: '2026-08-12'
    confidence: med
    verified: true

related_datasets:
  - id: china-domestic-trade-statistical-yearbook
    relation: complement
  - id: china-township-enterprises-statistical-yearbook
    relation: complement
---

## Positioning in one sentence

This is the historical industry-and-commerce administration compilation behind the earlier part of Jin and Qian's rural free-market transaction measure: its research value is the regional market-statistics layer through 1990, while its decisive uncertainty is whether the paper's cited 1990 volume is the same edition as the catalogued 1992 book.

## Select rules

- Prioritize CICAS for historical regional market-administration aggregates through 1990, not for current firm-level or merchant-level research.
- Pair it with CDTSY only after verifying the overlapping market concept, source year and table units; the two are distinct paper inputs.
- Use NDL/CiNii to obtain the physical source first; treat third-party digital files as leads until provenance and rights are checked.
- Do not claim exact reproduction until the edition, table, reference year and provincial coverage are confirmed.

## Get recipe

1. Search NDL record `a0000017642` or CiNii NCID `BN10718939` and request the 483-page volume.
2. Compare the title page and publication date with the QJE bibliography's 1990 citation; record both if they differ.
3. Locate regional market-management/free-market transaction tables and record table/page, unit, region and footnotes.
4. Compare the earlier CICAS values with the later CDTSY values without silently splicing or imputing missing years.
5. Keep any transcribed table or reconstructed panel separate from the copyrighted volume and document the exact source edition.

## Connections and Limitations

The safest join is historical province or region by reference year plus market category, indicator and source edition. CDTSY supplies a later domestic-trade component; CTESY supplies rural-enterprise activity. This record provides no firm identifiers, micro transactions or policy treatment. If the cited 1990 edition cannot be distinguished from the 1992 catalogue record, the researcher should label the edition uncertainty rather than present the route as exact replication.

## Decision sufficiency check

For a researcher studying historical regional market development, this record selects CICAS for the earlier aggregate market-administration input and gives two current, independent library routes to obtain the physical source and extract needed tables with page provenance. It is ready for that library-mediated source-table use, not for claiming an open panel or exact reproduction: the paper's 1990-versus-1992 edition mismatch, exact rural-market table, reference-year convention, regional coverage, copying terms and final cleaned panel still require the researcher to inspect the volume.
