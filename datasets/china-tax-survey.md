---
schema_version: 2
catalog_status: grounding
id: china-tax-survey
name: Chinese Enterprise Tax Survey Microdata
aka:
- 中国企业税收调查
- 企业税收调查
- 中国税收调查企业数据
- 全国税收调查企业数据
- 企业税收调查微观数据
- China Enterprise Tax Survey
provider: China Enterprise Tax Investigation; The verified institutional/commercial versions are held by universities or provided
  by platforms, and the original investigation authorities and unified application channels still need to be verified.
china_related: true
domains:
- tax
- public-finance
- firm
- finance
- trade
- innovation
unit_of_observation: Enterprise-year (the cross-year connectability and desensitization rules of different holding versions
  need to be verified separately)
structure: annual-enterprise-microdata
geo_granularity:
- enterprise
- City/Province (version field and desensitization permission need to be verified)
geography: China corporate tax survey sample; verified version coverage and industry description vary by agency/platform version
time_span:
  start: 2007
  end: 2020
  last_confirmed_release: 2020
  coverage_note: The version held by Xiamen University is 2007–2020; the version held by Shanghai University is 2008–2016;
    the CnOpenData processed version is marked 2008–2020. Years, sample sizes, or fields from any one version cannot be extrapolated
    to all holdings.
  last_checked: '2026-07-11'
frequency:
- annual
sample_size: The Xiamen University page states that it holds about 700,000 companies/year; the Shanghai University page says
  that the 2008–2016 version has a total of about 2 million companies and about 500,000 companies/year; the CnOpenData page
  says that the processed version holds about 600,000–700,000 companies/year.
key_variables:
- Basic information of the enterprise (name/taxpayer identification code, etc., version permissions need to be verified)
- Survey year
- Industry
- Property attributes
- Tax declaration information
- Corporate financial statement project
- Goods and services/output sales field
- corporate balance sheet
- income statement
- cash flow statement
research_fit:
  best_for:
  - Microscopic research on corporate tax burden, tax system reform, tax collection and management, tax incentives and business
    operations/investment/innovation
  - Requires tax reporting and financial statement items and accepts restricted access to corporate annual data
  - Research on enterprise-level matching with industrial enterprises, customs, patents or industrial and commercial data
    (verify version key and authorization first)
  choose_over:
  - When you need tax types, tax payments and more detailed financial statement items, you can give priority to investigating
    this data; when you need a mature and publicly processed version of industrial production variables, compare ASIF first
  - Before studying the service industry or the entire industry, first verify the target version coverage; do not infer from
    a certain university or business version that all versions are the same
  not_good_for:
  - Request projects that require no institutional affiliation, no subscription, and are immediately publicly downloadable
  - Treat different university-owned versions, commercially processed versions and original surveys as studies with exactly
    the same fields
  - Research that does not have available corporate identity or name cleaning rules but promises an exact match to ASIF/Customs/Patents
  needs_join_for:
  - Trade, patent, productivity or local policy issues usually require company name/restricted identification code, industry
    code, region and year; company name changes, group relationships and version cleaning need to be handled separately
  - Policy evaluation also requires external policy time points and administrative area crosstabs; the tax declaration field
    itself does not automatically provide processing variables
  variation_available:
  - Annual tax burden and financial changes of enterprises
  - Before and after tax reform
  - Regional/industry tax system differences
  - firm heterogeneity
  topics:
  - corporate tax
  - tax burden
  - tax cuts
  - value added tax
  - corporate income tax
  - Tax collection and administration
  - corporate finance
  - tax reform
  - tax investigation
good_for:
- The impact of tax cuts, tax-to-VAT reform, tax administration reforms and tax incentives on corporate investment, employment,
  financing and innovation
- The relationship between corporate tax burden and balance sheet, income statement, and cash flow or policy evaluation
- Restricted matching design of corporate tax data and customs/patent/industrial enterprise data
identification:
- firm fixed effects
- DID (tax system/collection reform)
- event study
- IV (needs to be demonstrated separately)
- Breakpoint or threshold design (depending on specific policy)
linkable_keys:
- Taxpayer identification code (already appears in the field description on the previous page; authority needs to be verified)
- Company name
- Survey year
- Industry
- Region code (version to be verified)
joins:
- target: asif
  relation: complement
  keys:
  - Business name or restricted business identity
  - Year
  - Industry/region auxiliary key
  method: entity-resolution
  evidence_status: plausible
- target: china-customs
  relation: complement
  keys:
  - Business name or restricted business identity
  - Year
  method: entity-resolution
  evidence_status: plausible
- target: china-patents
  relation: complement
  keys:
  - Business name or restricted business identity
  - Year
  method: entity-resolution
  evidence_status: plausible
access_routes:
- route: xmu-institutional-holding
  access_status: available-with-application
  direct_url: https://econpub.xmu.edu.cn/elib/db_detail/23/
  requirements: Xiamen University holds a version of the Economics Research Sharing Platform; first confirm your institutional
    identity, application qualifications, data use agreement and current access methods on the platform.
  steps:
  - Open the "Chinese Enterprise Contribution Database" page of Xiamen University and check the required year, three types
    of data tables and data dictionary.
  - Submit the application through the data acquisition/application portal on the page or the current process of the platform;
    if only online access is provided, confirm whether export is allowed.
  - Once approved, save the institution's version, year, and field description; do not generalize it to other held versions.
  deliverable: The school's page describes the three-category data table of the 2007-2020 agricultural, industrial and service
    enterprise tax survey; the page says that you can apply for bare data or access it online.
  cost: by-application
  last_checked: '2026-07-11'
  caveat: This is a route held by specific universities and is not a unified public download for all researchers; application
    qualifications, export permissions and current page processes should be reconfirmed when applying.
- route: shu-institutional-holding
  access_status: restricted-institutional
  direct_url: https://soe.shu.edu.cn/info/1203/44614.htm
  requirements: Shanghai University School of Economics has purchased the 2008–2016 edition. The page clarifies that teachers,
    postdoctoral students and doctoral students need to sign a use agreement; undergraduate/master students need a supervisor
    to apply and be responsible for process management.
  steps:
  - Confirm my applicable identity with Shanghai University School of Economics, and read the usage agreement linked to the
    school's page.
  - Submit the signed agreement as required by the announcement; after meeting the conditions, go to the designated laboratory
    to copy the original documents.
  - Confidentiality and redistribution restrictions were observed, and the 2008–2016 Shanghai University version was used
    in the study.
  deliverable: The school's announcement describes about 2 million enterprise data from 2008 to 2016, including basic information,
    enterprise and goods and labor services tables; the CSV compressed package is about 3GB.
  cost: by-application
  last_checked: '2026-07-11'
  caveat: This pathway is subject to on-campus procurement and agreement and does not constitute a public application commitment
    by outside researchers.
- route: cnopendata-commercial-version
  access_status: commercial-subscription
  direct_url: https://www.cnopendata.com/data/m/finance-tax/Tax-Survey.html
  requirements: CnOpenData commercial processing version; first confirm the subscription, module, export limit, field version
    and usage license with your institution's account.
  steps:
  - Open the China Tax Survey Enterprise Data page and check the target year, field descriptions and associated modules.
  - Confirm whether the module is available through your organization's subscription or platform sales/account process.
  - Save the platform version, field differences, and cleaning instructions before exporting; do not equate commercially processed
    versions with the original survey.
  deliverable: The 2008–2020 corporate tax survey processing data marked on the page contains approximately 600,000–700,000
    enterprises/year and 400–500 fields; fields may vary from year to year.
  cost: paid
  last_checked: '2026-07-11'
  caveat: The visibility of the webpage does not mean that the user has obtained the right to download; the price, institutional
    coverage and specific export permissions are subject to the subscription account.
access:
  url: https://econpub.xmu.edu.cn/elib/db_detail/23/
  cost: mixed
  license: Both institutionally held and commercially processed versions are subject to their respective agreements, confidentiality,
    and redistribution restrictions; free sharing should not be assumed simply because of the presence of an entry in the
    record.
  format:
  - csv
  api: false
  how_to_get: 'Priority is given to confirm whether the institution holds the version: the Xiamen University route can be
    applied for/accessed online from the sharing platform; the route to Shanghai University is limited to on-campus personnel
    specified in the announcement; other researchers can check the CnOpenData module under institutional subscription. Each
    time, record the year, fields, permissions, and agreement of the version obtained.'
caveats: This record intentionally separates the data product from the specific held/processed version. Verified are several
  agency/commercial versions, not a single authority responsible for the original survey, a nationally unique version, or
  a standard application channel for everyone. Cross-year tracking, cross-database matching, industry coverage, and variable
  comparability must all be double-checked against the actual approved version.
quality:
  profile_status: partial
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-08-11'
used_by:
- cite: 'Chen, Chen, Liu, Suárez Serrato & Xu (2025), Regulating Conglomerates: Evidence from an Energy Conservation Program in China'
  doi: https://doi.org/10.1257/aer.20211455
  journal: AER
  year: 2025
  dataset_role: Tax/ATS robustness measures for output and energy use, especially 2007–2010 fills
  evidence_type: data_appendix
  evidence_url: https://assets.aeaweb.org/asset-server/files/22048.pdf
  data_note: The appendix calls the source ATS in the data-comparison and robustness tables, reports tax-survey energy data,
    and uses ATS output for 2007–2010 while ASIF supplies 2001–2006 in one comparison. The paper does not establish that ATS
    is identical to any one university or commercial holding, so the product/version and current export permission must be
    verified before treating this record as the exact paper input.
- cite: 'Chen, Liu, Suárez Serrato & Xu (2021), Notching R&D Investment with Corporate Income Tax Cuts in China'
  doi: https://doi.org/10.1257/aer.20191758
  journal: AER
  year: 2021
  dataset_role: Firm-level tax records with R&D deduction eligibility for bunching and structural estimation
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/131201/
  data_note: Used the National Tax Survey (全国税收调查) enterprise panel to study how tax notches affect R&D investment. Combined
    tax deduction eligibility thresholds with firm-level R&D spending, applied bunching methods and structural estimation to
    quantify the R&D response to corporate income tax cuts.
- cite: 'Du, He & Yao (2026), Environmental Regulation and Indirect Innovation Effects Along Supply Chain: Evidence from China''s Water Pollution Prevention and Control Action Plan'
  doi: https://doi.org/10.1016/j.chieco.2026.102730
  journal: CER
  year: 2026
  dataset_role: Main firm-level panel for upstream innovation outcomes; National Tax Survey matched with SIPO patent data
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000805
  data_note: Uses the National Tax Survey firm panel combined with water-related green patent records from SIPO to study how downstream environmental regulation (WPPCAP 2015) induces upstream suppliers to produce green patents. Finds that regulated polluters do not innovate in-house but purchase abatement equipment from upstream suppliers, driving a pronounced rise in upstream water-related green patenting.
- cite: 'Wang, Wu & Wu (2025), Export Slowdown and Increasing Land Supply: Local Government''s Responses to Export Shocks in China'
  doi: https://doi.org/10.1016/j.jue.2025.103796
  journal: JUE
  year: 2025
  dataset_role: City-year local-government tax-revenue panel constructed from firm-level NTSD tax payments
  evidence_type: data_section_and_working_paper
  evidence_url: https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf
  data_note: The paper states that NTSD is jointly collected by the State Administration of Taxation and Ministry of Finance, covers roughly 680,000 sampled firms per year, and that the study uses 2008-2015 waves. It aggregates firm tax payments by city-year and applies estimated government share ratios to construct local tax revenue. This is a paper-derived city-year panel; the underlying firm microdata remain access-controlled and are not implied to be public by the paper's aggregate results.
provenance:
- source: https://econpub.xmu.edu.cn/elib/db_detail/23/
  field_scope:
  - identity
  - xmu_version_coverage
  - industry_scope
  - sample_size
  - table_structure
  - format
  - xmu_access
  added: '2026-07-11'
  confidence: high
  verified: true
- source: https://soe.shu.edu.cn/info/1203/44614.htm
  field_scope:
  - shu_version_coverage
  - sample_size
  - variables
  - format
  - shu_access_restrictions
  added: '2026-07-11'
  confidence: high
  verified: true
- source: https://www.cnopendata.com/data/m/finance-tax/Tax-Survey.html
  field_scope:
  - commercial_version_coverage
  - commercial_version_variables
  - commercial_access
  added: '2026-07-11'
  confidence: med
- source: Wang, Wu & Wu (2025) working-paper data section https://www.china-ces.org/Files/3055abstract/202401241534361470.pdf and JUE DOI https://doi.org/10.1016/j.jue.2025.103796
  field_scope:
  - NTSD producer description
  - approximate annual sample size
  - 2008-2015 wave use
  - city-year aggregation and tax-share construction
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://assets.aeaweb.org/asset-server/files/22048.pdf
  field_scope:
  - AER paper use of tax survey/ATS
  - 2007–2010 robustness role
  - unresolved ATS product identity
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://doi.org/10.3886/E196012V1
  field_scope:
  - public replication folder boundary
  - Raw_Data/ATS label
  added: '2026-08-11'
  confidence: high
  verified: true
related_datasets:
- id: asif
  relation: complement
- id: china-customs
  relation: complement
- id: china-patents
  relation: complement
---

## Positioning in one sentence

The microdata of the China Corporate Tax Survey is an important source of corporate annual tax declarations and financial information, and is suitable for research on tax systems, collection and management, and corporate behavior. The current executable route is a version held by specific universities or a commercially processed version, rather than a unified public download; when answering the research idea, you must explain the actual version and the acquisition threshold at the same time.

## Select rules

- When studying the impact of tax burdens, tax types, tax reductions or collections on corporate results, it is a priority to assess whether this data is available.
- When studying industrial productivity and only having access to the database of mature commercial enterprises, ASIF may be more realistic; when studying trade transactions, the customs database is more direct.
- Do not regard "Tax Survey", "Chinese Enterprise Contribution Database" and the business platform module as naturally the same version, and do not equate web page visibility with public downloadability.

## Get recipe

1. First determine which route you can take: whether your school has a university-owned version, or whether it has subscribed to a commercial module.
2. Use the page of this route to check the year, industry, table structure, fields and protocols before submitting the application or confirming the module in the institutional account.
3. After obtaining the data, save the version description, export log, field dictionary and usage agreement; perform name/identification code coverage diagnosis before matching other enterprise libraries.

## Connections and Limitations

- The Shangda announcement lists taxpayer identification codes and company names, but whether the precise identification can be exported, how to desensitize it, and the matching rate with other libraries still depend on the approved version.
- The time ranges, sample sizes, fields, and access rights of the Xiamen University Edition, Shanghai University Edition, and CnOpenData Edition should not be substituted for each other.
- Current records do not document the original survey authorities, the full sampling frame, or the unified application success rate as known facts; these are the focus of the next round of grounding.
