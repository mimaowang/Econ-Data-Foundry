---
schema_version: 2
catalog_status: grounding
id: asif
name: Annual Survey of Industrial Firms (ASIF; China Industrial Enterprise Database)
aka:
- 中国工业企业数据库
- 规模以上工业企业数据库
- 工业企业调查
- ASIF
- ASIE
- Annual Survey of Industrial Firms
- NBS工业统计
provider: National Bureau of Statistics of China (NBS); researchers often obtain processed editions through CAJ, CNRDS, or CSMAR
china_related: true
domains:
- firm
- trade
- IO
- development
- macro
- labor
- innovation
unit_of_observation: Firm-year (unbalanced panel; firms are linked across years using enterprise identifiers)
structure: unbalanced-panel
geo_granularity:
- enterprise
- County
- city
- province
geography: Above-scale industrial firms in mainland China (all state-owned firms plus non-state firms with annual main-business revenue of at least RMB 5 million; the threshold rose to RMB 20 million in 2011)
time_span:
  start: 1998
  end: 2013
  last_confirmed_release: 2013
  coverage_note: Research commonly uses the relatively well-documented 1998-2013 editions; 2008-2010 and the 2011 reporting-threshold change require separate treatment
  paper_specific_restud_window: Heblich, Seror, Xu & Zylberberg (2026 ReStud) use the NBS above-scale firm data for 1998-2007; the paper calls this the Annual Survey of Industrial Firms (ASIF), while the replication README identifies the purchased raw input as the NBS 2009 edition.
  last_checked: '2026-08-11'
frequency:
- annual
sample_size: Approximately 200,000-400,000 firms per year, with discontinuous growth in early years
key_variables:
- Company code
- Company name
- Industry code (4 digits)
- County, city, and province codes
- Registration type
- Gross industrial output value
- Industrial value added
- Number of employees
- Original value/net value of fixed assets
- Total assets
- Total liabilities
- Main business income
- export delivery value
- operating profit
- VAT payable
- Total salary
- R&D expenditure (part years)
- Year of establishment
- Affiliation
- Holdings
research_fit:
  best_for:
  - Productivity, entry and exit, ownership and policy impacts of industrial enterprises above designated size from 1998 to
    2013
  choose_over:
  - Prioritize ASIF over CSMAR/Wind for broad non-listed manufacturing production and firm dynamics during 1998-2013.
  - Prioritize CSMAR/Wind when studying listed company governance, market returns, and post-2014 financials
  not_good_for:
  - Service industry
  - Non-standard small businesses
  - After 2014
  - Family or personal research
  needs_join_for:
  - Imports and product destination countries require customs; innovation requires patents; emissions require enterprise pollution
    investigation
  variation_available:
  - Corporate Annual Panel
  - WTO accession and tariff changes
  - Regional/Industry Policies
  - Enterprise entry and exit
good_for:
- Research on enterprise-level productivity (TFP), markup, resource allocation and reweighted productivity
- Exports and enterprise performance (export learning effect, self-selection), the impact of trade liberalization (such as
  WTO accession/tariffs) on enterprises
- Foreign capital spillovers, imported intermediate goods and total factor productivity
- 'Enterprise-level identification of policy impacts: DID for environmental protection inspections, minimum wages, industrial
  policies, establishment of development zones, etc.'
- Enterprise entry and exit, aggregate productivity decomposition (Foster-Haltiwanger-Wanger decomposition)
identification:
- Panel fixed effects (firm)
- Control industry×year/region×year
- DID (policy time point/regional difference)
- IV (tariff/exchange rate/geographical exogenous shocks)
- Natural experiment (WTO accession/policy pilot)
linkable_keys:
- Corporate legal person code
- Organization code
- Company name
- County code
- Industry code GB/T4754
access_routes:
- route: CCER Special Data Platform (paper README-named route)
  access_status: needs-verification
  direct_url: https://www.ccerdata.cn/home/company
  requirements:
  - Institutional or paid access to the China Industrial Enterprises Database module.
  - Confirm whether the licensed edition includes the 1998-2013 years and the variables used by the paper.
  steps:
  - Ask the institution or vendor for the exact database name, edition, years, and export restrictions.
  - Confirm the firm identifiers and historical cleaning choices before matching to the 1985 survey or plant records.
  - Record the licensed version and access terms before building a panel.
  deliverable: Licensed processed industrial-firm data; the paper's name/location matches and cleaned 139-project panel are not guaranteed to be included.
  cost: paid
  last_checked: '2026-08-11'
  caveat: The route is named in the 2026 ReStud replication README; current module availability, pricing, and field coverage were not independently verified.
- route: ReStud Zenodo replication package (paper-specific code and public inputs)
  access_status: available-with-conditions
  direct_url: https://zenodo.org/records/20671189
  requirements:
  - Download the 1.05GB PUBLIC_PACKAGE.zip and README.pdf; the current Zenodo record is open and CC-BY-4.0, but verify the package version and any upstream-input terms before use.
  - Obtain the proprietary NBS above-scale firm input separately from the named vendor or another licensed institutional route.
  steps:
  - Open the Zenodo record and read the README before unpacking the package.
  - Place the licensed ASIF raw files in the package's documented confidential input folder without renaming the expected folders.
  - Run only the documented cleaning stages needed for the intended output, then compare the generated results with the released figures and tables.
  deliverable: Public replication code and redistributable auxiliary inputs; the underlying ASIF microdata and the paper's confidential transformed firm files are not released by this route.
  cost: mixed
  last_checked: '2026-09-28'
  caveat: Current Zenodo metadata confirms an open CC-BY-4.0 package with PUBLIC_PACKAGE.zip (1,052,415,593 bytes) and README.pdf, but not its interior manifest or the terms for upstream inputs. It is a reproduction route for this paper, not a free ASIF download. The README names Beijing Fu'ao Huamei Information Consulting Co., Ltd. as a purchase route, but current price, terms, and historical edition must be rechecked.
- route: ReStud 2025 shipbuilding Zenodo replication package (paper-specific code and public inputs)
  access_status: available-with-conditions
  direct_url: https://zenodo.org/records/14083198
  requirements:
  - Download the package and read its README and current Zenodo license metadata before reuse.
  - Obtain the proprietary Clarksons Research shipyard and NBS manufacturing-survey inputs separately; the package does not include those confidential inputs.
  steps:
  - Open the Zenodo record for Barwick, Kalouptsidi & Zahur and record the current version before downloading.
  - Use the released code and non-confidential auxiliary files only after checking which missing Clarksons/NBS files each cleaning stage expects.
  - If a full reproduction is needed, arrange lawful access to both providers and keep their files separate from the public package.
  deliverable: Public replication code and non-confidential auxiliary inputs for the shipbuilding paper; not a public replacement for the ASIF firm panel, the Clarksons shipyard panel, or the paper's confidential matched files.
  cost: mixed
  last_checked: '2026-08-12'
  caveat: The README identifies Clarksons shipyard production/market data and NBS firm/investment data as proprietary. Zenodo access therefore supports code inspection and partial reproduction, but does not itself supply the underlying firm or shipyard observations.
- route: nbs-microdata-lab
  access_status: needs-verification
  direct_url: https://microdata.stats.gov.cn/
  requirements: The supporting institution registers and submits the project; first confirm whether the current applicable
    catalog contains the year of the target industrial enterprise.
  steps:
  - Sign up for the Micro Data Lab.
  - Identify the year and usage of the industrial enterprise survey in the directory.
  - Submit projects, variables, and safe use requests.
  deliverable: Controlled microdata within approved scope; complete 1998–2013 database cannot be promised.
  cost: by-application
  last_checked: '2026-07-10'
- route: AEA/openICPSR replication project for Huang, Li, Ma & Xu (2017)
  access_status: available-with-conditions
  direct_url: https://www.openicpsr.org/openicpsr/project/113063/version/V1/view
  requirements:
  - An openICPSR/ICPSR account and acceptance of the current download terms; the checked download link redirected to login.
  - Read the V1 Readme.pdf and license file before using the deposited materials.
  steps:
  - Open the AEA article page and follow its Replication Package link to openICPSR project 113063, version V1.
  - Inspect the `20150592_data` folder and record the package version before downloading.
  - Use the deposited do-file and DTA files only for the paper-specific SOE analysis; obtain the underlying ASIF edition separately if a new firm panel is needed.
  deliverable: The V1 folder lists a 36.8 MB AER_2015_0592_R2__Data.zip, Readme.pdf, appendix170123.do, Figure-B-2.xlsx, Figure-I-1.xlsx, and named SOE analysis DTA files; it does not establish a public download of the complete ASIF source.
  cost: registration
  last_checked: '2026-08-11'
  caveat: The file manifest was verified, but the current download action redirected to ICPSR login and the repository states that materials are distributed as received and not reviewed or processed by ICPSR. Treat the deposited files as a paper-specific analysis package, not as a clean or complete ASIF release.
- route: AEA/openICPSR replication project for Imbert, Seror, Zhang & Zylberberg (2022)
  access_status: available-with-conditions
  direct_url: https://www.openicpsr.org/openicpsr/project/152203/version/V1/view
  requirements:
  - An openICPSR/ICPSR account and the current download terms; the project page lists the files but requires the repository's
    current access workflow for downloads.
  - Read the V1 README and Manifest.txt before using any deposited file.
  steps:
  - Follow the AEA article's Replication Package link to openICPSR project 152203, version V1.
  - Inspect `Code/Cleaning/ASIF`, `Code/Cleaning/Census`, `Code/Cleaning/UHS`, and `Code/Cleaning/NLP` to see which source files the
    scripts expect; inspect `Data/Public/Raw` separately from `Data/Public/Analysis` and `Intermediate`.
  - Keep the NBS ASIF input as a separate acquisition problem. The public raw tree lists auxiliary files such as Harvest.zip (2.7 MB)
    and Yield.zip (382.1 MB), but no complete ASIF firm file is listed at that level.
  deliverable: A paper-specific code/data/results deposit with cleaning scripts, derived analysis files, and public auxiliary inputs;
    it does not establish a public download of the complete NBS ASIF panel or permission to redistribute it.
  cost: registration
  last_checked: '2026-08-11'
  caveat: The repository says materials are distributed as received and are not reviewed or processed by ICPSR. The AEA appendix's
    2000–2006 firm panel and the repository metadata's 2000–2005 time field should both be preserved until the README resolves the
    discrepancy; neither should be silently substituted for the other.
- route: commercial-processed
  access_status: needs-verification
  direct_url: https://data.csmar.com/
  requirements: Institutions subscribe and have purchased industrial enterprise-related subdatabases; different schools have
    different permissions.
  steps:
  - Check the school’s CSMAR/CNRDS resource description.
  - Search the platform for relevant modules and tables of industrial enterprises.
  - Check the version, year, and cleaning instructions before exporting.
  deliverable: Commercial platform processing version; module existence and coverage must be confirmed in the organization's
    account.
  cost: paid
  last_checked: '2026-07-10'
access:
  url: https://microdata.stats.gov.cn/
  cost: mixed
  license: Only for academic research, a confidentiality agreement is required; most research is processed through subscriptions
    to university databases
  format:
  - dta
  - csv
  - xlsx
  api: false
  how_to_get: First confirm whether the target year can be applied for in the Micro Data Laboratory of the National Bureau
    of Statistics; in reality, it is more common to obtain the processed version through the commercial library purchased
    by the school, but the specific module, year and cleaned version must be confirmed in the institutional account. The National
    Bureau of Statistics public summary platform is not the ASIF micro-download portal.
caveats: 'Including early discontinuities and measurement definition changes: data quality declined from 2008 to 2010, and the scale threshold
  was raised from 5 million to 20 million in 2011, resulting in breakpoints; there are duplicate records and false positives,
  which need to be cleaned (commonly used for corrections such as Brandt); it is difficult to match enterprises across years,
  and proper name/code changes are common. Not suitable for use in service industries and non-standard enterprises. In the 2026 ReStud
  replication, the ASIF input remains proprietary: a public Zenodo package supplies code and redistributable inputs but not the raw or
  confidential transformed ASIF files, so downloading that package does not make the firm panel reproducible without a separate licensed input.'
quality:
  profile_status: partial
  access_status: needs-verification
  paper_use_status: verified
  last_audited: '2026-08-11'
used_by:
- cite: 'Imbert, Seror, Zhang & Zylberberg (2022), Migrants and Firms: Evidence from China'
  doi: https://doi.org/10.1257/aer.20191234
  journal: AER
  year: 2022
  dataset_role: Main above-scale manufacturing establishment panel for urban production, employment, labor cost, capital, value added,
    productivity, and product descriptions
  evidence_type: appendix_and_replication
  evidence_url: https://www.aeaweb.org/articles/materials/16850
  data_note: >-
    The AEA online appendix identifies the NBS Annual Survey of Industrial Firms (ASIF) as a census of all state-owned manufacturing
    establishments and non-state establishments above RMB 5 million in sales. The broader data cover 1992–2009, while the paper's
    comparable baseline is 2000–2006; annual samples range from about 150,000 to 300,000 legal units and the balanced panel used in
    most analyses contains about 32,000 establishments. The data include location, industry, ownership, exports, employment, output,
    value added, wages, assets, financial variables, and up to three textual product descriptions that the authors classify to HS-6.
    The openICPSR V1 deposit lists code, data, results, README, and manifest; its public raw tree lists auxiliary files but does not list
    a complete ASIF firm file. The deposit therefore supports paper-specific processing and released derived files, not an unrestricted
    replacement for the NBS source panel.
- cite: 'Giorcelli & Li (2026), Technology Transfer and Early Industrial Development: Evidence from the Sino-Soviet Alliance'
  doi: https://doi.org/10.1093/restud/rdag047
  journal: ReStud
  year: 2026
  dataset_role: 1998-2013 industrial-firm performance matched to 139 156-Project firms
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845
  data_note: The article says it manually matched 139 industrial firms to the China Industrial Plants database for 1998-2013; the replication README identifies this as the China Industrial Enterprises Database/ASIF and names NBS application, licensed institutions, and the CCER Special Data Platform as routes. The Zenodo package is synthetic and does not release the original firm records.
- cite: 'Barwick, Kalouptsidi & Zahur (2025), Industrial Policy Implementation: Empirical Evidence from China''s Shipbuilding Industry'
  doi: https://doi.org/10.1093/restud/rdaf011
  journal: ReStud
  year: 2025
  dataset_role: NBS annual firm component for shipyard location (province/city), fixed assets/investment, ownership, and longitudinal firm matching; joined to the Clarksons shipyard production panel
  evidence_type: data_section_and_replication_readme
  evidence_url: https://academic.oup.com/restud/article/92/6/3611/8099437
  data_note: >-
    The paper's data section identifies the NBS annual manufacturing-firm database as the source for shipyard province and city,
    fixed assets, ownership, and firm links over 1998-2013; the manuscript notes that missing NBS information in 2010 prevents
    constructing investment for 2009-2010. The companion Clarksons Research input is a quarterly worldwide shipyard panel from
    1998 Q1 to 2014 Q1 with orders, deliveries, and backlog by ship type; Chinese shipyards are matched to the NBS firm records.
    The Zenodo package (10.5281/zenodo.14083198) releases code and non-confidential auxiliary inputs, while its README states that
    the Clarksons and NBS inputs are proprietary and must be obtained separately. Downloading that package therefore does not
    make the ASIF source, the Clarksons panel, or the paper's confidential matched panel publicly reproducible.
- cite: 'Heblich, Seror, Xu & Zylberberg (2026), Industrial Clusters in the Long Run: Evidence from Million-Rouble Plants in China'
  doi: https://doi.org/10.1093/restud/rdag078
  journal: ReStud
  year: 2026
  dataset_role: Establishment-level production, productivity, innovation, and markup outcomes for counties around Million-Rouble plants
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  data_note: The article identifies NBS above-scale firm data (ASIF) for 1998-2007, using establishment product descriptions, production functions, patent links, and markup calculations. The authors' README says the raw ASIF input is proprietary and must be purchased or obtained through a licensed route; the Zenodo package provides code and public inputs but not the confidential ASIF files.
- cite: 'Chen, Chen, Liu, Suárez Serrato & Xu (2025), Regulating Conglomerates: Evidence from an Energy Conservation Program in China'
  doi: https://doi.org/10.1257/aer.20211455
  journal: AER
  year: 2025
  dataset_role: Firm characteristics and output cross-checks for Top 1,000/Top 10,000 firms; matched to CESD and CARD
  evidence_type: data_appendix
  evidence_url: https://assets.aeaweb.org/asset-server/files/22048.pdf
  data_note: The appendix reports ASIF matches for 1,001 of 1,008 Top 1,000 firms and 14,227 of 14,641 Top 10,000 firms, and
    uses ASIF output and firm controls over the 2001–2010 paper window (with tax/ATS data used for specified robustness fills).
    The openICPSR package lists Raw_Data/ASIF but does not turn the underlying restricted survey into a public release.
- cite: 'Kee & Tang (2016), Domestic Value Added in Exports: Theory and Firm Evidence from China'
  journal: AER
  year: 2016
  dataset_role: ASIF matched with customs transaction-level data as the main firm-level source for computing enterprise export domestic value-added rates (DVAR)
  evidence_type: article_and_replication
  evidence_url: https://www.aeaweb.org/articles?id=10.1257/aer.20131687
  data_note: Using ASIF+ customs transaction-level data to calculate the domestic value-added rate (DVAR) of enterprise exports,
    it was found that it rose from 65% to 70% from 2000 to 2007, and the main reason was the substitution of imported intermediate
    products.
- cite: Huang, Pagano & Panizza (2020), Local Crowding-Out in China
  journal: JF
  year: 2020
  dataset_role: 2006–2013 industrial enterprise database as the main firm panel for private-firm investment and cash-flow sensitivity in the local-debt crowding-out analysis
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/bla/jfinan/v75y2020i6p2855-2898.html
  data_note: Using the 2006–2013 industrial enterprise database to study the crowding-out effect of local public debt on private
    enterprise investment—private enterprises in high-debt cities invest less and are more sensitive to internal cash flow
- cite: 'Cui & Li (2023), Trade Policy Uncertainty and New Firm Entry: Evidence from China'
  journal: JDE
  year: 2023
  dataset_role: Chinese Industrial Enterprise Database as the main data source for measuring new firm entry
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v163y2023ics0304387823000482.html
  data_note: >-
    Use the Chinese Industrial Enterprise Database to study how the decline in trade policy uncertainty (TPU) affects new business
    entry—the decline in TPU significantly promotes new business entry and competition. Evidence boundary: the JDE abstract (read
    via the IDEAS/RePEc article record) confirms the new-firm-entry and WTO-accession analysis but does not name the Chinese
    Industrial Enterprise Database; the ScienceDirect data section was 403-blocked in this environment.
- cite: 'Xie, Xu & Yu (2024), Trade Liberalization, Labor Market Power, and Misallocation across Firms: Evidence from China''s
    WTO Accession'
  journal: JDE
  year: 2024
  dataset_role: ASIF enterprise-level panel as the main firm data for estimating labor-market wage markdowns and misallocation
  evidence_type: working_paper_data_section
  evidence_url: https://www.lnu.edu.cn/Manuscript.pdf
  data_note: >-
    Using ASIF enterprise-level panel data + China's WTO accession tariff reduction variation, study how trade liberalization
    affects resource misallocation among enterprises by changing the buyer's power (wage markdown) in the labor market. Evidence:
    the author-hosted working paper (Enze Xie, Mingzhi Xu, Miaojie Yu; dated August 13, 2024) names the Chinese Annual Survey of
    Industrial Firms (ASIF) for 1998-2007 as the firm-level production data collected by China's NBS (all SOEs and non-SOEs with
    annual sales above RMB 5 million); the published JDE version's data section remains 403-blocked in this environment.
- cite: Brandt, Van Biesebroeck, Wang & Zhang (2026), Where Has All the Dynamism Gone? Productivity Growth in China's Manufacturing
    Sector, 1998–2013
  journal: JDE
  year: 2026
  dataset_role: ASIF 1998-2013 (with State Administration of Taxation survey data) as the main firm panel for post-2007 quality correction and TFP growth measurement
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v181y2026ics0304387826000039.html
  data_note: >-
    Using ASIF (1998-2013) and State Administration of Taxation tax survey data, the Hellerstein-Imbens method was used to restore
    the implicit sampling weight of the STA survey → correct the ASIF data quality problem after 2007, and found that the TFP
    growth rate plummeted from 3.4-3.9% to 1.1% in 2007 - the contribution of private enterprise vitality and new enterprise entry
    to TFP was significantly attenuated. Evidence: the JDE abstract (read via the IDEAS/RePEc article record) explicitly names the
    NBS annual survey of industrial firms as the key data source and the STA survey as the alternative firm-level source for
    2007-2013.
- cite: 'Qi, Tang & Xi (2021), The Size Distribution of Firms and Industrial Water Pollution: A Quantitative Analysis of China'
  journal: AEJ:Macro
  year: 2021
  dataset_role: ASIF appears only as a comparison sample for firm size distributions in Appendix B (Figure B.1); the paper's
    main firm-level analysis uses the 2004 China National Economic Census full sample and the 2007 National General Survey of
    Pollution Sources
  evidence_type: appendix
  evidence_url: https://www.aeaweb.org/articles/materials/13866
  data_note: >-
    The AEA supplemental appendix (read in full) states that ASIF is used only as a comparison sample: 'while the ASIF data are
    widely used in studies of Chinese economy, we use the CNEC full sample in our paper, because both the small and large firms
    play a critical role in our empirical and quantitative analysis' (ASIF sample misses most small firms; Figure B.1 compares
    ASIF, NGSPS and CNEC firm size distributions). The main empirical analysis (Section I.B) draws on the 2007 National General
    Survey of Pollution Sources; the appendix also uses the 2004 China National Economic Census and U.S. Statistics of
    Businesses. The earlier data_note overclaim ('ASIF enterprise-level data as the main source for the firm size distribution')
    is corrected to this appendix-documented boundary. The paper's findings (eliminating correlated distortions would raise
    output ~30% and cut pollution ~20%) are confirmed by the AEA abstract and openICPSR record E112005V5.
- cite: 'Tian, Wang & Zhang (2024), Land Allocation and Industrial Agglomeration: Evidence from the 2007 Reform in China'
  journal: JDE
  year: 2024
  dataset_role: ASIF 2005-2010 as the firm-level outcome data (entry, employment, manufacturing TFP) in the 2007 land-reform DID analysis
  evidence_type: working_paper_data_section
  evidence_url: http://www.cfrn.com.cn/uploads/master/file/20240328/66058c34f30d9.pdf
  data_note: Using ASIF (2005-2010) + land transaction data (2143 counties) + 2004 economic census, and taking the 2007 industrial
    land bidding and auction reform as DID - the transparency of land distribution has enabled new enterprises in specialized
    matching industries to enter ↑3.6% and create employment ↑23%, and the country's newly entered manufacturing TFP has increased
    by 1.3% cumulatively.
- cite: 'Wu, Yu & Zhang (2023), Road Expansion, Allocative Efficiency, and Pro-Competitive Effect of Transport Infrastructure:
    Evidence from China'
  journal: JDE
  year: 2023
  dataset_role: ASIF 1998-2007 as the main firm data for the markup-dispersion measure of allocative efficiency
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v162y2023ics0304387823000056.html
  data_note: Use ASIF (1998-2007) enterprise markup rate dispersion to measure resource allocation efficiency + minimum cost
    path IV + network algorithm IV - road expansion makes the markup rate dispersion ↓ 28.8%, verifying the pro-competitive
    effect of transportation infrastructure (high markup rate enterprises reduce prices)
- cite: 'Jing & Liao (2026), Expressways, Market Access, and Industrial Development in China: Using Walled-City Panel Instrumental
    Variables of Minimum Spanning Tree'
  journal: JDE
  year: 2026
  dataset_role: ASIF micro-enterprise data as the firm-level source for manufacturing GDP and firm-count outcomes
  evidence_type: working_paper_data_section
  evidence_url: https://www.nsd.pku.edu.cn/docs/20190828105530904640.pdf
  data_note: >-
    Using ASIF micro-enterprise data + 2000-2009 county-level panel + 1820 walled city MST instrumental variable - highways make
    manufacturing GDP ↑0.28% / number of enterprises ↑0.07%, promote the transfer of capital-intensive industries to the inland,
    and reshape the economic geography pattern. Evidence: the NSD working-paper version (same authors, Kecen Jing and Wen-Chi
    Liao; URL-dated 2019-08-28) data section explicitly names the Annual Surveys of Industrial Firms (ASIF) conducted by the NBS
    for 2000-2009 firm performance, with four years (2000, 2003, 2006, 2009) used; the published JDE 2026 version (walled-city MST
    IV subtitle) data section remains 403-blocked in this environment, and the 0.28%/0.07% county-level results are read from the
    published abstract.
- cite: 'Huang, Li, Ma & Xu (2017), Hayek, Local Information, and Commanding Heights: Decentralizing State-Owned Enterprises
    in China'
  doi: https://doi.org/10.1257/aer.20150592
  journal: AER
  year: 2017
  dataset_role: Main SOE firm panel; joined with decentralization events and geographic distance to oversight governments
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/113063/
  data_note: Used ASIF 1998–2007 to identify SOEs by registration type and state ownership share (~17,500 unique SOEs).
    Combined with geographic distance to oversight government and communication costs to test Hayek's local-information theory
    — SOEs farther from government oversight are more likely to be decentralized, especially when communication costs are higher.
    The AEA-linked openICPSR V1 project (DOI 10.3886/E113063V1) lists the paper's 20150592_data folder, a 36.8 MB
    AER_2015_0592_R2__Data.zip, Readme.pdf, appendix170123.do, figures, and named SOE DTA files. The current download
    action redirected to ICPSR login; these deposited analysis files must not be treated as a public copy of the complete ASIF source.
- cite: 'Lian & Zhang (2026), Allocative Implications of Government Investment in Private Sector'
  doi: https://doi.org/10.1016/j.jdeveco.2025.103616
  journal: JDE
  year: 2026
  dataset_role: ASIF 1998-2007 firm-level panel used to calibrate the two-sector DSGE model
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v179y2026ics0304387825001671.html
  data_note: 'Uses ASIF 1998-2007 firm-level panel data to calibrate a two-sector DSGE model of state capital allocation to private
    firms. Documents that state equity participation raises firm leverage by 1.22% but lowers TFP by 5.38%, and finds that
    government investment in the private sector improves both within-sector and cross-sector capital allocation efficiency
    through selection: only high-productivity private firms accept state capital, and only low-productivity SOEs supply it.'
- cite: 'Feng & Zhang (2025), Limited Liability, Piercing the Corporate Veil and Pollution Abatement: Evidence from China'
  doi: https://doi.org/10.1016/j.chieco.2025.102529
  journal: CER
  year: 2025
  dataset_role: ASIF firm financial panel 2002-2013; treatment identification via corporate group affiliation (Qichacha)
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S1043951X25001877
  data_note: Uses ASIF manufacturing panel matched with Qichacha corporate group affiliation data and China Environmental Survey emissions. Exploits 2006 Company Law revision introducing Piercing the Corporate Veil (PCV) as PSM-DID. Finds PCV significantly reduces subsidiary pollution intensity — subsidiaries strengthen process control and end-of-pipe treatment rather than cutting output. Documents internal pollution shifting from high-pollution to low-pollution subsidiaries within business groups.
- cite: 'Tang, Wang & Qi (2026), Does Decentralization Improve Allocative Efficiency? Evidence from the Province-Managing-County Reform in China'
  doi: https://doi.org/10.1016/j.regsciurbeco.2026.104230
  journal: RSUE
  year: 2026
  dataset_role: ASIF manufacturing firm panel 2002-2013; difference-in-differences comparing reformed counties with unreformed counties
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0166046226000202
  data_note: Uses ASIF firm-level panel for 2002-2013 to study Province-Managing-County (省直管县) fiscal reform effects on capital and labor allocation. Finds capital increased by 41% and employment by 23% in high-distortion (high-MRPK) reformed-county firms relative to unreformed counties — reform reduces fiscal extraction by prefecture governments, allowing counties to retain more revenue and improve allocative efficiency.
- cite: 'Gerritse, Wang & van Oort (2026), Industrial Transfer Policy in China: Migration and Development'
  doi: https://doi.org/10.1016/j.jue.2025.103815
  journal: JUE
  year: 2026
  dataset_role: NBS Annual Survey of Industrial Firms (ASIF) firm-level supplement for 2011-2013 manufacturing outcomes linked to destination cities
  evidence_type: paper_data_section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0094119025000804
  data_note: The paper's data section and Appendix L state that the NBS ASIF is used for firm-level revenue, productivity, employment, and capital outcomes between 2011 and 2013; the appendix describes firms with sales above 20 million RMB and restricts the analysis to manufacturing firms, which are about 90% of observations. This is a paper-use boundary, not evidence of a new public ASIF release or a causal-variation record.
- cite: 'Mo & Zhang (2024), Neighboring Capital Imports and Non-Importer Productivity: Evidence from Geocoded Manufacturing Firms in China'
  doi: https://doi.org/10.1016/j.jue.2024.103692
  journal: JUE
  year: 2024
  dataset_role: ASIF manufacturing firm panel 2000-2006; geocoded for spatial proximity measurement
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0094119024000627
  data_note: Uses geocoded ASIF firm panel (2000-2006) with firm-level TFP estimation and spatial proximity measures. Finds neighboring firms' capital goods imports within 10km raise non-importing firms' TFP by 0.99% on average — six times the productivity gain from own R&D. Non-importers constitute 87.6% of manufacturing firms, and spillovers operate through supply-chain linkages (upstream-downstream capital goods) rather than learning effects, decaying beyond 10km.
- cite: 'Lin & Xi (2026), Impact of Place-Based Policy on Land Lease Price and Its Productivity Premium: Evidence From China''s Development Zone Program'
  doi: https://doi.org/10.1111/jors.70064
  journal: JRS
  year: 2026
  dataset_role: ASIF firm production panel matched with development-zone and land-parcel spatial data
  evidence_type: data-section
  evidence_url: https://onlinelibrary.wiley.com/doi/abs/10.1111/jors.70064
  data_note: Uses ASIF firm-level data linked to development zone boundaries and land transaction parcels in a boundary discontinuity design. Finds development zones raise land lease prices which function as a screening mechanism — higher land costs filter out low-productivity firms. Within zones, competition and agglomeration effects boost incumbent firm TFP. Documents land prices as a key mediating channel through which place-based policies affect firm productivity.
- cite: 'Hau & Ouyang (2024), Can Real Estate Booms Hurt Firms? Evidence on Investment Substitution'
  doi: https://doi.org/10.1016/j.jue.2024.103695
  journal: JUE
  year: 2024
  dataset_role: ASIF manufacturing firm panel (~900K firms, 2002-2007); core firm investment and productivity outcomes
  evidence_type: data-section
  evidence_url: https://ideas.repec.org/a/eee/juecon/v144y2024ics0094119024000652.html
  data_note: Uses ASIF firm panel (~900K manufacturing firms, 2002-2007) combined with 172 prefecture-level city housing price and land supply data and Customs trade data. Exploits exogenous variation in Chinese cities' residential land supply as an IV for housing prices. Finds that real estate price booms crowd out manufacturing firms' productive investment — a 10 log-point housing price increase reduces firms' fixed investment by 2.6% and TFP by 0.8%.
- cite: 'Zhao, Ploegmakers, Rouwendal & Ma (2024), Land Investment Regulation and Allocative Efficiency: Evidence from the Chinese Manufacturing Sector'
  doi: https://doi.org/10.1093/jeg/lbae024
  journal: JEG
  year: 2024
  dataset_role: ASIF firm panel (20,205 newly established firms 2007-2014); matched with land lease records
  evidence_type: data-section
  evidence_url: https://academic.oup.com/joeg/article/25/2/151/7725676
  data_note: Matches 20,205 newly established manufacturing firms (2007-2014) from ASIF with land lease records to estimate firm-level land production functions. Finds average land productivity gap of ~310 yuan/m² — over 30× the average land input cost — driven by China's Minimum Investment Intensity (MII) regulation. Uses spatial border discontinuity design at county boundaries to show MII regulation causes substantial land allocative inefficiency, extending misallocation research to the factor land.
- cite: 'Jiang, Yuan & Li (2024), Agglomeration Externalities, Industry Life Cycle and Firm Survival: Evidence from Chinese Manufacturing Start-ups'
  doi: https://doi.org/10.1080/00343404.2024.2417702
  journal: Regional Studies
  year: 2024
  dataset_role: ASIF panel — 95,090 manufacturing start-ups across 284 prefecture-level cities (1999-2013)
  evidence_type: data-section
  evidence_url: https://rsa.tandfonline.com/doi/suppl/10.1080/00343404.2024.2417702
  data_note: Uses 95,090 manufacturing start-ups from ASIF covering 284 prefectures, 29 two-digit and 509 four-digit industries (1999-2013) in discrete-time cloglog hazard models. Finds agglomeration externalities' effect on firm survival depends on industry life cycle — specialization and related variety reduce failure risk in growth/middle stages, while unrelated variety matters only at maturity. First study to integrate industry life cycle with agglomeration externalities for firm survival in China.
- cite: 'Zhang & Nguyen (2024), A Regional Perspective on the Privatisation of Chinese State-Owned Firms'
  doi: https://doi.org/10.1080/00343404.2024.2396362
  journal: Regional Studies
  year: 2024
  dataset_role: ASIF SOE panel — 63,599 firm-year observations covering 18,464 state-owned enterprises (1999-2013)
  evidence_type: data-section
  evidence_url: https://www.tandfonline.com/doi/full/10.1080/00343404.2024.2396362
  data_note: Uses ASIF data on 18,464 SOEs (63,599 firm-year obs, 1999-2013) during China's mass privatization era. DiD analysis finds privatization enhances SOE capacity utilization efficiency on average, with stronger effects in regions with higher marketization and Confucian values. Mainland Chinese private shareholders significantly improve performance while foreign shareholders show no significant effect on average, and HMT shareholders weaken privatization benefits in low-marketization regions.
- cite: 'Guo, Zhou, Feng & Hewings (2024), Chinese Firms'' Resilience After Financial Crisis in the Context of Local Economic Growth Targets'
  doi: https://doi.org/10.1080/00343404.2024.2354367
  journal: Regional Studies
  year: 2024
  dataset_role: ASIF firm panel; firm resilience measured as post-crisis recovery; cleaned following Brandt et al. (2012)
  evidence_type: data-section
  evidence_url: https://www.tandfonline.com/doi/full/10.1080/00343404.2024.2354367
  data_note: Uses ASIF firm-level data (cleaned per Brandt et al. 2012; 2010 excluded due to missing obs) to study how local economic growth targets affect firm resilience post-financial crisis. Finds ambitious growth targets boost firm resilience — local officials mobilize resources to meet targets under China's political centralization cum economic decentralization system. Effects stronger for large firms and foreign-owned firms, but distorted resource allocation creates long-term risks.
- cite: 'Huang, Jia & Ge (2024), Forced to Innovate? Consequences of United States'' Anti-Dumping Sanctions on Innovations of Chinese Exporters'
  doi: https://doi.org/10.1016/j.respol.2023.104899
  journal: Research Policy
  year: 2024
  dataset_role: ASIF firm panel 2000-2009; firm financials, employment, and export outcomes matched with Customs and patent data
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S004873302300183X
  data_note: Uses ASIF firm panel (2000-2009) matched with China Customs and CNIPA patent data. DiD on US anti-dumping sanctions against Chinese exports finds targeted firms significantly increase patented innovations — especially substantive invention patents. Firm financial and employment data from ASIF control for size, productivity, and ownership in the innovation response estimation.
- cite: 'Rong, Wang & Zhang (2026), Does Real Estate Expansion Hurt Manufacturing Employment: Evidence from China'
  doi: https://doi.org/10.1016/j.labeco.2026.102889
  journal: Labour Economics
  year: 2026
  dataset_role: ASIF/ASIE balanced panel of manufacturing firms across 70 major cities (2000-2009)
  evidence_type: replication
  evidence_url: https://data.mendeley.com/datasets/btk3vktc2s/2
  data_note: >-
    Uses ASIF/ASIE manufacturing firm panel (2000-2009, 70 major Chinese cities) combined with city-level real estate investment and housing price statistics, and province-level residential land transfer data as instrumental variable. IV estimates find a 10% increase in real estate investment reduces manufacturing firm employment by 1.46%. Adverse effect operates through rising wage costs rather than reduced capital formation. Stronger for private firms and firms in eastern/central cities; little effect on SOEs. Rural-urban migrant workers absorb construction demand shock.
provenance:
- source: Crossref abstract for https://doi.org/10.1257/aer.20191234 (supports the data type and years used by the paper)
  added: '2026-07-07'
  confidence: high
  verified: false
- source: openICPSR replication package doi:10.3886/E152203V1 (the page was intercepted by Cloudflare and the codebook was
    not read)
  added: '2026-07-07'
  confidence: med
  verified: false
- source: The overall attributes of the data set are based on common knowledge in the academic community (corrected by Brandt
    et al., NBS sources, etc.)
  added: '2026-07-07'
  confidence: high
  verified: false
- source: https://assets.aeaweb.org/asset-server/files/22048.pdf
  field_scope:
  - AER paper use
  - ASIF match rates
  - 2001–2010 output/control role
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://doi.org/10.3886/E196012V1
  field_scope:
  - paper replication folder boundary
  - public-versus-confidential input distinction
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  field_scope:
  - ReStud paper use of NBS above-scale firm data
  - 1998-2007 establishment-level role
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/20671189
  field_scope:
  - ReStud replication route
  - proprietary-versus-public ASIF boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: Zenodo record API 10.5281/zenodo.20671189 (queried 2026-09-28)
  field_scope:
  - current open CC-BY-4.0 status
  - PUBLIC_PACKAGE.zip and README.pdf inventory
  - current paper-specific replication-package identity
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845
  field_scope:
  - ReStud 1998-2013 firm-data use
  - 139-project matching role
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/19175276
  field_scope:
  - synthetic replication boundary
  - ASIF/China Industrial Enterprises Database access route named in README
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.aeaweb.org/articles?id=10.1257%2Faer.20150592
  field_scope:
  - AER paper identity
  - publisher-linked replication package route
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/113063/version/V1/view
  field_scope:
  - V1 project identity and citation
  - 20150592_data folder and file manifest
  - 36.8 MB package and named SOE analysis files
  - login/download and repository-processing boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.aeaweb.org/articles/materials/16850
  field_scope:
  - AER paper use
  - ASIF observation unit and 2000–2006 baseline window
  - establishment variables and HS-6 product construction
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/152203/version/V1/view
  field_scope:
  - paper-specific replication route
  - public code/data/results structure
  - public auxiliary file manifest and raw-ASIF boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://academic.oup.com/restud/article/92/6/3611/8099437
  field_scope:
  - ReStud 2025 paper identity
  - NBS firm-data and Clarksons shipyard-data roles
  - province/city and 1998-2013 NBS panel boundary
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.restud.com/wp-content/uploads/2025/02/MS31140manuscript.pdf
  field_scope:
  - data-section description of quarterly Clarksons production data
  - NBS location, fixed-assets, ownership, and matching fields
  - 2010 missing-data limit for investment construction
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://zenodo.org/records/14083198
  field_scope:
  - replication-package identity and public download route
  - CC-BY metadata and code/non-confidential-input boundary
  - proprietary Clarksons and NBS input statement in README
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://www.sciencedirect.com/science/article/pii/S0094119025000804
  field_scope:
  - JUE paper identity, Gerritse/Wang/van Oort authorship, volume 151 (2026), and ASIF role in city-development outcomes
  added: '2026-08-12'
  confidence: high
  verified: true
- source: https://papers.tinbergen.nl/24020.pdf
  field_scope:
  - China City Statistical Yearbook, ASIF, and DMSP supplementary-source description
  - ASIF 2011-2013 coverage, 20-million-RMB sales threshold, manufacturing restriction, and firm-level outcome fields
  added: '2026-08-12'
  confidence: high
  verified: true
related_datasets:
- china-customs
- china-patents
- china-firm-pollution
- csmar
---

## Positioning in one sentence
The China Industrial Enterprise Database (ASIF) is an annual survey of micro-data on industrial (mainly manufacturing) enterprises above designated size.
It is the most commonly used enterprise-level panel data for studying China's corporate operations, productivity, trade and industrial policies.
Long coverage, complete variables, and repeatedly used by top journals - the "number one data" for China's empirical enterprise-level research.

## Research questions suitable for answering/Typical identification strategies
- **Productivity and resource allocation**: Enterprise TFP and markup rate estimation; resource misallocation (misallocation) and reweighted productivity; Hsieh-Klenow type analysis.
- **Trade and Corporate Behavior**: The impact of WTO accession/tariff reduction/export tax rebate on corporate exports, productivity, and product range; use tariff changes as IV.
- **Migration and labor**: How labor supply shocks (such as the scale of migration) affect firm factor intensity and productivity (Imbert et al. 2022 AER approach: use agricultural income shocks as exogenous variation in migration).
- **Policy Assessment (DID/Natural Experiment)**: Environmental protection regulations (two control areas, inspections), minimum wages, development zones/industrial policies, etc., use the staggered differences of policies in regions/time points to do DID.
- **Not suitable**: service industry, non-standard small businesses, after 2014 (public micro data ends around 2013), family/individual level issues.

## Key variables/modules
- Financial module: output value/value added/assets/liabilities/income/profit/tax
- Element modules: employees, fixed assets, wages
- Trade module: Export delivery value (export only, no import flow; import requires customs data)
- Background: Industry (4 digits), region (county/city/province), ownership, affiliation, year of establishment

## How to get
1. Start by asking the university library or data administrator whether it has purchased a specifically named ASIF/industrial-enterprise module, what years and fields it contains, and what export and reuse conditions apply. CNRDS, CSMAR and other commercial platforms are possible processed distribution channels, not evidence that every institution, module or historical edition is available.
2. If no licensed module is confirmed, treat the original NBS survey as a controlled-data question rather than as a public download. The Micro Data Lab and paper-specific provider references are leads that require a current, written confirmation of the applicable catalogue, eligible project scope, edition and output conditions.
3. Use a paper's Zenodo or openICPSR replication package to inspect its code, released auxiliary inputs and derived files only. Such a package can clarify the expected ASIF input, but it does not supply a general ASIF panel or establish a current route through an overseas archive or a named university.
4. Before starting analysis, retain the exact acquired edition, year coverage, field list, cleaning documentation, licence and retrieval date. If those cannot be confirmed, choose a documented alternative or describe the design as non-reproducible rather than treating a familiar platform name as access.

## Connections to other data
- Use "Enterprise Name/Organization Code" to match **China Customs Database** → Get the detailed product-destination country flow of the enterprise's import and export.
- Use "company name/patent applicant" to match **Chinese patent data (CNIPA)** → research innovation (Imbert et al. use patents to look at production reorganization).
- Use "county/city code" to match **statistical yearbook, policy time point, geographical weather**→ to construct policies or exogenous impacts at the regional level.
- Use "Industry Code" to match **Industry Tariff/Input-Output Table** → Trade liberalization analysis.

## Remarks / Pitfalls
- **Matching across years**: Enterprise codes will change, and it is often necessary to use "enterprise name + legal person code + phone number + zip code" multi-key joint matching (Brandt et al. 2012 method).
- **Measurement definition Breakpoint**: The scale threshold was raised from 5 million to 20 million yuan in 2011, and the samples before and after cannot be directly connected; the data quality from 2008 to 2010 is recognized to be poor.
- **Variable outliers**: There are false positives in profits, added value, etc., and winsorize and logical verification are required according to the literature convention.
- **Import not included**: Only export delivery value, import flow must be accompanied by customs data.
- **Does not cover service industry**: Service industry enterprises need to use census data or tertiary industry survey.

<!--
  Traceability instructions (honest labeling):
  Data type and year (manufacturing enterprises 2000-2006) come from the paper Crossref abstract (high confidence).
  The replication package codebook has not been read due to Cloudflare interception of openICPSR, so verified=false.
  The overall attributes of the data set (coverage, variables, pitfalls) come from public knowledge in the academic community and are marked as "high confidence but not verified item by item".
  The next time you have a chance to read the replication package/original codebook, you should complete the fields and mark verified=true.
-->
