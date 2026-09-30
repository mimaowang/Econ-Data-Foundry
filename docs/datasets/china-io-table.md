---
schema_version: 2
catalog_status: ready
id: china-io-table
name: China Input-Output Tables
aka:
- 投入产出表
- 中国投入产出表
- Input-Output Tables
- China I-O Table
- 中国IO表
- 全国投入产出表
- 省际投入产出表
- 区域间投入产出表
- 多区域投入产出表
- MRIO
provider: National Bureau of Statistics (NBS); Chinese Academy of Sciences/National Information Center and other institutions
  prepare inter-provincial/multi-regional extended version
china_related: true
domains:
- IO
- trade
- macro
- firm
- environment
- development
unit_of_observation: industry-industry (product division × product division) or province-industry-province-industry (interprovincial/multi-regional
  version)
structure: matrix-and-multi-regional-matrix
geo_granularity:
- Nationwide
- province
- Region (8 major regions)
geography: Mainland China (national table); inter-provincial table covers about 30 provinces/municipalities/autonomous regions
time_span:
  start: 1987
  end: ongoing
  last_confirmed_release: 2022
  coverage_note: The national benchmark table has confirmed 1987/1992/1997/2002/2007/2012/2017/2022; the inter-provincial
    table has fewer years
  last_checked: '2026-07-10'
frequency:
- quinquennial
sample_size: The national table is usually 42/122/135/149 product sectors; the inter-provincial table is usually 30 provinces
  × 30 industries × 30 provinces × 30 industries
key_variables:
- Total output (industry×industry)
- Intermediate input (industry×industry)
- End use (consumption/investment/export/import)
- Value added (labor compensation/net production tax/depreciation of fixed assets/operating surplus)
- Direct consumption coefficient
- complete consumption factor
- Influence coefficient
- Sensitivity coefficient
- Dependence of various industries on imported intermediate goods
- Domestic Value Added Rate (DVAR)
- Interprovincial trade flows (interprovincial table)
- Inter-industry correlation strength (upstream degree/downstream degree)
research_fit:
  best_for:
  - Industry upstream and downstream input relationships, inter-provincial trade flows and structural model calibration
  choose_over:
  - Prioritize input-output tables over statistical yearbooks when inter-industry intermediate-input matrices and shock transmission are needed
  - Cannot replace invoice/enterprise transaction data when enterprise transaction network is required
  not_good_for:
  - High Frequency Panel of the Year
  - Single enterprise transaction relationship
  - Simple macro control without structural relationships
  needs_join_for:
  - Enterprise or customs data needs to be mapped by industry/HS; pollution research needs to combine industry emission coefficients
  variation_available:
  - Structural changes between base years
  - Industry network location
  - interprovincial trade flows
good_for:
- Global Value Chain (GVC) Analysis - Calculate the domestic value added rate (DVAR), upstream degree, and GVC participation
  of various industries in China
- Industry transmission of trade shocks - how tariff/exchange rate changes indirectly affect upstream and downstream industries
  through input-output correlations
- China's interprovincial trade costs and domestic market integration - using interprovincial input-output tables to estimate
  interprovincial trade barriers (Tombe & Zhu 2019 AER uses it to construct internal trade flows)
- Inter-industry transfer of carbon emissions/pollution – tracking emission responsibilities on the consumer side vs. the
  production side
- Industrial policy assessment - identify key upstream/strategic industries and measure the multiplier effect of industrial
  subsidies
identification:
- Quantitative model calibration (general equilibrium/CGE)
- Structure estimation
- counterfactual simulation
- network analysis
- DID (industry-year)
linkable_keys:
- Industry code (GB/T 4754
- various versions)
- Provincial code
- HS code (connected through BEC/industry comparison table)
access_routes:
- route: nbs-national-io
  access_status: available
  direct_url: https://data.stats.gov.cn/
  requirements: None
  steps:
  - Enter the National Bureau of Statistics data platform.
  - Position input-output topics/tables.
  - Select the base year and department table to download.
  deliverable: National benchmark input-output table; number of departments changes by year.
  cost: free
  last_checked: '2026-07-10'
- route: interregional-research-version
  access_status: needs-verification
  direct_url: http://www.sres.org.cn/
  requirements: Download according to the instructions of the preparation organization or contact the research team; first
    confirm the year, region and method version.
  steps:
  - Determine which interprovincial/MRIO version is required.
  - Obtain and save method documents from the preparation institution or research group.
  deliverable: For inter-provincial or multi-regional input-output tables, different institutions have different estimation
    methods.
  cost: mixed
  last_checked: '2026-07-10'
- route: AEA/openICPSR Tombe-Zhu V1 replication package
  access_status: available-with-conditions
  direct_url: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view
  requirements:
  - An openICPSR/ICPSR account and the repository's current download terms; file downloads currently redirect to login.
  - Read the deposited LICENSE.txt and ReadMe.pdf before reusing or redistributing any file.
  steps:
  - Follow the AEA article's Replication Package link to project 113071, version V1.
  - Inspect the `20150811_data` folder for `trade_ag.csv`, `trade_na.csv`, `trade_data.dta`, and the MATLAB/Stata scripts that consume them.
  - Treat those files as the paper's deposited internal-trade/model inputs; if a new project needs the underlying official regional input-output tables, obtain and document that source separately.
  deliverable: A paper-specific deposit of internal-trade files, model inputs, and code; it is not a general public release of the original NBS or other institution's interprovincial input-output tables.
  cost: registration
  last_checked: '2026-08-11'
  caveat: The project page lists a LICENSE.txt and says ICPSR distributes materials as received without reviewing or processing them. The visible file tree does not itself establish the source-table edition, all raw inputs, or redistribution rights.
access:
  url: https://data.stats.gov.cn (Summary of national benchmark tables); Key Laboratory of Regional Sustainable Development
    Analysis and Modeling, Chinese Academy of Sciences http://www.sres.org.cn provides interprovincial tables; Multiple international
    research institutions provide Chinese MRIO (such as WIOD, EXIOBASE, GTAP)
  cost: mixed
  license: National tables are public data from the government; provincial tables must indicate the source; each international
    MRIO database has its own terms of use.
  format:
  - xlsx
  - csv
  - pdf
  api: false
  how_to_get: '1) National benchmark table: data.stats.gov.cn → Input-output → Select a year to download (Excel format); 2)
    Inter-provincial/inter-regional table: Key Laboratory of Regional Sustainable Development Analysis and Simulation, Chinese
    Academy of Sciences website or contact the relevant research group to obtain; 3) International MRIO: WIOD (wiod.org),
    EXIOBASE (exiobase.eu), GTAP (gtap.agecon.purdue.edu, registration is free) all contain Chinese data.'
caveats: The benchmark table is only compiled in every 2 and 7 years, not annual data - only extended tables or linear interpolation
  can be used to approximate the two benchmark tables. The industry classification standards have been significantly revised
  in 1992/2002/2012/2017 (GB/T 4754 version changes), and alignment and comparison are required when using across versions.
  Methods of compiling inter-provincial tables vary between institutions (NBS vs CAS vs WIOD) – each requires understanding
  of their assumptions before comparing across sources.
quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-11'
used_by:
- cite: 'Tombe & Zhu (2019), Trade, Migration, and Productivity: A Quantitative Analysis of China'
  doi: https://doi.org/10.1257/aer.20150811
  journal: AER
  year: 2019
  dataset_role: Interprovincial internal-trade inputs used to calibrate the spatial general-equilibrium model
  evidence_type: article_and_replication
  evidence_url: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view
  data_note: >-
    The paper studies internal trade and migration frictions across Chinese regions. The linked V1 deposit describes China,
    2000-2005, and province-sector-year observations and lists `trade_ag.csv`, `trade_na.csv`, and `trade_data.dta`, alongside
    `tauhat.csv` and model scripts. These are the paper-specific deposited trade/model files. The deposit does not by itself prove
    that the original regional input-output tables, their source edition, or every raw input can be downloaded or redistributed;
    keep that production boundary separate from the public derived files.
- cite: Jiang, Zhao, Ouyang & Shen (2023), Integration in the Global Value Chain, Structural Change, and the Widening Gender
    Employment Gap in China
  journal: CER
  year: 2023
  dataset_role: Calculation of industry GVC participation and structural changes
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v81y2023ics1043951x23001189.html
  data_note: Using China's input-output table to measure GVC participation in various industries, it was found that GVC integration
    has exacerbated China's gender employment gap - through the channel of industrial structure change
provenance:
- source: https://www.aeaweb.org/articles?id=10.1257/aer.20150811
  field_scope:
  - AER paper identity and regional/urban economics scope
  - internal trade and migration model context for 2000-2005
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view
  field_scope:
  - replication project identity and citation
  - China, 2000-2005, province-sector-year metadata
  - public deposit versus raw input boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://www.openicpsr.org/openicpsr/project/113071/version/V1/view?path=%2Fpcms%2Fprojects%2F1%2F1%2F3%2F0%2F113071%2FV1.0.1%2F20150811_data&type=folder
  field_scope:
  - deposited `trade_ag.csv`, `trade_na.csv`, `trade_data.dta`, and `tauhat.csv` file names
  - model code and public file-tree boundary
  added: '2026-08-11'
  confidence: high
  verified: true
- source: National Bureau of Statistics data.stats.gov.cn input-output special page (confirm that the national benchmark table
    is public and can be downloaded)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- china-census
- china-customs
- china-stat-yearbook
- china-firm-pollution
---

## Positioning in one sentence
China's input-output table is an inter-industry transaction matrix compiled by the National Bureau of Statistics every five years, recording "who bought how much from whom"——
Intermediate inputs and final uses from 42 to 149 industries × industries, extending to inter-provincial trade in 30 provinces × 30 industries.
It is the basic "structural data" for global value chain, trade impact transmission, carbon footprint and industrial policy assessment.
Together with customs (imported intermediate goods) and ASIF (enterprise production), it forms a complete input-output picture from industry to enterprise.

## Research questions suitable for answering/Typical identification strategies
- **Global Value Chain and Domestic Value Added**: Use the industry-level direct and complete consumption coefficients and the proportion of imported intermediate goods to calculate the DVAR and GVC participation of each industry. This is the industry background for interpreting corporate-level DVAR changes such as Kee & Tang (2016 AER).
- **Interprovincial trade costs and domestic market integration**: Use the interprovincial trade flows in the interprovincial input-output table to estimate interprovincial trade barriers (Tombe & Zhu 2019 AER combines the IO table with migration data to simultaneously estimate the impact of trade and migration costs on overall productivity).
- **Upstream and downstream transmission of trade shocks**: The direct impact of tariffs on an industry → is transmitted to downstream industries through the complete consumption coefficient of the IO table → ultimately affecting prices and employment. This is a natural application of Caliendo & Parro's (2015 ReStud) approach in China.
- **Not suitable for**: research that requires annual frequency (IO table is once every 5 years), transaction network between individual enterprises (please use VAT invoice data), internal details of the service industry (IO table service industry sector has a coarser granularity).

## Key variables/modules
- **Intermediate usage matrix**: product department × product department, describing the value of each industry consuming other industry products
- **End use**: Residential consumption (rural/urban/government), fixed capital formation, inventory changes, exports, imports
- **Value added**: four components - labor compensation, net production tax, depreciation of fixed assets, operating surplus
- **Derivative coefficient**: direct consumption coefficient, complete consumption coefficient (Leontief inverse matrix), influence coefficient, sensitivity coefficient
- **Inter-provincial table extra**: transfer in/out matrix (province A industry i → province B industry j)

## How to get
1. **National Benchmark Table**: data.stats.gov.cn → Input-output topic → Directly download the national benchmark table for 2002/2007/2012/2017/2022 (including 42/135/149 departments) in free Excel format.
2. **Interprovincial/Interregional Table**: Contact the Key Laboratory of Regional Sustainable Development Analysis and Simulation of the Chinese Academy of Sciences or related research groups to obtain it (usually free for academic research).
3. **International standardized version**: WIOD (wiod.org), EXIOBASE (exiobase.eu), GTAP (gtap.agecon.purdue.edu, free registration and downloadable) - each has its own industry/regional classification system, including complete MRIO of China and other countries.

## Connections to other data
- **Customs Database**: Use "HS Code → Industry Code (BEC)" to compare the company's imported intermediate products to the industry classification of the IO table to calculate the DVAR at the company level.
- **ASIF Industrial Enterprise Database**: Use "industry code" to classify enterprises into the industry sectors of the IO table, and use the enterprise output/intermediate input share to weight and summarize them into industries.
- **Pollution Emission Database**: Use "industry code" to connect the emission data with the IO table to track the consumer's emission responsibility (scope 3).
- **Census**: Can be combined with the IO table to construct a spatial general equilibrium framework of "trade-migration-production" (unified analysis of Tombe & Zhu 2019 AER).

## Remarks / Pitfalls
- **Five-year compilation ≠ annual data**: There is no official benchmark table between 2012 and 2017 (only an extended table, with coarser industry granularity). When making the annual panel, either interpolation is used or only a static comparison of 5-year intervals is done.
- **Industry Classification Version**: GB/T 4754-1994/2002/2011/2017 - Four revisions mean that the industry boundaries of each new IO table have changed, and inter-period comparisons must be aligned using a standard comparison table.
- **Differences in inter-provincial table methods**: The inter-provincial table of the Chinese Academy of Sciences is based on gravity model estimation (including estimation components). It is essentially different in the data generation process from the "census-style" inter-provincial table (based on VAT invoice summary) that may be released by NBS in the future. Cross-source comparisons should be made with caution.
- **Imported intermediates treatment**: The "Imports" column of the national table is the total amount, without distinguishing which industry imports what - a complete matrix of imported intermediates usually requires additional assumptions (proportionality assumptions or calibration using customs data).
