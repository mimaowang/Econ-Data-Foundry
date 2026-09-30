---
schema_version: 3
catalog_status: grounding
id: china-historical-epidemic-records
name: Historical China county-level epidemic exposure panel 1368-1949 (Wang & Ang 2024 JCE; construction documented in NTU PhD thesis Chapter 1 + Appendix A1)
aka:
- 中国历史疫灾数据
- historical disease exposure China
- epidemic records China
- Wang-Ang epidemics dataset
provider: >-
  Researcher-constructed by Jun Wang (NTU PhD thesis 2023, Chapter 1 = the JCE
  2024 paper) under the supervision of James B. Ang. Raw disease data come from
  Gong (2019), Assembly of Historical Materials about Epidemics for 3,000 Years
  in China (中国三千年疫灾史料汇编, Jinan: Shandong Qilu Press), a published
  print compilation. The coded county-level panel itself has NO release (no data
  availability statement in the thesis; no replication deposit found).
china_related: true
domains:
- health
- historical
- development
- public-health

data_pathway:
  mode: inaccessible
  origin: researcher-constructed
  target_artifact: >-
    County-level index of historical epidemic exposure for China: for each year
    1368-1949, counties whose centroids (per CHGIS-converted historical
    boundaries) fall inside an area afflicted by an epidemic are coded 1 (normal
    epidemic) or 2 (severe epidemic); exposure is summed over years (with a 1%
    annual time discount per Appendix A1) into a disease-burden index per county.
    Companion measures: EPS (Epidemic Prevention Station) institution index -
    cumulative years of EPS serving a county, 1950-2010, from the CITAS database
    - and contemporary outcome NTL 2010 (NOAA DMSP-OLS).
  availability: unavailable
  ordinary_researcher_feasible: false
  summary: >-
    Grounding-b16 (2026-08-15): NTU PhD thesis of Jun Wang (dr.ntu.edu.sg,
    handle 10356/169647) downloaded and read in full; Chapter 1 IS the JCE 2024
    paper (Wang & Ang, JCE 52:93-112, DOI 10.1016/j.jce.2023.12.001) INCLUDING
    Appendix A1 "Construction of disease and institutions data". Construction
    verified from the thesis text: raw data = Gong (2019) compilation (records
    674 BC - 1949 AD; sample restricted 1368-1949, Ming onward, as data are more
    detailed and reliable); hand-coding normal=1 / severe=2; CHGIS to convert
    past administrative units into contemporary counties; ArcGIS assigns values
    to all counties whose centroids lie within the boundary of a place
    historically hit by an epidemic; county level for over 2,000 counties
    (descriptive statistics show 2,791 county observations for NTL/EPS). EPS
    index: founding years for over 10,000 institutions from the CITAS database
    (China in Time and Space, University of Washington); counties with missing
    institution info assigned the value of the nearest county. Outcome variable:
    NOAA DMSP-OLS Nighttime Lights Time Series 2010. No data release in the
    thesis or the paper; no replication package found.
  barrier: >-
    The coded county-year exposure panel and EPS index are not released anywhere
    (no DAS in thesis or paper; no replication deposit found 2026-08-15).
    Rebuilding requires: access to the Gong (2019) print compilation (published
    book, Qilu Press), manual coding of severity per record, CHGIS boundary
    conversion, ArcGIS centroid matching, and CITAS access for the institution
    layer - i.e., the paper's exact panel is not obtainable without substantial
    reconstruction whose fidelity cannot be validated against the original.

unit_of_observation: county (contemporary county boundaries per CHGIS), per year 1368-1949 (exposure); county cross-section for EPS index (1950-2010) and NTL 2010 outcome
structure: panel of county-year exposure values (constructed); county-level cross-section for institution and outcome measures
geo_granularity:
- county (over 2,000 counties; descriptive statistics show 2,791 county observations for NTL/EPS)
geography: China, all counties with historical records; coastal and Lower Yangtze regions had the highest historical exposure per the paper
time_span:
  start: '1368'
  end: '1949'
  last_confirmed_release: 'No release; construction documented in NTU thesis (2023) Chapter 1 + Appendix A1'
  coverage_note: >-
    Exposure index covers 1368-1949 (sample restricted from the full 674 BC -
    1949 AD record span of Gong 2019); EPS index covers 1950-2010 (CITAS);
    outcome NTL from NOAA DMSP-OLS for 2010. Thesis is 2023; JCE paper
    published 2024.
  last_checked: '2026-08-15'
frequency:
- annual (exposure index); EPS and NTL are single cross-sections
sample_size: >-
  Over 2,000 counties with epidemic-exposure values; 2,791 county observations
  in the main descriptive statistics (NTL and EPS number-years).
key_variables:
- Disease exposure index (county-year; normal epidemic = 1, severe = 2, summed 1368-1949, 1% annual time discount)
- EPS number-years (cumulative years of all Epidemic Prevention Stations serving a county, 1950-2010, from CITAS)
- NTL 2010 (average visible and stable nighttime light of a county, NOAA DMSP-OLS)
- Baseline controls (geography, transportation, historical development; e.g., distance to coast, elevation, Cao population series, education circa 1920)

research_fit:
  best_for:
  - Long-run development questions where historical epidemic exposure is the treatment or exposure of interest (county-level, 1368-1949)
  - Institutional channel analysis: early Epidemic Prevention Station establishment (1950-2010 EPS index) as a mechanism linking historical disease risk to contemporary development
  - Cross-county comparisons of historical disease burden within China (not province-level aggregates, not single-disease studies)
  choose_over:
  - Choose this over province-level historical disease statistics (e.g., Cheng et al. 2009, Liu & Yang 2012) when county-level resolution is needed - the paper explicitly improves on province-level aggregation
  - Choose this over single-disease or single-incident datasets (malaria, typhoid, yellow fever studies) when a comprehensive multi-disease exposure measure is needed
  not_good_for:
  - Town/village-level disease analysis (county is the finest feasible resolution per the paper)
  - Post-1949 epidemic analysis (sample ends 1949; EPS institutions continue to 2010 but exposure does not)
  - Disease-type-specific heterogeneity (pathogen is unknown/unrecorded for most incidents)
  - Obtaining the paper's exact panel: it is unreleased; any rebuild is approximate
  needs_join_for:
  - Contemporary outcomes (e.g., NTL 2010 from china-nighttime-lights family; population, GDP, education controls)
  - Modern public-health outcomes (mortality, life expectancy) if replicating the paper's mechanism analysis
  variation_available:
  - Cross-county variation in historical epidemic exposure (within-province comparisons with provincial fixed effects)
  - Timing variation in first EPS establishment across counties (1950-1986 adoption sequence)
  topics:
  - historical epidemics
  - disease control
  - long-run development
  - public health institutions
  - epidemic prevention stations

good_for:
- long-run development and health
- historical disease exposure
- institution persistence
identification:
- cross-sectional regression with provincial fixed effects
- institution-timing analysis (EPS adoption)
linkable_keys:
- County (contemporary boundaries; CHGIS-based concordance)
- Year (1368-1949 exposure)

joins:
- target: china-nighttime-lights
  relation: complement
  keys:
  - county
  method: Outcome variable NTL 2010 (NOAA DMSP-OLS) as used in the paper's main specification
  evidence_status: literature-used
- target: china-historical-clan-kinship-1470-1910
  relation: complement
  keys:
  - county
  - historical period
  method: Adjacent historical-asset family (clan networks 1470-1910); different construction and sources; useful for joint long-run-development designs
  evidence_status: plausible

access_routes:
- route: ntu-thesis-full-text
  access_status: available
  direct_url: https://dr.ntu.edu.sg/handle/10356/169647
  requirements: None (publicly downloadable NTU thesis PDF; fetched 2026-08-15)
  steps:
  - Download the thesis PDF from dr.ntu.edu.sg (handle 10356/169647).
  - Read Chapter 1 (= the JCE 2024 paper) and Appendix A1 "Construction of disease and institutions data" for the full construction recipe.
  deliverable: Full construction recipe (sources, coding, GIS matching, variables); NOT the data itself.
  cost: free
  last_checked: '2026-08-15'
  caveat: Thesis is the paper text + appendix; it documents construction but contains no data file.
- route: jce-published
  access_status: blocked
  direct_url: https://doi.org/10.1016/j.jce.2023.12.001
  requirements: Subscription or institutional access (Elsevier 403 for automated clients)
  steps:
  - Read the published JCE article (vol 52, pp. 93-112) for the paper version and any data-availability statement.
  deliverable: Published article text; no data release expected per the thesis.
  cost: mixed
  last_checked: '2026-08-15'
  caveat: Published-version data availability statement unread (Elsevier 403 in this environment); thesis contains no DAS.
- route: raw-source-gong-2019
  access_status: needs-verification
  direct_url: needs-verification
  requirements: 'Published book - Gong (2019), Assembly of Historical Materials about Epidemics for 3,000 Years in China (中国三千年疫灾史料汇编), Jinan: Shandong Qilu Press; print/library acquisition'
  steps:
  - Obtain the print compilation (library or purchase).
  - Replicate the paper's coding: extract timing, location, severity per record; restrict to 1368-1949.
  deliverable: Raw historical epidemic records (the paper's input); NOT the coded county panel.
  cost: paid
  last_checked: '2026-08-15'
  caveat: Rebuilding the exact county-year panel from this book is a large manual task (hand-coding + CHGIS/ArcGIS matching) with no released code to validate against.

access:
  url: https://dr.ntu.edu.sg/handle/10356/169647
  cost: by-application
  license: Thesis is publicly downloadable; the coded dataset is unreleased; Gong (2019) is a published book
  format: []
  api: false
  how_to_get: >-
    The coded panel is unavailable. The obtainable evidence is the NTU thesis
    full text (construction recipe) and the Gong (2019) print compilation (raw
    input). Rebuilding the paper's exact panel is possible in principle but
    large and unvalidated; treat the asset as inaccessible.
caveats: >-
  The 1% annual time discount and the exact coding rules are documented in
  Appendix A1 (thesis). The Gong (2019) compilation covers 674 BC - 1949 AD;
  only 1368-1949 enters the paper's sample. Severity coding (normal=1/severe=2)
  is hand-coded from archival wording and is the only systematic variation the
  authors use; disease type is mostly unknown. EPS missing-county imputation
  uses the nearest county.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Wang, Jun & James B. Ang (2024), Epidemics, disease control, and China''s long-term development'
  doi: https://doi.org/10.1016/j.jce.2023.12.001
  journal: Journal of Comparative Economics
  year: 2024
  dataset_role: Main treatment (county historical epidemic exposure 1368-1949) and institution channel (EPS index 1950-2010); outcome NTL 2010
  evidence_type: thesis-chapter-full-text
  evidence_url: https://dr.ntu.edu.sg/handle/10356/169647
  data_note: >-
    Read in full 2026-08-15 from the NTU PhD thesis (Jun Wang, 2023, "Essays on
    Culture, Institutions and Comparative Development", NTU School of Social
    Sciences; supervisor Assoc Prof James Ang). Chapter 1 = the JCE paper with
    Appendix A1. Verified: Gong (2019) raw source; 1368-1949 restriction;
    normal=1/severe=2 hand coding; CHGIS + ArcGIS centroid matching; over 2,000
    counties; 1% annual time discount index; EPS index from CITAS (founding
    years for over 10,000 institutions, 1950-2010); NOAA DMSP-OLS NTL 2010
    outcome; no data release.

provenance:
- source: https://dr.ntu.edu.sg/handle/10356/169647
  field_scope:
  - data_identity
  - construction
  - variables
  - sample
  - paper_use
  added: '2026-08-15'
  confidence: high
  verified: true
- source: 'https://doi.org/10.1016/j.jce.2023.12.001 (Crossref: JCE 52:93-112, Wang & Ang 2024)'
  field_scope:
  - published_metadata
  - paper_identity
  added: '2026-08-15'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-historical-epidemic-records, Layer-2b sweep 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-historical-clan-kinship-1470-1910
  relation: complement
- id: china-nighttime-lights
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

The Wang & Ang (2024 JCE) asset is an unreleased county-level panel of historical epidemic exposure for China (1368-1949, hand-coded from the Gong 2019 three-thousand-year compilation, matched to contemporary counties via CHGIS/ArcGIS, with an EPS institution index from CITAS) - the construction recipe is fully documented in the publicly downloadable NTU PhD thesis (Chapter 1 = the paper + Appendix A1), but the coded panel itself has no release and is not realistically reproducible.

## Select rules

- Use for county-level long-run development questions where historical epidemic burden is the exposure, and for the EPS-institution channel (1950-2010) linking historical disease risk to contemporary outcomes.
- Switch to province-level historical disease statistics or single-disease datasets when county resolution is unnecessary or a specific pathogen is the question.
- Do not treat this as obtainable microdata: no release exists; treat the thesis as the construction recipe and Gong (2019) as the raw input.

## Get recipe

1. Download the NTU thesis (dr.ntu.edu.sg handle 10356/169647) and read Chapter 1 + Appendix A1 - the complete construction recipe (raw source, coding, GIS matching, discount rate, imputation).
2. For the raw input, obtain Gong (2019), Assembly of Historical Materials about Epidemics for 3,000 Years in China (Qilu Press, Jinan) by library or purchase.
3. Rebuilding the exact panel requires hand-coding severity from archival wording, CHGIS boundary conversion, ArcGIS centroid assignment, and CITAS access - large manual work with no released code or data to validate against. Treat the exact panel as unobtainable; use the recipe to build an approximation only if the design tolerates it.

## Connections and Limitations

- The sample restriction (1368-1949) is the paper's own choice: Gong (2019) spans 674 BC - 1949 AD, but earlier records are less detailed/reliable.
- Unit is the contemporary county (CHGIS-converted boundaries); centroid-based assignment means boundary vintage matters for any rebuild.
- Severity coding (1/2) is the only systematic variation; disease type is unknown for most incidents, so pathogen-specific questions cannot be answered.
- EPS missing-county imputation (nearest county) and the 1% annual discount are construction choices documented in Appendix A1.
- No data availability statement exists in the thesis; the published JCE version's DAS is unread (Elsevier 403 here) but no deposit was found.
