---
schema_version: 3
catalog_status: grounding
id: china-weekly-provincial-hog-prices
name: China weekly provincial hog-price panel (2016-2020, 29 provinces)
aka:
- 省级生猪价格周度数据
- Weekly provincial hog prices (China)
- zhujiage.com.cn hog prices
- Chinese hog market weekly price panel
provider: >-
  Raw daily county-level hog prices from the commercial price-information site
  www.zhujiage.com.cn (猪价格网); ASF case and shipping-ban information from the
  Ministry of Agriculture and Rural Affairs (moa.gov.cn/gk/yjgl_l/); CPI and
  provincial hog output from the National Bureau of Statistics. The panel is
  researcher-constructed (Ma, Delgado & Wang).
china_related: true
domains:
- agriculture
- markets
- regional
- trade
- development

data_pathway:
  mode: constructed
  origin: researcher-constructed
  target_artifact: >-
    Province-week average hog-price panel: 29 provinces x 255 weeks (2016-01-01
    to 2020-11-10), real RMB/kg (CPI-deflated), built by aggregating daily
    county-level prices from zhujiage.com.cn.
  availability: partially-reproducible
  ordinary_researcher_feasible: false
  summary: >-
    The paper's data asset is a weekly province-level hog-price panel around the
    2018 African Swine Fever outbreak and the inter-province live-hog shipping
    ban. The same-author NBER book chapter documents construction: daily
    county-level prices from www.zhujiage.com.cn (2016-01-01 to 2020-11-10),
    averaged to weekly provincial prices, 29 provinces (Qinghai and Tibet
    excluded for >80-90% missing weeks), linear interpolation for remaining
    gaps, CPI-deflated. The raw site is currently unreachable from this
    environment and its current access terms are unverified, so reproduction
    feasibility is uncertain.
  barrier: >-
    The JDE article's own data section is unread: its nominal hybrid-OA/CC-BY
    publisher record does not itself provide a usable full-text file, and the
    current human-browser visit reached a ScienceDirect CAPTCHA rather than
    article text (2026-09-28). zhujiage.com.cn
    was unreachable (connection aborted / SSL EOF) on 2026-08-15; Wayback
    snapshots confirm the site existed (2008-2010 confirmed). The paper's
    cleaned panel is not released anywhere found.

unit_of_observation: Province-week average hog price (simple average of daily county-level prices within the province and week)
structure: Balanced panel of 29 provinces x 255 weeks (with interpolation for missing weeks)
geo_granularity:
- province
- county (raw daily prices before aggregation)
geography: '29 Chinese provinces: all mainland province-level units except Qinghai and Tibet (excluded for missingness); capital-city geodesic distances for pairs'
time_span:
  start: '2016-01-01'
  end: '2020-11-10'
  last_confirmed_release: null
  coverage_note: >-
    Period divided into 4 segments: pre-ASF (2016-01-01 to 2018-08-05), ban
    period (2018-08-06 to 2019-03-18), immediate post-ban pre-COVID
    (2019-03-19 to 2020-02-29), post-COVID (2020-03-01 to 2020-11-10). 255 weeks
    total; all 29 provinces observed at least 209 weeks (Ningxia 209, Shanghai
    221, Hainan 230, Guizhou 245; others 252+).
  last_checked: '2026-09-28'
frequency:
- weekly
sample_size: 29 provinces x 255 weeks (7,395 province-week observations before interpolation details; per chapter construction)
key_variables:
- Weekly provincial average hog price (nominal and CPI-deflated real RMB/kg; January 2018 = 100 base)
- ASF case and ban indicators (per province, from MOA and news reports)
- Provincial hog output 2017 and net importer/exporter status 2016 (controls, NBS/industry reports)
- Pairwise capital-city geodesic distance (R maps package)

research_fit:
  best_for:
  - Spatial market integration and price-transmission analysis of the Chinese live-hog market around the 2018 ASF shock
  - Testing how inter-province shipping bans segment and re-integrate markets (arbitrage under imperfect public information)
  - Province-level hog price dynamics for event studies of the ASF period
  choose_over:
  - Choose this reconstructed panel over generic agricultural price aggregates when weekly frequency, provincial granularity and the ASF-window coverage are essential.
  - Prefer NBS/MOA official weekly or monthly price series if only national or coarse series suffice and reproducibility matters (their coverage of the ASF window must be checked separately).
  not_good_for:
  - County-level price analysis: the released/described asset is aggregated to province-week; the raw county-level feed may itself be incomplete before 2018 (missing days in many weeks).
  - Firm-level or slaughter-plant-level analysis.
  - Current (post-2020) hog price monitoring.
  needs_join_for:
  - ASF case counts and ban timing must be re-collected from MOA (moa.gov.cn/gk/yjgl_l/) and news reports as documented in the chapter.
  - CPI deflation and hog output come from NBS statistics.
  - Consumption, trade or welfare analysis needs pork-demand and trade data from other sources.
  variation_available:
  - Cross-province price deviations and pairwise links estimated per period; the ban provides a natural-experiment timing (treatment side belongs to the variation repository).
  topics:
  - agricultural markets
  - market integration
  - price transmission
  - African swine fever
  - spatial economics

good_for:
- Pairwise inter-province price-link estimation around the 2018 ASF ban
- Distance effects on post-ban market reintegration
- Descriptive weekly hog-price dispersion across provinces 2016-2020
identification: []
linkable_keys:
- Province (29 province-level units; code vintage per construction)
- Week (ISO week within 2016-01-01..2020-11-10)
- Pairwise distance and ban-week variables

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province code
  - Year
  method: Join province-year macro controls (GDP, agriculture output) with consistent province codes; the panel's price series are research-constructed.
  evidence_status: plausible

access_routes:
- route: raw-source reconstruction (zhujiage.com.cn)
  access_status: blocked
  direct_url: http://www.zhujiage.com.cn/
  requirements:
  - Access to the live site (unverified: connection aborted / SSL EOF for automated clients on 2026-08-15); site terms unknown
  steps:
  - Verify whether www.zhujiage.com.cn still publishes daily county-level hog prices and under what terms.
  - Download daily county prices for 2016-01-01 to 2020-11-10, average to province-week, interpolate missing weeks, deflate by NBS monthly CPI.
  - Re-collect MOA ASF case/ban dates and NBS hog output for controls.
  deliverable: A reconstructed province-week price panel comparable to the paper's described asset
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Site unreachable from this environment on 2026-08-15; Wayback snapshots exist (2008-2010 confirmed, no recent snapshot verified). Machine readability and current terms unknown.
- route: chapter/paper documentation
  access_status: available-with-application
  direct_url: https://www.nber.org/books-and-chapters/risks-agricultural-supply-chains/exploring-spatial-price-relationships-case-african-swine-fever-china
  requirements:
  - None for the NBER chapter PDF (public download)
  - For the journal article, a publisher session that reaches the actual text rather than the current CAPTCHA; its CC-BY metadata is not a usable text-delivery route by itself
  steps:
  - Download the NBER chapter (Delgado, Ma & Wang 2023, NBER volume 'Risks in Agricultural Supply Chains', pp. 139-157) for the data-construction description and summary statistics.
  - Read the JDE article data section in a human browser to confirm the journal version's exact sample and any updates.
  deliverable: Construction documentation, summary statistics, source URLs; not the cleaned panel
  cost: free
  last_checked: '2026-08-15'
  caveat: >-
    The authors do not release the cleaned panel anywhere found this round.
    A direct 2026-09-28 human-browser visit to the nominally hybrid-OA journal
    page stopped at a CAPTCHA, so use the public NBER chapter for the
    documented construction unless the journal text is actually reached.

access:
  url: http://www.zhujiage.com.cn/
  cost: unknown
  license: Unknown; commercial price-information site terms not verified
  format:
  - unknown
  api: false
  how_to_get: 'Reconstruction route: obtain daily county-level prices from zhujiage.com.cn (site access unverified), aggregate to province-week, interpolate, deflate; documentation in the NBER chapter and JDE article.'
caveats:
- The NBER chapter (same authors, same study) is the source of the data-construction facts; the JDE article's own data section is still unread. Its hybrid-OA/CC-BY metadata does not guarantee that a browser reaches the article text: the checked publisher visit stopped at a CAPTCHA.
- The raw daily county-level data have missing days in many weeks before 2018; province-week averages and linear interpolation are part of the documented construction.
- Qinghai and Tibet are excluded (80%/90% missing weeks); Ningxia, Shanghai, Hainan, Guizhou have fewer observed weeks (209-245).
- Site access, current terms, and any dataset release by the authors remain unverified; reproduction feasibility is uncertain.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: partial
  last_audited: '2026-08-15'

production:
  raw_sources:
    - name: zhujiage.com.cn daily county-level hog prices (猪价格网)
      source_type: webpage
      role: Raw daily county-level hog prices aggregated into the province-week panel
      access_route: Direct site access (unreachable from this environment 2026-08-15; Wayback snapshots 2008-2010 confirmed)
      url: http://www.zhujiage.com.cn/
      coverage: '2016-01-01 to 2020-11-10 daily county-level prices; 31 provinces in raw set'
      last_checked: '2026-08-15'
    - name: MOA ASF case and shipping-ban information
      source_type: webpage
      role: Ban timing and case counts per province
      access_route: Public ministry page
      url: http://www.moa.gov.cn/gk/yjgl_l/
      coverage: 2018 ASF outbreak onward
      last_checked: '2026-08-15'
    - name: NBS monthly CPI and provincial hog output
      source_type: webpage
      role: Deflation (Jan 2018 = 100) and production-scale control
      access_route: Public statistics pages
      url: http://www.stats.gov.cn
      coverage: '2016-2020 CPI; 2017 hog output'
      last_checked: '2026-08-15'
  acquisition_methods:
  - download
  - manual coding
  sample_construction: >-
    All provinces with sufficient reporting kept (Qinghai and Tibet excluded for
    80%/90% missing weeks; Ningxia 209, Shanghai 221, Hainan 230, Guizhou 245
    observed weeks; others 252+). Daily county prices averaged to province-week;
    linear interpolation for missing weeks; nominal prices deflated by NBS
    monthly CPI (Jan 2018 = 100). Documented in the NBER chapter by the same
    authors.
  pipeline_stages:
    - stage: collect
      inputs:
      - zhujiage.com.cn daily county-level prices
      - MOA case/ban dates
      method: Download daily county-level hog prices and cross-check ban dates with news reports
      tools: []
      parameters:
      - period 2016-01-01 to 2020-11-10
      output: Raw daily county price series
      evidence: NBER chapter c14612 section 7.4 (data description)
    - stage: aggregate
      inputs:
      - Raw daily county price series
      method: Simple average of daily prices across available days within each province and week
      tools: []
      parameters:
      - weekly frequency; province level
      output: Weekly provincial price series
      evidence: NBER chapter c14612 section 7.4
    - stage: clean
      inputs:
      - Weekly provincial price series
      method: Exclude Qinghai and Tibet; linear interpolation for missing weeks of the 29 kept provinces
      tools: []
      parameters: []
      output: Balanced 29-province x 255-week nominal panel
      evidence: NBER chapter c14612 section 7.4
    - stage: model
      inputs:
      - Nominal panel
      - NBS monthly CPI
      method: Deflate to real RMB/kg (January 2018 = 100); compute capital-city geodesic distances (R maps package)
      tools:
      - R (maps package)
      parameters: []
      output: Real province-week price panel plus distance and ban-week variables
      evidence: NBER chapter c14612 section 7.4
  constructed_variables:
    - name: Weekly provincial average hog price (real)
      concept: Real RMB per kg province-week price, CPI-deflated
      source_fields:
      - Daily county-level hog prices (zhujiage.com.cn)
      - NBS monthly CPI
      method: Weekly simple average of daily county prices; monthly CPI deflation
      validation: Chapter reports summary statistics and coverage audit per province
      limitations: Pre-2018 weeks have missing days; interpolation fills gaps
    - name: Weeks under inter-province shipping ban (pair)
      concept: Number of weeks a province pair stayed under the live-hog shipping ban
      source_fields:
      - MOA case announcements
      - News reports
      method: Manual date collection and cross-check
      validation: Cross-checked with news reports per chapter
      limitations: None stated in chapter
  validation:
  - Chapter table 7.1 summary statistics; per-province observed-week audit (Ningxia 209 ... Guizhou 245, others 252+)
  - Stationarity of price-deviation series confirmed before spatial estimation
  output:
    unit_of_observation: Province-week
    structure: Balanced panel 29 provinces x 255 weeks
    geography: 29 mainland provinces (excl. Qinghai, Tibet)
    time_span: '2016-01-01 to 2020-11-10'
    key_variables:
    - Real province-week hog price
    - Pairwise distance, ban weeks, partner-province price
    formats: []
  reproducibility:
    level: needs-verification
    starting_point: zhujiage.com.cn daily county-level prices (access unverified) plus MOA and NBS inputs
    code_available: false
    code_url: null
    requirements:
    - Access to zhujiage.com.cn (unverified; unreachable from this environment 2026-08-15)
    - NBS CPI series and MOA ban dates
    - R or any panel software for aggregation/estimation
    blockers:
    - Raw site reachability and current terms unknown
    - Authors' cleaned panel not released anywhere found
  compliance:
    terms_or_license: Site terms of zhujiage.com.cn unverified
    robots_or_rate_limits: Unknown
    personal_or_sensitive_data: none
    redistribution: Not established; do not redistribute scraped content without terms review
    review_needed: false

used_by:
- cite: 'Ma, Delgado & Wang (2024), Risk, arbitrage, and spatial price relationships: Insights from China''s hog market under the African Swine Fever, JDE 166, 10.1016/j.jdeveco.2023.103200'
  doi: https://doi.org/10.1016/j.jdeveco.2023.103200
  journal: Journal of Development Economics
  year: 2024
  dataset_role: Main outcome data (weekly provincial hog prices, 29 provinces, around the 2018 ASF outbreak and shipping ban)
  evidence_type: data-section
  evidence_url: https://www.nber.org/books-and-chapters/risks-agricultural-supply-chains/exploring-spatial-price-relationships-case-african-swine-fever-china
  data_note: >-
    The JDE abstract confirms 'unique weekly data on provincial hog prices'
    (29 provinces) and the ASF natural experiment. The NBER book chapter by the
    same authors (Delgado, Ma & Wang 2023, pp. 139-157, read in full) documents
    the construction: daily county-level prices from www.zhujiage.com.cn
    (2016-01-01 to 2020-11-10), simple averages to province-week, 29 provinces
    (Qinghai/Tibet excluded), linear interpolation, CPI deflation (Jan 2018=100,
    NBS), MOA ban/case data, NBS hog output, geodesic distances. The JDE article
    data section itself is unread (the 2026-09-28 publisher visit reached a CAPTCHA; nominal hybrid-OA/CC-BY metadata is not treated as text access).

provenance:
- source: 'NBER chapter c14612 (Delgado, Ma & Wang 2023, Risks in Agricultural Supply Chains, University of Chicago Press, pp. 139-157), full PDF read 2026-08-15'
  field_scope:
  - raw data source (zhujiage.com.cn daily county-level prices)
  - period (2016-01-01 to 2020-11-10) and panel structure (29 provinces x 255 weeks)
  - aggregation, interpolation and CPI-deflation steps
  - province exclusions (Qinghai, Tibet) and missing-week coverage (Ningxia 209, Shanghai 221, Hainan 230, Guizhou 245)
  - MOA case/ban data source and NBS output/CPI controls
  - four-period division around ASF and ban
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Crossref/OpenAlex records for 10.1016/j.jdeveco.2023.103200
  field_scope:
  - authorship (Meilin Ma, Michael S. Delgado, H. Holly Wang, Purdue AgEcon)
  - abstract wording ('unique weekly data on provincial hog prices', 29 provinces, ASF)
  - hybrid OA status
  added: '2026-08-15'
  confidence: high
  verified: true
- source: >-
    Direct human-browser visit to
    https://www.sciencedirect.com/science/article/pii/S0304387823001566
    (2026-09-28); OpenAlex and Unpaywall metadata for DOI
    10.1016/j.jdeveco.2023.103200
  field_scope:
  - The journal version is catalogued as hybrid OA / CC-BY, but neither registry supplied a PDF or repository copy
  - The live publisher visit stopped at ScienceDirect's CAPTCHA rather than exposing the data section
  - Boundary that nominal open-access metadata must not be represented as a readable journal-text route
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Direct fetch attempts of zhujiage.com.cn (HTTP connection aborted; HTTPS SSL EOF) and Wayback CDX (2008-2010 snapshots confirmed)
  field_scope:
  - current site reachability (unreachable from this environment 2026-08-15)
  - historical site existence
  added: '2026-08-15'
  confidence: med
  verified: false
related_datasets:
- id: china-rural-economic-statistics-1949-1986
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

The paper's asset is a researcher-constructed weekly panel of province-level hog prices (29 provinces, 255 weeks, 2016-01-01 to 2020-11-10) built from daily county-level prices scraped from zhujiage.com.cn, whose unique value is weekly spatial price dynamics around the 2018 ASF shipping ban; the main barrier is that the raw site's current access is unverified (unreachable from this environment) and the authors' cleaned panel is not released.

## Select rules

- Prioritize it for weekly-frequency, province-level hog market integration questions around the ASF outbreak and ban.
- Switch to official NBS/MOA series when only national or coarser frequency suffices, or when reproducibility from a verified public source is mandatory.
- Do not use it for county-level analysis, post-2020 price monitoring, or as a ready-made download (it is a reconstruction).

## Get recipe

1. Read the NBER chapter (public PDF) for the construction recipe and summary statistics. Only use the JDE data section to confirm the journal version if a publisher session actually reaches that text; the checked public visit stopped at a CAPTCHA.
2. Verify zhujiage.com.cn accessibility and terms; if live, download daily county-level prices 2016-01-01 to 2020-11-10.
3. Aggregate to province-week simple averages, exclude Qinghai/Tibet, interpolate missing weeks, deflate by NBS monthly CPI (Jan 2018 = 100).
4. Re-collect MOA ASF case dates and ban timing, and NBS hog output and importer/exporter status for controls.

## Connections and Limitations

Pairwise distance (capital-city geodesic) and ban-week variables are part of the documented construction. The panel is province-week, so county-level joins require the raw feed. The JDE article data section remains unread; the NBER chapter documents the same study and is the current evidence anchor. Site access and author release status are the two unverified conditions that would invalidate a reproduction attempt.
