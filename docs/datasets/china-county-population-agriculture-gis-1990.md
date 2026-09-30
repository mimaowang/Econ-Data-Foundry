---
schema_version: 3
catalog_status: grounding
id: china-county-population-agriculture-gis-1990
name: China County-Level Data on Population (Census) and Agriculture, Keyed to 1:1M GIS Map (1990)
aka:
- China Dimensions county population and agriculture data
- CITAS county population-agriculture GIS data
- CDDC China County-Level Data on Population and Agriculture
- 中国县级人口（普查）和农业数据（1:100万 GIS 键接）
provider: China in Time and Space (CITAS; University of Washington and University of California-Davis) and CIESIN, archived by NASA SEDAC
china_related: true
domains:
- regional
- urban
- demography
- agriculture
- spatial
- public

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: A provider-compiled county-level 1990 census and agricultural-economic table set keyed to a 1:1M county boundary GIS layer; the archived granule is described as ArcInfo Interchange and DBF files
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: Current NASA CMR metadata identifies a single, free 7.5 MB granule in ArcInfo Interchange and DBF formats, with a detailed description of the 1990 census, agricultural, and 1:1M county-boundary components. That metadata and DOI are publicly readable. Its only listed GET DATA link, however, returned HTTP 404 on 2026-09-28, so the catalog currently supplies a precise identity and archive description but not a verified obtainable file.
  barrier: The current CMR delivery URL returns HTTP 404. The legacy SEDAC route had already been protected by a challenge. The collection's stated terms prohibit commercial/non-free resale or redistribution without written permission and require acknowledgement, but a researcher still lacks a working official download, codebook, field list, and boundary files. A successful provider delivery—not metadata alone—is needed before treating this as immediately usable.

unit_of_observation: County-level aggregate record keyed to a 1:1M GIS administrative boundary, with 1990 census/agricultural measures and selected 1985-1990 migration coverage
structure: county-level cross-section with GIS boundary key
geo_granularity:
- county
- 1:1M county boundary GIS
geography: Mainland China county-level administrative regions covered by the 1990 product; the catalog bounding box is 73-135°E, 18-54°N
time_span:
  start: '1985'
  end: '1990'
  last_confirmed_release: '1997-02-28'
  coverage_note: The core census, agricultural, and boundary data are for 1990. The catalog description specifically notes migration since 1985, so 1985-1990 is a variable-level window rather than a balanced annual panel.
  last_checked: '2026-09-28'
frequency:
- cross-sectional
sample_size: Not stated in the checked catalog metadata; do not infer a county count until the granule/codebook is retrieved
key_variables:
- Urban and rural residence
- Age and sex distribution
- Educational attainment and illiteracy
- Marital status, childbirth, and mortality
- Immigration since 1985
- Industrial/economic activity and occupation
- Ethnicity
- Rural population and agricultural labor force
- Forestry, livestock, fishery, commodities, equipment, utilities, and irrigation
- Agricultural output value
- County boundary geometry and the provider's GIS key

research_fit:
  best_for:
  - County-level 1990 population, education, labor, and agricultural aggregates that can be spatially joined to a historical boundary layer
  - Reconstructing a paper-specific city-proper education control by aggregating counties with an explicitly documented 1990 GIS concordance
  - Historical regional and urban research where a ready-made county table plus boundary key is more useful than raw census publications
  choose_over:
  - Choose this product over china-census when the task needs the public 1990 county aggregate tables and a 1:1M spatial key rather than census microdata or national benchmark aggregates
  - Choose it over a modern county yearbook when the research window is the 1990 census/agricultural cross-section and the historical boundary vintage matters
  - Use the China Statistical Yearbook system alongside it when annual city outcomes, prices, or controls are required; this product is not a substitute for an annual city panel
  not_good_for:
  - Individual or household microdata, confidential census records, or causal estimates by itself
  - A balanced county-year panel or current administrative boundaries
  - Fine urban-core or neighborhood geography; 1:1M county boundaries cannot be treated as city-proper polygons
  - Assuming that every census/agricultural table or the original raw source is included in the downloadable granule
  needs_join_for:
  - City-proper or prefecture outcomes, which require an explicit county-to-city boundary concordance and a decision about counties under a prefecture
  - Annual economic outcomes from statistical yearbooks
  - A treatment, policy, or exposure variable from another source
  variation_available:
  - 1990 county cross-sectional differences and a 1985-1990 migration-related field window are dimensions of the data; no causal or exogenous-variation classification is made here
  topics:
  - historical urbanization
  - county population
  - education geography
  - agricultural development
  - regional inequality
  - GIS concordance

good_for:
- County-level descriptive and spatial analysis using 1990 population/agriculture measures
- Aggregating county education or population measures to a documented historical city definition
- Benchmarking a city or regional panel against 1990 census and agricultural conditions
identification: []
linkable_keys:
- Historical downstream documentation names `GBCENMQ` as a census ID and `NMFULL` as a county-name field in the former county-boundary file; confirm those fields in any currently provider-delivered archive before using them
- County and province names after documented historical-name normalization
- 1990 reference year
- Boundary geometry or centroid from the accompanying GIS layer

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Historical county or city name/concordance
  - Province or prefecture identifier
  - 1990 reference year
  method: Aggregate or match the county table to the statistical-yearbook unit only after checking whether the target is city proper, municipal district, or whole prefecture and preserving boundary changes
  evidence_status: literature-used
- target: china-census
  relation: complement
  keys:
  - 1990 census reference year
  - County/province geography where a concordance is available
  method: Use this product for public county aggregates and GIS linkage, and use the census record for broader census releases or restricted microdata; do not treat them as the same file
  evidence_status: plausible

access_routes:
- route: NASA CMR/Earthdata collection metadata and currently broken delivery link
  access_status: blocked
  direct_url: https://cmr.earthdata.nasa.gov/search/collections.json?concept_id=C3540910546-ESDIS
  requirements:
  - A repaired Earthdata/SEDAC delivery route or a provider-supplied archive
  - Preserve the collection ID C3540910546-ESDIS, short name CIESIN_SEDAC_CD_CTY_POPAG_GIS, version 1.00, and DOI 10.7927/H43N21B3
  steps:
  - Open the CMR collection and its single granule to retain the collection and granule identifiers.
  - Test the listed GET DATA URL before planning analysis; it returned HTTP 404 on 2026-09-28.
  - If the provider repairs delivery, inspect the archive's codebook, file list, boundary key, and terms before constructing a join.
  deliverable: CMR metadata for one 7.5 MB granule described as ArcInfo Interchange and DBF files; no delivered archive was obtainable through the checked current link.
  cost: free
  last_checked: '2026-09-28'
  caveat: The CMR record has access constraints marked None and distribution fees of zero, but its listed Earthdata GET DATA URL returned HTTP 404. Treat a successful delivery, not those metadata fields, as confirmation of current access.
- route: CIESIN/SEDAC legacy data page or provider support
  access_status: needs-verification
  direct_url: https://sedac.ciesin.columbia.edu/data/set/cddc-china-population-census-and-agriculture/data-download
  requirements:
  - A route that is not blocked by the legacy site's challenge or a response from CIESIN metadata support
  steps:
  - Cite DOI 10.7927/H43N21B3 and collection short name when contacting the provider
  - Request the current archive, codebook, and terms if the Earthdata link remains unavailable
  - Record the delivered filenames and checksum before using the data
  deliverable: Provider-confirmed archive and documentation, if available
  cost: free
  last_checked: '2026-09-28'
  caveat: The catalog lists metadata@ciesin.columbia.edu as a contact, but no successful file delivery was verified in this task.

access:
  url: https://catalog.data.gov/dataset/china-dimensions-data-collection-china-county-level-data-on-population-census-and-agricult
  cost: free
  license: CITAS/CIESIN retain copyright; commercial or non-free resale or redistribution requires explicit written permission, and users must acknowledge the providers and notify them of redistribution efforts.
  format:
  - ArcInfo Interchange
  - DBF
  - GIS boundary data
  api: false
  how_to_get: Start with the Data.gov/CMR record and DOI, follow the current Earthdata granule link, and contact CIESIN if migration errors prevent retrieval. Do not substitute a generic 1990 census download for this keyed product.
caveats:
- This is a provider-compiled aggregate product, not 1990 census microdata or the complete raw agricultural source archive.
- A 2005 downstream GIS methodology records historical filenames (`my901.e00` and `chinaag1.dbf`) and the former boundary fields `GBCENMQ`/`NMFULL`; it does not establish that a repaired current archive has the same files, version, table labels, missing-value rules, or boundary topology.
- A 1:1M boundary layer is suitable for historical county aggregation, not for claiming exact urbanized-area or city-proper geography.
- The 1985-1990 temporal metadata should not be misread as annual repeated observations.
- Current NASA metadata specifies non-commercial/non-free resale and redistribution restrictions, but its listed delivery URL is broken; neither a catalog entry nor a zero-fee label establishes current file access.

production:
  raw_sources:
  - name: 1990 China population census aggregates
    source_type: census tables
    role: County-level demographic, education, occupation, and migration measures
    access_route: Provider-compiled CDDC granule
    url: https://catalog.data.gov/dataset/china-dimensions-data-collection-china-county-level-data-on-population-census-and-agricult
    coverage: 1990 county-level aggregate tables; migration is described from 1985
    last_checked: '2026-09-28'
  - name: County agricultural economic statistics
    source_type: statistical tables
    role: Rural population/labor, production, equipment, irrigation, and output measures
    access_route: Provider-compiled CDDC granule
    url: https://catalog.data.gov/dataset/china-dimensions-data-collection-china-county-level-data-on-population-census-and-agricult
    coverage: 1990 county-level agricultural-economic coverage as described by the catalog
    last_checked: '2026-09-28'
  - name: 1:1M county boundary GIS
    source_type: GIS boundary
    role: Spatial key for joining and aggregating county observations
    access_route: Provider-compiled CDDC granule
    url: https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C3540910546-ESDIS
    coverage: County-level administrative regions in the 1990 product
    last_checked: '2026-09-28'
  acquisition_methods:
  - direct download
  - table extraction
  - GIS join
  sample_construction: The provider's aggregate county coverage and any exclusions are not stated in the checked metadata; verify the delivered codebook rather than inferring a complete county universe.
  pipeline_stages:
  - stage: collect
    inputs:
    - 1990 census aggregates
    - agricultural economic tables
    - 1:1M county boundaries
    method: Use the released provider archive; the checked metadata does not document a reproducible raw-table assembly script.
    tools: []
    output: County aggregate records plus a GIS key and boundary layer
    evidence: NASA/Data.gov catalog and CMR collection/granule metadata
  - stage: aggregate
    inputs:
    - County records
    - County boundary key
    method: Researcher-defined aggregation to a city or prefecture after matching historical boundaries; this is downstream use, not part of the released asset.
    tools:
    - GIS software
    output: Researcher-constructed city/county spatial panel or cross-section
    evidence: Au and Henderson Appendix B establishes that education was aggregated from this county/GIS product for their city analysis; the exact concordance is not released in the checked source.
  constructed_variables: []
  validation:
  - Verify the archive's field list, codebook, missing-value codes, and county-key consistency before joining.
  - Compare the GIS vintage and county names with the target yearbook or census geography; do not silently use a later boundary file.
  - Record whether the delivered archive includes the table data, GIS layer, or only one component.
  output:
    unit_of_observation: County-level aggregate record with GIS key
    structure: Cross-section plus spatial boundary layer
    geography: 1990 county-level China product
    time_span: 1985-1990 variable window, core 1990 reference year
    key_variables:
    - Population/demographic measures
    - Education and occupation
    - Agricultural labor, inputs, and output
    - County GIS key and boundary
    formats:
    - ArcInfo Interchange
    - DBF
    - GIS boundary format to be confirmed from the archive
  reproducibility:
    level: low
    starting_point: https://cmr.earthdata.nasa.gov/search/collections.json?concept_id=C3540910546-ESDIS
    code_available: false
    code_url:
    requirements:
    - Access to the current Earthdata/SEDAC route or provider support
    - GIS software for downstream aggregation
    blockers:
    - The current CMR-listed Earthdata GET DATA route returned HTTP 404 on 2026-09-28
    - Exact archive contents, codebook, and county key cannot be inspected until a provider delivers the archive
  compliance:
    terms_or_license: Current CMR metadata states that CITAS/CIESIN hold copyright, prohibits commercial/non-free resale or redistribution without written permission, and requires acknowledgement and notice of redistribution.
    robots_or_rate_limits: No scraping is needed; use the official catalog or provider route and respect current Earthdata terms
    personal_or_sensitive_data: Aggregate census and agricultural records; no individual-level microdata are identified in the catalog description
    redistribution: Do not redistribute the archive or extracted source tables until the current rights statement is checked
    review_needed: true

quality:
  profile_status: verified
  access_status: blocked
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Au & Henderson (2006), Are Chinese Cities Too Small?'
  doi: https://doi.org/10.1111/j.1467-937X.2006.00387.x
  journal: ReStud
  year: 2006
  dataset_role: 1990 educational-attainment control aggregated to the city-proper analysis
  evidence_type: data_appendix
  evidence_url: https://www.brown.edu/Departments/Economics/Faculty/henderson/papers/chinatoosmallcities0905.pdf
  data_note: >-
    Appendix B names this product exactly and states that educational attainment was aggregated from it. The paper's city-level
    economic variables come mainly from the Urban Statistical Yearbook and Cities China 1949-1998; those are separate assets.

provenance:
- source: https://www.brown.edu/Departments/Economics/Faculty/henderson/papers/chinatoosmallcities0905.pdf
  field_scope:
  - exact paper-used dataset name
  - education aggregation role
  - city-proper versus municipal-district boundary warning
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://catalog.data.gov/dataset/china-dimensions-data-collection-china-county-level-data-on-population-census-and-agricult
  field_scope:
  - provider and project identity
  - census/agricultural/boundary contents
  - public catalog status
  - spatial and temporal metadata
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://cmr.earthdata.nasa.gov/search/collections.json?concept_id=C3540910546-ESDIS and https://cmr.earthdata.nasa.gov/search/granules.json?collection_concept_id=C3540910546-ESDIS
  field_scope:
  - collection ID and version
  - 1:1M spatial extent
  - 1985-1990 granule window
  - ArcInfo Interchange and DBF format description
  - current granule link and online-access flag
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://forum.earthdata.nasa.gov/viewtopic.php?t=8029
  field_scope:
  - migration-era 404 and authorization failure report for the exact collection
  added: '2026-08-11'
  confidence: med
  verified: true
- source: https://cmr.earthdata.nasa.gov/search/collections.umm_json?concept_id=C3540910546-ESDIS
  field_scope:
  - Current collection revision, DOI, complete abstract, ArcInfo Interchange/DBF distribution formats, zero fees, and use constraints
  - Provider-stated non-commercial/non-free resale and redistribution boundary
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://cmr.earthdata.nasa.gov/search/granules.umm_json?collection_concept_id=C3540910546-ESDIS
  field_scope:
  - Single current granule identity, 7.5 MB stated size, 1985-1990 range, and listed Earthdata GET DATA URL
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/data/set/cd-china-population-census-and-agriculture/data-download
  field_scope:
  - Current listed delivery route returned HTTP 404 on 2026-09-28
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.researchgate.net/publication/264556152_A_digital_global_map_of_irrigated_areas_An_update_for_Asia
  field_scope:
  - Historical downstream description of `my901.e00`, `chinaag1.dbf`, and the `GBCENMQ`/`NMFULL` county-boundary fields
  - Boundary that this historical file description does not prove the current provider archive is obtainable or unchanged
  added: '2026-09-28'
  confidence: med
  verified: true

related_datasets:
- id: china-stat-yearbook
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

This is a historically important, paper-used county aggregate product with a well-described 7.5 MB archive and a 1:1M GIS key, but its current official delivery link returns 404, so it cannot presently be treated as an obtainable file.

## Select rules

- Prioritize it when the research needs 1990 county education, demography, agriculture, or a historical county-to-city spatial key.
- Pair it with the China Statistical Yearbook system for annual city or prefecture outcomes; do not collapse the two products into one record.
- Switch to the broader China Census record when the question needs national census releases, later waves, or microdata access rather than this 1990 county aggregate.
- Do not use a current boundary file or a generic 1990 census table as a silent substitute for the product's historical GIS key.

## Get recipe

1. Open the CMR collection and single granule using `C3540910546-ESDIS` and DOI `10.7927/H43N21B3`.
2. Test the current Earthdata data-download link. It returned HTTP 404 on 2026-09-28; contact CIESIN/ESDIS with the DOI and identifiers rather than substituting another census product.
3. Inspect the codebook and confirm county identifiers, missing-value conventions, boundary vintage, and whether both tabular and GIS components are included.
4. Only then construct a county-to-city or county-to-prefecture concordance, preserving the distinction between city proper and municipal district.

## Connections and Limitations

The natural join is with a historical city or prefecture outcome by county/province names or the provider's GIS key and a 1990 reference year. That join is not automatic: Au and Henderson's paper demonstrates that the education table was aggregated to city proper, but the checked sources do not provide their exact concordance. The product is therefore a strong spatial input with a conditional access route, not a ready-made city panel or evidence for a particular identification strategy.
