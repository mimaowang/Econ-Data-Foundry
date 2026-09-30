---
schema_version: 3
catalog_status: ready
id: china-court-judgments-2014-2018-open-justice
name: China civil judgment corpus 2014-2018 (6.42M judgments) with court live-broadcast records (Chen, Chen & Yang, ReStud 2026)
aka:
- China Judgments Online (CJO) civil judgment corpus 2014-2018
- 中国裁判文书网民事判决语料（2014-2018）
- China Court Trial Online live-broadcast records
- 中国庭审公开网直播记录
provider: China Judgments Online (中国裁判文书网, wenshu.court.gov.cn) as the document source; China Court Trial Online (中国庭审公开网) for broadcast records; the paper's extract was obtained with assistance from an unnamed commercial data company
china_related: true
domains:
- judicial
- institutions
- gender
- law-and-economics
- governance

data_pathway:
  mode: hybrid
  origin: researcher-collected
  target_artifact: >-
    A case-level dataset built from roughly 6.42 million Chinese civil judgments
    (January 2014 - December 2018), restricted to civil litigation with individual
    litigants, plus matched live-broadcast indicators from China Court Trial Online.
    The current Zenodo replication record (10.5281/zenodo.15729271, CC-BY-4.0)
    publicly lists a readme PDF and a replication-package ZIP. Its inner manifest
    has not yet been inspected, so neither the code layout nor inclusion of the
    original full judgment-text corpus is asserted here.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The paper's full text (data construction section) states that the authors
    obtained legal documents published on China Judgments Online with assistance
    from a commercial data company, covering January 2014 to December 2018
    (6,424,324 civil judgments in the full sample; 4,601,718 with litigant gender
    in the main sample), and matched them to all 11,016,416 live-broadcast records
    available on China Court Trial Online as of April 2021. A Zenodo replication
    package exists under CC-BY-4.0. An ordinary researcher can therefore start from
    the official CJO website (registration-based, access confirmed for the homepage
    on 2026-08-15) and the Zenodo package, but reproducing the exact 6.42M-judgment
    corpus requires dealing with CJO's current search/download limits or a
    commercial-data route; the paper's exact corpus is not confirmed as a single
    public file.
  barrier: >-
    The paper does not name the commercial data company, disclose the CJO access
    agreement, or state whether the 2020 corpus vintage remains downloadable.
    CJO's current registration, verification, and download limits for bulk
    retrieval are not formally documented in this record. Zenodo establishes a
    public paper-specific replication package, but its ZIP interior has not been
    inspected, so it is unknown whether it includes derived analysis files, any
    judgment text, or only reproduction scripts and supporting materials.

unit_of_observation: One civil judgment document (case-level); broadcast matching is at judgment-to-broadcast level
structure: Repeated cross-section of judgment documents with case attributes; broadcast intensity aggregated to court-area x year-quarter
geo_granularity:
- court / court area (地区, sub-provincial court geography)
- prefecture (via China City Statistical Yearbook controls)
geography: All courts of China, restricted to civil cases with individual litigants; 3,517 courts connected to the broadcast platform by December 2017 (per the paper)
time_span:
  start: '2014-01'
  end: '2018-12'
  last_confirmed_release: '2025-07-28'
  coverage_note: >-
    Judgments were acquired in 2020 and are stated to closely approximate the
    complete set of cases up to 2018; broadcast records cover the platform up to
    April 2021 (11,016,416 cases). The paper is published in ReStud (online 28
    July 2025 per the ReStud page).
  last_checked: '2026-08-15'
frequency:
- case-level (each judgment is one record)
sample_size: 6,424,324 civil judgments (full sample); 4,601,718 with litigant gender (main sample); 11,016,416 broadcast records matched (as of April 2021)
key_variables:
- Judgment text (basic info, claims, facts, legal principles, outcomes sections)
- Case number (案号), instance (first/second), court, area, dates of trial and publication
- Litigant characteristics: names, gender (72% of judgments include gender), birth date, ethnicity, address, appearance; number of plaintiffs/defendants
- Lawyer names and affiliations, numbers of lawyers per side
- Judge name (from signature; gender inferred via Ngender algorithm, 92% validated accuracy)
- Litigation outcome: plaintiff win rate constructed from the share of legal costs borne by the defendant
- Case type: 50 types from an unsupervised topic model over the ~6M cases
- Broadcast intensity: ratio of broadcast cases to total cases at court-area x year-quarter (constructed from China Court Trial Online records)
- Region-level controls from China City Statistical Yearbook: prefecture GDP per capita, population, internet penetration

research_fit:
  best_for:
  - Studying gender disparities in Chinese civil litigation outcomes and their response to judicial transparency
  - Court-level DiD or Bartik-IV designs exploiting the staggered rollout of live trial broadcasting across courts (2016-2017)
  - Textual analysis of Chinese judicial decisions (structure is semi-fixed; sections are extractable)
  - Research on the open-justice reform (four disclosure platforms) and judge behavior under transparency
  choose_over:
  - Choose this corpus over pkulaw (regulation/document database) when the need is bulk civil judgment texts at case level for empirical analysis.
  - Choose this over hand-collected court-case candidates (china-sez-legal-cases-crime-2026, china-land-dispute-files-2027) when a large, systematic corpus with broadcast exposure is required; those candidates cover narrower case sets.
  - For pre-2014 or post-2018 judgment coverage, the corpus does not help: use CJO directly with a new sample definition.
  not_good_for:
  - Criminal, administrative, or enforcement documents (the paper's corpus is civil judgments only)
  - Official statistics on court workloads or case flows (use court yearbooks or judicial white papers instead)
  - A guaranteed complete post-2018 universe: CJO publication of new judgments declined after 2018; the paper's corpus stops at December 2018
  - Judge-level causal claims without the broadcast-exposure design: judge gender is inferred, not disclosed
  needs_join_for:
  - Court/prefecture economic controls (the paper uses China City Statistical Yearbook: GDP per capita, population, internet penetration)
  - Pre-2016 litigation outcomes or case characteristics from other sources if a longer baseline is needed
  - Individual judge career or evaluation data (e.g., Merit Judge lists) for gender validation or judge-fixed-effect designs
  variation_available:
  - Court-by-time staggered adoption of live broadcasting (courts connected September 2016 - December 2017; 383 courts by September 2016)
  - Broadcast intensity differences across courts and over time (court-area x year-quarter)
  - These are data-side variation dimensions; the treatment/identification design itself belongs to the Econ-Variation repository.
  topics:
  - judicial transparency
  - gender disparities
  - courts
  - open justice
  - judgment documents
  - live broadcasting

good_for:
- Court-level panel analyses of judicial outcomes with broadcast-intensity exposure
- Large-scale text analysis of Chinese civil judgments (structured five-section documents)
- Gender economics in litigation (plaintiff/defendant/judge gender)
identification:
- This is a paper-specific judgment, broadcast, and code package, not a stand-alone causal-variation record. It supports obtaining and inspecting the public replication artifact; any new identification claim requires its own design assessment.
linkable_keys:
- Case number (案号), used by the paper to merge judgments with broadcast records and other datasets
- Court identity (name and court) for judge identification
- Area (地区) and court-area
- Prefecture (via city statistical yearbook merge)
- Trial/publication dates

joins:
- target: pkulaw
  relation: often-confused-with
  keys:
  - Case number or court where retained
  method: pkulaw is a legal-document database; it is a discovery/reference route, not the bulk corpus the paper built.
  evidence_status: plausible
# Note: the paper merges prefecture-level controls (GDP per capita, population,
# internet penetration) from the China City Statistical Yearbook; the repository
# has no separate city-yearbook record, so no join target is declared here.

access_routes:
- route: Zenodo replication package (ReStud)
  access_status: available
  direct_url: https://zenodo.org/doi/10.5281/zenodo.15729271
  requirements:
  - No account or fee; CC-BY-4.0 license
  steps:
  - Open the current verified Zenodo record 10.5281/zenodo.15729271.
  - Download its two publicly listed files, readme.pdf and replication_package.zip.
  - Inspect the ZIP manifest before relying on any code, derived data, or raw-text availability; that internal inventory has not been verified yet.
  deliverable: A public 432.2MB replication_package.zip and readme.pdf. Zenodo describes a README, four sub-folders for paper figures/tables, run_all.do, and optional Stata environment configuration; the ZIP's complete interior and whether it contains any raw judgment corpus remain unverified.
  cost: free
  last_checked: '2026-09-28'
  caveat: The formerly cited record 10.5281/zenodo.15729270 now returns deleted. Current record 10.5281/zenodo.15729271 is open under CC-BY-4.0 and describes the replication layout, but it does not expose the ZIP's complete interior or establish that the original 6.42M full-text corpus is included.
- route: China Judgments Online (wenshu.court.gov.cn) official site
  access_status: available-with-conditions
  direct_url: https://wenshu.court.gov.cn/
  requirements:
  - Registration and login (the page contains a login component; verified reachable 2026-08-15)
  - Current site verification and download limits; bulk retrieval historically restricted
  steps:
  - Register an account and log in on wenshu.court.gov.cn.
  - Search civil judgments by court, case type, and period; download within current per-session limits.
  - For corpus-scale acquisition, assess compliance with current terms; the paper itself used a commercial data company for its 2020 extract.
  deliverable: Searchable judgment documents (text and metadata) within current site limits; not a one-shot 6.42M bulk download.
  cost: free
  last_checked: '2026-08-15'
  caveat: Homepage reachability was confirmed on 2026-08-15; the current registration, verification, and download-limit rules were not formally captured this round.
- route: China Court Trial Online (tingshen.court.gov.cn)
  access_status: available-with-conditions
  direct_url: http://tingshen.court.gov.cn/
  requirements:
  - Registration/login; browsing of live and archived trial broadcasts
  steps:
  - Access the platform to browse broadcast records; matching to judgment case numbers requires the case-level key.
  deliverable: Trial-broadcast records (live and archived); the paper used all 11,016,416 records as of April 2021.
  cost: free
  last_checked: '2026-08-15'
  caveat: Platform reachability confirmed 2026-08-15; bulk extraction terms were not captured this round.
- route: Supreme People's Court judicial big-data research service (司法大数据服务)
  access_status: needs-verification
  direct_url: http://data.court.gov.cn/pages/research.html
  requirements:
  - Application-based research access; terms unverified
  steps:
  - Review the research-service page for current application procedures for researcher access to judgment data.
  deliverable: Unknown until the application process is verified.
  cost: by-application
  last_checked: '2026-08-15'
  caveat: The link appears on the CJO homepage (2026-08-15 capture) as a research-data service; this record has not verified its application terms.

access:
  url: https://wenshu.court.gov.cn/
  cost: free
  license: Site terms apply; the replication package is CC-BY-4.0
  format:
  - judgment text (Chinese)
  - replication code (Stata .do files)
  api: false
  how_to_get: Start with the Zenodo replication package for the paper's tables/figures; for the underlying corpus, register on wenshu.court.gov.cn and work within current retrieval limits, or use an authorized commercial/data-service channel for a bulk extract.

caveats:
- The 6.42M figure is the paper's full sample of civil judgments with individual litigants, 2014-2018, acquired in 2020 via an unnamed commercial data company; it is not a claim about CJO's current holdings.
- The current Zenodo record lists only readme.pdf and replication_package.zip at top level. Its internal contents, including any code, derived files, or raw 6.42M judgment texts, remain unverified.
- CJO's current bulk-download rules, verification flow, and any fee structure were not formally captured; the homepage was reachable on 2026-08-15.
- The paper's broadcast matching uses all 11,016,416 China Court Trial Online records as of April 2021; today's platform holdings and matching feasibility are unverified.
- Judge gender is inferred via Ngender (92% accuracy on a ~2,000-judge validation list), not disclosed in documents.
- After 2018, CJO publication volume changed substantially; do not extend the corpus claim to later years.

production:
  raw_sources:
  - name: China Judgments Online (中国裁判文书网)
    source_type: webpage
    role: Source of the civil judgment documents (text plus basic-info fields)
    access_route: "Commercial data company assistance (per the paper); today: registered site access"
    url: https://wenshu.court.gov.cn/
    coverage: Launched July 2013; over 120 million documents by December 2021 (paper footnote); the paper's extract covers civil judgments January 2014 - December 2018
    last_checked: '2026-08-15'
  - name: China Court Trial Online (中国庭审公开网)
    source_type: webpage
    role: Live-broadcast records matched to judgments
    access_route: The paper obtained all broadcast records as of April 2021
    url: http://tingshen.court.gov.cn/
    coverage: Officially launched September 2016; 11,016,416 cases broadcast as of April 2021; over 16 million by end-2021 (paper text)
    last_checked: '2026-08-15'
  - name: China City Statistical Yearbook
    source_type: dataset
    role: Prefecture-level controls (GDP per capita, population, internet penetration)
    access_route: Public statistical yearbook
    url: needs-verification
    coverage: Prefecture-year controls for the study period
    last_checked: '2026-08-15'
  acquisition_methods:
  - commercial-data-company delivery (paper's own route, unnamed company)
  - official-site registered retrieval (today's route for individual researchers)
  sample_construction: >-
    The paper restricts the CJO corpus to civil litigations with individual
    litigants (not institutions or companies), January 2014 - December 2018;
    documents were acquired in 2020 and are stated to closely approximate the
    complete set up to 2018. The main sample drops judgments missing litigant
    gender (full 6,424,324 -> main 4,601,718; 72% of judgments include genders).
    Broadcast records (11,016,416 as of April 2021) are matched to judgments by
    case number.
  pipeline_stages:
  - stage: collect
    inputs:
    - CJO civil judgments 2014-2018 (acquired 2020)
    - China Court Trial Online broadcast records (as of April 2021)
    method: Acquisition via commercial data company assistance (paper section 3.1); broadcast records fully obtained and matched
    output: 6,424,324 civil judgment documents plus matched broadcast indicators
    evidence: Paper data construction section (3.1)
  - stage: parse
    inputs:
    - Judgment documents
    method: Extract variables from the semi-fixed five-section structure (basic info, claims, facts, legal principles, outcomes)
    output: Case-level structured variables (case number, instance, litigants, lawyers, judge, area, outcome)
    evidence: Paper section 3.2-3.3
  - stage: classify
    inputs:
    - All ~6M cases
    method: Unsupervised topic model assigns 50 case types based on the combination of laws applied
    output: Case-type control variable
    evidence: Paper section 3.3
  - stage: match
    inputs:
    - Judgment case numbers
    - Broadcast records
    method: Match broadcast records to judgments; construct broadcast intensity (broadcast cases / total cases) at court-area x year-quarter
    output: Court-area x year-quarter broadcast intensity
    evidence: Paper section 3.3
  constructed_variables:
  - name: Plaintiff win rate
    concept: Extent to which the court supports the plaintiff, inversely proportional to the share of legal costs the plaintiff pays
    source_fields:
    - Outcome section of judgment (cost allocation)
    method: Share of legal costs borne by the defendant
    validation: Consistent with civil procedure law cost-allocation rule (paper section 3.3)
    limitations: Defined for civil cases with cost allocation; special-procedure cases may differ
  - name: Judge gender
    concept: Judge gender used for judge-level analysis
    source_fields:
    - Judge name and court
    method: Ngender algorithm inference; validated at 92% accuracy against ~2,000 judges from Supreme Court Merit Judge lists (2000-2020)
    validation: Paper footnote 9
    limitations: Inferred, not disclosed; accuracy 92%
  - name: Broadcast intensity
    concept: Ratio of broadcast cases to total cases at a given aggregate level
    source_fields:
    - Broadcast records
    - Judgment sample
    method: Default level is court-area x year-quarter
    validation: Paper section 3.3
    limitations: Depends on broadcast-record matching completeness
  validation: []
  output:
    unit_of_observation: Civil judgment (case-level)
    structure: Repeated cross-section of judgment records with case, litigant, lawyer, judge, outcome, and broadcast variables
    geography: Court areas nationwide (civil cases with individual litigants)
    time_span: 2014-01 to 2018-12 (judgments); broadcast records to 2021-04
    key_variables:
    - Case number, instance, court, area, dates
    - Litigant gender and counts, appearance
    - Lawyer counts
    - Judge name and inferred gender
    - Case type (50 classes)
    - Plaintiff win rate (cost-share based)
    - Broadcast intensity (court-area x year-quarter)
    formats:
    - judgment text
    - structured case-level table
  reproducibility:
    level: medium
    starting_point: https://zenodo.org/doi/10.5281/zenodo.15729271
    code_available: needs-verification
    code_url: https://zenodo.org/doi/10.5281/zenodo.15729271
    requirements:
    - Zenodo readme.pdf and replication_package.zip (inspect internal manifest before selecting software or commands)
    - Access to CJO for any needed raw judgment texts not contained in the package
    - Compliance with CJO retrieval limits for bulk collection
    blockers:
    - Unverified whether the package contains code, derived files, or the raw 6.42M judgment corpus
    - CJO current bulk-retrieval terms unverified
    - The paper's commercial data company is unnamed; the 2020 corpus vintage has no public mirror
  compliance:
    terms_or_license: Replication package CC-BY-4.0; CJO site terms apply to direct retrieval
    robots_or_rate_limits: CJO has historically enforced login, verification, and download limits; bulk crawling without authorization is not a documented route
    personal_or_sensitive_data: Judgments contain litigant personal information (names, addresses, birth dates) as published by courts; reuse must respect current publication and privacy rules
    redistribution: Do not redistribute the corpus or derived personal fields beyond the terms of the source and package licenses
    review_needed: true

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Chen, Heng; Chen, Yuyu; Yang, Qingxu (2026), Women in the Courtroom: Technology and Justice, Review of Economic Studies'
  doi: https://doi.org/10.1093/restud/rdaf066
  journal: Review of Economic Studies
  year: 2026
  dataset_role: Main dataset for gender-disparity and live-broadcast DiD/Bartik-IV analyses plus judgment-text analysis
  evidence_type: data-section
  evidence_url: https://www.restud.com/women-in-the-courtroom-technology-and-justice/
  data_note: >-
    Paper section 3.1: documents obtained from China Judgments Online with
    assistance from a commercial data company; 2014-2018 civil judgments,
    full sample 6,424,324, main sample 4,601,718 (with litigant gender);
    broadcast records from China Court Trial Online (11,016,416 as of April 2021)
    fully obtained and matched. Section 3.3 describes variable construction
    including plaintiff win rate from legal-cost shares, Ngender-inferred judge
    gender (92% validation accuracy), 50-case-type topic model, and broadcast
    intensity at court-area x year-quarter. The current public replication route
    is Zenodo 10.5281/zenodo.15729271 (CC-BY-4.0); its ZIP contents remain to be
    inspected.

provenance:
- source: Paper full text (ReStud submission PDF, cached court_resub_pdf.txt), data construction sections 3.1-3.4 and footnotes
  field_scope:
  - judgment source (CJO via commercial data company)
  - sample construction, years, counts (6,424,324 / 4,601,718)
  - broadcast data source and counts (11,016,416)
  - variable construction (outcome, gender inference, case types, broadcast intensity)
  - CJO platform history footnote (launched July 2013; 120M+ documents by Dec 2021)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Previously cited Zenodo record API 10.5281/zenodo.15729270
  field_scope:
  - obsolete route check: API returned deleted on 2026-09-27
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Zenodo record API 10.5281/zenodo.15729271 (current replication package metadata)
  field_scope:
  - current public replication route, creator, year (2025), and CC-BY-4.0 license
  - top-level public filenames (readme.pdf and replication_package.zip), not the ZIP's internal manifest
  added: '2026-09-27'
  confidence: high
  verified: true
- source: Zenodo record API 10.5281/zenodo.15729271 (queried 2026-09-28)
  field_scope:
  - open access and CC-BY-4.0 status
  - current 432.2MB ZIP and readme file inventory
  - Zenodo-described README, four replication sub-folders, run_all.do, and optional Stata configuration
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Live captures of wenshu.court.gov.cn and tingshen.court.gov.cn (2026-08-15), plus ReStud article page
  field_scope:
  - official site reachability and login component presence
  - research-data service link (data.court.gov.cn/pages/research.html)
  - publication date (online 28 July 2025) and authors
  added: '2026-08-15'
  confidence: high
  verified: true
related_datasets:
- id: pkulaw
  relation: often-confused-with
# china-sez-legal-cases-crime-2026 and china-land-dispute-files-2027 (candidate
# ledgers, not yet canonical) remain overlap-check targets noted in the prose.
---

## Positioning in one sentence

A case-level corpus of ~6.42M Chinese civil judgments (2014-2018) with matched live-broadcast exposure, built by the ReStud authors from China Judgments Online via an unnamed commercial data company; Zenodo 10.5281/zenodo.15729271 is a direct CC-BY-4.0 route to a readme PDF and package ZIP, while the full original corpus requires registered CJO retrieval or a commercial channel unless later package inspection establishes otherwise.

## Select rules

- Prioritize it when the research question needs bulk civil judgment texts with court and time identifiers, especially designs exploiting the 2016-2017 staggered rollout of live trial broadcasting (court-by-time DiD, Bartik IV).
- Switch to pkulaw when the need is legal documents or regulations for reference, not a systematic empirical corpus; switch to hand-collected court-case collections for narrow, case-specific research questions where the 6.42M corpus sample restrictions (civil, individual litigants, 2014-2018) do not fit.
- It cannot answer questions about criminal/administrative cases, about post-2018 judgment universes, or about official court statistics; it cannot support judge-level claims without the paper's broadcast-exposure design and its gender-inference caveats.

## Get recipe

1. Download Zenodo 10.5281/zenodo.15729271 (CC-BY-4.0): its current public record lists readme.pdf and replication_package.zip.
2. Inspect the package ZIP manifest to learn whether it contains code, derived files, the 6.42M raw judgments, or only pointers to them.
3. If raw corpus is needed, register on wenshu.court.gov.cn and collect within current retrieval limits, or pursue an authorized data-service/commercial channel for a bulk extract; verify current terms first (homepage reachable 2026-08-15; exact limits not captured).
4. For broadcast exposure, use tingshen.court.gov.cn records matched by case number; the paper used all 11,016,416 records as of April 2021.
5. Add prefecture controls (China City Statistical Yearbook: GDP per capita, population, internet penetration) as the paper does.

## Connections and Limitations

Judgments link to broadcast records by case number; judge identity is court+name (Ngender-inferred gender, 92% accuracy); prefecture controls need boundary-vintage checks. The corpus stops at December 2018 and covers only civil cases with individual litigants; CJO publication volume declined after 2018, so extending coverage to later years requires a new sample definition. The exact 2020 corpus vintage and the commercial company behind it are unnamed, and the current replication ZIP's internal contents, including any raw texts, are unverified - both are open verification items.
