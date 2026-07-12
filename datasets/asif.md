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
  last_checked: '2026-07-10'
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
  - Priority is given to CSMAR/Wind when studying the overall unlisted manufacturing industry and corporate production.
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
  and proper name/code changes are common. Not suitable for use in service industries and non-standard enterprises.'
quality:
  profile_status: partial
  access_status: needs-verification
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Imbert, Seror, Zhang & Zylberberg (2022), Migrants and Firms: Evidence from China'
  journal: AER
  year: 2022
  data_note: Using the 2000–2006 manufacturing enterprise panel and using agricultural income shocks as the exogenous variation
    of migration, we study the impact of migration on enterprise production organization.
- cite: 'Kee & Tang (2016), Domestic Value Added in Exports: Theory and Firm Evidence from China'
  journal: AER
  year: 2016
  data_note: Using ASIF+ customs transaction-level data to calculate the domestic value-added rate (DVAR) of enterprise exports,
    it was found that it rose from 65% to 70% from 2000 to 2007, and the main reason was the substitution of imported intermediate
    products.
- cite: Huang, Pagano & Panizza (2020), Local Crowding-Out in China
  journal: JF
  year: 2020
  data_note: Using the 2006–2013 industrial enterprise database to study the crowding-out effect of local public debt on private
    enterprise investment—private enterprises in high-debt cities invest less and are more sensitive to internal cash flow
- cite: Hu, Li, Lin & Wei (2024), What Causes Privatization? Evidence from Import Competition in China
  journal: Management Science
  year: 2024
  data_note: Using the trade liberalization after China's accession to the WTO as the impact of product market competition,
    we study how import competition promotes the privatization of state-owned enterprises - the proportion of private ownership
    increases when SOEs face higher competition.
- cite: 'Cui & Li (2023), Trade Policy Uncertainty and New Firm Entry: Evidence from China'
  journal: JDE
  year: 2023
  data_note: Use the Chinese Industrial Enterprise Database to study how the decline in trade policy uncertainty (TPU) affects
    new business entry—the decline in TPU significantly promotes new business entry and competition
- cite: 'Xie, Xu & Yu (2024), Trade Liberalization, Labor Market Power, and Misallocation across Firms: Evidence from China''s
    WTO Accession'
  journal: JDE
  year: 2024
  data_note: Using ASIF enterprise-level panel data + China's WTO accession tariff reduction variation, study how trade liberalization
    affects resource misallocation among enterprises by changing the buyer's power (wage markdown) in the labor market.
- cite: Brandt, Van Biesebroeck, Wang & Zhang (2026), Where Has All the Dynamism Gone? Productivity Growth in China's Manufacturing
    Sector, 1998–2013
  journal: JDE
  year: 2026
  data_note: Using ASIF (1998-2013) and State Administration of Taxation tax survey data, the Hellerstein-Imbens method was
    used to restore the implicit sampling weight of the STA survey → correct the ASIF data quality problem after 2007, and
    found that the TFP growth rate plummeted from 3.4-3.9% to 1.1% in 2007 - the contribution of private enterprise vitality
    and new enterprise entry to TFP was significantly attenuated
- cite: 'Qi, Tang & Xi (2021), The Size Distribution of Firms and Industrial Water Pollution: A Quantitative Analysis of China'
  journal: AEJ:Macro
  year: 2021
  data_note: Using ASIF enterprise-level data + water pollution emission data, it is found that the size distribution of Chinese
    industrial enterprises is distorted (large enterprises face higher distortion) → Large enterprises are more likely to
    adopt clean technologies but are inhibited → Eliminating relevant distortions can increase output ↑30% + pollution ↓20%
- cite: 'Tian, Wang & Zhang (2024), Land Allocation and Industrial Agglomeration: Evidence from the 2007 Reform in China'
  journal: JDE
  year: 2024
  data_note: Using ASIF (2005-2010) + land transaction data (2143 counties) + 2004 economic census, and taking the 2007 industrial
    land bidding and auction reform as DID - the transparency of land distribution has enabled new enterprises in specialized
    matching industries to enter ↑3.6% and create employment ↑23%, and the country's newly entered manufacturing TFP has increased
    by 1.3% cumulatively.
- cite: 'Wu, Yu & Zhang (2023), Road Expansion, Allocative Efficiency, and Pro-Competitive Effect of Transport Infrastructure:
    Evidence from China'
  journal: JDE
  year: 2023
  data_note: Use ASIF (1998-2007) enterprise markup rate dispersion to measure resource allocation efficiency + minimum cost
    path IV + network algorithm IV - road expansion makes the markup rate dispersion ↓ 28.8%, verifying the pro-competitive
    effect of transportation infrastructure (high markup rate enterprises reduce prices)
- cite: 'Jing & Liao (2026), Expressways, Market Access, and Industrial Development in China: Using Walled-City Panel Instrumental
    Variables of Minimum Spanning Tree'
  journal: JDE
  year: 2026
  data_note: Using ASIF micro-enterprise data + 2000-2009 county-level panel + 1820 walled city MST instrumental variable
    - highways make manufacturing GDP ↑0.28% / number of enterprises ↑0.07%, promote the transfer of capital-intensive industries
    to the inland, and reshape the economic geography pattern
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
1. Priority for universities: download the processed version through the "Industrial Enterprise Research" subscription module of CNRDS / CSMAR (the easiest).
2. Original micro data: Upon application from the National Bureau of Statistics or university data centers (such as Fudan and Tsinghua), a confidentiality agreement is required.
3. Overseas: Some versions are provided by the University of Michigan ICPSR/China Data Center.

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
