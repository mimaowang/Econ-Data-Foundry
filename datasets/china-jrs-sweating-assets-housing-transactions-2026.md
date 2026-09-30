---
schema_version: 3
catalog_status: grounding
id: china-jrs-sweating-assets-housing-transactions-2026
name: Pang, Feng & Zhao (2026 JRS) second-hand housing transaction data
aka:
- Sweating Assets housing transaction records
- China second-hand housing transactions (26-city paper sample)
- 中国二手住房交易数据（极端高温与住房市场）
provider: Jindong Pang, Jie Feng, and Yuan Zhao; paper-specific data held by the authors and made available on request
china_related: true
domains:
- urban
- regional
- housing
- real-estate
- climate
- environment

data_pathway:
  mode: inaccessible
  origin: researcher-collected
  target_artifact: >-
    The authors' paper-specific transaction-level data and replication code for
    "Sweating Assets: The Effect of Extreme Heat on the Housing Market". The public
    article page exposes an online appendix, while the data and code are stated to be
    available from the authors upon request.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    The publisher confirms a distinct micro-level housing asset: more than 1.5 million
    second-hand housing transaction records from 26 Chinese cities, used for prices,
    transaction volumes, property visits, and heterogeneity by housing and neighborhood
    characteristics. A researcher can start with the public article and appendix, but
    the actual files require an author request and are not a predictable public download.
  barrier: >-
    The checked public page does not identify the transaction platform or provider, exact
    city list, transaction years, file format, variable dictionary, cleaning/deduplication
    code, price, or redistribution terms. An author response and the delivered version
    are therefore necessary before this can be recommended as a reproducible asset.

unit_of_observation: Second-hand housing transaction or property record; exact row grain and repeated-sales structure require the author file
structure: Transaction-level records with city/time and property attributes; exact panel structure is not publicly documented
geo_granularity:
- property or housing unit
- building/neighborhood where retained
- city
geography: 26 Chinese cities; the checked publisher page does not list the cities or establish a national sample
time_span:
  start: unknown
  end: unknown
  last_confirmed_release: '2026-04-24'
  coverage_note: >-
    The article was first published on 24 April 2026. The public abstract confirms the
    26-city transaction sample but does not disclose the transaction years; a university
    presentation mentioning 2010-2020 and 70 cities is contextual and is not treated as
    the paper's exact file coverage.
  last_checked: '2026-08-13'
frequency:
- transaction-level
- date/season fields if retained
sample_size: More than 1.5 million second-hand housing transaction records across 26 Chinese cities, according to the publisher abstract
key_variables:
- Transaction price and transaction occurrence/volume
- Property-visit or on-site viewing measure
- Housing type and building characteristics, including high-end, top-floor, and high-rise categories where retained
- City, property, building, or neighborhood identifiers where retained
- Transaction date or season where retained
- Temperature/extreme-heat exposure fields or linked inputs, exact provider and construction not yet identified

research_fit:
  best_for:
  - Micro-level urban housing-market research requiring second-hand transaction prices and transaction activity
  - Studying property visits and heterogeneity by building, unit, and neighborhood characteristics when the authors grant the relevant fields
  - Reproducing or extending the 2026 JRS paper's China housing and heat analysis
  choose_over:
  - Choose this asset over city statistical yearbooks when transaction-level prices, volumes, or property characteristics are essential.
  - Choose the general China Statistical Yearbook record for public city-year housing indicators or a broad, reproducible regional panel.
  - Choose a separate weather product such as ERA5-Land for a transparent replacement exposure only when the paper's original weather fields cannot be obtained; such a replacement is not the paper's replication file.
  not_good_for:
  - A public nationwide housing transaction panel, a guaranteed long-run series, or a representative sample of all Chinese homes
  - Reconstructing the exact study without the author-held file, city list, transaction dates, and cleaning rules
  - Treating the paper's extreme-heat analysis as a standalone policy/variation record
  needs_join_for:
  - Weather or temperature exposure if it is not included in the delivered package
  - City-year controls and boundary concordance for regional comparisons
  - A public housing or land product when access is denied or the research needs a different market segment
  variation_available:
  - Transaction dates, seasons, and temperature exposure may define the paper's analytical comparisons; they are data dimensions only and are not recorded here as a treatment or variation database.
  topics:
  - housing market
  - second-hand housing
  - house prices
  - urban climate
  - extreme heat
  - property visits

good_for:
- Hedonic analysis of second-hand housing prices with detailed property characteristics, conditional on author access
- City-level aggregation of transaction volume or visits when the delivered file retains a stable city and date key
- Comparing urban housing-market responses across the 26-city paper sample
identification: []
linkable_keys:
- City name or code
- Property/building/neighborhood identifier where retained
- Transaction date or month
- Geographic coordinates or address, if supplied under the author terms
- Housing type and building attributes

joins:
- target: era5-land
  relation: complement
  keys:
  - Property coordinates or a documented city/grid location
  - Transaction date or month
  method: Match the delivered property or city location to ERA5-Land after defining the spatial aggregation and heat window; do not assume that a city label gives building-level exposure.
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - City code or normalized city name
  - Year
  method: Use city-year housing, income, population, or macro controls only after checking the paper file's city list and administrative-boundary vintage.
  evidence_status: plausible
- target: china-land-transaction
  relation: often-confused-with
  keys:
  - City and year only as a broad contextual comparison
  method: Keep second-hand home sales separate from government land-transfer announcements; they are different markets, units, and production routes.
  evidence_status: verified

access_routes:
- route: author-requested paper data and replication code
  access_status: available-with-conditions
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
  requirements:
  - Written request to the corresponding authors listed on the article page
  - A clear research purpose and agreement to any author or provider terms
  - Confirmation of whether the delivered package includes raw transactions, cleaned analysis files, code, and a data dictionary
  steps:
  - Read the article page and download the public online appendix.
  - Contact Jindong Pang or Yuan Zhao using the addresses on the article page, citing DOI 10.1111/jors.70066.
  - Ask for the exact 26-city list, transaction years, source platform, field dictionary, cleaning/deduplication scripts, weather inputs, and redistribution conditions.
  - Record the response, delivered version, file formats, and any permitted joins before using the data.
  deliverable: Author-provided transaction data and replication code if approved; the public statement does not guarantee that raw platform records or all source inputs will be released.
  cost: by-application
  last_checked: '2026-09-28'
  caveat: A current direct publisher-page request returned HTTP 403 to this environment on 2026-09-28, so it did not expose a new repository, manifest, or changed data-and-code statement. Data availability on request is not proof that a request will be accepted or that the delivered files reproduce the paper's original raw transactions.
- route: Wiley supporting information
  access_status: available
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
  requirements: A web browser and acceptance of the publisher's current terms for the article materials
  steps:
  - Open the article page and download jors70066-sup-0001-Online_Appendix.pdf.
  - Use the appendix to identify definitions and missing acquisition questions, but do not treat it as the transaction data.
  deliverable: Public online appendix PDF; it is documentation, not a confirmed data or code release.
  cost: free
  last_checked: '2026-08-13'
  caveat: The publisher notes that supporting information is supplied by the authors and may not provide a permanent repository or raw data route.

access:
  url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
  cost: by-application
  license: Article and appendix are subject to Wiley terms; the transaction file and any code supplied by authors may have separate conditions and no redistribution right is inferred.
  format:
  - unknown transaction format
  - pdf appendix
  api: false
  how_to_get: Start with the public article/appendix, then submit a documented request to the corresponding authors and preserve the response and delivered version.

caveats:
- The 26-city and more-than-1.5-million figures come from the publisher abstract; they do not establish the exact city list, years, or representativeness.
- The source platform, weather provider, identifiers, coordinates, price definition, and cleaning rules remain open verification items.
- A current commercial housing-data product must not be called equivalent without paper-specific source and field evidence.
- Property addresses or fine locations, if included, may require additional privacy and redistribution review.
- If authors provide only cleaned or aggregated files, that is still a paper-specific derivative and not evidence that the original platform data can be reproduced.

production:
  raw_sources:
  - name: Paper-specific second-hand housing transaction records
    source_type: dataset
    role: Main transaction prices, transaction activity, property visits, and housing characteristics used in the JRS study
    access_route: Author request described in the article's data availability statement
    url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
    coverage: More than 1.5 million transactions in 26 Chinese cities; exact years, provider, and field coverage require the delivered file
    last_checked: '2026-08-13'
  acquisition_methods:
  - author-request delivery
  sample_construction: >-
    The public publisher page confirms the transaction sample and its research role but
    does not disclose the platform, sampling frame, city selection, duplicate handling,
    exclusions, or weather merge. These construction facts must be taken from the author
    package or recorded as unresolved rather than inferred.
  pipeline_stages:
  - stage: collect
    inputs:
    - Second-hand housing transaction records
    method: The authors collected or assembled the paper's transaction records; the checked public sources do not disclose the platform or extraction protocol.
    output: Author-held paper-specific transaction data, if released in response to a request
    evidence: Wiley article abstract and data availability statement
  - stage: validate
    inputs:
    - Delivered transaction data
    - Delivered replication code and online appendix
    method: Check city counts, transaction counts, field labels, sample restrictions, and one published table/figure before reuse.
    output: A versioned paper-compatible file and an access/replication note
    evidence: Requested author documentation plus the published article/appendix; no public validation run has been performed
  output:
    unit_of_observation: Transaction or property record, depending on the delivered file
    structure: Transaction-level records with city/time and property attributes
    geography: 26 Chinese cities as reported by the publisher; exact city list remains to be obtained
    time_span: Unknown until author documentation or file metadata is received
    key_variables:
    - Transaction price and activity
    - Property visits
    - Building and neighborhood characteristics
    - City/date and temperature exposure fields if delivered
    formats:
    - author-supplied format to be verified
  reproducibility:
    level: needs-verification
    starting_point: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
    code_available: true
    code_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
    requirements:
    - Author approval and any data-use agreement
    - The delivered data, code, dictionary, and appendix
    - Software and storage matching the author package
    - Separate weather or city-control data if omitted from the delivery
    blockers:
    - No public repository or downloadable transaction file was identified.
    - The source platform, years, city list, cleaning, field dictionary, and redistribution terms are unresolved.
    - A request may return only derived files or may not be approved.
  compliance:
    terms_or_license: Article/appendix terms are public; transaction and code terms must be read from the author response or supplied agreement.
    robots_or_rate_limits: Do not scrape commercial housing platforms or Wiley to recreate the paper without a lawful, documented route.
    personal_or_sensitive_data: Check for addresses, coordinates, or other fine-location fields and follow the supplied access conditions.
    redistribution: Do not redistribute author-provided files or derived joins unless the written terms permit it.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-13'

used_by:
- cite: 'Pang, Feng & Zhao (2026), Sweating Assets: The Effect of Extreme Heat on the Housing Market'
  doi: https://doi.org/10.1111/jors.70066
  journal: Journal of Regional Science
  year: 2026
  dataset_role: Main second-hand housing transaction records for price, transaction-volume, property-visit, and housing-heterogeneity analyses
  evidence_type: data-availability-and-abstract
  evidence_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
  data_note: >-
    The publisher abstract states that the paper analyzes more than 1.5 million
    second-hand housing transactions in 26 Chinese cities and reports price, volume,
    property-visit, and building/neighborhood heterogeneity results. The data
    availability statement says data and replication code are available from the authors
    upon request; the public supporting file is an online appendix, not the raw data.

provenance:
- source: https://onlinelibrary.wiley.com/doi/10.1111/jors.70066
  field_scope:
  - paper identity, authors, DOI, and first-publication date
  - 26-city geography and more-than-1.5-million transaction scale
  - reported price, volume, property-visit, and housing-feature roles
  - data availability statement and public online appendix
  added: '2026-08-13'
  confidence: high
  verified: true
- source: Current direct request to the Wiley DOI page (2026-09-28)
  field_scope:
  - current automated-route availability
  - absence of a newly verifiable public repository or manifest in this environment
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: era5-land
  relation: complement
- id: china-stat-yearbook
  relation: complement
- id: china-land-transaction
  relation: often-confused-with
---

## Positioning in one sentence

This is a very recent (2026) paper-specific urban housing transaction asset: more than 1.5 million second-hand sales across 26 Chinese cities, with an author-request route rather than a public download. Its recency makes it a light priority when a research idea matches the topic, but it does not raise the evidence or access standard.

## Select rules

- Prioritize it when transaction-level second-hand prices, transaction activity, property visits, or building heterogeneity are central and an author request is feasible.
- Switch to China Statistical Yearbooks for public city-year indicators, or to a separately verified housing product when a reproducible national or long panel is required.
- Keep it separate from government land-transfer announcements: second-hand home sales and land supply have different units, markets, and production paths.

## Get recipe

Read the Wiley article and online appendix first, then email the corresponding authors with the DOI and a precise request for the data, code, dictionary, city list, years, source platform, and terms. Preserve the response and delivered version. Before analysis, compare the file's city and transaction counts with the paper and verify whether weather inputs and fine-location fields are included. If the request fails, record the asset as restricted and use a separately documented substitute rather than calling a commercial product the same data.

## Connections and Limitations

A join to ERA5-Land is only as precise as the delivered location and date fields; city labels cannot justify building-level temperature exposure. City Statistical Yearbook controls require a boundary and city-code check. The strongest current knowledge is the paper's identity, scale, research role, and author-request route; the platform, exact coverage, file contents, and reproducibility remain intentionally open.
