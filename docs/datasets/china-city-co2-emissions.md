---
schema_version: 3
catalog_status: grounding
id: china-city-co2-emissions
name: CEADs China City-Level CO2 Emission Inventories (城市碳排放核算清单)
aka:
- CEADs
- 中国碳核算数据库
- 城市碳排放
- 中国城市二氧化碳排放
- Carbon Emission Accounts and Datasets
- City-level CO2 emission inventory China
provider: >-
  CEADs (Carbon Emission Accounts and Datasets, 中国碳核算数据库), established
  2016 by Professor Guan Dabo's team at Tsinghua University (per the official
  homepage read 2026-08-15: "established in 2016 by Professor Guan Dabo's
  team at Tsinghua University... free, open, and verifiable... platform's
  data have been downloaded more than 10 million times"). The City data
  family is one module of the CEADs multiscale inventory system.
china_related: true
domains:
- environment
- energy
- urban
- climate

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    City-level (prefecture) CO2 emission inventory files listed in CEADs'
    current City data catalog, flagship product "China City-Level CO2 Emission
    Inventory" (1997-2019), plus other city-level inventories. Its visible
    download control routes an anonymous visitor to the CEADs Account login
    page for product id 2032; the post-login route and delivered file are not
    publicly evidenced.
  availability: ready-made
  ordinary_researcher_feasible: false
  summary: >-
    Provider-first grounding (refreshed 2026-09-28): the current CEADs City
    page lists the 290-city 1997-2019 inventory and a visible download control,
    but that control opens a login page for the product rather than a public
    file. The provider's current disclaimer says
    CEADs data are made freely available to the public and scientific community,
    while asking users to cite the data, inform CEADs at the outset of a
    publication/presentation use, and discuss co-authorship early if the data
    are essential. A public China city study now directly
    verifies this product's research use: Jiang and Huang (2024) use the
    "Emission Inventories for 290 Chinese Cities from 1997 to 2019" as their
    city carbon-emissions input for a 222-city 2011-2019 analysis. This is
    distinct from the CEADs county/district nighttime-light inventory used by
    the separately checked JEEM 2024 paper. The City module remains a strong
    candidate for a researcher able to use the provider account/contact route,
    but the post-login delivery flow, file contents, and detailed terms remain
    unclosed.
  barrier: >-
    The current City catalog lists the product and the broader data directory
    labels City Level as "files." Its visible download control opens a CEADs
    login page for this product; anonymous access therefore establishes an
    account boundary, not a file delivery route. Whether registration alone
    yields a file, along with file contents and any product-specific licence
    terms, remains unclosed.

unit_of_observation: >-
  city (prefecture-level) x year; emission inventories per city-year
  (flagship: 290 Chinese cities, 1997-2019)
structure: panel (city-year)
geo_granularity:
- prefecture-level city
geography: >-
  China, prefecture-level cities (flagship product: 290 cities, 1997-2019);
  CEADs homepage claims inventories covering "over 400 cities and regions"
  across its multiscale system.
time_span:
  start: '1997'
  end: '2019'
  last_confirmed_release: '290-city inventory 1997-2019 listed on the CEADs City page (fetched 2026-08-15)'
  coverage_note: >-
    The flagship product covers 1997-2019; the JEEM 2024 anchor paper uses
    2003-2017 city-level per-capita CO2 and CO2 intensity. Other CEADs city
    products cover subsets (e.g., 18 cities in Central China 2000-2014, 24
    cities 2010, 29 cities in the Central Plain, Tibetan cities).
  last_checked: '2026-09-28'
frequency:
- annual
sample_size: >-
  290 cities (flagship 1997-2019 inventory); additional city-subset products
  on the same page; CEADs platform claims 400+ cities and regions overall
  (homepage, 2026).
key_variables:
- City-level CO2 emissions (production-based; total and per-capita)
- CO2 intensity of GDP (paper-level use: per-capita CO2 and CO2 intensity of GDP)
- Emission inventories by sector/energy for some products (per product documentation)
- Supplementary city products: water inventory, mercury inventory, inclusive wealth index

research_fit:
  best_for:
  - City-level CO2 outcomes and carbon intensity panels for Chinese prefecture cities
  - City-level climate-policy or carbon-target work once the researcher separately establishes the relevant policy assignment and the exact CEADs product vintage
  - Cross-city carbon accounting and city-level climate-policy research
  choose_over:
  - Choose this over national/provincial carbon inventories when the unit of analysis is the prefecture-level city.
  - The CEADs family is the standard China CO2 inventory product; do not substitute satellite-derived proxies for accounting-based inventories without a documented measurement concept.
  not_good_for:
  - Firm-level emissions (use china-firm-pollution / firm-level reporting)
  - Real-time or post-2019 city CO2 (flagship product ends 2019; newer releases unverified)
  - Consumption-based/embodied city carbon without verifying the specific product module
  needs_join_for:
  - City-level covariates (GDP, population, industry structure) from statistical yearbooks or china-stat-yearbook family
  - Policy exposure (Low-Carbon City Pilot assignments) belongs to the variation side (Econ-Variation) - this record documents the data product only
  variation_available:
  - City-year differences in CO2 levels and intensity are outcome dimensions of the inventory.
  - Policy assignments are external to this record and require their own evidence; no policy treatment is encoded here.
  topics:
  - carbon emissions
  - CO2 inventory
  - low-carbon city pilot
  - climate policy
  - city panel

good_for:
- city-level carbon accounting
- low-carbon city pilot evaluation
- carbon intensity outcomes
identification:
- The City inventory is an outcome/covariate product, not a causal design or a verified policy-assignment dataset.
- Any synthetic-control, difference-in-differences, or fixed-effects design requires independently verified assignment, timing, and comparison information.
linkable_keys:
- City (prefecture) name/code
- Year

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - city
  - year
  method: city-year covariates (GDP, population) matching
  evidence_status: plausible

access_routes:
- route: official-download
  access_status: needs-verification
  direct_url: https://www.ceads.net/data/carbon-inventory/city-level/
  requirements: Use the provider's Account/contact route; clicking the named product's download control currently leads anonymous visitors to a login page, and the public evidence does not establish whether registration is sufficient
  steps:
  - Open the current carbon-inventory City Level catalog (https://www.ceads.net/data/carbon-inventory/city-level/).
  - Locate "China City-Level CO2 Emission Inventory" (1997-2019) and preserve its listing date and stated unit before contacting or using Account access.
  - Log in through an existing legitimate CEADs account, or contact the provider, to confirm whether a named individual can obtain the file, what registration/approval is required, and the exact delivered filename/version.
  - Read and follow the CEADs disclaimer before use: cite the data, inform CEADs at the outset if using it for a publication or presentation, and discuss authorship early if the data are essential to the work.
  deliverable: >-
    Provider catalog listing for a city-year CO2 inventory (1997-2019); a
    delivered data file is not yet independently observed.
  cost: free
  last_checked: '2026-09-28'
  caveat: The provider calls CEADs data freely available, but its public download control sends anonymous visitors to login rather than a file. Do not describe this as registration-only access until an actual provider route and deliverable are verified.
- route: chinese-site
  access_status: needs-verification
  direct_url: https://www.ceads.net.cn/
  requirements: Navigate from the Chinese portal and verify the target product's actual Account/contact route
  steps:
  - Use the Simplified Chinese portal for Chinese-language product pages.
  - Confirm that its listed product, delivery and terms match the English catalog before using it.
  deliverable: Chinese-language provider portal; no end-to-end city-file delivery was observed.
  cost: free
  last_checked: '2026-08-15'
  caveat: The CN data/city/ path returned 404 for the guessed URL (2026-08-15); homepage navigation and the shared header do not prove the same registration/download workflow.

access:
  url: https://www.ceads.net/data/city/
  cost: free
  license: >-
    CEADs says its data are freely available to the public and scientific community;
    users should cite them and inform CEADs when data are intended for a publication
    or presentation. Discuss co-authorship early when the data are essential to the work.
    Exact product-specific licence terms remain unverified.
  format: []
  api: false
  how_to_get: Start with the current City Level catalog and its product-specific Account login route, then verify the precise delivered product before planning analysis; the public page alone does not prove a registration-only download.
caveats: >-
  The JEEM 2024 paper does not use this 290-city City-module product as its
  stated input: it uses a distinct CEADs 2020 county/district nighttime-light
  inventory and aggregates it. The flagship City product ends 2019; verify
  its exact product vintage, downloadable contents, coverage, and applicable
  terms against the research design. The current structured catalog has a
  download control but stops anonymous visitors at login, so it does not
  prove an end-to-end registration/download route.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Jiang & Huang (2024), Impact of urban vitality on carbon emission—an analysis of 222 Chinese cities based on the spatial Durbin model'
  doi: https://doi.org/10.1057/s41599-024-03708-9
  journal: Humanities and Social Sciences Communications
  year: 2024
  dataset_role: Carbon-emissions input in a 222-prefecture-city panel for 2011-2019
  evidence_type: published-paper-full-text
  evidence_url: https://www.nature.com/articles/s41599-024-03708-9
  data_note: >-
    Open full text, data-source section, read 2026-09-28: the paper states
    that it uses CEADs' "Emission Inventories for 290 Chinese Cities from
    1997 to 2019" for carbon emissions, covering 47 socioeconomic categories
    and 17 fossil fuels. The paper's analysis keeps 222 prefecture-level
    cities and 2011-2019 after its own data-availability restrictions; that
    analysis subset must not be mistaken for the provider product's 290-city
    1997-2019 coverage.

provenance:
- source: https://www.ceads.net/
  field_scope:
  - provider
  - platform_claims
  - coverage
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.ceads.net/data/city/
  field_scope:
  - product_family
  - coverage_years
  - access
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.ceads.net/disclaimer/
  field_scope:
  - Provider statement that CEADs data are freely available to the public and scientific community
  - Expected citation, pre-publication/presentation notice, and possible early co-authorship discussion for essential data use
  - Provider contact route for data questions
  added: '2026-09-28'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-city-co2-emissions, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/221669299/ZhangH2024Climate.pdf
  field_scope:
  - Primary-paper clarification that its main 2003-2017 city outcomes use CEADS (2020) county/district nighttime-light emissions aggregated to cities
  - 2,735 counties/districts, around 350 administrative divisions, and 1997-2017 coverage for that distinct source asset
  - Boundary that this citation does not prove use of the City module's 290-city 1997-2019 product
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.nature.com/articles/s41599-024-03708-9 (open paper text, read 2026-09-28)
  field_scope:
  - actual use of the 290-city 1997-2019 CEADs product
  - product's stated 47 socioeconomic categories and 17 fossil-fuel scope
  - paper-specific 222-city, 2011-2019 analysis subset
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.ceads.net/data/carbon-inventory/city-level/ and https://www.ceads.net/data/
  field_scope:
  - Current provider catalog lists China City-Level CO2 Emission Inventory, 1997-2019, as an annual City product published 2022-10-11
  - Current public directory labels the City Level collection as files
  - Visible download control for product id 2032
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.ceads.net/user/index.php?id=2032&lang=en (read 2026-09-28)
  field_scope:
  - The named product's visible download control opens this CEADs Account page
  - Anonymous visitors receive a Login form with a Sign Up link, not a delivered data file
  - Boundary that the post-login delivery, filename/version, fields, permissions and product-specific terms remain unobserved
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets: []
---

## Positioning in one sentence

CEADs is a China carbon-accounting platform whose City module lists a 290-city 1997-2019 product; it is a distinct product from the CEADs county/district inventory that the checked JEEM 2024 paper actually aggregates to cities.

## Select rules

- Consider it for city-level CO2 levels/intensity panels in Chinese prefecture cities after confirming the registered deliverable and exact product vintage.
- Verify the exact product vintage and city coverage against the research window (flagship ends 2019).
- Do not use the JEEM 2024 paper as evidence that this 290-city product was used; its data section identifies a separate CEADs county/district inventory.

## Get recipe

1. Open the current CEADs City Level catalog and identify the named 290-city, 1997--2019 product (or the smaller product matching the research design); record the listing date, unit and stated coverage.
2. The download icon for the named item currently opens an Account login page. Use a legitimate account or the provider contact route to verify whether a named researcher can obtain that exact file, which registration or approval is required, and the delivered filename, version, fields and terms. Anonymous access stops before these facts.
3. Only after observing the actual delivered file, review the applicable disclaimer/citation expectations, retain the precise version with the analysis record, and distinguish it from CEADs county/district or other city-subset inventories.

## Connections and Limitations

- Jiang and Huang (2024) directly use the 290-city City-module product, while the checked JEEM 2024 paper identifies a different CEADs county/district inventory; do not treat the two assets as interchangeable.
- Product coverage varies across CEADs city modules (290 cities vs smaller subsets); always verify city count and years for the specific file.
- The current catalog establishes identity, paper use, and an account-login boundary, not an end-to-end ordinary acquisition route. Until a delivered file and its terms are observed, do not promise that a new researcher can download the product merely by registering.
- This record documents the data product only; policy assignment and treatment timing (Low-Carbon City Pilot) belong to the variation side of the research design.
