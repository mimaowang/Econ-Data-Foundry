---
schema_version: 3
catalog_status: grounding
id: china-historical-clan-kinship-1470-1910
name: Historical China prefecture-decade clan, weather and cannibalism panel (Chen, Lin & Zhang 2024 JCE)
aka:
- Hedging desperation data
- Confucian clan kinship network 1470-1910
- 宗族网络与饥荒
provider: >-
  Researcher-constructed by Zhiwu Chen, Zhan Lin and Xiaoming Zhang. The paper
  manually assembled cannibalism instances from Zhang (2004)'s multi-volume
  Comprehensive Compilation of Weather Records for the Last Three Millennia of
  China and the Ming and Qing Veritable Records; it joins these to Shanghai
  Library (2009) genealogy-catalogue data, Chinese Academy of Meteorological
  Science (1981) prefectural weather data, and historical population estimates.
  No release of the resulting analytical panel was located.
china_related: true
domains:
- economic-history
- demography
- rural
- development

data_pathway:
  mode: inaccessible
  origin: researcher-constructed
  target_artifact: >-
    A researcher-constructed panel for 267 prefectures in China Proper, using
    1820 administrative zoning. The paper aggregates manually collected annual
    cannibalism records to prefecture-decade observations for 1470-1910, and
    joins annual weather, lagged genealogy density, population and historical
    controls. The underlying collection spans 1,810 cannibalism instances in
    1368-1911; 1,670 instances enter the 1470-1910 analytical window.
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: >-
    Identity repair (2026-09-28): an openly hosted copy of the published JCE
    article was read. The main panel is prefecture-decade, not county-level:
    267 China-Proper prefectures defined by 1820 zoning, 1470-1910, with 11,481
    usable observations after the paper's lag. Cannibalism is hand-collected
    from Zhang (2004)'s gazetteer-based compilation and the Ming/Qing Veritable
    Records, first placed in prefecture-year form, then aggregated to decades.
    Genealogy density is the count of pre-decade genealogies per 100,000 people
    from Shanghai Library (2009)'s General Catalogue of Chinese Genealogy;
    precipitation categories are from Chinese Academy of Meteorological Science
    (1981). The full construction is readable, but no panel, code, or data
    deposit was located; documentation does not make the author panel directly
    obtainable.
  barrier: >-
    The article identifies the source books and manual aggregation steps but
    does not supply its extracted events, entity crosswalks, analysis panel or
    code. Rebuilding would require lawful access to the cited historical
    sources, record-by-record extraction, matching to the paper's 1820
    prefectural geography, and validation choices that the released article
    cannot mechanically reproduce.

unit_of_observation: 'Prefecture-decade in the main analytical panel: 267 China-Proper prefectures using 1820 administrative zoning, 1470-1910'
structure: historical prefecture-year source panel aggregated to a prefecture-decade analytical panel
geo_granularity:
- 267 prefectures in China Proper (1820 administrative zoning)
geography: China Proper; the 267 prefectures represented over 90% of the study-period population
time_span:
  start: '1470'
  end: '1910'
  last_confirmed_release: 'No public release identified (rechecked 2026-09-28)'
  coverage_note: >-
    Manual source collection spans 1368-1911; historical weather availability
    limits the main panel to 1470-1910. The paper first constructs a
    prefecture-year panel, then uses decades because nonzero events are rare.
  last_checked: '2026-09-28'
frequency:
- annual source records; decade-level analytical panel
sample_size: >-
  267 prefectures; 1,810 manually collected cannibalism instances during
  1368-1911, of which 1,670 fall in the 1470-1910 main window; 11,481 usable
  prefecture-decade observations after the lagged genealogy measure.
key_variables:
- Cannibalism instances, manually collected and aggregated from prefecture-year to prefecture-decade
- Genealogy density: pre-decade genealogies per 100,000 population
- Annual prefectural weather category (five-point flood-to-drought scale), summarized by decade
- Historical prefectural population estimates used for normalization

research_fit:
  best_for:
  - Historical kinship, weather hardship and violence research requiring the paper's documented prefecture-decade construction
  - Assessing whether an approximate reconstruction is feasible before committing to manual historical-source extraction
  choose_over:
  - Choose this record over china-clan-network-carbon-emissions-2026 (candidate, Land Economics) only after comparing constructions - different period, method, and outcomes; overlap unverified.
  not_good_for:
  - Assuming a public download exists (none found; CQH archives show no clan dataset).
  - Modern kinship measures or post-1910 data.
  needs_join_for:
  - Prefecture-compatible historical outcomes and an explicit historical-boundary crosswalk where another source uses a different geography
  variation_available:
  - The documented panel differs across prefectures and decades, but it describes historical data rather than a causal assignment; any identification claim belongs in separate research-design work.
  topics:
  - kinship networks
  - historical famine
  - risk sharing
  - Confucian institutions

good_for:
- historical clan/kinship research design
- famine and demographic crisis analysis
identification: []
linkable_keys:
- 1820-prefecture geography / historical prefecture name
- Decade (1470-1910)

joins: []

access_routes:
- route: open-access-full-text
  access_status: available
  direct_url: https://cbdb.hsites.harvard.edu/sites/g/files/omnuum3101/files/cbdb/files/hedging_desperation_how_kinship_networks_reduced_cannibalism_in_historical_china.pdf
  requirements: None
  steps:
  - Open the openly hosted published-paper PDF.
  - Read section 3 for source roles and the manual source-to-prefecture-decade construction.
  - Treat the article as documentation, not as a data download.
  deliverable: Published full-text construction documentation; not a data file.
  cost: free
  last_checked: '2026-09-28'
  caveat: The openly hosted article does not supply the constructed panel, source extracts or code.
- route: working-paper
  access_status: needs-verification
  direct_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3955923
  requirements: Human browser (SSRN blocks automated clients in this environment)
  steps:
  - Open the SSRN WP page and download the PDF.
  - Compare WP and published data sections for version differences.
  deliverable: WP PDF (if downloadable by human).
  cost: free
  last_checked: '2026-08-15'
  caveat: SSRN connect-timeout for automated clients (2026-08-15); two SSRN IDs (3955923, 3943899) found - relationship unverified.

access:
  url: https://doi.org/10.1016/j.jce.2024.01.003
  cost: free
  license: >-
    Paper: CC BY-NC-ND 4.0 (hybrid OA). Data: no public file/license
    identified.
  format:
  - paper full text (HTML/PDF via publisher)
  api: false
  how_to_get: >-
    Read the open-access article in a human browser; no public data file.
caveats: >-
  The paper documents the source books and aggregate construction, not a
  reproducible digital pipeline. Surviving genealogy counts are subject to
  geographically varying survivorship; cannibalism records can be
  under-recorded and 87 of 1,810 events lack location. This asset is not a
  county panel and should not be joined to county data without a separately
  justified geography crosswalk.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Chen, Lin & Zhang (2024), Hedging desperation: How kinship networks reduced cannibalism in historical China'
  doi: https://doi.org/10.1016/j.jce.2024.01.003
  journal: JCE
  year: 2024
  dataset_role: Historical kinship-network and famine/cannibalism data 1470-1910 (main analysis)
  evidence_type: published-paper-full-text
  evidence_url: https://cbdb.hsites.harvard.edu/sites/g/files/omnuum3101/files/cbdb/files/hedging_desperation_how_kinship_networks_reduced_cannibalism_in_historical_china.pdf
  data_note: >-
    Published paper read 2026-09-28. The main analysis uses a 267-prefecture,
    1470-1910 prefecture-decade panel: manual cannibalism records from Zhang
    (2004) and Ming/Qing Veritable Records; Shanghai Library (2009) genealogy
    catalogue; Chinese Academy of Meteorological Science (1981) weather; and
    historical population estimates. The analytical files themselves are not
    released.

provenance:
- source: Crossref API 10.1016/j.jce.2024.01.003 (read 2026-08-15)
  field_scope:
  - author list
  - journal/volume/date
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Elsevier core-data API (PII S0147596724000040, read 2026-08-15)
  field_scope:
  - open access status (hybrid, CC BY-NC-ND)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Unpaywall 10.1016/j.jce.2024.01.003 (read 2026-08-15)
  field_scope:
  - OA status and location
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.cqh.hku.hk/data-archives-and-repositories/ (read 2026-08-15)
  field_scope:
  - absence of a public clan/lineage dataset at CQH
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://cbdb.hsites.harvard.edu/sites/g/files/omnuum3101/files/cbdb/files/hedging_desperation_how_kinship_networks_reduced_cannibalism_in_historical_china.pdf (published paper read 2026-09-28)
  field_scope:
  - actual paper use
  - prefecture-decade observation unit and 1820 geography
  - source and construction steps
  - coverage and sample counts
  - source-specific limitations
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets: []
---

## Positioning in one sentence

This is the unreleased prefecture-decade historical kinship, weather and cannibalism panel behind the JCE 2024 paper: the published text documents the sources and construction, but not a reusable data file or code.

## Select rules

- Choose this record when the research needs the paper's 267-prefecture, 1470-1910 historical clan, weather and cannibalism measures; assess the documented reconstruction burden first.
- Compare with the Land Economics clan candidate before merging identities; its construction is separate and unresolved.
- Do not assume a download exists: no public file, no CQH dataset.

## Get recipe

1. Open the publicly hosted JCE paper and read section 3, which documents the source-to-panel pathway.
2. Obtain the identified source materials lawfully before attempting a reconstruction; the paper does not provide their extracted digital panel.
3. Match historical events and source locations to the paper's 1820 prefectural geography, aggregate to decades, and retain the original source and matching uncertainty.

## Connections and Limitations

- The source recipe is now known, but source access, event extraction and the authors' geographic crosswalk remain unreleased.
- The analytical geography is 1820 prefectures, not counties; any link to county-level historical panels requires an explicit, independently justified crosswalk.
- No article documentation alone establishes that a reconstruction exactly reproduces the authors' events, coding or panel.
