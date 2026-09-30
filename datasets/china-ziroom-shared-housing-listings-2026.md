---
schema_version: 3
catalog_status: grounding
id: china-ziroom-shared-housing-listings-2026
name: Ziroom (自如) Nanjing bedroom rental listings, weekly web-scraped July 2021-June 2022 (Cao 2026 Urban Studies)
aka:
- 自如南京合租房源
- Ziroom Nanjing bedroom listings
- 自如网房源数据
- Gender homophily and rent premiums in platform-mediated shared housing
provider: Data collected by the paper's author (Weiyi Cao, Wageningen University/MIT) by weekly web scraping of the Ziroom (自如) website; the platform operates the listings (rents units from owners, renovates, sublets bedrooms via app/website). Wageningen's research portal links an open-access article PDF, but no dataset or code delivery route is established in the checked sources.
china_related: true
domains:
- urban
- housing
- platform-economy
- inequality
- gender
- real-estate

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: "The paper's analysis dataset: 42,423 unique bedroom listings (after deduplication of 373,964 weekly raw listings) for shared apartments on Ziroom in Nanjing, July 2021-June 2022, with hedonic price analysis of gender composition (all-female/all-male/mixed roommate units) interacted with platform room status (reserve/sign/sublease). No public delivery route was found in the checked article and institutional listing; this does not establish that the author cannot share an archived sample."
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: A single-author hedonic study of bedroom-level rents on Ziroom in Nanjing. The institutional PDF, actually retrieved 2026-09-28, confirms weekly collection July 2021-June 2022 and retention of each listing's most recent observation (373,964 raw observations to 42,423 unique bedrooms). It also documents administrative districts, Euclidean accessibility distances, complex-level average apartment transaction price and management-fee controls. Neither the checked article nor its institutional listing supplies a dataset/code route. A new collection would be a different-period asset, not reproduction of these historical snapshots; author-held archives or another legitimate historical source remain unverified.
  barrier: No verified delivery route to the historical sample or code; archive retention and author-sharing conditions unknown. Current Ziroom collection terms and any historical listing service are unverified.

unit_of_observation: Bedroom listing (one 卧室 within a shared apartment/unit on Ziroom, leased independently) at the weekly scrape date; deduplicated to one observation per unique listing (most recent observation kept)
structure: Repeated cross-section of listings (weekly snapshots) collapsed to unique listing observations
geo_granularity:
- neighborhood (Nanjing)
- Nanjing city (second-tier city, ~9.58 million resident population per the paper)
geography: Nanjing (南京市), Jiangsu Province, China - Ziroom bedroom listings only
time_span:
  start: '2021-07'
  end: '2022-06'
  last_confirmed_release: null
  coverage_note: Weekly collection over 52 weeks (July 2021-June 2022), confirmed in the institutional article PDF, p. 8. No later waves or public sample delivery are established in the checked sources.
  last_checked: '2026-09-28'
frequency:
- weekly (collection frequency; analysis uses one observation per unique listing)
sample_size: 373,964 raw weekly listings -> 42,423 unique bedroom listings after deduplication (most recent observation per listing retained)
key_variables:
- Monthly rent of the bedroom (RMB; ln_rent dependent variable)
- Roommate gender composition (all-female / all-male / mixed-gender unit)
- "Platform room status: reserve (standard rent), sign (immediate move-in, discounted), sublease (listed by current tenant)"
- "Bedroom attributes: size (area), window orientation, independent bathroom, independent balcony, furnishing style"
- "Apartment attributes: number of bedrooms, number of 'ting' (厅, living rooms)"
- "Complex/building attributes: elevator availability, total stories, construction year, floor-area ratio"
- Location: distance to nearest metro station (mean 1,347-1,453 m across gender groups), distance to Xinjiekou (Nanjing city/employment center)
- Month of listing collection
- Administrative district (paper Table 1 lists Jianye, Qixia, Jiangning, Pukou, Xuanwu, Qinhuai, Yuhuatai and Gulou; not a claim of all-Nanjing administrative coverage)
- Average apartment transaction price within the residential complex (quality proxy, CNY/m2; its underlying source and matching procedure are not specified in the checked data section)
- Monthly management fee (additional control)

research_fit:
  best_for:
  - "Platform-mediated shared-housing pricing in China: how algorithmic platform pricing (reserve/sign/sublease) interacts with roommate gender composition to set bedroom rents"
  - Gender homophily as a priced amenity in formalized (platform) rental markets; PropTech and housing-inequality questions at the listing level
  - Hedonic analyses of bedroom-level attributes (orientation, bathroom, balcony, furnishing) in a second-tier Chinese city
  choose_over:
  - Choose over china-jrs-sweating-assets-housing-transactions-2026 (second-hand sales transactions, 26 cities) when the question is the rental side of the market or platform-mediated shared housing
  - Choose over china-shanghai-rental-records-gentrification-2025 (candidate; Shanghai individual rental records with move tracking) when the question is Nanjing or platform listing dynamics specifically; that candidate is ungrounded
  not_good_for:
  - Any question outside Nanjing or outside July 2021-June 2022 (single-city, single-year sample)
  - "Actual transactions or realized rents: the data are listing prices on the platform, not signed contracts; sublease rents are tenant-set"
  - Tenant outcomes, move behaviour, or renter characteristics (only listing-level attributes; no tenant panel)
  - "Generalizing to lower-income or non-platform renters (paper notes its own limitation: Ziroom users are mainly young, college-educated migrant professionals)"
  needs_join_for:
  - Additional neighborhood socioeconomic context or amenities beyond the documented district and accessibility controls; the complex transaction-price proxy is documented, but its source and matching key remain unknown
  - Gender-of-occupant outcomes or tenure dynamics (not observed at listing level)
  variation_available:
  - Cross-sectional variation in gender composition and room status within and across apartments; platform pricing regime (reserve vs sign vs sublease) as the identification-relevant dimension
  topics:
  - platform real estate
  - shared housing
  - rent premiums
  - gender homophily
  - hedonic pricing
  - PropTech
  - Nanjing
  - China housing

good_for:
- Platform-mediated shared-rental pricing and gender premium analysis in China
identification: []
linkable_keys:
- Listing identity (internal; duplicates removed by retaining most recent observation)
- Apartment/unit (bedrooms within the same unit share apartment-level attributes)
- Neighborhood (location attributes per listing; no public ID scheme documented)
- Administrative district (documented categories; no released geographic code scheme)

joins:
- target: china-jrs-sweating-assets-housing-transactions-2026
  relation: complement
  keys:
  - City
  - Neighborhood
  method: Rental listings (this record) vs second-hand sales transactions; both price-side assets for Nanjing-related work, different market segments; join on city/neighborhood names requires geocoding (not documented in either paper)
  evidence_status: plausible

access_routes:
- route: Wageningen institutional article PDF (documentation only)
  access_status: available
  direct_url: https://edepot.wur.nl/721107
  requirements:
  - No login was required for the successful ordinary HTTP GET on 2026-09-28; the WUR publication listing labels this document CC BY
  steps:
  - Follow the article's Access to Document link in the WUR research portal to edepot.wur.nl/721107.
  - Read pp. 7-9 for collection, deduplication and variable definitions, and Tables 1 and 3 for descriptive coverage and controls.
  - Distinguish the 26-page article from a dataset release; it supplies no verified sample or code download route.
  deliverable: Article PDF (26 pages), not the 42,423-row dataset or weekly raw snapshots
  cost: free
  last_checked: '2026-09-28'
  caveat: The web-reading tool returned 403 and an HTTP HEAD returned 405, but an ordinary GET returned HTTP 200 application/pdf and readable article text. Prefer the verified document route; a tool-specific failure does not prove provider withdrawal.
- route: Open-access article full text (documents the data; does not release it)
  access_status: blocked-this-session
  direct_url: https://sage.cnpereading.com/doi/10.1177/00420980261456151
  requirements:
  - The mirror served full text on 2026-08-14, but the 2026-09-28 visit returned a human-verification page; use the institutional PDF above for current documentation
  steps:
  - Read the paper's 'Data and method' section for the collection protocol (weekly scrape, July 2021-June 2022, 52 weeks; 373,964 raw -> 42,423 unique listings).
  - Note that no data-availability statement exists in the article; no replication package was found.
  deliverable: Full methodological documentation of the Ziroom scrape and variables; NOT the dataset
  cost: free
  last_checked: '2026-09-28'
  caveat: Earlier successful full-text access is retained as provenance, not a guarantee that this mirror currently delivers text.
- route: Author's Wageningen PhD thesis (likely contains the same or adjacent analysis)
  access_status: blocked-this-session
  direct_url: https://doi.org/10.18174/681437
  requirements:
  - "None (thesis 'Housing the 'Others': Migrant and gender disparities in housing cost, satisfaction, and opportunity', Wageningen University 2025-04-16, 198 pp; official PDF link https://edepot.wur.nl/681437)"
  steps:
  - Follow the WUR thesis record's PDF link to edepot.wur.nl/681437; verify actual document delivery before relying on chapter-level claims.
  deliverable: Thesis text incl. the Nanjing platform-data chapters (chapter-level data sections unread this session)
  cost: free
  last_checked: '2026-09-28'
  caveat: The WUR thesis listing and PDF link are verified; the web-reading tool could not access the PDF this session. Thesis chapter contents and any data-sharing details remain unread, and human-browser success is not established.
- route: Forward reconstruction by scraping Ziroom (ziroom.com)
  access_status: needs-verification
  direct_url: https://www.ziroom.com
  requirements:
  - A current scrape of Ziroom listings is technically conceivable but the platform's terms, anti-bot measures, and listing schema are unverified
  steps:
  - Verify current Ziroom website/app terms and structure before considering new collection; separately check whether historical snapshots are available rather than assuming their retention or deletion.
  deliverable: A forward-looking listing dataset with similar fields (rent, room status, gender composition, attributes) for a new period; NOT the paper's sample
  cost: free
  last_checked: '2026-08-14'
  caveat: No evidence this session on current Ziroom scrape-ability or terms; do not treat as a route to the paper's data.

production:
  raw_sources:
  - name: Ziroom (自如) website bedroom listing pages (ziroom.com), Nanjing
    source_type: webpage
    role: Raw input - weekly snapshots of all visible bedroom listings with rent, room status, gender composition, bedroom/apartment/complex/location attributes
    access_route: Website scraped by the author in 2021-07 to 2022-06; current access to those historical snapshots is unverified
    url: https://www.ziroom.com
    coverage: Nanjing listings only; 52 weekly snapshots July 2021-June 2022; 373,964 raw listing observations
    last_checked: '2026-08-14'
  acquisition_methods:
  - crawl (weekly web scrape by the author; mechanism details beyond 'web-scraped' not specified in the paper)
  sample_construction: All visible Nanjing Ziroom bedroom listings captured weekly for 52 weeks; duplicates across weeks removed by retaining the most recent observation of each listing (final n = 42,423 unique bedrooms).
  pipeline_stages:
  - stage: collect
    inputs:
    - Ziroom website listing pages
    method: Weekly scraping over 52 weeks (July 2021-June 2022); the paper does not specify the scraper implementation, parsing library, or anti-bot handling
    tools: []
    parameters:
    - weekly frequency
    - 52 weeks (2021-07 to 2022-06)
    output: Raw listing corpus (373,964 observations)
    evidence: Paper data section (read in full 2026-08-14 via CNPeReading mirror)
  - stage: clean
    inputs:
    - Raw listing corpus
    method: Deduplication of listings active across multiple weeks, keeping the most recent observation; gender composition classified into all-female / all-male / mixed
    tools: []
    parameters:
    - "duplicate rule: retain most recent observation per listing"
    output: Analysis dataset of 42,423 unique bedroom listings
    evidence: Paper data section
  constructed_variables:
  - name: Roommate gender composition
    concept: Gender composition of the leased bedrooms within the apartment at listing time (all-female / all-male / mixed)
    source_fields:
    - Platform listing gender info (composition evolves with tenant turnover)
    method: Classification into three categories from listing data
    validation: None documented beyond descriptive balance checks in the paper
    limitations: Cross-sectional at listing time; turnover not observed
  - name: Platform room status
    concept: reserve (standard algorithm-set rent), sign (immediate move-in, discounted), sublease (tenant-listed, tenant-set rent)
    source_fields:
    - Listing status field
    method: Direct platform field
    validation: Paper interprets coefficients against its description of Ziroom's dynamic pricing
    limitations: Status is point-in-time per listing observation
  validation:
  - Descriptive balance checks across gender groups (distances to metro/Xinjiekou, bedrooms per apartment, duplicate counts)
  output:
    unit_of_observation: Unique bedroom listing (deduplicated)
    structure: Cross-sectional hedonic analysis dataset (42,423 rows) built from weekly snapshots
    geography: Nanjing, China
    time_span: 2021-07 to 2022-06
    key_variables:
    - ln_rent, gender composition, room status, bedroom attributes, apartment attributes, location attributes
    formats:
    - unreleased (no files found)
  reproducibility:
    level: not-reproducible
    starting_point: Institutional article PDF documents the main collection and analysis; no public dataset/code delivery is established in the checked sources
    code_available: false
    code_url: null
    requirements:
    - A new collection needs separately verified platform access and terms; it would not reproduce the historical snapshots
    blockers:
    - Historical snapshot availability and author-archive sharing conditions unknown
    - No dataset/code delivery route or data-availability statement found in the checked article/institutional listing; earlier search negatives do not prove that no release or archive exists
    - Source and matching procedure for the complex-level apartment transaction-price control remain unspecified in the checked data section
  compliance:
    terms_or_license: Ziroom website terms at collection time unverified; paper does not document consent or terms
    robots_or_rate_limits: Unverified for ziroom.com
    personal_or_sensitive_data: Listing-level rental data (addresses/room attributes); no tenant identities in the described fields
    redistribution: Not applicable (no data released); article is CC BY
    review_needed: Verify current Ziroom terms before any new collection; do not redistribute any scraped data without platform authorization

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Cao, Weiyi (2026), Gender homophily and rent premiums in platform-mediated shared housing: Evidence from Ziroom in urban China'
  doi: https://doi.org/10.1177/00420980261456151
  journal: Urban Studies
  year: 2026
  dataset_role: Main data - weekly web-scraped Ziroom bedroom listings in Nanjing (373,964 raw -> 42,423 unique, July 2021-June 2022) used for hedonic rent regressions on roommate gender composition and platform room status
  evidence_type: data-section
  evidence_url: https://edepot.wur.nl/721107
  data_note: "The institutional 26-page article PDF was actually retrieved by HTTP GET and read 2026-09-28, independently of the earlier mirror. Data and method, pp. 7-9, confirms weekly collection July 2021-June 2022, most-recent-observation deduplication (373,964 to 42,423), and the bedroom/apartment/building/complex controls. Page 9 specifies Euclidean distances, administrative district, complex-level apartment transaction-price proxy and monthly management fees. No sample/code download or data-availability statement was found in the article; the thesis remains an unread documentation lead. These are paper-use facts, not evidence of current data delivery."

provenance:
- source: https://edepot.wur.nl/721107 and https://research.wur.nl/en/publications/gender-homophily-and-rent-premiums-in-platform-mediated-shared-ho/ (read 2026-09-28)
  field_scope:
  - Institutional Access to Document link and document-level CC BY label
  - Successful HTTP GET delivered a 26-page article PDF despite web-tool 403 and HEAD 405
  - Data and method pp. 7-9 and Table 1 confirm collection, deduplication, district/accessibility and additional price/management-fee controls
  - Article documentation is not a delivered sample; no dataset/code route is established by the checked document or institutional listing
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://sage.cnpereading.com/doi/10.1177/00420980261456151 and https://research.wur.nl/en/publications/housing-the-others-migrant-and-gender-disparities-in-housing-cost/ (checked 2026-09-28)
  field_scope:
  - Mirror currently returned human verification rather than article text
  - Official thesis listing still links edepot.wur.nl/681437, but thesis contents were not retrieved with the web-reading tool
  - Neither a past scrape window nor search negatives proves author archive deletion or impossibility of legitimate historical delivery
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Paper full text (data section, tables, limitations) read via CNPeReading mirror of SAGE (sage.cnpereading.com/doi/10.1177/00420980261456151), 2026-08-14
  field_scope:
  - collection window and frequency
  - raw and deduplicated counts
  - observation unit and variables
  - pricing mechanism interpretation (reserve/sign/sublease)
  - no-DAS status
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Crossref + OpenAlex + Semantic Scholar (paper identity, hybrid CC BY OA status; WUR Pure page for the thesis DOI 10.18174/681437 and edepot PDF link)
  field_scope:
  - bibliographic identity
  - OA status
  - thesis existence and download link
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Negative checks (DataCite/OpenAlex/Semantic Scholar searches found no replication dataset for the paper DOI)
  field_scope:
  - no replication dataset found in the named searches on that date, not proof of universal absence
  added: '2026-08-14'
  confidence: med
  verified: false

related_datasets:
- id: china-jrs-sweating-assets-housing-transactions-2026
  relation: complement
---

## Positioning in one sentence

Cao (2026, Urban Studies) documents a researcher web-scrape of 42,423 unique Ziroom bedroom listings in Nanjing (373,964 weekly observations, July 2021-June 2022). The verified institutional PDF supports the sample identity and main fields, but not a data download or exact reconstruction. The record helps researchers assess suitability without mistaking accessible documentation for an accessible sample.

## Select rules

- Use this record when a research idea needs Chinese platform-mediated shared-rental pricing at the bedroom level - gender composition, algorithmic room-status pricing, or PropTech-driven rent discrimination in a second-tier city.
- Choose china-jrs-sweating-assets-housing-transactions-2026 for the sales side of the market, or the Shanghai rental candidate when Shanghai/move tracking is the target; neither substitutes for this listing-level Nanjing product.
- Do NOT use it for transaction prices, tenant outcomes, other cities, or any period outside July 2021-June 2022.

## Get recipe

1. Start with the institution-linked article PDF at https://edepot.wur.nl/721107; it actually delivered readable text on 2026-09-28. Read pp. 7-9 and Tables 1 and 3 for the sample and controls. The earlier mirror currently stops at human verification.
2. No public sample/code route was found in the checked article and institutional listing. Before planning this historical sample, confirm archive availability, sharing conditions, listing identifiers and the source/match of the complex transaction-price proxy. Author clarification is a possible next investigation, not an established sharing route.
3. A separately authorized new collection could produce a similar asset for a new period; it does not reproduce the original 52 weekly snapshots. Current platform terms, schema and historical retention remain unverified.
4. The official thesis listing links DOI 10.18174/681437 and edepot.wur.nl/681437. Its chapter-level details remain unread; verify delivery before treating it as fuller construction or data-sharing evidence.

## Connections and Limitations

- Observation unit is the deduplicated bedroom listing at its most recent weekly observation; duplicates in the raw data (avg 8.0-8.9 occurrences per listing) are a platform-tenure signal, not repeated units in the analysis.
- Rents are platform listing rents, not contracts: 'reserve' is the algorithm-set standard, 'sign' is discounted for immediate move-in, 'sublease' rents are set by current tenants - the paper exploits exactly this status variation.
- Coverage is Nanjing-only and single-year; the paper's own limitation: Ziroom users skew young, college-educated, migrant professionals, so strict gender-homophily or low-income renters may self-select out of the platform.
- Exact historical reconstruction is not established: no sample/code route, archive-sharing conditions or historical source delivery are verified. This is an evidence gap, not proof that the author has lost the data or that a legitimate historical route is impossible.
- The paper uses administrative districts and a complex-level transaction-price proxy in addition to bedroom rents. The proxy's source and matching procedure are not specified in the checked data section, so it cannot simply be assumed to come from the Ziroom listing or from the distinct JRS housing sample.
