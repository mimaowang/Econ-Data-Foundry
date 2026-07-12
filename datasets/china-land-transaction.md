---
schema_version: 2
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
provider: Public announcement on the China Land Market Network (www.landchina.com) under the Ministry of Natural Resources
  (MNR, formerly the Ministry of Land and Resources MLR)
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
unit_of_observation: Land plot-transaction (land transfer/transfer records one by one)
structure: transaction-records
geo_granularity:
- Land plot (GPS coordinates/address)
- County
- city
- province
geography: All provinces/cities in mainland China (covering all cities at county level and above, the most complete record
  of urban land transactions in China)
time_span: 2000-present (data coverage and quality improved significantly after the implementation of the bidding, auction
  and listing system in 2006; continuously updated)
frequency:
- transaction-level
- Annual (can be summed up to city - year)
sample_size: Accumulated millions of land transaction records; approximately 100,000-300,000 new transfer records are added
  every year
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
- Lot number (unique identifier)
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
- Panel fixed effects (city/county × year)
- DID (policy/land transfer system reform/bidding, auction and listing pilot)
- IV (geography/history/planning exogenous shocks)
- RD (Administrative Boundary/Planning Control)
- spatial metrology
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
  url: https://www.landchina.com (China Land Market Network, official public disclosure platform)
  cost: free (original disclosure information is public data; Batch scraping or structured data must be handled manually)
  license: Government public information, free to use and research
  format:
  - csv
  - dta
  - xlsx
  - json
  api: false
  how_to_get: '1) Direct access https://www.landchina.com → Query single transaction announcement information by province/city/year/land
    use; 2) Batch acquisition (recommended): Download structured csv/dta through university databases (such as CNRDS land
    market module, CSMAR land research module); 3) Self-crawling: Write a crawler to crawl from landchina.com (pay attention
    to frequency control and robots.txt); 4) Some economics research teams have compiled 2000–2020 clean panel data, which
    can be obtained through cooperation.'
caveats: Before 2006, agreement transfer was the main → data coverage and quality were poor. After the reform of the bidding,
  auction and listing system in 2006, the data quality has been greatly improved, but there are still a few omissions (some
  small cities/counties have incomplete publicity). The company name is not standardized (with the same name written differently,
  and the name changed before and after) - it needs to be cleaned when matching with ASIF/industrial and commercial database.
  Land use classification systems may not be entirely consistent with statistics/planning department classifications. There
  is doubt whether the published price is the actual transaction price - there is an incentive to falsely report high/low
  prices (in line with the local government's land transfer strategy).
access_routes:
- route: China Land Market public search
  access_status: available-with-technical-friction
  direct_url: https://www.landchina.com/
  requirements:
  - Can access the current public page of the website
  - Comply with website terms of use, robots rules and reasonable request frequency
  steps:
  - Search transaction announcements by province, city, year and land use
  - Save parcel number, query criteria and page date
  - Organize item by item or write speed-limited collection program within the allowed range
  - Check for missing, duplicate and administrative division changes
  deliverable: Public land parcels/transaction announcement records; batch completeness and availability of historical pages
    need to be verified by yourself
  cost: free
  last_checked: '2026-07-10'
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
  last_audited: '2026-07-10'
used_by:
- cite: 'Cheng, Zhao & Liu (2024), Incentive Adjustments and Land Leasing Behavior Shifts: A Quasi-Natural Experiment of Off-Office
    Audits'
  journal: CER
  year: 2024
  data_note: Using China's land transfer microdata + outgoing audit system to conduct a quasi-experiment, study how the official
    accountability mechanism changes local government land transfer behavior - land transfer shifts from agreement to bidding,
    auction and listing
- cite: 'Lu & Wang (2023), How Revolving-Door Recruitment Makes Firms Stand Out in Land Market: Evidence from China'
  journal: CER
  year: 2023
  data_note: Using land transfer microdata + enterprise database, we study how the "revolving door" of government officials
    (employed by enterprises after leaving their jobs) affects the competitive advantage of enterprises in the land market
    - enterprises with revolving door connections obtain cheaper and larger land parcels.
- cite: 'Tian, Wang & Zhang (2024), Land Allocation and Industrial Agglomeration: Evidence from the 2007 Reform in China'
  journal: JDE
  year: 2024
  data_note: Using China's land transaction microdata (2143 counties) + ASIF + 2004 Economic Census, and taking the 2007 industrial
    land bidding, auction and listing reform as DID - the transparency of land distribution promotes industrial agglomeration
    that matches local specialization, and the stricter the implementation of the reform, the stronger the regional effect.
provenance:
- source: China Land Market Network https://www.landchina.com (official disclosure platform supporting variables and coverage)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: Cheng et al. (2024 CER) and Lu & Wang (2023 CER) papers (confirming the use of Chinese land transfer microdata in
    CER)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- asif
- china-stat-yearbook
- china-io-table
---

## Positioning in one sentence
China's land market data is a transaction-by-transaction record of all state-owned construction land transfers/allocations/transfers published on the "China Land Market Network" (landchina.com) by the Ministry of Natural Resources of China since the 2000s——
It contains complete information such as plot location, area, price, purpose, transfer method and transferee, covering all cities at or above the county level across the country, with a total of millions of records.
Because land transfer is the most important source of revenue for local governments ("land finance"), this data is not only useful for studying China's urban development,
Basic data on land finance and local officials’ behavior can also be connected with corporate data (ASIF/industrial and commercial registration) to study the impact of land costs on corporate behavior.
Available at no charge under the provider agreement - extremely rare high-value, zero-cost Chinese microeconomic data.

## Research questions suitable for answering/Typical identification strategies
- **Political Economy of Land Finance**: How promotion incentives/financial pressure/tenure of local officials affect land transfer strategies (selection of transfer methods: high-price auction vs. low-price agreement, industrial land vs. commercial/residential land supply structure).
  Use city-year panel + official characteristics to do DID/panel fixed effects identification.
- **Land Prices and Urban Spatial Structure**: Use land-by-lot transaction prices to create a hedonic pricing model—how to capitalize land prices by distance from the city center, planning controls, and transportation accessibility. Administrative boundaries/planning lines can be used for spatial RD.
- **Land cost and corporate behavior**: Use the "transferee" field to match ASIF companies → How the land acquisition price affects the company's TFP/investment/site selection/entry and exit.
  Typical identification: Use the cross-city differences in the implementation time of the bidding, auction and listing system to do DID.
- **Land transfer and housing prices**: Time series changes in land transfer area/price → elasticity of housing supply → fluctuations in house prices.
- **Not suitable for**: rural collective construction land (the land market network mainly covers state-owned construction land), land below the county level before 2010 (incomplete coverage), accurate post-land use assessment (the publicized conditions are the agreed conditions at the time of transfer, not the actual construction situation).

## Key variables/modules
- **Plot identification and location**: plot number (unique), province/city/county/district/street, specific address/fourth, longitude and latitude (requires third-party matching)
- **Transaction attributes**: transfer method (bidding/auction/listing/agreement), transaction price (10,000 yuan), starting price, transaction date
- **Land characteristics**: area (hectares), land use (industrial/commercial/residential/comprehensive), transfer period, floor area ratio, building density, green space ratio
- **Transferee**: Company name (key connection point! Can be matched with ASIF/industrial and commercial registration data)
- **Construction Agreement**: Agreed start date, agreed completion date

## How to get
1. **China Land Market Network** (direct query): Visit https://www.landchina.com → Enter "Land Transfer Result Announcement" → Filter by province/city/district/year/land use → View item by item (suitable for small sample inquiries).
2. **Commercial database** (the easiest to obtain in batches): CNRDS/CSMAR has a "land market" module that can directly export structured panel data by city/enterprise/year (institutional subscription).
3. **Crawling by yourself** (free + full coverage): Write a Python crawler to crawl batches (about millions of items) from landchina.com, and need to handle anti-crawling and HTML parsing - multiple research teams have done this and are willing to share the crawler code.
4. **Cooperation access**: Contact existing land economics research teams (Tsinghua University/Peking University/Fudan/Zhejiang University, etc.). Many teams have compiled clean versions that can be used in cooperation.

## Connections to other data
- **With ASIF (industrial enterprise database)**: Match with "transferee enterprise name" - this is the core connection for studying "land cost → enterprise performance". Pay attention to company name cleaning (it is as time-consuming as the ASIF→Customs connection).
- **With the Statistical Yearbook**: Use "administrative division code" to connect macro indicators such as city-level housing prices/GDP/population/fiscal revenue.
- **With housing data**: Use "city/location/time" to connect housing price data (such as CREIS Zhongzhi database, Fangtianxia, etc.) to study the transmission of land supply → housing prices.
- **With input-output table**: Use "Land Use Mapping Industry" to connect industry related relationships.

## Remarks / Pitfalls
- **2006 was a watershed**: Before 2006, transfers were mainly by agreement - the data was confusing and the price information was distorted (the agreement price was often far away from the market price). Time series analysis generally starts in 2006 or 2007.
- **Price Authenticity**: The published "transaction price" may not be the actual price paid. Local governments have incentives to raise prices for industrial land to avoid "low-price transfer" review and lower prices for residential land to cooperate with developers.
- **Company name cleaning is a compulsory course**: We face the same problems when matching with ASIF - different spellings of the same name, parent and subsidiary companies, and name changes. The transferee field does not have a unified social credit code and can only rely on name + address fuzzy matching.
- **Note on land use classification**: There are subdivisions under the four major categories of industrial/commercial/residential/comprehensive - such as "other ordinary commercial housing land" vs. "affordable housing land" with completely different policy meanings. When doing your research, read the definitions of each category carefully.
- **Data integrity of agreement vs. bidding, auction, and listing**: The bidding, auction, and listing data have been basically complete since 2007, and the agreement transfer data may be missing in some years/cities (because the publicity requirements are lower than those of bidding, auction, and listing).
