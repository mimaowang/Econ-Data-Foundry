---
schema_version: 3
catalog_status: grounding
id: china-51job-vacancy-postings-2019
name: 51job.com (前程无忧) vacancy postings corpus used by He, Mau & Xu (2021 Labour Economics)
aka:
- 51job.com job vacancies May-November 2019
- Qian Cheng Wu You 51job.com corpus
- Trade War vacancy postings corpus
- 前程无忧招聘信息数据
provider: Raw source 51job.com (前程无忧, Qian Cheng Wu You); corpus collected and processed by the paper's authors (He, Mau & Xu)
china_related: true
domains:
- labor
- urban
- firm
- trade
- regional
data_pathway:
  mode: inaccessible
  origin: researcher-collected
  target_artifact: "The paper-specific corpus: monthly-frequency job vacancy postings crawled from 51job.com, May through November 2019; the authors' analysis sample is 30,123 firms matched to China Customs statistics with 607,532 vacancies"
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: The paper's own working paper (Maastricht GSBE Research Memorandum RM21001, read in full 2026-08-14) confirms the platform identity (51job.com), the collection window (May-November 2019, four crawls per month), the observation unit (vacancy postings with unique URL-based vacancy IDs, linked to firm pages), the fields, and the analysis sample. No data availability statement, released data package, or replication files were found in the working paper; the historical 2019 postings are not recoverable from the live site, so the exact corpus is obtainable only by author contact. A new crawl of 51job.com would be a different asset with a different period and fresh terms.
  barrier: No released package identified (working paper contains no data availability statement; published Labour Economics version's data section unread - ScienceDirect 403 in this environment). The historical May-November 2019 posting universe no longer exists on the live platform, so the corpus cannot be reconstructed for the same window; only a new-period collection is feasible, subject to current 51job.com terms and the paper's documented crawler recipe.
unit_of_observation: Job vacancy posting on 51job.com, uniquely identified by the vacancy ID embedded in the posting URL and linked to the posting firm's page
structure: Monthly-frequency repeated cross-section of vacancy postings (universe downloaded four times per month, duplicates removed keeping the first monthly observation), May through November 2019
geo_granularity:
- city (prefecture)
- province
geography: 297 prefecture cities in 31 Chinese provinces
time_span:
  start: '2019-05'
  end: '2019-11'
  coverage_note: 'Working paper Section 2.1: "We collected information systematically since May 2019 to construct a dataset with monthly frequency covering the period through November 2019." Appendix A.2: universe of postings downloaded four times per month (end of each week), duplicates removed keeping first monthly observation. The paper''s own words say the data window is May-November 2019; earlier secondary summaries (HUST/Zhang Peigang institute pages) said "2018-2019", which does not match the working paper text.'
  last_checked: '2026-08-14'
frequency:
- monthly observations (May-November 2019)
- four crawl passes per month within each month
sample_size: 1.7-2.7 million distinct job vacancies per month across all 51job postings; analysis sample = 30,123 firms matched to Chinese Customs records, posting 607,532 distinct vacancies in May-November 2019
key_variables:
- Offered salary and non-wage compensation (subsidies, bonus, insurance package)
- Job requirements: education, work experience, language and computer skills
- Detailed job description with keywords
- Working location (prefecture city / province)
- Firm characteristics via linked firm page: ownership, scale of employment, main industry
- Unique URL-based vacancy identifier (posting ID)
- Posting/refresh timing (monthly observations)
research_fit:
  best_for:
  - Understanding which Chinese online recruitment platform products exist and how they differ (51job vs Zhaopin): this record fixes 51job as a distinct, paper-verified platform product with a documented collection recipe
  - Employer-side hiring demand of Chinese importers/exporters during the 2019 US-China trade-war tariff waves (the paper's own research question)
  - A template for a new 51job vacancy-posting collection (the working paper documents crawl frequency, deduplication, and the platform's 100,000-postings-per-city capacity limit)
  choose_over:
  - Choose this identity/record over the Zhaopin records when the platform in question is 51job.com: it is a different company (founded 1999, about 150 million registered job-seekers, roughly 460,000-520,000 unique employers per year per its 20-F), a different period, and a different posting universe
  - Choose the paper's method description over a generic "scrape a job board" plan when designing a new Chinese vacancy collection, because the working paper documents the platform mechanics in detail
  not_good_for:
  - A nationally representative measure of Chinese employment or vacancies (51job overrepresents white-collar, college-requiring jobs; >70% of advertised jobs require college education, higher than the ~30% census share)
  - The 2018 period: the working paper's own collection window is May-November 2019 (the earlier "2018-2019" wording in secondary pages is not supported by the paper text)
  - Any use of the paper's exact corpus: no release was found and the historical postings are gone
  - Firm outcomes or realized hires: the data observe postings, not actual employment or filling
  needs_join_for:
  - Chinese Customs trade statistics (the paper matches firm names to customs records for tariff exposure)
  - Census employment benchmarks (2015 Population Census; 2018 Economic Census) for coverage comparisons
  - City-level controls for a trade-war labor-demand design
  variation_available:
  - Firm-by-month variation in posting counts and advertised wages/requirements across May-November 2019
  - City and industry variation (about 60 industry sectors; 297 prefecture cities)
  - Within-firm changes in vacancy content over the trade-war tariff timeline (causal design claims belong to the Econ-Variation repository, not this record)
  topics:
  - online job postings
  - vacancies
  - trade war
  - employer demand
  - urban labor markets
good_for:
- Platform-identity routing: distinguishing 51job from Zhaopin online recruitment products
- Documenting the paper-verified production recipe for a 51job vacancy corpus
identification: []
linkable_keys:
- Vacancy ID embedded in the posting URL (paper-described)
- Firm name (as posted on 51job.com; matched to customs records by name)
- Prefecture city and province labels
- Industry sector (about 60 categories)
joins:
- target: china-customs
  relation: complement
  keys:
  - Firm name (normalized Chinese company name)
  method: The paper matches firm names stated on 51job.com to Chinese Customs statistics to build the trade-exposed firm sample (30,123 firms)
  evidence_status: literature-used
- target: china-zhaopin-job-ads-2008-2010
  relation: often-confused-with
  keys:
  - None (different platform, different period)
  method: "Keep the two products separate: Zhaopin.com 2008-2010 (that record) vs 51job.com May-November 2019 (this record); both are Chinese online vacancy corpora but different platforms, periods, and releases"
  evidence_status: verified
access_routes:
- route: Author/paper route to the exact corpus
  access_status: no-public-route-found
  direct_url: needs-verification
  requirements:
  - Contact the authors (working paper has no DAS, no replication package, no repository deposit found)
  - The published Labour Economics version's data availability statement was not readable in this environment (ScienceDirect 403)
  steps:
  - Read the working paper data section and Appendix A.2 (URL below) to confirm what the corpus contains
  - Contact the corresponding author for any released data; do not assume a deposit exists
  deliverable: Unknown; no public artifact confirmed
  cost: by-application
  last_checked: '2026-08-14'
  caveat: Absence of a release in the working paper is not proof that no release exists elsewhere; the published-version statement must be checked in a human browser. Cost is unknown until the authors respond.
- route: New-period collection from 51job.com (a different asset)
  access_status: needs-verification
  direct_url: https://www.51job.com/
  requirements:
  - Review current 51job.com terms, robots/rate limits, and login requirements before any crawl
  - Historical May-November 2019 postings are not recoverable; only a new period can be collected
  steps:
  - Follow the working paper recipe: download the universe of postings four times per month (end of each week), identify vacancies by the URL-embedded vacancy ID, remove duplicates keeping the first monthly observation
  - Note the platform's per-city capacity limit of 100,000 postings and automatic refresh behavior
  - Document the new window, coverage, and validation as a new asset
  deliverable: A newly collected vacancy corpus for a period chosen by the researcher
  cost: free
  last_checked: '2026-08-14'
  caveat: New collection is a distinct research asset, not the paper's 2019 corpus; platform state and terms have changed since 2019.
access:
  url: https://www.51job.com/
  cost: free
  license: Platform terms apply; no released research artifact known
  format:
  - working paper PDF (RM21001) documenting the data
  - live platform pages (for new collection)
  api: false
  how_to_get: The exact 2019 corpus is not publicly obtainable; start from the working paper's data section to understand the asset, contact the authors for the corpus, or plan a new-period 51job collection under current terms.
caveats: This record documents a paper-verified paper-specific corpus that is not released. The platform identity (51job.com) and production recipe are the durable knowledge; the corpus itself is unavailable. Do not treat 51job.com as interchangeable with Zhaopin.com, and do not cite the paper's "2018-2019" summary wording - the working paper's own collection window is May through November 2019.
production:
  raw_sources:
  - name: 51job.com public vacancy postings
    source_type: webpage
    role: Public job postings from which the authors extracted salary, requirements, job description, location, and firm-page linkage
    access_route: Web crawler downloading the universe of postings four times per month during May-November 2019; historical pages no longer available
    url: https://www.51job.com/
    coverage: 297 prefecture cities in 31 provinces; about 60 industry sectors; per-city posting capacity limit of 100,000 with automatic refresh
    last_checked: '2026-08-14'
  acquisition_methods:
  - crawl
  - manual coding (none; fields are standardized on the platform)
  sample_construction: 'The paper treats the downloaded universe of postings as the frame. Four crawl passes per month (end of each week); duplicates of a job removed keeping only the first monthly observation. Analysis sample restricted to firms matched by name to Chinese Customs statistics: 30,123 firms, 607,532 vacancies, May-November 2019.'
  pipeline_stages:
  - stage: collect
    inputs:
    - 51job.com posting pages
    method: "Web crawler searches automatically for vacancy postings; city-level pages have a 100,000-posting capacity limit and refresh several times per day; download universe four times per month (end of each week)"
    tools:
    - Paper-described web crawler
    parameters:
    - Four crawl passes per month
    - URL-based vacancy ID used for identification
    output: Raw posting snapshots May-November 2019
    evidence: Working paper Section 2.1 and Appendix A.2 (read in full 2026-08-14)
  - stage: clean
    inputs:
    - Raw posting snapshots
    method: Remove all duplicates of a job within the month, keeping the first monthly observation; revisions observed only across months (wage offers most often revised, 6.19% of ads)
    tools: []
    output: Monthly-frequency distinct vacancy records
    evidence: Working paper Appendix A.2 and Table A.1
  - stage: extract
    inputs:
    - Distinct vacancy records
    method: "Parse standardized fields: salary, non-wage compensation, education/experience/language/computer-skill requirements, job description, location; firm characteristics from linked firm page (ownership, employment scale, main industry)"
    tools: []
    output: Vacancy-level variables used in the analysis
    evidence: Working paper Section 2.1
  - stage: match
    inputs:
    - Vacancy records with firm names
    - Chinese Customs statistics
    method: Match company names stated on 51job.com to customs records; analysis sample = 30,123 firms, 607,532 vacancies
    tools: []
    output: Trade-exposed firm vacancy sample
    evidence: Working paper Section 2.3
  constructed_variables: []
  validation:
  - "Compare posted-job education requirements with the 2015 Population Census (paper finds 51job overrepresents college-requiring jobs: >70% vs census ~30%)"
  - Compare industry composition with census sectoral employment and firm populations
  - Note the general white-collar skew of online vacancy data as a coverage limit
  output:
    unit_of_observation: Vacancy posting (URL-identified), firm-linked
    structure: Monthly repeated cross-section, May-November 2019
    geography: 297 prefecture cities, 31 provinces
    time_span: 2019-05 to 2019-11
    key_variables:
    - Salary and non-wage compensation
    - Education, experience, language, computer-skill requirements
    - Job description keywords
    - Location, industry, firm characteristics
    - Vacancy ID and posting month
    formats:
    - Not released (paper-created files only)
  reproducibility:
    level: not-reproducible
    starting_point: No public data or code found; the working paper documents the collection recipe
    code_available: false
    code_url: ''
    requirements:
    - Author contact for the corpus (unknown response)
    - Or a new crawl under current 51job.com terms
    blockers:
    - No released package or DAS found in the working paper
    - Historical 2019 postings no longer exist on the platform
    - Published-version data availability statement unread (ScienceDirect 403)
  compliance:
    terms_or_license: Current 51job.com terms apply to any new collection; 2019-era terms are historical context only
    robots_or_rate_limits: Review current platform robots/rate limits before crawling; do not assume the 2019 crawler behavior is still permitted
    personal_or_sensitive_data: Postings may include employer contact information; minimize and protect identifying fields
    redistribution: Do not redistribute any author-provided or newly collected data without applicable permission
    review_needed: Recheck platform terms and the published paper's data availability statement before a new project
quality:
  profile_status: verified
  access_status: unavailable
  paper_use_status: verified
  last_audited: '2026-08-14'
used_by:
- cite: 'He, Mau & Xu (2021), Trade Shocks and Firms'' Hiring Decisions: Evidence from Vacancy Postings of Chinese Firms in the Trade War, Labour Economics 71, 102021'
  doi: https://doi.org/10.1016/j.labeco.2021.102021
  journal: Labour Economics
  year: 2021
  dataset_role: Main employer-side vacancy-posting corpus (51job.com, May-November 2019) for estimating hiring responses to US-China tariff waves; analysis sample 30,123 customs-matched firms, 607,532 vacancies
  evidence_type: working_paper_data_section
  evidence_url: https://cris.maastrichtuniversity.nl/ws/portalfiles/portal/61116950/RM21001.pdf
  data_note: 'Working paper (Maastricht GSBE RM21001, read in full 2026-08-14) Section 2 names 51job.com as the source, states the May-November 2019 monthly collection (four crawls per month, duplicates removed), the URL-based vacancy ID, firm-page linkage, and the 30,123-firm/607,532-vacancy customs-matched sample. The working paper contains no data availability statement; the published version''s data section was not readable here (ScienceDirect 403).'
provenance:
- source: https://cris.maastrichtuniversity.nl/ws/portalfiles/portal/61116950/RM21001.pdf
  field_scope:
  - platform identity
  - collection window and method
  - observation unit
  - fields and firm linkage
  - analysis sample
  - coverage limits
  - absence of DAS in the working paper
  added: '2026-08-14'
  confidence: high
  verified: true
- source: https://doi.org/10.1016/j.labeco.2021.102021
  field_scope:
  - paper identity
  - journal and DOI
  added: '2026-08-14'
  confidence: high
  verified: true
related_datasets:
- id: china-zhaopin-job-ads-2008-2010
  relation: often-confused-with
- id: china-customs
  relation: complement
---

## Positioning in one sentence

This record fixes the identity of the paper-verified 51job.com (前程无忧) vacancy corpus behind He, Mau & Xu (2021 Labour Economics): a researcher-collected monthly corpus of public postings, May-November 2019, 297 prefecture cities, that was never released and whose historical postings no longer exist; its durable value is the platform identity, the collection recipe, and the boundary against the Zhaopin records.

## Select rules

Use this record when a research idea involves 51job.com vacancy data: it tells you the platform's 2019 collection recipe (four crawls per month, URL-based vacancy IDs, per-city 100,000-posting capacity, deduplication keeping first monthly observation) and that the paper's exact corpus is unavailable. Choose the Zhaopin records when the platform is Zhaopin.com; the two are different companies and different products. Do not use the paper's "2018-2019" summary wording: the working paper's own collection window is May through November 2019. For a new vacancy-collection project in China, start from this recipe plus current platform terms, and treat the result as a new asset.

## Get recipe

Read the working paper (RM21001 PDF, linked above) Sections 2.1, 2.3 and Appendix A.2 to understand the corpus and its construction. The exact corpus is not publicly obtainable: check the published Labour Economics version's data availability statement in a human browser and, if needed, contact the authors. If the goal is a new 51job collection, review current platform terms, then crawl the posting universe four times per month, deduplicate by URL-embedded vacancy ID, and validate coverage against census benchmarks as the paper does.

## Connections and Limitations

51job.com is a distinct platform from Zhaopin.com: different company, different period, different posting universe, and (unlike the Zhaopin corpus) no author-released data files found. The corpus overrepresents white-collar, college-requiring jobs and misses blue-collar demand; it observes postings, not realized hires. The paper joins firm names to Chinese Customs statistics; a similar join is the natural connection for trade-related designs. Historical 2019 postings are gone, so the paper's exact window cannot be reconstructed.

## Decision sufficiency check

From this record alone, an agent can say what the He/Mau/Xu corpus is (51job.com postings, May-November 2019, monthly crawls, 30,123 customs-matched firms), why it is not obtainable (no release found; historical postings gone), how a new 51job collection would proceed, and why 51job and Zhaopin must not be merged. The one open item is the published version's data availability statement, which needs a human browser.
