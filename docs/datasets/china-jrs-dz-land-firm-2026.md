---
schema_version: 3
catalog_status: grounding
id: china-jrs-dz-land-firm-2026
name: Mei & Xi (2026 JRS) DZ-Land-Firm spatial dataset
aka:
- Development Zone, Land Lease Price, and Firm Productivity data
- DZ-Land-Firm
- 中国开发区—土地—企业空间数据
provider: Lin Mei and Qiangmin Xi; paper-specific constructed research asset; upstream providers are not identified in the checked public sources
china_related: true
domains:
- urban
- regional
- land
- firm
- development
- spatial

data_pathway:
  mode: inaccessible
  origin: researcher-constructed
  target_artifact: >-
    A paper-specific matched spatial dataset linking development-zone locations or
    boundaries, land-lease/parcel observations, and firm observations, described by the
    authors as the “DZ-Land-Firm” spatial data set and constructed with spatial
    positioning technology and overlay analysis.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    The 2026 Journal of Regional Science article confirms that its China study combines
    development-zone, land, and firm microdata. The authors' working-paper description
    gives the constructed asset a distinct name and explains the spatial positioning and
    overlay step. A 2026 official Tianjin University of Finance and Economics release
    further identifies the output as a block-level (区块层面) DZ--land--firm
    micro-spatial dataset. Public materials do not expose a file, code repository, exact
    raw providers, or a routine access application, so this is a grounded identity and
    routing warning rather than a reproducible download recommendation.
  barrier: >-
    The checked sources leave the land-transaction product, development-zone boundary
    vintage, firm database, study years, spatial unit, identifiers, matching files,
    cleaning code, price, and redistribution conditions unresolved. Documentation or an
    author-provided package is needed before claiming the asset can be rebuilt or joined
    to ASIF or the general land-transaction record.

unit_of_observation: >-
  Spatial block-level matched development-zone, land-lease/parcel, and firm
  microdata observation; the official release establishes the block-level output,
  but not the exact parcel-to-firm row relation.
structure: Researcher-constructed block-level spatial matched records; panel or cross-section structure remains to be verified
geo_granularity:
  - spatial block
  - development zone
  - land parcel or land-lease record
  - firm
  - city or surrounding boundary where retained
geography: China; exact cities, zones, boundary vintage, and sample frame are not established by the checked public sources
time_span:
  start: unknown
  end: unknown
  last_confirmed_release: '2026-04-27'
  coverage_note: >-
    The Wiley page first published the JRS article on 27 April 2026. Neither the
    publisher abstract nor the public working-paper description gives the final asset's
    study years; any years in a later author package must be recorded with its version.
  last_checked: '2026-08-13'
frequency:
- unknown; likely transaction/firm observation with spatial matching, to be verified
sample_size: Not disclosed in the checked public sources
key_variables:
- Development-zone membership, boundary, or distance fields where retained
- Land-lease price and parcel characteristics
- Firm productivity, entry, or firm-level characteristics
- Spatial coordinates or geocoded locations used for positioning/overlay
- City, administrative, or zone identifiers if supplied

research_fit:
  best_for:
  - Research needing the paper's linked spatial relationship among development zones, industrial land leases, and firms
  - Urban/regional studies of land-lease prices and firm productivity where a boundary-aware matched asset is essential
  - Reproducing or extending the 2026 JRS paper after its source and construction details are obtained
  choose_over:
  - Choose this asset over china-land-transaction only when the question needs its zone-to-land-to-firm overlay and can tolerate restricted access.
  - Choose china-land-transaction for a documented collection route to land-transfer announcements or a broader parcel panel; it does not automatically supply the DZ-Land-Firm linkage.
  - Choose ASIF for a known industrial-firm panel, but do not assume that the paper's firm source is ASIF until author documentation says so.
  not_good_for:
  - A public national development-zone boundary database, current land-market panel, or general firm-productivity panel
  - Estimating new zone effects without verifying boundary vintage, spatial sample, and firm/land matching rules
  - Treating the development-zone policy or boundary-discontinuity design as a variation record in this catalog
  needs_join_for:
  - A verified city-year economic panel and boundary concordance
  - Firm financial or production outcomes if the delivered package does not include them
  - A separately documented land source or development-zone registry if authors release only derived matches
  variation_available:
  - Zone membership, distances, land prices, and firm outcomes are data dimensions; the policy assignment and boundary-discontinuity design are not recorded as canonical variation here.
  topics:
  - development zones
  - industrial land
  - land lease prices
  - firm productivity
  - spatial matching
  - place-based urban development

good_for:
- Boundary-aware development-zone and industrial-land research if the source package is obtained
- Connecting land prices to firm outcomes through an explicitly documented spatial overlay
- Checking whether the paper's linked land/firm object is available before an independent reconstruction
identification: []
linkable_keys:
- Development-zone identifier or polygon
- Land parcel/lease identifier
- Firm identifier or normalized name
- Coordinates or geocoded location
- City/county code and year where supplied

joins:
- target: china-land-transaction
  relation: often-confused-with
  keys:
  - Parcel or lease identifier
  - City/county code
  - Transaction/lease year
  method: Compare the author-supplied land source, parcel definitions, and boundary vintage before joining; public land announcements are not evidence of the paper's linked file.
  evidence_status: plausible
- target: asif
  relation: complement
  keys:
  - Firm identifier or normalized name
  - City/county code
  - Industry and year
  method: Attempt a firm join only after the paper package identifies its firm source and identifier; ASIF coverage and cleaning differ from any unknown firm input.
  evidence_status: plausible
- target: china-stat-yearbook
  relation: complement
  keys:
  - City code or normalized city name
  - Year
  method: Add city-level controls after confirming the paper's spatial unit and administrative-boundary vintage.
  evidence_status: plausible

access_routes:
- route: paper and author documentation request
  access_status: needs-verification
  direct_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
  requirements:
  - Read the final article and any supporting information
  - Contact the corresponding author with a precise data request
  - Ask for the DZ-Land-Firm file, raw-source descriptions, boundary version, dictionary, code, and terms
  steps:
  - Record the final article DOI and publication version.
  - Request the exact data and code used for the land-price and firm-productivity analyses.
  - Ask separately whether raw land, development-zone polygons, and firm inputs may be shared or only derived matches.
  - Preserve the response, file list, version dates, and no-redistribution conditions.
  deliverable: Author-provided documentation or a paper-specific data/code package if approved; no public file is established by the checked page.
  cost: by-application
  last_checked: '2026-08-13'
  caveat: The publisher page confirms data roles but does not state a public repository or guarantee an author request will be fulfilled.
- route: SSRN working-paper description
  access_status: documentation-only
  direct_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4029422
  requirements: Web access to the working-paper record; the abstract is not a data download
  steps:
  - Read the abstract to understand the named DZ-Land-Firm object and spatial construction.
  - Use it to formulate a source request, not to infer fields, years, or access.
  deliverable: Working-paper description of the constructed asset; no underlying file or code is confirmed.
  cost: free
  last_checked: '2026-08-13'
  caveat: The working-paper version predates the 2026 JRS publication and may not have identical coverage or construction.

access:
  url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
  cost: by-application
  license: Article terms are separate from the paper-specific data; no redistribution license for the DZ-Land-Firm asset is established.
  format:
  - unknown
  api: false
  how_to_get: Start with the final article and SSRN description, then request data/code and source documentation; do not substitute a commercial or public land product without an identity check.

caveats:
- “DZ-Land-Firm” and “spatial positioning/overlay analysis” identify a constructed research object, not a provider or public product.
- The raw land, zone, and firm sources may be public, commercial, administrative, or author-collected; the checked sources do not decide among them.
- The output is described as block-level, but final study years, cities, zone list, parcel fields, firm identifiers, block definition, matching tolerance, and sample restrictions remain unknown.
- The general land-transaction and ASIF records are complements or alternatives, not silent replacements for this paper-specific asset.

production:
  raw_sources:
  - name: Development-zone microdata or spatial boundaries
    source_type: dataset
    role: Identify zone membership, boundary, or location for the paper's spatial comparison
    access_route: Paper-specific source not identified; request from authors
    url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
    coverage: China development zones; exact zone universe and boundary vintage are unknown
    last_checked: '2026-08-13'
  - name: Industrial land-lease or parcel microdata
    source_type: dataset
    role: Land-lease price and parcel observations linked to development zones and firms
    access_route: Paper-specific source not identified; request from authors
    url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
    coverage: China land observations; exact years, cities, provider, and fields are unknown
    last_checked: '2026-08-13'
  - name: Firm microdata
    source_type: dataset
    role: Firm entry/productivity outcomes linked through the spatial data set
    access_route: Paper-specific source not identified; request from authors
    url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
    coverage: China firms in the paper's sample; exact database, years, and identifiers are unknown
    last_checked: '2026-08-13'
  acquisition_methods:
  - author-request documentation or data delivery
  - spatial positioning as described by the authors
  - overlay analysis as described by the authors
  sample_construction: >-
    The authors combine development-zone, land, and firm microdata and describe a
    DZ-Land-Firm data set produced through positioning and overlay. Public sources do
    not establish raw files, sampling frame, exclusions, boundary version, or matching
    tolerance; these remain open until documentation is obtained.
  pipeline_stages:
  - stage: collect
    inputs:
    - Development-zone data or boundaries
    - Land-lease/parcel microdata
    - Firm microdata
    method: Combine the three named classes of microdata; exact providers and acquisition methods are not disclosed in the checked sources.
    output: Source-level inputs for the paper-specific spatial data set
    evidence: 2026 JRS publisher abstract
  - stage: geocode
    inputs:
    - Development-zone locations or polygons
    - Land parcels/leases
    - Firm locations
    method: Apply spatial positioning technology as described in the authors' working-paper abstract; coordinate system, geocoder, and tolerance are unknown.
    output: Spatially positioned zone, land, and firm objects
    evidence: SSRN working-paper abstract for 4029422
  - stage: match
    inputs:
    - Spatially positioned zone, land, and firm objects
    method: Use spatial overlay analysis to construct the named DZ-Land-Firm object; exact overlay rules and boundary handling are unknown.
    output: Matched spatial data set used for land-price and firm-productivity analysis
    evidence: SSRN working-paper abstract for 4029422
  output:
    unit_of_observation: Matched zone, land, and firm records; exact row grain unknown
    structure: Spatial matched data set; panel/cross-section status unknown
    geography: China; exact cities and zones unknown
    time_span: Unknown until author documentation is obtained
    key_variables:
    - Zone membership or boundary
    - Land-lease price and parcel attributes
    - Firm productivity/entry fields
    - Spatial coordinates and identifiers where retained
    formats:
    - unknown
  reproducibility:
    level: needs-verification
    starting_point: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
    code_available: false
    requirements:
    - Author response or an approved paper-specific file/code package
    - Source-specific access for omitted land, zone, or firm inputs
    - GIS/spatial software matching the authors' construction if a rebuild is attempted
    - Boundary and identifier documentation
    blockers:
    - No public data repository or code route was identified.
    - Raw providers, years, spatial units, identifiers, overlay tolerance, and cleaning rules are unresolved.
    - A commercial land source or ASIF extract cannot be assumed equivalent without author evidence.
  compliance:
    terms_or_license: Check the author response and each upstream provider's terms; no paper-specific data license is inferred.
    robots_or_rate_limits: Do not scrape Wiley, SSRN, commercial land platforms, or firm databases to recreate undocumented inputs.
    personal_or_sensitive_data: Review firm identifiers, addresses, or coordinates before use or sharing.
    redistribution: Do not redistribute author-provided or source-provider files without written permission.
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-13'

used_by:
- cite: 'Mei & Xi (2026), Impact of Place-Based Policy on Land Lease Price and Its Productivity Premium: Evidence From China''s Development Zone Program'
  doi: https://doi.org/10.1111/jors.70064
  journal: Journal of Regional Science
  year: 2026
  dataset_role: Main paper-specific spatial data linking development zones, industrial land-lease prices, and firm productivity
  evidence_type: publisher-abstract-and-working-paper
  evidence_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
  data_note: >-
    The final Wiley abstract says the study combines development-zone, land, and firm
    microdata in China. The authors' SSRN working-paper abstract names the “DZ-Land-Firm”
    spatial data set and says it is constructed with spatial positioning technology and
    overlay analysis. A 2026 official university release describes the resulting asset as
    block-level micro-spatial data. Neither source establishes a public file, raw providers,
    exact coverage, or an author-request outcome.

provenance:
- source: https://onlinelibrary.wiley.com/doi/10.1111/jors.70064
  field_scope:
  - final paper identity, authors, DOI, and first-publication date
  - China development-zone, land, and firm microdata roles
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4029422
  field_scope:
  - predecessor working-paper identity
  - DZ-Land-Firm name
  - spatial positioning and overlay-analysis construction description
  - development-zone, land-lease-price, and firm-productivity roles
  added: '2026-08-13'
  confidence: high
  verified: true
- source: https://csgg.tjufe.edu.cn/info/1037/1350.htm (Tianjin University of Finance and Economics official school release, read 2026-09-28)
  field_scope:
  - block-level output identity (区块层面开发区--宗地--企业微观空间数据集)
  - confirmation that the output combines development zones, parcels, and firms
  - boundary that the announcement does not document inputs, block construction, coverage, access, code, or terms
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://www.sciencedirect.com/science/article/pii/S0264837722002083
  field_scope:
  - related development-zone land-transfer literature and possible discovery context only
  - not proof of the 2026 paper's raw provider or file equivalence
  added: '2026-08-13'
  confidence: med
  verified: true

related_datasets:
- id: china-land-transaction
  relation: often-confused-with
- id: asif
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

This is a very recent (2026) paper-specific spatial asset linking Chinese development zones, land leases, and firm outcomes through positioning and overlay, but the public record exposes only identity and construction. Treat it as a restricted author-documentation lead rather than a public land or firm database.

## Select rules

- Prioritize it when the question needs the paper's zone–land–firm overlay and a controlled author request is realistic.
- Switch to china-land-transaction when a documented public collection/reconstruction route matters more than exact paper replication.
- Use ASIF or another firm panel only after confirming that the paper's firm input is compatible; do not infer this from the word “firm.”

## Get recipe

Read the final Wiley article and the authors' SSRN description, then ask the corresponding author for the exact DZ-Land-Firm file, source list, boundary version, spatial identifiers, matching code, and terms. Preserve the response and file manifest. If the package is unavailable, document the missing component and build any substitute from its own verified source rather than calling it the paper's data.

## Connections and Limitations

The decisive future join is spatial: zones, parcels, firms, and city boundaries must share a documented coordinate system and vintage. A city-level land table or ASIF panel cannot substitute for the overlay object without changing the asset. The current record preserves the strongest confirmed construction facts while making every unverified source and access assumption visible.
