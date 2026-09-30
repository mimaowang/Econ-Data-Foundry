---
schema_version: 3
catalog_status: ready
id: china-hk-2047-lease-housing-transactions-2024
name: Hong Kong housing transaction data with 2047 land-lease-horizon variation (He, Hu, Wang & Yao 2024 AER)
aka:
- Valuing Long-Term Property Rights replication data
- EPRC Hong Kong residential transactions (1992-2020 extract)
- openICPSR project 196501
provider: EPRC Ltd. (commercial vendor of Hong Kong Land Registry electronic transaction data) for transactions; Land Registry (website) for land-auction data; Hong Kong Census and Statistics Department (1% quinquennial census) and district council election results for demographics/political sentiment; replication deposit at ICPSR/openICPSR
china_related: true
domains:
- housing
- urban
- asset-pricing
- political-risk
- real-estate

data_pathway:
  mode: hybrid
  origin: researcher-collected
  target_artifact: >-
    Transaction-level hedonic dataset of 551,790 second-hand private residential
    transactions in Hong Kong (January 1998 - February 2020, 17 districts, 45
    subdistricts) with land-lease expiration year, geocoded amenities, district
    demographics, and political-sentiment measures, used to value lease-horizon
    exposure to the 2047 regime shift. Published as openICPSR replication package
    10.3886/E196501V1 ("Replication package including data and code", ICPSR, 2024).
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The paper's full text documents the data: all residential property transactions
    in Hong Kong were obtained from EPRC Ltd. (which purchased all electronic
    transaction data from the Land Registry), covering January 1992 to February 2020
    with housing characteristics, lease expiration year, and transaction details;
    land-auction data came from the Land Registry website, matched by land lot
    number; district demographics from the 1% quinquennial censuses (2001, 2006,
    2011, 2016) and district council election results (1999-2019). The final sample
    is 551,790 transactions after exclusions. The AER article page links the
    replication package to openICPSR (10.3886/E196501V1); DataCite confirms the
    deposit. The deposit's file manifest has not been opened (openICPSR blocks
    automated clients).
  barrier: >-
    openICPSR project pages return 403 to automated clients; the file manifest and
    formats are unverified. The raw EPRC/Land Registry transaction data are
    commercially licensed; researchers wanting the full EPRC extract must purchase
    it, and the paper's exact extract vintage (through February 2020) is not a
    public file.

unit_of_observation: Second-hand private residential property transaction (one registered transaction per record)
structure: Transaction-level repeated cross-section with property, building, district, and lease attributes
geo_granularity:
- "property/building (geocoded: latitude/longitude)"
- district (17) and subdistrict (45)
geography: Hong Kong (Hong Kong Island, Kowloon, New Territories; Islands District excluded)
time_span:
  start: '1992-01'
  end: '2020-02'
  last_confirmed_release: '2024-06-19'
  coverage_note: >-
    EPRC data cover January 1992 - February 2020; the analysis sample keeps
    transactions January 1998 - February 2020 (pre-1998 excluded for registration
    consistency around the 1997 handover). Replication deposit registered
    2024-06-19 (DataCite).
  last_checked: '2026-08-15'
frequency:
- transaction-level (dates within January 1998 - February 2020)
sample_size: 551,790 residential transactions in 17 districts and 45 subdistricts (analysis sample)
key_variables:
- Transaction price (total and unit price; log price used as dependent variable)
- Land lease expiration year (from EPRC); auction date and land price (Land Registry, matched by lot number)
- Address, building construction year and month, district name/code, floor and unit numbers
- Property amenities (swimming pool, club house), bay window size, net living area, bedrooms, living rooms
- Transaction sale date, buyer and seller names
- Geocoded distances: MTR, bus stop, hospital, school (K-12), university, coastline
- District demographics (1% censuses 2001/2006/2011/2016) and district council pro-democracy seat share (elections 1999-2019)

research_fit:
  best_for:
  - Valuing long-term property rights and lease-horizon exposure to political regime risk (2047 extension protection)
  - Hedonic analysis of Hong Kong housing transactions with lease type and remaining lease horizon
  - Comparing protected (auto-extended to 2097) vs unprotected (HKSAR-granted, post-2047 expiry) and colonial lease discounts
  - Spillover and price-path analyses approaching a known political deadline
  choose_over:
  - Choose this over mainland housing transaction candidates (china-beike-housing-transactions-2026 etc.) when the research question is Hong Kong lease/regime-risk variation.
  - Choose this over RVD or Land Registry raw data when the researcher wants the paper's cleaned transaction-level sample with lease-classification and amenities already constructed.
  - For a representative mainland housing market, switch to mainland transaction or survey assets.
  not_good_for:
  - Mainland China housing markets (Hong Kong only)
  - Public housing, houses/townhomes, non-arm's-length deals, and Islands District (excluded from the sample)
  - Post-February 2020 transactions (data end) or rental-market analysis beyond the paper's placebo checks
  - Reconstructing the paper's exact sample without the EPRC extract and the lease-classification rules
  needs_join_for:
  - Rental transaction data (used only for placebo tests in the paper)
  - District-level demographics and political sentiment (already merged in the paper from census/elections)
  - Any post-2020 price or policy data for updating the analysis
  variation_available:
  - Lease expiration before vs after July 1, 2047 (treatment: HKSAR-granted unprotected leases; colonial leases) vs control (auto-extended to 2097)
  - Remaining lease horizon continuous variation and time-to-2047 discount path
  - These are data-side variation dimensions; the institutional design belongs to the Econ-Variation repository.
  topics:
  - housing prices
  - land lease
  - political risk
  - property rights
  - Hong Kong
  - hedonic regression

good_for:
- Hedonic valuation of lease-horizon and renewal-risk discounts in Hong Kong housing
- Political-regime-shift pricing (2047) and time-varying discount patterns
- Spillover analyses using Hong Kong transaction-level data (same EPRC data used by Bhattacharya et al. 2021 on "haunted" houses)
identification:
- This is a housing-transaction and replication-data asset, not a stand-alone causal-variation record. A researcher can reproduce the paper's documented lease classification from the released route, but must evaluate identification separately for any new design.
linkable_keys:
- Land lot number (for land-auction matching)
- Building unique ID (per paper's exclusion criteria)
- District and subdistrict codes
- Address/geocoded location (latitude/longitude)
- Transaction date

joins: []
# The candidate china-hk-metro-smartcard-trips-2025 (transit smartcard trips) is a
# different unit and market segment; it is a candidate-ledger lead, not an active
# dataset, so no join target is declared.
# Mainland housing transaction products are separate markets; keep HK lease data
# distinct (no merge target declared).

access_routes:
- route: openICPSR replication deposit (AEA Data and Code policy)
  access_status: available-with-conditions
  direct_url: https://doi.org/10.3886/E196501V1
  requirements:
  - Free ICPSR/openICPSR account; download terms per the deposit
  steps:
  - Open the AER article page (doi.org/10.1257/aer.20211242) and follow the Additional Materials > Replication Package link (https://doi.org/10.3886/E196501V1).
  - Alternatively go directly to https://www.openicpsr.org/openicpsr/project/196501/version/V1/view.
  - Use a human browser/account to obtain the current deposit, then download and read its README/manifest to confirm included files (transactions, code, constructed variables).
  deliverable: Replication package including data and code (per DataCite description); exact manifest unverified (openICPSR 403 to automated clients).
  cost: free
  last_checked: '2026-09-28'
  caveat: The current DataCite DOI remains findable and describes a v1 ICPSR replication package including data and code. openICPSR returned 403 to this automated client and DataCite exposes neither licence nor file manifest, so the deposit may include derived/cleaned data rather than the full raw EPRC extract; verify before treating it as the complete transaction history.
- route: EPRC Ltd. / Hong Kong Land Registry commercial extract
  access_status: available-with-conditions
  direct_url: needs-verification
  requirements:
  - Commercial license/purchase from EPRC Ltd. (or the Land Registry electronic data)
  - Payment; terms per vendor
  steps:
  - Contact EPRC Ltd. for the residential transaction database covering the required period.
  - Replicate the paper's sample filters (private, arm's-length, non-Islands, 1998-2020, 1% price trimming) and lease-classification rules.
  deliverable: Full electronic transaction data (1992-2020 vintage as purchased); requires reconstructing the paper's cleaning pipeline.
  cost: paid
  last_checked: '2026-08-15'
  caveat: The paper names EPRC Ltd. as the vendor; current pricing, coverage, and licensing are unverified this round.
- route: Hong Kong Land Registry website (land-auction and transaction records)
  access_status: available-with-conditions
  direct_url: https://www.landreg.gov.hk/
  requirements:
  - Public access with possible search fees; terms per Land Registry
  steps:
  - Obtain land-auction data (price, date) and match to housing transactions by land lot number as the paper does.
  deliverable: Public land records; building the full transaction panel still requires the commercial extract or registry bulk data.
  cost: mixed
  last_checked: '2026-08-15'
  caveat: The paper used the Land Registry website for auction data only; the full transaction history came from EPRC.

access:
  url: https://doi.org/10.3886/E196501V1
  cost: free
  license: ICPSR deposit terms; EPRC/Land Registry data are separately licensed commercial/public data
  format:
  - replication package (data + code), formats unverified
  api: false
  how_to_get: Resolve DOI 10.3886/E196501V1 or follow the AER Replication Package link to openICPSR project 196501 V1, then use a human browser/account to inspect and obtain the deposit described as including data and code. For the raw transaction history, purchase from EPRC Ltd. or use Land Registry records and rebuild the sample.

caveats:
- EPRC data start January 1992 but the analysis sample starts 1998 (registration-consistency filters around the 1997 handover).
- The final sample excludes public housing (housing ~46% of the population), houses/townhomes, non-arm's-length deals, and Islands District.
- "Lease classification (control: expires 2047-06-30, auto-extended to 2097; treatment: post-2047-07-01 HKSAR leases and colonial leases) is the paper's core constructed variable; reuse requires the same rules."
- The openICPSR deposit manifest is unverified (403 to automated clients); the exact contents (raw vs derived data) remain unknown.
- EPRC's current commercial terms are unverified this round.

production:
  raw_sources:
  - name: EPRC Ltd. residential transaction data (from Hong Kong Land Registry electronic records)
    source_type: dataset
    role: All residential property transactions with characteristics and lease expiration year
    access_route: Commercial purchase from EPRC Ltd.
    url: needs-verification
    coverage: January 1992 - February 2020 (as purchased by the authors)
    last_checked: '2026-08-15'
  - name: Hong Kong Land Registry website land-auction data
    source_type: webpage
    role: Land auction price and auction date for lease classification (before/after 2047-07-01)
    access_route: Public website
    url: https://www.landreg.gov.hk/
    coverage: Land lots matching the sample; matched by land lot number
    last_checked: '2026-08-15'
  - name: Hong Kong 1% Quinquennial Population Census (2001, 2006, 2011, 2016)
    source_type: dataset
    role: District-level demographic characteristics
    access_route: Public statistics; restricted microdata not needed for district aggregates
    url: https://www.censtatd.gov.hk/
    coverage: District-level census waves 2001-2016
    last_checked: '2026-08-15'
  - name: Hong Kong district council election results (1999, 2003, 2007, 2011, 2015, 2019)
    source_type: dataset
    role: District-level pro-democracy seat share (political sentiment)
    access_route: Public election records
    url: needs-verification
    coverage: Six election years
    last_checked: '2026-08-15'
  acquisition_methods:
  - commercial purchase (EPRC)
  - public website retrieval (Land Registry auctions)
  - public statistics (census, elections)
  - geocoding of buildings
  sample_construction: >-
    Start with all EPRC residential transactions; keep private housing with
    market-driven prices; drop missing lease-expiration year, price, date, or floor
    number; exclude pre-1998 transactions (registration-consistency around the 1997
    handover); exclude houses/townhomes, non-arm's-length transactions, and Islands
    District; trim top/bottom 1% of unit and total prices. Final sample: 551,790
    transactions, 17 districts, 45 subdistricts, January 1998 - February 2020.
  pipeline_stages:
  - stage: collect
    inputs:
    - EPRC transaction data
    - Land Registry auction data
    - Census and election data
    method: Commercial purchase plus public retrieval; match land auctions to transactions by land lot number
    output: Transaction dataset with lease-expiration and auction fields
    evidence: Paper section 4.1
  - stage: geocode
    inputs:
    - Building addresses in the sample
    method: Geocode all buildings; compute distances to MTR, bus stops, hospitals, schools, universities, coastline
    output: Distance/amenity controls
    evidence: Paper section 4.1
  - stage: clean
    inputs:
    - Full transaction extract
    method: Apply sample filters (private, arm's-length, non-Islands, 1998-2020, 1% trimming, completeness)
    output: Analysis sample of 551,790 transactions
    evidence: Paper section 4.2
  - stage: classify
    inputs:
    - Lease expiration year and auction dates
    method: Separate leases expiring before vs after 2047-07-01; control = leases expiring 2047-06-30 auto-extended to 2097; treatment = unprotected HKSAR leases and colonial leases
    output: Treatment/control lease groups
    evidence: Paper sections 2.3 and 4.3
  constructed_variables: []
  validation:
  - Balance tests between main treatment and control groups (paper subsection 4.5)
  - Placebo tests using rental transactions
  - Matched-sample robustness pairing estates in main treatment vs control lease groups
  output:
    unit_of_observation: Second-hand private residential transaction
    structure: Transaction-level repeated cross-section
    geography: Hong Kong, 17 districts, 45 subdistricts (Islands District excluded)
    time_span: January 1998 - February 2020 (analysis); EPRC source 1992-2020
    key_variables:
    - Log price, unit price
    - Lease expiration year and group
    - Building age/completion, area, floor, rooms, bay window, amenities
    - Geocoded amenity distances
    - District demographics and pro-democracy seat share
    formats:
    - deposit formats unverified
  reproducibility:
    level: medium
    starting_point: https://doi.org/10.3886/E196501V1
    code_available: true
    code_url: https://doi.org/10.3886/E196501V1
    requirements:
    - openICPSR account and download
    - The deposit's data/code (manifest unverified)
    - EPRC commercial extract if the full raw transaction history is needed
    blockers:
    - openICPSR 403 for automated clients
    - EPRC licensing and cost unverified
    - Lease-classification details require the paper's appendix rules
  compliance:
    terms_or_license: ICPSR deposit terms; EPRC/Land Registry data have their own commercial/public terms
    robots_or_rate_limits: Respect Land Registry website terms; openICPSR blocks automated clients
    personal_or_sensitive_data: Transaction records include buyer/seller names (paper notes this field); handle per license and privacy rules
    redistribution: Do not redistribute the commercial EPRC extract or restricted fields beyond license terms
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'He, Zhiguo; Hu, Maggie; Wang, Zhenping; Yao, Vincent (2024), Valuing Long-Term Property Rights with Anticipated Political Regime Shifts, American Economic Review 114(9): 2701-2747'
  doi: https://doi.org/10.1257/aer.20211242
  journal: American Economic Review
  year: 2024
  dataset_role: Main dataset (551,790 HK residential transactions) for hedonic valuation of lease-horizon political risk
  evidence_type: data-section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257%2Faer.20211242
  data_note: >-
    Paper section 4.1: EPRC Ltd. (all Land Registry electronic transaction data,
    Jan 1992 - Feb 2020), Land Registry website land-auction data matched by lot
    number, 1% quinquennial censuses (2001-2016), and district council election
    results (1999-2019); section 4.2: final sample of 551,790 transactions in 17
    districts/45 subdistricts, Jan 1998 - Feb 2020. AER page links the replication
    package to openICPSR 10.3886/E196501V1 (DataCite: "Replication package
    including data and code", ICPSR, 2024).

provenance:
- source: Working-paper full text (cached nber_hk2047.txt), sections 4.1-4.2 and table notes
  field_scope:
  - data sources (EPRC, Land Registry, census, elections)
  - sample filters and final sample (551,790; 17 districts; 45 subdistricts)
  - variables and lease-group classification
  - geocoding and amenity distances
  added: '2026-08-15'
  confidence: high
  verified: true
- source: AER article page (cached aea_hk2047.html) Additional Materials section
  field_scope:
  - Replication Package link to https://doi.org/10.3886/E196501V1
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite record 10.3886/E196501V1
  field_scope:
  - deposit existence, title, publisher (ICPSR), year (2024), "Replication package including data and code" description
  - does not prove file contents or automated downloadability
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite API record 10.3886/E196501V1, queried 2026-09-28
  field_scope:
  - current v1 DOI title, ICPSR publisher, 2024 publication year and findable state
  - current description as a replication package including data and code
  - current openICPSR landing route and absence of exposed rights/file-manifest metadata
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- china-new-housing-buyer-transactions
- china-jrs-sweating-assets-housing-transactions-2026
---

## Positioning in one sentence

A transaction-level Hong Kong housing asset (551,790 second-hand private transactions, Jan 1998 - Feb 2020) built from the commercial EPRC/Land Registry extract with lease-horizon variation around the 2047 regime shift; the openICPSR replication package (10.3886/E196501V1) is the current route, while the raw EPRC history is a separately licensed commercial product.

## Select rules

- Prioritize it when the question needs Hong Kong transaction-level prices with lease-expiration and political-risk variation, or hedonic valuation of property-rights horizons.
- Switch to mainland transaction candidates (beike etc.) for mainland markets; switch to RVD/Land Registry raw records when the researcher wants to build a custom sample beyond the paper's filters.
- It cannot answer questions about public housing, houses/townhomes, Islands District, or post-February 2020 transactions; rental data enter only as placebo in the paper.

## Get recipe

1. Download the openICPSR replication package (10.3886/E196501V1) via a human browser (automated clients get 403) and read the manifest.
2. If the paper's full raw transaction history is needed, purchase the EPRC extract (or Land Registry electronic data) and rebuild the sample using the paper's filters and lease-classification rules.
3. Match land-auction data from the Land Registry website by land lot number; add district demographics (census 2001-2016) and election-based political sentiment if not in the deposit.
4. Verify the deposit's coverage (1998-2020 analysis sample) before extending any analysis beyond February 2020.

## Connections and Limitations

Transactions join to land auctions by lot number and to districts/subdistricts for demographics; buildings are geocoded for amenity distances. The deposit manifest is the key open item - it may contain derived data rather than the full EPRC extract. EPRC licensing, current cost, and exact vintage are unverified; the paper's lease classification (2047-06-30 control vs post-2047 treatment) must be applied exactly for replication.
