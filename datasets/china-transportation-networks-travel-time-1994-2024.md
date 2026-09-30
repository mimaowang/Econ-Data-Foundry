---
schema_version: 3
catalog_status: ready
id: china-transportation-networks-travel-time-1994-2024
name: China Transportation Networks dataset - prefecture-pair road/rail travel times 1994-2024 (Lin Ma release; related paper Ma & Tang 2024 JIE)
aka:
- 中国交通网络数据
- Transportation Networks of China
- prefecture travel time China
- Ma-Tang transport networks
provider: >-
  Released by Lin Ma (Singapore Management University) on his personal website
  (Data page) and GitHub (malin84/transportation_networks_of_china). The
  related paper is Ma & Tang (2024 JIE, "The Distributional Impacts of
  Transportation Networks in China", DOI 10.1016/j.jinteco.2023.103873), whose
  transport-network construction this dataset formalizes. Author-side release,
  not an official government product.
china_related: true
domains:
- transportation
- urban
- trade
- spatial-equilibrium

data_pathway:
  mode: direct
  origin: researcher-constructed
  target_artifact: >-
    Downloadable dataset with three components (per the author's Data page):
    1) prefecture-to-prefecture travel time on road and railroad from 1994 to
    2024; 2) years of construction and design codes (road/rail engineering
    standard revisions); 3) pixel-level design speed and trespassing time.
    Distributed as a public GitHub repository under its displayed GPL-3.0
    repository license.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    Grounding-b16 (2026-08-15): third-priority completion for the
    china-interregional-trade-flows candidate. The Ma & Tang (2024 JIE) paper
    is a QUANTITATIVE SPATIAL MODEL - it uses NO observed interregional
    trade-flow dataset (bilateral trade flows are model objects); its economic
    inputs are the 2005 One Percent Population Survey (prefecture-pair
    population flows), the Customs Transaction Dataset 2000-2005 (trade
    elasticity), and City Statistical Yearbooks (traffic volume by mode) per
    the author-hosted final working paper (lin-ma.com, read in full,
    Appendix B.4). The paper's transport-network construction (digital maps +
    MOT Technical Standard of Highway Engineering design-speed revisions,
    1988/1997/2003/2014) IS released by the author: "Transportation Networks of
    China" dataset on GitHub (API record read 2026-08-15: description
    "Datasets that cover the road and rail transportation networks in China",
    license GPL-3.0, ~1.7 GB, active) plus the author's Data page listing the
    three components and a Latest Release link. Related-paper link: Ma & Tang
    2024 JIE. The public README checked 2026-09-27 closes the package-level
    description: Version 2.0 has documented files, 279 prefectures, 1994-2024
    coverage, variables, and Dijkstra sample code. Version correspondence with
    the paper's earlier T_ijt matrix remains a separate question.
  barrier: >-
    The public repository has no documented access barrier. Pixel-level files
    and custom routing require suitable local storage and computing tools;
    Version 2.0 should not be casually substituted when an exact paper-era
    matrix is required.

unit_of_observation: prefecture-pair (travel time by road and railroad); pixel (design speed and trespassing time); construction-year records (road/rail segments)
structure: panel of prefecture-pair travel times over years 1994-2024, plus cross-section/pixel files
geo_granularity:
- prefecture pair (road and railroad travel time)
- pixel level (design speed, trespassing time)
geography: China, prefecture-level (mainland); road and railroad networks
time_span:
  start: '1994'
  end: '2024'
  last_confirmed_release: 'Version 2.0 README checked 2026-09-27; it covers 1994-2024 and extends Version 1.0 (1994-2017).'
  coverage_note: >-
    Version 2.0 documents 1994-2024 and adds 2018-2024 infrastructure while
    correcting some earlier segments. The related paper's analysis spans
    1995-2016, so exact correspondence still needs a version-specific check.
  last_checked: '2026-09-27'
frequency:
- annual (travel time panel 1994-2024)
sample_size: >-
  The prefecture-pair component covers 279 prefectures. Each of its three
  mode-specific CSVs has 38,781 lower-triangle origin-destination rows and
  annual columns for 1994-2024; pixel and segment components are separate.
key_variables:
- Prefecture-to-prefecture travel time on road (1994-2024)
- Prefecture-to-prefecture travel time on railroad (1994-2024)
- Years of construction and design codes (road/rail)
- Pixel-level design speed and trespassing time
- City four-digit division code, coordinates, census population, and city class (cityinfo.csv)

research_fit:
  best_for:
  - Prefecture-pair travel-time or transportation-cost panels for China 1994-2024 (road and rail) for market-access, connectivity, or gravity-style research
  - Transport-network exposure measures consistent with the Ma-Tang design-speed methodology
  - Replication or extension of Ma & Tang (2024 JIE) quantitative spatial analysis
  choose_over:
  - Choose this over china-high-speed-rail-network when BOTH road and rail networks (not HSR alone) are needed at prefecture-pair level
  - Choose this over china-amap-migration-flow-indices / china-mobile-signaling-mobility-data when the research needs travel time/cost, not observed population flows
  - Choose this over china-io-table interprovincial trade files (Tombe-Zhu family) for transport cost inputs - the Ma & Tang paper does NOT use IO-table trade flows
  not_good_for:
  - Freight volumes, trade flows, or traffic counts (the dataset covers travel time/design speed, not flows)
  - Post-2024 or pre-1994 travel times
  - Directly reproducing the Ma & Tang model without the paper's code and the restricted inputs (2005 1% survey, customs data)
  needs_join_for:
  - Economic outcomes (population, wages, output) for distributional analysis
  - Population flows (2005 One Percent Population Survey per the paper; china-census family)
  - Trade elasticity estimation data (customs transactions 2000-2005; china-customs)
  variation_available:
  - Time variation in prefecture-pair travel times 1994-2024 (network expansion)
  - Cross-pair and cross-mode (road vs rail) variation
  - Design-speed standard changes over time (construction vintage)
  topics:
  - transportation networks
  - travel time
  - market access
  - road and rail
  - spatial economics

good_for:
- market access panels
- transportation costs
- connectivity and development
identification:
- network-expansion variation over time (reduced-form and quantitative-model use)
linkable_keys:
- Prefecture (pair)
- Year
- Pixel coordinates (design speed files)

joins:
- target: china-high-speed-rail-network
  relation: complement
  keys:
  - prefecture
  - year
  method: HSR network replication asset (Borusyak-Hull) vs this road+rail travel-time dataset; complementary for connectivity measures
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - prefecture
  - year
  method: The paper's population-flow input is the 2005 One Percent Population Survey (china-census family)
  evidence_status: literature-used
- target: china-customs
  relation: complement
  keys: []
  method: The paper estimates the trade elasticity from the Customs Transaction Dataset 2000-2005 (china-customs family)
  evidence_status: literature-used
- target: china-io-table
  relation: often-confused-with
  keys: []
  method: Ma & Tang do NOT construct interprovincial trade flows from IO tables; the Tombe-Zhu internal-trade files in china-io-table are a different asset
  evidence_status: verified

access_routes:
- route: github-repository
  access_status: available
  direct_url: https://github.com/malin84/transportation_networks_of_china
  requirements: Public GitHub access; enough local storage and a CSV-capable tool for the desired component.
  steps:
  - Open the repository (malin84/transportation_networks_of_china).
  - Read the repository README to choose among pref_pair, pixel_info, and seg_info.
  - For a city-pair panel, download pref_pair/cityinfo.csv and the three time_cost_prefecture_pair CSVs; use origin, destination, and year_yyyy columns.
  - For point-to-point routing, use pixel_info with sample_codes; for construction or design-standard work, use seg_info and its segment-year and segment-pixel files.
  deliverable: Documented CSV components and sample routing code from the public repository.
  cost: free
  last_checked: '2026-09-27'
  caveat: Version 2.0 revises the original paper-era data. Cite Ma--Tang as instructed by the repository and check version correspondence before claiming an exact paper replication.
- route: author-data-page
  access_status: available
  direct_url: https://lin-ma.com/data.html
  requirements: None
  steps:
  - Open Lin Ma's Data page, which describes the three components and links the GitHub repo, Latest Release, and citation.
  deliverable: Component description and authoritative links.
  cost: free
  last_checked: '2026-08-15'
  caveat: Page text cached 2026-08-15; links point to the GitHub repo.
- route: paper-wp-full-text
  access_status: available
  direct_url: https://lin-ma.com/uploads/3/6/0/7/36070314/mt_transportation.pdf
  requirements: None
  steps:
  - Download the final working-paper version of Ma & Tang (JIE 2024) from the author's site (cached 2026-08-15).
  - Read Section 2 and Appendix B for the network construction (digital maps, design-speed standards) and Appendix B.4 for the economic data inputs.
  deliverable: Full paper text documenting the construction that the dataset formalizes; NOT the dataset itself.
  cost: free
  last_checked: '2026-08-15'
  caveat: Author-hosted WP; may differ slightly from the published JIE version.

access:
  url: https://github.com/malin84/transportation_networks_of_china
  cost: free
  license: GPL-3.0 repository license; separately assess underlying source-material terms before redistributing material beyond the released repository
  format: [CSV, MATLAB sample code, Markdown documentation]
  api: false
  how_to_get: >-
    Public GitHub download: open the repository, read the README/release notes,
    and download the release files. The author's Data page (lin-ma.com/data.html)
    is the authoritative description of the three components.
caveats: >-
  Version 2.0 changed the routing algorithm, added 2018-2024 infrastructure,
  and corrected some earlier segments. It is a documented usable release, not
  automatically an exact copy of the paper-era matrix. The related paper (Ma & Tang 2024 JIE)
  is a quantitative spatial model - it does NOT release or use an observed
  interregional trade-flow dataset; do not route trade-flow questions here.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

production:
  raw_sources:
  - name: 'Digital maps of China road/rail networks (per paper Appendix B: e.g. 2007 Guangdong Maps 1:6 million Lambert; 2007 national roads/expressways/railways map)'
    source_type: other
    role: Network geometry input for the travel-time construction
    access_route: Map products cited in the paper; current availability unverified
    url: needs-verification
    coverage: China road, highway, railroad, and waterway layers
    last_checked: '2026-08-15'
  - name: Ministry of Transportation Technical Standard of Highway Engineering revisions (1988, 1997, 2003, 2014; JTG B01-2014)
    source_type: document
    role: Design-speed standards used to classify roads and set travel costs
    access_route: Ministry of Transportation publications (paper section 2.2)
    url: needs-verification
    coverage: Design speed by road class, terrain, and revision year
    last_checked: '2026-08-15'
  - name: GTOPO30 (USGS) and USGS Global Land Cover Characteristics
    source_type: dataset
    role: Terrain and land cover for construction-cost approximation (minimum spanning tree per Faber 2014)
    access_route: USGS public downloads
    url: needs-verification
    coverage: ~1 km grid, global
    last_checked: '2026-08-15'
  acquisition_methods:
  - download
  - other (map parsing and standardization)
  sample_construction: >-
    The released dataset's three components (prefecture-pair travel times on
    road and railroad 1994-2024; construction years and design codes;
    pixel-level design speed and trespassing time) follow the paper's network
    construction (Section 2, Appendix B): roads re-classified by design speed
    per the MOT standard revision in force at construction, pixel-level travel
    costs, and prefecture-pair shortest-path times. The Version 2.0 README
    documents the released components, their fields, and the Dijkstra routing
    implementation used for the current release.
  pipeline_stages:
  - stage: collect
    inputs:
    - digital maps
    - MOT standard revisions
    method: Gather road/rail layers and the design-speed standards by revision year (paper section 2.2)
    tools: []
    parameters: []
    output: Standardized network layers with construction years
    evidence: 'Ma & Tang WP section 2.2 and Appendix B (lin-ma.com PDF, read in full 2026-08-15)'
  - stage: model
    inputs:
    - standardized layers
    - GTOPO30 terrain
    - land cover
    method: Assign pixel-level travel costs (design speed by road class/revision), approximate construction costs via minimum spanning tree, compute prefecture-pair travel times
    tools: []
    parameters:
    - design speed per revision (e.g. 120 km/h highways in plain areas post-2014)
    - pixel cost baselines (e.g. no road 10, highway 2.5, national road 3.75 per paper section 2.3)
    output: Transportation cost matrix and travel times
    evidence: 'Ma & Tang WP section 2.3 (parameters quoted) - paper-level methodology; released-file equivalence unverified'
  - stage: validate
    inputs:
    - traffic-volume shares by mode
    method: Calibrate mode-choice parameters to China City Statistics Yearbook 2005 traffic volume by mode (paper section 2.3)
    tools: []
    parameters: []
    output: Network matrix T_ijt used in the paper's quantitative model
    evidence: 'Ma & Tang WP section 2.3; released dataset components per lin-ma.com/data.html'
  constructed_variables:
  - name: Prefecture-pair travel time (road; railroad)
    concept: Shortest-path travel time between prefectures by mode, 1994-2024
    source_fields:
    - digital maps
    - design speed
    method: Pixel-level cost assignment plus shortest-path computation
    validation: Mode-choice calibration to yearbook traffic shares (paper)
    limitations: Version 2.0 uses Dijkstra routing and revises the earlier
      release; it is not automatically identical to the paper-era matrix.
  - name: Pixel-level design speed and trespassing time
    concept: Design speed per pixel and traversal time
    source_fields:
    - MOT standard revisions
    - terrain
    method: Design speed assigned by road class/revision and terrain
    validation: None evidenced beyond the paper's calibration
    limitations: The files include built-infrastructure pixels; a user
      computing new routes must choose an empty-pixel traversal speed.
  validation:
  - Paper-level: mode-choice parameters calibrated to China City Statistics Yearbook 2005 traffic shares (section 2.3)
  - >-
    Release-level: public Version 2.0 README documents the component files,
    fields, 279-prefecture panel, annual coverage, and sample routing code
    (checked 2026-09-27)
  output:
    unit_of_observation: prefecture-pair (travel times); pixel (design speed/trespassing time); segment (construction years/design codes)
    structure: annual travel-time panel 1994-2024 plus pixel/segment files
    geography: China prefecture-level road and rail networks
    time_span: '1994-2024'
    key_variables:
    - prefecture-pair road travel time
    - prefecture-pair railroad travel time
    - construction years and design codes
    - pixel-level design speed and trespassing time
    formats:
    - CSV
    - MATLAB sample code
    - Markdown documentation
  reproducibility:
    level: medium
    starting_point: GitHub release download (repo malin84/transportation_networks_of_china)
    code_available: true
    code_url: https://github.com/malin84/transportation_networks_of_china/tree/main/sample_codes
    requirements:
    - Public GitHub download
    - Local storage and a CSV-capable analysis tool; custom pixel routing also
      needs the supplied sample-code workflow or an equivalent implementation
    blockers:
    - Exact equivalence between Version 2.0 and the paper-era analysis matrix
      is not established
  compliance:
    terms_or_license: GPL-3.0 repository license displayed with the public README (checked 2026-09-27)
    robots_or_rate_limits: None known (public GitHub release)
    personal_or_sensitive_data: None evidenced (network/travel-time data)
    redistribution: Follow the GPL-3.0 repository license for released contents; assess underlying third-party source terms separately if redistributing material beyond the release
    review_needed: false

used_by:
- cite: 'Ma, Lin & Yang Tang (2024), The Distributional Impacts of Transportation Networks in China'
  doi: https://doi.org/10.1016/j.jinteco.2023.103873
  journal: Journal of International Economics
  year: 2024
  dataset_role: Related paper - the author's released dataset formalizes the paper's transport-network construction (design-speed methodology, prefecture-pair costs)
  evidence_type: author-site-plus-working-paper
  evidence_url: https://lin-ma.com/data.html
  data_note: >-
    Author's Data page (cached 2026-08-15) lists the dataset with "Related
    Paper" = Ma & Tang JIE 2024. Author-hosted final WP read in full: the
    paper constructs transportation networks from digital maps and MOT
    Technical Standard of Highway Engineering design-speed revisions
    (1988/1997/2003/2014); economic inputs per Appendix B.4 are the 2005 One
    Percent Population Survey, the Customs Transaction Dataset 2000-2005, and
    City Statistical Yearbooks. Trade flows are model objects, not a released
    dataset. Published JIE version unread (Elsevier 403); the author's
    published-version link exists on the research page (URL unverified).

provenance:
- source: https://lin-ma.com/data.html
  field_scope:
  - data_identity
  - components
  - access
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://api.github.com/repos/malin84/transportation_networks_of_china (GitHub API record)
  field_scope:
  - repository_identity
  - license
  - size
  - dates
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://github.com/malin84/transportation_networks_of_china
  field_scope:
  - file_inventory
  - coverage
  - unit_of_observation
  - variables
  - version_changes
  - access
  - sample_code
  added: '2026-09-27'
  confidence: high
  verified: true
- source: https://lin-ma.com/uploads/3/6/0/7/36070314/mt_transportation.pdf (author-hosted final WP)
  field_scope:
  - paper_use
  - construction
  - economic_inputs
  added: '2026-08-15'
  confidence: high
  verified: true
- source: ledgers/dataset_candidates.jsonl (china-interregional-trade-flows, Layer-2b sweep 2026-08-15; identity corrected 2026-08-15)
  field_scope:
  - paper_use
  added: '2026-08-15'
  confidence: med
  verified: false

related_datasets:
- id: china-high-speed-rail-network
  relation: complement
- id: china-census
  relation: complement
- id: china-customs
  relation: complement
- id: china-io-table
  relation: often-confused-with
---

## Positioning in one sentence

The "Transportation Networks of China" dataset is a public, documented Version 2.0 author release: it supplies 1994-2024 road and rail travel times for 279 prefectures, plus pixel and segment components, making the transport-network construction behind Ma & Tang (2024 JIE) directly usable without confusing it with a trade-flow dataset.

## Select rules

- Use for prefecture-pair travel-time or transportation-cost panels (road and rail, 1994-2024) for market-access, connectivity, or spatial-model research.
- Pair with china-high-speed-rail-network when HSR-specific market-access measures are needed alongside road/rail travel times.
- Do NOT route interregional trade-flow questions to this record: Ma & Tang's trade flows are model objects, and the paper uses no IO-table-based trade-flow dataset (china-io_table Tombe-Zhu files are a different asset).

## Get recipe

1. Open the public GitHub repository and choose the component that answers the question: pref_pair for city-pair travel times, pixel_info for custom routes, or seg_info for construction and design-standard information.
2. For the usual prefecture-pair panel, obtain cityinfo.csv and the three documented time-cost CSVs, then use origin and destination four-digit division codes with the year_yyyy column for the chosen year.
3. For a new route between pixels, follow the supplied Dijkstra sample code and explicitly set the empty-pixel traversal assumption; for an exact Ma--Tang replication, first compare the required analysis vintage with Version 2.0.

## Connections and Limitations

- Version 2.0 adds 2018-2024 network data, changes the routing algorithm, and corrects some earlier segments. It is documented and usable, but a paper-era replication needs a version check rather than a casual substitution.
- The dataset covers travel time/design speed, not flows - join economic outcomes and population flows (2005 1% survey via china-census) for distributional analysis.
- The paper's model inputs (customs transactions 2000-2005 for the trade elasticity; city statistical yearbooks for traffic volume by mode) are separate restricted/public inputs, not part of this dataset.
