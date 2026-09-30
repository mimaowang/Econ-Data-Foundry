---
schema_version: 3
catalog_status: grounding
id: china-agricultural-census-1997-1pct
name: 1997 China First National Agricultural Census 1% sample (county-level extract)
aka:
- 第一次全国农业普查
- China First National Agricultural Census 1997
- 1997 Agricultural Census 1% sample
- 农业普查1%抽样
provider: >-
  National Bureau of Statistics of China (国家统计局) / 全国农业普查办公室
  (First National Agricultural Census Office). The 1% sample extract used by
  Qian (2008 QJE) was obtained through the Michigan China Data Center and
  personal research channels (paper acknowledgements); no public or
  application-based release of the 1% sample is evidenced.
china_related: true
domains:
- agriculture
- demography
- regional
- census

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    The 1% sample of the 1997 Chinese Agricultural Census: county-level
    microdata/aggregates aggregated to birth-year-county cells (used by Qian
    2008 QJE for sex-imbalance analysis; includes county-level sown-area
    inputs for tea, orchard, cash crops in mu). No public download or
    application route is evidenced.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    Grounding pass (2026-08-15): existence of the first national
    agricultural census (reference date 1997-01-01) is confirmed, and the
    published aggregate compendium 中国第一次农业普查资料综合提要 (全国农业普查办公室
    编, 中国统计出版社 2000, 448 pp, ISBN 7-5037-2871-X) is bibliographically
    confirmed via a library MARC record - aggregate tables only (households,
    villages, townships, eight parts). The 1% SAMPLE specifically: the GHDx
    catalog holds a metadata-only record (China First National Agricultural
    Census 1997, household survey, 01-12/1997) with no microdata access;
    no NBS lab, IPUMS, World Bank or IHSN route surfaced (World Bank/FAO
    NADA search APIs did not honor query terms in this environment;
    IHSN citation 63062 404s; WB study 462 is the 1990 population census
    IPUMS subset, not this census). Qian (2008 QJE) obtained the 1% sample
    via Michigan China Data Center and personal channels (paper
    acknowledgements: Michigan Data Center, Huang Guofang, Terry Sicular).
  barrier: >-
    No public provider, NBS lab, or author-site route delivers the 1997 1%
    extract. Qian's paper has no data-availability statement or replication
    package. The only confirmed public artifacts are aggregate tables (the
    2000 compendium; NBS first-census HTML tables, verified 2026-08-13),
    which are NOT the 1% sample.

unit_of_observation: >-
  Per the paper: individuals in the 1% sample of the 1997 agricultural
  census aggregated to birth-year-county cells; county-level sown-area
  inputs from the same 1% extract
structure: cross-section (1% sample), aggregated to birth-year-county cells in the paper
geo_granularity:
- county
geography: >-
  All 1,621 counties of the 15 southern tea-producing provinces (per Qian
  2008 QJE sample definition); the census itself is national
time_span:
  start: '1997'
  end: '1997'
  last_confirmed_release: 'Census reference date 1997-01-01 (GHDx catalog period 01/1997-12/1997)'
  coverage_note: >-
    The census is a 1997 cross-section; the paper restricts to rural
    residents born 1962-1990 living in a rural area in 1990 with 5+ years
    residence in the same county.
  last_checked: '2026-08-15'
frequency:
- cross-sectional
sample_size: >-
  The census covered all agricultural households nationally (universe);
  the 1% sample is a 1-per-100 extract. Sample sizes for the paper's
  analysis cells are not published outside the paper.
key_variables:
- Sex/age structure (used for sex-imbalance outcome)
- County identifiers (matching to the 1990 census within cross-section)
- Sown-area inputs: tea, orchard, cash crops (mu), county level
- Rural residence and migration-stability indicators (per paper sample definition)

research_fit:
  best_for:
  - Documenting the exact asset behind Qian (2008 QJE) sex-ratio analyses and its inaccessibility boundary
  - County-level 1997 agricultural aggregates via the published compendium when the 1% sample is not required
  choose_over:
  - Choose the published aggregate compendium (综合提要 2000) or NBS first-census HTML tables when county/province-level aggregates suffice - they are public and bibliographically confirmed.
  - Choose china-county-population-agriculture-gis-1990 (SEDAC CDDC 1990 granule) for 1990 county population/agriculture GIS-keyed aggregates - a different census year and product.
  - Do NOT choose any commercial resale or scan of the compendium as a substitute for the 1% sample.
  not_good_for:
  - Replicating Qian (2008 QJE) from public sources - the 1% sample is not publicly obtainable
  - Treating NBS aggregate tables or the compendium as the 1% sample
  - Assuming GHDx/IHSN/World Bank catalog records imply microdata access (metadata-only records)
  needs_join_for:
  - 1990 census 1% sample and GIS boundaries (see china-county-population-agriculture-gis-1990) for the paper's within-cross-section matching
  variation_available:
  - Within-census county and birth-year variation (1% sample, paper-internal)
topics:
- agricultural census
- sex ratio
- county data
- historical microdata

good_for:
- Understanding what Qian (2008 QJE) actually used and why it is not obtainable
- County-level 1997 agricultural aggregates from public published tables
identification: []
linkable_keys:
- County (geographic identifiers; paper notes cross-census county linking is difficult - footnote 20)
- Birth year

joins:
- target: china-county-population-agriculture-gis-1990
  relation: complement
  keys:
  - County
  method: The paper matched the 1990 census and the 1997 agricultural census within one cross-section; public GIS keys require name/boundary normalization
  evidence_status: literature-used

access_routes:
- route: restricted-personal-channel
  access_status: inaccessible
  direct_url: needs-verification
  requirements: >-
    Qian (2008 QJE) obtained the 1% sample via the Michigan China Data
    Center and personal assistance (acknowledgements). No application form,
    fee schedule, or repository route is evidenced.
  steps:
  - Contact the author (Nancy Qian, Kellogg) to ask whether the county-birth-year sample, the sown-area extract or code exists and under what conditions it could be shared (per candidate next-action; not yet attempted).
  deliverable: Unverified; author discretion only
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Author-contact route is a research courtesy, not an established access channel.
- route: public-aggregates
  access_status: available
  direct_url: https://www.stats.gov.cn/sj/pcsj/nypc/dycnypc/
  requirements: None
  steps:
  - Use the NBS first-agricultural-census HTML aggregate tables (national/provincial/terrain level; verified 2026-08-13) or the printed compendium 中国第一次农业普查资料综合提要 (2000, ISBN 7-5037-2871-X).
  deliverable: Aggregate tables only - NOT the 1% sample
  cost: free
  last_checked: '2026-08-15'
  caveat: Do not treat these aggregates as the 1% sample extract.

access:
  url: needs-verification
  cost: by-application
  license: Unknown; no release terms evidenced
  format: []
  api: false
  how_to_get: >-
    No public route. The 1% sample is obtainable only through the paper
    authors' personal channel (unverified). Public alternatives: NBS
    aggregate tables and the 2000 printed compendium.
caveats:
- The GHDx record is metadata-only (catalog entry, no data access link) - not proof of availability.
- WB study 462 is the 1990 population census IPUMS subset, not the 1997 agricultural census.
- The paper's acknowledgements show acquisition via Michigan China Data Center + personal assistance; no data-availability statement exists.

quality:
  profile_status: verified
  access_status: blocked
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Qian (2008), Missing Women and the Price of Tea in China'
  doi: https://doi.org/10.1162/qjec.2008.123.3.1251
  journal: QJE
  year: 2008
  dataset_role: >-
    Sex-imbalance outcome and county sown-area inputs (tea, orchard, cash
    crops) from the 1% sample of the 1997 Chinese Agricultural Census,
    aggregated to birth-year-county cells
  evidence_type: data-section
  evidence_url: https://www.kellogg.northwestern.edu/faculty/qian/resources/Missing-Women_QJE_20080407_all.pdf
  data_note: >-
    Final PDF read in full (2026-08-13): the sex-imbalance analysis uses
    'the 1% sample of the 1997 Chinese Agricultural Census, the 1% sample
    of the 1990 China Population Census and GIS data from the Michigan
    China Data Center'; sample = all 1,621 counties of the 15 southern
    tea-producing provinces, rural residents born 1962-1990; footnote 20
    notes county linking across censuses is difficult so matching is within
    one cross-section; acknowledgements thank the Michigan Data Center,
    Huang Guofang and Terry Sicular. No DAS or replication package.

provenance:
- source: http://opac.sdtbu.edu.cn/opac/show_format_marc.php?marc_no=0f6e5263503153640e635167016652330e355633 (read 2026-08-15)
  field_scope:
  - compendium bibliographic record: 中国第一次农业普查资料综合提要, 全国农业普查办公室编, 中国统计出版社 2000, 448 pp, ISBN 7-5037-2871-X, F32-66
  - contents description: eight parts incl. households, villages, townships - aggregate tables
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://ghdx.healthdata.org/record/china-first-national-agricultural-census-1997 (read 2026-08-15)
  field_scope:
  - GHDx catalog record: China First National Agricultural Census 1997, survey (household), period 01/1997-12/1997, China
  - no microdata download/access link in the record (metadata-only)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://microdata.worldbank.org/index.php/catalog/462 (read 2026-08-15)
  field_scope:
  - WB study 462 = China Fourth National Population Census IPUMS Subset 1990 (NOT the 1997 agricultural census)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: NBS first agricultural census pages (verified 2026-08-13; cited in candidate ledger)
  field_scope:
  - official aggregate HTML tables only (national/provincial/terrain); no county level, no 1% sample, no microdata
  added: '2026-08-13'
  confidence: high
  verified: true
- source: Qian (2008 QJE) final PDF (Kellogg copy; read 2026-08-13)
  field_scope:
  - exact asset use, sample definition, matching strategy, acquisition channel (acknowledgements)
  added: '2026-08-13'
  confidence: high
  verified: true

related_datasets:
- id: china-county-population-agriculture-gis-1990
  relation: complement
- id: china-census
  relation: often-confused-with
---

## Positioning in one sentence

The 1% sample of the 1997 China First National Agricultural Census - the exact asset behind Qian (2008 QJE)'s sex-ratio analysis - is confirmed to exist but is not publicly obtainable (personal/Michigan-China-Data-Center channel only); the public substitutes are NBS aggregate tables and the printed compendium 中国第一次农业普查资料综合提要 (2000, ISBN 7-5037-2871-X), which are NOT the 1% sample.

## Select rules

- Use this record to prevent false recommendations: any claim that the 1997 census 1% sample is downloadable is unsupported.
- For county-level 1997 agricultural aggregates, use the public compendium/NBS tables; for 1990 county census-GIS aggregates, use china-county-population-agriculture-gis-1990.
- Contact the author only as a research-courtesy route; do not promise access.

## Get recipe

1. If the research needs the 1% sample itself: no public route exists; the realistic step is author contact (Nancy Qian, Kellogg) - outcome unverified.
2. For public aggregates: NBS first-census HTML tables (stats.gov.cn/sj/pcsj/nypc/dycnypc/) or the printed 综合提要 (2000).
3. Do not confuse GHDx/WB/IHSN catalog records with data access; do not treat aggregate tables as the 1% extract.

## Connections and Limitations

The paper matched the 1990 census and 1997 agricultural census within one cross-section because cross-census county linking is difficult (footnote 20); the public GIS-keyed 1990 product (china-county-population-agriculture-gis-1990) is the nearest obtainable spatial layer, not a substitute for the 1% sample. Blocked routes this round: IHSN citation 63062 (404), WB/FAO NADA search APIs (query terms not honored), NLC OPAC (timeout), Wayback infra (timeout), duxiu scan (not used as evidence).
