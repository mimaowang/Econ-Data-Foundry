---
schema_version: 3
catalog_status: ready
id: china-zhaopin-job-ads-2008-2010
name: Zhaopin.com Job Advertisements Corpus used by Kuhn & Shen (2008-2010)
aka:
- Zhaopin.com job ads
- 智联招聘招聘广告数据
- GenderDiscrimData
- China online recruitment advertisements 2008-2010
provider: Zhaopin.com (智联招聘) as the raw platform; corpus collected and processed by Peter Kuhn and Kailing Shen
china_related: true
domains:
- labor
- urban
- firm
- development
- public
data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: Author-posted GenderDiscrimData.zip and do_files.zip replication materials for the QJE job-ad analysis, plus the online appendix
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The authors provide a direct route to the paper's data files and code through their data page. The package is the target research asset; it is not a live mirror of Zhaopin.com and does not make the historical platform archive or a new full crawl available.
  barrier: The original historical ads came from a platform whose pages, terms, and archive access can change. The author links currently lead to Google Drive files and may require an account; file-level license and contents should be checked before redistribution.
unit_of_observation: Unique job advertisement (with firm linkage where retained); firm-level summaries are derived
structure: Repeated short observation windows of web-posted vacancies; reposts are deduplicated and renewal counts retained
geo_granularity:
- city
- province
- national aggregate
geography: Zhaopin postings across all Chinese provinces, with the corpus concentrated in large urban labor markets; Beijing and Shanghai account for large shares of the ads
time_span:
  start: '2008-05-19'
  end: '2010-02-21'
  coverage_note: 'Four collection windows: 2008-05-19 to 2008-06-22, 2009-01-19 to 2009-02-22, 2009-05-18 to 2009-06-21, and 2010-01-18 to 2010-02-21. These are observation windows, not a continuous panel of vacancies or firms.'
  last_checked: '2026-08-10'
frequency:
- daily collection within four windows
- short repeated cross-section
sample_size: 1,057,538 unique job advertisements and 74,202 distinct firms in the paper's reported corpus; secondary summaries sometimes round or report slightly different counts, so preserve the paper's primary count and the release version separately
key_variables:
- Posting and renewal timing
- Job location at city/province level
- Firm identifier or name where retained
- Occupation and industry categories
- Education and experience requirements
- Explicit gender preference
- Age, height, and appearance requirements
- Vacancy count where reported
- Wage information where reported
- Employer ownership or firm characteristics where retained in the release
research_fit:
  best_for:
  - Employer-side hiring preferences and gender targeting in urban Chinese labor markets
  - City- and occupation-level comparison of advertised job requirements, skill demand, and vacancy composition
  - Reproducing or extending the QJE paper's descriptive analysis of firm- and occupation-specific advertised preferences
  choose_over:
  - Choose this corpus over household surveys when the outcome is the content or composition of employer vacancies rather than realized worker employment, wages, or household welfare.
  - Choose the author package over a new Zhaopin crawl when reproducing the historical QJE sample; a new crawl is a different time period and must be documented as a new asset.
  not_good_for:
  - Nationally representative employment, worker-side job search, realized hiring, wages, or vacancy filling
  - A continuous city panel or causal policy design without an external treatment and additional outcome data
  - Historical ads outside the four windows, or the full population of Chinese jobs
  needs_join_for:
  - City or province labor-force benchmarks, including the 2005 1% Population Sample Survey
  - Local policy, industry, firm registry, or population measures by city and period
  - Worker outcomes or application/callback data, which are not supplied by this ad corpus alone
  variation_available:
  - Cross-city and cross-province differences in advertised vacancies
  - Four short time windows between 2008 and 2010
  - Within-firm, within-occupation, and job-level differences in advertised requirements and gender preferences
  topics:
  - online job postings
  - urban labor markets
  - gender discrimination
  - employer demand
  - vacancies
  - occupational sorting
good_for:
- Urban labor-market demand and job-ad content
- Employer gender, age, height, and appearance preferences
- Skill requirements and firm-specific vacancy comparisons
identification:
- Descriptive cross-city and cross-occupation comparisons
- Within-firm and within-firm-occupation comparisons
- Short-window comparisons with external policy or market shocks only after a separate treatment is documented
linkable_keys:
- City and province labels as posted
- Firm identifier or normalized firm name, if present in the released file
- Occupation and industry categories
- Ad posting or collection window
- Ad identifier, if retained in the release
joins:
- target: china-census
  relation: complement
  keys:
  - City or province
  - Occupation or industry category
  - Gender, age, and education aggregates
  - 2005 benchmark year
  method: Aggregate benchmark comparison; the QJE paper uses 2005 Census urban employment distributions for this purpose
  evidence_status: literature-used
access_routes:
- route: Author replication page
  access_status: public-direct-download
  direct_url: https://sites.google.com/view/peter-kuhn/home/data/gender-discrimination-in-job-ads
  requirements: A browser and the author page's current Google Drive download flow; verify file-level terms before reuse or redistribution.
  steps:
  - Open the author page and save the online appendix and page version.
  - Download GenderDiscrimData.zip and do_files.zip from the linked files when access is granted.
  - Read the do-file comments and appendix before changing filters or treating a file as raw versus derived.
  - Re-run the supplied do-files in the documented folder structure, or preserve the released data as the reproduction target.
  deliverable: Author-posted data files, Stata do-files, and online appendix for the paper's analysis; not a current Zhaopin archive
  cost: free
  last_checked: '2026-08-10'
  caveat: >-
    On 2026-09-28 the author page and all three named Google Drive links returned public download responses:
    GenderDiscrimData.zip (18,814,289 bytes), do_files.zip (15,891 bytes), and
    GenderDiscrimOnlineAppendix.pdf (134,942 bytes). This confirms an acquisition start, not the archive interiors,
    file-level license, or redistribution terms.
- route: Paper and online appendix documentation
  access_status: documentation
  direct_url: https://broomcenter.ucsb.edu/sites/default/files/publications/pdf/kuhn3.pdf
  requirements: Read the appendix and data section; the publisher article may require subscription access.
  steps:
  - Read the data section and Appendix 2 for the collection windows, crawler logic, deduplication, and filters.
  - Compare the released files with the paper's reported sample and variable definitions.
  - Treat any missing raw HTML or intermediate files as a reproducibility boundary, not as an invitation to infer them.
  deliverable: Public paper/appendix documentation for the production path and limitations
  cost: free
  last_checked: '2026-08-10'
access:
  url: https://sites.google.com/view/peter-kuhn/home/data/gender-discrimination-in-job-ads
  cost: free
  license: Author-posted files; confirm Google Drive and author terms before reuse or redistribution
  format:
  - zip archives
  - Stata do-files
  - online appendix PDF
  api: false
  how_to_get: Start at the author's data page, download the named archives if the links permit, read the appendix and README/comments, and reproduce only the released historical target. A new scrape of Zhaopin.com would be a separate collected asset with new terms, coverage, and validation.
production:
  raw_sources:
  - name: Zhaopin.com job advertisements
    source_type: webpage
    role: Historical public job-posting pages from which the authors collected vacancy, firm, location, occupation, and requirement fields
    access_route: Historical web crawling during the four paper-specific observation windows; no current bulk archive is promised
    url: https://www.zhaopin.com/
    coverage: Four windows from May 2008 through February 2010; all Chinese provinces represented, with platform-specific urban and occupational selection
    last_checked: '2026-08-10'
  acquisition_methods:
  - Daily web crawler during the four paper-specific windows
  - Master-list comparison to identify reposts and count renewals
  - Download of author-posted replication archives
  sample_construction: The paper treats the universe of unique ads appearing during four observation windows as the sample. Reposted ads are not downloaded again; renewals are counted. Ads listing multiple occupations are restricted to single-occupation ads for the principal analysis, which reduces the sample by about one fifth.
  pipeline_stages:
  - stage: collect
    inputs:
    - Zhaopin.com pages listed on each collection day
    method: A web crawler began at about 11:30 pm each sampling day, retained ads posted that day, and compared later observations with a master list of previously posted jobs.
    tools:
    - Paper-described web crawler
    output: Daily posting records and renewal information for the four windows
    evidence: Kuhn & Shen Appendix 2 in the public paper mirror
  - stage: clean
    inputs:
    - Daily posting records
    - Master list of previously observed jobs
    method: Collapse repeated postings of the same ad while retaining renewal counts and firm linkage; treat the resulting stock as unique ads, not a flow of new vacancies.
    tools:
    - Author do-files where supplied
    output: Unique historical job-ad records
    evidence: Paper data section and Appendix 2
  - stage: extract
    inputs:
    - Unique historical job-ad records
    method: Parse location, occupation, industry, education, experience, gender, age, height, appearance, vacancy count, and other posted requirements where present.
    tools:
    - Author do-files and data files where supplied
    output: Ad-level variables used in the QJE analysis
    evidence: Paper tables, data section, and online appendix
  - stage: other
    inputs:
    - Parsed ad-level records
    method: Restrict the principal sample to ads with one listed occupation; retain alternative specifications for all ads or first-occupation/fractional allocation only when the released code supports them.
    tools:
    - Author do-files
    output: Analysis sample with transparent occupation treatment
    evidence: Paper footnote and online appendix
  - stage: validate
    inputs:
    - Released analysis files
    - 2005 Census urban employment benchmark
    method: Reconcile counts, city/province coverage, occupation definitions, and benchmark composition; report that Zhaopin overrepresents expanding, high-turnover, and relatively skilled jobs.
    tools:
    - Author do-files
    output: Version-specific reproduction table and a coverage/selection note
    evidence: Paper Appendix 2 and Appendix Table A.1
  constructed_variables: []
  validation:
  - Compare released ad and firm counts with the paper's 1,057,538 ads and 74,202 firms
  - Check that reposts are not silently treated as independent new vacancies
  - Preserve the single-occupation restriction and any alternative allocation rule
  - Compare city, occupation, education, and industry composition with the 2005 Census benchmark
  - Record missing wages and platform selection rather than imputing representativeness
  output:
    unit_of_observation: Unique job advertisement, with firm-level summaries derived by code
    structure: Four short repeated cross-sections with renewal counts
    geography: Chinese cities and provinces represented on Zhaopin during the windows
    time_span: 2008-05-19 to 2010-02-21 in four windows
    key_variables:
    - Location, occupation, industry, and firm linkage
    - Education and experience requirements
    - Gender, age, height, and appearance preferences
    - Posting/renewal timing
    formats:
    - Author-posted ZIP archives and Stata files as contained in the release
  reproducibility:
    level: medium
    starting_point: Author data page and GenderDiscrimData.zip/do_files.zip
    code_available: true
    code_url: https://sites.google.com/view/peter-kuhn/home/data/gender-discrimination-in-job-ads
    requirements:
    - Download permission for the author-posted archives
    - Stata or a compatible interpreter for the do-files
    - Folder structure documented on the author page
    - 2005 Census benchmark if reproducing the composition checks
    blockers:
    - Historical Zhaopin pages and raw HTML are not guaranteed to remain available
    - Current file permissions and redistribution terms require rechecking
    - The released package may omit intermediate crawler output or proprietary platform metadata
    - A new collection would not reproduce the historical windows without the same platform state
  compliance:
    terms_or_license: Confirm the author-posted archive terms and Zhaopin historical/current platform conditions before reuse.
    robots_or_rate_limits: Do not crawl the current platform merely because the paper used a crawler; a new collection requires a fresh terms and rate-limit review.
    personal_or_sensitive_data: Job ads may contain contact or employer information; minimize and protect any identifying fields.
    redistribution: Do not redistribute the author files or a newly collected copy unless the applicable terms explicitly permit it.
    review_needed: Recheck file contents, licenses, platform terms, and any personal-data obligations before a new project.
caveats: This is a paper-specific employer-side vacancy corpus, not a representative labor-force survey. The four windows observe the stock of unfilled ads and overrepresent expanding, high-turnover, and relatively skilled jobs; the exact QJE analysis file and the original crawler output are distinct deliverables. A current Zhaopin scrape would be a new asset, not a reproduction of the 2008-2010 corpus.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-09-28'
used_by:
- cite: 'Kuhn & Shen (2013), Gender Discrimination in Job Ads: Evidence from China'
  doi: https://doi.org/10.1093/qje/qjs046
  journal: QJE
  year: 2013
  dataset_role: Main employer-side job-ad corpus for advertised gender, age, height, appearance, and skill requirements; firm and occupation comparisons
  evidence_type: paper_appendix_and_replication
  evidence_url: https://sites.google.com/view/peter-kuhn/home/data/gender-discrimination-in-job-ads
  data_note: The paper reports 1,057,538 unique ads from four windows between May 2008 and February 2010, linked to 74,202 firms and represented across Chinese provinces. The author page supplies GenderDiscrimData.zip, do_files.zip, and the online appendix; these support conditional reproduction of the released analysis asset, not a guarantee of a current Zhaopin archive or a nationally representative job universe.
provenance:
- source: https://sites.google.com/view/peter-kuhn/home/data/gender-discrimination-in-job-ads
  field_scope:
  - replication route
  - code availability
  - target artifact
  - access boundary
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://broomcenter.ucsb.edu/sites/default/files/publications/pdf/kuhn3.pdf
  field_scope:
  - collection windows
  - crawler method
  - deduplication
  - sample size
  - variables
  - limitations
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://academic.oup.com/qje/article-abstract/128/1/287/1839620?login=false
  field_scope:
  - paper identity
  - journal
  - DOI
  - research question
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://sites.google.com/view/peter-kuhn/home/data/gender-discrimination-in-job-ads
  field_scope:
  - current author-page availability
  - named public download routes
  - current file names and response sizes
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: china-census
  relation: complement
---

## Positioning in one sentence

This is the author-released, paper-specific employer-side vacancy corpus behind the 2013 QJE study of gender targeting in Chinese job ads. It is unusually useful for urban labor-demand and employer-preference questions, but its four short windows, platform selection, and dependence on a historical crawl mean that it should not be mistaken for a national labor-force panel or a live Zhaopin database.

## Select rules

Use the author package when reproducing the historical QJE design or studying ad content, firm/occupation heterogeneity, and city-level vacancy composition. Prefer household or census data for realized employment, worker outcomes, population representativeness, or long-run regional trends. Treat a new crawl as a different asset with fresh coverage, legal, and validation conditions.

## Get recipe

Open the author data page, save the online appendix and page version, and download the linked GenderDiscrimData.zip and do_files.zip if the current Google Drive permissions allow it. Recreate the documented folder structure, inspect the do-file comments and sample counts, and compare the released files with the four windows and single-occupation rule in the paper. Do not infer that the raw Zhaopin pages or every intermediate crawler file are included.

## Connections and Limitations

The QJE paper compares the ad corpus with 2005 Census urban employment distributions; that is an aggregate benchmark, not an ad-level join. City and province labels may require normalization before joining policy, population, industry, or firm data. Firm identifiers and contact details may be missing or restricted. Platform selection, stock-versus-flow sampling, repost handling, and short observation windows are central limits on interpretation.

## Decision sufficiency check

From this record alone, an agent can choose the corpus for an employer-side urban labor-market question, reject it for representative worker outcomes, start at the author replication page, reproduce the released historical target with code, and explain why a new Zhaopin crawl or the 2005 Census is not the same asset.
