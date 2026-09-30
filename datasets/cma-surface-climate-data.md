---
schema_version: 3
catalog_status: grounding
id: cma-surface-climate-data
name: China Meteorological Data Service Center surface climate observations (中国气象数据网 地面气象观测数据)
aka:
- 中国气象数据网
- data.cma.cn
- 中国地面气象观测数据
- 中国地面气候资料日值数据集 V3.0 (commonly cited family member; product page unverified)
- China Meteorological Administration surface station data
- NMIC surface observations
provider: >-
  国家气象信息中心 (National Meteorological Information Center, NMIC), the
  data-service arm of the China Meteorological Administration (CMA), operating
  the 中国气象数据网 (China Meteorological Data Service Center) at data.cma.cn.
  Verified from the official home page title and content (fetched 2026-08-15):
  "国家气象信息中心-中国气象数据网", with a product catalog including 地面气象资料
  (surface), 高空气象资料 (upper air), 海洋气象资料, 大气成分资料, 辐射资料, 农气资料,
  数值预报, 天气雷达资料, 风云气象卫星 and more.
china_related: true
domains:
- environment
- climate
- weather
- agriculture
- health
- labor
- urban

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Choose a named CMA surface product rather than treating the platform as one
    uniform panel. The verified historical choices are the monthly
    international-exchange-station series (A.0019.0001.S001, SURF_CHN_MUL_MON)
    and annual counterpart (A.0019.0001.S002, SURF_CHN_MUL_YER). They deliver
    station-by-period observations. The similarly named A.0012.0001.S011 is a
    different rolling near-real-time product, not a historical-series substitute.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Provider-first grounding (2026-09-28): official product pages identify the
    monthly and annual historical products as data from Chinese international
    exchange meteorological stations, supplied by NMIC and open to real-name
    education/research users. The monthly page reports 1995-01 through
    2026-07 and monthly updating; the annual page reports a 1995 start and
    annual updating. A separate S011 page is a daily-updated international
    exchange-station product limited to the most recent seven days and lagged
    two days. The pages do not establish file format, full station roster,
    price, terms, or paper-specific use.
  barrier: >-
    Real-name education/research registration is required for the verified
    historical products. The data-use agreement, file format, full station
    roster, price or quota, and paper-specific use remain unverified; check
    these in the logged-in product flow before committing to a design.

unit_of_observation: >-
  International-exchange meteorological station x month or year for the two
  verified historical products. Aggregation to a city or county is a researcher step.
structure: panel (station-month or station-year; named product dependent)
geo_granularity:
- international-exchange meteorological station
geography: >-
  Chinese international-exchange meteorological stations. The reviewed pages
  do not provide a complete roster, so this record does not infer mainland
  completeness or national basic/benchmark-station coverage.
time_span:
  start: '1995-01 for monthly A.0019.0001.S001; 1995 for annual A.0019.0001.S002'
  end: '2026-07 on the monthly page; annual page reports current coverage without an exact end date'
  last_confirmed_release: 'Monthly historical page reported coverage through 2026-07, checked 2026-09-28'
  coverage_note: >-
    These bounds apply only to the two named historical international-exchange
    station products. They do not establish coverage for the commonly cited
    daily V3.0 family, whose current product page remains unverified. S011 is
    a separate short rolling product and must not be used to fill historical gaps.
  last_checked: '2026-09-28'
frequency:
- monthly (A.0019.0001.S001)
- annual (A.0019.0001.S002)
- daily update of a rolling near-seven-day product (A.0012.0001.S011; not a historical panel)
sample_size: unknown
key_variables:
- Surface air temperature (station observations)
- Precipitation
- Wind speed/direction
- Relative humidity
- Weather phenomena and monthly day-count fields (product-dependent)
- Station identifier and coordinate documentation is not verified on the reviewed public pages

research_fit:
  best_for:
  - Station-level weather exposure for climate-health, climate-labor, agriculture and energy studies on Chinese stations (temperature, precipitation, wind)
  - Official Chinese international-exchange-station data when the design needs observed CMA stations rather than a reanalysis grid
  choose_over:
  - Choose the official CMA station data over era5-land when the design needs station-observed values (or specific stations) rather than a modeled reanalysis grid.
  - Choose era5-land for continuous gridded surfaces, global coverage, or long seamless series without station access.
  - For air pollution research, join CMA weather to china-air-quality-monitoring stations rather than substituting one for the other.
  not_good_for:
  - Continuous gridded climate surfaces (use era5-land)
  - Nationwide station completeness, daily historical coverage, or a particular station roster not confirmed in the logged-in product metadata
  - Real-time high-frequency feeds: the reviewed S011 page is a short rolling window, not an archive
  - Station data do not give population-weighted exposure without an aggregation step
  needs_join_for:
  - Admin boundaries or other outcomes: first confirm that the selected download supplies usable station identity or coordinates
  variation_available:
  - Monthly or annual observations across the included international-exchange stations; the public pages do not establish a full station roster or daily historical series
  topics:
  - weather
  - climate
  - temperature
  - precipitation
  - station data
  - China Meteorological Administration

good_for:
- weather exposure measures
- climate-economy studies
- agricultural weather controls
- station-to-observation matching
identification: []
linkable_keys:
- Time period; station-code and coordinate fields must be verified in the selected download

joins:
- target: era5-land
  relation: complement
  keys:
  - location
  - time
  method: station observations vs reanalysis grid comparison/validation
  evidence_status: plausible
- target: china-air-quality-monitoring
  relation: complement
  keys:
  - time
  - station identity or coordinates after confirming the CMA download metadata
  method: Weather controls require an evidenced station identity or spatial crosswalk; neither is supplied by the reviewed public landing pages.
  evidence_status: plausible

access_routes:
- route: official-registration-download
  access_status: available-with-registration
  direct_url: https://data.cma.cn/
  requirements: Real-name education/research account for the verified monthly and annual historical products
  steps:
  - Open the named historical product page: A.0019.0001.S001 (monthly) or A.0019.0001.S002 (annual).
  - Complete real-name education/research registration and inspect the logged-in download flow for the intended station, time and format.
  - Read the applicable data-use agreement and confirm price/quota before ordering or downloading.
  deliverable: >-
    A provider-delivered station-by-month or station-by-year historical file,
    subject to confirmation of the logged-in selection and format.
  cost: registration
  last_checked: '2026-09-28'
  caveat: >-
    The two pages still returned 200 to an ordinary public retrieval on
    2026-09-28 and explicitly display the real-name education/research access
    level. They do not expose an automated proof of the final cart, download
    format, full station roster, terms or price. Do not claim S011 supplies the
    historical products.

access:
  url: https://data.cma.cn/
  cost: needs-verification
  license: Official data-use agreement (气象数据使用协议) applies; details unread this round
  format:
  - needs-verification
  api: false
  how_to_get: Register as an education/research user, select the named monthly or annual historical product, then verify the logged-in cart, format, terms and price before download.
caveats: >-
  The historical monthly/annual series are confined here to Chinese
  international exchange stations and the stated 1995-era coverage. The
  commonly cited daily V3.0 family still has no verified current product page.
  Station counts, downloadable station metadata, file formats, price/quota and
  data-use terms require confirmation in the logged-in product flow. Do not
  assume a free tier or use the short S011 rolling feed as a historical substitute.

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: needs-verification
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://data.cma.cn/ (home page, fetched 2026-08-15)
  field_scope:
  - provider
  - platform
  - product_categories
  - access_tiers
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://data.cma.cn/data/detail/dataCode/A.0012.0001.S011.html (product page, fetched 2026-08-15)
  field_scope:
  - product_family
  - product_names
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://data.cma.cn/data/detail/dataCode/A.0019.0001.S001.html (official monthly historical product page, read 2026-09-28)
  field_scope:
  - named monthly product identity
  - international-exchange-station geography
  - 1995-01 to 2026-07 coverage stated on page
  - weather-element list
  - monthly update
  - real-name education/research user access condition
  - NMIC production source
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://data.cma.cn/data/detail/dataCode/A.0019.0001.S002.html (official annual historical product page, read 2026-09-28)
  field_scope:
  - named annual product identity
  - 1995 start stated on page
  - annual update
  - real-name education/research user access condition
  - NMIC production source
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Direct public retrieval of A.0019.0001.S001 and A.0019.0001.S002 product pages (HTTP 200, inspected 2026-09-28)
  field_scope:
  - current reachability of both named historical product pages
  - visible education/research real-name access condition
  - negative boundary: public static pages did not expose a final download cart, file format, full roster, price or agreement terms
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://data.cma.cn/data/cdcindex/cid/f0fb4b55508804ca.html (surface category page, fetched 2026-08-15; JS shell)
  field_scope:
  - product_family
  added: '2026-08-15'
  confidence: med
  verified: false
- source: >-
    Direct public retrieval on 2026-09-28 of the legacy daily V3.0 product
    paths: https://m.data.cma.cn/data/detail/dataCode/SURF_CLI_CHN_MUL_DAY_V3.0.html,
    https://data.cma.cn/data/detail/dataCode/SURF_CLI_CHN_MUL_DAY_V3.0.html,
    and https://data.cma.cn/data/cdcdetail/dataCode/SURF_CLI_CHN_MUL_DAY_V3.0.html
  field_scope:
  - All three legacy detail URLs returned HTTP 404 in this public retrieval
  - Search-index descriptions of the old daily V3.0 product do not establish a current acquisition route
  - This result does not establish product withdrawal or absence from the logged-in catalogue
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: era5-land
  relation: complement
- id: china-air-quality-monitoring
  relation: complement
---

## Positioning in one sentence

The CMA/NMIC 中国气象数据网 provides named, registration-gated surface-station products; for the verified historical route, select its 1995-era monthly or annual international-exchange-station series rather than the separate short rolling S011 feed. It is complementary to the era5-land reanalysis grid, but the final file, station roster and terms must still be confirmed after login.

## Select rules

- Prioritize the named historical product for monthly or annual station weather exposure or controls when the research design can use its international-exchange-station coverage.
- Switch to era5-land for continuous gridded surfaces, global coverage, or long seamless series without registration-dependent products.
- Do not treat the short S011 feed as a historical series. For a pollution-weather design, do not assume a station join until the selected download's station identifiers or coordinates are verified.

## Get recipe

1. Decide whether the intended timing is monthly (A.0019.0001.S001) or annual (A.0019.0001.S002); neither is the short rolling S011 product.
2. Open its product page and complete the required real-name education/research registration.
3. In the logged-in flow, confirm that the required station, period, field list, format, price/quota and data-use terms are available.
4. Download only after those details support the intended design; preserve product code and access date with the resulting file.

## Connections and Limitations

- The two named historical product pages now give their core timing, geography, elements and registration condition; their complete station roster and delivered file metadata remain unknown until the logged-in flow is inspected.
- The widely cited 中国地面气候资料日值数据集 V3.0 is not established by this record: its current product page is unverified, not necessarily unavailable.
- The legacy daily V3.0 detail URLs on both the mobile and desktop official sites returned HTTP 404 in a public check on 2026-09-28. Search still exposes an old provider description, but it is a discovery lead rather than a current download route. Next inspect the current named-product catalogue or ask NMIC for the replacement product code and applicable access conditions; repeating these legacy URLs cannot settle delivery, station coverage or terms.
- Any aggregation to administrative units, nearest-station match, or population-weighted exposure is a further researcher step. It needs verified station metadata and a stated crosswalk.
- Price/quota and the data-use agreement are not established for the two historical products. Do not infer them from platform-level PLUS language.
