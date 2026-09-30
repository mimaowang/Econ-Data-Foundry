---
schema_version: 3
catalog_status: ready
id: china-pku-digital-financial-inclusion-index
name: Peking University Digital Financial Inclusion Index of China (PKU-DFIIC, 北京大学数字普惠金融指数)
aka:
- PKU-DFIIC
- 北大数字普惠金融指数
- 北京大学数字金融研究中心数字普惠金融指数
- The Peking University Digital Financial Inclusion Index of China
provider: 北京大学数字金融研究中心 (PKU Institute of Digital Finance, idf.pku.edu.cn) 课题组，与蚂蚁集团研究院合作编制；课题组成员郭峰、王靖一、曹友斌、程志云、李勇国、王芳，顾问黄益平（中心主任）、李振华（蚂蚁集团研究院院长）
china_related: true
domains:
- finance
- digital-economy
- regional
- urban
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Official free download of the index workbook: an XLSX with six sheets
    (数据说明/Note, Regionalism_Code, Provinces, Prefecture_Level_Cities, Counties)
    plus the 52-page index report PDF 北京大学数字普惠金融指数（2011-2023）.
    The Provinces sheet has 403 province-year rows (31 provinces x 2011-2023),
    Prefecture_Level_Cities 4,369 city-year rows (2011-2023), Counties 26,090
    county-year rows (2014-2023) - all verified by opening the downloaded file
    on 2026-08-15.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The standard, freely downloadable regional digital-financial-inclusion panel for
    mainland China: annual index values at province, prefecture-city and county level,
    built by the PKU Institute of Digital Finance with Ant Group from Ant's desensitized
    digital-finance big data. The current official release covers 2011-2023 for
    provinces/cities and 2014-2023 for counties. The underlying Ant microdata is
    proprietary and never released; the released product is the compiled index.
  barrier: >-
    No registration or fee on the official page; citation of the compilation paper
    (郭峰 et al. 2020, 经济学（季刊）19(4)) is requested. Geographic codes use specific
    administrative-division vintages (city codes labeled year18/year14, county codes
    year14), so joins to other datasets need vintage alignment.

unit_of_observation: Region-year (province-year / prefecture-city-year / county-year) index observations
structure: Annual panel by administrative region and year, with the aggregate index and sub-indices in wide columns per row
geo_granularity:
- province
- prefecture-level city
- county
geography: >-
  Mainland China: 31 provinces (municipalities/autonomous regions), 337 prefecture-level
  and above cities (regions, autonomous prefectures, leagues), and about 2,800 counties
  (county-level cities, banners, municipal districts). Hong Kong SAR, Macao SAR and
  Taiwan province are excluded per the workbook data notes.
time_span:
  start: '2011'
  end: '2023'
  last_confirmed_release: '2026-03'
  coverage_note: >-
    Official page (fetched 2026-08-15) hosts the 2011-2023 table (files under
    /docs/2026-03/). Report PDF (dated 2024-10) states province and city indices span
    2011-2023 and county indices 2014-2023, verified in the XLSX (Counties sheet starts
    at 2014; last year 2023). Page narrative says the index was first released in 2016
    with the second and third releases in 2019 and 2021, while the current downloadable
    table is the 2011-2023 update - the page text and file vintage differ slightly and
    both are preserved here. Earlier vintages (e.g. 2011-2018, 2011-2020, 2011-2021
    tables) are no longer linked on this page.
  last_checked: '2026-09-28'
frequency:
- annual
sample_size: >-
  Verified in the downloaded workbook: 403 province-year rows, 4,369 city-year rows
  (about 336 cities x 13 years, slight imbalance), 26,090 county-year rows (about
  2,609 counties x 2014-2023).
key_variables:
- index_aggregate (总指数)
- coverage_breadth (数字金融覆盖广度)
- usage_depth (数字金融使用深度)
- digitization_level (普惠金融数字化程度)
- usage-depth sub-indices: payment, insurance, monetary_fund, investment, credit, credit_investigation
- administrative codes: prov_code; pref_name_year18/pref_code_year18 and pref_name_year14/pref_code_year14; county_name_year14/county_code_year14; county rows also carry prov_code/prov_name/pref_code/pref_name

research_fit:
  best_for:
  - City-, province- or county-year measures of digital financial inclusion in China for 2011-2023, matched as a treatment/control or control variable into regional, household-survey or firm analyses
  - Comparing regional digital-finance coverage, usage and digitization using the product's documented total index and sub-indices; a paper-specific use must be verified separately.
  choose_over:
  - Choose PKU-DFIIC over ad-hoc digital-finance proxies (single-platform penetration, e-commerce ratios) because it is the widely cited, free, standardized three-level index with published methodology
  - Choose it over china-neri-marketization-index when the question is specifically digital finance rather than general marketization; NERI is a different construct
  - For household-level financial behavior microdata, choose chfs/cfps instead - this index is a regional aggregate, not individual records
  not_good_for:
  - Individual-, firm- or platform-level digital finance usage (the index is region-year aggregate)
  - Hong Kong/Macao/Taiwan observations (excluded by construction)
  - Years after 2023 until a newer official release appears; earlier-vintage tables are not linked on the current page
  - Reproducing the index from the raw Ant Group data (proprietary; never released - only the compiled index is public)
  needs_join_for:
  - Outcome variables: social-capital/survey outcomes (cgss, cfps), firm or household panels, trade/economic outcomes
  - Controls: city-year statistics (china-stat-yearbook) or other regional panels
  variation_available:
  - Regional and time variation in a standardized aggregate index and sub-indices; data-side variation only - treatment assignment designs belong to the variation repository
  topics:
  - digital finance
  - financial inclusion
  - fintech
  - regional development
  - internet finance

good_for:
- Regional digital finance exposure measures for 2011-2023 at three administrative levels
- Heterogeneous analysis by usage-depth components (payment/insurance/monetary fund/investment/credit)
- Cross-province, cross-city and cross-county convergence and diffusion studies
identification:
- The index is a descriptive region-year measure, not an identification design; causal use requires a separately justified design and belongs with the research project rather than this data record.
linkable_keys:
- prov_code (province statistical code)
- pref_code_year18 / pref_code_year14 (prefecture code by vintage)
- county_code_year14 (county code)
- region name + year

joins:
- target: cgss
  relation: complement
  keys:
  - Province or city identifier
  - Year (survey wave year)
  method: Match respondent's province/city to the index of the same or prior year; check survey wave timing against annual index values.
  evidence_status: plausible
- target: cfps
  relation: complement
  keys:
  - Province or city identifier
  - Year
  method: Same direction; CFPS waves are biennial so index year must be aligned to wave year.
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - City code or name
  - Year
  method: Align administrative-division vintages before joining; the index ships year18/year14 and year14 codes for city and county respectively.
  evidence_status: plausible

access_routes:
- route: Official PKU IDF page direct download (Chinese page)
  access_status: verified
  direct_url: https://idf.pku.edu.cn/zsbz/bjdxszphjrzs/index.htm
  requirements: None (free download; no account, no fee)
  steps:
  - Open the 北京大学数字普惠金融指数 page under 指数编制 on idf.pku.edu.cn
  - Click 表格数据：北京大学数字普惠金融指数（2011-2023）to download the XLSX workbook
  - Optionally download 指数报告：北京大学数字普惠金融指数（2011-2023）PDF (also a 2011-2020 report PDF is linked)
  - Cite 郭峰、王靖一、王芳、孔涛、张勋、程志云，测度中国数字普惠金融发展：指数编制与空间特征，经济学（季刊）2020年第19卷第4期，1401-1418页
  deliverable: XLSX workbook (6 sheets, verified 2026-08-15) + report PDFs; English column names inside the workbook
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    Page and files are Chinese; download links are direct (idf.pku.edu.cn/docs/2026-03/...).
    Future updates will likely replace these files; keep a copy of the vintage you use.
- route: Free request by email (stated in the report)
  access_status: verified
  direct_url: https://idf.pku.edu.cn/zsbz/bjdxszphjrzs/index.htm
  requirements: None stated; free of charge
  steps:
  - Email pku_dfiic@163.com requesting the index data (route stated in the 2011-2023 report, page 6: 指数全部数据可向课题组免费索取)
  deliverable: Index data files (exact deliverable/vintage per the team's response)
  cost: free
  last_checked: '2026-09-28'
  caveat: Email route is the report-stated channel; the direct XLSX page link is the faster current route.

access:
  url: https://idf.pku.edu.cn/zsbz/bjdxszphjrzs/index.htm
  cost: free
  license: Free use with citation of the compilation paper; official page welcomes use by all sectors
  format:
  - XLSX
  - PDF
  api: false
  how_to_get: Direct download from the official 指数编制 section; no registration
caveats: >-
  The compiled index is derived from Ant Group proprietary desensitized data; the raw
  data cannot be obtained. Geographic-code vintages differ across sheets (year18/year14),
  which matters when merging with other division-vintage data. County level starts 2014,
  not 2011.

production:
  raw_sources:
    - name: Ant Group desensitized digital-finance big data (蚂蚁集团数字普惠金融脱敏大数据)
      source_type: dataset
      role: Proprietary input used by the compiling team since 2016; not obtainable by researchers; only the compiled index is released
      access_route: None (proprietary)
      url: https://idf.pku.edu.cn
      coverage: Not public
      last_checked: '2026-08-15'
  acquisition_methods:
  - download
  sample_construction: >-
    Region-year aggregation at three administrative levels by the PKU-DFIIC team; the
    report states 33 indicators across 3 dimensions (coverage breadth, usage depth,
    digitalization level) normalized and combined with analytic hierarchy process (AHP).
    The released file is the compiled result, not the underlying records.
  pipeline_stages:
    - stage: aggregate
      inputs:
      - Ant Group desensitized digital finance data
      method: >-
        Indicator system (33 indicators, 3 dimensions), dimensionless normalization and
        AHP-based synthesis per the report appendix 2 (指标体系与指数计算方法); compiled by
        the PKU IDF team with Ant Group Research Institute.
      tools: []
      parameters:
        levels: province / prefecture-city / county
        years: 2011-2023 (province, city), 2014-2023 (county)
      output: Annual index tables at three levels with aggregate and component indices
      evidence: Report PDF appendix 2 (pp. 42-48) and page 4 (内容提要)
  constructed_variables:
    - name: index_aggregate
      concept: Overall digital financial inclusion index (总指数)
      source_fields:
      - 33 component indicators
      method: AHP synthesis of three dimension indices (coverage_breadth, usage_depth, digitization_level)
      validation: Report analyses trends and convergence; component sub-indices provided
      limitations: Composite index; absolute levels are not directly comparable across releases
  validation:
  - Official report documents methodology (appendix 2); the index is the most-cited Chinese economics index per the official page
  output:
    unit_of_observation: region-year
    structure: Annual panel, wide by index component
    geography: Mainland China, 31 provinces / 337 prefecture cities / about 2,800 counties
    time_span:
      start: '2011'
      end: '2023'
    key_variables:
    - index_aggregate
    - coverage_breadth
    - usage_depth
    - digitization_level
    - payment, insurance, monetary_fund, investment, credit, credit_investigation
    formats:
    - XLSX
  reproducibility:
    level: high
    starting_point: Official page XLSX download (the released artifact itself)
    code_available: false
    code_url: ''
    requirements:
    - None; the index is the deliverable
    blockers:
    - Reproducing the index from raw Ant data is impossible (proprietary input)
  compliance:
    terms_or_license: Free use with citation; official page welcomes use (欢迎各界人士使用)
    robots_or_rate_limits: ''
    personal_or_sensitive_data: Index compiled to avoid leaking financial-consumer privacy and business secrets (report page 4)
    redistribution: Redistribution of the released files not explicitly addressed; citation required for use
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: "Lan, Liu, Pan & Peng (2024), 'Building bridges of trust: Impact of regional digital financial inclusion on social capital in China', JRS 64(4)"
  doi: 10.1111/jors.12708
  journal: Journal of Regional Science
  year: 2024
  dataset_role: Unverified product match; the abstract describes regional digital financial inclusion as an explanatory variable for social trust but does not identify PKU-DFIIC.
  evidence_type: abstract-only
  evidence_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.12708
  data_note: >-
    Crossref abstract (read 2026-08-15) says 'regional digital financial inclusion' but
    does not name the index. The paper's data section is unread (Wiley 403 for automated
    clients). This is a discovery lead, not verified use of PKU-DFIIC; both product
    identity and release vintage remain to be confirmed from the paper or authors.
- cite: 郭峰、王靖一、王芳、孔涛、张勋、程志云，测度中国数字普惠金融发展：指数编制与空间特征，经济学（季刊）2020年第19卷第4期，1401-1418页
  doi: ''
  journal: 经济学（季刊）
  year: 2020
  dataset_role: Index compilation and methodology paper (official recommended citation)
  evidence_type: data-section
  evidence_url: https://idf.pku.edu.cn/zsbz/bjdxszphjrzs/index.htm
  data_note: Official page and workbook data notes request this citation for the index.

provenance:
- source: Editorial consistency review against the existing abstract-only evidence for DOI 10.1111/jors.12708 (2026-09-29)
  field_scope:
  - Removed the unconfirmed paper example from research-fit claims; retained the lead with explicit product-identity and vintage uncertainty throughout the record.
  - No new paper full-text or provider verification; product readiness does not verify this paper's data source.
  added: '2026-09-29'
  confidence: high
  verified: true
- source: Official PKU IDF page (idf.pku.edu.cn/zsbz/bjdxszphjrzs/index.htm), fetched 2026-08-15 and rechecked 2026-09-28; XLSX workbook downloaded and sheets/headers/year ranges inspected; report PDF pages 1-7 (title, contents, 内容提要) read
  field_scope:
  - Product identity, producer team, dimensions/indicators, three-level coverage, current 2011-2023 table-download route, citation and compilation-paper use
  - File-level row counts, sheet names, column names, code vintages
  added: '2026-08-15'
  confidence: high
  verified: true
- source: Wiley article page (onlinelibrary.wiley.com/doi/10.1111/jors.12708) - 403 for automated clients; Crossref abstract
  field_scope:
  - Paper identity and abstract-level data characterization only
  added: '2026-08-15'
  confidence: low
  verified: false

related_datasets:
- id: china-neri-marketization-index
  relation: often-confused-with
- id: cgss
  relation: complement
- id: cfps
  relation: complement
- id: chfs
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

PKU-DFIIC is the standard, freely downloadable annual digital-financial-inclusion index for mainland China at province, prefecture-city and county level (2011-2023 / county 2014-2023), compiled by the PKU Institute of Digital Finance with Ant Group from Ant's proprietary desensitized data; a researcher downloads the compiled XLSX directly and must treat the raw Ant microdata as permanently unavailable.

## Select rules

- Prioritize it whenever a research design needs a region-year measure of digital finance penetration, usage or digitalization in China, especially for matching with surveys (CGSS/CFPS/CHFS), firm panels, or city-year outcomes.
- Switch to household financial microdata (chfs/cfps) for individual-level financial behavior; switch to china-neri-marketization-index for general market institutions rather than digital finance.
- Not suitable for Hong Kong/Macao/Taiwan, for years after 2023 before a newer official release, or for any attempt to reconstruct the underlying Ant data.

## Get recipe

1. Open https://idf.pku.edu.cn/zsbz/bjdxszphjrzs/index.htm (指数编制 > 北京大学数字普惠金融指数).
2. Download 表格数据：北京大学数字普惠金融指数（2011-2023）(XLSX; verified 2026-08-15: Provinces 403 rows, Prefecture_Level_Cities 4,369 rows, Counties 26,090 rows; English column names; sheets also contain a regionalism code table and data notes).
3. Download the 2011-2023 report PDF for methodology (appendix 2) if needed.
4. Cite 郭峰 et al. 2020 经济学（季刊）19(4):1401-1418 as requested. Alternative free channel stated in the report: email pku_dfiic@163.com.
5. Save the downloaded vintage; the page may replace files with newer updates.

## Connections and Limitations

- Match by administrative code and year: prov_code for provinces; pref_code_year18 (or _year14) for cities; county_code_year14 for counties. Code vintages differ across sheets - align with the vintage of your other data before joining.
- County-level series starts 2014; province/city start 2011. All levels end at 2023 in the current release.
- The index is annual; survey waves (e.g. biennial CFPS) must be aligned to the index year.
- The compiled index is derived from proprietary Ant data; no raw-data reconstruction is possible, and earlier index vintages (2011-2018/2020/2021 tables) are no longer linked on the current page.
- The JRS 2024 social-capital paper (10.1111/jors.12708) remains a discovery lead: its use of this product and its release vintage are unconfirmed. Read the paper's data section through a legitimate access route or obtain author confirmation before citing it as a PKU-DFIIC use case.

## Decision sufficiency check

A future agent can now: name the asset, say what one row is (region-year index), who produces it (PKU IDF + Ant Group), where to download it (official page XLSX, free), what the deliverable contains (verified sheet/row structure), how to cite it, and what it cannot support (raw Ant data, HK/Macao/Taiwan, post-2023 years, individual-level behavior). Remaining unknown: whether the JRS 2024 paper used this index at all and, if so, which vintage; a paper-specific replication release is also unconfirmed. These gaps do not prevent using the documented product itself.
