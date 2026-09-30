---
schema_version: 3
catalog_status: ready
id: china-nighttime-lights
name: China nighttime lights from the DMSP-OLS and NPP-VIIRS family (EOG official composites; China-corrected versions PANDA and harmonized NTL)
aka:
- 夜间灯光数据
- DMSP-OLS
- NPP-VIIRS
- VIIRS DNB
- Nighttime light data
- Night-time lights (NTL)
- 夜光遥感
- VNL (EOG annual VIIRS Nighttime Lights)
- PANDA 中国长序列夜间灯光数据
- Harmonized global nighttime light dataset
provider: "Earth Observation Group (EOG), Payne Institute for Public Policy, Colorado School of Mines — current official distributor of the DMSP-OLS and VIIRS DNB composites (successor of NOAA NGDC/NCEI distribution); the China-corrected versions are separate researcher-built products — PANDA by the Tsinghua University / HKU team hosted on the National Tibetan Plateau / Third Pole Environment Data Center (TPDC); harmonized NTL by Li, Zhou, Zhao et al. (Iowa State Univ. et al.) hosted on figshare"
china_related: true
domains:
- urban
- geography
- environment
- regional
- energy
- infrastructure
- development

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Gridded GeoTIFF composites of nighttime light intensity — EOG DMSP-OLS Version 4 annual composites (1992-2013) and EOG VIIRS DNB monthly/annual composites (2012- ); China-corrected long-series versions are separate downloadable products (PANDA 1984-2020, harmonized NTL 1992-2018/2024)
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: "A ready public route is the harmonized global NTL dataset on figshare: its live API confirms a dataset titled 'Harmonization of DMSP and VIIRS nighttime light data from 1992-2024 at the global scale', CC BY 4.0, with 34 annual GeoTIFF files (rechecked 2026-09-28). This direct long-series route is distinct from the official EOG original composites, which require a free account, and from China-specific PANDA on TPDC. EOG DMSP-OLS gives annual ~1 km composites 1992-2013 in DN 0-63 (not calibrated radiance); NPP-VIIRS DNB gives monthly ~500 m radiance composites (nW/cm2/sr) from 2012. The triggering RSUE 2026 paper's publisher-visible text establishes 2015 NASA-nighttime-light use but not its exact product, version, resolution or delivery route."
  barrier: EOG bulk downloads require a free account (registration page returns 404 to anonymous clients; signup mechanics need a human browser). NOAA NGDC/NCEI legacy download pages are dead (404/SSL-EOF). DN values are not radiance and are not comparable across DMSP years without intercalibration.

unit_of_observation: Grid cell — 30 arc-second (~1 km at the equator) for DMSP-OLS annual composites; 15 arc-second (~500 m) for VIIRS DNB monthly and annual composites; PANDA and harmonized NTL are annual grids at ~1 km scale (PANDA space scope = China 73.33E-135.05E, 3.51N-53.33N)
structure: Gridded time series (annual composites; monthly VIIRS layer)
geo_granularity:
- grid
- City/county/province (after user aggregation from grids)
geography: "Global coverage incl. mainland China (DMSP-OLS — 180W-180E, 65S-75N; VIIRS DNB — 180W-75N-180E-65S; PANDA — China only)"
time_span:
  start: '1992'
  end: ongoing
  last_confirmed_release: '2022 (annual VNL v22 directory observed on eogdata.mines.edu; monthly series documented through 2020 v1 with v2.1 lit masks through 2021)'
  coverage_note: "DMSP-OLS annual — 1992-2013. VIIRS DNB monthly v1 — 2012-2020 non-tiled (vcm/vcmsl); annual VNL — V1 (vcm) and V2 consistent series 2012*-2020 with two 2012 sets (A — 201204-201212; B — 201204-201303); v2.1 lit masks 2012-2021; product directories v20/v21/v22 observed (2020/2021/2022). PANDA — 1984-2020 annual, China. Harmonized NTL — 1992-2018 annual global (paper), figshare v10 titled 1992-2024 with 34 annual GeoTIFFs. EOG FAQ documents a VIIRS DNB calibration change on 2017-01-12 (dark offset switched from dark-ocean to space view, small upward radiance shift) that matters for time-series work."
  last_checked: '2026-08-14'
frequency:
- annual (DMSP-OLS; EOG annual VNL; PANDA; harmonized NTL)
- monthly (VIIRS DNB cloud-free composites)
sample_size: Global grids; China subset depends on the study boundary; PANDA = 37 annual China grids (1984-2020), 308 MB archive per TPDC metadata
key_variables:
- "DMSP-OLS v4 — avg_vis (average visible-band DN, 0-63), stable_lights.avg_vis (1-63, ephemeral lights removed), intercal.stable_lights.avg_vis, orm_avg_vis, cf_cvg/cvg (observation counts), lit_mask; GeoTIFF EPSG:4326"
- "VIIRS DNB monthly v1 — avg_rade9 / avg_rade9h (mean radiance nW/cm2/sr), cf_cvg/cvg"
- "VNL V2 annual — average / average-masked (mean radiance, background masked), cf_cvg/cvg, lit masks (v2, v2.1)"
- "PANDA — annual simulated artificial nighttime-light intensity, China 1984-2020 (NTLSTM deep-learning synthesis of DMSP-OLS + NPP-VIIRS)"
- "Harmonized NTL — Harmonized_DN_NTL_YYYY_calDMSP.tif (DN, 30 arc-sec, stepwise-calibrated DMSP 1992-2013 + simulated DMSP-like from VIIRS 2014-2018)"

research_fit:
  best_for:
  - Long-run (1992- ) gridded measures of urbanization / human activity intensity for China at ~1 km (DMSP) or ~500 m (VIIRS), e.g. urban-subcenter identification, urban expansion, electrification/energy proxies
  - Constructing city/county-level light-intensity aggregates for spatial panels by zonal statistics from the grids
  - Pre-2012 applications that need the DMSP-OLS annual series (the longest running NTL archive)
  choose_over:
  - Choose PANDA (1984-2020, China) or harmonized NTL (1992-2018+) when the design needs one consistent cross-sensor series and the researcher does not want to do their own intercalibration/harmonization
  - Choose EOG raw composites when the researcher needs the original products, wants to control intercalibration themselves, or needs VIIRS monthly frequency
  - Over china-satellite-pm25 for light intensity itself (PM2.5 grids answer pollution exposure, not human activity)
  not_good_for:
  - Treating DN values as calibrated radiance without intercalibration (DMSP has no on-board calibration; use intercal.stable_lights or a published intercalibration table)
  - Cross-year or cross-sensor level comparisons without harmonization (sensor drift, DN saturation/blooming in bright city cores, the 2017-01-12 VIIRS calibration change)
  - Month-level work before 2012 (monthly VIIRS starts 2012; DMSP is annual only)
  - Measuring actual economic output, population or energy at fine scale directly: NTL is a proxy with saturation and blooming limits
  - Areas with zero cloud-free observations in a composite (must use cf_cvg to exclude; missing coverage is not zero)
  needs_join_for:
  - Administrative-level analysis (aggregate grids to counties/cities; needs boundary shapefiles or admin codes)
  - Socioeconomic outcomes (surveys, yearbooks, census) for validation or outcomes
  - Weather/pollution controls at the same grid (era5-land, china-satellite-pm25)
  variation_available:
  - Annual (and monthly for VIIRS) temporal variation in light intensity at grid level; cross-city/county spatial gradients; the DMSP-VIIRS overlap 2012-2013 and the VIIRS calibration shift 2017-01-12 are documented measurement breaks
  topics:
  - nighttime lights
  - urbanization
  - urban expansion
  - satellite remote sensing
  - regional development
  - energy consumption proxy

good_for:
- Long-run China urbanization and urban-structure measurement (subcenters, built-up expansion)
- Grid-to-admin zonal aggregates for spatial panels 1992-2024
identification:
- >-
  For the ready direct route, identify the product as figshare article 9828827,
  titled "Harmonization of DMSP and VIIRS nighttime light data from 1992-2024
  at the global scale", with annual files named
  Harmonized_DN_NTL_YYYY_calDMSP.tif and CC BY 4.0. It is a harmonized annual
  DN series, not EOG's original radiance product.
- >-
  Identify EOG DMSP-OLS originals by the 1992-2013 annual v4 composite family
  and DN 0-63 fields, and EOG VIIRS by 2012-onward radiance fields such as
  avg_rade9. PANDA is a separate China-only, NTLSTM-constructed 1984-2020
  product hosted through TPDC. Do not substitute among these products merely
  because all are described as "nighttime lights".
linkable_keys:
- Grid cell (lat/lon)
- Year / month
- Administrative unit (after zonal aggregation with boundary data)

joins:
- target: china-satellite-pm25
  relation: complement
  keys:
  - Grid cell
  - Year
  method: Both are global grids; aggregate both to the same admin unit or grid scale before joining; verify grid registration (EPSG:4326) and resolution mismatch (1 km vs 0.01 deg)
  evidence_status: plausible
- target: era5-land
  relation: complement
  keys:
  - Grid cell
  - Year/month
  method: Spatial-temporal match at grid or admin level; resolution differs (0.1 deg), aggregate consistently
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - County code or name
  - Census year
  method: Zonal-mean light by county, matched on NBS codes/boundaries; census geography changes across waves
  evidence_status: plausible

access_routes:
- route: EOG official download (DMSP-OLS v4 annual and VIIRS DNB monthly/annual)
  access_status: available-with-registration
  direct_url: https://eogdata.mines.edu/products/dmsp/
  requirements:
  - Free EOG account. FAQ official text: 'Most data in EOG are now required user to have an EOG account in order to download.'
  - Data tree requires the account: anonymous fetches of /wwwdata/dmsp/v4composites_rearrange/ and /wwwdata/vnl/v22/ redirect to the EOG Keycloak login (eogauth.mines.edu/realms/eog, verified 2026-08-14)
  steps:
  - Register the free EOG account in a human browser (the register page /register/index.html returns 404 to anonymous clients; signup mechanics were not verifiable from this environment)
  - Open https://eogdata.mines.edu/products/dmsp/ (DMSP-OLS v4, files F1?YYYY_v4b_*.tif in the v4composites_rearrange tree) or https://eogdata.mines.edu/products/vnl/ (VIIRS monthly and annual VNL)
  - Download the GeoTIFFs; for time series, also download the intercalibration coefficient table for DMSP
  deliverable: GeoTIFFs, EPSG:4326 — DMSP-OLS annual composites 1992-2013 (30 arc-sec); VIIRS DNB monthly v1 2012-2020 (15 arc-sec) and annual VNL series
  cost: registration
  last_checked: '2026-08-14'
  caveat: NOAA NGDC/NCEI legacy pages are dead (ngdc.noaa.gov/eog/dmsp/downloadV4composites.html and /eog/viirs/download_dnb_composites.html return 404 as of 2026-08-14); the register page and exact account mechanics need a human browser; many products carry CC BY 4.0 with an EOG citation requirement (license PDF on the EOG site)
- route: PANDA (China 1984-2020) via TPDC
  access_status: needs-verification
  direct_url: https://data.tpdc.ac.cn/
  requirements:
  - TPDC account (platform norms; the account/download flow was not re-verified this pass)
  steps:
  - Find the record 'A Prolonged Artificial Nighttime-light Dataset of China (1984-2020)' (PANDA), DOI 10.11888/Socioeco.tpdc.271202 (metadata export verified 2026-08-14)
  - Download the annual China grids (archive ~308 MB)
  deliverable: 37 annual China grids 1984-2020 (filesize 308 MB per TPDC metadata)
  cost: free
  last_checked: '2026-08-14'
  caveat: TPDC is the official national data center host named by the authors (Tsinghua/HKU); the paper is Zhang et al. (2024) Scientific Data 11:414, DOI 10.1038/s41597-024-03223-1. The CAS Earth mirror (data.casearth.cn dataset 653a5b40819aec42f0f38e48) exists but its page is a JS shell in this environment — not used as evidence.
- route: Harmonized global NTL (Li et al. 2020) via figshare or GEE mirror
  access_status: available
  direct_url: https://doi.org/10.6084/m9.figshare.9828827
  requirements:
  - "figshare — none (public download; CC BY 4.0). GEE mirror — free Earth Engine account"
  steps:
  - Download the annual GeoTIFFs Harmonized_DN_NTL_YYYY_calDMSP.tif from figshare article 9828827 (v10, 34 files, series titled 1992-2024; API verified 2026-08-14)
  - Alternatively load the community GEE assets projects/sat-io/open-datasets/Harmonized_NTL/dmsp and /viirs (1992-2021 v7 per the community catalog page)
  deliverable: Annual global 30 arc-sec harmonized DN grids (paper range 1992-2018; figshare v10 extends to 2024)
  cost: free
  last_checked: '2026-08-14'
  caveat: The paper's data-availability metadata record is figshare 10.6084/m9.figshare.12312125 (metadata only); the actual data article is 9828827 (verified via figshare API). The GEE mirror is community-curated, not the authors' official host.

access:
  url: https://doi.org/10.6084/m9.figshare.9828827
  cost: free
  license: Harmonized NTL on figshare is CC BY 4.0; many EOG products are also CC BY 4.0 with account-based access; TPDC terms apply separately to PANDA
  format:
  - geotiff
  api: false
  how_to_get: For a directly downloadable long annual series, start with the CC BY 4.0 figshare harmonized NTL dataset (article 9828827; 34 annual GeoTIFFs, 1992-2024), subset China and aggregate grids as needed. Use EOG originals only when their separate account-gated DMSP/VIIRS products or monthly VIIRS timing is required; use PANDA when its China-specific 1984-2020 construction is the intended product.
caveats:
- The triggering paper (Wang & Dong 2026 RSUE, DOI 10.1016/j.regsciurbeco.2026.104246) is publisher-visible as using NASA nighttime-light data to identify 2015 city subcenters, but does not expose the exact product/version/resolution or a delivery route in the available text. Do not infer DMSP versus VIIRS from the year alone. The paper's full methods and any replication materials remain unavailable through the checked public routes.
- DMSP DN values (0-63) are not radiance and saturate in bright urban cores; use intercalibrated versions for multi-year panels.
- VIIRS DNB had a calibration change on 2017-01-12 (documented in the EOG FAQ); monthly composites have missing-coverage areas that must be handled via cf_cvg.
- Annual VNL V2 2012 exists in two sets (A and B) with different month spans — choose deliberately.

production:
  raw_sources:
  - name: EOG official product pages (DMSP-OLS v4, VIIRS DNB monthly, VNL annual, FAQ)
    source_type: webpage
    role: Identity, coverage, resolution, file types, license and access requirements for the official composites
    access_route: Direct fetch; pages cached (eog_dmsp.html, eog_vnl.html, eog_faq.html, fetched 2026-08-14)
    url: https://eogdata.mines.edu/products/dmsp/
    coverage: DMSP-OLS 1992-2013; VIIRS DNB 2012- ; VNL V2 2012*-2020 + v2.1 masks through 2021
    last_checked: '2026-08-14'
  - name: TPDC metadata export for PANDA (10.11888/Socioeco.tpdc.271202)
    source_type: dataset
    role: PANDA identity, authors, construction method (NTLSTM), space scope, time frame, filesize, references
    access_route: Official metadata export fetched 2026-08-14
    url: https://data.tpdc.ac.cn/view/export/exportWordMetadata?metadataId=e755f1ba-9cd1-4e43-98ca-cd081b5a0b3e&isChinese=false
    coverage: China, 1984-2020 annual
    last_checked: '2026-08-14'
  - name: Scientific Data pages for harmonized NTL (Li et al. 2020, 7:168) and PANDA (Zhang et al. 2024, 11:414)
    source_type: document
    role: Product identity, method, data-availability pointers
    access_route: Springer page fetched 2026-08-14 (10.1038/s41597-020-0510-y); PANDA paper identity via TPDC metadata and search-index title match (paper page not fetched)
    url: https://link.springer.com/article/10.1038/s41597-020-0510-y
    coverage: 1992-2018 (paper); figshare v10 extends to 2024
    last_checked: '2026-08-14'
  - name: figshare API records 9828827 and 12312125
    source_type: dataset
    role: Actual harmonized NTL file manifest (34 GeoTIFFs, CC BY 4.0, v10) and the separate metadata record
    access_route: figshare API fetched 2026-08-14
    url: https://api.figshare.com/v2/articles/9828827
    coverage: Annual files 1992-2024 (per v10 title)
    last_checked: '2026-08-14'
  acquisition_methods:
  - download
  sample_construction: "No sampling: composites are the complete official products; the researcher's choice is which product family/version and how to aggregate grids."
  pipeline_stages: []
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: Grid cell (30 arc-sec DMSP; 15 arc-sec VIIRS; PANDA/harmonized annual grids)
    structure: Gridded annual (and monthly VIIRS) time series
    geography: Global (EOG, harmonized NTL); China (PANDA)
    time_span: 1992-2024 (per family/version)
    key_variables:
    - DN intensity (DMSP, harmonized)
    - Radiance nW/cm2/sr (VIIRS)
    - Cloud-free coverage counts
    formats:
    - geotiff
  reproducibility:
    level: high
    starting_point: EOG product pages (free account) for official composites; TPDC/figshare for China-corrected versions
    code_available: false
    code_url: ''
    requirements:
    - Free EOG account (human browser for signup)
    - GIS/zonal-statistics skills to aggregate grids to admin units
    blockers:
    - EOG register page 404 for anonymous clients (signup mechanics unverified)
    - Paper-level product identity for RSUE 104246 unresolved (SSRN/ScienceDirect blocked)
  compliance:
    terms_or_license: CC BY 4.0 for many EOG products with EOG citation; figshare harmonized NTL CC BY 4.0; TPDC platform terms
    robots_or_rate_limits: Normal download use; EOG account-based access is the intended channel
    personal_or_sensitive_data: None
    redistribution: Cite EOG / the product papers when redistributing or republishing derived grids
    review_needed: false

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: partial
  last_audited: '2026-09-28'

used_by:
- cite: 'Wang, Yalin & Dong, Xiaofang (2026), Urban Internal Structures and Gender Commuting Gap: Evidence from China, RSUE 120(C)'
  doi: https://doi.org/10.1016/j.regsciurbeco.2026.104246
  journal: RSUE
  year: 2026
  dataset_role: Input for urban subcenter identification ('subcenters identified from nighttime light data')
  evidence_type: publisher-visible article excerpt
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0166046226000566
  data_note: >-
    The publisher-visible article excerpt, checked 2026-09-28, states that the authors use nighttime
    light data obtained from NASA as a proxy for economic density to identify city subcenters for 2015.
    This verifies the data role, provider family and year, but not a product name, version, resolution,
    file, access route, preprocessing, or code. ScienceDirect full text is subscriber-only and the SSRN
    working-paper page is CAPTCHA-blocked in this environment; the exact NTL product remains unresolved.

provenance:
- source: EOG official pages eogdata.mines.edu/products/dmsp/ and /products/vnl/ and /products/faq (fetched and cached 2026-08-14, previous pass; re-read this pass)
  field_scope:
  - identity
  - coverage
  - resolution
  - file types
  - license
  - access (account requirement)
  added: '2026-08-14'
  confidence: high
  verified: true
- source: EOG auth redirect probe eogauth.mines.edu/realms/eog (fetched 2026-08-14)
  field_scope:
  - account-based access
  added: '2026-08-14'
  confidence: high
  verified: true
- source: NOAA NCEI legacy pages (ngdc.noaa.gov/eog/dmsp/downloadV4composites.html, /eog/viirs/download_dnb_composites.html) — 404 both (2026-08-14)
  field_scope:
  - legacy route status (dead)
  added: '2026-08-14'
  confidence: high
  verified: true
- source: TPDC metadata export (10.11888/Socioeco.tpdc.271202) fetched 2026-08-14
  field_scope:
  - PANDA identity, authors, method, coverage, filesize
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Springer page for Li et al. 2020 Scientific Data 7:168 (fetched 2026-08-14) + figshare API 9828827/12312125
  field_scope:
  - harmonized NTL identity, method, resolution, data host, license, file manifest
  added: '2026-08-14'
  confidence: high
  verified: true
- source: https://api.figshare.com/v2/articles/9828827
  field_scope:
  - Current public-delivery check: HTTP 200, dataset title, CC BY 4.0 licence and 34 annual GeoTIFF files
  - Boundary that this is the harmonized product, not proof of the triggering paper's unresolved NASA product/version
  added: '2026-09-28'
  confidence: high
  verified: true
- source: IDEAS/RePEc article page for 10.1016/j.regsciurbeco.2026.104246 (cached 2026-08-14)
  field_scope:
  - paper identity
  - abstract-level NTL use
  added: '2026-08-14'
  confidence: med
  verified: true
- source: "ScienceDirect publisher result for S0166046226000566, checked 2026-09-28 (publisher-visible excerpt; full page itself returned 403 to the reader)"
  field_scope:
  - paper use of NASA nighttime-light data
  - 2015 city-subcenter purpose
  - boundary that product, version, resolution, delivery and processing remain unexposed
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-satellite-pm25
  relation: often-confused-with
- id: era5-land
  relation: complement
- id: china-census
  relation: complement
---

## Positioning in one sentence

This is a ready family of gridded nighttime-light products for China: its directly downloadable anchor is the public CC BY 4.0 figshare harmonized NTL series (1992-2024), alongside EOG DMSP-OLS annual composites 1992-2013 at ~1 km and VIIRS DNB monthly/annual composites 2012- at ~500 m (free account), plus China-specific PANDA 1984-2020 via TPDC. These are standard proxies for long-run urbanization and human-activity intensity, provided the researcher handles intercalibration and documented sensor breaks.

## Select rules

- Use EOG DMSP-OLS v4 annual composites for 1992-2013 ~1 km light-intensity panels; use VIIRS DNB monthly/annual products for 2012+ at ~500 m.
- When the design spans the DMSP-VIIRS break and needs one consistent series without doing your own calibration, choose PANDA (China-only, 1984-2020, TPDC) or the global harmonized NTL (Li et al. 2020, figshare).
- Do not use raw DN values as radiance, do not compare DMSP years without intercalibration, and exclude zero-coverage cells via cf_cvg.
- Do not confuse NTL with china-satellite-pm25: light intensity is not air-pollution exposure, even though both are global grids.

## Get recipe

1. For a direct public long series, download the 34 annual GeoTIFFs from figshare article 9828827 (CC BY 4.0; 1992-2024), subset China and retain the release/version metadata.
2. Register the free EOG account in a human browser only when original DMSP-OLS v4 annual composites (1992-2013) or VIIRS DNB monthly/annual products are needed; the EOG registration page is not verifiable anonymously.
3. Use PANDA from TPDC (DOI 10.11888/Socioeco.tpdc.271202) when its China-specific 1984-2020 construction, rather than the global harmonized series, is the intended measurement product.
4. Aggregate grids to your admin units with zonal statistics, record the intercalibration/masking choices, and validate against cf_cvg coverage.

## Connections and Limitations

Joins to surveys, censuses and yearbooks run through zonal aggregation of grids to counties/cities, so boundary shapefiles and admin-code vintages are required; the grids carry no administrative identifiers. Measurement breaks to handle: DMSP DN saturation and lack of onboard calibration; the VIIRS 2017-01-12 calibration shift; the VNL V2 2012 double set; and monthly missing-coverage areas. The ready recommendation rests on the independently accessible harmonized NTL release, not on a claim that the triggering paper’s exact NTL product is identified or that EOG signup mechanics are known.
