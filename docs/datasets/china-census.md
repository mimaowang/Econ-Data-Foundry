---
schema_version: 2
catalog_status: ready
id: china-census
name: China Census (Population Census/National 1% Population Sample Survey)
aka:
- 人口普查
- 全国人口普查
- Population Census of China
- Chinese Census
- 中国人口普查数据
- 五普/六普/七普
- 1%抽样调查
- 小普查
- Mini-Census
- 全国1%人口抽样调查
provider: National Bureau of Statistics (NBS, National Bureau of Statistics of China)
china_related: true
domains:
- labor
- demography
- development
- public
- macro
- health
- education
unit_of_observation: Individual/family household/collective household (micro level); can be aggregated to counties/cities/provinces
structure: decennial-census-and-sample
geo_granularity:
- personal
- family household
- village/community
- Township/street
- County
- city
- province
geography: All of mainland China (including all provinces/autonomous regions/municipalities except Hong Kong, Macao and Taiwan)
time_span:
  start: '1982'
  end: '2020'
  last_confirmed_release: '2020 Seventh National Population Census aggregates; IPUMS China samples through 2000'
  coverage_note: >-
    Large census: 1990 (fourth census), 2000 (fifth), 2010 (sixth) and 2020
    (seventh); 1% surveys: 1995, 2005 and 2015; 1982 third census and
    earlier historical censuses also exist. This record's directly described
    microdata route is IPUMS 1982/1990/2000 only.
  last_checked: '2026-09-28'
paper_specific_restud_windows: The ReStud Million-Rouble Plants paper's data section lists population censuses in 1953, 1964, 1982, 1990, 2000, and 2010 plus the 2015 1% Population Survey for county population, urbanization, migration, and sector measures. Its README separately identifies the 2000/2010 census and 2005/2015 1% survey inputs as non-purchasable NBS data; this is not evidence of a public all-wave microdata release.
frequency:
- decennial census
- intercensal one-percent sample survey
sample_size: Large censuses cover the entire population of the country (billions); small censuses sample about 1% (tens of
  millions); microdata samples (long table/short table) usually range from millions to tens of millions of personal records
key_variables:
- age
- gender
- nation
- Household registration type (agricultural/non-agricultural)
- Place of household registration
- Current residence (province/city/county)
- Migration status (whether you left the place of household registration, length of departure, reason for departure)
- education level
- Marital status
- Number of children born
- Employment status
- Career
- Industry
- housing type
- Housing area
- Year when the house was built
- Household structure (head of household/spouse/children/parents)
- place of birth
- Place of permanent residence five years ago (Fifth Census/Sixth Census)
- Is it literate?
- Health status (some years)
good_for:
- Determinants and consequences of internal migration - gravity model estimation of bilateral migration flows (Tombe & Zhu
  2019 AER uses the Fifth Census and the 2005 Small Census to construct an inter-provincial migration matrix)
- The economic consequences of skewed sex ratios—how regional/cohort-level marriage market pressure affects savings rates
  (classic identification of Wei & Zhang 2011 JPE)
- Population structure and economic growth - the impact of working-age population proportion, dependency ratio, and aging
  on regional economic growth
- Human capital and returns to education - Estimating wage premiums by education/experience/region using census microdata
- Household registration/household registration system and welfare inequality—differences in living conditions, education,
  and employment between agricultural and non-agricultural household registrations
- Urbanization and urban systems—micro-observations of city size distribution, commuting patterns, and urban agglomeration
  formation
identification:
- Census observations support descriptive or cross-sectional demographic comparisons; they do not themselves supply a causal assignment.
linkable_keys:
- County code
- City code
- Provincial code
- Industry code
- Occupation code
research_fit:
  best_for:
  - County/city/provincial measures of population migration matrix, sex ratio and population structure
  - Census cross-sectional comparison of household registration, education and labor force structure
  choose_over:
  - Select Census when you need nationwide county-level coverage, usual residence five years ago, or cross-census population
    benchmarks
  - Choose CFPS/CHFS when annual household panels, balance sheets or detailed causal results are needed rather than treating
    the census as a panel
  not_good_for:
  - annual family panel
  - Full balance sheet of household financial results
  - Enterprise production and trade micro results
  needs_join_for:
  - Pollution, policy, education and economic results need to be joined by county/city/province and year
  - Household savings or other behavioral results usually require separate survey microdata such as CHIP/CFPS/CHFS;
    the census-derived sex-ratio table is not the household outcome file
  variation_available:
  - Census and 1% survey waves provide point-in-time observations at documented reference dates.
  - Geographic, cohort, hukou/residence, demographic, education, and labor fields are observed dimensions whose definitions and geographic detail vary by wave.
access:
  url: 'https://data.stats.gov.cn (National Bureau of Statistics Data Query Platform, summary table); Micro Data: https://microdata.stats.gov.cn
    (National Bureau of Statistics Micro Data Laboratory, application required)'
  cost: mixed
  license: Academic research only; microscopic data may not be redistributed and must be used in a secure environment (some
    require on-site analysis in NBS designated laboratories)
  format:
  - csv
  - xlsx (summary table)
  - DTA (microscopic sample)
  api: false
  how_to_get: '1) Summary table: Directly access data.stats.gov.cn to query summary indicators at the national/provincial/city/county
    levels; 2) Micro data: Submit a formal application to the National Bureau of Statistics → Review → Sign a confidentiality
    agreement → Obtain desensitized samples (usually 1% of the long form or 10% of the short form); 3) Some universities/institutions
    (Renmin University, Peking University, Tsinghua University, etc.) have been authorized to be used on campus; 4) IPUMS
    International (international.ipums.org) provides harmonized micro-samples of the 1982, 1990 and 2000 population censuses
    (each about a 1% sample; 1990 Fourth Census ~11.8 million person records, 2000 Fifth Census ~11.8 million person records),
    free of charge but by approved application (proposed research and institutional affiliation required; scholarly/educational
    use only, no redistribution); no China census sample later than 2000 is offered.'
caveats: The microdata acquisition threshold is high and the approval cycle is long (usually 3–6 months); the microscopic
  samples provided by NBS have been desensitized (precise addresses/dates of birth, etc. have been removed); the questionnaires
  and variable definitions of each round of census have changed, and cross-round comparisons need to be aligned; the sampling
  methods and coverage of the small census (1%) and the large census (100%) are essentially different. IPUMS provides samples
  of the 1982, 1990 and 2000 censuses only - censuses after 2000 (2010, 2020) must go through domestic channels. The IPUMS
  sample-characteristics page and current PERWT documentation have displayed inconsistent expansion-factor wording for China
  2000; use the current extract's PERWT/codebook documentation for weighting and re-check the provider documentation before
  treating the summary-page number as authoritative.
access_routes:
- route: NBS aggregate data portal
  access_status: available
  direct_url: https://data.stats.gov.cn/
  requirements:
  - No registration is required to query the public summary table; the specific export capabilities are subject to the current
    functions of the website.
  steps:
  - Open the National Bureau of Statistics data query platform
  - Filter indicators by census topic, region and year
  - Export or record summary tables and save query conditions
  deliverable: Publicly available aggregated indicators at the province/city/county level; not a census microsample
  cost: free
  last_checked: '2026-09-28'
  caveat: >-
    The official portal currently serves a JavaScript application to automated
    clients; that is not a disappearance of the public aggregate route. Use a
    normal browser, preserve the selected indicator, geography and reference
    year, and treat a returned table as an aggregate product rather than a
    microdata extract.
- route: NBS microdata laboratory application
  access_status: needs-verification
  direct_url: https://microdata.stats.gov.cn/
  requirements:
  - formal research project
  - Relying institution
  - Pass review and sign a confidentiality or controlled use agreement
  - Use in designated safe environment
  steps:
  - Confirm target census waves and catalogs in microdata lab
  - Submit project, variant and usage requests
  - Wait for review and sign the agreement
  - Use desensitized samples in approved environments
  deliverable: Approved census micro-sample; waves, variables and carryout ranges are subject to the approval results
  cost: by-application
  last_checked: '2026-07-10'
- route: IPUMS International China census micro-samples (1982/1990/2000)
  access_status: available-with-registration
  direct_url: https://international.ipums.org/international-action/sample_details/country/cn
  requirements:
  - Apply for access via the IPUMS International application form (international.ipums.org/international-action/menu), providing a proposed-research description and institutional affiliation
  - Wait for individual review and approval by IPUMS project staff
  - Accept the electronic license, which requires scholarly and educational use only (including public policy research), no commercial use, no redistribution, and no attempts to identify individuals
  - Note that registrations expire after one year and can be renewed
  steps:
  - Open the IPUMS International samples page and add China 1990 (cn1990a), 2000 (cn2000a), or 1982 (cn1982a)
  - Select variables and submit an extract in the unified IPUMS format
  - Download the extract and review the IPUMS sample, weighting and variable documentation
  deliverable: 'Harmonized about-1% micro-samples of the 1982/1990/2000 censuses. 1990 Fourth Census (cn1990a): stratified
    cluster sample, sample fraction 0.01, ~11,835,947 person records, self-weighting (expansion factor 100). 2000 Fifth Census
    (cn2000a): systematic household sample, sample fraction 0.01, ~11,804,344 person records, flat weighting; current IPUMS
    sample-characteristics page currently reports expansion factor 10, while
    the documented PERWT description previously reported 100 persons per
    China 2000 record. This unresolved provider-documentation conflict is not
    a reason to avoid the route, but the actual downloaded extract and its
    codebook must determine weighting. Geography: GEO1 province (GIS), GEO2
    prefecture/city (GIS), GEO3 county (GIS only for selected urban areas in
    2000). No China sample later than 2000.'
  cost: free
  last_checked: '2026-08-13'
  caveat: Access is by reviewed application, not unconditional direct download. The provider's summary sample page and current
    PERWT documentation have displayed inconsistent expansion-factor wording for China 2000; use the extract/codebook weighting
    documentation and re-check the provider before relying on a summary-page factor. The World Bank Microdata Catalog entry
    CHN_1990_PHC_v01_M_v7.6_A_IPUMS (catalog 462) is a mirror of the same IPUMS 1990 subset and is not an independent source.
- route: AEA/openICPSR Tombe-Zhu V1 replication package
  access_status: available-with-conditions
  direct_url: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view
  requirements:
  - An openICPSR/ICPSR account and the repository's current download terms; the project page exposes metadata without login, while file download currently redirects to login.
  - Read the deposited LICENSE.txt and ReadMe.pdf before treating any file as reusable or redistributable.
  steps:
  - Follow the AEA article's Replication Package link to project 113071, version V1.
  - Inspect the `20150811_data` folder and preserve the file names and version date in the project log.
  - Use `migration_data.dta`, `mij2000.csv`, and `mij2005.csv` as deposited paper-specific migration outputs; do not treat them as the underlying NBS census microdata.
  - If the research needs to rebuild the matrices or change the sample definition, obtain the relevant census waves through an approved NBS or controlled microdata route and document the new construction separately.
  deliverable: A paper-specific replication deposit with migration matrices/derived files and model code; it does not establish a public release of the raw 2000 Census or 2005 1% Population Survey microdata.
  cost: registration
  last_checked: '2026-08-11'
  caveat: The project metadata describes China, 2000-2005, and province-sector-year observations. ICPSR states that materials are distributed as received and have not been reviewed or processed; inspect the README and license for file-level terms.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-13'
used_by:
- cite: 'Imbert, Seror, Zhang & Zylberberg (2022), Migrants and Firms: Evidence from China'
  doi: https://doi.org/10.1257/aer.20191234
  journal: AER
  year: 2022
  dataset_role: Prefecture-to-prefecture rural-urban migration flows and migrant-selection comparisons used to measure destination
    labor-market exposure
  evidence_type: appendix_and_replication
  evidence_url: https://www.aeaweb.org/articles/materials/16850
  data_note: >-
    The AEA appendix identifies the 2005 1% Population Survey (Mini-Census) as the source for migration flows. It is a roughly 1.3%
    sample drawn from about 600,000 primary enumeration districts with three-stage cluster sampling and NBS sampling weights. The
    data record current residence at the prefecture level, hukou location/type, and departure timing, allowing yearly origin-destination
    flows for 2000–2005; the paper also uses earlier migrant cohorts observed in 2000 to describe destination shares. The appendix
    warns about registration-based under-sampling in high-immigration areas, step migration, return migration, and limited geographic
    resolution. The openICPSR deposit supplies cleaning scripts and related files but does not turn the restricted NBS census/microdata
    into a general public release.
- cite: 'Heblich, Seror, Xu & Zylberberg (2026), Industrial Clusters in the Long Run: Evidence from Million-Rouble Plants in China'
  doi: https://doi.org/10.1093/restud/rdag078
  journal: ReStud
  year: 2026
  dataset_role: County-level population, urbanization, migration, and sector outcomes from historical censuses and the 2015 1% survey
  evidence_type: data_section
  evidence_url: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  data_note: The article lists 1953, 1964, 1982, 1990, 2000, and 2010 population censuses and the 2015 1% Population Survey, with wave-specific variables. The replication README says the 2000/2010 census and 2005/2015 1% survey inputs are confidential and must be obtained from NBS or secured university portals; the Zenodo package does not turn them into a general public release.
- cite: 'Tombe & Zhu (2019), Trade, Migration, and Productivity: A Quantitative Analysis of China'
  doi: https://doi.org/10.1257/aer.20150811
  journal: AER
  year: 2019
  dataset_role: 2000 Census and 2005 1% Population Survey inputs for bilateral province-sector migration matrices
  evidence_type: article_and_replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view
  data_note: >-
    The paper uses the 2000 Fifth Census and 2005 1% Population Survey to construct bilateral interprovincial migration matrices
    split into agricultural and non-agricultural sectors. The AEA page classifies the paper under P25, R12 and R23; the linked V1
    deposit describes China, 2000-2005, and province-sector-year observations and lists `migration_data.dta`, `mij2000.csv`, and
    `mij2005.csv`. Those files are deposited migration outputs for the paper's model, not proof that the underlying NBS census
    microdata or the authors' full cleaning procedure is publicly downloadable.
- cite: 'Wei & Zhang (2011), The Competitive Saving Motive: Evidence from Rising Sex Ratios and Savings Rates in China'
  doi: https://doi.org/10.1086/660887
  journal: JPE
  year: 2011
  dataset_role: China Population Census regional/cohort sex-ratio, housing, and population-structure inputs for cross-regional saving analysis
  evidence_type: paper_and_data_appendix
  evidence_url: https://users.nber.org/~confer/2009/China09/wei.pdf
  data_note: >-
    The paper's data appendix identifies county/city sex ratios, age shares, housing area/living space, and housing values as
    Census-derived inputs. It uses the 1990 and 2000 Population Censuses, with the 2000 Census used to infer cohort sex ratios
    for years outside 2000; a 2005 1% Population Survey value appears only in the appendix's supplemental 2005 birth-sex-ratio
    series. Household savings outcomes are from the separate CHIP 2002 survey, not from the Census. These are census-derived
    regional aggregates and inputs, not a public release of the authors' cleaned analysis panel.
- cite: Khanna, Liang, Mobarak & Song (2025), The Productivity Consequences of Pollution-Induced Migration in China
  journal: 'AEJ: Applied'
  year: 2025
  dataset_role: China's population migration data as the migration-flow input for quantifying pollution-induced migration of skilled labor and its effects on total productivity and welfare
  evidence_type: working_paper_data_section
  evidence_url: https://www.nber.org/system/files/working_papers/w28401/w28401.pdf
  data_note: Using China's population migration data and air pollution data, we quantify the impact of pollution-induced migration
    of skilled labor on total productivity and welfare under a spatial equilibrium framework.
- cite: 'Chen, Oliva & Zhang (2022), The Effect of Air Pollution on Migration: Evidence from China'
  journal: JDE
  year: 2022
  dataset_role: County-level migration data from previous censuses as the net in-migration outcome in the air-pollution-and-migration analysis
  evidence_type: working_paper_data_section
  evidence_url: https://www.nber.org/system/files/working_papers/w24036/w24036.pdf
  data_note: Using county-level migration data from previous censuses + atmospheric temperature inversion as IV, it was found
    that a 10% increase in air pollution led to a decrease in net in-migration population of approximately 2.8% - migration
    was mainly driven by highly educated young people
- cite: Guo, Zhang & Zhou (2024), The Demography of the Great Migration in China
  journal: JDE
  year: 2024
  dataset_role: 2010 Sixth National Population Census used to construct the bilateral migration matrix between 331 prefecture-level cities
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v167y2024ics0304387823001918.html
  data_note: Using the 2010 Sixth National Population Census to construct a bilateral migration matrix between 331 prefecture-level
    cities, and using the birth cohort size differences caused by the famine and family planning in the 1960s as an IV—identifying
    how the push and pull forces of demographic structure shape the largest internal migration in human history
- cite: 'Chen, Ding & Tian (2026), The Stalled Quiet Revolution: Population Control, Skewed Sex Ratios, and the Widening Gender
    Gap in Labor Force Participation'
  journal: JDE
  year: 2026
  dataset_role: 1990/2015 census microdata as the cohort-level source for sex-ratio imbalance and female labor force participation outcomes in the family-planning cohort DID
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/deveco/v182y2026ics0304387826000817.html
  data_note: Using 1990/2015 census microdata + CFPS, using the intensity of family planning fines in each province as a cohort
    DID - it is found that the gender ratio imbalance caused by the one-child policy makes women's LFP relative to men's LFP
    through the marriage market channel (female marriage ↑/bargaining power ↑ → leisure choice) ↓~12pp
- cite: 'Almond, Li & Zhang (2019), Land Reform and Sex Selection in China'
  doi: https://doi.org/10.1086/701030
  journal: JPE
  year: 2019
  dataset_role: 1990 Census 1% microdata for sex ratio analysis by birth cohort and birth order
  evidence_type: paper_data_section
  evidence_url: https://www.nber.org/papers/w19153
  data_note: Used 1990 Population Census 1% microdata (births 1974–1986 across 914 counties) to estimate the effect of the Household
    Responsibility System (HRS) land reform on sex selection. Combined with county gazetteer data on HRS rollout timing and
    One Child Policy implementation. Found that post-reform, sex ratio for second births following a firstborn girl rose from
    ~1.1 to ~1.3 — driven by increased household income making sex selection affordable.
- cite: 'Borusyak & Hull (2023), Nonrandom Exposure to Exogenous Shocks'
  doi: https://doi.org/10.3982/ECTA19367
  journal: Econometrica
  year: 2023
  dataset_role: 2000 population counts for 340 prefectures used to weight market access in the China high-speed-rail application
  evidence_type: data_appendix
  evidence_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10795685/
  data_note: >-
    The data appendix uses 2000 Census population for all 340 mainland prefectures (excluding Hainan, Taiwan, Hong Kong and
    Macau, while including six sub-prefecture cities) to construct market-access weights. The paper obtained the population
    series through Brinkhoff (2018), so this is evidence of the Census-derived input and paper use, not a claim that the article's
    cleaned prefecture table is itself a public NBS microdata release.
- cite: 'Au & Henderson (2006), Are Chinese Cities Too Small?'
  doi: https://doi.org/10.1111/j.1467-937X.2006.00387.x
  journal: ReStud
  year: 2006
  dataset_role: 1990 county-level population and agriculture GIS source aggregated to city-level education-attainment controls
  evidence_type: data_appendix
  evidence_url: https://www.brown.edu/Departments/Economics/Faculty/henderson/papers/chinatoosmallcities0905.pdf
  data_note: >-
    Appendix B says education attainment is aggregated from China County-Level Data on Population (Census) and Agriculture,
    keyed to the 1:1M GIS map, 1990. This is a paper-use of a historical census/GIS compilation rather than a claim that the
    current NBS microdata portal offers the same ready-made city-level table.
- cite: 'Author (2026), Urban Internal Structures and Gender Commuting Gap: Evidence from China'
  doi: https://doi.org/10.1016/j.regsciurbeco.2026.104246
  journal: RSUE
  year: 2026
  dataset_role: 2015 1% Population Census microdata — first Chinese census wave with self-reported commuting time (abstract-level)
  evidence_type: abstract-only
  evidence_url: https://ideas.repec.org/a/eee/regeco/v120y2026ics0166046226000566.html
  data_note: >-
    Downgraded from data-section to abstract-only on 2026-08-14 (grounding unit on the NTL family):
    the IDEAS/RePEc article page (fetched 2026-08-14) confirms the paper identity and the abstract
    statement that subcenters were identified from nighttime light data. The paper's own data section
    was NOT read: ScienceDirect is subscriber-only and SSRN is CAPTCHA-blocked in this environment.
    The previously cited SSRN abstract_id=5108088 is unverifiable and conflicts with 5108086 found via
    search-index title match; the 'NASA nightlight data' phrase in the old note is unverifiable from
    any accessible source and is NOT treated as product-level evidence. The exact census waves and the
    exact NTL product used by the paper remain unresolved; see datasets/china-nighttime-lights.md for
    the NTL-family record.
- cite: 'Author (2026), Transportation Infrastructure and College Admissions Quality: Evidence from China''s National College Entrance Examination'
  doi: https://doi.org/10.1016/j.regsciurbeco.2026.104223
  journal: RSUE
  year: 2026
  dataset_role: 2005 and 2015 Population Census data for population mobility validation
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/regeco/v119y2026ics0166046226000335.html
  data_note: >-
    Abstract/bibliographic level only, downgraded on 2026-08-13: the RePEc record
    confirms the paper identity and the abstract-level claim that the paper combines
    HSR connectivity with population-mobility validation using census data, CNRDS
    high-speed-rail data and Sina Gaokao cutoffs (2006-2018). The paper's data
    section was not read when this entry was recorded, so the exact census waves and
    their role are not verified from the paper itself; the finding summary is
    abstract-derived and the author names remain unresolved in this record. Do not
    treat this entry as data-section evidence.
- cite: 'Author (2025), Structural Transformation and the Urban Growth Shadows: County-Level Evidence from China, 1990-2020'
  doi: https://doi.org/10.1016/j.regsciurbeco.2025.104141
  journal: RSUE
  year: 2025
  dataset_role: Four waves of Population Census (1990, 2000, 2010, 2020) covering 2,225 counties
  evidence_type: data-section
  evidence_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4765694
  data_note: Uses four decadal Census waves covering 2,225 counties to construct decadal population growth rates (dependent variable) and inter-county migration flows. Combined with county-level statistical yearbooks for industrial structure and Economic Census data for economic structure. Finds urban growth shadows — larger cities drain population from nearby smaller counties — and that structural transformation (initial agricultural employment share) determines which counties grow vs. shrink.
- cite: 'Author (2025), Skills and the City in China'
  doi: https://doi.org/10.1016/j.regsciurbeco.2024.104082
  journal: RSUE
  year: 2025
  dataset_role: Multiple Census waves (1982, 1990, 2000, 2010, 2015) for city-level skill and wage distributions
  evidence_type: data-section
  evidence_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4517629
  data_note: Uses five Census waves (1982-2015) to construct city-level distributions of occupational skills and wages, combined with CFPS individual-level data and O*NET/DCOC text-based skill intensity measures. Finds that larger Chinese cities disproportionately attract and reward workers with higher cognitive and social skills — skill sorting explains a significant portion of the urban wage premium.
- cite: 'Wang & Felice (2026), Internal Migration and Structural Change in China'
  doi: https://doi.org/10.1111/jors.70049
  journal: JRS
  year: 2026
  dataset_role: IPUMS 2000 Census 1% microdata — migration flows, employment sector, demographics
  evidence_type: data-section
  evidence_url: https://ideas.repec.org/a/bla/jregsc/v66y2026i2p602-625.html
  data_note: Uses IPUMS 2000 Census 1% microdata combined with CMDS and City Statistical Yearbooks to construct prefecture-level internal migration measures and structural change outcomes. Census data provides baseline population distribution and inter-prefecture migration flows for 2SLS estimation of migration's contribution to structural transformation from agriculture to non-agricultural sectors.
- cite: 'Zhang & Zong (2025), Women''s Empowerment and Participation in Innovation: Evidence from the One-Child Policy in China'
  doi: https://doi.org/10.1016/j.respol.2025.105334
  journal: Research Policy
  year: 2025
  dataset_role: 2010 Population Census and 2005 1% Population Sample Survey for regional demographic controls
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S0048733325001635
  data_note: Uses 2010 Census and 2005 1% Mini-Census data for regional demographic and socioeconomic controls in studying how OCP-induced women's empowerment affects innovation participation. Census data provides baseline female education, labor participation, and fertility measures across regions. Combined with CFPS, CMDS, CNIPA patents, and CSMAR.
- cite: 'An, Qin, Wu & You (2024), The Local Labor Market Effect of Relaxing Internal Migration Restrictions: Evidence from China'
  doi: https://doi.org/10.1086/722620
  journal: JLE
  year: 2024
  dataset_role: Population Census data for regional hukou reform exposure and migration stock measurement
  evidence_type: data-section
  evidence_url: https://www.journals.uchicago.edu/doi/10.1086/722620
  data_note: >-
    Uses Population Census data combined with CMDS and CFPS to study how China's 2014 hukou reform affected local labor markets. Census data provides baseline migration stock and regional demographic structure for identifying reform exposure intensity. Finds migrant workers' wages fell by 2.6-7.9% post-reform while local workers' wages were unaffected — competition is within migrant skill groups rather than between migrants and locals.
- cite: 'Qin, Yi & Zhang (2025), Quarter of Birth, Gender Inequality, and Economic Development'
  doi: https://doi.org/10.1086/737993
  journal: JLE
  year: 2025
  dataset_role: Six waves of Population Census (1990, 2000, 2005, 2010, 2015, 2020) covering cohorts born 1940-1995
  evidence_type: replication
  evidence_url: https://opendata.pku.edu.cn/dataverse/pku
  data_note: >-
    Uses six Census waves spanning 1990-2020 as the primary data source to construct birth quarter effects on lifecycle outcomes (education, labor market) across cohorts born 1940-1995. Combined with CFPS, CEPS, CHNS, statistical yearbooks, and meteorological data. Finds Q4 births have better outcomes — effect significantly larger for females, driven by agricultural seasonality interacting with son preference in neonatal investment. Economic development (post-1979 reforms) reduces the gender gap in birth quarter effects.
- cite: 'Lin Zhang (2024), Longer Time for School: The 1981 Marriage Law and Rural Female Education in China'
  doi: https://doi.org/10.3368/jhr.0822-12475R5
  journal: JHR
  year: 2024
  dataset_role: Population Census microdata for cohort-level educational attainment of rural women by birth year and province
  evidence_type: inferred-from-methods
  evidence_url: https://jhr.uwpress.org/content/early/2024/07/09/jhr.0822-12475R5
  data_note: >-
    Uses Population Census microdata (inferred from cohort-DID methodology exploiting 1981 Marriage Law reform) to measure rural female educational attainment by birth cohort. Treats the 1981 Marriage Law raising women's minimum marriage age from 18 to 20 as a natural experiment. Finds significant improvement in rural women's upper secondary school enrollment — extended pre-marriage schooling duration drives the effect. Regression probability jump/kink with DiD and cohort DiD designs.
- cite: 'Fang & Miao (2024), Expanding Boundaries: The Impact of Kindergarten Availability on Women''s Employment in China'
  doi: https://doi.org/10.1016/j.labeco.2024.102542
  journal: Labour Economics
  year: 2024
  dataset_role: 2010 Population Census microdata; primary data source for RDD on kindergarten eligibility and maternal employment
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S092753712400037X
  data_note: >-
    Uses 2010 Population Census microdata as the primary data source for a regression discontinuity design exploiting the August 31 cutoff for kindergarten eligibility (children must turn 3 by August 31 to enroll). Compares mothers with children just above vs. below the age threshold. Finds rural mothers' non-agricultural employment probability increases by 2.9pp and weekly hours by 1.1 hours. Urban mothers show no significant effect (private childcare alternatives). Grandmother spillover — rural grandmothers' non-agricultural employment increases by 1.6pp.
- cite: 'Chen Chen (2025), Long-Run Impacts of Fertility Restriction Policy on China''s Gender Gap in Career Advancement'
  doi: https://doi.org/10.1016/j.labeco.2025.102782
  journal: Labour Economics
  year: 2025
  dataset_role: Census and population statistics for constructing provincial fertility policy exposure (Expected Reduction Rate)
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S092753712500106X
  data_note: >-
    Uses Census-based fertility data and population statistics to construct provincial-level Expected Reduction Rate (ERR) in fertility as the policy exposure measure for China's "Later, Longer, Fewer" (LLF) campaign of the 1970s. Combined with CGSS (2003-2021, 12 waves). Cohort triple-difference finds LLF reduced the gender gap in attaining managerial positions by ~20% and administrative rank by ~18%. Mechanism — women pursued more college education and increased labor input. Effects stronger in state sector (~25%).
- cite: 'Qian (2025), Market-Oriented Reforms and Human Capital Reallocation in Urban China: A Gender Perspective'
  doi: https://doi.org/10.1016/j.labeco.2025.102811
  journal: Labour Economics
  year: 2025
  dataset_role: Population Census data (1990, 2000, 2010) for documenting occupational and educational distributions over time
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0927537125001356
  data_note: >-
    Uses Population Census waves (1990, 2000, 2010) combined with UHS (1986-2014, 1M+ individuals) to document the transformation of China's urban labor market occupational and educational structure. Census data calibrates the quantitative general equilibrium model of occupational choice with gender-specific education wedges. Market-oriented reforms (abolition of job assignment 1993-1996, college expansion 1999) reduced occupational mismatch by ~19% and raised aggregate output by ~0.8%. Female education barriers in high-skill occupations account for ~80% of efficiency losses.
- cite: 'Chen, Fan, Gu & Zhou (2020), Arrival of Young Talent: The Send-Down Movement and Rural Education in China'
  doi: https://doi.org/10.1257/aer.20191414
  journal: AER
  year: 2020
  dataset_role: Population Census component of a county-level historical exposure and education dataset
  evidence_type: replication
  evidence_url: https://doi.org/10.3886/E119690V1
  data_note: >-
    The paper combines population-census information with local gazetteers to construct a county-level dataset on exposure to the Cultural Revolution send-down movement and rural education outcomes for 1968-1977. The replication deposit identifies the units as individual, county, and county-by-year and covers rural China; the derived exposure panel is paper-specific and should not be confused with a ready-made census panel. A separate candidate tracks the derived send-down asset and its reconstruction boundary.
- cite: 'Kuhn & Shen (2013), Gender Discrimination in Job Ads: Evidence from China'
  doi: https://doi.org/10.1093/qje/qjs046
  journal: QJE
  year: 2013
  dataset_role: 2005 1% Population Sample Survey benchmark for comparing the urban employment composition of the Zhaopin job-ad corpus
  evidence_type: paper_appendix
  evidence_url: https://broomcenter.ucsb.edu/sites/default/files/publications/pdf/kuhn3.pdf
  data_note: >-
    The paper uses 2005 Census/1% Population Sample Survey urban employment distributions as a benchmark for the separately constructed Zhaopin.com job-ad data. This is an aggregate comparison input, not a claim that the census contains the job-ad variables or that the paper's cleaned job-ad corpus is a census release.
- cite: 'Qian (2008), Missing Women and the Price of Tea in China: The Effect of Sex-Specific Earnings on Sex Imbalance'
  doi: https://doi.org/10.1162/qjec.2008.123.3.1251
  journal: QJE
  year: 2008
  dataset_role: County-birth-year population-census outcomes matched to 1997 agricultural-census crop-area inputs and Michigan China Data Center GIS
  evidence_type: final_paper_and_provider_pages
  evidence_url: https://www.kellogg.northwestern.edu/faculty/qian/resources/Missing-Women_QJE_20080407_all.pdf
  data_note: >-
    The author's final-paper PDF identifies a 1% sample of the 1997 China Agricultural Census, a 1% sample of the 1990 Population
    Census, and Michigan China Data Center GIS matched at the birth-year/county level. It covers 1,621 counties in 15 southern
    provinces; the empirical sample is rural residents born 1962–1990, further restricted to people who report living in the same
    county for more than five years. The paper uses a 0.05% 2000 Population Census sample for the education analysis. Census
    microdata, the agricultural-census 1% extract, and the exact GIS/concordance files are not thereby public or interchangeable
    with the general census record. The paper also uses RCRE/NFS 1986–1990 as an auxiliary check on migration, which is recorded
    separately in the rfd record rather than treated as the main Qian outcome panel.
provenance:
- source: https://academic.oup.com/qje/article-abstract/123/3/1251/1928174
  field_scope:
  - final QJE identity, DOI, publication date, and paper topic
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.kellogg.northwestern.edu/faculty/qian/resources/Missing-Women_QJE_20080407_all.pdf
  field_scope:
  - 1997 Agricultural Census 1% sample and 1990 Population Census 1% sample
  - 0.05% 2000 Population Census education sample
  - Michigan China Data Center GIS and birth-year/county aggregation
  - 1,621-county, 15-southern-province, rural, same-county-five-years scope
  - RCRE/NFS 1986–1990 auxiliary migration check
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.stats.gov.cn/sj/pcsj/dycnypc/
  field_scope:
  - official first agricultural census publication page and public aggregate-table route
  - distinction between public aggregates and the paper's 1% extract
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.journals.uchicago.edu/doi/abs/10.1086/660887
  field_scope:
  - final JPE article identity and DOI
  - cross-regional and household evidence context
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://users.nber.org/~confer/2009/China09/wei.pdf
  field_scope:
  - 1990/2000 Population Census sex-ratio, housing, and population-structure inputs
  - 2005 1% Population Survey supplemental series
  - Census-derived regional aggregates versus separate CHIP household outcomes
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.aeaweb.org/articles/materials/16850
  field_scope:
  - AER paper use
  - 2005 Mini-Census sampling and migration variables
  - 2000–2005 flow-construction boundary and limitations
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/152203/version/V1/view
  field_scope:
  - paper-specific census cleaning route
  - public replication versus restricted NBS census boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.aeaweb.org/articles?id=10.1257/aer.20150811
  field_scope:
  - AER paper identity and regional/urban economics scope
  - 2000-2005 study window and migration/trade model context
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view
  field_scope:
  - replication project identity and citation
  - China, 2000-2005, province-sector-year metadata
  - visible migration output files and public-versus-raw census boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view?path=%2Fpcms%2Fprojects%2F1%2F1%2F3%2F0%2F113071%2FV1.0.1%2F20150811_data&type=folder
  field_scope:
  - deposited `migration_data.dta`, `mij2000.csv`, and `mij2005.csv` file names
  - README/code/data folder boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://international.ipums.org/international-action/sample_details/country/cn (official IPUMS-I sample
    characteristics for China covering cn1982a/cn1990a/cn2000a sample design, fraction, person-record counts, weights, and smallest geography)
  field_scope:
  - CN1990A Fourth National Population Census - stratified cluster sample, fraction 0.01, 11,835,947 person records, self-weighting (expansion factor 100)
  - CN2000A Fifth National Population Census - systematic household sample, fraction 0.01, 11,804,344 person records; sample is flat-weighted according to the current PERWT documentation
  - no China sample later than 2000
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://international.ipums.org/international-action/source_variable/PERWT/ajax (official IPUMS-I person-weight documentation)
  field_scope:
  - China 1982/1990/2000 samples are flat; each record represents 100 persons in the population
  - The extract's PERWT variable and its implied decimals remain the operational weighting field
  added: '2026-08-14'
  confidence: high
  verified: true
- source: https://international.ipums.org/international-action/samples and https://international.ipums.org/international/geography_variables_list.shtml
    plus official variable pages GEO1/GEO2/GEO3_CN1990 and GEO1/GEO2/GEO3_CN2000
  field_scope:
  - availability of cn1982a, cn1990a, cn2000a in the samples index
  - GEO1 province (GIS), GEO2 prefecture/city (GIS), GEO3 county (GIS only for selected urban areas in 2000)
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://international.ipums.org/international-action/faq, https://international.ipums.org/international/index.shtml,
    and https://international.ipums.org/international-action/menu (official IPUMS-I access conditions and application form)
  field_scope:
  - free of charge for qualified researchers; data access by reviewed application (research description, institutional affiliation)
  - scholarly/educational use only, commercial use prohibited, no redistribution, no re-identification
  - registration valid one year and renewable
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://international.ipums.org/international-action/sample_details/country/cn and https://international.ipums.org/international-action/faq (re-read 2026-09-28)
  field_scope:
  - live China sample-selection page: 1982, 1990 and 2000 census samples
  - provider-recorded person/household observation structure, sample fractions and smallest stated geography
  - current application, individually reviewed access, one-year registration and extract-delivery route
  - scholarly/educational-use, no-commercial-use, no-redistribution and no-reidentification conditions
  - current China 2000 sample-page expansion-factor wording, which conflicts with the previously recorded PERWT wording
  added: '2026-09-28'
  confidence: high
  verified: true
- source: National Bureau of Statistics data.stats.gov.cn and microdata.stats.gov.cn (confirm summary table and microdata
    application channels)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903
  field_scope:
  - ReStud paper census waves and county-level roles
  - 1953-2015 historical coverage described in the data section
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://zenodo.org/records/20671189
  field_scope:
  - ReStud census access boundary
  - public replication package versus NBS confidential inputs
  added: '2026-08-11'
  confidence: high
  verified: true
related_datasets:
- china-stat-yearbook
- china-satellite-pm25
- chip
- cfps
- uhs
---

## Positioning in one sentence
China's census is a comprehensive survey covering the entire country's population once every 10 years - from personal information to migration history to housing conditions.
It is the "underlying geo-demographic information infrastructure" for research on China's population structure, migration, urbanization and labor force.
Summary tables are publicly available, and microdata (1% or short form sampling) can be obtained through application or IPUMS International.
It can support descriptive migration matrices and population-structure indicators when the selected wave, geography, and access route match the question.

## Appropriate data roles

- **Migration and spatial population structure**: use the documented residence, hukou, and prior-residence fields to build a migration or population-distribution table, but check the selected wave's definition, geographic grain, and whether the requested microdata or only aggregates are obtainable.
- **Demography, education, labor, and housing composition**: use the appropriate census cross-section for a nationwide benchmark by county, city, province, or permitted microdata geography. It is a cross-section, not an annual household panel.
- **Not a substitute for other assets**: use ASIF/Economic Census for firm and industry production questions; use household surveys for longitudinal balance-sheet or behavioral outcomes; and use a separately documented data asset whenever the desired source is a policy, treatment, or historical event.
- **IPUMS boundary**: it covers 1982, 1990, and 2000 only. Align variables and weights with the released extract and do not assume that it supplies later NBS waves.
- **IPUMS version**: covers 1982, 1990 and 2000 (Third, Fourth and Fifth censuses) only. When using it, please pay attention to the subtle differences in variable definitions and weights with the domestic official version.

## Key variables/modules
- **Demographic Basics**: age, gender, ethnicity, marital status, literacy level
- **Migration Core** (highest value): Place of household registration (province/city/county), current place of residence, length of time away from the place of household registration, reason for migration, place of permanent residence five years ago
- **Human capital**: education level (from illiterate to graduate student), study status, graduation time
- **Labor force**: employment status, occupation (major category/medium category), industry (category/major category), reason for not working
- **Housing**: Type of housing, year of construction, building area, number of rooms, kitchen/toilet/water facilities
- **Fertility**: number of live births, number of surviving children (special for women of childbearing age)

## How to get
1. **Summary table (the simplest)**: data.stats.gov.cn → Census special topic → Check summary indicators by province/city/county/township/industry/occupation and other dimensions, download Excel/CSV for free.
2. **Microdata (formal application)**: Submit an application to the Microdata Laboratory of the National Bureau of Statistics (microdata.stats.gov.cn) → review and approval (3-6 months) → sign a confidentiality agreement → obtain desensitized long form 1% or short form 10% samples.
3. **IPUMS International (International Alternative)**: international.ipums.org provides standardized about-1% micro-samples of the 1982, 1990 and 2000 censuses, free of charge but by approved application (research description and institutional affiliation; scholarly use only, no redistribution), with variable names consistent with other global censuses - suitable for international comparative research.
4. **University authorization channels**: Some universities such as Renmin University, Peking University, and Tsinghua University are authorized by NBS to use more detailed microscopic samples in on-campus laboratories.

## Connections to other data
- Use "county code/city code/province code" to connect **Statistical Yearbook** and other outcome or covariate assets after checking the reference-year and boundary vintage.
- Use "Industry/Occupation Code" to connect **Economic Census** or **Enterprise Database** to construct an industry-regional matrix of the labor market.
- Baseline weights and sampling frames can be provided for sample surveys such as **CFPS / UHS / CGSS** - the census is the parent frame for these surveys.

## Remarks / Pitfalls
- **Micro data threshold is extremely high** - This is not a public data set. The alternative paths adopted by most scholars are: ①Use summary tables to create provincial/municipal/county-level panels; ②Use the 1982/1990/2000 micro-samples of IPUMS (application required); and ③Switch to public micro-surveys such as CFPS/CHNS.
- **Changes in the definition of migration data**: The definition of migration (threshold of departure time/whether intra-city migration is included) in the Fourth Census/Fifth Census/Sixth Census is not completely consistent. Cross-census comparisons require careful checking of the definitions.
- **Industry/occupation code alignment**: Each census round uses different versions of the national standard (GB/T 4754) → manual alignment is required for comparison across rounds.
- **IPUMS Restrictions**: covers 1982/1990/2000 only, excluding later waves - to do research in the 2010s or 2020s you can only use the NBS formal application or fall back to the summary table.
