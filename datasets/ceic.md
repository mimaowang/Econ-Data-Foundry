---
schema_version: 3
catalog_status: ready
id: ceic
name: CEIC China Economic Database (中国经济数据库 / China Premium Database)
aka:
- CEIC
- CEIC Data
- 中国经济数据库
- CEIC中国数据库
- China Premium Database
- CEIC宏观经济数据库
provider: >-
  CEIC Data (founded 1992, Hong Kong; part of ISI Emerging Markets Group /
  ISI Markets). Official product pages and 2026 university library trial
  notices describe CEIC as a global economic/industry time-series data
  provider with 2,500+ (ZJU notice) to 3,500 (NEUQ notice) data sources;
  platform support contact oge@isimarkets.com per the NEUQ notice.
china_related: true
domains:
- macro
- industry
- finance
- regional
- county

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Time-series indicator access through the CEIC web platform
    (insights.ceicdata.com, which redirects to insights.ceicdata.com.cn; a
    JavaScript application, login page read 2026-08-15), typically obtained
    as an institutional subscription or trial; users browse/query indicator
    series, save searches and charts after registration, and download series
    subject to the institution's limits.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider-first grounding (2026-08-15): CEIC's China product line is 中国
    经济数据库 / China Premium Database (EN+CN versions), delivered as
    time-series indicators through the CEIC web platform. Three 2026
    university library notices read this round (ZJU 2026-06-18; GUFE
    2026-04-15; NEUQ 2026-04-27) corroborate identity (CEIC founded 1992 in
    Hong Kong, part of ISI Emerging Markets Group), the access route
    (insights.ceicdata.com(.cn), on-campus IP, registration for
    personalization), and the China database scope (province/prefecture/
    county/municipality coverage, history to 1949), and add one concrete
    deliverable condition: trial accounts have download limits (NEUQ). An
    open 2025 city-panel paper also verifies that CEIC China Economic
    Database was actually used alongside yearbooks, EPS and CNRDS for a
    260-prefecture-city, 2014-2023 China study; its data-availability
    statement confirms that CEIC requires institutional or individual
    purchase/subscription.
  barrier: >-
    The verified paper lists CEIC among several sources but does not allocate
    every final variable to a source, so it cannot identify a particular CEIC
    table or reproduce the authors' compiled panel. The main marketing site
    (ceicdata.com / ceicdata.com.cn) is now AWS-WAF challenge-blocked for
    automated clients (202 + awsWafCookie, 2026-08-15); platform naming
    (CDMNext vs "CEIC数据管理平台") and API/export conditions are not
    documented in any machine-readable official source; official coverage
    counts conflict across pages and years.

unit_of_observation: Time-series indicators (indicator-country/region/period)
structure: time-series indicator database
geo_granularity:
- country
- province
- prefecture-level city
- prefecture region
- county
- municipality
geography: >-
  Global coverage (210+ countries/regions per 2026 library notices); the
  China database covers provinces, prefecture-level cities, prefecture
  regions, 2,000+ counties and municipalities (GUFE notice), with history
  back to 1949 (GUFE; official CN page claimed history to 1949 in 2026)
time_span:
  start: '1949'
  end: ongoing
  last_confirmed_release: 'China database history traced to 1949 (GUFE 2026 notice; official CN product page 2026)'
  coverage_note: >-
    History-to-1949 applies to Chinese series; per-series coverage varies.
    Series-level coverage must be verified inside the platform.
  last_checked: '2026-08-15'
frequency:
- daily
- monthly
- quarterly
- annual
sample_size: >-
  Conflicting provider/notice claims - none independently audited: ZJU
  2026 notice: 200+ countries, 6.6M series, 2,500+ sources; GUFE 2026
  notice: 210+ countries, ~9M series; NEUQ 2026 notice: 3,500 sources,
  10M+ series; GUFE China database: 700K+ series, 19 macro + 21 industry
  indicators, 287 prefecture-level cities, 53 prefecture regions, 2,000+
  counties, 4 autonomous regions; official CN page (2026, read 2026-08-14):
  420K+ series, 18 macro/23 industry sectors, 297 prefecture-level cities,
  2,000+ counties.
key_variables:
- National accounts, fiscal, social and demographic macro indicators (20+ categories per GUFE notice)
- GDP, CPI, RPI, PPI, industrial output (city-level series per the China Premium Database page)
- Land market (300+ prefectures) and real estate (290+ cities) series (per info page)
- Local government debt by province (monthly) and industrial output series
- Industry data for ~10-23 sectors depending on source version
- High-frequency alternative data (supply chain, consumption, mobility, business statistics, social sentiment - per NEUQ notice)

research_fit:
  best_for:
  - Macro/industry time-series research where an institutional subscription to the China database provides province/prefecture/county-level indicator series in one platform with long history
  - Cross-country or China-regional indicator comparisons using the CEIC web platform
  choose_over:
  - Choose CEIC over RESSET/CSMAR/Wind when the question is macro/industry/county time-series indicators rather than listed-company market data; the CEIC China database is a dedicated economic-indicator product.
  - For county/city microdata or firm-level data, use the relevant canonical records (asif, china-stat-yearbook, china-neri-marketization-index) - CEIC is an indicator database, not microdata.
  not_good_for:
  - Firm-level or household-level microdata
  - Inferring which specific variables or tables came from CEIC when a paper lists CEIC together with yearbooks and other commercial sources
  - Reproducing provider coverage counts as facts (they conflict across sources)
  needs_join_for:
  - Firm outcomes, customs transactions, or survey microdata - external joins by region/indicator
  - Policy timing/assignment design evidence (see Econ-Variation)
  variation_available:
  - Long regional time series; regional and temporal variation in economic indicators
topics:
- macro indicators
- regional economy
- county data
- industry data
- time series

good_for:
- Regional macro/industry indicator extraction for Chinese provinces, cities and counties
- Long-run historical series (to 1949) from one commercial platform
- Cross-country macro comparisons via the global/world-trends databases
identification:
- Time-series and cross-sectional variation in subscribed indicator series across Chinese provinces, prefecture cities, counties and municipalities
- The 2025 documented use confirms a city-year research role in a 260-city 2014-2023 panel, but it does not define a treatment or establish a separate policy-variation record
linkable_keys:
- Region names/administrative units (province/city/county)
- Indicator codes (per series)
- Time period

joins:
- target: china-stat-yearbook
  relation: substitute-and-benchmark
  keys:
  - Region
  - Indicator
  - Year
  method: Compare series definitions before joining; CEIC series may have different definitions/vintages than NBS yearbooks
  evidence_status: plausible
- target: china-neri-marketization-index
  relation: complement
  keys:
  - Province
  - Year
  method: Join by province-year after checking indicator definitions
  evidence_status: plausible

access_routes:
- route: institutional-web
  access_status: available-with-subscription
  direct_url: https://insights.ceicdata.com
  requirements: >-
    Institutional subscription or trial (library arrangement); on-campus IP
    access; registration for personalization (per 2026 ZJU/GUFE/NEUQ
    notices). NEUQ trial required school-email registration and reported
    download limits on trial accounts.
  steps:
  - Check the school library's CEIC page for the current trial/subscription period and access host.
  - Open insights.ceicdata.com (redirects to insights.ceicdata.com.cn) from the campus network and register if personalization is needed.
  - Browse/query the China database series; use the platform menus (CEIC数据管理平台 video tutorial per GUFE notice) and export/download within institutional limits.
  deliverable: >-
    Time-series indicator query and download of the subscribed databases
    (China, Global, World Trends) within platform limits; trial accounts are
    download-limited (NEUQ).
  cost: paid
  last_checked: '2026-08-15'
  caveat: >-
    Main marketing site is WAF-blocked for automated clients; the platform
    is a JS application - series-level coverage and export limits must be
    verified from a logged-in session.
- route: trial
  access_status: available-with-conditions
  direct_url: https://insights.ceicdata.com
  requirements: Library-initiated trial; on-campus IP; registration with school email (NEUQ pattern)
  steps:
  - Ask the library to open/confirm the trial (2026 examples: ZJU trial to 2026-09-30; CTBU 2026-03-27 to 2026-09-24; NEUQ to 2026-05-26).
  - Register and use within the trial window; expect download limits (NEUQ).
  deliverable: Time-limited platform access to the trial database scope
  cost: free
  last_checked: '2026-08-15'
  caveat: Trial scope, host (insights.ceicdata.com vs .com.cn) and download limits vary by institution.

access:
  url: https://insights.ceicdata.com
  cost: paid
  license: >-
    Institutional subscription/trial terms; trial accounts download-limited
    (NEUQ notice); no redistribution terms read from an official source
    (marketing site WAF-blocked this round)
  format:
  - web query
  - spreadsheet export (per platform; unverified)
  api: false
  how_to_get: >-
    Via institutional subscription: library page -> insights.ceicdata.com
    (on-campus IP) -> register -> query/download China or global series.
    API/developer docs (developer.isimarkets.com) are a JS shell with no
    machine-readable content this round.
caveats:
- Coverage numbers conflict across official pages and library notices (420K+ vs 700K+ vs "close to 1M" China series; 6.6M vs 9M vs 10M+ global) - record conflicts, never pick one as fact.
- A verified 2025 paper uses CEIC jointly with China City Statistical Yearbook, EPS, CNRDS and local yearbooks, but does not allocate each variable to its source; its compiled panel is not a CEIC deliverable.
- CDMNext naming is NOT confirmed on any machine-readable official source; 2026 notices use insights.ceicdata.com(.cn) and "CEIC数据管理平台".
- Export/download limits and per-institution module scope are undocumented machine-readably.
- info.ceicdata.com premium product page 404s as of 2026-08-15 (earlier route dead).

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Mao, Pan, Wang & Liu (2025), Does market access drive trade growth? Evidence from China'
  doi: https://doi.org/10.1371/journal.pone.0334661
  journal: PLOS ONE
  year: 2025
  dataset_role: >-
    One named source, alongside yearbooks, EPS and CNRDS, for a 260-prefecture-city China panel spanning 2014-2023.
  evidence_type: published-paper-full-text
  evidence_url: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0334661
  data_note: >-
    The open data-source section lists CEIC China Economic Database among the
    sources for the city panel, and the data-availability statement says CEIC
    requires institutional or individual purchase/subscription. The paper
    does not attribute particular final variables to CEIC rather than its
    other named sources, and neither its compiled panel nor its constructed
    market-access measure is represented as a CEIC download.

provenance:
- source: https://libweb.zju.edu.cn/2026/0618/c55543a3180374/page.htm (read 2026-08-15)
  field_scope:
  - CEIC founded 1992; 200+ countries, 6.6M series, 2,500+ sources
  - access host insights.ceicdata.com/login; on-campus IP; trial to 2026-09-30
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://library.gufe.edu.cn/info/1023/3553.htm (read 2026-08-15)
  field_scope:
  - China database scope: 700K+ series, 19 macro + 21 industry indicators, 287 prefecture cities, 53 prefecture regions, 2,000+ counties, 4 autonomous regions, history to 1949
  - sub-databases (Global, World Trends, China); platform naming CEIC数据管理平台
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://lib.neuq.edu.cn/info/1068/4301.htm (read 2026-08-15)
  field_scope:
  - access host insights.ceicdata.com.cn; school-email registration; trial download limits
  - CEIC founded 1992 in Hong Kong; 3,500 sources / 10M+ series marketing claims; support oge@isimarkets.com
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://insights.ceicdata.com/ (read 2026-08-15; redirects to insights.ceicdata.com.cn/login)
  field_scope:
  - current platform host and login (JS application)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.ceicdata.com/en (2026-08-15; AWS WAF challenge, 202)
  field_scope:
  - main marketing site now challenge-blocked for automated clients
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://developer.isimarkets.com/ (2026-08-15)
  field_scope:
  - developer portal exists (ISI Group) but is a JS shell; no machine-readable API docs
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://info.ceicdata.com/en/products/china-premium-database (404, 2026-08-15)
  field_scope:
  - earlier premium product page route is dead
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.openalex.org/works/https://doi.org/10.1016/j.jdeveco.2025.103674 (read 2026-08-15)
  field_scope:
  - JDE 2025 anchor paper identity (Chen Zhu, Jipeng Zhang, Kang Zhou; closed access; no abstract) - paper use of CEIC unverified
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0334661 (read 2026-09-28)
  field_scope:
  - actual CEIC China Economic Database use in a 260-prefecture-city China panel for 2014-2023
  - paper's multi-source boundary and CEIC subscription requirement
  - non-release of the authors' compiled panel and non-allocation of individual variables to CEIC
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-stat-yearbook
  relation: substitute-and-benchmark
- id: resset
  relation: substitute-and-benchmark
- id: wind
  relation: substitute-and-benchmark
---

## Positioning in one sentence

CEIC's China Economic Database (中国经济数据库 / China Premium Database) is a commercial time-series indicator product for Chinese provinces, prefecture cities, counties and municipalities (history to 1949) reached through an institutional subscription at insights.ceicdata.com(.cn); an open 2025 paper verifies use in a 260-city China panel but leaves the exact CEIC table/variable allocation unresolved, and provider coverage numbers still conflict across sources.

## Select rules

- Choose CEIC for macro/industry/county time-series indicator research when the institution subscribes; it is not microdata and not a listed-company market database (use CSMAR/Wind/RESSET for those).
- Compare series definitions with NBS yearbook series before joining (china-stat-yearbook); never treat provider coverage counts as audited facts.
- The verified 2025 multi-source paper proves CEIC use but not which final variables came from it; choose the table inside the subscribed platform rather than treating its compiled panel as the CEIC download.

## Get recipe

1. Check the school library's CEIC page for the current trial/subscription and access host (2026 examples: ZJU, GUFE, CTBU, NEUQ notices).
2. Open insights.ceicdata.com (redirects to .com.cn) from the campus network and register for personalization (school email per NEUQ).
3. Query the China database series (or Global/World Trends) and download within institutional limits (trial accounts are download-limited).
4. For API/developer access, note developer.isimarkets.com is a JS shell with no machine-readable docs this round.

## Connections and Limitations

CEIC is an indicator database, not microdata; joins to firm/survey assets require external keys by region/period. The main marketing site is WAF-blocked for automated clients as of 2026-08-15, the earlier info.ceicdata.com premium page is dead (404), and platform naming (CDMNext vs "CEIC数据管理平台") plus API/export conditions remain undocumented machine-readably. Coverage conflicts (China 420K+ vs 700K+ series; global 6.6M vs 9M vs 10M+) are retained as conflicts.
