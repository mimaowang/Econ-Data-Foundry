---
schema_version: 2
catalog_status: ready
id: cmds
name: China Migrants Dynamic Survey (CMDS)
aka:
- CMDS
- 流动人口动态监测
- 中国流动人口调查
- China Migrants Dynamic Survey
- 流动人口监测
- 卫健委流动人口调查
provider: National Health Commission (NHC, formerly National Health and Family Planning Commission) Migrant Population Service
  Center
china_related: true
domains:
- labor
- migration
- health
- development
- sociology
- public
unit_of_observation: Individual-year (migrant population over 15 years old who has lived in the place of arrival for more
  than one month; repeated cross-sectional design)
structure: repeated-cross-section
geo_granularity:
- personal
- community/street
- County
- city
- province
geography: 31 provinces/municipalities/autonomous regions in mainland China (covering major inflow and outflow places)
time_span:
  start: 2009
  end: 2018
  last_confirmed_release: 2018
  coverage_note: Standalone CMDS discontinued/consolidated after 2018, subsequent surveys cannot automatically be considered
    the same product
  last_checked: '2026-07-10'
frequency:
- annual
- repeated-cross-section
sample_size: Approximately 150,000–200,000 individual records per year (nationally representative)
key_variables:
- Demographics (age/gender/marriage/ethnicity/hukou type)
- Flow characteristics (place of inflow/place of outflow/duration of flow/reason for flow/whether across provinces)
- Employment (employment status/occupation/industry/monthly income/working hours/contract type)
- Residence (housing type/number of people living together/monthly rent)
- Health (self-rated health/chronic diseases/recent illnesses/health records)
- Medical insurance (type of insurance/place of insurance/reimbursement in other places)
- Children’s education (migrant children attending school/left-behind children)
- Social integration (number of local friends/language adaptation/willingness to stay/identity)
- Family planning/marriage and childbearing (number of children/contraception/maternity health care)
research_fit:
  best_for:
  - Large-sample annual repeated cross-sections of employment, residence, medical insurance, children's education and social
    integration of floating population from 2009 to 2018
  choose_over:
  - Priority is given to small sample migrants in CFPS/CGSS when studying special issues on migrant population.
  - It cannot replace the real panel when you need to track the migration trajectory of the same person.
  not_good_for:
  - local non-migrant population
  - Independent CMDS after 2019
  - Personal long-term tracking
  - Accurate flow out of counties and villages
  needs_join_for:
  - Urban housing prices, broadband, pollution and public services need to be joined according to the city and year of inflow.
  variation_available:
  - annual repeated sections
  - urban policy differences
  - The difference between the place of inflow and the place of outflow
good_for:
- Migrant labor market - migration decision, employment quality, wage gap (migrant vs local/inter-provincial vs intra-provincial)
- Household registration system and public service accessibility - barriers to medical insurance reimbursement/children’s
  schooling/housing for migrant populations
- Migration and health - the impact of migration on physical and mental health, healthy migrant effect
- Social integration and identity—migrant population’s intention to stay, local friend network, language adaptation
- Left-behind children and migrant children - the causal effect of parents’ migration on children’s education/health (with
  data from the place of emigration)
- Evaluation of new urbanization policies - DID of policies such as residence permit/points-based residence/equalization of
  public services
identification:
- DID (Policy/City Difference)
- IV (place of departure/distance/policy impact)
- Repeated Section Composite Panel
- discrete choice model
linkable_keys:
- Provincial code
- City code
- Community code (authorization required)
access_routes:
- route: cmds-platform
  access_status: available-with-application
  direct_url: https://www.chinaldrk.org.cn/
  requirements: Platform registration, research purpose and data agreement; platform accessibility and open rounds need to
    be confirmed one by one.
  steps:
  - Register for the floating population data platform.
  - Find the year you want and submit your application.
  - Download the data and questionnaire after approval.
  deliverable: Repeated cross-section data for year of approval; sensitive geographic variables may be restricted.
  cost: free
  last_checked: '2026-07-10'
access:
  url: https://www.chinaldrk.org.cn (China Mobile Population Data Platform); The original application channel should contact
    the National Health Commission Mobile Population Service Center
  cost: free
  license: Academic research only, registration + signing of agreement required
  format:
  - dta
  - csv
  - sav
  api: false
  how_to_get: 1) Visit https://www.chinaldrk.org.cn → Register → Submit application → Download the annual data after passing
    the review; 2) Contact the Migrant Population Service Center of the National Health Commission to apply formally (institutional
    cooperation channel); 3) Some universities (Renmin University/Peking University/Fudan, etc.) have been authorized for
    on-campus use.
caveats: CMDS is a repeated cross-section (different samples every year) and a non-tracking panel - it cannot track the migration
  trajectory of the same person and can only perform composite panel analysis of repeated cross-sections. After 2018, CMDS
  was integrated into the new survey system, and independent brands no longer exist. Outflow location information is only
  available at the provincial level - the outflow county/village cannot be accurately identified. Access to some sensitive
  variables (such as precise income, HIV/AIDS) may be restricted.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: Liao, Du & Zhang (2026), How Do Housing Rents Affect Migrants' Health? Evidence from the China Migrants Dynamic Survey
  journal: CER
  year: 2026
  dataset_role: Main migrant population health and housing rental outcomes
  data_note: Using CMDS migrant population data to study the impact of housing rent on the health of the migrant population
    - High rent cities significantly reduce the self-rated health and mental health of the migrant population
- cite: 'Cao, Ni & Guo (2025), Broadband Internet and Income Inequality among the Floating Population: Evidence from the ''Broadband
    China'' Strategy in China'
  journal: CER
  year: 2025
  dataset_role: Income results of migrant population; connected with broadband China urban policy
  data_note: Using CMDS 2011-2018 panel data + DID for 35 major cities, it was found that broadband Internet has significantly
    expanded the income gap within the floating population - the gap between high-skilled vs low-skilled and urban vs rural
    registered migrants has widened, which is a skill-biased technological progress effect.
provenance:
- source: Crossref abstract for Liao et al., https://doi.org/10.1016/j.chieco.2026.102691 (supports use of the China Migrants Dynamic Survey)
  added: '2026-07-08'
  confidence: high
  verified: true
- source: China Migrant Population Data Platform https://www.chinaldrk.org.cn (supports survey design, waves, and access conditions)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- cfps
- cgss
- china-census
- uhs
---

## Positioning in one sentence
CMDS (Dynamic Monitoring of Migrant Population) is an annual survey conducted by the former National Health and Family Planning Commission on about 200,000 migrant population (15+ years old, who has left their place of residence for more than one month) since 2009.
A nationally representative sample survey - covering places of inflow/outflow, employment, income, residence, health, medical insurance,
Children’s education and **social integration** full-dimensional information,
It is the most specialized data for studying China’s floating population (245 million migrant workers and their families).
Because of its special focus on the floating population, annual frequency, and large sample size, it has irreplaceable advantages in quantitative research on the floating population.

## Research questions suitable for answering/Typical identification strategies
- **"Who is moving, why they are moving, and where they are going"**: CMDS has detailed inflow/outflow information (province-city-street three levels), which can accurately depict the spatial pattern of migration in China and its determinants (push-pull factor analysis).
- **Labor market consequences of household registration barriers**: The gap in wages, occupation, contract security and social security participation between mobile vs. local household registration - the employment module of CMDS is more detailed than the general household survey.
- **Social Integration**: CMDS is the best data source for social integration research - variables such as intention to stay, number of local friends, language adaptation, and identity ("Do you consider yourself a local?") are rarely found in other surveys.
- **Not suitable for**: non-migrant population (local residents - please use CFPS/CGSS), after 2019 (CMDS has been integrated into the new survey system), and those who need to track individual migration trajectories on a panel (CMDS is an annual repeated cross-section).

## Key variables/modules
- **Mobility Core**: Place of household registration (province/city), current place of residence (province/city/street), duration of this movement, reason for movement (work/business/migration/marriage)
- **Employment module**: Employment status (employee/employer/self-employed/household worker), occupation, industry, monthly income, weekly working hours, labor contract
- **Residential Module**: housing type, monthly rent, shared living situation
- **Health and Medical Insurance**: Self-assessed health, chronic diseases, whether you have been sick in the past year, and the location and type of medical insurance coverage
- **Social integration module** (unique value): number of local friends, whether you can speak local dialects, willingness to stay (long-term/short-term), whether you identify as a "local"
- **Children’s Education**: Whether school-age children will move with them, and the type of school they attend in the place of migration (public/private/school for children of migrant workers)

## How to get
1. Visit https://www.chinaldrk.org.cn → Register → Submit data application → Download annual data in Stata/SPSS/CSV format after approval.
2. Contact the Migrant Population Service Center of the National Health Commission to obtain it through formal institutional cooperation (applicable to studies that require more detailed subsamples or supplementary variables).
3. Some universities have been authorized to use it directly on campus.

## Connections to other data
- **Census/1% Sampling**: CMDS is a special sampling of the floating population - the macro distribution of migration in the census can be used for weight calibration.
- **CFPS/CGSS**: CFPS/CGSS includes a subsample of migrants but has a small sample size – CMDS complements the large sample coverage of migrants.
- **Statistical Yearbook**: Use "inflow city code" to connect macro indicators such as city housing prices/GDP/industrial structure/public services.

## Remarks / Pitfalls
- **Non-tracking panel**: The CMDS is an annual repeated cross-section – it cannot track the migration and employment trajectories of the same individuals. Doing dynamic research on "flow → integration" requires the composite panel method.
- **Terminated in 2018**: The CMDS independent brand will be discontinued after 2018 (integrated into the seventh census and subsequent national population change survey system) - new channels are needed for micro data on floating population after 2019.
- **The accuracy of the outflow place information is limited**: only to the province or prefecture-level city level - cannot accurately identify the outflow place at the district, county/village level.
- **Representative**: CMDS uses the inflow area as the sampling frame - it mainly covers the floating population in big cities. Attention should be paid to the representativeness at the level of rural outflow areas.
