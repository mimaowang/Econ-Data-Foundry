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
- route: CNIPA Patent Search and Analysis System (public service)
  access_status: available-with-registration
  direct_url: https://pss-system.cponline.cnipa.gov.cn/
  requirements: Register and log in as an individual, legal entity, or agency user under the CNIPA system rules. CNIPA describes the service as free public search, analysis, document-browsing, and data-download support; exact query, download, volume, and reuse conditions must be checked in the logged-in interface.
  steps:
  - Register and log in at the CNIPA Patent Search and Analysis System.
  - Define and save a reproducible query by application number, applicant, IPC, date, or other supported fields.
  - Inspect the logged-in download options, fields, result limits, and then-current terms before planning a research extract.
  - Preserve the query, legal-status date, and any downloaded-file manifest with the research project.
  deliverable: Search, analysis, document browsing, and provider-described data-download functions for the logged-in query; an unrestricted national-scale patent panel, API, or reproducible historic bulk export is not established by the public documentation.
  cost: free
  last_checked: '2026-09-28'
  caveat: CNIPA's public documentation establishes the service and registration route, not any particular output volume, file schema, national all-record export, API quota, or reuse right. Automated access returned a platform challenge/gateway response in the prior check; use a normal browser for the supported logged-in route.
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
  cost: 'CNIPA public search and provider-described download functions: free after registration; the scope and volume of a research extract must be confirmed in the system. Processed versions: paid institutional subscriptions (for example CSMAR/CNRDS modules).'
  license: 'CNIPA public-service access and download do not by themselves establish unrestricted bulk reuse or redistribution; check current system terms for the intended extract. Commercial processed versions are subject to their subscription agreement.'
  format:
  - csv
  - dta
  - xlsx
  - json(API)
  api: false
  how_to_get: Start at the registered CNIPA Patent Search and Analysis System for a defined query and inspect its live download limits and terms. For a large, standardized research panel, first ask the institutional library/database administrator which CSMAR/CNRDS/professional patent module is subscribed and what its coverage, fields, export limits, and licence permit. No CNIPA open API or unrestricted national bulk-export route is established here.
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
  last_audited: '2026-09-28'
used_by:
- cite: 'Heblich, Seror, Xu & Zylberberg (2026), Industrial Clusters in the Long Run: Evidence from Million-Rouble Plants in China'
  doi: https://doi.org/10.1093/restud/rdag078
  journal: ReStud
  year: 2026
  dataset_role: Establishment-level patent applications linked to ASIF firms in utility, invention, and design categories
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  data_note: The paper uses the establishment-to-patent links of He et al. (2018) to observe innovation. The replication README names the corresponding firm patent database as a purchasable INCOPAT input and says the transformed patent files used in the paper came from Imbert et al. (2022b); the Zenodo package therefore does not establish a free public download of the linked historical patent file.
- cite: 'Rong, Zhang & Chen (2023), Short-term Loans and Firms'' High-quality Innovation: Evidence from the Access to Patent-backed
    Loans in China'
  journal: CER
  year: 2023
  dataset_role: China's patent data (application/authorization/pledge) as the innovation-outcome source, matched with listed company data, in the patent pledge loan quasi-experiment
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v78y2023ics1043951x23000032.html
  data_note: Using China's patent data (application/authorization/pledge) + listed company data, a patent pledge loan pilot
    was used as a quasi-experiment, and it was found that patent pledge financing significantly improved the company's high-quality
    invention patent output.
- cite: 'Wan, Wan, Yang & Zhao (2026), Judicial Institution and Innovation: Evidence from China''s Intellectual Property Courts
    Reform'
  journal: JDE
  year: 2026
  dataset_role: China's city-level patent data (CNIPA) as the innovation-outcome source (urban invention patents, patent structure) in the intellectual-property-court DID
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v179y2026ics0304387825001816.html
  data_note: Using China's city-level patent data (CNIPA) + the establishment of intellectual property courts as DID, it was
    found that IP courts increased the number of urban invention patents by 22.6% (annual average +215), and the patent structure
    transformed from utility models to inventions - the mechanism is to shorten the trial time + increase the plaintiff's
    winning rate
- cite: 'Chen & Wang (2025), How Air Pollution Affects Innovation Value in China Urban Area?'
  doi: https://doi.org/10.1016/j.chieco.2025.102550
  journal: CER
  year: 2025
  dataset_role: SIPO patent records with renewal model estimated patent values 2007-2015; matched to city-level PM2.5
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001403
  data_note: Uses SIPO patent tracking data and patent renewal model to estimate monetary patent values, then instruments PM2.5 with thermal inversion. Finds PM2.5 reduces patent value by 1.19% per 1% concentration increase. Investigates both intensive (productivity, specialization) and extensive (patent quality downgrading, inventor out-migration) margins.
- cite: 'Du, He & Yao (2026), Environmental Regulation and Indirect Innovation Effects Along Supply Chain: Evidence from China''s Water Pollution Prevention and Control Action Plan'
  doi: https://doi.org/10.1016/j.chieco.2026.102730
  journal: CER
  year: 2026
  dataset_role: SIPO water-related green patent records matched to National Tax Survey firm panel
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000805
  data_note: Matches SIPO green patent applications to tax survey firm identifiers to trace how downstream water-pollution regulation (WPPCAP 2015) induces upstream suppliers' green patenting. Finds regulated firms purchase rather than invent abatement technology — upstream suppliers drive the innovation response in end-of-pipe control patents.
- cite: 'Jia, Li, Liu & Shao (2025), Centralized Procurement Authority and Corporate Innovation'
  doi: https://doi.org/10.1016/j.chieco.2025.102574
  journal: CER
  year: 2025
  dataset_role: Patent output (R&D and patent data for A-share listed pharmaceutical firms 2010-2021)
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S1043951X25002020
  data_note: Uses patent application and grant data for ~201 Chinese A-share listed pharmaceutical firms combined with CSMAR financial data and yaozhi.com drug sales data. Treats the establishment of China's National Healthcare Security Administration (NHSA) in 2018 as an exogenous shock to centralized procurement. Finds NHSA significantly boosts pharmaceutical innovation — firms facing financial pressure from centralized procurement increase R&D and patenting, especially those with stronger internal resources.
- cite: 'Su, Tang & Guan (2026), How Digital Firms Shape Innovation Networks: Evidence from Corporate Patent Citations'
  doi: https://doi.org/10.1016/j.chieco.2026.102674
  journal: CER
  year: 2026
  dataset_role: CNIPA patent registration and citation data (605,740 citation records from 4,866 firms 2012-2021)
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X26000684
  data_note: Uses CNIPA patent citation network data (605,740 citation records across 4,866 A-share listed firms) combined with CSMAR firm characteristics. Examines how digital firms reshape innovation networks through patent citations — digital firms act as knowledge hubs, increasing citation flows and innovation diffusion across the network.
- cite: 'Fan, Li & Song (2025), Factor Market Segmentation and Regional Innovation: Evidence From China'
  doi: https://doi.org/10.1111/jors.70031
  journal: JRS
  year: 2025
  dataset_role: Patent data measuring regional innovation output across 279 prefecture-level cities (1999-2019)
  evidence_type: abstract-only
  evidence_url: https://metatoc.com/papers/121633-factor-market-segmentation-and-regional-innovation-evidence-from-china
  data_note: Uses patent data combined with a price-method factor market segmentation index across 279 prefecture-level Chinese cities (1999-2019). Constructs a spatial weight matrix of factor flows to test how labor and capital market segmentation affect regional innovation. Finds that under fiscal decentralization, local governments implement factor market segmentation strategies without sacrificing local innovation performance, and innovation-peripheral cities benefit more from segmentation while large-market segmentation negatively impacts other regions' innovation through reduced labor inflows.
- cite: 'Wang, Hou, Liu, Wang & Dai (2024), Can Urban Agglomeration Policy Improve the Innovation Efficiency of Cities in China?'
  doi: https://doi.org/10.1080/00343404.2024.2398562
  journal: Regional Studies
  year: 2024
  dataset_role: Patent data measuring urban innovation output; city-level statistics
  evidence_type: abstract-only
  evidence_url: https://www.tandfonline.com/doi/abs/10.1080/00343404.2024.2398562
  data_note: Uses patent data and city statistics in a DID framework to evaluate China's urban agglomeration policies on innovation efficiency. Finds a surprising net -3.65% overall effect — core cities gain +10.1% while non-core cities lose -3.89%, revealing a pronounced innovation siphoning effect where talent and capital concentrate in dominant centers within agglomerations. Mechanism confirmed through labor and commodity market channels.
- cite: 'Li, Ren & Tu (2025), Urban Innovation Structures and Economic Productivity of Chinese Cities'
  doi: https://doi.org/10.1080/00343404.2025.2579626
  journal: Regional Studies
  year: 2025
  dataset_role: >-
    9.5 million geocoded patents across 233 Chinese cities (2009-2020); 1km-grid innovation center identification
  evidence_type: data-section
  evidence_url: https://www.tandfonline.com/doi/pdf/10.1080/00343404.2025.2579626
  data_note: Uses 9.5M geocoded patents across 233 cities (2009-2020) to construct innovation polycentricity and dispersion indices at 1km grid resolution. IV estimation using historical Confucian temples as instruments for innovation structure. Finds moderately polycentric yet concentrated innovation structures enhance economic productivity through agglomeration economies and external knowledge linkages. Policymakers should strategically allocate innovation resources across multiple centers.
- cite: 'Sun & Li (2025), How the Nature of Technologies Influences Their Cross-City Inflows: Empirical Evidence from China, 2001-2020'
  doi: https://doi.org/10.1080/00343404.2025.2572710
  journal: Regional Studies
  year: 2025
  dataset_role: >-
    10 million patent applications tracking inter-city technology flows (2001-2020)
  evidence_type: abstract-only
  evidence_url: https://www.tandfonline.com/doi/abs/10.1080/00343404.2025.2572710
  data_note: Uses 10M+ patent applications tracking technology inflows across Chinese cities (2001-2020). Finds inverted-U relationship between technology inflow and relative complexity — cities absorb technologies matching their complexity level. Technology structural hole position and relatedness to local knowledge base positively drive inflows. Documents compensation effects between relatedness density and structural holes, and threshold effects of relative complexity on relatedness density.
- cite: 'Huang, Jia & Ge (2024), Forced to Innovate? Consequences of United States'' Anti-Dumping Sanctions on Innovations of Chinese Exporters'
  doi: https://doi.org/10.1016/j.respol.2023.104899
  journal: Research Policy
  year: 2024
  dataset_role: CNIPA patent database 1985-2015; invention and utility model patents as innovation outcomes
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S004873302300183X
  data_note: >-
    Uses CNIPA patent records (1985-2015) matched with ASIF-Customs firm panel and WTO anti-dumping case data. DiD finds US anti-dumping sanctions significantly increased patented innovations by targeted Chinese exporters — especially substantive invention patents, not marginal utility models. Effect amplified during China's 2006 pro-innovation national policy period. Documents unintended consequence — protectionism spurs innovation upgrading in targeted exporting firms.
- cite: 'Zhang & Zong (2025), Women''s Empowerment and Participation in Innovation: Evidence from the One-Child Policy in China'
  doi: https://doi.org/10.1016/j.respol.2025.105334
  journal: Research Policy
  year: 2025
  dataset_role: CNIPA patent data 2009-2021; inventor names matched to gender via Bayesian ML (86% accuracy)
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733325001635
  data_note: >-
    Uses CNIPA patent data (2009-2021) with machine learning gender identification from inventor names. Combined with CFPS (2010-2018), Census (2005, 2010), CMDS, CSMAR, and provincial OCP fines (Ebenstein 2010). Finds One-Child Policy empowered women — each unit increase in OCP enforcement raises female inventor probability by ~1% and share by ~0.3%. Women's participation also increases patent quality (forward citations). Four mechanisms — education, reduced domestic burden, gender equality norms, delayed marriage.
- cite: 'Shi & Zhang (2025), Short Technology Cycle Time and Firm Innovation: Evidence from China'
  doi: https://doi.org/10.1016/j.respol.2025.105305
  journal: Research Policy
  year: 2025
  dataset_role: CNIPA patent records for 3,079 A-share listed firms (1990-2022); backward citation-based TCT construction
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733325001349
  data_note: >-
    Uses CNIPA patent backward citation data to construct firm-level technology cycle time (TCT) — average citation lag measures how quickly technology turns over. Combined with CSMAR financial data. Finds latecomer firms benefit from short TCT technologies — faster knowledge obsolescence creates catch-up windows. Private firms, high-tech/competitive industries, and early-lifecycle firms benefit most.
- cite: 'Zhang, Bai, He & Guo (2026), Greening but Concentrating? The Unintended Effects of China''s Voluntary Participatory Environmental Regulations on Firms'' Innovation Portfolios'
  doi: https://doi.org/10.1016/j.respol.2026.105531
  journal: Research Policy
  year: 2026
  dataset_role: CNIPA patent records for listed manufacturing firms; green vs non-green patent classification
  evidence_type: abstract-only
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733326001228
  data_note: Uses CNIPA patents to construct innovation portfolios distinguishing green vs non-green knowledge recombination (creation vs reuse). Multi-period DiD with double/debiased ML on China's Green Factory certification. Finds VPERs increase green knowledge recombination but crowd out non-green creation — a "greening but concentrating" effect. Documents resource reallocation tradeoffs as the mechanism.
- cite: 'Yu, Zheng & Liu (2026), Digital Innovation as a Bank Risk Mitigator: Empirical Insights from Chinese Commercial Banks'
  doi: https://doi.org/10.1016/j.respol.2026.105501
  journal: Research Policy
  year: 2026
  dataset_role: CNIPA patent records for 391 Chinese commercial banks; digital/fintech patent identification
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0048733326000922
  data_note: Uses CNIPA patent data with IPC codes (G06Q20/30/40) to identify digital/fintech patents filed by 391 Chinese commercial banks. Combined with CSMAR, Wind, and BankFocus. Constructs five-dimensional digital innovation index (volume, quality, agency, generativity, convergence). Finds digital innovation reduces bank risk through market discipline (transparency → external oversight) and market power (better loans → less aggressive risk-taking) channels.
provenance:
- source: CNIPA official site https://www.cnipa.gov.cn (supports patent types, legal status, and public access channels)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: "CNIPA Patent Search and Analysis System introduction (2023-02-13) and the CNIPA Public-Service Platform data-use manual/open catalogue, checked 2026-09-28"
  field_scope:
  - current official system identity
  - registration/login requirement
  - provider-described search, analysis, document-browsing, and data-download functions
  - boundary that public materials do not document a national unrestricted bulk export, API, output quota, schema, or reuse right
  added: '2026-09-28'
  confidence: high
  verified: true
- source: CSMAR/CNRDS patent module introduction pages for many universities (confirmed universities can obtain the compiled
    version through subscription)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  field_scope:
  - ReStud use of He et al. (2018) establishment-to-patent links
  - utility, invention, and design patent categories
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/20671189
  field_scope:
  - ReStud patent acquisition boundary
  - INCOPAT purchase and transformed-file distinction
  added: '2026-08-11'
  confidence: high
  verified: true
- source: Evidence-boundary review of publisher and aggregator abstract landing pages in used_by (2026-09-28)
  field_scope:
  - Reclassified entries whose linked evidence is an abstract or /abs/ landing page as abstract-only
  - Did not alter the separately supported ReStud full-text and replication-package evidence
  added: '2026-09-28'
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
