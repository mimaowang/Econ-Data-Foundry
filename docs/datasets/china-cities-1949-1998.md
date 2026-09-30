---
schema_version: 3
catalog_status: ready
id: china-cities-1949-1998
name: Cities China 1949-1998 (新中国城市50年)
aka:
- 新中国城市50年
- 新中国城市五十年
- Xin Zhongguo Chengshi 50 Nian
- Cities China 1949-1998
provider: National Bureau of Statistics Urban Social and Economic Survey Group (国家统计局城市社会经济调查总队); bibliographic records list Xinhua Press, Beijing, 1999
china_related: true
domains:
- urban
- regional
- demography
- public
- spatial

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: A 685-page Chinese statistical compilation containing selected city statistics and historical city-establishment/administrative-area information; the paper uses the printed compilation as a source, not a separately released machine-readable panel
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The current CiNii Books record directly identifies the Chinese-language volume as a 1999.12 Xinhua Press publication edited by the NBS Urban Social and Economic Survey Group, ISBN 7501147531, with 685 pages and nine listed holdings. A researcher can therefore choose a specific holding or request interlibrary access and extract only the needed tables with page provenance. No stable public bulk download or author replication file is identified; reproducing a panel remains manual table extraction plus boundary-history interpretation.
  barrier: This is a library-mediated printed source, not a free digital data route. Holding availability, copying permissions, and scan delivery vary by institution, and the catalog record does not license redistribution of scans or a full transcription.

unit_of_observation: City-level statistical entry and historical city-establishment/administrative-area record; exact table grain varies by section and requires inspection of the volume
structure: Historical city compilation with selected city statistics and administrative-history tables
geo_granularity:
- prefecture-level city
- city
- administrative area history
geography: Chinese cities covered by the 1949-1998 compilation; Au and Henderson use prefecture-level city data and a city-proper definition for their estimating sample
time_span:
  start: '1949'
  end: '1998'
  last_confirmed_release: '1999-12'
  coverage_note: The title and catalog cover 1949-1998, but the paper-specific statistical use verified here is selected prefecture-city data for 1990-1997 plus a history of city establishment and administrative-area changes. The book also documents 1992-1993 prefecture-city GDP that was missing from the corresponding annual Yearbook volumes.
  last_checked: '2026-09-28'
frequency:
- historical annual tables (selected years/series)
- event-dated administrative history
sample_size: Not stated as a single machine-readable count; Au and Henderson begin with 223 prefecture-level cities and estimate on 205 after exclusions, which is a paper sample rather than the book's total coverage
key_variables:
- Selected prefecture-city statistics for 1990-1997
- City GDP entries, including 1992-1993 values documented where annual Yearbook data were missing
- City establishment history
- Administrative-area changes of cities
- Historical city population and urban-system statistics (table-level availability requires inspection)

research_fit:
  best_for:
  - Filling historical city-year gaps and recovering a boundary-aware city series for the 1990s
  - Reconstructing when cities were established or their administrative areas changed
  - Long-run urban-system work that needs a historical compilation rather than only current statistical-yearbook releases
  choose_over:
  - Choose it over the China Statistical Yearbook system when the research needs the book's historical administrative history or the 1992-1993 prefecture-city GDP entries documented by Au and Henderson
  - Use the annual Urban Statistical Yearbook alongside it when consistent annual variable definitions and table-by-table source pages are the priority
  - Choose it over a modern city database when the boundary vintage and long historical city sequence are part of the research question
  not_good_for:
  - Household, firm, or individual microdata
  - A guaranteed machine-readable panel, current city coverage, or post-1998 statistics
  - Treating all historical entries as comparable annual observations without checking table definitions and boundary changes
  - Assuming the book itself supplies the county GIS crosswalk used for education aggregation in Au and Henderson
  needs_join_for:
  - Annual city outcomes and controls from the Urban Statistical Yearbook or other statistical-yearbook tables
  - County-level education/population inputs and a historical GIS key
  - Policy, treatment, or exposure variables from another source
  variation_available:
  - City-establishment and administrative-area dates are historical fields in the compilation; no causal or exogenous-variation classification is made here
  topics:
  - urbanization
  - city size
  - administrative boundaries
  - historical regional development
  - city statistics

good_for:
- Historical descriptive city panels after manual extraction and boundary harmonization
- Boundary-aware aggregation of city and prefecture outcomes
- Reproducing the book component of Au and Henderson's 1990-1997 city-data construction
identification:
- This printed statistical compilation is a descriptive data source, not a causal design or a verified treatment-assignment dataset.
- Historical establishment and administrative-area dates help define geography but do not independently identify a causal effect.
linkable_keys:
- City name in the volume's historical spelling
- Province and prefecture-city label
- Year or city-establishment/administrative-change date
- Researcher-built concordance to the target boundary vintage

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - City name and province
  - Year 1990-1997
  - Statistical table/indicator label
  method: Use the book to supplement or cross-check annual Yearbook entries; preserve the source edition and definition instead of silently blending values
  evidence_status: literature-used
- target: china-county-population-agriculture-gis-1990
  relation: complement
  keys:
  - Historical city/county boundary concordance
  - 1990 reference year
  method: If reproducing the education aggregation, build and document a separate county-to-city crosswalk; the checked sources do not show that this book contains the GIS layer itself
  evidence_status: plausible

access_routes:
- route: Library catalog and interlibrary loan
  access_status: available-with-conditions
  direct_url: https://ci.nii.ac.jp/ncid/BA55841244
  requirements:
  - Library membership or interlibrary-loan/scan request
  - Chinese-language table extraction and a reproducible transcription log
  steps:
  - Search by ISBN 7501147531, NCID BA55841244, or the Chinese title 新中国城市50年
  - Use the current CiNii record to select one of its nine listed holdings, then confirm the physical title page, edition, and table of contents at consultation
  - Request the relevant 1990-1997 city tables and administrative-history pages under the library's copyright rules
  - Record page/table numbers, units, definitions, and any missing or changed city boundaries before digitizing
  deliverable: Physical consultation, library scan, or researcher-transcribed tables; no public machine-readable file was verified
  cost: mixed
  last_checked: '2026-09-28'
  caveat: Current CiNii metadata lists nine holdings and identifies the Xinhua Press imprint, but availability and scan permissions differ by institution. A citation to the book does not grant permission to redistribute a scan or a full transcription.
- route: Commercial or institutional Chinese book/database access
  access_status: needs-verification
  direct_url: https://search.worldcat.org/search?q=isbn%3A7501147531
  requirements:
  - A library or vendor subscription that actually holds this 1999 volume
  steps:
  - Verify the physical or digitized edition and publisher before purchase
  - Ask whether table-level export or scan reuse is permitted
  - Preserve the source edition and page references in any derived panel
  deliverable: Vendor or library copy subject to its terms
  cost: mixed
  last_checked: '2026-08-11'
  caveat: No stable public full-text or bulk-data endpoint was found in this grounding pass.

access:
  url: https://ci.nii.ac.jp/ncid/BA55841244
  cost: mixed
  license: Library and publisher copyright terms; no open-data license was identified
  format:
  - printed Chinese volume
  - library scan if permitted
  - researcher-transcribed table
  api: false
  how_to_get: Locate the ISBN/NCID record, obtain a library copy, verify the title page and tables, and transcribe only the needed variables with page-level provenance. Do not present the book as a downloadable panel unless a verified digital release is found.
caveats:
- The current CiNii record identifies the volume as Xinhua Press (1999.12); retain the edition and page evidence from the consulted copy because other secondary citations can still be imprecise.
- The selected 1990-1997 city statistics are not evidence that every city or every variable is present for every year.
- Historical administrative changes can make a city label refer to different geographic areas; use the book's history and a documented concordance.
- The book component is distinct from the annual Urban Statistical Yearbook, the 1990 county/GIS product, and the paper's final cleaned analysis file.
- Copyright and scan/transcription permissions remain unresolved.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Au & Henderson (2006), Are Chinese Cities Too Small?'
  doi: https://doi.org/10.1111/j.1467-937X.2006.00387.x
  journal: ReStud
  year: 2006
  dataset_role: Selected city statistics and administrative-history source for the 1990-1997 city-level agglomeration analysis
  evidence_type: data_appendix
  evidence_url: https://www.brown.edu/Departments/Economics/Faculty/henderson/papers/chinatoosmallcities0905.pdf
  data_note: >-
    Appendix B states that most city-level economic and amenity variables came from the 1991-1998 annual Urban Statistical
    Yearbook volumes and Cities China 1949-1998. The paper begins with 223 prefecture-level cities, retains 205 after exclusions,
    and measures the city proper rather than the whole municipal district. A related data appendix also notes that the book
    documents prefecture-city GDP for 1992-1993 when the annual Yearbook lacks those entries.

provenance:
- source: https://www.brown.edu/Departments/Economics/Faculty/henderson/papers/chinatoosmallcities0905.pdf
  field_scope:
  - exact paper use
  - 1990-1997 statistical role
  - city-establishment and administrative-area history role
  - city-proper versus municipal-district boundary warning
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://users.nber.org/~confer/2003/cwgf03/henderson.pdf
  field_scope:
  - selected 1990-1997 prefecture-city compilation
  - 1992-1993 GDP gap in annual Yearbook and book supplementation
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://ci.nii.ac.jp/ncid/BA55841244
  field_scope:
  - Chinese title and aliases
  - editor/organization
  - 1999 publication metadata
  - ISBN, NCID, page count, language, and library holdings
  added: '2026-08-11'
  confidence: high
  verified: true
- source: https://ci.nii.ac.jp/ncid/BA55841244
  field_scope:
  - Current direct catalog access, Xinhua Press 1999.12 imprint, ISBN 7501147531, 685-page extent, and Chinese-language identity
  - Nine currently listed library holdings and a concrete library-consultation route
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-stat-yearbook
  relation: complement
- id: china-county-population-agriculture-gis-1990
  relation: complement
---

## Positioning in one sentence

Cities China 1949-1998 is a paper-used historical city compilation, not a generic synonym for the China Statistical Yearbook: its distinctive value is the combination of selected 1990-1997 city statistics with city-establishment and administrative-area history, while its realistic route is manual extraction from a specifically identified library-held 685-page volume rather than a downloadable panel.

## Select rules

- Prioritize it when a historical city panel needs boundary history or when the annual Yearbook has a documented gap, such as the 1992-1993 prefecture-city GDP entries used by Au and Henderson.
- Pair it with the annual Urban Statistical Yearbook rather than replacing the Yearbook wholesale; record which edition supplied each variable.
- Use the county/GIS product separately for county-level education aggregation. This volume is not evidence that a GIS crosswalk or paper's final city panel is publicly released.
- If a study needs post-1998 or machine-readable current data, switch to a verified statistical-yearbook or another explicitly released city panel.

## Get recipe

1. Search the CiNii record by ISBN `7501147531`, NCID `BA55841244`, or the Chinese title.
2. Select a listed holding, obtain a library copy or permitted scan, and retain the consulted copy's title-page and edition evidence.
3. Extract only the needed tables and administrative-history entries with page, unit, and definition references.
4. Build a city-name and boundary concordance before joining the annual Yearbook, county GIS, or another outcome source; preserve missing years and definition changes.

## Connections and Limitations

The practical connection is to the annual city statistical yearbooks by city, province, year, and indicator label, with the book supplying historical boundary and selected missing-year information. A second, conditional connection is to the 1990 county/GIS product for city-proper education aggregation. Neither connection is automatic, and neither makes a printed compilation equivalent to the paper's final cleaned analysis file.
