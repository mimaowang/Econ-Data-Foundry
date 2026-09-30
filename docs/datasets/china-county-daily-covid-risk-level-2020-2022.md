---
schema_version: 3
catalog_status: ready
id: china-county-daily-covid-risk-level-2020-2022
name: "County-daily COVID-19 Risk Level panel from the State Council risk-level directory (paper release: combined_data_1215_revisitJan012024.xlsx, CER 2024 zero-COVID study)"
aka:
- 全国中高风险地区名单
- 疫情风险等级
- 中高风险地区
- COVID risk level county panel
- 国务院客户端 疫情风险等级查询
- bmfw.www.gov.cn/yqfxdjcx/risk.html
provider: "Composite: the classification framework is 国务院联防联控机制 (State Council Joint Prevention and Control Mechanism, 指导意见 issued 2020-02-17); county-list updates were the duty of 各省级人民政府 per that framework; the national daily directory of 中高风险地区 was aggregated in the 国务院客户端 (State Council client app) / 国家政务服务平台 (bmfw.www.gov.cn/yqfxdjcx/risk.html). The released panel file is the paper authors' own GitHub release (dadasmash/China_COVID_Risk_Level_Dataset; contributors Da Gong, Andong Yan, Qi Zhang - matching authors of CER 2024, DOI 10.1016/j.chieco.2023.102101; the repo README asks users to cite that article)."
china_related: true
domains:
- health
- covid-19
- spatial
- urban
- regional
- public-policy

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: "Two distinct artifacts. (a) RELEASED PANEL (verified download): combined_data_1215_revisitJan012024.xlsx from the authors' GitHub - 62,027 rows x 16 columns, county-day observations with 0/1 flags high_risk/mid_risk/low_risk, coverage 2021-04-02..2022-12-15, 31 provinces, up to ~1,231 counties per day (rows exist only for county-days that appear in the risk directory; 'unlisted county-date is defined as county without _Risk_ at the given date' per the repo README). (b) PUBLIC ANNOUNCEMENT SERIES (reconstruction raw material, partially headless-fetchable): 联防联控机制 framework document (gov.cn, 200), provincial/city risk-level adjustment announcements (e.g., henan.gov.cn 商丘市通告 series, 200), and provincial health-commission daily republications of the national 中高风险地区 list (e.g., wjw.guizhou.gov.cn, 200); the national directory itself (bmfw.www.gov.cn) is TLS-blocked from this environment and per the authors' scrape log expired 2022-12-16."
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: "The county-day COVID risk-level panel behind CER 2024's zero-COVID study is directly downloadable from the paper authors' GitHub repo (dadasmash/China_COVID_Risk_Level_Dataset), and I verified the actual xlsx: 62,027 county-day rows, 2021-04-02..2022-12-15, flags high_risk/mid_risk/low_risk, county admin codes (PAC/NAME/省/市/类型), 31 provinces. The underlying public series exists and is partly headless-fetchable: the 2020-02-17 联防联控机制 指导意见 (county-level 低/中/高风险 framework, provincial governments update county lists) on gov.cn; serialized city-level 关于调整疫情风险等级的通告 (e.g., 商丘 2021年第25号 on henan.gov.cn); provincial health-commission daily 疫情信息发布 with 附全国中高风险地区 (Guizhou example); the national directory aggregated in the 国务院客户端/国家政务服务平台 (mini-program; bmfw.www.gov.cn TLS-blocked here, and the authors record the page expired 2022-12-16). Honest gaps: the released cleaned file covers 2021-04-02..2022-12-15 - NOT the 2020-2022 window of the abstract; paper-use evidence remains abstract-level (article full text untouched per unit boundary); the repo has NO license; the released file contains 11,986 duplicate (county,date) rows; sub-county 中高风险地区 listings (streets/communities/compounds from late 2020 onward) require mapping to counties if a researcher rebuilds the panel from raw announcements."
  barrier: "None for the released authors' file (public GitHub download, no license though). For rebuilding from raw announcements: no single national machine-readable series exists - the daily directory lived in the 国务院客户端 mini-program / bmfw.www.gov.cn (expired 2022-12-16 per the authors; TLS-blocked in this environment), and daily snapshots must be recompiled from provincial mirrors or third-party archives."

unit_of_observation: "County-day (released file rows = county-days present in the State Council risk directory; author README: 'Unlisted county-date is defined as county without _Risk_ at the given date')"
structure: "Panel (sparse: not every county appears every day; 62,027 rows over ~623 days; up to ~1,231 counties/day, 1,740 distinct county names / 1,711 distinct PAC codes)"
geo_granularity:
- county (市辖区/县/县级市/旗/自治县/自治旗/林区; 类型 column also contains 地级市 entries - 996 rows - not interpreted here)
geography: "China, 31 province-level units; county units incl. 新疆 production-corps cities (e.g., 石河子市) with missing 市代码 in some rows"
time_span:
  start: '2021-04-02'
  end: '2022-12-15'
  last_confirmed_release: '2026-09-28 (author README and direct xlsx route rechecked; repo last push 2024-02-22)'
  coverage_note: "Released cleaned file: 2021-04-02..2022-12-15 (author README: official reporting ended 2022-12-26; last ~10 days' raw data exist but were not cleaned; 卫健委 stopped daily publication 2022-12-25 per readme.txt). The current CER publisher page independently describes daily county/prefecture risk data from April 2021 through December 2022. The study discusses 2020-2022 impacts, but that broader study horizon does not establish released risk observations for 2020 or Jan-Mar 2021."
  last_checked: '2026-09-28'
frequency:
- daily (released file; announcements were updated multiple times per day in some periods - the authors used a fixed daily snapshot time point, proxying 2022-05-14 with the 05-15 00:00 snapshot per readme.txt)
sample_size: "62,027 county-day rows (released xlsx); 31 provinces; 1,740 county names; 4,474 duplicate (county,date) groups of which 2,942 have identical flags across rows"
key_variables:
- "date (2021-04-02..2022-12-15)"
- "high_risk / mid_risk / low_risk (0/1 flags: county has >=1 sub-area at that risk level on that date; encoding semantics per author README + readme.txt: before 2022-07-21 unlisted regions = low risk; 2022-07-21+ the directory listed high/mid/low with unlisted = 常态化防控区域; 2022-11-15/16+ only high/low categories)"
- "county, prov (Chinese names), PAC (6-digit county admin code; 1,378 NaN), NAME, 省代码, 省, 市代码 (98 NaN), 市, 类型 (county type), pref, _ID"
- "Treatment-construction advice in README: high_risk/mid_risk/low_risk can generate own treatment variables; 4 adjustments to the high/mid/low criteria are recorded in readme.txt"

research_fit:
  best_for:
  - "County-day measurement of the zero-COVID risk-level regime (which counties were designated high/medium risk on which days) for 2021-04..2022-12, as the treatment/event layer of COVID-policy economic-impact studies"
  - "Immediate reuse of the paper's own cleaned panel (authors' GitHub file) when the design window fits 2021-04-02..2022-12-15 and county-day granularity suffices"
  - "Reconstructing daily risk-state panels from public announcements (framework doc + provincial 通告 + health-commission daily lists) when a longer or custom window is needed"
  choose_over:
  - "Choose the released authors' file over rebuilding from announcements when 2021-04..2022-12 coverage suffices - rebuilding requires daily snapshots of a directory that is no longer online (expired 2022-12-16) and sub-county-to-county mapping"
  - "For mobility outcomes of the same COVID era use china-amap-migration-flow-indices (city-dyad daily indices, provider-run public page) - different construct and granularity, join by date/city only after normalization"
  - "For economic-activity outcomes of the same paper use china-nighttime-lights and china-satellite-pm25 grids (aggregate to county); the risk panel is the policy-state layer, not an activity measure"
  not_good_for:
  - "2020 or Jan-Mar 2021 risk states from the released file (starts 2021-04-02; the abstract's 2020-2022 window is not covered by the release)"
  - "Sub-county (street/community/compound) granularity: the released panel is already county-aggregated; raw 中高风险地区 listings name streets/communities"
  - "Case counts or epidemic severity: the risk directory captures policy designation, and per the authors' readme.txt it only reflects the strictest quarantine policies in some waves (Shanghai 2022 lockdown = 0 high-risk days; Ruili/Jilin anomalies recorded by the authors)"
  - "Current (post-2022) risk states: the directory expired 2022-12-16; only the WeChat mini-program remained, showing nothing for Beijing by 2022-12-24 per readme.txt"
  - "Paper-side inference: the article's exact panel (possibly 2020-extended), outcome construction and GDP-loss estimates are not reproducible from this record alone (paper use still abstract-level)"
  needs_join_for:
  - "Outcome layers of the same study: NTL grids (china-nighttime-lights) and PM2.5 grids (china-satellite-pm25) aggregated to county; mobility layer (china-amap-migration-flow-indices, prefecture-level) - all at abstract-level identity for this paper"
  - "County boundary shapefiles for mapping 中高风险地区 sub-units to counties if rebuilding (author README notes county.shp/pref.shp were excluded from the repo; 'publicly available on the internet' or by email)"
  - "Policy-timing/treatment interpretation belongs to the variation repository (Econ-Variation), not this data record"
  variation_available:
  - "Daily temporal variation in risk designations 2021-04-02..2022-12-15; cross-county spatial variation within 31 provinces"
  - "Regime changes within the window: 4 documented criteria adjustments (2022-07-21 high/mid/low + 常态化防控区域; 2022-11-15/16 high/low only) usable as design breaks with caution"
  topics:
  - COVID-19
  - zero-COVID policy
  - risk level
  - county panel
  - public health policy
  - lockdown

good_for:
- County-day zero-COVID risk-state panels (released 2021-04..2022-12)
- Treatment/event layer for COVID economic-impact studies at county granularity
identification:
- Daily county-level policy-state variation; no causal identification is supplied by the data itself
linkable_keys:
- County name (Chinese) + date
- PAC 6-digit county admin code (1,378 NaN rows)
- 省/市 Chinese names and codes

joins:
- target: china-amap-migration-flow-indices
  relation: complement
  keys:
  - date
  - prefecture city (市 name; AMAP is prefecture-level, risk panel is county-level - aggregate risk panel to prefecture or map AMAP indices to counties with weights)
  method: "Overlap check (2026-08-15, canonical records read): AMAP = city-dyad DAILY migration intensity indices (Gaode LBS users, 365 prefecture cities, provider-run public page); risk panel = county-day administrative risk-designation flags (paper-constructed from the State Council directory). Different unit (city-dyad vs county-day), different construct (mobility intensity vs policy risk state). The CER paper's 'population mobility' layer is unnamed at abstract level - whether it is AMAP is unverified."
  evidence_status: plausible
- target: china-nighttime-lights
  relation: complement
  keys:
  - county (after zonal aggregation of grids)
  - year/month vs day (aggregate risk flags to month/year or NTL to daily where possible)
  method: "Overlap check (2026-08-15, canonical record read): NTL = gridded annual/monthly composites (DMSP 1992-2013, VIIRS 2012+, PANDA/harmonized), unit = grid cell; risk panel = county-day policy state. Same paper (CER 102101) uses NTL as economic-activity outcome ('satellite data on night lights', abstract-level; exact product/version unresolved - same status as the RSUE 104246 entry in the NTL record). Complementary roles: treatment layer (risk) vs outcome layer (NTL)."
  evidence_status: plausible
- target: china-satellite-pm25
  relation: complement
  keys:
  - county (zonal aggregation)
  - month/year
  method: "CER abstract names 'satellite data on night lights and PM2.5' as activity measures (abstract-level; PM2.5 product identity unverified - likely the canonical china-satellite-pm25 grid family but not read for this paper)."
  evidence_status: plausible

access_routes:
- route: "Paper authors' GitHub release (dadasmash/China_COVID_Risk_Level_Dataset) - direct download of the cleaned panel"
  access_status: available
  direct_url: https://github.com/dadasmash/China_COVID_Risk_Level_Dataset
  requirements:
  - "None (public GitHub; raw.githubusercontent.com worked headless 2026-08-15)"
  steps:
  - "Download combined_data_1215_revisitJan012024.xlsx (3.95 MB; README.md mentions the .csv form; the repo tree shows the .xlsx)"
  - "Read readme.md + readme.txt for encoding semantics and the 4 criteria adjustments before using the flags"
  - "Deduplicate (county,date) rows before use: 11,986 of 62,027 rows are duplicates of a (county,date) key (4,474 groups; 2,942 with identical flags)"
  - "Request county.shp/pref.shp from the authors by email if boundaries are needed (not in repo)"
  deliverable: "62,027-row county-day panel, 2021-04-02..2022-12-15, flags high_risk/mid_risk/low_risk + admin codes"
  cost: free
  last_checked: '2026-09-28'
  caveat: "Current author README still names the data file and requests citation of CER 102101; the direct xlsx route returns HTTP 200 (3,946,284 bytes). No LICENSE file or reuse permission was established, so downloadability does not settle redistribution or publication-use rights. Repo last pushed 2024-02-22; README last updated Jan 2024."
- route: "Official current-state directory: 国家政务服务平台 各地疫情风险等级查询 (国务院客户端)"
  access_status: blocked
  direct_url: https://bmfw.www.gov.cn/yqfxdjcx/risk.html
  requirements:
  - "Environment block: TLS handshake fails headless (SSL EOF, both https and http, 2026-08-15); page also recorded as EXPIRED 2022-12-16 by the paper's own scrape log (readme.txt)"
  steps:
  - "Human browser / WeChat mini-program '国务院客户端 疫情风险等级查询' (per app.www.gov.cn 2022-04-26 article: 按省/市筛选, 一键复制); current snapshot only, no history"
  deliverable: "Current 中高风险地区 list (sub-county granularity), not historical series"
  cost: free
  last_checked: '2026-08-15'
  caveat: "Current-state only; history unverifiable headless; environment TLS block is not evidence of absence for the mini-program"
- route: "Provincial health-commission daily republication of the national list (e.g., 贵州省卫健委 疫情信息发布 附全国中高风险地区)"
  access_status: available
  direct_url: https://wjw.guizhou.gov.cn/xwzx/gzdt/202112/t20211222_78924315.html
  requirements:
  - "None (fetched 200 headless 2026-08-15); series is daily 疫情信息发布 with the national 中高风险地区 list appended, sourced from 国务院客户端 目录调整"
  steps:
  - "Scan the 工作动态/新闻中心 column for daily entries (2020-12..2022-12); extract the appended national list (province -> city -> district/street/community)"
  - "Map sub-county units to counties with boundary/admin-code data for county-day reconstruction"
  deliverable: "Daily national 中高风险地区 lists, sub-county granularity, for the province's publication span"
  cost: free
  last_checked: '2026-08-15'
  caveat: "One province's mirror covers the national list but only for the days it published; reconstructing a full 2020-2022 series requires multiple mirrors + archives"
- route: "Provincial/city serialized risk-adjustment 通告 (e.g., 商丘市新冠肺炎疫情防控指挥部 关于调整疫情风险等级的通告)"
  access_status: available
  direct_url: https://www.henan.gov.cn/2021/08-31/2303966.html
  requirements:
  - "None (fetched 200 headless 2026-08-15; example is 商丘市通告 2021年第25号 reposted on henan.gov.cn, 来源：商丘市卫健委)"
  steps:
  - "Collect 通告 by city/province for the study window; each 通告 lists specific sub-county units (医院院区/村/社区) and their risk-level changes"
  deliverable: "Event-level risk-adjustment records (sub-county granularity) for the covered cities"
  cost: free
  last_checked: '2026-08-15'
  caveat: "Fragmented: no single national series; each 通告 is a separate document; county-level era (Feb-Apr 2020) documents exist per the framework but provincial pages (e.g., scjg.hubei.gov.cn repost of 湖北县级风险等级评估) return 412 anti-bot to headless clients"
- route: "Third-party archives of the daily 中高风险地区 lists (community-maintained)"
  access_status: available
  direct_url: https://github.com/sunbqxyz/china_covid_riskareas_history
  requirements:
  - "None (GitHub API metadata + README fetched 2026-08-15); README: 2020-07-29..2022-04-15, 625 days, ~4k risk areas / 35k records, json with [省,市,县,详细地址], built from 贵州/浙江/江苏卫健委 raw texts; 8 days hand-entered; geocoding via AMAP API"
  steps:
  - "Use as a supplementary daily-list archive for the early window (2020-07..2022-04) that the released county panel does not cover"
  - "Cross-check against official mirrors before relying on it"
  deliverable: "Area-level daily risk records (hlist/mlist + hcount/mcount) 2020-07-29..2022-04-15"
  cost: free
  last_checked: '2026-08-15'
  caveat: "NO license; community-maintained with documented quality caveats (e.g., source inconsistency 210808 武汉条目, count-consistency-only validation); related repos: panghaibin/RiskLevelAPI (archived, latest-list API, homepage risk-region.ml), KaikePing/RiskLevel (2021-08..10 daily-change recorder, Python)"

access:
  url: https://github.com/dadasmash/China_COVID_Risk_Level_Dataset
  cost: free
  license: "None stated (no LICENSE file; author README requests citation of CER 2024 102101); official directory and announcements are government public information"
  format:
  - xlsx
  api: false
  how_to_get: "Direct download of combined_data_1215_revisitJan012024.xlsx from the authors' GitHub (verified headless 2026-08-15); for rebuilt panels, compile daily snapshots from provincial health-commission mirrors + 通告 series + third-party archives (all unlicensed) - the official bmfw.www.gov.cn directory is expired (2022-12-16) and TLS-blocked from this environment."
caveats:
- "Released file covers 2021-04-02..2022-12-15 - NOT the abstract's 2020-2022 window; whether the in-paper panel extends to 2020 (e.g., from the Feb-Apr 2020 county-level 名单 era) is unread (Elsevier 403; paper-use evidence abstract-level per unit boundary)."
- "11,986 duplicate (county,date) rows in the released xlsx (4,474 groups; 2,942 identical-flag groups) - dedupe before use; Dec-2022 rows especially noisy (author: data format changed after switching to Beijing BendiBao on 2022-12-16)."
- "Flag semantics changed 4 times within the window (author readme.txt): pre-2022-07-21 unlisted = low risk; 2022-07-21+ high/mid/low listed, unlisted = 常态化防控区域; 2022-11-15/16+ only high/low. Treat flags as 'county has >=1 area at that level' - not mutually exclusive categories."
- "The risk directory only captured the strictest quarantine policies in some waves (author readme.txt: Shanghai 2022 full lockdown recorded 0 high-risk days; Ruili 'COVID-0' claim vs continued quarantine; Jilin anomaly)."
- "No license on the authors' repo; community archives are also unlicensed."
- "Upload_Large_File_Medium.pdf (7.03 MB) sits in the authors' repo - content NOT inspected this unit (paper-use evidence deliberately kept abstract-level)."
- "Shapefiles county.shp/pref.shp are not in the repo (GitHub size limits; available 'on the internet' or by email per README)."
- "Elsevier/CER full text remains 403 for automated clients (known); no claim about the paper's in-paper construction details is made beyond the abstract and the authors' READMEs."

production:
  raw_sources:
  - name: 国家政务服务平台 / 国务院客户端 疫情风险等级查询 (全国中高风险地区目录)
    source_type: webpage
    role: "Daily snapshot source of the paper's panel (author readme.txt); URL bmfw.www.gov.cn/yqfxdjcx/risk.html; page expired 2022-12-16; WeChat mini-program remained"
    access_route: "TLS-blocked headless (2026-08-15); author scraped it live during 2021-2022"
    url: https://bmfw.www.gov.cn/yqfxdjcx/risk.html
    coverage: "National 中高风险地区 list, daily snapshots, sub-county granularity, 2020-12..2022-12 (directory era)"
    last_checked: '2026-08-15'
  - name: 国务院联防联控机制《关于科学防治精准施策分区分级做好新冠肺炎疫情防控工作的指导意见》(2020-02-17)
    source_type: webpage
    role: "Framework establishing county (县市区旗) 低/中/高风险 classification; provincial governments to dynamically adjust county lists"
    access_route: "gov.cn repost of 新华社 text, fetched 200 headless 2026-08-15"
    url: https://www.gov.cn/xinwen/2020-02/18/content_5480514.htm
    coverage: "2020-02 framework; county-level era"
    last_checked: '2026-08-15'
  - name: Beijing BendiBao 风险名单 mirror (m.bj.bendibao.com/news/gelizhengce/fengxianmingdan.php)
    source_type: webpage
    role: "Author's fallback scrape source after the State Council page expired (2022-12-16..12-24); different data format"
    access_route: "Not fetched this unit (documented in author readme.txt)"
    url: http://m.bj.bendibao.com/news/gelizhengce/fengxianmingdan.php
    coverage: "2022-12-16..12-24"
    last_checked: ''
  acquisition_methods:
  - crawl
  - download
  sample_construction: "Author (readme.txt): daily snapshot at a fixed time point; 2022-05-14 proxied by the 2022-05-15 00:00 update ('they did not update on 2022-05-14'); unlisted county-date = no _Risk_ (README); rows present only for listed county-days in the released file"
  pipeline_stages:
  - stage: collect
    inputs:
    - bmfw.www.gov.cn/yqfxdjcx/risk.html daily snapshots (2021-04..2022-12-15); Beijing BendiBao after 2022-12-16
    method: "Daily scrape of the State Council risk directory; fallback mirror in Dec 2022 (author readme.txt)"
    tools: []
    parameters:
      snapshot_time: "fixed daily time point (05-15 00:00 proxy for 05-14)"
    output: "Daily 中高风险地区 lists (sub-county units)"
    evidence: "dadasmash/China_COVID_Risk_Level_Dataset readme.txt (author's own scrape log)"
  - stage: aggregate
    inputs:
    - Daily sub-county risk lists
    method: "Aggregate sub-area designations to county-day flags high_risk/mid_risk/low_risk (county has >=1 area at that level); encode unlisted = no risk"
    tools: []
    parameters: {}
    output: "County-day panel (released xlsx)"
    evidence: "Repo README.md + readme.txt (encoding notes, 4 criteria adjustments); exact aggregation rule for the paper's in-paper panel unread"
  constructed_variables:
  - name: high_risk / mid_risk / low_risk
    concept: "County-level daily risk-state flags from the State Council 中高风险地区 directory"
    source_fields:
    - daily sub-county risk listings
    method: "County = 1 at level L if any of its sub-units was listed at level L that day; unlisted = no risk (README); criteria changed 4 times (readme.txt)"
    validation: "Author's own caveats: Shanghai 2022 lockdown 0 high-risk days (captures strictest policies only); Ruili/Jilin anomalies; 2022-05-14 proxied"
    limitations: "Not a mutually exclusive coding across categories; low_risk always 1 for listed counties pre-2022-07-21 (unlisted = low by definition); 2022-11-15+ only high/low"
  validation: []
  output:
    unit_of_observation: "County-day"
    structure: "Sparse panel, 62,027 rows"
    geography: "China, 31 provinces"
    time_span: "2021-04-02..2022-12-15 (released cleaned file)"
    key_variables:
    - date
    - county
    - high_risk
    - mid_risk
    - low_risk
    - PAC
    - 省/市 codes and names
    formats:
    - xlsx
  reproducibility:
    level: high
    starting_point: "Authors' GitHub xlsx (direct download, verified); or rebuild from the framework doc + provincial 通告/卫健委 daily lists + third-party archives"
    code_available: false
    code_url: null
    requirements:
    - "Dedupe + flag-semantics handling (4 criteria changes) if using the released file"
    - "For rebuilding: daily snapshots of a directory that no longer exists -> provincial mirrors + archives; county mapping for sub-county units; boundary shapefiles (not in repo)"
    blockers:
    - "No scraping code or shapefiles released by the authors"
    - "2020-01..2021-03 county-day coverage not in the release (county-level-era lists are fragmented across provincial pages, several anti-bot 412 headless)"
  compliance:
    terms_or_license: "No license on the authors' repo (citation requested); government announcements are public information; community archives unlicensed"
    robots_or_rate_limits: "GitHub download normal use; official directory expired; provincial mirrors fetched once each (no bulk crawling attempted)"
    personal_or_sensitive_data: "None (aggregated administrative designations of places, not persons)"
    redistribution: "Unstated for the released file; cite CER 2024 102101 per author README"
    review_needed: true

quality:
  profile_status: verified
  access_status: available
  paper_use_status: partial
  last_audited: '2026-09-28'

used_by:
- cite: "Gong, Da; Shang, Zhuocheng; Su, Yaqin; Yan, Andong; Zhang, Qi (2024) Economic impacts of China's zero-COVID policies. China Economic Review 83:102101"
  doi: 10.1016/j.chieco.2023.102101
  journal: China Economic Review
  year: 2024
  dataset_role: "Main explanatory/event layer (county-daily COVID-19 Risk Level panel)"
  evidence_type: abstract-only
  evidence_url: https://ideas.repec.org/a/eee/chieco/v83y2024ics1043951x23001864.html
  data_note: "Abstract (IDEAS article page, 200, cached 2026-08-15): 'an original county-daily panel data set on the COVID-19 Risk Level issued by the State Council of the People's Republic of China' for 2020-2022; outcomes = satellite night lights, PM2.5, population mobility; zero-COVID 2022: mobility -30%, PM2.5 -1.17%, NTL -7.7%, GDP -3.9%. The authors' own GitHub release (README cites this exact article) is the data-level confirmation; the article's full text and in-paper construction details were NOT read (Elsevier 403 for automated clients; unit boundary kept paper-use evidence abstract-level)."

provenance:
- source: "gov.cn/xinwen/2020-02/18/content_5480514.htm (新华社 text of 联防联控机制 指导意见, fetched 200 2026-08-15, cached govcn_20200218_fenfengji_guidance.*)"
  field_scope:
  - framework existence (county-level 低/中/高风险 classification)
  - provincial duty to update county lists
  - issue date 2020-02-17
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "GitHub dadasmash/China_COVID_Risk_Level_Dataset: API metadata + README.md + readme.txt + combined_data_1215_revisitJan012024.xlsx (all fetched 2026-08-15; xlsx inspected with pandas)"
  field_scope:
  - author identity of the release (Gong/Yan/Zhang, matching CER 2024)
  - released file existence, columns, row count, date range, provinces
  - scrape source (bmfw.www.gov.cn), snapshot protocol, criteria changes, expiry 2022-12-16
  - duplicate rows and NaN admin codes (my inspection)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "wjw.guizhou.gov.cn/xwzx/gzdt/202112/t20211222_78924315.html (贵州卫健委 daily 疫情信息发布 with 附全国中高风险地区, fetched 200 2026-08-15)"
  field_scope:
  - provincial republication of the national list (sub-county granularity)
  - source attribution to 国务院客户端 目录调整
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "henan.gov.cn/2021/08-31/2303966.html (商丘市防控指挥部 关于调整疫情风险等级的通告 2021年第25号 repost, fetched 200 2026-08-15)"
  field_scope:
  - serialized city-level 通告 series existence (sub-county adjustments)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "app.www.gov.cn/govdata/gov/202204/26/484335/article.html (国务院客户端 中高风险地区名单查询 feature, fetched 200 2026-08-15)"
  field_scope:
  - national directory aggregation in 国务院客户端 mini-program
  - 按省/市筛选 + 一键复制 features (current-state only)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "GitHub API metadata + README for sunbqxyz/china_covid_riskareas_history, panghaibin/RiskLevelAPI, KaikePing/RiskLevel (fetched 200 2026-08-15)"
  field_scope:
  - third-party daily-list archives and their coverage/sources (supplementary route only)
  added: '2026-08-15'
  confidence: med
  verified: true
- source: "IDEAS article page for 10.1016/j.chieco.2023.102101 (cached 2026-08-15 by the CER/JDE recovery unit; abstract + authors)"
  field_scope:
  - abstract-level paper use
  - author names
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "Blocked routes this unit: bmfw.www.gov.cn (TLS SSL EOF, https+http, 2026-08-15); scjg.hubei.gov.cn repost of 湖北县级风险等级评估 (412 anti-bot); gov.cn sousuo API (code 1001/no results, consistent with grounding-b14 record)"
  field_scope:
  - negative route evidence (environment blocks, not absence)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: "Current author GitHub README and direct xlsx route; CER publisher page (checked 2026-09-28)"
  field_scope:
  - current public author README naming the data file, 2021-04-02..2022-12-15 range, contributors and requested citation to CER 102101
  - current direct xlsx availability (HTTP 200, 3,946,284 bytes)
  - publisher description of daily county/prefecture risk data from April 2021 through December 2022
  - distinction between the released panel and the study's broader 2020-2022 horizon
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-amap-migration-flow-indices
  relation: complement
- id: china-nighttime-lights
  relation: complement
- id: china-satellite-pm25
  relation: complement
---

## Positioning in one sentence

The county-day COVID risk-level panel linked by the CER 2024 authors is directly downloadable from their GitHub: a verified 62,027-row county-day file (2021-04-02..2022-12-15) with high/mid/low-risk flags built from daily State Council-directory snapshots. It is ready for that released window, not a claim that the paper's broader 2020-2022 study horizon or every original raw snapshot is publicly supplied.

## Select rules

- Use the released authors' file directly when the design window fits 2021-04-02..2022-12-15 and county-day policy-state granularity is what the research needs - no scraping required, but dedupe the 11,986 duplicate (county,date) rows and respect the 4 criteria changes documented in readme.txt.
- For 2020 or Jan-Mar 2021 risk states, the release does not cover them: rebuild from the 联防联控机制 framework (county-level era, Feb-Apr 2020) + provincial 通告/卫健委 daily lists + third-party archives (sunbqxyz covers 2020-07-29..2022-04-15 at area level), or extend the authors' data.
- Switch to china-amap-migration-flow-indices for mobility outcomes and china-nighttime-lights / china-satellite-pm25 for activity outcomes - the risk panel is the policy-state layer, not an activity or mobility measure.
- Do not use this record for case counts, for sub-county granularity, for post-2022 risk states, or as proof that the direct release includes 2020 or the paper's complete final analysis panel.

## Get recipe

1. Download https://github.com/dadasmash/China_COVID_Risk_Level_Dataset (raw.githubusercontent.com/master/combined_data_1215_revisitJan012024.xlsx works headless; verified 2026-08-15).
2. Read readme.md and readme.txt first: they define the unlisted-county rule and the 4 criteria adjustments (2022-07-21, 2022-11-15/16, Dec-2022 format switch).
3. Deduplicate (county,date) rows (11,986 duplicates), handle 1,378 missing PAC / 98 missing 市代码, and decide how to treat the non-mutually-exclusive flags.
4. If a longer window (2020) or independent rebuild is needed: start from the framework doc (gov.cn/xinwen/2020-02/18/content_5480514.htm), then collect provincial 通告 (e.g., henan.gov.cn series) and health-commission daily lists (e.g., wjw.guizhou.gov.cn 疫情信息发布 附全国中高风险地区), and cross-check against the sunbqxyz third-party archive (2020-07-29..2022-04-15). Note the official bmfw.www.gov.cn directory is expired and TLS-blocked from headless environments; a human browser can still reach the 国务院客户端 mini-program for current-state queries only.
5. For the same paper's outcome layers, aggregate china-nighttime-lights and china-satellite-pm25 grids to counties; the mobility layer is unnamed at abstract level.

## Connections and Limitations

- County-day flag semantics changed within the window; treat flags as 'county has at least one area at that level', not exclusive categories; low_risk is uninformative pre-2022-07-21 (unlisted = low by definition).
- Measurement caveats from the authors themselves: the directory captured only the strictest quarantine policies in some 2022 waves (Shanghai 0 high-risk days under full lockdown; Ruili/Jilin anomalies); 2022-05-14 is proxied by the 05-15 00:00 snapshot.
- No license on any of the GitHub artifacts (paper release and community archives); citation is requested for the paper release, but reuse/redistribution permission remains unresolved.
- Join to AMAP mobility at prefecture level (city-dyad) and to NTL/PM2.5 grids via county zonal aggregation; boundary shapefiles are not in the repo (email the authors).
- The paper's broader 2020-2022 study horizon does not make 2020/early-2021 risk rows part of the direct release; do not assume the paper's complete final analysis panel equals this public file.

## Decision sufficiency check

A researcher can now obtain the paper-linked county-day panel by direct download, confirm its named file and dates through the authors' current README and the publisher's April-2021-to-December-2022 description, and choose it for a 2021-04..2022-12 county-day risk-state question. They can also see the decision boundaries before use: duplicates, changing flag semantics, missing 2020/early-2021 coverage, no bundled shapefiles, no redistribution licence, and no evidence that this file is the paper's complete final analysis panel. Those unknowns narrow the recommendation; they do not prevent acquisition of the documented released asset.
