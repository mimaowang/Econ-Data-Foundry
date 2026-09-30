---
schema_version: 3
catalog_status: ready
id: china-aer-loan-access-experiment-markets-2024
name: Cai & Szeidl (2024 AER) China loan-access field experiment data (3,173 firms in 78 retail markets)
aka:
- Indirect Effects of Access to Finance replication data
- China SME loan-product market-level RCT dataset
- openICPSR project 197302
provider: Jing Cai (University of Maryland) and Adam Szeidl (Central European University); replication deposit at ICPSR/openICPSR; partner bank (unnamed major Chinese commercial bank) supplied loan records
china_related: true
domains:
- finance
- firm
- development
- urban-markets
- field-experiment

data_pathway:
  mode: hybrid
  origin: researcher-collected
  target_artifact: >-
    Firm-level panel of 3,173 firms in 78 government-defined retail markets in one
    large prefecture-level city of a southeastern-China province, with market-level
    and firm-level experimental treatment assignment (80%/50%/0% intensity), three
    long surveys (2013 baseline, 2015 midline, 2016 endline) plus a 2020 short
    follow-up (market/firm/consumer surveys), and partner-bank loan records
    (borrowing, month, interest rate, amount). Published as openICPSR replication
    package 10.3886/E197302V1 ("Data and code").
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The paper's full text documents the experiment and data construction: in summer
    2013 the authors randomized treatment intensity across 78 retail markets (37 at
    80%, 10 at 50%, 31 pure control) for a new collateral-free bank loan product
    introduced in 2013 by a partner bank; 3,173 firms (random half of the 6,000+
    firm population) were surveyed at baseline/midline/endline, with a 2020 follow-up
    adding price and consumer-satisfaction data, and the bank provided borrowing
    records. The AER article page links the replication package to openICPSR
    (10.3886/E197302V1); the current DataCite record confirms a findable ICPSR v1
    deposit ("Data and code for: Indirect Effects of Access to Finance", 2024,
    geoLocation China) pointing to the same openICPSR project. The deposit's
    file manifest has not been opened (openICPSR blocks automated clients), so the
    exact contents remain unverified.
  barrier: >-
    The released deposit is the acquisition route, but openICPSR project pages return
    403 to automated clients and its file manifest, formats, and whether raw survey
    responses and bank records are both included have not been verified. The
    underlying raw inputs (market-office firm lists, partner-bank loan records) are
    confidential partnership data; only the released deposit can be shared.

unit_of_observation: Firm (small and medium enterprise) in a retail market; outcomes and treatment at firm level, treatment intensity randomized at market level
structure: Panel of firms (2013 baseline, 2015 midline, 2016 endline, 2020 short follow-up) nested in 78 markets
geo_granularity:
- market (government-defined cluster of retail/service firms)
- county (stratification)
- one large prefecture-level city (over 20,000 sq km)
geography: One large prefecture-level city in a southeastern-China province; 78 local markets; province anonymized in the paper
time_span:
  start: '2013'
  end: '2020'
  last_confirmed_release: '2024-07-10'
  coverage_note: >-
    Baseline summer 2013 (fiscal-year data ending June 2013), midline summer 2015,
    endline summer 2016, short follow-up summer 2020. Bank loan records cover
    borrowing under the new loan product from 2013 onward. Replication deposit
    registered 2024-07-10 (DataCite).
  last_checked: '2026-08-15'
frequency:
- panel waves (2013, 2015, 2016, 2020)
sample_size: 3,173 surveyed firms in 78 markets (random half of the 6,000+ firm population); average ~41 surveyed firms per market, ~82 total per market
key_variables:
- Firm characteristics: sales (self-reported and book value at endline), profits, employment, cost categories, balance-sheet variables
- Managerial characteristics: demographics (age, gender, education), political connections (past government work)
- Financial and business activities: formal and informal borrowing, trade credit, number of suppliers and clients, product introduction, renovation, advertising; loan purpose (endline)
- Consumer measures (2020): price of main product in 2016, share of employees with high school education in 2016, customer ratings of service quality, shopping environment, value for money, overall satisfaction
- Bank records: whether borrowed under the new product, borrowing month, interest rate, loan amount
- Treatment: firm-level treatment (loan-officer visits), market-level intensity arm (80%/50%/0%), stratification cells (22 market strata; firm strata by employment)
- Market identity and broad product category; competitor definition = same market + same specialized product category

research_fit:
  best_for:
  - Estimating direct and indirect (spillover) effects of access to finance on firm performance, business quality, prices, and consumer surplus
  - Market-level treatment-intensity designs with firm-level spillovers (randomized intensity across markets)
  - Welfare evaluation combining producer and consumer surplus from experimental variation
  - Research on SME lending frictions (collateral requirements, information frictions) in Chinese retail markets
  choose_over:
  - Choose this over observational firm panels (asif, china-firm-registry) when the research question requires experimentally randomized access to credit and measured competitor spillovers.
  - Choose this over survey-based credit-access studies when treatment assignment, bank records, and consumer-side outcomes are all needed.
  - Not a substitute for nationally representative firm data; the sample is one city's retail/service markets.
  not_good_for:
  - Nationally representative SME credit statistics or aggregate financial-inclusion trends
  - Identifying bank credit supply outside the single partner bank and loan product
  - Long-run firm dynamics beyond 2020 (only one short follow-up after 2016)
  - Reconstructing the raw experiment without the deposit: market-office lists and bank records are confidential partnership inputs
  needs_join_for:
  - Macro or regional controls (city-year statistics) if generalizing beyond the study city
  - Firm registration or tax records for external validation of survey-reported outcomes
  - Other bank or FinTech lending data for comparing the loan product with the market outside the experiment
  variation_available:
  - Market-level randomization into 80%/50%/0% treatment-intensity arms (stratified by county and market size)
  - Firm-level randomization of loan-officer visits within treated markets
  - Both dimensions support direct/indirect effect decomposition; the design details belong to the Econ-Variation repository.
  topics:
  - access to finance
  - field experiment
  - firm performance
  - spillovers
  - SME lending
  - retail markets

good_for:
- Direct/indirect effect decomposition of credit access on firm outcomes
- Consumer surplus and welfare evaluation of credit expansion
- Spillover analysis within localized product markets
identification:
- This is a paper-specific firm-survey, bank-record, and code asset, not a stand-alone causal-variation record. It supports reproducing the documented experiment and inspecting released treatment/outcome fields; any new identification claim needs its own design assessment.
linkable_keys:
- Firm identifier within the survey sample
- Market identifier and market broad product category
- County and stratification cells
- Survey wave (year)

joins:
- target: china-firm-registry
  relation: complement
  keys:
  - Firm name/registration identifiers if released and mappable
  method: External validation of firm existence or characteristics would require the deposit's identifiers; registry extracts cover different vintages and coverage, so matching is unverified.
  evidence_status: plausible
# City-level context joins are constrained because the study city is anonymized
# in the paper; no city-yearbook join target is declared (repository has no
# city-yearbook record).

access_routes:
- route: openICPSR replication deposit (AEA Data and Code policy)
  access_status: available-with-conditions
  direct_url: https://doi.org/10.3886/E197302V1
  requirements:
  - Free ICPSR/openICPSR account; download terms per the deposit
  steps:
  - Open the AER article page (doi.org/10.1257/aer.20220711) and follow the Additional Materials > Replication Package link (https://doi.org/10.3886/E197302V1).
  - Alternatively go directly to https://www.openicpsr.org/openicpsr/project/197302/version/V1/view.
  - Download the package and read the README/file manifest to confirm which files are included (survey data, bank records, code).
  deliverable: Data and code for the paper (per DataCite title); exact file list unverified because openICPSR blocks automated clients (403).
  cost: free
  last_checked: '2026-09-28'
  caveat: DataCite metadata and the AEA page confirm the deposit; the manifest itself was not opened this round. Raw market-office lists and bank-internal records are not expected to be public beyond the deposit.
- route: NBER working paper (w23906-style preprint, cached full text)
  access_status: available
  direct_url: https://www.nber.org/papers/w23906
  requirements: None for the working paper PDF
  steps:
  - Use the working-paper full text to understand the design and data construction before requesting the deposit.
  deliverable: Working-paper text (design, surveys, summary statistics); not the data.
  cost: free
  last_checked: '2026-08-15'
  caveat: The NBER working-paper URL is the paper's standard preprint location; the cached file was fetched from a university mirror this round - verify the exact NBER page before relying on it.

access:
  url: https://doi.org/10.3886/E197302V1
  cost: free
  license: ICPSR deposit terms; no redistribution of restricted components
  format:
  - replication package (data + code), formats unverified
  api: false
  how_to_get: From the AER article page follow the Replication Package link to openICPSR project 197302 V1; download with a free account and read the manifest before reuse.

caveats:
- The experiment site (province, city, partner bank) is anonymized in the cached full text; the replication package may name them or keep them anonymized - unverified.
- The bank's loan approval rate was ~47% and repayment rate ~98% (paper); bank screening was independent of the authors.
- The loan product: uncollateralized, ~0.7% monthly interest (15% discount vs existing formal loans), credit limit up to 30% of net assets, capped at RMB 500,000, two-year repayment.
- Survey sample = random half of the 6,000+ market firm population (3,173 firms); consumer survey samples customers visiting firms in 2020.
- Exact contents of the openICPSR deposit (variables, waves included, code) are unverified; treat the deposit as the authoritative source before any replication claim.

production:
  raw_sources:
  - name: Market-office firm lists (78 markets)
    source_type: dataset
    role: Sampling frame of all active firms with formal-employee counts (6,000+ firms)
    access_route: Provided to the authors by market offices in spring 2013; not public
    url: needs-verification
    coverage: All active firms in the 78 study markets, spring 2013
    last_checked: '2026-08-15'
  - name: Partner-bank loan records
    source_type: dataset
    role: Which firms borrowed under the new product, borrowing month, interest rate, loan amount
    access_route: Supplied to the authors by the partner bank; confidential partnership data
    url: needs-verification
    coverage: New-loan-product borrowing in the study markets, 2013 onward
    last_checked: '2026-08-15'
  - name: Author-run surveys (2013/2015/2016 long surveys; 2020 short follow-up)
    source_type: dataset
    role: Firm, manager, market, and consumer outcomes
    access_route: Collected in person by locally hired enumerators with market-office and bank introductions
    url: needs-verification
    coverage: 3,173 surveyed firms; consumer survey at 2020 follow-up
    last_checked: '2026-08-15'
  acquisition_methods:
  - in-person survey (long surveys)
  - retrospective survey (2020 follow-up)
  - bank administrative records
  - market-office administrative lists
  sample_construction: >-
    Population = all active firms in the 78 markets (6,000+, lists from market
    offices, spring 2013). Random half sampled within each market-strata cell for
    surveying (3,173 firms). Market-level randomization: 37 markets 80% intensity,
    10 markets 50%, 31 markets 0%, stratified by county and market size relative to
    county median (22 strata). Firm-level randomization of treated firms within
    markets stratified by employment relative to market median.
  pipeline_stages:
  - stage: collect
    inputs:
    - Market-office firm lists
    - Baseline/midline/endline surveys
    - Bank records
    - 2020 follow-up surveys
    method: Field experiment with market- and firm-level randomization; in-person surveys; bank administrative extract
    output: Firm-wave panel with treatment arms and bank borrowing records
    evidence: Paper section 2 (Context, design, and data)
  - stage: validate
    inputs:
    - Survey data
    - Book-value sales (endline, physically shown by accountant/manager)
    - Bank records
    method: Book-value sales cross-check; summary statistics and balance tests in Table 1 (clustered at market level)
    output: Balance-checked analysis sample
    evidence: Paper section 2.2 and Table 1
  constructed_variables: []
  validation:
  - Balance tests of treatment arms on baseline characteristics (paper Table 1)
  - Book-value sales verification at endline (paper section 2.1)
  output:
    unit_of_observation: Firm (with market, treatment-arm, wave identifiers); consumer-survey records at customer level (2020)
    structure: Panel with market-level intensity arms and firm-level treatment
    geography: One prefecture-level city in southeastern China (anonymized); 78 markets
    time_span: 2013-2020 (survey waves; bank records 2013 onward)
    key_variables:
    - Sales, profits, employment, costs
    - Manager demographics and political connections
    - Borrowing (formal/informal), trade credit, suppliers/clients
    - Price and consumer satisfaction (2020)
    - Bank borrowing, month, rate, amount
    - Treatment indicators and intensity arms
    formats:
    - deposit formats unverified
  reproducibility:
    level: medium
    starting_point: https://doi.org/10.3886/E197302V1
    code_available: true
    code_url: https://doi.org/10.3886/E197302V1
    requirements:
    - openICPSR account and download
    - Stata or the language used by the deposit code
    - Read the manifest to identify included waves and variables
    blockers:
    - openICPSR 403 for automated clients (human browser needed)
    - Manifest and file contents unverified
    - Raw partnership inputs (bank records, market lists) not public
  compliance:
    terms_or_license: ICPSR/openICPSR terms for the deposit; AEA data-policy compliance expected
    robots_or_rate_limits: openICPSR blocks automated clients (403 observed); use a human browser
    personal_or_sensitive_data: Survey and bank records may contain firm/manager-identifying information; follow deposit terms
    redistribution: Redistribute only as the deposit license permits; never redistribute raw bank or market-office data
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Cai, Jing; Szeidl, Adam (2024), Indirect Effects of Access to Finance, American Economic Review 114(8): 2308-2351'
  doi: https://doi.org/10.1257/aer.20220711
  journal: American Economic Review
  year: 2024
  dataset_role: Main dataset (3,173-firm experiment across 78 markets) for direct/indirect effect and welfare analyses
  evidence_type: data-section
  evidence_url: https://www.aeaweb.org/articles?id=10.1257%2Faer.20220711
  data_note: >-
    Paper section 2 documents the design and data: 78 markets in a southeastern-China
    prefecture city; summer-2013 randomization into 80%/50%/0% intensity arms
    (37/10/31 markets); 3,173 surveyed firms; 2013 baseline, 2015 midline, 2016
    endline, 2020 follow-up; bank records on borrowing month, rate, amount. AER
    article page links the replication package to openICPSR 10.3886/E197302V1
    (DataCite: "Data and code for: Indirect Effects of Access to Finance", ICPSR,
    2024).

provenance:
- source: Working-paper full text (cached loan_pdf_mktudegy.txt), section 2 (Context, design, and data)
  field_scope:
  - experiment design (78 markets, 3 arms, stratification)
  - sample construction (3,173 of 6,000+ firms)
  - survey waves and variables
  - bank records and loan product terms
  - summary statistics and balance approach
  added: '2026-08-15'
  confidence: high
  verified: true
- source: AER article page (cached aea_loan.html) Additional Materials section
  field_scope:
  - Replication Package link to https://doi.org/10.3886/E197302V1
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite record 10.3886/E197302V1
  field_scope:
  - deposit existence, title ("Data and code..."), publisher (ICPSR), year (2024), geoLocation (China)
  - does not prove file contents or downloadability for automated clients
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite API record 10.3886/E197302V1, queried 2026-09-28
  field_scope:
  - current findable v1 ICPSR data-and-code deposit identity and openICPSR project route
  - title, 2024 publication year, and China geography
  - does not establish a file manifest, deposit license, current download terms, or public access to raw bank and market-office inputs
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-firm-registry
  relation: complement
- id: asif
  relation: complement
---

## Positioning in one sentence

A paper-specific field-experiment asset: 3,173 Chinese retail-market firms with randomized credit-access intensity at market level and firm level (2013-2020), released as an openICPSR replication package (10.3886/E197302V1) whose file manifest is still unverified; the raw bank and market-office inputs are confidential.

## Select rules

- Prioritize it when the question needs experimentally randomized access to credit with measured competitor spillovers and consumer-side outcomes.
- Switch to asif or china-firm-registry for observational firm panels and administrative registration records; switch to survey-based credit data for representative or national coverage.
- It cannot support national SME statistics, long-run dynamics past 2020, or re-creating the raw experiment: the bank's records and market-office lists are partnership-confidential.

## Get recipe

1. Read the working-paper full text (design and data section) to understand arms, waves, and variables.
2. Open the AER article page and follow Additional Materials > Replication Package to https://doi.org/10.3886/E197302V1 (openICPSR project 197302 V1); use a human browser (automated clients receive 403).
3. Download with a free ICPSR account and read the manifest: confirm which waves and variables are included and whether the bank-record component is released.
4. Run the deposit code against the released files before any extension; do not treat the working-paper text as the data.

## Connections and Limitations

Firms nest in markets (competitor = same market and same specialized product category); treatment intensity is at market level, treatment at firm level, so spillover analysis needs both identifiers. The city/province/bank are anonymized in the cached text, limiting joins to outside sources; city-yearbook context joins are coarse. The deposit's exact contents - the decisive open item - require a human browser on openICPSR.
