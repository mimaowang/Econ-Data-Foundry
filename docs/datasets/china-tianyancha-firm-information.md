---
schema_version: 3
catalog_status: ready
id: china-tianyancha-firm-information
name: Tianyancha Firm Information and Relationship Data (天眼查企业信息/API)
aka:
- 天眼查
- Tianyancha
- Tianyancha Open Platform
- 天眼查企业数据接口
provider: Tianyancha Open Platform; the current API protocol names Beijing Jindi Credit Service Co., Ltd. (北京金堤征信服务有限公司) as the API operator
china_related: true
domains:
- firm
- finance
- innovation
- regional
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Paid API responses or permitted query exports for selected Chinese firms; not the historical 7,837-firm panel assembled for Beraja, Yang and Yuchtman
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The official open platform currently documents a paid, token-authorized JSON API with a searchable catalogue of firm-identity, registration, ownership/relationship, operating, legal-risk and intellectual-property modules. A researcher can obtain a bounded current firm extract by choosing and purchasing a named endpoint, then querying with a company name, Tianyancha ID, registration number or unified social credit code. This makes the current commercial route usable, while internal-use conditions and changing endpoint scope make it only partially reproducible.
  barrier: The paper's historical database snapshot, firm universe, extraction date, and cleaning are not released. Current endpoint fields, prices, historical-event depth, geographic fields, and rate limits can change; a paid API response therefore does not reproduce the paper's panel or guarantee a complete firm census.

# Identity and Coverage
unit_of_observation: Company/entity record or company-linked event returned by a selected Tianyancha endpoint; the grain depends on the API module
structure: On-demand firm lookup with module-specific event and relationship lists
geo_granularity:
- Firm registered or operating location when the selected endpoint returns it
- Province/city labels require endpoint-level verification and researcher normalization
geography: Chinese firms and related entities represented in Tianyancha's current commercial database; universe completeness and historical geographic coverage are not established here
time_span:
  start: unknown
  end: ongoing
  last_confirmed_release: 'Official API catalogue checked 2026-09-28; endpoint-specific pages show current GET JSON services and token authorization'
  coverage_note: The ReStud paper used a database snapshot to identify 7,837 facial-recognition AI firms and collected founding year, capitalization, financing, subsidiary, and mother-firm information. The current API documentation does not establish that the same historical snapshot or a complete longitudinal universe is available.
  last_checked: '2026-09-28'
frequency:
- on-demand API query
- event history where the selected module supplies historical records
sample_size: Paper-specific use identified 7,837 Chinese facial-recognition AI firms; current API universe size and queryable historical coverage are not verified
key_variables:
- Company name and company ID
- Company type, establishment date, operating status, and registered capital
- Legal representative, registration number, unified social credit code, organization code, and taxpayer identification number where supplied by the basic-information endpoint
- Registration, ownership, investment, financing, operating, legal-risk, and intellectual-property fields in the selected module
- Parent/subsidiary or relationship links where the purchased endpoint supplies them
- Location fields only after confirming the endpoint's current schema

# Research routing
research_fit:
  best_for:
  - Resolving Chinese firm identity and linking firms across procurement, industrial, patent, or regional datasets
  - Firm-level ownership, financing, registration, risk, or relationship questions when paid commercial access is acceptable
  - Building a bounded regional firm roster from explicit identifiers and a documented query date
  choose_over:
  - Choose it over a manually scraped public website when a licensed API response and stable identifier are required; the protocol prohibits copying or machine scraping outside the API service
  - Choose an official enterprise registry or a released replication file when legal-source authority, full-population coverage, or reproducible historical snapshots matter more than cross-module enrichment
  - For exact replication of the ReStud AI-firm sample, seek the authors' licensed snapshot or replication materials; do not substitute today's API results
  not_good_for:
  - A free, shareable, nationally complete firm panel
  - Assuming that every firm, historical event, or city field is present for every year
  - Reconstructing the paper's 7,837-firm AI universe from a single keyword query
  - Causal treatment or exogenous-variation classification
  needs_join_for:
  - Government procurement contracts and prefecture outcomes
  - ASIF production or employment outcomes
  - Patent or software-product records
  - Statistical-yearbook population, GDP, or administrative boundary concordances
  variation_available:
  - Firm-level and regional cross-sectional dimensions only; no causal classification is made here
  topics:
  - firm registration
  - ownership and corporate networks
  - financing
  - innovation firms
  - regional firm composition

good_for:
- Company-name and identifier resolution before joining Chinese firm datasets
- Bounded, documented firm-level extracts under a paid licence
identification:
- >-
  Choose a named Tianyancha API endpoint rather than treating “Tianyancha” as
  one downloadable database. The current basic-information endpoint accepts a
  company name or ID and returns a JSON company record; the separate search
  endpoint accepts a keyword and returns a firm list. Ownership, annual-report,
  investment and historical fields are distinct paid modules. Record the
  endpoint ID/version, query date, input identifier and quota purchase with
  every extract, because the platform does not promise one static firm census.
linkable_keys:
- Company name
- Tianyancha company ID
- Registration number
- Unified social credit code
- Researcher-normalized province/city and query date

joins:
  - target: china-gov-procurement
    relation: complement
    keys:
    - Awardee firm name
    - Tianyancha company ID or unified social credit code where available
    - Contract year
    method: Resolve procurement awardee names to a stable firm identity, retain one-to-many and unresolved matches, and preserve the query date and endpoint used
    evidence_status: literature-used
  - target: asif
    relation: complement
    keys:
    - Firm name and registration identifiers where available
    - Province/city and year
    method: Use a documented entity-resolution crosswalk; do not assume the API's current name or ownership history matches the ASIF vintage
    evidence_status: plausible
  - target: china-patents
    relation: complement
    keys:
    - Firm name and normalized identifier
    - Application or grant year
    method: Resolve aliases and subsidiaries before aggregating patents to a parent firm
    evidence_status: plausible

access_routes:
  - route: Tianyancha Open Platform API
    access_status: available-with-conditions
    direct_url: https://open.tianyancha.com/api_list
    requirements:
    - Tianyancha account and acceptance of the current API protocol
    - Prepaid or package-based API quota; endpoint prices and quotas must be checked at purchase
    - Internal-use compliance and a review of privacy, copyright, and redistribution restrictions
    steps:
    - Select the exact endpoint from the official catalogue; its current pages distinguish, for example, basic-company information, keyword search, shareholder, investment and annual-report modules
    - Read the current schema, price, authorization method, rate limit, and coverage note before purchase
    - Query a small set of known firms by company name, ID, registration number, or unified social credit code
    - Save raw JSON responses, endpoint version, query date, and quota/account metadata
    - Build any regional or longitudinal panel separately, retaining unresolved names and missing modules
    deliverable: Current endpoint responses or permitted internal export; no historical paper snapshot or public bulk dump was verified
    cost: paid
    last_checked: '2026-09-28'
    caveat: Current official pages describe GET JSON calls with an Authorization token and display endpoint-level prices, but prices, quotas, schemas and available fields can change. The accessible catalogue documents a route, not a guarantee that a purchased module contains every historical or geographic field.
  - route: Tianyancha web query
    access_status: available-with-conditions
    direct_url: https://www.tianyancha.com/
    requirements:
    - User account and any applicable subscription
    - Manual use within the site's terms
    steps:
    - Search a firm by name or identifier to inspect identity and public-facing modules
    - Use the API route for machine-readable research extraction; do not scrape or mirror the website
    deliverable: Manual verification only; not a reproducible bulk dataset
    cost: mixed
    last_checked: '2026-09-28'
    caveat: The current user/API agreements prohibit unauthorized copying, machine scraping, mirroring, and redistribution.

access:
  url: https://open.tianyancha.com/api_list
  cost: paid
  license: Commercial API terms; internal use only unless a separate written permission applies, with explicit restrictions on scraping, copying, selling, or providing the service/data to other parties
  format:
  - JSON API response
  - permitted vendor export if offered
  api: true
  how_to_get: Read the current API catalogue and protocol, purchase a bounded endpoint quota, query by stable company identifiers, and retain the response and endpoint/version metadata. Do not present current API results as a release of the paper's historical firm panel.
caveats:
- The paper describes Tianyancha as a comprehensive Chinese firm database and uses it with Pitchbook to identify 7,837 facial-recognition AI firms; that establishes paper use, not public access to the extracted list.
- Current API fields and prices are dynamic. Verify whether registered address, historical ownership, financing, subsidiary, and parent-firm fields are available in the purchased endpoint before promising a regional panel.
- The API protocol states that API data are for internal use and prohibits unauthorized copying, machine scraping, mirroring, resale, or provision to other parties; public underlying records do not remove those contractual constraints.
- Firm names, subsidiaries, aliases, and historical ownership changes require a versioned entity-resolution crosswalk. A current lookup may not reproduce a historical firm identity.
- No claim is made here that the service is a representative census, that all historical events are complete, or that the paper's AI classification can be reconstructed from one endpoint.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-08-11'

used_by:
  - cite: 'Beraja, Yang & Yuchtman (2023), Data-intensive Innovation and the State: Evidence from AI Firms in China'
    doi: https://doi.org/10.1093/restud/rdac056
    journal: ReStud
    year: 2023
    dataset_role: Firm discovery and characteristics for the facial-recognition AI firm universe, including founding year, capitalization, financing, and subsidiary/mother-firm information
    evidence_type: data_section
    evidence_url: https://cbade.hkbu.edu.hk/wp-content/uploads/2023/01/20200812_YANG.pdf
    data_note: The paper identifies 7,837 Chinese facial-recognition AI firms from Tianyancha, validates the classification manually and against Pitchbook, and then links firms to software and procurement records. The paper-specific database snapshot, firm list, and cleaning file are not treated as a public release.

provenance:
  - source: https://cbade.hkbu.edu.hk/wp-content/uploads/2023/01/20200812_YANG.pdf
    field_scope:
    - paper actually uses Tianyancha
    - 7,837-firm AI universe
    - founding year, capitalization, financing, subsidiary, and mother-firm fields
    - Pitchbook cross-check and paper-specific snapshot boundary
    added: '2026-08-11'
    confidence: high
    verified: true
  - source: https://open.tianyancha.com/api_list
    field_scope:
    - current endpoint families and example company identifiers/fields
    - displayed pricing and API query route
    added: '2026-08-11'
    confidence: high
    verified: true
  - source: https://open.tianyancha.com/open/365
    field_scope:
    - Current basic-information endpoint identity, GET JSON delivery, Authorization-token method, company-name-or-ID input and endpoint-level price display
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://open.tianyancha.com/open/816
    field_scope:
    - Current keyword-search endpoint identity, JSON delivery, company-list result and name/company-ID/registration-number/unified-credit-code search boundary
    added: '2026-09-28'
    confidence: high
    verified: true
  - source: https://open.tianyancha.com/property/protocol
    field_scope:
    - current API operator and commercial terms
    - internal-use, anti-scraping, copying, and redistribution restrictions
    added: '2026-08-11'
    confidence: high
    verified: true

related_datasets:
  - id: china-gov-procurement
    relation: complement
  - id: asif
    relation: complement
  - id: china-patents
    relation: complement
---

## Positioning in one sentence

Tianyancha is a paid firm-information/API route for resolving and enriching Chinese company records, not a downloadable census and not the historical 7,837-firm file used in the ReStud paper; its value is cross-module identity and relationship information, while its main risks are changing fields, contractual restrictions, and non-reproducible historical snapshots.

## Select rules

- Use the API when a research project needs a licensed company identifier, ownership/financing/risk module, or a bounded firm extract that can be joined to procurement or regional outcomes.
- Use the official enterprise registry or a released replication file when legal-source authority, full-population coverage, public reproducibility, or historical version control is the priority.
- For the ReStud AI-firm application, treat Tianyancha as the source behind the paper's firm universe and seek the authors' or provider's historical snapshot; do not claim that a current API query reproduces it.
- Never use website scraping or mirror the result. The API and user agreements are part of the acquisition boundary.

## Get recipe

1. Open the official API catalogue and select the exact module needed; record price, quota, schema, and terms before purchase.
2. Test a small set of firms using company name, company ID, registration number, or unified social credit code. Save raw responses and endpoint/version metadata.
3. Construct the target firm table and regional crosswalk separately. Preserve aliases, subsidiaries, unresolved matches, query dates, and missing modules.
4. Join the resulting identities to procurement, ASIF, patents, or yearbooks only after checking the relevant time and geography definitions.
5. If the research requires the paper's historical AI sample or a shareable panel, stop and obtain a licensed snapshot or switch to an explicitly released alternative.

## Connections and Limitations

The most defensible join is by a stable company identifier, with name matching used only as a documented fallback. Province/city fields and historical ownership should be treated as endpoint-specific rather than assumed from the platform name. A current lookup can identify a firm that existed in the past but cannot by itself establish what the database contained when the ReStud authors collected their data. Any derived table must respect internal-use and redistribution restrictions.

## Decision sufficiency check

For a project linking Chinese government procurement to firm location or ownership, this record gives a concrete API start, a paid-access expectation, and the exact identifiers to test. It also states the failure boundary: if the chosen endpoint lacks the needed historical or geographic fields, if a shareable extract is required, or if a historical paper snapshot cannot be licensed, Tianyancha should not be presented as the solution.
