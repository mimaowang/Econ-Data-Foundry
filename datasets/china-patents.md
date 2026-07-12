---
schema_version: 2
catalog_status: grounding
id: china-patents
name: China Patent Data (CNIPA / SIPO)
aka:
- 专利数据
- 中国专利
- CNIPA
- SIPO
- 国家知识产权局专利
- China Patent
- 中国专利数据库
- 发明专利申请/授权
- 实用新型
- 外观设计
provider: National Intellectual Property Office (CNIPA, formerly SIPO); researchers often obtain processed versions through
  CSMAR/CNRDS/Hexiang Xinchuang/Patentics/Google Patents, etc.
china_related: true
domains:
- innovation
- firm
- finance
- trade
- IO
- development
unit_of_observation: Patent-year (patent-by-patent level); can be summed to company-year/industry-year/city-year
structure: event-records
geo_granularity:
- enterprise
- inventor
- County
- city
- province
geography: All patents applied for or authorized in China (including patents in China by foreign applicants)
time_span:
  start: 1985
  end: ongoing
  last_confirmed_release: ongoing
  coverage_note: The application, disclosure, authorization and legal status updates are at different times.
  last_checked: '2026-07-10'
frequency:
- annual
sample_size: Tens of millions of patents have been accumulated; since 2020, more than 1.5 million invention patent applications
  have been filed every year, and hundreds of thousands have been authorized.
key_variables:
- Patent application number/publication number/authorization number
- Patent name
- Applicant name (enterprise/individual/university/scientific research institution)
- Inventor's name
- Application date
- open day
- Grant date (invention patent)
- Patent type (invention/utility model/design)
- IPC classification number (International Patent Classification)
- Number of claims
- Citations (forward/backward)
- Patent Attorney/Agency
- Legal status (valid/invalid/transfer/permit/pledge)
- Applicant address (province/city/county)
- priority information
- Patent family (patent family)
research_fit:
  best_for:
  - Enterprise/city innovation output, technology classification, inventor network and patent legal status
  choose_over:
  - When national applicant and patent-level records are required, they take precedence over patent summaries in public company
    financial libraries.
  - When you only research listed companies and need to match stock codes, you can give priority to the CSMAR patent module.
  not_good_for:
  - Unpatented process or trade secrets
  - Directly equate utility models with inventions
  - Exact business matching of name variations is not handled
  needs_join_for:
  - Corporate finance, export and pollution results need to be joined according to the applicant’s name/unified code
  variation_available:
  - Application and authorization time
  - IPC technology field
  - Citations and legal status
  - policy pilot
good_for:
- Measurement of enterprise innovation output - number of patent applications/authorizations, patent quality (number of claims/number
  of citations/IPC width)
- The impact of the intellectual property system on innovation - revision of the patent law/establishment of IP courts/policy
  of patent pledge loans DID
- Innovation network and knowledge spillover—patent citation network, co-inventor network, cross-region/cross-industry knowledge
  flow
- 'After joining with ASIF/Customs: How export/foreign investment/industrial policies affect corporate innovation - the main
  explained variable in the empirical evidence of Chinese corporate innovation'
- Patent pledge financing - the impact of credit availability of patents as collateral on corporate R&D and innovation
- Technology trade and catching up—the quality gap and convergence of foreign patents in China vs. local patents
identification:
- Panel fixed effects (firm/industry/region×year)
- DID (Patent Law Revision/IP Court/Pledge Pilot)
- IV(History/Geography)
- RD
- Patent count model (Poisson/negative binomial)
linkable_keys:
- Company name
- Unified social credit code
- Applicant name
- Industry Code (IPC→Industry Comparison Table)
- area code
access_routes:
- route: cnipa-public-search
  access_status: needs-verification
  direct_url: https://pss-system.cponline.cnipa.gov.cn/
  requirements: According to the registration and usage rules of CNIPA search system; suitable for search and verification,
    not equivalent to opening batch API.
  steps:
  - Enter the CNIPA patent search system.
  - Search by application number, applicant or IPC.
  - Save query criteria and legal status date.
  deliverable: Single item/search results and documents; batch export capability needs to be confirmed according to platform
    rules. This entrance cannot currently be used as a stable and available batch download channel.
  cost: free
  last_checked: '2026-07-10'
  caveat: This round of automatic access returns platform challenge/gateway response, which needs to be reviewed by a manual
    browser or institutional network before upgrading the status.
- route: commercial-processed
  access_status: available-with-subscription
  direct_url: https://data.csmar.com/
  requirements: Institutions subscribe to patent-related sub-repositories.
  steps:
  - Confirm that our school has purchased the patented module.
  - Export by company/year/patent type and field.
  deliverable: Collated version of patents or matched listed company panels.
  cost: paid
  last_checked: '2026-07-10'
access:
  url: 'https://www.cnipa.gov.cn (National Intellectual Property Administration); Commercial platforms: CSMAR/CNRDS patent
    modules (institutional subscriptions); Free platforms: Google Patents (patents.google.com), China Patent Publication Announcement
    (sj.cnipa.gov.cn)'
  cost: 'Original data: free (publicly available by CNIPA); Processed version: paid (subscriptions from CSMAR/CNRDS/Hexiang
    New Startups, etc.)'
  license: Patent data is government public information and can be used freely; the processed version of the commercial database
    is subject to a subscription agreement
  format:
  - csv
  - dta
  - xlsx
  - json(API)
  api: false
  how_to_get: For a small amount of verification, the CNIPA official search system can be used; a more realistic route for
    batch research is the CSMAR/CNRDS/professional patent platform that the institution has purchased. Currently, no CNIPA
    open batch API has been verified that can be used stably in the long term, and web page retrieval capabilities cannot
    be written as a public API.
caveats: The number of patents ≠ the quality of innovation - needs to be corrected by the number of citations/number of claims/IPC
  width, etc. There is a huge gap in innovation content between inventions vs utility models vs designs - usually only invention
  patents are used for research. The names of companies and applicants are not standard - different spellings of the same
  name, mother-child relationship, name changes, etc. require a lot of cleaning (commonly used are CEC/Tianyancha and other
  industrial and commercial databases for matching). There is a time lag of 1.5–3 years from patent application to grant—pay
  attention when doing time series research. CNIPA's crackdown on 'irregular applications' after 2021 has led to a sharp increase
  in the rejection rate - pay attention to the trend analysis across 2021.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Rong, Zhang & Chen (2023), Short-term Loans and Firms'' High-quality Innovation: Evidence from the Access to Patent-backed
    Loans in China'
  journal: CER
  year: 2023
  data_note: Using China's patent data (application/authorization/pledge) + listed company data, a patent pledge loan pilot
    was used as a quasi-experiment, and it was found that patent pledge financing significantly improved the company's high-quality
    invention patent output.
- cite: 'Wan, Wan, Yang & Zhao (2026), Judicial Institution and Innovation: Evidence from China''s Intellectual Property Courts
    Reform'
  journal: JDE
  year: 2026
  data_note: Using China's city-level patent data (CNIPA) + the establishment of intellectual property courts as DID, it was
    found that IP courts increased the number of urban invention patents by 22.6% (annual average +215), and the patent structure
    transformed from utility models to inventions - the mechanism is to shorten the trial time + increase the plaintiff's
    winning rate
provenance:
- source: CNIPA official site https://www.cnipa.gov.cn (supports patent types, legal status, and public access channels)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: CSMAR/CNRDS patent module introduction pages for many universities (confirmed universities can obtain the compiled
    version through subscription)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- asif
- china-customs
- csmar
- wind
---

## Positioning in one sentence
China patent data is a complete record of all patent applications/authorizations/citations/legal status in China disclosed by the State Intellectual Property Office——
Tens of millions of pieces since 1985, covering three types of inventions/utility models/appearance designs.
It is the "standard output variable" for empirical research on enterprise innovation and the "data infrastructure for inter-enterprise knowledge flow networks".
ASIF/Customs/CSMAR can be connected through the company name, forming the "innovation dimension" of Chinese enterprise research.

## Research questions suitable for answering/Typical identification strategies
- **"What drives the innovation of Chinese enterprises"** - Use the number of patent applications/authorizations as explained variables, and various policy impacts as DID identification (free trade zones/development zones/subsidies/taxes/industrial policies → innovation effects).
- **Patent Law Revision** - Changes in specific provisions in the five revisions of 1985/1992/2000/2008/2021 (such as strengthening protection, introducing pledges, improving review standards) → quasi-experiments → causal effects on corporate innovation.
- **Patent Pledge Financing** - The patent pledge loan pilot started in the 2010s provides companies with external financing channels using intangible assets as collateral → Rong et al. (2023 CER) found that this significantly improved the output of high-quality inventions.
- **Not suitable for**: Hidden innovations that do not apply for patents (such as trade secrets/process improvements) - patents only cover innovations that are "codable and choose to apply for protection"; service industry innovations (service industry companies rarely apply for patents).

## Key variables/modules
- **Basic information**: Patent number, name, type (invention/utility model/design), application date/publication date/authorization date
- **Applicant/Inventor**: name, address, nationality (can be used to match companies and track inventor movement)
- **Technical Classification**: IPC classification number (can be mapped to industry/technical field)
- **Quality indicators**: number of claims, number of forward citations (cited), number of backward citations (cited documents), patent family size
- **Legal status**: valid/invalid/deemed withdrawn/rejected/transfer/permit/pledge

## How to get
1. **CSMAR/CNRDS (easiest)**: Through the university library → CSMAR "Company Research Series/Patent Research" → Export the panel by company/year/IPC. Contains a version that has been matched with the listed company code.
2. **Google Patents** (free): patents.google.com → Batch search + CSV download, suitable for global comparative research.
3. **CNIPA public system** (official source): sj.cnipa.gov.cn → Check the legal status of each case + PDF full text.
4. **Self-built cleaning**: Get the original patent text from CNIPA API or commercial platform → match the company name/unified social credit code with ASIF/industrial and commercial registration database.

## Connections to other data
- **ASIF Industrial Enterprise Database**: Use "Enterprise Name" to match → study the innovative behavior of manufacturing enterprises (export/FDI/subsidy/TFP → patent).
- **CSMAR listed companies**: The business platform has matched the stock code → study the relationship between patents and stock price/finance/governance of listed companies.
- **Customs database**: Use "company name" to match → the interaction between export behavior and patent innovation.
- **Industrial and Commercial Registration Database**: Use "Unified Social Credit Code" to accurately match corporate identity → solve the problem of corporate name inconsistency/change.

## Remarks / Pitfalls
- **Company name cleaning is the largest project**: CNIPA does not require applicants to fill in the unified social credit code (it will only be gradually implemented after 2020). There may be 20–30% variations in the company name in historical data (same name for the same company/mother-child relationship/clerical errors). Cleaning company names is the most time-consuming step in empirical research on Chinese patents.
- **Invention ≠ Utility model ≠ Design **: The creativity requirements for utility models are much lower than those for inventions, and design does not involve technology - most high-level research only uses the number of invention patent applications/grants.
- **Authorization time lag**: It takes about 2 years on average from application to authorization for invention patents - using "number of applications" as an output indicator is more timely, using "number of authorizations" is more accurate but has a lag.
- **Citation truncation**: The citation information of Chinese patents is not as standardized and complete as that of US patents (the CNIPA citation system was established later) - pay attention to comparability when doing citation analysis.
