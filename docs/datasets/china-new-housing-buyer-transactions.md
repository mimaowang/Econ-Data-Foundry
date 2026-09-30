---
schema_version: 3
catalog_status: ready
id: china-new-housing-buyer-transactions
name: Chu, Kuang & Zhao (ECIN 2025) new-housing transaction data with buyer identity (anti-corruption)
aka:
- ECIN replication package 213181
- 'The Effect of the Anti-Corruption Campaign in China: Evidence from Housing Transactions'
- full_data.dta (openICPSR 213181)
provider: >-
  Paper authors Yongqiang Chu (UNC Charlotte), Weida Kuang (RUC School of
  Business), Daxuan Zhao (RUC School of Business); replication data
  deposited at openICPSR project 213181 ("ECIN Replication Package..."),
  distributed by ICPSR.
china_related: true
domains:
- housing
- urban
- political-economy
- public-economics

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: >-
    openICPSR project 213181 replication package containing the paper's
    analysis data (at least full_data.dta and regression_tables_figures.do
    per search-indexed openICPSR file records for V2) and code; versions
    V1, V2 (modified 2025-03-07), V4 (DataCite publicationYear 2026,
    updated 2026-04-22, view V4.1). DOI family 10.3886/E213181V1/V2/V4
    (IsVersionOf 10.3886/e213181).
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Grounding pass (2026-08-15): the replication package is confirmed via
    openICPSR OAI metadata (title, creators = paper authors, full abstract,
    subjects H10/O10/R31 + "administration records") and DataCite records
    for V1/V2/V4. The package is the paper's own data: price discounts
    government officials receive when buying new housing units (corruption
    measure), anti-corruption campaign 2012, discounts decrease sharply
    after the campaign, no effect on existing housing sales, officials
    less likely to buy lucky-number units. Full-data file exists
    (full_data.dta). Access requires the openICPSR download flow (project
    page 403s automated clients; ICPSR V4.1 page is a JS shell).
  barrier: >-
    The paper's data section is unread (Wiley 403 for automated clients;
    SSRN WP 3437329 exists per search index but is blocked), so the
    contents of full_data.dta (cities, years, buyer-identity fields,
    sample construction) are unverified. The current ICPSR download terms,
    access level, and file manifest must be checked in a human browser.

unit_of_observation: >-
  New-housing-unit transaction with buyer identity (government official
  status inferred from price discounts) - unit unverified until the dta or
  paper data section is read
structure: transaction-level data (full_data.dta)
geo_granularity:
- city (unverified)
geography: China (city coverage unverified)
time_span:
  start: '2008'
  end: '2017'
  last_confirmed_release: 'openICPSR 213181 V4.1 (DataCite updated 2026-04-22)'
  coverage_note: >-
    Anti-corruption campaign launched 2012; exact transaction window
    unverified (candidate registered the paper as EI 2025, DOI
    10.1111/ecin.70002, published 2025-10).
  last_checked: '2026-08-15'
frequency:
- transaction-level
sample_size: >-
  Unverified (package file sizes unread).
key_variables:
- New-housing transaction price and discount measure (corruption proxy)
- Buyer identity fields (per paper design)
- Existing-housing-sales comparison series
- Lucky-number unit indicator (robustness per abstract)

research_fit:
  best_for:
  - Reproducing or extending the Chu-Kuang-Zhao anti-corruption/housing-discount analysis with the authors' own data and code
  - Buyer-identity-linked new-housing transaction research where the openICPSR file is the starting point
  choose_over:
  - Choose this record over china-jrs-sweating-assets-housing-transactions-2026 (second-hand, 26 cities) and china-beike-housing-transactions-2026 (Beike, candidate) when the design needs buyer-identity/discount information with the paper's released file.
  not_good_for:
  - Treating the package as raw developer or government transaction records (it is the paper's prepared analysis file).
  - Assuming unrestricted redistribution (openICPSR terms apply).
  needs_join_for:
  - City covariates (china-stat-yearbook family)
  - Policy timing details of the anti-corruption campaign (Econ-Variation side)
  variation_available:
  - Transaction-level variation around the 2012 campaign (paper's DiD design)
  topics:
  - housing transactions
  - anti-corruption
  - buyer identity
  - corruption measurement

good_for:
- corruption-in-housing research
- new-housing transaction panels
- replication of ECIN 2025 results
identification:
- This is a paper-specific housing-transaction and code package, not a stand-alone causal-variation record. It supports obtaining and inspecting the released replication artifact; any new causal-design claim requires a separate assessment.
linkable_keys:
- City identifier (unverified)
- Transaction/unit identifiers (unverified)

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - city
  - year
  method: city-year covariate matching
  evidence_status: plausible

access_routes:
- route: openicpsr-replication
  access_status: available-with-registration
  direct_url: https://www.openicpsr.org/openicpsr/project/213181/version/V4/view
  requirements: openICPSR account and the current download flow; project page 403s automated clients
  steps:
  - Open project 213181 (latest version V4/V4.1) and inspect the file listing.
  - Download full_data.dta and regression_tables_figures.do (and any README).
  - Read the paper's data section (SSRN WP 3437329 or Wiley full text in a human browser) for variable definitions.
  deliverable: The authors' analysis data and Stata code.
  cost: free
  last_checked: '2026-09-28'
  caveat: Current DataCite verifies that the authors' active, findable V4 study resolves to ICPSR's V4.1 study page, but does not expose a file manifest, licence, or current download terms. Earlier OAI/search-index evidence names at least full_data.dta and regression_tables_figures.do for V2; do not assume that V4.1 has the same files.
- route: working-paper
  access_status: needs-verification
  direct_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3437329
  requirements: Human browser (SSRN blocks automated clients)
  steps:
  - Download the WP PDF for the data description.
  - Compare WP and published versions.
  deliverable: WP PDF.
  cost: free
  last_checked: '2026-08-15'
  caveat: SSRN connection timeout for automated clients (2026-08-15); WP identity from search index only.

access:
  url: https://www.openicpsr.org/openicpsr/project/213181/version/V4/view
  cost: free
  license: openICPSR distribution terms (as received from depositor; exact license file unverified)
  format:
  - dta
  - do
  api: false
  how_to_get: >-
    Register on openICPSR, open project 213181 V4, and download the package
    files.
caveats: >-
  full_data.dta contents (sample, cities, years, buyer-identity fields) are
  unverified - the paper's data section and the dta itself are unread by an
  automated client. The package is the paper's prepared analysis file, not
  raw developer records. Redistribution follows openICPSR terms.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Chu, Kuang & Zhao (2025), The effect of the anti-corruption campaign in China: Evidence from housing transactions'
  doi: https://doi.org/10.1111/ecin.70002
  journal: Economic Inquiry
  year: 2025
  dataset_role: New-housing transaction data with buyer-identity price discounts (main analysis; author-deposited replication data)
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/213181/version/V4/view
  data_note: >-
    Replication package identity verified 2026-08-15 via openICPSR OAI
    (title, creators, abstract, subjects) and DataCite (V1/V2/V4). Full
    abstract: price discounts for government officials buying new housing;
    discounts decrease sharply after the 2012 campaign; no effect on
    existing housing sales; officials less likely to buy lucky-number
    units. Paper data section unread (Wiley 403); SSRN WP 3437329 exists
    (search-index identity only).

provenance:
- source: openICPSR OAI record 213181 (pcms.icpsr.umich.edu, read 2026-08-15)
  field_scope:
  - package identity
  - creators
  - full abstract
  - subjects (H10/O10/R31, administration records)
  - DOI 10.3886/E213181V1/V2
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite API 10.3886/E213181V1/V2/V4 (read 2026-08-15)
  field_scope:
  - version dates (V2 modified 2025-03-07; V4 updated 2026-04-22)
  - latest view URL (V4.1)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite API record 10.3886/E213181V4 (queried 2026-09-28)
  field_scope:
  - current V4 identity and authorship
  - current ICPSR V4.1 study route
  - active/findable status
  - package abstract and 2025 issuance
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Crossref API 10.1111/ecin.70002 (read 2026-08-15)
  field_scope:
  - author affiliations (UNC Charlotte, RUC)
  - publication date (2025-10)
  - abstract (partial)
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: china-jrs-sweating-assets-housing-transactions-2026
  relation: often-confused-with

production:
  raw_sources:
  - name: Paper-specific new-housing transaction records with buyer identity (developer-side; provider unnamed in all readable sources)
    source_type: dataset
    role: Source records behind the released full_data.dta (price discounts for officials buying new housing units)
    access_route: Not public; released in prepared form via openICPSR 213181
    url: https://www.openicpsr.org/openicpsr/project/213181/version/V4/view
    coverage: Unverified (cities, years, fields unread)
    last_checked: '2026-08-15'
  acquisition_methods:
  - repository download
  - researcher-collected source records (origin per paper)
  sample_construction: >-
    The openICPSR package is the authors' prepared analysis data (full_data.dta)
    and code (regression_tables_figures.do); the underlying raw transaction
    records are not released. Exact sample construction (cities, window, buyer-
    identity coding) must be read from the paper's data section (SSRN WP 3437329
    or Wiley full text in a human browser) - unverified this round.
  pipeline_stages:
  - stage: collect
    inputs:
    - New-housing transaction records (provider unnamed)
    method: Authors' collection of transaction records with buyer identity; details unread
    tools: []
    output: Source transaction records (not released)
    evidence: Paper abstract (discount measure) and openICPSR metadata; exact collection method unread
  - stage: clean
    inputs:
    - Source transaction records
    method: Authors' cleaning into full_data.dta (fields unverified)
    tools:
    - Stata
    output: full_data.dta
    evidence: openICPSR file URL (search-indexed OAI record, V2)
  - stage: other
    inputs:
    - full_data.dta
    method: Regression tables and figures via the deposited do-file
    tools:
    - Stata
    output: regression_tables_figures.do outputs
    evidence: openICPSR file URL (search-indexed OAI record, V2)
  output:
    unit_of_observation: New-housing transaction (unverified)
    structure: Transaction-level dataset
    geography: China (cities unverified)
    time_span: Around the 2012 anti-corruption campaign (exact window unverified)
    key_variables:
    - Transaction price and discount
    - Buyer identity (official status per paper design)
    - Existing-housing comparison series
    formats:
    - dta
  reproducibility:
    level: needs-verification
    starting_point: https://www.openicpsr.org/openicpsr/project/213181/version/V4/view
    code_available: true
    requirements:
    - openICPSR account
    - Stata
    blockers:
    - full_data.dta contents (sample, fields) unread
    - Raw transaction records not released
  compliance:
    terms_or_license: openICPSR distribution terms (as received from depositor); exact license file unverified
    robots_or_rate_limits: Use the openICPSR download route; do not scrape
    personal_or_sensitive_data: Buyer-identity fields may be sensitive; follow depositor terms
    redistribution: Verify the package license before redistribution
    review_needed: true
---

## Positioning in one sentence

The EI 2025 anti-corruption housing paper's own data is downloadable: the authors deposited their analysis data (full_data.dta) and code at openICPSR 213181 (V1-V4.1), so a researcher can reproduce or extend the buyer-discount analysis - though the file's exact sample and fields are unverified until the dta is inspected.

## Select rules

- Choose this record when the research needs buyer-identity-linked new-housing transactions and the authors' released file is the intended starting point.
- Use the second-hand transaction records (china-jrs-sweating-assets-housing-transactions-2026) or Beike candidate for different provider/sample frames - do not merge without comparing the dta.
- Read the paper data section (SSRN WP or Wiley, human browser) before interpreting full_data.dta fields.

## Get recipe

1. Register on openICPSR and open project 213181 V4.
2. Download full_data.dta, regression_tables_figures.do, and any README.
3. Read the WP (SSRN 3437329) or published data section for variable definitions and sample construction.
4. Record the exact version (V1/V2/V4.1) used.

## Connections and Limitations

- "Administration records" (OAI subject) suggests administrative transaction records, but the raw provider identity (developer records vs platform) is unread.
- The package is the paper's analysis file - treat it as research output, not raw housing-market data.
- openICPSR terms apply to redistribution; verify the license file in the package.
