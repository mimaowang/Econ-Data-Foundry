---
schema_version: 3
catalog_status: ready
id: china-mofcom-rural-ecommerce-demo-counties
name: MOFCOM E-commerce into Rural Areas Comprehensive Demonstration Counties batch lists (电子商务进农村综合示范县名单)
aka:
- 电子商务进农村综合示范县名单
- 电商进农村综合示范县
- E-commerce into Rural Areas Comprehensive Demonstration County lists
- 电商进农村示范县
- MOFCOM rural e-commerce demonstration county program lists
provider: 商务部 (MOFCOM) 市场体系建设司 / 流通业发展司, jointly with 财政部 and 国务院扶贫办 (later 国家乡村振兴局); batch lists published on official MOFCOM pages and republished by provincial and prefectural commerce departments
china_related: true
domains:
- rural
- e-commerce
- regional
- policy
- digital-economy
- poverty-alleviation

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A researcher-built county-batch panel for the fully evidenced 2014-2018
    core of the national demonstration program, assembled from the official
    county-name-by-province lists (and the 2016 government republication);
    this is not a provider-released machine-readable file and does not include
    the as-yet-unclosed 2019-2021 continuation.
  availability: reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The official MOFCOM notices now provide a directly extractable 2014-2018
    core: complete HTML tables for 2014 (56 counties) and 2015 (200), a
    government-hosted 2016 republication sourced to MOFCOM (240), and the
    MOFCOM 2017 (260) and 2018 (260) tables. A researcher can legally turn that bounded core
    into a county-batch file after normalizing Chinese county names and adding
    an external administrative-code concordance. This makes the bounded
    2014-2018 core a usable, reproducible research asset. It is not a complete
    2014-2021 panel: the 2019 and first-2020 national roster pages expose their
    lists as images; an official 2020 reply points to a public WeChat roster;
    and the 2021 central notice establishes selection rather than a final
    county roster. The lists carry no per-county funding, effective dates, or
    administrative codes. Direct empirical use is now verified from Xie, Zhao
    and Lei (2025): its county panel says the demonstration-county list comes
    from the MOFCOM website and encodes an entry-year-and-after indicator.
  barrier: >-
    No central machine-readable index of all batches exists. The 2014-2018
    core is publicly readable, but 2019-2021 cannot yet be coded as a complete
    county-year continuation from the checked materials; county-name strings
    also require parsing and code-matching.

unit_of_observation: County (demonstration county within a batch year), listed under its province
structure: Repeated cross-section of annual batches (each county appears in the batch(s) that selected it)
geo_granularity:
- county
geography: China; batches targeted 国家级贫困县 and 欠发达革命老区县 (2017+ explicitly), covering 8 provinces (2014), 26 provinces/regions incl. 新疆兵团 (2015), 23 provinces/regions (2016), 21 provinces (2017), 22 provinces (2018)
time_span:
  start: '2014'
  end: '2018'
  last_confirmed_release: '2018-09-25'
  coverage_note: 'The ready, reproducible core is 2014-2018: 2014 (56 counties, 8 provinces) and 2015 (200 counties, 26 provinces) were published together 2015-07-14 by 商务部流通业发展司; 2016 (240 counties, 23 provinces/regions incl. 兵团 4) is available through an official Tongren municipal commerce-bureau republication; 2017 (260 counties, 21 provinces; 237 国家级贫困县 + 23 欠发达革命老区县; 8 整体推进市州) and 2018 (260 counties, 22 provinces; 238 国家级贫困县 + 22 欠发达革命老区县) each have a MOFCOM HTML roster. The located 2019 MOFCOM notice is graphic-only; government reporting confirms its aggregate of 215 counties, including 138 国家级贫困县, but the individual rows were not text-verified. The 2020 first-batch roster is likewise graphic-only. A MOFCOM public reply states that the complete 2020 roster was published through the public 电子商务进农村 WeChat channel; that channel’s historic roster was not independently retrieved. The 2021 central notice is selection documentation, not a complete final roster. These later sources are extension leads, not coverage of this ready core.'
  last_checked: '2026-09-28'
frequency:
- annual (batch)
sample_size: '2014: 56 counties / 8 provinces; 2015: 200 counties / 26 provinces+兵团; 2016: 240 counties / 23 provinces+兵团; 2017: 260 counties / 21 provinces; 2018: 260 counties / 22 provinces; 2019: 215 counties (138 国家级贫困县; county rows not text-verified); cumulative 1,016 by 2018 (per MOFCOM roster/news)'
key_variables:
- Province (省/区/市)
- Demonstration county name (Chinese, as printed in the official list)
- Batch year
- 2017+ rows also flag 国家级贫困县 vs 欠发达革命老区县 and 整体推进市州 membership
- No administrative codes, no per-county funding, no per-county program dates

research_fit:
  best_for:
  - Constructing county-level program-entry or coverage variables for the verified 2014-2018 core of the national rural e-commerce demonstration program
  - Joining program counties to county-level outcomes or household surveys (CFPS, CHIP, census) by normalized county name
  - Auditing which counties were ever covered (poverty-county coverage 88.6% by 2018 per MOFCOM)
  choose_over:
  - Choose these lists over the Taobao village/town lists (separate record layer) when the research needs the government program's county-level rollout rather than platform-identified villages
  - Choose these lists over the Couture et al. RCT replication corpus when the question needs the documented 2014-2018 national-program county batches rather than one 2015-2017 RCT in 100 villages
  not_good_for:
  - Village-level e-commerce activity or Taobao village identification
  - Per-county subsidy amounts, implementation dates, or program intensity
  - Outcomes or platform sales inside demonstration counties (the lists only say which counties were selected)
  - "The Alibaba 农村淘宝 (Rural Taobao) program: that is a different program run by Alibaba, not the MOFCOM demonstration program"
  needs_join_for:
  - Administrative codes (NBS 行政区划代码; the lists print names only) and boundary changes across 2014-2018
  - County characteristics and outcomes (statistical yearbooks, economic census, fiscal data)
  - Household-level outcomes (CFPS etc.) for welfare analysis
  variation_available:
  - Batch membership in the documented 2014-2018 county lists is a data dimension of this asset; treatment assignment mechanisms and identification threats belong to the Econ-Variation repository
  topics:
  - rural e-commerce
  - e-commerce demonstration program
  - county policy coverage
  - digital divide
  - poverty alleviation
  - rural development

good_for:
- Reproducible county-batch roster for the 2014-2018 program core
- Coverage audit of the national demonstration program
identification:
- >-
  One row is a county name as printed in a particular program batch, paired
  with province and batch year. It is not a county-year outcome, a funding
  record, or a complete 2014-2021 program panel; researcher-created codes and
  post-2018 rows require separate documented work.
linkable_keys:
- Normalized county name (Chinese)
- Province
- Batch year

joins:
- target: cfps
  relation: complement
  keys:
  - County name or county code
  - Survey year
  method: Normalize county names to the NBS code vintage used by CFPS; verify each sample county's code before merging; the lists themselves carry no codes
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - County or prefecture name
  - Year
  method: Join county-level outcomes by normalized name/code; beware boundary changes across batches and yearbook vintages
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - County code or name
  - Census year
  method: Use census county identifiers for demographic controls; verify code vintage
  evidence_status: plausible

access_routes:
- route: MOFCOM official complete roster tables (2014, 2015, 2017)
  access_status: available
  direct_url: https://www.mofcom.gov.cn/zfxxgk/gkml/art/2016/art_249b5fd97b17441dbe52fdc731819254.html
  requirements:
  - Public web access; no account
  steps:
  - Open the current MOFCOM 2014/2015 table (2015-07-14, 市场建设司) and the 2017 MOFCOM table (2017-08-21, 市场体系建设司).
  - Extract the county names by province from the HTML tables (the 2014/2015 combined notice gives 56 + 200 counties; the 2017 notice gives 260 with poverty/old-area flags).
  - Record batch year, province, and printed county name for each row.
  deliverable: Official HTML lists of county names by province for 2014, 2015, and 2017; 56, 200, and 260 printed rows respectively
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    The current central-site pages render the complete 2014/2015, 2017 and 2018
    tables. They do not establish the later 2019-2021 continuation, nor do
    they supply administrative codes.
- route: MOFCOM official 2018 complete roster table
  access_status: available
  direct_url: https://www.mofcom.gov.cn/tjsj/ywtjxxhz/qcltsj/art/2018/art_4d252367fba047418b36965508c1cbe4.html
  requirements:
  - Public web access; no account
  steps:
  - Open the 2018-09-25 MOFCOM roster table and extract province, printed county name, and poverty/old-area columns.
  - Reconcile the extracted rows with the table total of 260 (238 poverty counties and 22 old-area counties).
  deliverable: Official HTML list of 260 county names across 22 provinces, with printed category counts
  cost: free
  last_checked: '2026-09-28'
  caveat: The printed county names still require name-to-code matching; the roster supplies no administrative codes, per-county funding or implementation dates.
- route: MOFCOM 2019/2020 graphic roster notices and 2020 complete-roster statement
  access_status: available
  direct_url: https://www.mofcom.gov.cn/bnjg/art/2019/art_d0464ddb10bd45b3a8f1d21d08a1fd42.html
  requirements:
  - Public web access
  - Manual transcription or an independently checked OCR workflow for graphic-only rosters
  steps:
  - Open the official 2019 roster notice and the 2020 first-batch notice at https://ltfzs.mofcom.gov.cn/ncsytxjs/zcfb/art/2020/art_98c2aa1fb0e840d9973c139cf6a2cd4d.html.
  - Treat their embedded images as source material, not as already machine-readable county rows; transcribe and validate every county against printed totals before a panel is used.
  - For the remainder of 2020, follow the public-channel lead recorded in MOFCOM’s reply https://gzly.mofcom.gov.cn/info/detail?id=11948589f34a4b8c9ff7c553726a55b7&replayId=11948589f34a4b8c9ff7c553726a55b7, then preserve the original post or a government republication alongside any transcription.
  deliverable: Public official roster images for 2019 and the first 2020 batch, plus an official lead to the complete 2020 roster. The 2019 batch total is independently reported as 215 counties (138 国家级贫困县), but no checked text county-row panel is available.
  cost: free
  last_checked: '2026-09-28'
  caveat: The 2019/2020 pages are evidence that official roster publications exist, but the text-accessible page copies do not expose their county rows. The complete 2020 WeChat post and its full roster were not independently retrieved in this work unit.
- route: MOFCOM 2021 program notice (selection framework, not final roster)
  access_status: available
  direct_url: https://ltfzs.mofcom.gov.cn/ncsytxjs/zcfb/art/2021/art_721ea1f57d9e41449e36ac6f3f74279c.html
  requirements: Public web access
  steps:
  - Read the notice for the 2021 program’s scope, provincial selection process, and stated direct inclusion of ten rural-e-commerce incentive counties.
  - Obtain each final provincial or central roster separately before coding county-year exposure.
  deliverable: Official 2021 program and selection documentation, not a finished 2021 county list
  cost: free
  last_checked: '2026-09-28'
  caveat: The notice does not enumerate the final 2021 county roster and cannot by itself support a 2021 county-panel row.
- route: Official government republication for the 2016 batch
  access_status: available
  direct_url: http://swj.trs.gov.cn/ztzl/dzswjnc/201903/t20190306_21835611.html
  requirements:
  - Public web access; no account
  steps:
  - Open the Tongren Municipal Commerce Bureau page 全国2016年电子商务进农村综合示范县名单 (a government-hosted copy of the national list).
  - Extract the 240 county names across 23 provinces/regions.
  - Cross-check counts against the printed 合计 (240).
  deliverable: Full 2016 batch list (240 counties)
  cost: free
  last_checked: '2026-09-28'
  caveat: This is a municipal-government republication of the national list, not the mofcom.gov.cn origin page (which was not located this pass); treat name spellings as the government's official copy.
- route: 贾铖 & 易红梅 (2023) review for the series scope 2014-2021
  access_status: available
  direct_url: https://nyxsj.cbpt.cnki.net/
  requirements:
  - Journal access (CNKI or open PDF if available)
  steps:
  - Use the review as a coverage map of the 示范县库 (2014-2021 county-level) and as a lead for the batches not verified on mofcom this pass.
  deliverable: Secondary coverage map; not a substitute for the official lists
  cost: free
  last_checked: '2026-08-14'
  caveat: The review was fetched 2026-08-14; the CNKI landing page above is the journal home - the exact article URL was not re-verified this pass.

access:
  url: https://ltfzs.mofcom.gov.cn/ncsytxjs/xyfz/art/2015/art_a6ccfaf081f8449d9be6297eb3b2bc39.html
  cost: free
  license: Public government notices; no redistribution restriction observed beyond citing the source
  format:
  - html
  api: false
  how_to_get: Collect the batch notices from MOFCOM official pages and government republications, parse county names, and normalize names/codes to build the county-batch panel.
caveats:
- The lists print county names only: no administrative codes, no per-county funding or dates, no county characteristics.
- The MOFCOM 2019 and first-2020 graphic roster notices are now located, and a MOFCOM reply points to the complete 2020 public WeChat roster; neither fact substitutes for a checked county-row transcription. The 2021 central notice is a selection framework, not its final roster. The MOFCOM origin page for 2016 remains unlocated.
- County names and administrative boundaries changed over 2014-2021 (e.g. 撤县设区, 兵团师市); any panel needs an explicit name-to-code concordance.
- The demonstration program is the MOFCOM/财政部/扶贫办 policy; it is distinct from Alibaba's 农村淘宝 program studied by Couture et al. (2021).

production:
  raw_sources:
  - name: MOFCOM 2014/2015 batch notice (商务部流通业发展司, 2015-07-14)
    source_type: webpage
    role: Official county lists for the 2014 (56) and 2015 (200) batches
    access_route: Direct public page; HTTPS verified 2026-08-14
    url: https://ltfzs.mofcom.gov.cn/ncsytxjs/xyfz/art/2015/art_a6ccfaf081f8449d9be6297eb3b2bc39.html
    coverage: 56 counties/8 provinces (2014) and 200 counties/26 provinces+兵团 (2015)
    last_checked: '2026-08-14'
  - name: MOFCOM 2017 batch notice (市场体系建设司, 2017-08-21)
    source_type: webpage
    role: Official county list for the 2017 batch (260 counties) with poverty/old-area flags
    access_route: Direct public page; HTTPS verified 2026-08-14
    url: https://www.mofcom.gov.cn/tjsj/ywtjxxhz/qcltsj/art/2017/art_26c5c2ea2621478c95cf2ff77f6ac43a.html
    coverage: 260 counties/21 provinces, 237 国家级贫困县 + 23 欠发达革命老区县, 8 整体推进市州
    last_checked: '2026-08-14'
  - name: MOFCOM 2018 complete county roster (市场体系建设司, 2018-09-25)
    source_type: webpage
    role: Official county-name-by-province roster for the 2018 batch
    access_route: Direct public page; rendered and read 2026-09-28
    url: https://www.mofcom.gov.cn/tjsj/ywtjxxhz/qcltsj/art/2018/art_4d252367fba047418b36965508c1cbe4.html
    coverage: 260 counties across 22 provinces; 238 poverty counties and 22 old-area counties
    last_checked: '2026-09-28'
  - name: Tongren Municipal Commerce Bureau republication of the 2016 national list
    source_type: webpage
    role: Government-hosted copy of the 2016 batch list (240 counties)
    access_route: Direct public page; fetched 2026-08-14
    url: http://swj.trs.gov.cn/ztzl/dzswjnc/201903/t20190306_21835611.html
    coverage: 240 counties/23 provinces+兵团 (2016)
    last_checked: '2026-08-14'
  - name: 贾铖 & 易红梅 (2023) 农业大数据学报 5(4):95-102 review of the 示范县库
    source_type: document
    role: Independent review confirming the series is county-level 2014-2021, sourced from 商务部流通发展司
    access_route: CNKI journal access; fetched via the journal site 2026-08-14
    url: https://nyxsj.cbpt.cnki.net/
    coverage: 2014-2021 series-level map
    last_checked: '2026-08-14'
  acquisition_methods:
  - page fetch
  - manual coding
  - document parsing
  sample_construction: "No sampling: the ready core includes every county printed in the documented 2014-2018 batch lists; county rows are defined by (batch year, province, printed county name). The unclosed 2019-2021 continuation is not part of this target panel."
  pipeline_stages:
  - stage: collect
    inputs:
    - MOFCOM batch notices and official republications
    method: Fetch each batch page and save the HTML; verify page identity (issuing unit, date) before parsing.
    tools:
    - HTTPS fetch
    - text extraction
    output: One HTML/text file per batch with the county list
    evidence: Batch pages listed in raw_sources; all verified 2026-08-14
  - stage: parse
    inputs:
    - Batch HTML files
    method: Extract the province rows and county-name strings from the HTML tables; reconcile the row count with the printed 合计.
    tools:
    - HTML parsing
    - manual review
    output: Structured (batch, province, county name) rows
    evidence: Official lists; counts verified against printed totals (56/200/240/260)
  - stage: clean
    inputs:
    - Structured rows
    method: Normalize name variants (县/旗/市/区/林区, historical names, 兵团 divisions), dedupe within batch, flag 整体推进市州 sub-counties.
    tools:
    - Manual coding
    output: Cleaned county-batch records
    evidence: Name normalization is researcher work; the lists themselves print raw names
  - stage: match
    inputs:
    - Cleaned county-batch records
    - NBS administrative-division codes
    method: Match each county name to an administrative code vintage; record the vintage and any unmatchable names (name changes, 撤县设区).
    tools:
    - Manual coding
    - NBS code tables
    output: County-batch panel with admin codes
    evidence: Coding step is researcher work; official lists carry no codes
  - stage: validate
    inputs:
    - County-batch panel
    - Official totals and review coverage statements
    method: Check batch counts against official totals and cross-check coverage with the 2023 review; record unmatched names.
    tools:
    - Manual review
    output: Validated panel with documented coverage gaps
    evidence: Official totals; 贾铖 & 易红梅 (2023)
  constructed_variables:
  - name: batch entry indicator
    concept: Whether/when a county entered the demonstration program
    source_fields:
    - Batch year
    - County name
    method: Indicator = 1 for each county appearing in a batch; a county can appear once per batch (repeated selection across batches is possible in principle; verify per row).
    validation: Compare cumulative counts with MOFCOM news totals (e.g. 1,016 cumulative by 2018).
    limitations: No official machine-readable panel exists; cumulative totals from MOFCOM news are aggregates, not a county roster.
  output:
    unit_of_observation: County-batch row
    structure: Reproducible panel of county-batch selections 2014-2018
    geography: China, county level
    time_span: 2014-2018
    key_variables:
    - Batch year
    - Province
    - County name (Chinese)
    - Admin code (researcher-matched)
    - Poverty/old-area flag where printed (2017+)
    formats:
    - csv
  reproducibility:
    level: medium
    starting_point: MOFCOM batch notices listed in raw_sources; first route is the 2014/2015 origin page
    code_available: false
    code_url: ''
    requirements:
    - Public web access
    - Manual parsing of Chinese county names
    - NBS administrative-division code tables for the code step
    blockers:
    - MOFCOM origin page for 2016 remains unlocated; 2019/2020 rosters require checked transcription from graphic or historic-channel sources, and the 2021 final roster is not in the central notice
    - No official machine-readable index of the full series
  compliance:
    terms_or_license: Public government notices; no observed redistribution restriction
    robots_or_rate_limits: Use normal page access; no bulk scraping of mofcom.gov.cn observed as needed
    personal_or_sensitive_data: None
    redistribution: Cite the MOFCOM source when republishing extracted lists
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Xie Huiqiang, Zhao Ying & Lei Yiming (2025), Research on the impact and mechanism of digital village construction on the integrated development of agriculture and tourism'
  doi: https://doi.org/10.13872/j.1000-0275.2024.0576
  journal: Research of Agricultural Modernization
  year: 2025
  dataset_role: >-
    County-year indicator for entry into the MOFCOM e-commerce-into-rural-areas
    comprehensive-demonstration county list; the paper sets it to one in the
    entry year and thereafter.
  evidence_type: published-paper-full-text
  evidence_url: https://cdn.sciengine.com/doi/pdf/78B62CC0207F48519A8AB26B1BD41018
  data_note: >-
    Open full text, data-source and variable-definition sections read
    2026-09-28: the paper states that its demonstration-county list comes from
    the MOFCOM website; it uses 2009-2020 data for 1,266 counties and codes a
    county as one in and after the year it enters the list. It reports 1,089
    treated counties entering during 2014-2020. This verifies use of the
    county-entry roster, not a downloadable author panel or the completeness
    of post-2017 rosters.
- cite: 贾铖 & 易红梅 (2023) 电子商务进农村综合示范政策研究综述, 农业大数据学报 5(4):95-102
  doi: ''
  journal: 农业大数据学报
  year: 2023
  dataset_role: Review of the demonstration-county series scope (2014-2021 county-level) and program facts
  evidence_type: data-review
  evidence_url: https://nyxsj.cbpt.cnki.net/
  data_note: >-
    Review fetched 2026-08-14; it describes the 示范县库 as a 2014-2021 county-level series sourced from 商务部流通发展司
    and documents the Taobao village/town list series 2009-2022. The review establishes series scope, not the identity
    of any individual research paper's dataset use. No empirical paper using the MOFCOM lists as its core data was
    verified this pass (leads exist in the review's references but were not opened).

provenance:
- source: https://cdn.sciengine.com/doi/pdf/78B62CC0207F48519A8AB26B1BD41018 (Xie, Zhao & Lei 2025, full text read 2026-09-28)
  field_scope:
  - actual paper use of MOFCOM demonstration-county roster
  - county-entry-and-after coding rule
  - 2009-2020, 1,266-county analysis sample and reported 1,089 treated counties
  added: '2026-09-28'
  confidence: high
  verified: true
- source: MOFCOM 2014/2015 notice https://www.mofcom.gov.cn/zfxxgk/gkml/art/2016/art_249b5fd97b17441dbe52fdc731819254.html (rendered and read 2026-09-28)
  field_scope:
  - batch identity and dates
  - county lists 2014/2015
  - issuing unit
  added: '2026-09-28'
  confidence: high
  verified: true
- source: MOFCOM 2017 notice https://www.mofcom.gov.cn/tjsj/ywtjxxhz/qcltsj/art/2017/art_26c5c2ea2621478c95cf2ff77f6ac43a.html (rendered and read 2026-09-28)
  field_scope:
  - 2017 batch list and poverty/old-area flags
  - 整体推进市州 definition
  added: '2026-09-28'
  confidence: high
  verified: true
- source: MOFCOM 2018 news https://www.mofcom.gov.cn/bnjg/art/2018/art_793cf6908e1b4c3b8d7305915882be49.html (fetched and read 2026-08-14)
  field_scope:
  - 2018 batch aggregates
  - cumulative coverage totals
  added: '2026-08-14'
  confidence: high
  verified: true
- source: https://www.mofcom.gov.cn/tjsj/ywtjxxhz/qcltsj/art/2018/art_4d252367fba047418b36965508c1cbe4.html (rendered and read 2026-09-28)
  field_scope:
  - Official 2018 county-name-by-province roster
  - 260 total counties across 22 provinces, including 238 poverty counties and 22 old-area counties
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Tongren Commerce Bureau 2016 list republication https://swj.trs.gov.cn/ztzl/dzswjnc/201903/t20190306_21835611.html (rendered and read 2026-09-28; page attributes source to MOFCOM)
  field_scope:
  - 2016 batch county list
  - 2016 total (240)
  added: '2026-09-28'
  confidence: med
  verified: true
- source: 贾铖 & 易红梅 (2023) review (fetched 2026-08-14, previous pass)
  field_scope:
  - series-level coverage 2014-2021
  - program provenance
  added: '2026-08-14'
  confidence: med
  verified: false
- source: MOFCOM 2019/2020 roster notices, 2020 complete-roster reply, and 2021 program notice (checked 2026-09-28)
  field_scope:
  - official public existence and dates of the 2019 and 2020 first-batch roster notices
  - graphic-only presentation boundary on those text-accessible pages
  - MOFCOM statement that the complete 2020 roster was published through the public 电子商务进农村 WeChat channel
  - 2021 program continuation, selection framework, and the fact that its central notice is not a final county roster
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://snw.yancheng.gov.cn/art/2019/11/27/art_24595_3299823.html (government reporting, read 2026-09-28)
  field_scope:
  - 2019 batch aggregate of 215 counties and 138 国家级贫困县
  - Boundary that the count does not enumerate or verify individual county rows
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-rural-ecommerce-couture-2021-replication
  relation: often-confused-with
- id: cfps
  relation: complement
- id: china-census
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is the official, public, county-name-by-province roster for the reproducible 2014-2018 core of China's national rural e-commerce demonstration program: free to collect from MOFCOM pages and a government republication, and the right raw material for a county-level batch panel. The lists carry no admin codes or program dates. The 2019/2020 graphic rosters and 2021 final roster remain separate extension work, not part of the ready core.

## Select rules

- Prioritize it when the research needs the MOFCOM program's documented 2014-2018 county batches rather than platform-identified e-commerce villages.
- Switch to the Taobao village/town list layer when the question is village-level e-commerce activity identified by Alibaba; switch to the Couture et al. replication corpus when the question needs an RCT evaluation with household microdata in 100 villages.
- Do not use this record for Alibaba's 农村淘宝 program: that is a separate company program.

## Get recipe

1. Fetch the 2014/2015 notice (ltfzs.mofcom.gov.cn; mirror at www.mofcom.gov.cn/zfxxgk/gkml/art/2016/art_249b5fd97b17441dbe52fdc731819254.html), 2017 notice, and 2018 roster (www.mofcom.gov.cn/tjsj/ywtjxxhz/qcltsj/art/2018/art_4d252367fba047418b36965508c1cbe4.html). The 2018 table was verified live 2026-09-28.
2. Fetch the 2016 national list from the Tongren Commerce Bureau republication (swj.trs.gov.cn) — the mofcom origin page was not located.
3. Parse county names by province, normalize names, and match to an explicitly chosen NBS administrative-code vintage; validate each of the five core batches against its printed total (56, 200, 240, 260, 260).
4. If the question needs 2019-2021, stop the ready-core route here: transcribe the located official graphic rosters only after retaining their original pages and validating totals, and obtain a final 2021 roster separately. Do not silently append aggregate counts as county rows.

## Connections and Limitations

The join unit is county with batch year; the lists themselves print Chinese names only, so every join to surveys (CFPS), censuses, or yearbooks requires an explicit name-to-code concordance with a recorded vintage. The ready boundary is the complete 2014-2018 core (1,016 printed county-batch rows across the five batches), not a machine-readable provider file and not a promise that every later-year roster is obtainable. The 2019-2020 transcription and 2021-final-roster gaps remain the main extension limits. The program's assignment mechanism and identification threats are variation knowledge that belongs to the Econ-Variation repository, not this data record.
