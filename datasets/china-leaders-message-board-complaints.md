---
schema_version: 3
catalog_status: grounding
id: china-leaders-message-board-complaints
name: '人民网领导留言板 (People''s Daily Online Leader Message Board, MBLL) complaint messages'
aka:
- MBLL
- liuyan.people.com.cn
- 领导留言板
- Message Board for Leaders
- Leader Message Board
- 人民网领导留言板
provider: >-
  人民网 (People's Daily Online), the online arm of People's Daily; operates the
  national leader message board at liuyan.people.com.cn. The public home page
  was again reachable without authentication on 2026-09-28. Its returned HTML
  is a JavaScript-driven front end whose thread anchors use a client-side
  placeholder rather than immediately exposing a safe, concrete thread URL;
  earlier direct observation documented the thread-route shape
  liuyan.people.com.cn/threads/content?tid=NNN.
china_related: true
domains:
- governance
- public-opinion
- text-data
- complaint
- weather
- urban
- government-response

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    City-day panel of complaint-message counts (per million population) built
    from MBLL complaint threads 2014-2018 across 317 prefecture cities, as
    constructed by Han & Zhu (2024 CEJ). The underlying raw asset is the public
    MBLL thread archive (925,023 messages in the paper's window: 325,334 labeled
    'complaint', 215,400 'query', 282,532 'seeking help', 101,757 'others').
    Neither the platform nor the authors release a machine-readable bulk file;
    the paper's extract is reconstructable from public thread pages only with
    substantial scraping and text-classification work.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    Provider identity verified (人民网, liuyan.people.com.cn; public home page
    reachable); paper channel NOW VERIFIED from the author-hosted published
    PDF (hanyajie.com/doc/extreme_weather_complaints.pdf, read in full 2026-08-15):
    the complaint data are MBLL messages labeled 'complaint' (label present from
    Aug 2013; sample 2014-2018), 317 cities, aggregated city-day and normalized
    by city population; content recategorized from the platform's 14 user labels
    into 15 domains via jiebaR segmentation and 556 keywords; weather matched
    from the China Meteorological Data Service Center (844 stations). No data
    availability statement and no replication deposit found. Platform pages are
    readable in a browser but the site is JS-driven; bulk machine collection
    rules are not documented on public pages.
  barrier: >-
    No public bulk download or API for the message archive; the paper's extract
    is unreleased; reconstruction requires page collection (JS-driven site),
    message-label parsing, and the paper's keyword classification protocol
    (556 keywords, jiebaR, manual domain assignment), which is only partially
    specified in the text.

unit_of_observation: >-
  Raw asset: individual complaint message (thread) submitted to a government
  leader on MBLL. Paper asset: prefecture city-day counts of complaints per
  one million population (and per-domain counts).
structure: Raw message archive (cross-section of threads with timestamps and locations); paper constructs a city-day panel
geo_granularity:
- prefecture city (317 cities in the paper)
- message-level location (city identified per complaint)
geography: China, 317 prefecture-level cities (paper sample, 2014-2018); platform itself covers national, provincial, prefecture and county leaders
time_span:
  start: '2006'
  end: ongoing
  last_confirmed_release: '2024'
  coverage_note: >-
    Platform founded 2006; >2 million messages by October 2019 (per the paper's
    data section). The paper restricts to 2014-2018 because the 'complaint'
    message label first appears in August 2013; 925,023 messages in the sample
    window across 317 cities (516,481 city-day observations).
  last_checked: '2026-09-28'
frequency:
- message-level (continuous)
- paper aggregates to city-day
sample_size: >-
  Paper sample: 925,023 messages total (325,334 complaints; 215,400 query;
  282,532 seeking help; 101,757 others) from 317 cities, 2014-2018; 516,481
  city-day observations. Platform total: >2 million messages by Oct 2019.
key_variables:
- Message label chosen by the filer: complaint / seeking help / query / others
- User-chosen content label (14 labels: government services, safety, environment, urban construction, education, transportation, firms, finance, tourism, entertainment, employment, medical system, agriculture, others)
- Paper-recategorized domain (15 domains from 556 keywords, e.g. public service, power shortage, noise, construction, safety)
- Message location (prefecture city) and timestamp
- Government response: reply dummy and time-to-reply (paper-constructed)
- Weather match (city-day averages from CMA stations)

research_fit:
  best_for:
  - Research on citizen-government interaction and local government responsiveness using national online complaint data (2014-2018 window is the evidenced paper extract)
  - Constructing prefecture city-day (or city-year) complaint-intensity measures from a public platform, e.g. for weather/climate, public-service-delivery, or governance studies
  - Text classification exercises on Chinese complaint text with the paper's 15-domain protocol as a template
  choose_over:
  - Choose MBLL over china-aer-squeaky-wheel-citizen-appeals-2020 (12369/CEMS environmental appeals, openICPSR package) when the question is general citizen complaints to leaders rather than environmental hotline appeals
  - Choose MBLL over 12345-hotline-derived datasets (not currently catalogued) when a national cross-city coverage is needed rather than one city's hotline records
  not_good_for:
  - Representative measures of public opinion: complaints are self-selected messages to leaders
  - City coverage outside the paper's 317 cities without re-collection from the platform
  - Machine-readable bulk history: no download or API exists; the paper's extract is not released
  - Identification of treatment effects of government responses (the paper's response analysis is correlational)
  needs_join_for:
  - Weather (China Meteorological Data Service Center daily station data; the paper averages stations within city boundaries)
  - City population (denominator for per-million rates) and city characteristics (statistical yearbooks)
  - Governance/policy variables for response analyses
  variation_available:
  - Daily temperature variation across 317 cities 2014-2018 (the paper's design); message-label variation (complaint vs query/seeking-help as placebo); content-domain variation
  topics:
  - online complaints
  - leader message board
  - citizen-government interaction
  - government responsiveness
  - extreme weather
  - text analysis
  - public service delivery

good_for:
- City-day complaint intensity panels 2014-2018 from a national platform
- Studies of local government responsiveness (reply and time-to-reply)
- Chinese complaint-text classification
identification: []
linkable_keys:
- Prefecture city (name/code normalization needed)
- Date (city-day aggregation)
- Thread ID (tid on the platform)

joins:
- target: china-aer-squeaky-wheel-citizen-appeals-2020
  relation: often-confused-with
  keys:
  - City
  - Year
  method: Both are citizen-complaint assets but different channels (12369 environmental hotline with released openICPSR bundle vs MBLL leader message board with no release); compare by channel, topic and release status
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - City name or code
  - Year
  method: Join city characteristics/population controls; normalize city names to a common code vintage
  evidence_status: plausible

access_routes:
- route: Public platform pages (raw messages)
  access_status: available
  direct_url: https://liuyan.people.com.cn/
  requirements:
  - Public web access for the home page; no account was requested on the
    2026-09-28 home-page check
  - Browser or JS-capable client for the site's dynamic pages
  steps:
  - Browse the home page (provincial leader pages, totals counters, 30-day reply-rate rankings).
  - Locate an actual thread through normal browser navigation before opening its
    documented thread route (liuyan.people.com.cn/threads/content?tid=NNN).
  - Before any collection, obtain a documented permitted bulk route or make a
    project-specific compliance decision; the home page alone does not establish
    that systematic collection is allowed or complete.
  deliverable: Public homepage; individual thread delivery needs a fresh, normal-browser confirmation; no bulk file
  cost: free
  last_checked: '2026-09-28'
  caveat: On 2026-09-28 the home page returned a client-side thread-link placeholder, so this check confirms homepage availability but not a current anonymous thread delivery path. The site remains JS-driven; bulk collection rules and rate limits are not documented on public pages; the paper's exact 2014-2018 extract is not downloadable anywhere.
- route: Paper full text (author-hosted published PDF)
  access_status: available
  direct_url: https://www.hanyajie.com/doc/extreme_weather_complaints.pdf
  requirements: None (public author site)
  steps:
  - Download the published-version PDF (typeset China Economic Journal pages 118-136) for the data section (Section 2), classification protocol, and summary statistics.
  deliverable: Full published text; no data file
  cost: free
  last_checked: '2026-08-15'
  caveat: This is the paper text (evidence of construction), not the dataset.
- route: T&F article page
  access_status: blocked
  direct_url: https://www.tandfonline.com/doi/full/10.1080/17538963.2023.2300869
  requirements:
  - Subscription or library access (T&F returns 403 to automated clients)
  steps:
  - Read the published version via institutional access.
  deliverable: Published article
  cost: paid
  last_checked: '2026-08-15'
  caveat: Closed access; the author-hosted PDF above covers the same content for data purposes.

access:
  url: https://liuyan.people.com.cn/
  cost: free
  license: Platform terms of use not documented on public pages (observed 2026-08-15); messages are public threads
  format:
  - html
  api: false
  how_to_get: >-
    Start from the public home page in a normal browser. Do not treat the
    documented thread URL pattern as a bulk endpoint: first establish a
    permitted, concrete collection route and then apply the paper's
    classification protocol. There is no observed bulk download or API.
caveats:
- The paper's exact extract (925,023 messages, 317 cities, 2014-2018) is NOT released; no DAS in the published text and no replication deposit found (searched 2026-08-15).
- Platform JS-driven: bulk automated collection may face challenges; comply with site terms and be conservative with request rates.
- The 'complaint' label appears only from August 2013; pre-2014 complaint labels are not comparable.
- Content labels are user-chosen and unreliable; the paper's 15-domain recategorization (jiebaR + 556 keywords + manual assignment) is the evidenced protocol but is only partially reproducible from the text alone.

production:
  raw_sources:
  - name: 人民网领导留言板 (MBLL) public thread archive
    source_type: webpage
    role: Complaint messages to government leaders with labels, timestamps, locations
    access_route: Public homepage; JavaScript-driven; no observed bulk route. Individual-thread delivery was not re-confirmed in the 2026-09-28 bounded homepage check.
    url: https://liuyan.people.com.cn/
    coverage: National; 317 prefecture cities in the paper's 2014-2018 window
    last_checked: '2026-08-15'
  - name: China Meteorological Data Service Center station data
    source_type: dataset
    role: Daily weather (max/min/avg temperature, precipitation, humidity, wind, sunshine, pressure) for 844 stations; averaged within city boundaries
    access_route: Official CMA open data service (separate ready-made asset; route per its own portal)
    url: https://data.cma.cn/
    coverage: 844 stations, daily, 2014-2018
    last_checked: '2026-08-15'
  acquisition_methods:
  - page fetch
  - manual coding
  - text mining
  sample_construction: >-
    Paper: all MBLL messages labeled 'complaint' from 317 sample cities,
    2014-2018 (label present from Aug 2013); 325,334 complaint messages from a
    total 925,023 messages. City-day counts normalized by city population
    (per million); content recategorized into 15 domains.
  pipeline_stages:
  - stage: collect
    inputs:
    - MBLL thread pages
    method: Collect messages city-by-city over the sample window (site JS-driven; collection mechanics not documented in the paper)
    output: Message-level corpus with labels, timestamps, locations
    evidence: Paper Section 2.1 (author-hosted PDF, read 2026-08-15); platform pages (read 2026-08-15)
  - stage: classify
    inputs:
    - Message subjects
    method: jiebaR word segmentation in R; stopwords (custom + github list); nouns only; 556 keywords appearing >300 times; 15 domains; manual classification of unambiguous keywords, majority-subject for ambiguous ones, 'others' for keyword-free posts
    tools:
    - R
    - jiebaR
    output: 15-domain complaint categories (public service incl. power shortage, noise, construction, safety, etc.)
    evidence: Paper Section 2.1 (read 2026-08-15)
  - stage: aggregate
    inputs:
    - Classified messages
    - City population
    method: Aggregate to prefecture city-day counts; normalize per million population; weight regressions by city population
    output: City-day complaint panel (516,481 observations)
    evidence: Paper Sections 2-3 (read 2026-08-15)
  - stage: match
    inputs:
    - City-day panel
    - CMA station daily weather
    method: Identify stations within city boundaries; average weather to city-day
    output: City-day panel with weather
    evidence: Paper Section 2.2 (read 2026-08-15)
  constructed_variables:
  - name: complaint rate
    concept: Daily complaints per one million population in a city
    source_fields:
    - Message label
    - Message location and date
    - City population
    method: Count 'complaint'-labeled messages by city-day; divide by city population (per million)
    validation: Summary statistics Table 1 (mean 0.279 per million city-day)
    limitations: Population denominator vintage not spelled out in the text
  - name: content domains (15)
    concept: Recategorized complaint subjects (public service, power shortage, noise, construction, safety, law violation, government services, environment, housing, transportation, education, firm, medical, agriculture, entertainment, others)
    source_fields:
    - Message subject text
    method: jiebaR tokenization; 556 frequent keywords; manual + majority-subject assignment
    validation: Table 6 decomposition; power-shortage subset validated by manual inspection
    limitations: Keyword list is not published in the paper; one complaint can appear in multiple categories (acknowledged in the text)
  - name: government response measures
    concept: Reply dummy and time-to-reply for each complaint
    source_fields:
    - Platform reply records
    method: Dummy for whether the leader replied; days until reply
    validation: Table 8
    limitations: Response behavior of leaders is a governance outcome, not a data-product field
  validation:
  - Summary statistics reconcile with platform totals (paper Table 1)
  - Placebo checks using 'query'/'seeking help'/'others' labels
  output:
    unit_of_observation: Prefecture city-day
    structure: City-day panel 2014-2018 (516,481 observations)
    geography: 317 prefecture cities
    time_span: 2014-2018
    key_variables:
    - Complaint count and rate per million population
    - Domain-specific counts (15 domains)
    - Weather variables (city-day averages)
    - Response dummies and response times
    formats:
    - not released (paper tables only)
  reproducibility:
    level: medium
    starting_point: https://liuyan.people.com.cn/ (raw threads) and the author-hosted PDF for the protocol
    code_available: false
    code_url: ''
    requirements:
    - Web collection tooling with JS handling
    - R + jiebaR for the classification protocol
    - City population series and CMA weather data for the panel
    blockers:
    - No bulk download or API; platform terms for bulk collection undocumented
    - The 556-keyword list and exact stopword set are not published
    - No replication deposit
  compliance:
    terms_or_license: Platform terms not documented on public pages; treat messages as public threads; avoid bulk scraping that disrupts the site
    robots_or_rate_limits: Unknown for the platform; be conservative
    personal_or_sensitive_data: Complaints may contain personal details of citizens; deidentify before any redistribution
    redistribution: No observed license permitting redistribution; cite the platform and the paper
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Han, Yajie & Hongjia Zhu (2024), Extreme Weather and Complaints: Evidence from Chinese Netizens, China Economic Journal 17(1):118-136'
  doi: https://doi.org/10.1080/17538963.2023.2300869
  journal: China Economic Journal
  year: 2024
  dataset_role: Main outcome data - MBLL complaint messages labeled 'complaint' aggregated to prefecture city-day rates (per million population), 2014-2018, 317 cities
  evidence_type: data-section
  evidence_url: https://www.hanyajie.com/doc/extreme_weather_complaints.pdf
  data_note: >-
    Author-hosted published-version PDF read in full 2026-08-15. Section 2.1:
    data from the online complaint platform of People's Daily Online, MBLL
    (liuyan.people.com.cn), founded 2006, >2 million messages by Oct 2019;
    filers label messages 'complaint'/'seeking help'/'query'/'others'; the
    'complaint' label appears from Aug 2013 so the sample is 2014-2018; from
    925,023 total messages, 325,334 are complaints, 215,400 query, 282,532
    seeking help, 101,757 others; 14 user content labels recategorized into
    15 domains via jiebaR + 556 keywords; Section 2.2: weather from the China
    Meteorological Data Service Center (844 stations), stations within city
    boundaries averaged to city-day; 317 sample cities, 516,481 city-day
    observations; response measures: reply dummy and time-to-reply (Section 6).
    No DAS and no replication deposit in the text.

provenance:
- source: Author-hosted published PDF https://www.hanyajie.com/doc/extreme_weather_complaints.pdf (downloaded and read in full 2026-08-15)
  field_scope:
  - MBLL as the data source (platform identity, founding year, message totals)
  - Sample construction (2014-2018, 317 cities, 925,023 messages)
  - Classification protocol (jiebaR, 556 keywords, 15 domains)
  - Weather matching (CMA, 844 stations, city-day averages)
  - Government response measures
  - Absence of DAS/replication
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Semantic Scholar abstract for DOI 10.1080/17538963.2023.2300869 (fetched 2026-08-15)
  field_scope:
  - Abstract-level findings (+11.1% on hot days; category decomposition shares)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Platform home page liuyan.people.com.cn (read 2026-08-15 by an earlier unit; recorded in the candidate ledger)
  field_scope:
  - Provider identity and public page structure (thread URLs, counters)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Platform home page https://liuyan.people.com.cn/ (anonymous bounded request, 2026-09-28)
  field_scope:
  - Public homepage returned HTTP 200 with title '领导留言板-人民网'
  - Returned thread anchors were client-side templates rather than a concrete homepage-linked thread to inspect safely
  - No claim about an individual message, bulk access, terms, completeness, or paper-extract availability
  added: '2026-09-28'
  confidence: high
  verified: true
- source: OpenAlex W4390541983 / Crossref (fetched 2026-08-15)
  field_scope:
  - Publication identity (CEJ 17(1), 2024; authors Han & Zhu)
  - Closed access, no OA locations
  added: '2026-08-15'
  confidence: high
  verified: true
- source: OpenAlex W3167138003 (SSRN preprint 3805516, 2021, Han/Qin/Zhu)
  field_scope:
  - Working-paper existence; SSRN pages blocked for automated clients (abstract read via S2)
  added: '2026-08-15'
  confidence: med
  verified: true

related_datasets:
- id: china-aer-squeaky-wheel-citizen-appeals-2020
  relation: often-confused-with
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

人民网领导留言板 (MBLL, liuyan.people.com.cn) is China's national leader message board — the public raw source of the Han & Zhu (2024 CEJ) complaint dataset (925,023 messages, 325,334 complaints, 317 cities, 2014-2018, city-day complaint rates) — but there is no bulk download: a researcher must collect public thread pages and rebuild the paper's classification protocol, and the paper's extract itself is unreleased.

## Select rules

- Prioritize MBLL when the research needs a national, cross-city measure of citizen complaints to government leaders (evidenced window 2014-2018, 317 cities) — e.g. weather/complaint, public-service delivery, or government-responsiveness designs.
- Switch to china-aer-squeaky-wheel-citizen-appeals-2020 when the question is environmental appeals through the 12369 hotline and a released openICPSR bundle is needed; the two are different channels and topics.
- Do not use this record to promise a downloadable complaint panel: neither the platform nor the paper releases machine-readable bulk data.

## Get recipe

1. Read the data section of the author-hosted published PDF (hanyajie.com/doc/extreme_weather_complaints.pdf) — free and authoritative for construction (Section 2).
2. Browse liuyan.people.com.cn in a browser to confirm current page structure and thread URLs (liuyan.people.com.cn/threads/content?tid=NNN); note that the site is JS-driven.
3. For a research panel: collect complaint threads for the needed cities/window, parse label/timestamp/location/text, and rebuild the 15-domain classification with jiebaR + keyword protocol (the 556-keyword list itself is not published — this is the main reconstruction burden).
4. Match city-day weather from the China Meteorological Data Service Center and normalize complaint counts by city population.
5. Do not expect a replication package: none exists, and the paper has no data-availability statement.

## Connections and Limitations

The natural unit is the complaint message, aggregated to prefecture city-day; joins need city-name/code normalization and a population series. The platform's message labels are user-chosen (the 'complaint' label only exists from August 2013), and content labels are unreliable — the paper's recategorization is the evidenced protocol but its keyword list is unpublished. No bulk route, no API, no release: the biggest practical barrier is collection and classification effort, and platform bulk-access terms are undocumented. The paper's weather/complaint identification design belongs to the Econ-Variation repository, not this data record.
