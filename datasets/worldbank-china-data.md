---
schema_version: 3
catalog_status: ready
id: worldbank-china-data
name: World Bank WDI - China country indicators
aka:
- WDI China
- World Development Indicators China
- World Bank Open Data China
- data.worldbank.org China
provider: >-
  The World Bank Group, World Development Indicators (WDI) database,
  data.worldbank.org. Verified 2026-08-15: country page
  (data.worldbank.org/country/china, fetched 200, ~2MB indicator list read),
  CSV/XML download links via api.worldbank.org, and indicator metadata
  carrying License_Type CC BY-4.0 (datacatalog.worldbank.org/int/
  public-licenses#cc-by). API probe (api.worldbank.org/v2/country/CHN) 200.
china_related: true
domains:
- macro
- development
- international
- public

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    WDI country indicators for China: national-level macro and development
    series (GDP, growth, trade, poverty, health, education, environment,
    etc.) downloadable as CSV/XML (api.worldbank.org/v2/en/country/CHN?
    downloadformat=csv|xml) or via the API; bulk WDI files available through
    the data catalog. License per indicator metadata: CC BY-4.0.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    WDI is the World Bank's flagship cross-country development database;
    China coverage is national-level indicators. Verified 2026-08-15: the
    China country page (200) exposes CSV/XML downloads and per-indicator
    CC BY-4.0 license metadata; the API responds. China-specific granularity
    is national only - for subnational series the china-stat-yearbook family
    dominates.
  barrier: >-
    National-level only for China; indicator definitions and revisions are
    Bank-managed; bulk-catalog file layout not verified this round.
  last_checked: '2026-09-28'

unit_of_observation: Country-year (China national series) per indicator
structure: country-indicator-year panel
geo_granularity:
- national (China)
geography: China (national); cross-country comparisons supported
time_span:
  start: null
  end: null
  last_confirmed_release: null
  coverage_note: >-
    Indicator-specific start years (some series begin in the 1960s); the
    exact China series start/end per indicator not audited this round.
  last_checked: '2026-08-15'
frequency:
- annual (most indicators; some quarterly/monthly series exist in WDI - not audited)
sample_size: >-
  Indicator-specific. The current tested GDP (current US$) endpoint reports 66
  China annual observations; other WDI indicators have their own time coverage
  and missingness, which must be inspected at retrieval rather than inferred
  from this example.
key_variables:
- National macro/development indicators (GDP and components, growth, trade, fiscal, monetary)
- Poverty, inequality, health, education, labor, environment series (indicator list on the China page)
- Metadata: indicator definitions, source, limitations, license (CC BY-4.0)

research_fit:
  best_for:
  - Cross-country panel regressions including China at national level
  - Standard, internationally comparable national development indicators
    with documented definitions and free bulk access
  choose_over:
  - Choose WDI when cross-country comparability and free CC BY-4.0 access
    matter; choose china-stat-yearbook / CEIC for China-subnational series.
  not_good_for:
  - Subnational (province/city) China series - national only
  - China-specific survey or firm microdata
  - Latest China data where NBS monthly releases are faster (WDI lags)
  needs_join_for:
  - Subnational China variables (china-stat-yearbook family)
  - Micro-level outcomes (surveys, firm data)
  variation_available:
  - Time-series variation per indicator; cross-country variation
  topics:
  - development indicators
  - macro statistics
  - cross-country comparison
  - World Bank

good_for:
- cross-country panels
- national development indicators
identification:
- WDI is a descriptive country-indicator-year source, not an identification design; any causal use needs a separately justified design and comparison.
linkable_keys:
- Country code (CHN)
- Indicator code
- Year

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - year
  method: combine WDI national series with subnational yearbook series by year (different units/geography - national vs subnational)
  evidence_status: plausible

access_routes:
- route: World Bank Open Data country page + downloads
  access_status: available
  direct_url: https://data.worldbank.org/country/china
  requirements: none
  steps:
  - Open the China country page; select indicators or use the CSV/XML download links (api.worldbank.org/v2/en/country/CHN?downloadformat=csv|xml).
  - For the full WDI bulk set, use the data catalog bulk files (datacatalog.worldbank.org; layout not verified this round).
  deliverable: WDI China indicator series (CSV/XML/JSON); CC BY-4.0
  cost: free
  last_checked: '2026-09-28'
  caveat: 'bulk-catalog file layout unverified; per-indicator coverage years to be checked at download'
- route: World Bank API
  access_status: available
  direct_url: https://api.worldbank.org/v2/country/CHN
  requirements: none
  steps:
  - Query indicators via api.worldbank.org/v2/country/CHN/indicator/... (probe 200).
  deliverable: JSON/XML indicator series
  cost: free
  last_checked: '2026-09-28'
  caveat: API limits/terms per World Bank Open Data rules

access:
  url: https://data.worldbank.org/country/china
  cost: free
  license: CC BY-4.0 per indicator metadata (License_URL datacatalog.worldbank.org/int/public-licenses#cc-by)
  format:
  - CSV
  - XML
  - JSON (API)
  api: true
  how_to_get: Download from the country page or query the API; attribution per CC BY-4.0.
caveats:
- National-level only for China.
- The general worldbank.org terms page (fetched) covers website content; the dataset license is the CC BY-4.0 noted in indicator metadata.
- Indicator revisions and vintage changes are Bank-managed; download dates matter for reproducibility.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: needs-verification
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://api.worldbank.org/v2/country/CHN/indicator/NY.GDP.MKTP.CD?format=json&per_page=5
  field_scope:
  - current anonymous API delivery of a concrete China country-indicator series
  - returned country, indicator, year, and value fields
  - current example coverage includes 2025, 2024, and 2023 values; each indicator has its own availability
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://api.worldbank.org/v2/indicator/NY.GDP.MKTP.CD?format=json
  field_scope:
  - indicator identity and World Development Indicators source metadata for the tested delivery route
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://data.worldbank.org/country/china (fetched 200, ~2MB, read 2026-08-15)
  field_scope:
  - country page identity and indicator list
  - CSV/XML download links (api.worldbank.org)
  - per-indicator License_Type CC BY-4.0 and license URL
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.worldbank.org/v2/country/CHN?format=json (probe, 200, 2026-08-15)
  field_scope:
  - API availability and China record
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets (fetched 200, redirected to worldbank.org/ext/en/legal/terms-conditions, 2026-08-15)
  field_scope:
  - general website terms (limited license with attribution)
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

WDI gives free, CC BY-4.0, national-level development indicators for China (CSV/XML/API) - the standard cross-country layer; it is national-only, so subnational China research needs the china-stat-yearbook family.

## Select rules

- Use WDI for cross-country panels and standard national indicators.
- Use china-stat-yearbook/CEIC for province/city-level China series.
- For faster, official China macro updates use NBS monthly releases.

## Get recipe

1. Open the China country page and select indicators, or use the CSV/XML download links.
2. For bulk use, fetch the WDI bulk files from the data catalog (layout unverified).
3. Keep the download date for reproducibility (Bank-managed revisions).

## Connections and Limitations

National-level only; subnational needs the yearbook family. Indicator definitions are Bank-managed; the dataset license (CC BY-4.0) is recorded in indicator metadata, while the general website terms cover the site itself.

## Decision sufficiency check

A researcher can now download WDI China series with license clarity and knows the national-only boundary - grounding is appropriate (bulk-file layout is the only mechanical unknown).
