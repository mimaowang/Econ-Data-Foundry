---
schema_version: 3
catalog_status: ready
id: china-aer-quid-pro-quo-auto-replication-2025
name: 'Data and Code for: Quid Pro Quo, Knowledge Spillovers, and Industrial Quality Upgrading: Evidence from the Chinese Auto Industry (openICPSR 229381 V1)'
aka:
- openICPSR project 229381
- AER 2025 Quid Pro Quo Auto replication package
- Bai-Barwick-Cao-Li Chinese auto industry quality replication data
provider: >-
  American Economic Association (publisher; AEA Data and Code policy route);
  ICPSR/openICPSR (distributor of the replication deposit). Deposited by the
  authors Jie Bai, Panle Jia Barwick, Shengmao Cao and Shanjun Li. The paper's
  underlying data sources are third-party: J.D. Power (China Initial Quality
  Study IQS and APEAL surveys, 2001-2014), LinkedIn China (worker employment
  histories), MarkLines (Who Supplies Whom supplier database), China's SIPO/CNIPA
  (patent transfer records), auto firms' official websites (plant locations), and
  the China National Information Center (household vehicle-ownership survey
  2009-2014).
china_related: true
domains:
- firm
- international-trade-and-fdi
- technology
- industrial-organization
- development
- manufacturing

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: >-
    Replication package (data and code) for the AER 2025 paper, containing the
    authors' compiled Chinese automobile-industry analysis files: model-year
    vehicle quality measures from J.D. Power IQS/APEAL (2001-2014; nine IQS and
    ten APEAL standardized quality dimensions per model-year), ownership
    affiliation network (JV / affiliated SOE / non-affiliated domestic),
    worker-flow records from LinkedIn (52,898 users; 3,086 final job switches),
    supplier-network links from MarkLines (1,378 suppliers, 271 parts under 31
    categories, 459 models), SIPO patent transfers (2001-2018), and plant-city
    locations. The current public openICPSR tree verifies a Replication folder
    with code, data, output, and raw subfolders; its listed non-confidential
    files include Stata scripts and selected .dta files. That tree does not prove
    that every commercial source or every paper input is released.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The AEA article page lists a Replication Package linking to DOI
    10.3886/E229381V1 (openICPSR project 229381 V1). DataCite confirms the
    deposit: "Data and Code for: Quid Pro Quo, Knowledge Spillovers, and
    Industrial Quality Upgrading: Evidence from the Chinese Auto Industry",
    ICPSR 2025, creators Barwick/Cao/Li/Bai; OpenAlex classifies it as a dataset
    with green OA status and an ICPSR source. The paper's data section (NBER WP
    w27644 section 2.2, re-confirmed by the published Supplemental Appendix A.2)
    names the underlying sources. A current public openICPSR recheck now shows
    the package tree, six named Stata scripts, and several named non-confidential
    .dta files. Download actions redirect to the ICPSR login flow, so the route
    is concrete but its account cost and exact license terms remain unverified.
  barrier: >-
    Download actions redirect to the ICPSR login flow, while the public listing
    does not state account cost or an exact license. The raw commercial inputs
    (J.D. Power IQS/APEAL, MarkLines, LinkedIn) are NOT established as a standard
    public route; use the listed non-confidential replication materials rather
    than assuming the underlying commercial databases are released.

unit_of_observation: >-
  Main quality analysis: vehicle model x year, with quality measured across nine
  IQS dimensions / ten APEAL dimensions within each model-year (within-product
  variation is the exploited variation). Supporting layers: worker (LinkedIn job
  moves between 60 JVs/domestic firms), supplier-part-model links (MarkLines),
  patent-transfer pairs (SIPO), and model-plant-city assignments.
structure: >-
  Model-year panel of quality measures (2001-2014) plus cross-sectional network
  and worker-mobility files. The verified deposit tree separates code, data,
  output, and raw folders; deeper contents remain only partly enumerated.
geo_granularity:
- city (plant locations of models, mapped from firm websites)
- province (auto production correlation checks)
- national (China passenger-vehicle market)
geography: China's passenger-vehicle market (J.D. Power surveys recruit buyers in 50+ Chinese cities; models cover >90% of market share in sales)
time_span:
  start: '2001'
  end: '2018'
  last_confirmed_release: '2025'
  coverage_note: >-
    Core quality panel 2001-2014 (IQS launched 2001, APEAL 2003; both through
    2014). SIPO patent transfers 2001-2018; China National Information Center
    household survey 2009-2014; MarkLines supplier data mostly models produced
    after 2012 (pooled across years). Deposit registered 2025 per DataCite.
  last_checked: '2026-09-27'
frequency:
- annual (IQS/APEAL studies)
- cross-sectional (network files)
sample_size: >-
  18,884 survey respondents in 2014 (~110 per model); 52,898 LinkedIn users in
  60 JVs/domestic firms (3,086 final job switches, 617 JV-to-domestic); 1,378
  suppliers, 271 parts, 459 models (MarkLines); model-level quality panel for the
  major passenger-vehicle models
key_variables:
- IQS problems per 100 vehicles across nine quality dimensions (exterior, driving experience, feature/control/display, audio/entertainment/navigation, seats, HVAC, interior, engine and transmission; WP also lists a ninth category)
- APEAL satisfaction ratings across ten performance dimensions
- Ownership affiliation: JV model / affiliated domestic (SOE) / non-affiliated domestic
- Model-year identifiers and standardized dimension z-scores (per-question standardization, WP section 2.3)
- Plant city of each model
- Worker moves: firm and location before/after switch, occupation, education
- Supplier-part-model links
- Patent transfers between firms

research_fit:
  best_for:
  - Knowledge-spillover estimation from FDI/JV ownership affiliation in the Chinese automobile industry (quid pro quo policy)
  - Model-level quality upgrading analysis using within-product, across-dimension quality variation (IQS/APEAL)
  - Studies of worker flows or supplier networks as knowledge-transfer mechanisms in the auto sector
  choose_over:
  - Choose this over asif or china-firm-registry when the question needs product-level QUALITY measures and ownership-affiliation structure, which firm-financial panels do not contain.
  - Choose this over china-customs (trade transactions) - the paper does not use customs data at all; trade flows answer different questions.
  - The visible compiled package is the released route for this paper-specific model-year quality work; the raw J.D. Power studies remain a commercial product.
  not_good_for:
  - Firm financial performance, productivity, or employment regressions (no ASIF-style financial variables)
  - Trade/export analysis (no customs data in this package)
  - Quality dynamics after 2014 or current market analysis
  - Treating the package as the raw J.D. Power or MarkLines databases (the package is the paper's compiled extract; raw sources are commercial)
  - Supplier "census" claims - the paper itself notes MarkLines is not a complete census of suppliers
  needs_join_for:
  - Firm financials or productivity: asif (firm-level) - matching is model/firm-name based and unverified
  - Trade outcomes: china-customs
  - Broader patent analysis: china-patents (SIPO layer is one input here)
  - Regional controls: city/province statistics (plant-city layer)
  variation_available:
  - Within-product variation across quality dimensions (exploited for identification)
  - Ownership affiliation network (JV vs affiliated vs non-affiliated domestic)
  - Partial overlap between ownership and geographic (plant-city) networks
  - Identification-design details belong to the Econ-Variation repository; this record only notes which variation exists in the data.
  topics:
  - FDI spillovers
  - knowledge transfer
  - joint ventures
  - automobile industry
  - product quality
  - worker mobility
  - supplier networks

good_for:
- JV knowledge-spillover and quality-upgrading studies in the Chinese auto industry
- Replication and extension of Bai, Barwick, Cao & Li (2025 AER)
identification:
- The released package can support replication of the documented model-year quality analysis, but its files alone do not establish a causal interpretation or release the underlying commercial source databases.
linkable_keys:
- Model name and model-year (quality panel)
- Automaker/firm name (ownership group; JV partners)
- Plant city
- Worker-level records in the LinkedIn layer (anonymized form unknown)
- Part and model identifiers in the MarkLines layer

joins:
- target: asif
  relation: complement
  keys:
  - Firm name (ownership groups) - exact identifiers in the deposit unverified
  method: Firm-level financials joined to model-level quality requires name normalization across different units (firm vs model); the deposit's identifier set is unverified.
  evidence_status: plausible
- target: china-customs
  relation: complement
  keys:
  - Firm name - unverified
  method: The paper does not use customs data; a trade-outcome extension would need its own firm-level matching.
  evidence_status: plausible
- target: china-patents
  relation: complement
  keys:
  - Firm name - unverified
  method: The paper's SIPO patent-transfer layer (2001-2018) overlaps china-patents coverage; package files unverified.
  evidence_status: plausible

access_routes:
- route: openICPSR replication deposit (AEA Data and Code policy)
  access_status: available-with-login
  direct_url: https://doi.org/10.3886/E229381V1
  requirements:
  - ICPSR login is required by the current download flow; account cost and deposit-specific terms were not displayed in the public listing.
  steps:
  - Open the AER article page (https://www.aeaweb.org/articles?id=10.1257/aer.20221501) and follow Additional Materials > Replication Package (https://doi.org/10.3886/E229381V1).
  - Or go directly to https://www.openicpsr.org/openicpsr/project/229381/version/V1/view.
  - Before downloading, inspect the public tree: Replication/code, data, output, and raw. The listed code files are P1_clean_data_main.do, P2_table_figure_main.do, P3_clean_data_appendix.do, P4_table_figure_appendix.do, master.do, and setup.do.
  - Download after login, then read README.pdf and preserve the package structure before running any scripts.
  deliverable: A login-mediated replication package with a public tree showing code, data, output, and raw folders. The non-confidential data listing includes data_JV_founding_year.dta, data_basemap.dta, data_map.dta, survey_results.dta, JV_rand.dta, crosswalk_JD_modelid.dta, and crosswalk_attributes_modelid.dta; other nested contents were not enumerated.
  cost: registration
  last_checked: '2026-09-27'
  caveat: The current public tree verifies package structure and selected file names, but not the full nested manifest, deposit-specific license, or the inclusion of raw J.D. Power, MarkLines, or LinkedIn source databases.
- route: AEA article page and supplemental appendix
  access_status: available
  direct_url: https://www.aeaweb.org/articles?id=10.1257/aer.20221501
  requirements: None for the abstract/materials pages; the full-text PDF is subscription-only (pubs.aeaweb.org 403 for automated clients)
  steps:
  - Read the abstract; download the Supplemental Appendix (public PDF, cached this round) for data summaries (section A.2) and additional analyses.
  deliverable: Article metadata, abstract, supplemental appendix PDF; NOT the replication data.
  cost: free
  last_checked: '2026-08-15'
  caveat: The published full text itself was not read (subscription wall); paper-use evidence comes from the NBER WP full text and the published Supplemental Appendix.
- route: NBER working paper w27644 (2020 preprint)
  access_status: available
  direct_url: https://www.nber.org/papers/w27644
  requirements: None
  steps:
  - Download the WP PDF (cached this round, full text read): section 2.2 documents the datasets.
  deliverable: Working-paper text (design and data documentation); NOT the data.
  cost: free
  last_checked: '2026-08-15'
  caveat: 2020 preprint; the published version (AER Nov 2025) may differ in details; the Supplemental Appendix is the published-side confirmation.

access:
  url: https://doi.org/10.3886/E229381V1
  cost: registration
  license: ICPSR deposit terms; the current public listing did not display the exact license text.
  format:
  - Stata .do scripts
  - selected non-confidential Stata .dta files
  - README.pdf
  api: false
  how_to_get: From the AER article page follow the Replication Package link to openICPSR project 229381 V1. Inspect the public tree, then use the current ICPSR login-mediated download flow, read README.pdf, and retain the tree before reuse.

caveats:
- The public openICPSR tree can now be read, but clicking Download redirects to ICPSR login. Its account cost, exact license, and the full nested manifest remain unverified.
- The package is the paper's COMPILED analysis data; the raw J.D. Power IQS/APEAL studies, MarkLines database, and LinkedIn data are commercial/third-party and not a standard public route.
- Main analysis period 2001-2014; do not use for post-2014 quality dynamics.
- The WP (2020) predates the published version (AER 115(11), November 2025, pp. 3825-52). Task-brief year label "AER 2024" is corrected to 2025 by Crossref/AEA official metadata.

production:
  raw_sources:
  - name: J.D. Power China Initial Quality Study (IQS) and APEAL surveys
    source_type: dataset
    role: Main outcome - model-year vehicle quality measures (nine IQS dimensions, ten APEAL dimensions)
    access_route: Commercial survey product; authors obtained it for 2001-2014; not public
    url: needs-verification
    coverage: Annual surveys April-June; buyers in 50+ Chinese cities; >90% of market share models; 18,884 respondents in 2014
    last_checked: '2026-08-15'
  - name: LinkedIn (China) employment histories
    source_type: dataset
    role: Worker-flow mechanism (52,898 users in 60 JVs/domestic firms; 3,086 final job switches)
    access_route: Platform data collected by the authors; not public
    url: needs-verification
    coverage: Auto-industry employees registered on LinkedIn, collected through the paper's sample period
    last_checked: '2026-08-15'
  - name: MarkLines Who Supplies Whom
    source_type: dataset
    role: Auto parts supplier network (1,378 suppliers, 271 parts, 459 models)
    access_route: Commercial supplier database; not public
    url: needs-verification
    coverage: Collected from 2008; most supplier info for models produced after 2012; pooled across years
    last_checked: '2026-08-15'
  - name: SIPO/CNIPA patent transfer records
    source_type: dataset
    role: Direct technology transfers between firms (2001-2018)
    access_route: Official records; see china-patents for the general patent-data route
    url: needs-verification
    coverage: Universe of patent transfers between firms 2001-2018
    last_checked: '2026-08-15'
  - name: Auto firms' official websites (plant locations)
    source_type: webpage
    role: Model-to-plant-city mapping
    access_route: Public websites
    url: needs-verification
    coverage: Plants of the sample automakers (Table E.2 / Figure E.4 of the paper)
    last_checked: '2026-08-15'
  - name: China National Information Center household vehicle-ownership survey
    source_type: dataset
    role: Consumer preference correlation check (vehicle purchased and alternatives considered)
    access_route: Annual nationally representative household survey 2009-2014; access unverified
    url: needs-verification
    coverage: 2009-2014 national household survey
    last_checked: '2026-08-15'
  acquisition_methods:
  - purchase/licensing (J.D. Power, MarkLines)
  - platform data collection (LinkedIn)
  - official records (SIPO patent transfers)
  - manual compilation (plant locations from firm websites)
  - survey data (China National Information Center)
  sample_construction: >-
    Per the WP (section 2.1-2.2): the sample is the major passenger-vehicle models
    in China (IQS/APEAL cover >90% of sales market share); models classified by
    ownership affiliation (JV / affiliated SOE / non-affiliated domestic); worker
    moves kept where location data complete (3,086 of 4,099 movers); supplier
    network pooled across all years due to sparse annual data. The deposit's own
    sample files are unverified.
  pipeline_stages:
  - stage: collect
    inputs:
    - J.D. Power IQS/APEAL
    - LinkedIn histories
    - MarkLines
    - SIPO records
    - Firm websites
    - CNIC survey
    method: Multi-source compilation documented in WP section 2.2 and Supplemental Appendix A.2
    output: Model-year quality panel plus network/worker-mobility files
    evidence: WP section 2.2; published Supplemental Appendix A.2
  - stage: clean
    inputs:
    - Raw IQS/APEAL responses
    method: Per-question standardization, then aggregation to nine IQS / ten APEAL dimension z-scores
    output: Standardized dimension-level quality measures
    evidence: WP section 2.3 (standardization described; details in the paper)
  - stage: match
    inputs:
    - Ownership network
    - Plant-city locations
    method: Ownership affiliation assignment from JV structure; plant locations from firm websites
    output: Affiliation and location layers
    evidence: WP section 2.1-2.2
  constructed_variables:
  - name: IQS/APEAL dimension z-scores
    concept: Standardized quality measures per model-year within each quality dimension
    source_fields:
    - IQS question-level responses
    - APEAL question-level responses
    method: Standardize each question using all model-year observations; aggregate to dimensions
    validation: Price-quality correlation checks (WP Figure 2)
    limitations: Consumer-perception component in APEAL; IQS is the more objective measure (WP footnote)
  - name: Ownership affiliation type
    concept: JV model vs affiliated domestic (SOE) vs non-affiliated domestic
    source_fields:
    - JV structure and brand ownership
    method: Assignment from the industry ownership network (WP section 2.1)
    validation: Paper Table 1 summary statistics
    limitations: All affiliated domestic automakers are SOEs in the sample period
  validation:
  - Price-quality correlations (WP Figure 2)
  - LinkedIn geographic distribution vs provincial auto production correlation 0.89 (WP section 2.2)
  output:
    unit_of_observation: Vehicle model x year (quality panel); worker moves; supplier links
    structure: Model-year panel + network files
    geography: China (plant cities)
    time_span: 2001-2014 core; SIPO layer to 2018
    key_variables:
    - IQS/APEAL dimension scores
    - Ownership affiliation
    - Plant city
    - Worker moves
    - Supplier links
    - Patent transfers
    formats:
    - Stata .do scripts and selected non-confidential Stata .dta files verified in the public tree; other nested formats unverified
  reproducibility:
    level: medium
    starting_point: https://doi.org/10.3886/E229381V1
    code_available: true
    code_url: https://doi.org/10.3886/E229381V1
    requirements:
    - ICPSR login-mediated openICPSR download
    - Stata (six public code files use .do format)
    - Read README.pdf and inspect any unenumerated nested directories before execution
    blockers:
    - Exact account cost and deposit-specific license are unverified
    - Full nested manifest and file contents are not yet enumerated
    - Raw commercial inputs (J.D. Power, MarkLines, LinkedIn) not public
  compliance:
    terms_or_license: ICPSR deposit terms (unverified); J.D. Power/MarkLines data use subject to their own commercial licenses
    robots_or_rate_limits: Public file-tree browsing is available; downloads route through ICPSR login. Do not automate authenticated retrieval without authorization.
    personal_or_sensitive_data: Worker records may be identifying; follow deposit terms
    redistribution: Redistribute only as the deposit license permits; never redistribute raw commercial inputs
    review_needed: true

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

used_by:
- cite: 'Bai, Jie; Barwick, Panle Jia; Cao, Shengmao; Li, Shanjun (2025), Quid Pro Quo, Knowledge Spillovers, and Industrial Quality Upgrading: Evidence from the Chinese Auto Industry, American Economic Review 115(11): 3825-52'
  doi: https://doi.org/10.1257/aer.20221501
  journal: American Economic Review
  year: 2025
  dataset_role: Main dataset (vehicle model-year quality panel and ownership network; worker-flow and supplier-network mechanism layers) for the knowledge-spillover analysis
  evidence_type: data-section
  evidence_url: https://www.nber.org/papers/w27644
  data_note: >-
    NBER WP w27644 section 2.2 (read in full, cached) documents the datasets:
    J.D. Power IQS (2001-2014) and APEAL quality measures; LinkedIn China worker
    histories (52,898 users; 3,086 final switches); MarkLines Who Supplies Whom
    supplier network (1,378 suppliers / 271 parts / 459 models); plant locations
    from firm websites; SIPO patent transfers 2001-2018; China National
    Information Center household survey 2009-2014. The published Supplemental
    Appendix A.2 (cached) re-confirms the LinkedIn and MarkLines descriptions.
    The AER article page (cached) links the Replication Package to
    https://doi.org/10.3886/E229381V1. Published as AER 115(11), November 2025
    (Crossref).

provenance:
- source: NBER WP w27644 full text (cached nber_qpq_w27644.txt), sections 2.1-2.3
  field_scope:
  - datasets used and their coverage (quality, worker flow, supplier network, plant locations, patents, household survey)
  - unit of observation (model-year; within-model quality dimensions)
  - sample construction and validation
  - ownership network structure
  added: '2026-08-15'
  confidence: high
  verified: true
- source: AEA article page (cached aea_qpq_article.html) for 10.1257/aer.20221501
  field_scope:
  - publication identity (AER 115(11), November 2025, pp. 3825-52)
  - Replication Package link to https://doi.org/10.3886/E229381V1
  - abstract (Chinese auto industry, 2001-2014 quality upgrading, 8.3% contribution)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Published Supplemental Appendix PDF (cached aea_qpq_supp.pdf.txt), section A.2
  field_scope:
  - published-side confirmation of LinkedIn and MarkLines data descriptions
  added: '2026-08-15'
  confidence: high
  verified: true
- source: DataCite records 10.3886/E229381V1 and 10.3886/e229381 (parent)
  field_scope:
  - deposit existence, title ("Data and Code for: ..."), publisher (ICPSR), year (2025), creators
  - does NOT prove file contents, license, or downloadability for automated clients
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Current openICPSR project 229381 V1 public file tree https://www.openicpsr.org/openicpsr/project/229381/version/V1/view
  field_scope:
  - current public project identity, China coverage, and 2001-2014 period
  - Replication/code, data, output, and raw folder structure
  - six named Stata code files and selected named non-confidential .dta files
  - current login-mediated download boundary
  added: '2026-09-27'
  confidence: high
  verified: true
- source: OpenAlex work for DOI 10.3886/E229381V1
  field_scope:
  - deposit classified as dataset; green OA status; ICPSR Data Holdings source
  added: '2026-08-15'
  confidence: med
  verified: true
- source: Crossref record for 10.1257/aer.20221501
  field_scope:
  - publication date 2025-11-01, volume 115, issue 11
  added: '2026-08-15'
  confidence: high
  verified: true
related_datasets:
- id: asif
  relation: often-confused-with
- id: china-customs
  relation: complement
- id: china-patents
  relation: complement
---

## Positioning in one sentence

A paper-specific replication asset: the compiled Chinese auto-industry model-year quality data (J.D. Power IQS/APEAL 2001-2014) plus ownership, worker-flow, supplier-network, and patent-transfer layers for the AER 2025 quid-pro-quo spillover study. Its openICPSR 229381 V1 tree publicly shows Stata code and selected non-confidential data files; download currently requires ICPSR login, while commercial source-database availability and exact license terms remain separate questions.

## Select rules

- Prioritize it when the question needs product-level QUALITY measures with within-model quality-dimension variation and ownership-affiliation structure for the Chinese auto industry - the only released form of this model-year quality panel.
- Switch to asif for firm financial performance, productivity, or employment questions (no quality measures there); do not expect customs/trade variables here at all (the paper never uses china-customs).
- It cannot support post-2014 quality dynamics, supplier-census claims, or any use of the raw J.D. Power/MarkLines databases; the package is the authors' compiled extract.

## Get recipe

1. Read the NBER WP w27644 (free PDF) section 2 to understand the datasets and construction before touching the deposit.
2. Open the AER article page and follow Additional Materials > Replication Package to https://doi.org/10.3886/E229381V1 (openICPSR project 229381 V1). Confirm the public Replication tree: code, data, output, and raw.
3. Use the ICPSR login-mediated download flow, then read README.pdf. The visible code directory contains six Stata scripts; the visible non-confidential directories contain selected .dta files, but inspect all nested folders and terms before relying on them.
4. Run the deposit code against the released files before any extension; do not treat the working-paper text as the data, and do not expect raw commercial inputs inside the package.

## Connections and Limitations

The quality panel is model-year level with dimensions within each model. Joins to asif or china-customs are firm-name based and remain unverified; the visible crosswalk filenames are not proof that their identifiers match those external datasets. The package is ready for a researcher to locate, obtain after login, and inspect, but it does not establish that all underlying commercial inputs or every paper layer is downloadable. Before extension, confirm the exact license, full nested manifest, and whether the SIPO patent-transfer layer is a usable file or only summarized.
