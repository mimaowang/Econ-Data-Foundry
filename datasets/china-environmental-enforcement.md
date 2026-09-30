---
schema_version: 3
catalog_status: ready
id: china-environmental-enforcement
name: China Environmental Enforcement Records and Geocoded Firm-City Panel used by Axbard & Deng (2010-2017)
aka:
- 中国环境执法记录
- 地方环境处罚记录
- IPE environmental enforcement records
- Axbard-Deng enforcement data
provider: Institute of Public & Environmental Affairs (IPE) source records; Axbard & Deng processing, matching, and geocoding
china_related: true
domains:
- environment
- firm
- urban
- public
- regional

# The public target is the paper-specific deposit, not a claim that the complete historical IPE/ASIF/Tianyancha archives are public.
data_pathway:
  mode: direct
  origin: mixed
  target_artifact: Public openICPSR replication deposit E174901V1 for Axbard & Deng, including processed enforcement panels, depositor-supplied inputs, and replication code
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The best current route is a public paper-specific package. It supplies the authors' processed enforcement and firm/city files plus code, but it is not a guaranteed download of the complete historical IPE archive, the full ASIF survey, or all original Tianyancha/Google geocoding inputs.
  barrier: A researcher needs the repository's current browser/account workflow, substantial storage for the large Stata files, and Stata/Python. Rebuilding the source records from scratch may still require historical IPE pages, restricted ASIF data, commercial Tianyancha access, and geocoding terms that are not included as a redistributable archive.

# Identity and Coverage
unit_of_observation: Raw local enforcement event; matched firm-quarter; and city-period aggregates in separate tables
structure: Multi-table event data plus repeated firm-quarter and city-period panels
geo_granularity:
- firm
- city
- prefecture-level city
- monitoring station
geography: Axbard & Deng's main firm analysis covers 177 small Chinese cities that installed pollution monitors for the first time in 2015; the deposit also contains city, firm, monitor, and weather tables. This is not an all-China firm universe.
time_span:
  start: 2010
  end: 2017
  last_confirmed_release: 2024 paper and openICPSR V1 deposit
  coverage_note: The paper's firm-level enforcement panel is quarterly for 2010-2017. The appendix reports 1,155,296 firm-quarter observations in the main analysis; file-specific counts and the monitor/weather/Baidu/mayor tables differ.
  last_checked: '2026-08-12'
frequency:
- event
- quarterly
- annual
- daily
- monthly
sample_size: 1,155,296 firm-quarter observations in the main firm analysis; 177 first-monitor cities in the main sample; the deposit contains additional event, city, monitor, PM, weather, mayor, and search-index tables.
key_variables:
- Environmental enforcement type: air, water, solid waste, or procedural
- Air enforcement response: suspension, equipment upgrade, fine, or warning
- Firm name, address, industry and identifiers where retained in the supplied file
- Firm latitude, longitude, city, and monitor distance or monitor linkage
- City-quarter and city-year enforcement aggregates
- Monitor identifiers and pollution measures supplied with the replication package
- Weather and prevailing-wind measures, where present in the supplied tables
- Baidu search-index and local-leader fields, where present in the supplied tables

# Research routing
research_fit:
  best_for:
  - Studying which firms or cities received documented environmental enforcement, using the paper's geocoded firm and city panels
  - Linking administrative enforcement records to firm characteristics, monitor locations, pollution measures, or local conditions for 2010-2017
  - Reproducing or extending Axbard & Deng's enforcement-data component with the same paper-specific sample boundary
  choose_over:
  - Choose this record over china-air-quality-monitoring when the outcome is an administrative enforcement or penalty record rather than measured ambient pollution.
  - Choose this record over china-firm-pollution when the question concerns public enforcement actions and their timing, not a firm's emissions or treatment-facility measures.
  - Choose this record over a generic IPE or ASIF description when exact paper-compatible 2010-2017 files, code, and the 177-city boundary matter.
  not_good_for:
  - A complete current archive of every IPE enforcement record in China
  - A nationally representative universe of all firms or all cities
  - Individual health, household, migration, or employment outcomes without another outcome source
  - A policy or treatment-timing database, or a substitute for an independently documented identification design
  needs_join_for:
  - Firm accounting, production, or ownership outcomes beyond the fields supplied in the deposit
  - Individual, household, health, migration, or labor outcomes
  - Current IPE updates, a full ASIF panel, or a newly licensed Tianyancha/geocoding extract
  variation_available:
  - This data asset intentionally does not encode a treatment or assignment rule; consult the separate variation project for that question.
  topics:
  - environmental regulation
  - public enforcement
  - urban pollution
  - industrial firms
  - local government
  - China

# Compatible with existing search fields; these terms do not replace the paper-specific selection rules above.
good_for:
- Firm-level environmental enforcement outcomes
- City-level enforcement aggregates
- Enforcement records linked to monitor exposure and local conditions
identification:
- This is a paper-specific enforcement, firm-location, and code package, not a stand-alone causal-variation record. It supports reproducing the documented 2010-2017 enforcement analysis and inspecting released fields; any new identification claim requires separate design assessment.
linkable_keys:
- Firm name, address, or retained firm identifier (file-specific; inspect the codebook before relying on it)
- City or prefecture name/code
- Year and quarter
- Latitude and longitude
- Monitor identifier and coordinates

joins:
  - target: asif
    relation: complement
    keys:
    - firm identity or normalized name/address
    - city or county code
    - year
    method: Match the supplied firm/enforcement panel to the licensed ASIF edition only after checking identifier and year definitions; the paper used ASIF 2013 as the firm frame.
    evidence_status: literature-used
  - target: china-tianyancha-firm-information
    relation: complement
    keys:
    - firm name
    - address
    - latitude and longitude
    method: Tianyancha and other web sources were used to identify and geocode firms; a current commercial extract is not assumed to reproduce the historical match.
    evidence_status: literature-used
  - target: china-air-quality-monitoring
    relation: complement
    keys:
    - monitor identifier
    - city
    - date or year
    - coordinates
    method: Use the monitor and pollution files supplied with the deposit or a separately verified CNEMC/MEE series; reconcile station openings and measurement definitions before joining.
    evidence_status: literature-used
  - target: china-firm-pollution
    relation: often-confused-with
    keys:
    - firm identity
    - city
    - year
    method: Keep enforcement events separate from emissions or treatment-facility measures; join only when the research question needs both outcomes.
    evidence_status: plausible

# Preserve distinct provider, public-deposit, and source-reconstruction routes.
access_routes:
  - route: openICPSR-paper-specific-replication-deposit
    access_status: available-with-conditions
    direct_url: https://www.openicpsr.org/openicpsr/project/174901/version/V1/view
    requirements:
    - Browser access and the repository's current account/download workflow
    - Enough disk space for the large Stata files, especially firm_enf.dta and raw PM/weather files
    - Stata for the .do files and Python for classify.py; read the README before running code
    steps:
    - Open the V1 project page and read README.pdf and the file manifest.
    - Download the replication Data, Do-file, and ado folders, keeping Raw inputs distinct from processed outputs.
    - Inspect Master.do, MakeData.do, classify.py, and the documented paths before running any script.
    - Treat the deposit as the paper-specific target artifact; do not describe its Raw folder as a complete original IPE/ASIF/Tianyancha archive.
    deliverable: Public V1 files including processed enforcement/city/firm panels, source-input files supplied by the depositor, and replication code; the exact original archives and all current source pages are not guaranteed.
    cost: free
    last_checked: '2026-09-28'
    caveat: Current DataCite metadata verifies the active, findable v1 DOI and matching openICPSR route, but not a deposit license or current download terms. openICPSR says the materials are distributed as supplied by the depositor and are not reviewed or processed by ICPSR; recheck package version and redistribution rights.
  - route: AEA-online-appendix-documentation
    access_status: available
    direct_url: https://www.aeaweb.org/articles/materials/20030
    requirements: Browser access
    steps:
    - Read the appendix data section for source production, classification, validation, geocoding, and sample definitions.
    - Use it to interpret the deposit and to distinguish paper-specific inputs from current provider products.
    deliverable: Author documentation; not a replacement for the data files.
    cost: free
    last_checked: '2026-08-12'
    caveat: Documentation confirms how the paper built the asset but does not promise that every original source archive remains downloadable.
  - route: IPE-current-provider-route
    access_status: needs-verification
    direct_url: https://www.ipe.org.cn/industryrecord/regulatory.aspx
    requirements:
    - Check the current Blue Map/regulatory-record interface, historical retention, terms, and export options.
    steps:
    - Use the current IPE interface to understand present source records and provider definitions.
    - Do not infer that current pages reproduce the paper's 2010-2017 historical extract or its firm matching.
    deliverable: Current provider records or documentation, subject to the provider's terms; not automatically the paper's panel.
    cost: free
    last_checked: '2026-08-12'
    caveat: IPE's current product and historical page retention may differ from the authors' collection window.

access:
  url: https://www.openicpsr.org/openicpsr/project/174901/version/V1/view
  cost: mixed
  license: Recheck openICPSR depositor terms, IPE record terms, Tianyancha terms, and any geocoding-provider conditions before reuse or redistribution.
  format:
  - dta
  - do
  - py
  - pdf
  api: false
  how_to_get: Start with the openICPSR V1 README and manifest, then download the paper-specific processed and raw-supplied files and code. Obtain any missing licensed source separately rather than treating the deposit as a complete raw archive.
caveats: The public deposit is a reproducibility starting point, not proof that the historical IPE archive, ASIF 2013 microdata, Tianyancha records, Google geocoding responses, or all source pages can be independently reacquired. Exact field names, identifier retention, and file-specific coverage must be checked in the downloaded README/codebook.

# The asset is researcher-collected and researcher-constructed even though its best current access route is a direct public deposit.
production:
  raw_sources:
    - name: IPE local environmental enforcement records
      source_type: webpage
      role: Public enforcement notices collected from local environmental bureaus, government websites, media, and official government Weibo; source events for the paper's enforcement database
      access_route: IPE-current-provider-route
      url: https://www.ipe.org.cn/industryrecord/regulatory.aspx
      coverage: Historical records used by the paper for 2010-2017; exact current retention and complete archive availability are unresolved
      last_checked: '2026-08-12'
    - name: Annual Survey of Industrial Firms (ASIF) 2013
      source_type: dataset
      role: Firm frame and accounting/address fields used to match enforcement records; underlying microdata are not established as public in this deposit
      access_route: Institutional or licensed ASIF route; see asif record
      url: https://microdata.stats.gov.cn/
      coverage: Active manufacturing firms above the reporting threshold and all SOEs in the paper's 2013 firm frame
      last_checked: '2026-08-12'
    - name: Tianyancha firm registry and web geocoding sources
      source_type: webpage
      role: Firm identity/address checks and coordinates; the authors also used Google Maps API and manual web searches for remaining firms
      access_route: Current provider terms and paper-specific deposit/code
      url: https://www.tianyancha.com/
      coverage: Firms retained in the paper's match and geocoding process; not a promise of a reproducible historical registry extract
      last_checked: '2026-08-12'
    - name: Axbard & Deng replication package inputs
      source_type: archive
      role: Depositor-supplied raw/processed inputs for the paper-specific target artifact
      access_route: openICPSR-paper-specific-replication-deposit
      url: https://doi.org/10.3886/E174901V1
      coverage: 2010-2017 paper package, with file-specific tables and additional monitor, PM, weather, search, and mayor inputs
      last_checked: '2026-08-12'
  acquisition_methods:
  - Public-record extraction from government pages, media, and official social-media posts
  - Manual validation and image-record transcription
  - Keyword-based classification of enforcement notices
  - Firm matching using ASIF names/addresses and web identity sources
  - Geocoding with Tianyancha, Google Maps API, and manual internet sources
  - Download of the paper-specific public replication deposit
  sample_construction: The authors first extracted and categorized enforcement records for each city, then matched them to annual ASIF industrial firms and geocoded the matched firms. The main analysis uses 177 cities that installed monitors for the first time in 2015; the deposit contains the resulting firm, city, monitor, PM, weather, mayor, and search-index tables.
  pipeline_stages:
    - stage: collect
      inputs:
      - IPE/local-bureau enforcement notices
      - Government websites, media, and official government Weibo
      method: Extract all located enforcement records available to the authors for the paper's cities and period.
      tools: []
      parameters: 2010-2017 historical collection; retention gaps remain possible because pages may be removed after five years.
      output: Enforcement-record source set
      evidence: AEA online appendix, data details section
    - stage: validate
      inputs:
      - Enforcement records
      method: Manually check a 1,000-firm baseline sample for 2015-2017 against the source records; the appendix reports year-specific classified counts and notes possible missing pages.
      tools: [manual review]
      parameters: 1,000-firm validation sample; exact denominators and exclusions are in the appendix.
      output: Validated enforcement classifications with known source-retention limits
      evidence: AEA online appendix, enforcement-data validation discussion
    - stage: classify
      inputs:
      - Enforcement notices
      - Approximately 1,500 image records
      method: Keyword algorithm for air, water, solid-waste, and procedural violations and for suspension, upgrade, fine, and warning outcomes; image records manually extracted.
      tools: [Python classify.py, manual extraction]
      parameters: Paper-specific keyword categories; inspect classify.py and appendix before reuse.
      output: Coded enforcement type and punishment fields
      evidence: AEA online appendix and openICPSR Do-file/classify.py manifest
    - stage: geocode
      inputs:
      - ASIF firm names and addresses
      - Tianyancha and Google Maps/web sources
      method: Resolve firm locations and monitor distances; approximately 4,000 firms required manual internet sources.
      tools: [Tianyancha, Google Maps API, manual web search]
      parameters: The appendix reports precise geolocation for 98.7% of firms in the relevant matched set; file-specific missingness must still be checked.
      output: Firm coordinates and spatial links to monitors/cities
      evidence: AEA online appendix, geocoding discussion
    - stage: match
      inputs:
      - Coded enforcement records
      - ASIF firm frame
      - Geocoded firm and city information
      method: Match enforcement records to annual manufacturing firms and aggregate to firm-quarter and city-period tables.
      tools: [paper code in openICPSR deposit]
      parameters: Main firm panel 2010-2017; main first-monitor sample 177 cities.
      output: firm_enf.dta, enf.dta, city_enf.dta, city_enf_rd.dta and related processed files
      evidence: AEA online appendix table C1 and openICPSR Data/Do-file folders
    - stage: aggregate
      inputs:
      - Matched firm/city enforcement data
      - Monitor, PM, weather, Baidu, and mayor inputs
      method: Supply city-period and firm-quarter analysis tables used by the paper's empirical code.
      tools: [Stata do-files in openICPSR deposit]
      parameters: File-specific frequencies include quarterly, annual, daily, and monthly inputs.
      output: Public paper-specific analysis package
      evidence: openICPSR V1 replication manifest and AEA appendix table C1
  constructed_variables:
    - name: enforcement_category
      concept: Air, water, solid-waste, or procedural violation category
      source_fields: [enforcement notice text/image]
      method: Paper-specific keyword coding with manual image extraction
      validation: Manual 1,000-firm check described in the appendix
      limitations: Missing or removed source pages and classification errors can remain; categories are not a universal current IPE taxonomy.
    - name: air_punishment_type
      concept: Suspension, equipment upgrade, fine, or warning response
      source_fields: [enforcement notice text/image]
      method: Keyword coding and manual extraction
      validation: Appendix validation sample and replication code
      limitations: A recorded public notice is not a complete measure of every enforcement action.
    - name: firm_coordinates_and_monitor_distance
      concept: Spatial location of matched firms relative to pollution monitors/cities
      source_fields: [ASIF firm address, Tianyancha/web identity, monitor coordinates]
      method: Web geocoding and manual resolution; paper reports 98.7% precise geolocation in the relevant set
      validation: Appendix geocoding checks
      limitations: Historical business names, address changes, and missing coordinates can affect matches; current registry results do not guarantee historical reproduction.
  validation:
  - AEA appendix documents a 1,000-firm manual validation sample for 2015-2017 and reports possible page-retention gaps.
  - The replication deposit supplies code and processed outputs; use the README and do-files to check file-specific observations and variable definitions.
  - The package's public availability does not validate the completeness of the underlying IPE/ASIF/Tianyancha sources.
  output:
    unit_of_observation: Raw enforcement event, firm-quarter, city-period, monitor-day/hour, weather-day, and auxiliary control rows in separate files
    structure: Multi-table event and panel package
    geography: 177 first-monitor cities plus the file-specific firm/city/monitor coverage in the deposit
    time_span: 2010-2017 for the enforcement/firm target; auxiliary tables may have narrower windows
    key_variables:
    - Enforcement category and punishment fields
    - Firm identity/address and geocoded coordinates
    - City/monitor identifiers and dates
    - PM, weather, wind, search-index, and mayor fields where supplied
    formats: [Stata .dta, Stata .do, Python .py, PDF README/appendix]
  reproducibility:
    level: medium
    starting_point: Public openICPSR E174901V1 paper-specific replication deposit and the AEA online appendix
    code_available: true
    code_url: https://www.openicpsr.org/openicpsr/project/174901/version/V1/view?path=%2Fopenicpsr%2F174901%2Ffcr%3Aversions%2FV1%2Freplication%2FDo-file&type=folder
    requirements:
    - Browser/account access under current openICPSR terms
    - Large local storage and download time for multi-gigabyte Stata files
    - Stata and Python; read README and edit paths only as documented
    - Separate licensed/researcher access if reconstructing missing ASIF, Tianyancha, IPE, or geocoding inputs
    blockers:
    - The exact complete historical IPE archive and removed source pages are not guaranteed to be downloadable.
    - The underlying ASIF and commercial Tianyancha/geocoding inputs are not established as redistributable in the deposit.
    - The repository distributes depositor-supplied materials without independent ICPSR review; recheck package version, terms, and file integrity through the documented code.
  compliance:
    terms_or_license: Recheck openICPSR deposit terms and the provider terms for IPE, Tianyancha, Google Maps, Baidu, and any licensed NBS data before reuse.
    robots_or_rate_limits: Do not bulk-crawl current provider sites or geocoding services without checking their current terms and rate limits.
    personal_or_sensitive_data: Firm and public-record information; do not infer that all identifiers or any personal fields are safe to redistribute.
    redistribution: The public deposit's redistribution scope and the source providers' terms must be checked separately; a public download is not blanket permission to mirror source archives.
    review_needed: Yes, before any new collection from IPE/Tianyancha/Google/Baidu or any release of a derivative file.

# Separate verification profiling, access, and paper use.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-12'

used_by:
  - cite: 'Axbard & Deng (2024), Informed Enforcement: Lessons from Pollution Monitoring in China'
    doi: https://doi.org/10.1257/app.20210386
    journal: AEJ:Applied
    year: 2024
    dataset_role: Main paper-specific geocoded environmental-enforcement records matched to the ASIF firm frame; city enforcement outcomes and related monitor/environment inputs
    evidence_type: replication_and_appendix
    evidence_url: https://www.aeaweb.org/articles/materials/20030
    data_note: The appendix describes IPE records, classification, manual validation, ASIF matching, Tianyancha/Google/manual geocoding, a 177-city first-monitor sample, and 2010-2017 coverage. The openICPSR E174901V1 deposit is the current public reproduction route, with original-source and rights limits recorded above.

provenance:
  - source: https://www.aeaweb.org/articles?id=10.1257%2Fapp.20210386
    field_scope:
    - paper_identity
    - journal
    - year
    - China and urban/regional relevance
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://www.aeaweb.org/articles/materials/20030
    field_scope:
    - paper_use
    - IPE_source_role
    - classification
    - validation
    - ASIF_matching
    - geocoding
    - sample_boundary
    - time_span
    - variables
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://www.openicpsr.org/openicpsr/project/174901/version/V1/view
    field_scope:
    - public_target_artifact
    - access_route
    - file_manifest
    - geography
    - time_span
    - reproducibility_boundary
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://www.ipe.org.cn/about/about.html
    field_scope:
    - current_provider_identity
    - current_provider_scope
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: DataCite API record 10.3886/E174901V1, queried 2026-09-28
    field_scope:
    - current active, findable v1 ICPSR data-and-code deposit identity and openICPSR project route
    - title, 2023 publication year, China geography, and paper-aligned abstract
    - does not establish a deposit license, current download terms, or public reproducibility of historical IPE, ASIF, Tianyancha, or geocoding source inputs
    added: '2026-09-28'
    confidence: high
    verified: true

related_datasets:
  - id: china-air-quality-monitoring
    relation: complement
  - id: asif
    relation: complement
  - id: china-tianyancha-firm-information
    relation: complement
  - id: china-firm-pollution
    relation: often-confused-with
---

## Positioning in one sentence

This is the paper-specific enforcement asset behind Axbard & Deng: public local enforcement notices were classified, checked, matched to industrial firms, and geocoded into firm and city panels. The openICPSR deposit makes the processed target and code reachable, while the historical IPE archive and several licensed source inputs remain separate reconstruction problems.

## Select rules

Choose this record when the research idea needs a documented environmental enforcement action, its firm/city location, and the Axbard–Deng 2010-2017 sample boundary. Choose the air-monitoring record when the outcome is measured pollution, and choose a firm-pollution record when the outcome is emissions or treatment facilities. Do not treat a current IPE search page, an ASIF subscription, or an openICPSR download as interchangeable with the full historical source archive.

## Get recipe

1. Read the AEA appendix and openICPSR README before downloading or running anything.
2. Download the V1 Data, Do-file, and ado folders; record which files are under `Raw` and which are processed outputs.
3. Inspect `firm_enf.dta`, `enf.dta`, `city_enf.dta`, and the code paths in `Master.do`/`MakeData.do` before using a field or joining another source.
4. If a new study needs the original notices, a later period, a complete ASIF panel, or fresh geocoding, acquire those inputs under their own provider and license conditions. Do not silently substitute current IPE pages for the paper's historical extract.

## Connections and Limitations

The most useful joins are firm identity/address to ASIF or a licensed registry, city and year/quarter to city panels, and monitor identifier/date/coordinates to a separately verified air-quality series. Names and addresses can change, code systems can differ, and the deposited match may retain only file-specific identifiers; inspect the README and code rather than assuming a universal key. Enforcement records measure documented public actions, not total pollution or every unobserved inspection. The paper reports a 1,000-firm manual validation and 98.7% precise geolocation in the relevant set, but page removal, classification error, missing coordinates, source retention, and the 177-city sample limit external coverage.

## Decision sufficiency check

For an idea about whether firms near newly monitored cities received documented environmental enforcement in 2010-2017, start with this record and its openICPSR deposit: it contains the paper-compatible enforcement outcome and the spatial links. Add `china-air-quality-monitoring` for measured pollution, `asif` for licensed firm accounting, or `china-tianyancha-firm-information` for a separately verified registry route. If the idea requires all Chinese cities, current IPE updates, individual outcomes, or a new causal treatment definition, this record is not sufficient by itself; that gap is explicit rather than filled by inference.
