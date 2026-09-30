---
schema_version: 2
catalog_status: grounding
id: rfd
name: National Rural Fixed Point Survey (NFP/NFPS)
aka:
- 全国农村固定观察点
- 农村固定观察点
- National Fixed Point Survey
- NFP
- NFPS
- National Rural Fixed Observation Point Survey
provider: Research Center for Rural Economy, Ministry of Agriculture and Rural Affairs (RCRE, formerly Research Center for
  Rural Economy, Ministry of Agriculture)
china_related: true
domains:
- agriculture
- development
- labor
- land
- public
- migration
unit_of_observation: Farmer-year/Family member-year/Farmer-crop-year/Village-year
structure: longitudinal-panel
geo_granularity:
- personal
- farmers
- village
- province
geography: Fixed observation villages in various provinces in mainland China; the provinces, villages and sample periods of
  the version used in the paper are not exactly the same
time_span:
  start: 1986
  end: unknown
  known_gaps:
  - 1992
  - 1994
  last_confirmed_release: unknown
  last_checked: '2026-07-10'
frequency:
- annual
sample_size: The full survey covers more than 300 villages and more than 20,000 households; the specific research versions
  vary greatly. For example, Chari et al. used 2003–2010, 399 villages, and more than 19,000 households, and Adamopoulos et
  al. used 1993–2002, 110 villages in 10 provinces, and about 8,000 households each year.
key_variables:
- Family members and labor force allocation
- Farm and non-farm work days
- Migration and employment
- household income and expenses
- Land holding and leasing out
- Crop sown area and physical output
- Agricultural inputs such as fertilizers and machinery
- agricultural production costs
- Village economy and public services
research_fit:
  best_for:
  - A long-term panel study on rural land allocation, land rental and farmer household productivity
  - Intra-household allocation of rural labor migration to non-agricultural sectors and cities
  - Farmer-level causal assessment of agricultural policies, land rights and pension policies
  choose_over:
  - Priority is given to CFPS/CHFS when crop input-output, land lease and long-term farmer panel are required.
  - Research on household balance sheets or publicly downloadable data should not take precedence over CHFS/CFPS
  not_good_for:
  - Projects that have no institutional cooperation channels and require immediate public downloading
  - Research on urban households or listed companies
  - Studies that require a unified national sample and do not allow differences between different paper versions
  - Studies requiring confirmed subdivision boundaries, parcel coordinates, or parcel-by-parcel property rights information
  needs_join_for:
  - When researching specific policies, it is usually necessary to join county/provincial policy time points, prices, weather
    or traffic data
  variation_available:
  - Farmer, village and year panel changes
  - Regional phased implementation of land system and pension policies
  topics:
  - land transfer
  - rural land reform
  - Crop productivity
  - Farmer productivity
  - Agricultural input and output
  - rural pension
good_for:
- Rural Land System and Agricultural Productivity—Using Regional Time Differences in Land Rights Reform to Do DID
- Land and capital misallocation - using farmer-crop input and output to estimate TFP and marginal product dispersion
- Rural pensions, migration costs and cross-sector allocation of labor
identification:
- Farmer fixed effects
- Village fixed effects
- DID (policy implemented in phases)
- IV (Policy Eligibility or Geographic Impact)
- structural model
linkable_keys:
- Farmer ID (internal)
- Village code (restricted)
- Provincial code
- Year
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Provincial code
  - Year
  method: exact
  evidence_status: plausible
- target: china-census
  relation: benchmark
  keys:
  - Provincial code
  - Year
  method: aggregate-level
  evidence_status: plausible
access_routes:
- route: institutional-cooperation
  access_status: no-public-download
  direct_url: https://www.rcre.agri.cn/
  requirements: Rely on universities/research institutions to contact the Rural Economic Research Center of the Ministry of
    Agriculture and Rural Affairs; usually requires formal projects, cooperative relationships, and confidentiality commitments.
  steps:
  - First confirm the year, questionnaire level and variables required for the study.
  - Explain the institution, project and data needs through the contact/message channel on the official website of the Rural
    Economic Research Center.
  - Submit research plans, data usage instructions and confidential materials as required by the other party.
  deliverable: The approved version may be a desensitized farmer/village panel in a specified year and region, and is not
    a unified public disclosure of the entire database.
  cost: by-application
  last_checked: '2026-07-10'
  caveat: As of the verification date, no standard download or online application page for the public has been found; we cannot
    guarantee that the application will be successful or give a fixed period.
- route: econometrica-supplement
  access_status: publisher-listed-supporting-material
  direct_url: https://onlinelibrary.wiley.com/doi/10.3982/ECTA16598
  requirements: The publisher page lists an online appendix (147.4 KB) and a data-and-programs archive (271.1 MB). The
    archive must be inspected before use; its listing does not prove that the confidential RCRE/NFPS survey microdata are
    included or redistributable.
  steps:
  - Open the Econometrica article page and follow the Supporting Information links for the appendix and data-and-programs archive.
  - Read the archive README or manifest and record which files are supplied, which are derived outputs, and which raw RCRE inputs
    are absent before attempting a rerun.
  - If the raw household/farm panel is absent, apply through the RCRE institutional-cooperation route for the paper's 1993–2002
    sample; use the public supplement for code, documentation, and any released derived files only.
  deliverable: A publisher-hosted appendix and data/programs archive, with the exact file contents and raw-data boundary to be
    confirmed from the downloaded manifest; raw RCRE/NFPS access remains a separate institutional question.
  cost: mixed
  last_checked: '2026-08-11'
  caveat: The publisher page is public and labels the article open access, but automated access to the file links may be blocked
    or change. Do not treat possession of the supplement as possession of the RCRE survey or as permission to redistribute it.
- route: public-alternative
  access_status: available
  direct_url: https://www.isss.pku.edu.cn/cfps/
  requirements: Proxy using CFPS rural subsample.
  steps:
  - Obtain public data by application route for CFPS entries.
  deliverable: Common variables such as income, consumption, employment, and family structure; agricultural crop input and
    output are significantly weaker.
  cost: free
  last_checked: '2026-07-10'
access:
  url: https://www.rcre.agri.cn/
  cost: by-application
  license: For approved research use only, no redistribution
  format:
  - unknown
  api: false
  how_to_get: There is no public download entrance. The supporting institution should contact the Rural Economic Research
    Center of the Ministry of Agriculture and Rural Affairs, explain the year, variables and research purpose, and submit
    cooperation and confidentiality materials as required; if it is not available, use the CFPS/CHNS rural subsample instead.
caveats: Different papers hold different years, provinces, and questionnaire levels. The sample size of a certain paper cannot
  be regarded as a fixed attribute of the entire database. What has been verified is the input and output at the farmer-crop
  level, which does not mean that all versions have been confirmed to contain plot boundaries or plot coordinates. Data non-disclosure
  is the biggest obstacle.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-11'
used_by:
- cite: 'Adamopoulos, Brandt, Leight & Restuccia (2022), Misallocation, Selection, and Productivity: A Quantitative Analysis
    with Panel Data from China'
  doi: https://doi.org/10.3982/ECTA16598
  journal: Econometrica
  year: 2022
  dataset_role: Key farmer-crop panel; used to estimate household productivity, land and capital misallocation
  evidence_type: paper_data_section_and_publisher_supplement
  evidence_url: https://www.econometricsociety.org/publications/econometrica/browse/2022/05/01/misallocation-selection-and-productivity-quantitative-analysis/file/ecta200400.pdf
  data_note: >-
    The official article describes the RCRE/Ministry of Agriculture household-farm panel for 1993–2002: 110 villages (104
    observed for all 9 years), with approximately 6,000 households observed for all 9 years. The household-farm data include
    land holdings, sown area and crop output, labor, fertilizer, machinery, and non-agricultural income/work. Wiley lists a
    147.4 KB online appendix and a 271.1 MB data-and-programs archive. The public supplement is a route to code, documentation,
    and any released derived files, but does not by itself establish that raw RCRE microdata are included; exact reruns therefore
    remain conditional on legitimate institutional access to the source panel.
- cite: Chari, Liu, Wang & Wang (2021), Property Rights, Land Misallocation, and Agricultural Efficiency in China
  doi: https://doi.org/10.1093/restud/rdaa072
  journal: ReStud
  year: 2021
  dataset_role: Main farmers-crop panel; joined with the implementation time of rural land contract laws in each province
  evidence_type: working_paper_data_section
  evidence_url: https://www.nber.org/system/files/working_papers/w24099/w24099.pdf
  data_note: National Fixed Point Survey, 2003–2010, 399 villages, more than 19,000 households.
- cite: Gai, Guo, Li, Shi & Zhu (2025), Rural Pensions, Labor Reallocation, and Aggregate Income
  doi: https://doi.org/10.3982/ECTA19699
  journal: Econometrica
  year: 2025
  dataset_role: Main individual/farmer panel; joined with the county-level implementation of the new rural insurance
  evidence_type: paper_data_section
  evidence_url: https://onlinelibrary.wiley.com/doi/10.3982/ECTA19699
  data_note: >-
    The paper describes the RCRE National Fixed Point Survey as an annual longitudinal survey of roughly 20,000 households
    and 80,000 individuals in about 350 villages across all 31 mainland provinces. Its individual questionnaire (available from
    2003 onward) records schooling, sector of work, working days, out-of-town migration for work, and migrant earnings; the
    paper uses 2003–2013 waves and combines the panel with county-level timing of the New Rural Pension Scheme. The survey is
    institutionally restricted, so the article's sample description does not imply a public download or a universally identical
    release; the paper-specific sample and the underlying NFP identity must remain separate.
- cite: 'Martinez-Bravo, Padró i Miquel, Qian & Yao (2022), The Rise and Fall of Local Elections in China'
  doi: https://doi.org/10.1257/aer.20181249
  journal: AER
  year: 2022
  dataset_role: Village-level public goods, land allocation, and governance outcomes over 1986–2019
  evidence_type: replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/166506/
  data_note: Combined the MOA National Fixed Point Survey (NFS) village panel (1986 onward, ~3,600–4,300 village-year obs)
    with the authors' own Village Democracy Survey to study the introduction and subsequent erosion of village elections. NFS
    outcome variables include public goods expenditures, land allocation, and village committee composition.
- cite: 'Adamopoulos, Brandt, Chen, Restuccia & Wei (2024), Land Security and Mobility Frictions'
  doi: https://doi.org/10.1093/qje/qjae010
  journal: QJE
  year: 2024
  dataset_role: Main household/individual panel for labor supply, farm production, incomes, land rentals, and rural-to-urban mobility
  evidence_type: replication
  evidence_url: https://doi.org/10.7910/DVN/G3WBU7
  data_note: >-
    Uses the RCRE National Fixed Point Survey for 2004–2018: an unbalanced panel with more than 20,000 households per year drawn
    from about 300 villages nationwide, with individual labor-supply data available from 2003 onward. The paper also uses a
    smaller supplementary RCRE survey on perceived land-reallocation risk and public Statistical Yearbooks for aggregate shares.
    The Harvard Dataverse deposit is CC0 and contains cleaning/program files, data moments, and model inputs, but its README states
    that the raw RCRE microdata are not publicly downloadable and were accessed through collective university access; the deposit
    therefore reproduces the analysis conditional on those moments rather than providing the underlying survey itself.
- cite: 'Qian (2008), Missing Women and the Price of Tea in China: The Effect of Sex-Specific Earnings on Sex Imbalance'
  doi: https://doi.org/10.1162/qjec.2008.123.3.1251
  journal: QJE
  year: 2008
  dataset_role: Auxiliary RCRE/NFS household-village observations used to check migration prevalence in tea-producing versus non-tea regions
  evidence_type: final_paper
  evidence_url: https://www.kellogg.northwestern.edu/faculty/qian/resources/Missing-Women_QJE_20080407_all.pdf
  data_note: >-
    The final-paper data section says RCRE's National Fixed Point Survey (NFS) for 1986–1990 is used to show that the probability
    of a household member working away from the home village was low and similar across tea and non-tea regions, with almost no
    migrants under age 20. This is an auxiliary migration-robustness check, not the paper's main outcome panel: the main matched
    data are the 1990/2000 Population Census and 1997 Agricultural Census samples recorded in china-census. The paper does not
    establish a public NFS download, exact delivered village list, or a reproducible Qian-specific extract.
provenance:
- source: https://www.kellogg.northwestern.edu/faculty/qian/resources/Missing-Women_QJE_20080407_all.pdf
  field_scope:
  - Qian paper's RCRE/NFS 1986–1990 auxiliary migration check
  - distinction between auxiliary NFS evidence and main census/agricultural-census inputs
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://onlinelibrary.wiley.com/doi/10.3982/ECTA16598
  field_scope:
  - identity
  - sample
  - variables
  - paper_use
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://www.nber.org/system/files/working_papers/w24099/w24099.pdf
  field_scope:
  - identity
  - sample
  - variables
  - paper_use
  added: '2026-07-10'
  confidence: high
  verified: true
- source: https://www.rcre.agri.cn/
  field_scope:
  - provider
  - access
  added: '2026-07-10'
  confidence: med
  verified: true
- source: https://academic.oup.com/qje/article/139/3/1941/7632762 and https://doi.org/10.7910/DVN/G3WBU7
  field_scope:
  - paper_use
  - sample
  - production
  - access
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://www.econometricsociety.org/publications/econometrica/browse/2022/05/01/misallocation-selection-and-productivity-quantitative-analysis/file/ecta200400.pdf
  field_scope:
  - identity
  - sample
  - variables
  - paper_use
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://onlinelibrary.wiley.com/doi/10.3982/ECTA16598
  field_scope:
  - paper_use
  - access
  added: '2026-08-11'
  confidence: high
  verified: true
related_datasets:
- id: rhs
  relation: often-confused-with
- id: cfps
  relation: substitute
- id: chns
  relation: substitute
---

## Positioning in one sentence

The national rural fixed observation point is the annual panel of rural households and villages organized continuously by the Rural Economic Research Center of the Ministry of Agriculture and Rural Affairs. It is significantly stronger than the general household survey in terms of land, crop input and output, and labor allocation. It is a high-value data for agricultural productivity and rural land research: a publisher-hosted Econometrica supplement is a useful public starting point for one China application, but the underlying RCRE panel still has no confirmed public download entrance and access depends on institutional cooperation.

## Select reminder

- Choose RFD/NFP when you need agricultural production details and long annual farmer panels.
- When only claimable household income, consumption, or employment need to be disclosed, look to CFPS/CHNS first.
- Don’t think of it as the same data as the Office for National Statistics Rural Household Survey (RHS).
- The farmer-crop information available in the paper does not equal the spatial information of plots confirmed by the current record; when plot boundaries or coordinates are involved, a separate questionnaire/approved version must be checked.

## How to get

For the Adamopoulos et al. (2022) application, first download the appendix and data/programs archive from the Wiley article page and inspect its manifest; this gives the public documentation and any released derived files, not automatically the RCRE survey. If the raw panel is absent, confirm the required 1993–2002 waves and variables, then contact the Rural Economic Research Center through its official website and submit the research plan and confidentiality materials for institutional cooperation. There is currently no public application process that promises success, so answers to users must clarify the thresholds and provide CFPS/CHNS alternatives.
