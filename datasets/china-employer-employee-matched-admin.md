---
schema_version: 3
catalog_status: grounding
id: china-employer-employee-matched-admin
name: China employer-employee matched Housing Provident Fund (HPF) administrative records (JHR 2024)
aka:
- 住房公积金
- Housing Provident Fund
- HPF
- 公积金数据
- employer-employee matched administrative data China
provider: >-
  City Housing Provident Fund Management Center (住房公积金管理中心) of an
  unnamed major Chinese city (per the authors' 2020 CES presentation: "an
  employer-employee matched administrative data... covers all the employees
  contributing HPF in a major city"). The HPF system is a compulsory monthly
  salary-contribution scheme (per the same presentation and the system's
  statutory basis).
china_related: true
domains:
- labor
- firm
- gender
- administrative

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    Employer-employee matched HPF contribution records for one major Chinese
    city (city anonymized in the paper): employee-month observations with
    deposit amount (from which salary base is inferred: deposit = base salary
    x 12% x 2), employee attributes (salary, age, gender), and employer
    attributes (sector, industry). Working-paper version: 138,532,302
    employee-month observations 2012-2014, 5.4 million employees, 100,000+
    employers; analysis file at employer-quarter level (new-hire salary,
    new-hire counts, job-leaver counts by gender).
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    Route-B grounding (2026-08-15): le.uwpress.org full text 403 for
    automated clients (recorded), so the data identity was recovered from the
    authors' own 2020 CES (China Economics Summer Institute) presentation by
    Agarwal, Li, Qin & Wu (fetched from cesi.econ.cuhk.edu.hk, read in full):
    the asset is HOUSING PROVIDENT FUND administrative data - NOT social
    security - covering all HPF contributors in one unnamed major city,
    138.5M employee-month observations 2012-2014, 5.4M employees, 100k+
    employers; salary inferred from deposit records (base salary x 12% x 2);
    employee attributes salary/age/gender; employer sector/industry; analysis
    at employer-quarter level with female-vs-male DiD around the November
    2013 One-Child relaxation. The published JHR 2024 version (Agarwal, Li,
    Qin, Wu & Yan, DOI 10.3368/jhr.0122-12126r2, published 2024-05-08) uses
    "an employer-employee matched administrative data" (abstract-level; data
    section unread). SSRN WP 3507515 exists (Dec 2019; SSRN timed out for
    automated clients). Access: restricted city HPF administrative microdata;
    city anonymized; no public route evidenced.
  barrier: >-
    City HPF administrative microdata are restricted (unnamed city); no
    public download or application route evidenced. Published JHR data
    section unread (le.uwpress.org 403); sample window of the published
    version (2012-2014 in the WP) unverified.

unit_of_observation: employee-month record within employer (matched employer-employee); analysis at employer-quarter (by gender)
structure: panel (employee-month; employer-quarter aggregates)
geo_granularity:
- city (one unnamed major city)
geography: One unnamed major Chinese city (WP version 2012-2014)
time_span:
  start: '2012'
  end: '2014'
  last_confirmed_release: '2020 CES presentation (WP version): 2012-2014 employee-month panel'
  coverage_note: >-
    WP version: 2012-2014, 138,532,302 employee-month observations. The
    published JHR 2024 version's sample window is unread (abstract does not
    state years; data section 403).
  last_checked: '2026-08-15'
frequency:
- monthly (contributions)
- quarterly (analysis)
sample_size: >-
  138,532,302 employee-month observations (2012-2014), 5.4 million
  employees, more than 100,000 employers (WP version); working sample after
  cleaning 72.37M observations (1.72M new hires, 1.21M leavers).
key_variables:
- HPF deposit amount (salary base x 12% x 2; new hires deposit current monthly salary)
- Inferred salary (new-hire salary from deposit records)
- Employee age, gender
- Employer sector and industry
- Derived: new-hire counts and job-leaver counts by gender and employer-month

research_fit:
  best_for:
  - Gender wage gap and hiring-discrimination studies using matched employer-employee administrative records
  - Fertility-policy shocks on labor-market outcomes (the JHR 2024 application: November 2013 One-Child relaxation, female-vs-male DiD at employer-quarter level)
  - New-hire salary setting and employer-level hiring/retention margins
  choose_over:
  - Choose this over survey data (cfps, charls) when the question needs population-wide employer-employee matched administrative records in one city with salary-based deposits.
  - The asset is city-specific and city-anonymized; for multi-city matched admin panels no catalog alternative exists.
  not_good_for:
  - Multi-city or national coverage (one city only)
  - Post-2014 outcomes unless the published version extends the window (unverified)
  - Total compensation (only the HPF-contribution-based salary measure)
  - Reconstructing the exact analysis extract: no public release evidenced
  needs_join_for:
  - Policy/timing details of the 2013 One-Child relaxation (variation side; Econ-Variation)
  - City-level context (housing, labor market) from statistical yearbooks
  variation_available:
  - Female vs male (treatment vs control within employers)
  - Pre/post November 2013 policy timing
  - Employer heterogeneity (SOEs vs private, size, industry)
  topics:
  - gender wage gap
  - employer-employee matched data
  - housing provident fund
  - fertility policy
  - labor market discrimination

good_for:
- gender wage gap
- hiring discrimination
- fertility policy and labor market
- administrative matched employer-employee data
identification:
- difference-in-differences (female vs male, pre/post policy)
- employer fixed effects
linkable_keys:
- Employer ID (anonymized)
- Employee ID (anonymized)
- Month/quarter

joins:
- target: china-census
  relation: complement
  keys:
  - city
  - year
  method: city-level context (coarse; one city only)
  evidence_status: plausible

access_routes:
- route: author-held
  access_status: unavailable
  direct_url: https://jhr.uwpress.org/content/early/2024/05/01/jhr.0122-12126R2
  requirements: None public; data availability statement of the published version unread (le.uwpress.org 403 for automated clients)
  steps:
  - Expect the HPF microdata to be author-held under a city HPF center agreement.
  - Contact the authors only if an access agreement is being negotiated; no public route evidenced.
  deliverable: No public deliverable; restricted city HPF administrative microdata.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Do not promise obtainability; city is anonymized in the paper.
- route: working-paper-evidence
  access_status: available
  direct_url: https://cesi.econ.cuhk.edu.hk/wp-content/uploads/PPT_Keyang_Li.pdf
  requirements: None
  steps:
  - Read the authors' 2020 CES presentation (Agarwal, Li, Qin & Wu) for the data description (HPF system, 2012-2014, 138.5M employee-month observations, cleaning steps, employer-quarter analysis).
  - SSRN WP 3507515 (Dec 2019) is the paper's working-paper version (SSRN timed out for automated clients on 2026-08-15).
  deliverable: Data description and construction details; not the data itself.
  cost: free
  last_checked: '2026-08-15'
  caveat: WP version may differ from the published JHR 2024 version.

access:
  url: https://jhr.uwpress.org/content/early/2024/05/01/jhr.0122-12126R2
  cost: by-application
  license: Restricted administrative data; no public license
  format: []
  api: false
  how_to_get: >-
    No public route. The asset is city HPF administrative microdata held
    under the city HPF center agreement (city anonymized). Working-paper
    materials describe the construction (2020 CES PPT, SSRN 3507515).
caveats: >-
  Identity refined this round: the asset is Housing Provident Fund
  (住房公积金) administrative data, NOT social security contribution records
  (the Layer-2b hypothesis). The published JHR 2024 version's data section
  is unread (le.uwpress.org 403); its sample window and exact fields may
  differ from the 2020 WP description.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: partial
  last_audited: '2026-08-15'

used_by:
- cite: 'Agarwal, Li, Qin, Wu & Yan (2024), The Impact of Fertility Relaxation on the Gender Wage Gap'
  doi: https://doi.org/10.3368/jhr.0122-12126r2
  journal: JHR
  year: 2024
  dataset_role: Employer-employee matched administrative data; new-hire salary gender gap around the 2013 One-Child relaxation
  evidence_type: working_paper_data_section
  evidence_url: https://cesi.econ.cuhk.edu.hk/wp-content/uploads/PPT_Keyang_Li.pdf
  data_note: >-
    Published abstract (Layer-2b) names "an employer-employee matched
    administrative data". Data identity recovered from the authors' 2020 CES
    presentation (Agarwal, Li, Qin & Wu): HPF contribution records, one
    unnamed major city, 2012-2014, 138.5M employee-month observations, 5.4M
    employees. Published-version data section unread (le.uwpress.org 403 on
    2026-08-15; same block recorded by grounding-b11). Authors confirmed via
    Semantic Scholar: Sumit Agarwal, Keyang Li, Yu Qin, Jing Wu, Jubo Yan.

provenance:
- source: https://cesi.econ.cuhk.edu.hk/wp-content/uploads/PPT_Keyang_Li.pdf
  field_scope:
  - data_identity
  - sample
  - variables
  - construction
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.semanticscholar.org/graph/v1/paper/DOI:10.3368/jhr.0122-12126r2
  field_scope:
  - authors
  - year
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.ablesci.com/assist/detail?id=J0Eyor
  field_scope:
  - metadata
  added: '2026-08-15'
  confidence: med
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-employer-employee-matched-admin, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets: []
---

## Positioning in one sentence

The JHR 2024 paper's "employer-employee matched administrative data" is Housing Provident Fund contribution microdata from one unnamed major Chinese city (2012-2014, 138.5M employee-month records in the WP version) - restricted city administrative data with no public route, documented here from the authors' own presentation because the journal full text is 403-gated.

## Select rules

- Use for gender wage-gap and fertility-policy labor-market questions that require employer-employee matched administrative records; expect restricted access.
- Do not confuse with social security contribution records (unverified hypothesis, corrected this round) or with survey-based matched data.
- For obtainable alternatives with city coverage, survey panels (cfps) or job-posting data (china-51job-vacancy-postings-2019) answer different margins.

## Get recipe

1. Read the working-paper materials for the data description: 2020 CES PPT (URL above) and SSRN WP 3507515.
2. If the research design needs the actual microdata, the route is author/city-HPF-center negotiation - no public route evidenced; the city is anonymized.
3. Verify the published JHR 2024 version's sample window and fields via a human browser/library before relying on WP-era details.

## Connections and Limitations

- WP-era evidence (2012-2014, one city) may not match the published version; the published data section is unread.
- The salary measure is HPF-deposit-based (12% x 2); it is not total compensation.
- Single-city coverage limits spatial variation; identification rests on gender and policy timing within employers.
