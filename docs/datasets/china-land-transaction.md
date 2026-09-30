---
schema_version: 3
catalog_status: grounding
id: china-land-transaction
name: China Land Market Data (China Land Transaction Data/China Land Transfer Data)
aka:
- 土地出让数据
- 土地交易数据
- 土地市场网数据
- China Land Transaction
- 土地招拍挂数据
- 中国土地市场网
- Landchina
- 土地微观交易
- 地块级数据
provider: >-
  China Land Market Network (中国土地市场网, landchina.com), whose current
  mobile landing page identifies the host as the Ministry of Natural Resources
  Real Estate Registration Center / Legal Affairs Center. The exact governance
  and data-production chain for every historical announcement remains to be
  verified.
china_related: true
domains:
- public
- urban
- housing
- firm
- development
- macro
- environment
- finance
data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: Structured plot-transaction table reconstructed from public land-transfer announcements
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The current public mobile landing page visibly separates land-supply plans,
    transfer announcements, parcel publicity and land-supply results, and
    displays a nationwide daily count plus individual parcel summaries. A
    research-ready historical table still has to be built from source pages
    with documented query/selection conditions, or obtained through a
    separately verified commercial provider.
  barrier: >-
    The checked landing page does not establish a bulk export, API, complete
    historical archive, detailed-record field list, query/filter behaviour,
    bulk-reuse terms, or that every public category is a completed transaction.
    Browser access to the desktop URL returned blank in this environment.
unit_of_observation: Land plot-transaction (land transfer/transfer records one by one)
structure: transaction-records
geo_granularity:
- Land plot (GPS coordinates/address)
- County
- city
- province
geography: >-
  Current landing-page examples and its national daily summary establish a
  nationwide public-facing service. They do not establish complete coverage of
  every province, county, historical year or transaction category.
time_span: >-
  Current public service is live; exact historical archive coverage is
  unverified. Paper-specific extracts independently establish, for example,
  2007-2017 residential parcels in 326 cities, but those are not proof of a
  continuously downloadable all-category national archive.
frequency:
- transaction-level
- Annual (can be summed up to city - year)
sample_size: >-
  Unknown for the current provider service. The mobile landing page displayed
  one daily nationwide count (63 parcels when viewed 2026-09-28), while
  published papers document their own bounded extracts.
key_variables:
- Lot location (province/city/county/district/street/specific address)
- Land area (hectare/square meter)
- Transfer method (bidding/auction/listing/agreement)
- Transaction price (10,000 yuan)
- Starting price/floor price
- Land use (industrial/commercial/residential/complex/public)
- Floor area ratio
- building density
- Green space rate
- Transfer period
- Transferee (company name/individual)
- contract signing date
- Agreed start/completion date
- Land use right type (transfer/allocation/lease)
- Lot number (uniqueness must be checked within the retained source and sample)
- Administrative division code
good_for:
- Land finance and local government behavior - determinants of cross-city/cross-time differences in land transfer income/price
  (interaction between land price and house price, official promotion incentives, financial pressure → land transfer strategy)
- Land market and corporate behavior - how land costs affect corporate location selection, entry and exit, and productivity
  (the name of the transferee company can be matched with ASIF/industrial and commercial registration data)
- Urban spatial structure - spatial distribution of industrial vs commercial vs residential land, land price gradient and
  urban sprawl
- Distorted land resource allocation - the difference in land costs between agreements vs. bidding, auctions and listings,
  the distorted pattern of low industrial land prices/high residential land prices
- Land and housing market - land transfer price → house price transmission, the impact of land supply control on house prices
- Environmental consequences - the spillover effects of polluting enterprise location selection, industrial land transfer,
  and land marketization on environmental quality
identification:
- This record describes a land-data source and researcher-built transaction tables; it does not define policy treatment, comparison groups, or causal identification.
linkable_keys:
- Company name (transferee)
- Administrative division code (province/city/county)
- Land latitude and longitude/GPS coordinates
- Lot number
- Land use classification (mapped industries)
research_fit:
  best_for:
  - Plot-level land transfer prices, uses, methods and local government land supply behavior
  - Research on land cost and enterprise location selection, industrial agglomeration, urban space and housing market
  choose_over:
  - Select land market data when lot/transaction level and transfer method are required instead of just using land revenue
    from city yearbooks
  - Join land transactions with ASIF, industrial and commercial or patent data when enterprise production, exit or innovation
    results are needed
  not_good_for:
  - Rural collective land and undisclosed transactions
  - Actual construction starts, completions and home sales results
  - Family education, income, or health outcomes without additional matching
  needs_join_for:
  - Enterprise productivity, innovation and entry and exit need to be matched with ASIF/business/patent data
  - Housing prices, finance, pollution and policy results need to be joined according to the region and year where the plot
    is located.
  variation_available:
  - Transaction records from 2000 to the present, the quality is more stable after the bidding, auction and listing system
    was introduced in 2006
  - Parcel, County/City and Year Differences
  - Land use, transfer method, price, planning constraints and transferee differences
access:
  url: https://m.landchina.com/
  cost: Public landing page is free; any detail-page, bulk, subscription or reuse cost remains unverified
  license: Publicly viewable government information; bulk collection, reuse, and redistribution terms require current verification
  format:
  - public HTML/mobile web pages
  api: false
  how_to_get: >-
    Start at the official mobile landing page and identify the correct public
    category (announcement, publicity, result or plan). Before research-scale
    collection, verify the detail-page route, terms, historical reach and
    fields for the exact category; do not infer a bulk download from the
    public-facing dashboard.
production:
  raw_sources:
  - name: China Land Market public land-transfer announcements
    source_type: webpage
    role: Official source records for plot identity, location, use, transfer method, price, transferee, and dates
    access_route: >-
      Current mobile landing page links to separate public categories for land
      supply plans, transfer announcements, parcel publicity and supply results;
      detailed query/filter behaviour is unverified.
    url: https://www.landchina.com/
    coverage: Individual announcement availability; historical batch completeness varies and must be audited
    last_checked: '2026-09-28'
  acquisition_methods:
  - public web query
  - manually documented public-page extraction after terms and detail route are verified
  sample_construction: >-
    Choose one public category and define observed geography, date, status and
    land-use rules only after confirming the corresponding detail-page fields;
    preserve the route, criteria and retrieval date for every collection batch.
  pipeline_stages:
  - stage: collect
    inputs:
    - Public search results and announcement pages
    method: >-
      Start from the public category route and save the source page together
      with the category, criteria and collection date. The current landing
      page alone does not prove a province/year/land-use query form.
    tools:
    - browser or policy-compliant collection program
    output: Raw announcement records with collection provenance
    evidence: Current official mobile landing page; detailed collection flow remains unverified
  - stage: parse
    inputs:
    - Raw announcement records
    method: Extract plot number, administrative location, land attributes, transaction terms, transferee, and dates while retaining the original record reference.
    tools:
    - HTML parser or manual extraction
    output: Structured plot-level rows
    evidence: Published announcement fields and the entry's recorded key variables
  - stage: clean
    inputs:
    - Structured plot-level rows
    method: Check duplicates, missing pages, unit consistency, administrative-boundary changes, land-use labels, and non-standard transferee names.
    tools:
    - tabular data-processing software
    output: Versioned plot-transaction research table
    evidence: Existing access recipe and caveats in this record
  - stage: validate
    inputs:
    - Versioned plot-transaction research table
    method: Report missingness and duplicates by geography and year and audit coverage breaks, especially before and after the 2006-2007 institutional change.
    tools:
    - tabular data-processing software
    output: Coverage and quality diagnostics accompanying the research table
    evidence: Existing coverage caveats and public-route deliverable limitations in this record
  constructed_variables: []
  validation:
  - Missing and duplicate records by geography and year
  - Administrative-boundary and category consistency
  - Coverage and category discontinuity across the actually obtainable pages
  output:
    unit_of_observation: Land plot transaction or transfer announcement
    structure: transaction records, aggregable to geography-year panels
    geography: Mainland China where announcements are available
    time_span: Defined by the collection's actual, documented query route; no all-category 2000-present archive is established here
    key_variables:
    - plot identifier and location
    - area, use, transfer method, and transaction price
    - transferee and contract dates
    formats:
    - researcher-created tabular file
  reproducibility:
    level: low
    starting_point: China Land Market public search and announcement pages
    code_available: false
    requirements:
    - Ability to collect and parse public web records under current provider rules
    - Data cleaning for names, units, categories, and administrative divisions
    - Storage and quality auditing for a large historical collection
    blockers:
    - No verified public bulk API or complete historical dump
    - Historical pages and site behavior may change
    - Exact paper-specific filters and cleaning code are not established by this record
  compliance:
    terms_or_license: Check current provider terms before automated collection; public visibility does not by itself grant unrestricted bulk reuse.
    robots_or_rate_limits: Respect robots rules, rate limits, and technical access controls.
    personal_or_sensitive_data: Review transferee names and any personal records before processing or redistribution.
    redistribution: Do not assume that a researcher-created bulk copy may be redistributed.
    review_needed: Recheck current terms, historical-page access, and permitted collection method before each new build.
caveats: >-
  A public category can mean a plan, announcement, publicity or completed
  supply result; choose and document the status layer before analysis. Paper
  extracts verify particular historical samples, not the completeness of the
  current portal. Any transferee-name match, parcel geocode, land-use mapping,
  price interpretation, historical continuity and coverage assessment must be
  based on fields actually delivered by the selected detail route.
access_routes:
- route: China Land Market public mobile landing page
  access_status: available-with-technical-friction
  direct_url: https://m.landchina.com/
  requirements:
  - Browser access to the current mobile service
  - Verify detail-page terms and permitted collection before any research-scale extraction
  steps:
  - Choose the public category matching the research object: 供地计划, 出让公告, 地块公示 or 供地结果.
  - Confirm that the detail page exposes the intended fields and historical query range before treating an item as a transaction observation.
  - Preserve page URL, status category, observed place, date and fields for every retained item.
  - Stop and retain a bounded sample if terms, detailed fields or historical reach cannot be verified.
  deliverable: >-
    Public dashboard/category observations and, only after separate detail
    verification, researcher-documented announcement or result records; no
    bulk panel is established.
  cost: free
  last_checked: '2026-09-28'
- route: Commercial structured land modules
  access_status: needs-verification
  direct_url: https://data.csmar.com/
  requirements:
  - Subscriptions from universities or research institutions
  - Confirm that current subscription includes the Land Market module and target year
  steps:
  - Check with the library or database administrator for the CNRDS/CSMAR land module
  - Check the coverage year, fields, cleaning measurement definition and download restrictions
  - Export and save versions, filters, and licensing information as needed for your project
  deliverable: Structured land transaction documents compiled by the vendor; not a lossless substitute for the official original
    publication
  cost: paid
  last_checked: '2026-07-10'
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'
used_by:
- cite: 'Cheng, Zhao & Liu (2024), Incentive Adjustments and Land Leasing Behavior Shifts: A Quasi-Natural Experiment of Off-Office
    Audits'
  journal: CER
  year: 2024
  dataset_role: China's land transfer microdata as the land-leasing-behavior outcome in the outgoing-audit quasi-experiment
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v87y2024ics1043951x24001184.html
  data_note: Using China's land transfer microdata + outgoing audit system to conduct a quasi-experiment, study how the official
    accountability mechanism changes local government land transfer behavior - land transfer shifts from agreement to bidding,
    auction and listing
- cite: 'Lu & Wang (2023), How Revolving-Door Recruitment Makes Firms Stand Out in Land Market: Evidence from China'
  journal: CER
  year: 2023
  dataset_role: Land transfer microdata as the land-market outcome (parcel price and size) in the revolving-door analysis
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v78y2023ics1043951x23000275.html
  data_note: Using land transfer microdata + enterprise database, we study how the "revolving door" of government officials
    (employed by enterprises after leaving their jobs) affects the competitive advantage of enterprises in the land market
    - enterprises with revolving door connections obtain cheaper and larger land parcels.
- cite: 'Tian, Wang & Zhang (2024), Land Allocation and Industrial Agglomeration: Evidence from the 2007 Reform in China'
  journal: JDE
  year: 2024
  dataset_role: China's land transaction microdata (2143 counties) as the land-allocation outcome in the 2007 industrial land reform DID
  evidence_type: working_paper_data_section
  evidence_url: http://www.cfrn.com.cn/uploads/master/file/20240328/66058c34f30d9.pdf
  data_note: Using China's land transaction microdata (2143 counties) + ASIF + 2004 Economic Census, and taking the 2007 industrial
    land bidding, auction and listing reform as DID - the transparency of land distribution promotes industrial agglomeration
    that matches local specialization, and the stricter the implementation of the reform, the stronger the regional effect.
- cite: 'Wang, Wu & Wu (2025), Export Slowdown and Increasing Land Supply: Local Government''s Responses to Export Shocks in China'
  doi: https://doi.org/10.1016/j.jue.2025.103796
  journal: JUE
  year: 2025
  dataset_role: Residential primary-land transaction microdata collapsed to city-year area, price and revenue measures
  evidence_type: data_section_and_working_paper
  evidence_url: https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf
  data_note: The paper identifies the Ministry of Natural Resources landchina.com as the official source and collects 279,534 residential land parcels in 326 cities from 2007-2017 supplied through tender, English auction, and two-stage auction (revenue-oriented methods). It collapses parcel area, price, and revenue to city-year measures and keeps non-revenue residential and industrial supply as comparison data. This confirms a paper-used subset and construction route, not a guarantee of a complete historical download or redistribution right.
- cite: 'Xu & Jiang (2026), Extrapolative Households and Strategic Firms: Evidence from China''s Land and Housing Market'
  doi: https://doi.org/10.1016/j.jue.2026.103864
  journal: JUE
  year: 2026
  dataset_role: Land transaction microdata as core land supply measurement; combined with housing price and firm behavior data
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0094119026000169
  data_note: Uses China's land transaction microdata (land supply, land prices, and land allocation across cities) to study how local governments strategically manage land supply in response to extrapolative housing price expectations, and how developers' land-banking behavior amplifies housing market cycles. Documents that land supply responds to expected future housing prices, with firms strategically adjusting land inventory.
- cite: 'Mei & Xi (2026), Impact of Place-Based Policy on Land Lease Price and Its Productivity Premium: Evidence From China''s Development Zone Program'
  doi: https://doi.org/10.1111/jors.70064
  journal: JRS
  year: 2026
  dataset_role: Block-level "development zone — land parcel — firm" micro-spatial dataset
  evidence_type: publisher_and_working_paper_description
  evidence_url: https://onlinelibrary.wiley.com/doi/abs/10.1111/jors.70064
  data_note: The publisher record identifies the study as using development-zone, land-parcel, and firm microdata. The authors' working-paper description says that a "DZ-Land-Firm" spatial dataset is constructed with spatial positioning and overlay analysis. The raw land, zone-boundary, and firm providers, boundary vintage, matching files, access conditions, and redistribution rights are not established here, so this paper-specific constructed asset remains separate from the general land-transaction record and is not treated as a public download.
- cite: 'Dong & Huang (2025), The Impact of Polluters'' Cleanup on Land Values: Evidence From Pollution-Intensive Industries in China'
  doi: https://doi.org/10.1111/jors.12753
  journal: JRS
  year: 2025
  dataset_role: Geocoded land transaction parcels matched with pollution-intensive firm locations
  evidence_type: data-section
  evidence_url: https://onlinelibrary.wiley.com/doi/abs/10.1111/jors.12753
  data_note: Uses geocoded land transaction data combined with location/closure information on polluting firms. Finds that cleanup of at least one heavy-polluting firm within 2km raises surrounding land parcel prices by 15.2%. Effect is stronger for commercial-use parcels, farther from CBD, and in smaller noncapital cities — driven by entry of new clean/high-tech firms and population growth post-cleanup.
- cite: 'Brueckner, Liu, Xiao & Zhang (2025), Government-Directed Urban Growth, Firm Entry, and Industrial Land Prices in Chinese Cities'
  doi: https://doi.org/10.1093/jeg/lbaf059
  journal: JEG
  year: 2025
  dataset_role: Nationwide land-lease transaction data; county-to-city annexation identification
  evidence_type: data-section
  evidence_url: https://academic.oup.com/joeg/advance-article-abstract/doi/10.1093/jeg/lbaf059/8382698
  data_note: Uses nationwide land-lease transaction data to study county-to-city annexations as government-directed urban spatial expansion. Finds annexation raises industrial land prices in annexed counties by ~7%, with increased firm entry and investment as the driving mechanism. Annexation coordinates firm expectations about future urban growth direction — no price displacement in neighboring counties or central cities.
- cite: 'Brueckner, Liu, Xiao & Zhang (2025), Building Tall, Falling Short: An Empirical Assessment of Chinese Skyscrapers'
  doi: https://doi.org/10.1016/j.jue.2024.103731
  journal: JUE
  year: 2025
  dataset_role: Land transaction parcel-level data 2006-2014; used to estimate government land subsidies for skyscraper parcels
  evidence_type: data-section
  evidence_url: https://voxchina.org/show-3-409.html
  data_note: Uses land transaction records (2006-2014) combined with a geocoded dataset of 1,575 skyscrapers (≥100m) in China. Compares skyscraper land parcel prices with neighboring parcels to estimate government land price discounts — finds average 40.1% subsidy. Also uses firm registration data to track new business formation near skyscrapers for spillover analysis. Government-subsidized skyscrapers generate limited economic spillovers — most are commercially non-viable and financed via municipal debt.
- cite: 'Zhao, Ploegmakers, Rouwendal & Ma (2024), Land Investment Regulation and Allocative Efficiency: Evidence from the Chinese Manufacturing Sector'
  doi: https://doi.org/10.1093/jeg/lbae024
  journal: JEG
  year: 2024
  dataset_role: Land lease transaction records matched with ASIF (20,205 new firms 2007-2014)
  evidence_type: data-section
  evidence_url: https://academic.oup.com/joeg/article/25/2/151/7725676
  data_note: Matches land lease records with ASIF firm data to estimate firm-level land production functions. Uses Minimum Investment Intensity (MII) regulation and county-border spatial discontinuity design to identify how land use regulation causes allocative inefficiency. Average land productivity gap of ~310 yuan/m² — regulation prevents optimal land allocation by requiring minimum fixed capital investment per hectare.
- cite: 'Shen, Wu, Wu & Zheng (2026), Disrupted Development: Urban Productivity Under Changing Place-Based Industrial Policies in China'
  doi: https://doi.org/10.1111/jors.70050
  journal: JRS
  year: 2026
  dataset_role: 319,276 industrial land parcels across 285 cities (2008-2016); measure changing spatial targeting of place-based policies
  evidence_type: publisher_and_bibliographic
  evidence_url: https://ideas.repec.org/a/bla/jregsc/v66y2026i3p868-890.html
  data_note: The publisher-indexed bibliographic record confirms a dataset of 319,276 industrial land parcels in 285 Chinese cities during 2008-2016. The checked public material does not establish the raw provider, parcel fields, zone-boundary source, construction code, or access/redistribution route; those details must not be inferred from the general landchina record. Keep this paper-specific lead separate until those facts are verified.
- cite: 'Rong, Wang & Zhang (2026), Does Real Estate Expansion Hurt Manufacturing Employment: Evidence from China'
  doi: https://doi.org/10.1016/j.labeco.2026.102889
  journal: Labour Economics
  year: 2026
  dataset_role: Province-level residential land transfer areas (one-year lagged) as instrumental variable for city-level real estate investment
  evidence_type: replication
  evidence_url: https://data.mendeley.com/datasets/btk3vktc2s/2
  data_note: >-
    Uses province-level urban residential land transfer area data (one-year lagged) as the instrumental variable for city-level real estate investment, following Hau & Ouyang (2024) and Waxman et al. (2020). Combined with ASIF firm panel and city statistics across 70 major Chinese cities (2000-2009). IV estimates find real estate expansion crowds out manufacturing employment through rising wage costs — 10% increase in real estate investment → 1.46% decline in manufacturing firm employment.
provenance:
- source: https://m.landchina.com/ (official mobile landing page, browser-read 2026-09-28)
  field_scope:
  - current service identity and host text
  - separate public categories: 供地计划, 出让公告, 地块公示, 供地结果, 其他公告 and 土地推介
  - nationwide previous-day dashboard counts and visible parcel-summary fields including place, status, land use, floor-area-ratio text and area
  - boundary that a dashboard does not prove detailed historical query, complete coverage, export or bulk reuse
  added: '2026-09-28'
  confidence: high
  verified: true
- source: China Land Market Network https://www.landchina.com (official disclosure platform supporting variables and coverage)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: Cheng et al. (2024 CER) and Lu & Wang (2023 CER) papers (confirming the use of Chinese land transfer microdata in
    CER)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: Wang, Wu & Wu (2025) working-paper data section https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf and JUE DOI https://doi.org/10.1016/j.jue.2025.103796
  field_scope:
  - MNR/landchina source identity
  - 279,534-parcel and 326-city scope
  - 2007-2017 period
  - revenue-oriented method filters
  - city-year aggregation
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Shen, Wu, Wu & Zheng (2026) bibliographic record https://ideas.repec.org/a/bla/jregsc/v66y2026i3p868-890.html
  field_scope:
  - authorship and DOI
  - 319,276-parcel count
  - 285-city scope
  - 2008-2016 period
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Mei & Xi (2026) publisher record https://onlinelibrary.wiley.com/doi/10.1111/jors.70064 and working-paper description https://doi.org/10.2139/ssrn.4029422
  field_scope:
  - authorship and DOI
  - development-zone, land-parcel and firm roles
  - DZ-Land-Firm construction description
  - spatial positioning and overlay analysis
  added: '2026-08-12'
  confidence: high
  verified: true
related_datasets:
- asif
- china-stat-yearbook
- china-io-table
---

## Positioning in one sentence
China Land Market is a public portal family for distinct land-supply status layers. Its mobile landing page makes current nationwide summaries and parcel snippets visible, while a researcher-grade historical transaction table remains a separate, evidence-dependent construction project rather than an already downloadable national panel.
The verified public landing page is free to view. Historical microdata acquisition, research-scale reuse terms and the cost of producing a usable table remain separate questions; this record stays `grounding`.

## Research questions suitable for answering/Typical identification strategies
- **Political Economy of Land Finance**: How promotion incentives/financial pressure/tenure of local officials affect land transfer strategies (selection of transfer methods: high-price auction vs. low-price agreement, industrial land vs. commercial/residential land supply structure).
  Use city-year panel + official characteristics to do DID/panel fixed effects identification.
- **Land Prices and Urban Spatial Structure**: Use land-by-lot transaction prices to create a hedonic pricing model—how to capitalize land prices by distance from the city center, planning controls, and transportation accessibility. Administrative boundaries/planning lines can be used for spatial RD.
- **Land cost and corporate behavior**: Use the "transferee" field to match ASIF companies → How the land acquisition price affects the company's TFP/investment/site selection/entry and exit.
  Typical identification: Use the cross-city differences in the implementation time of the bidding, auction and listing system to do DID.
- **Land transfer and housing prices**: Time series changes in land transfer area/price → elasticity of housing supply → fluctuations in house prices.
- **Not established by the current evidence**: complete rural collective-land coverage or complete local historical coverage, including periods before 2010. Announced construction conditions also do not establish what was ultimately built on a parcel.

## Key variables/modules

The fields below describe research uses and legacy field expectations, not a verified current download schema. The checked landing page exposes only parcel summaries; verify each needed field in the selected announcement/result category and historical sample before designing a collection or join.
- **Plot identification and location**: plot number (test uniqueness within the source and sample), province/city/county/district/street, address/boundary description, longitude and latitude (may require separately documented geocoding)
- **Transaction attributes**: transfer method (bidding/auction/listing/agreement), transaction price (10,000 yuan), starting price, transaction date
- **Land characteristics**: area (hectares), land use (industrial/commercial/residential/comprehensive), transfer period, floor area ratio, building density, green space ratio
- **Transferee**: Company name (key connection point! Can be matched with ASIF/industrial and commercial registration data)
- **Construction Agreement**: Agreed start date, agreed completion date

## How to get
1. **Official starting point:** Visit https://m.landchina.com/ and choose the status layer that actually matches the intended observation: 供地计划, 出让公告, 地块公示 or 供地结果.
2. **Verify before collecting:** inspect the relevant detail-page fields, historical reach and terms. The public dashboard does not itself prove a province/year filter, a parcel-level historical archive, a machine-readable file or permission for bulk extraction.
3. **Build only a bounded documented sample** when the route supports it: keep the page URL, status category, retrieval date, observed fields and a missingness audit. If that verification fails, stop rather than fill the gap from a different layer.
4. **Commercial or cooperative copies:** may be useful only after the exact product, coverage, definition, licence and export restrictions are independently checked. They are not automatically equivalent to the public portal or to a paper's cleaned extract.

## Connections to other data
- **With ASIF (industrial enterprise database)**: Match with "transferee enterprise name" - this is the core connection for studying "land cost → enterprise performance". Pay attention to company name cleaning (it is as time-consuming as the ASIF→Customs connection).
- **With the Statistical Yearbook**: Use "administrative division code" to connect macro indicators such as city-level housing prices/GDP/population/fiscal revenue.
- **With housing data**: Use "city/location/time" to connect housing price data (such as CREIS Zhongzhi database, Fangtianxia, etc.) to study the transmission of land supply → housing prices.
- **With input-output table**: Use "Land Use Mapping Industry" to connect industry related relationships.

## Remarks / Pitfalls
- **Historical comparisons**: Legacy notes identified 2006/2007 as a possible break in transfer methods and disclosure. This record does not establish a universal break date or a complete archive from that date. Use the chosen paper's sample definition and source documentation to justify a time window.
- **Price interpretation**: Keep starting prices, announced transaction prices and evidence of actual payment distinct. Earlier notes proposed strategic misreporting as a concern, but the evidence preserved here does not verify its direction or prevalence; do not encode those conjectures as established data properties.
- **Company name cleaning is a compulsory course**: We face the same problems when matching with ASIF - different spellings of the same name, parent and subsidiary companies, and name changes. The transferee field does not have a unified social credit code and can only rely on name + address fuzzy matching.
- **Note on land use classification**: There are subdivisions under the four major categories of industrial/commercial/residential/comprehensive - such as "other ordinary commercial housing land" vs. "affordable housing land" with completely different policy meanings. When doing your research, read the definitions of each category carefully.
- **Coverage by transfer method**: Published samples demonstrate their own year/city/method selections, not complete national coverage since 2007. Audit missingness separately by year, locality and method; the current evidence does not establish that agreement transfers or auction/listing records are complete.
