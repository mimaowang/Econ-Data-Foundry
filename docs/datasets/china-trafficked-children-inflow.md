---
schema_version: 3
catalog_status: grounding
id: china-trafficked-children-inflow
name: BCBH-based inflow of trafficked/illegally-adopted children dataset (China, prefecture-year)
aka:
- 被拐儿童流入数据
- Baby Come Back Home (BCBH) trafficked children records
- 宝贝回家数据
provider: >-
  Paper-constructed dataset by Yanjun Li, Yu Bai (Tohoku University) and
  Masaki Nakabayashi (University of Tokyo), built from public case records
  of the 宝贝回家志愿者协会 (Baobeihuijia / Baby Come Back Home, BCBH)
  platform (baobeihuijia.com), China's largest public missing-children
  platform (platform meta description, read 2026-08-15).
china_related: true
domains:
- labor
- crime
- demography
- regional
- policy

data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: >-
    A prefecture-year dataset of the inflow of illegally adopted (abandoned
    or abducted) children under 14, constructed by the paper from
    self-reported BCBH case posts: ~29,000 self-reported cases aggregated to
    destination-prefecture units (paper Section 3.1, full text read
    2026-08-15). Not released: no data-availability statement or replication
    package in the paper (supplementary materials = appendices B/C only).
  availability: partially-reproducible
  ordinary_researcher_feasible: false
  summary: >-
    Paper and platform both verified first-hand (2026-08-15). The paper's
    data section (JCE 53:182-208, full text via the author's researchmap
    attachment) names the source exactly: the BCBH website
    (http://www.baobeihuijia.com), established after the Ministry of Public
    Security's April 2009 anti-trafficking action; 110,000+ missing-children
    cases reported 1900-2022, police-verified before publication; each case
    records name, gender, birth date, lost type, year and location of
    disappearance, destination location (title of post), current location.
    The paper keeps self-reported cases with identifiable destination
    prefectures and children under 14 at disappearance, excludes
    welfare-adoption/runaway cases, classifies rural vs non-rural destination
    by keyword rules, and aggregates to destination-prefecture-year: nearly
    29,000 cases; top destination provinces Henan, Fujian, Hebei, Guangdong,
    Shandong, Jiangsu = 71% of cases. The BCBH platform itself is live and
    machine-readable on content pages (case pages, forum threads,
    reg.baobeihuijia.com registration sections; home page Cloudflare-521 for
    automated clients).
  barrier: >-
    The paper's cleaned prefecture-year dataset and code are not released
    (no DAS/replication); reproducing it means re-collecting and parsing
    BCBH posts with the paper's inclusion rules (self-reported, destination
    in title, age<14, lost-type keywords, rural/non-rural classification) -
    substantial manual/NLP work, and the exact matching to the HRS rollout
    ratio (Almond et al. 2019 / Hu et al. 2021 county-gazette data) is a
    separate data layer.

unit_of_observation: >-
  Paper dataset: prefecture-year counts of inflow of illegally adopted
  children (children under 14 at disappearance; abandoned or abducted;
  self-reported cases with identifiable destination prefecture)
structure: prefecture-year panel (constructed); raw source = case-level posts
geo_granularity:
- prefecture (destination, analysis unit)
- county (HRS rollout layer)
geography: 'Nationwide; destination prefectures of reported cases (top provinces: Henan, Fujian, Hebei, Guangdong, Shandong, Jiangsu = 71%)'
time_span:
  start: '1900'
  end: '2022'
  last_confirmed_release: >-
    BCBH platform: 110,000+ cases spanning 1900-2022 (earliest case 1926),
    per the paper. Paper analysis: main estimation 1974-1984 (HRS rollout
    window); long-term analysis post-1984.
  coverage_note: >-
    Platform cases span 1900-2022, but the paper's estimation window is
    driven by the HRS rollout (1974-1984); the paper uses 1974-1984 for the
    baseline.
  last_checked: '2026-08-15'
frequency:
- event (case level)
- annual (prefecture aggregation)
sample_size: >-
  BCBH platform: 110,000+ missing-children cases (paper); paper analysis
  sample: nearly 29,000 self-reported illegal-adoption cases
key_variables:
- Child name, gender, date of birth
- Lost type (abandoned / sold-placed-sent for adoption / abducted / other)
- Year and location of disappearance
- Destination location (in post title for self-reported cases)
- Current location
- Rural vs non-rural destination classification (keyword rules)
- Prefecture-year inflow counts (constructed)
- HRS rollout ratio (county share adopted, from gazette data)

research_fit:
  best_for:
  - Research on the geography and timing of child trafficking/illegal adoption inflow in China using a public platform's case records
  - Reconstructing the Li-Bai-Nakabayashi (JCE 2025) dataset or its approach for related trafficking research
  choose_over:
  - Choose this BCBH-based asset over court-judgment records (china-court-judgments-2014-2018-open-justice) for trafficking inflow measurement: BCBH records capture underground transfers that never reach court records, and the paper follows Wang et al. (2018) and Bao et al. (2023) in using missing-children records to measure illegal child trade.
  - Do NOT use it as a measure of total trafficking incidence: it covers reported missing children with verified posts, and destination is known only for self-reported (victim) cases.
  not_good_for:
  - Total trafficking incidence or official crime statistics (paper itself notes China collects no official statistics on child trafficking)
  - Claiming the paper's cleaned dataset is downloadable (it is not released)
  - Individual-level outcome analysis beyond the paper's prefecture-year aggregation without re-collection
  needs_join_for:
  - HRS rollout timing (Almond et al. 2019 JPE county-gazette data; Hu et al. 2021 WP) for the paper's design
  - Demographic or economic controls (prefecture level)
  variation_available:
  - Destination-prefecture and year variation in inflow; HRS rollout timing variation (prefecture share) - assignment/design details belong to Econ-Variation
topics:
- child trafficking
- illegal adoption
- missing children
- platform data
- prefecture panel

good_for:
- Prefecture-level trafficking inflow measurement from a public platform
- Understanding the construction and limits of the JCE 2025 dataset
identification: []
linkable_keys:
- Destination prefecture name (text-extracted from posts)
- Year of disappearance
- Case number (BCBH)

joins:
- target: china-court-judgments-2014-2018-open-justice
  relation: complement
  keys:
  - Prefecture
  - Year
  method: Compare/cross-validate trafficking case inflows; different recording universes (court records vs platform reports)
  evidence_status: plausible

access_routes:
- route: platform-public-pages
  access_status: available-with-technical-friction
  direct_url: https://baobeihuijia.com/
  requirements: None for content pages; home page returns Cloudflare 521 to automated clients (2026-08-15), content pages fetch fine
  steps:
  - Browse case content pages (e.g., /bbhj/contents/13/256644.html), forum threads (bbs.baobeihuijia.com/thread-226914-1-1.html), and registration sections (reg.baobeihuijia.com/seek/findhome.html etc.).
  - Collect self-reported case posts (宝贝寻家) with destination locations in titles; parse fields per the paper's rules.
  - Verify case details with local police per platform practice (the platform does this; researchers should respect privacy).
  deliverable: Raw public case posts; the paper's cleaned prefecture-year dataset is NOT released
  cost: free
  last_checked: '2026-08-15'
  caveat: >-
    Reproduction requires the paper's inclusion rules (self-reported,
    destination identifiable, age<14, lost-type filtering, rural/non-rural
    keyword classification); privacy/redistribution caution - case posts
    contain personal data (children and families).
- route: author-contact
  access_status: needs-verification
  direct_url: needs-verification
  requirements: Author discretion (corresponding author Yu Bai, Tohoku University)
  steps:
  - Ask the authors whether the cleaned dataset or extraction code can be shared; no established release route exists.
  deliverable: Unverified; author discretion only
  cost: by-application
  last_checked: '2026-08-15'
  caveat: Research courtesy route; no DAS or replication package exists in the paper.

access:
  url: https://baobeihuijia.com/
  cost: free
  license: >-
    Platform content is publicly posted by the 宝贝回家志愿者协会 (吉ICP备08101543号-1);
    case posts contain personal data - handle with privacy/IRB care; no
    redistribution terms read from the platform (法律声明 page not fetched)
  format:
  - html
  api: false
  how_to_get: >-
    Public platform: collect case posts from baobeihuijia.com (content pages
    and bbs threads) and rebuild the paper's prefecture-year inflow dataset
    using its documented inclusion rules. The paper's own dataset is not
    released.
caveats:
- The paper's dataset is not released (no DAS/replication); do not promise a download.
- Platform home is Cloudflare-521 for automated clients; content pages are machine-readable.
- Cases are self/family-reported and police-verified but not a complete register of trafficking; destination prefectures exist only for self-reported cases (paper restriction).
- Personal data: case posts name children and families; collection/redistribution needs privacy review.
- HRS rollout layer (Almond et al. 2019 / Hu et al. 2021) is a separate dataset; design details belong to Econ-Variation.

production:
  raw_sources:
  - name: BCBH (宝贝回家) platform case posts
    source_type: webpage
    role: Missing-children case records (self-reported + family-reported)
    access_route: https://baobeihuijia.com/ content pages; https://bbs.baobeihuijia.com/ forum threads
    url: https://baobeihuijia.com/
    coverage: 110,000+ cases 1900-2022 (paper); destination prefecture only for self-reported cases
    last_checked: '2026-08-15'
  - name: HRS rollout data (county gazettes)
    source_type: dataset
    role: County-by-county HRS first-adoption year; prefecture rollout ratio
    access_route: Digitized by Almond, Li & Zhang (2019 JPE 127(2):560-585) and Hu, Huang, Luo & You (2021 WP) from county gazettes
    url: needs-verification
    coverage: County-level HRS first appearance 1976-1984 (some counties 1976-77; all by end 1984)
    last_checked: '2026-08-15'
  acquisition_methods:
  - crawl
  - manual coding
  - text extraction
  sample_construction: >-
    Paper Section 3.1 (read in full): keep self-reported (victim) cases;
    extract destination prefecture from post title; exclude posts without
    identifiable destination; keep only children under 14 at disappearance;
    classify lost types - abandonments/informal adoption (keywords
    "abandoned", "sold/placed/sent for adoption") and abductions kept;
    welfare-adoption and runaway cases excluded; rural vs non-rural
    destination by keyword rules (rural terms vs municipal-district names);
    aggregate to destination-prefecture-year. Final: ~29,000 cases.
  pipeline_stages:
  - stage: collect
    inputs:
    - BCBH self-reported case posts
    method: Collect posts; extract destination prefecture from titles (text format)
    tools: []
    output: Case-level records with destination prefecture
    evidence: Paper Section 3.1 + Appendix Fig A.1 (example post) and Appendix B
  - stage: clean
    inputs:
    - Case-level records
    method: Apply lost-type filters, age<14 restriction, rural/non-rural classification; aggregate to prefecture-year
    tools: []
    output: ~29,000-case dataset aggregated to destination-prefecture-year
    evidence: Paper Section 3.1, Table 1 Panel A, Appendix B
  - stage: match
    inputs:
    - Prefecture-year inflow counts
    - HRS rollout ratio (county share adopted)
    method: Aggregate HRS county rollout to prefecture; join to inflow counts; baseline window 1974-1984
    tools: []
    output: Analysis panel (DDD with land-reform rollout)
    evidence: Paper Section 3.2
  constructed_variables:
  - name: Rural vs non-rural destination
    concept: Whether the child was adopted by a rural or non-rural household
    source_fields:
    - Destination description
    method: Keyword rules - rural terms (rural households, farmers, village, rural areas) vs municipal-district names
    validation: Appendix B examples
    limitations: Reduces sample size; misclassification risk for mixed descriptions
  - name: Prefecture-year inflow count
    concept: Number of illegally adopted children reported into each destination prefecture per year
    source_fields:
    - Destination prefecture
    - Disappearance year
    method: Aggregate self-reported cases; adoption year approximated within 1 year of disappearance year (Appendix B justification)
    validation: Court documents/literature on trafficking-case timing (paper cites sales within 6 months, often 3)
    limitations: Self-reported only; undercounts cases without known destination
  validation:
  - Paper validates against court documents and trafficking-case literature for adoption timing.
  - Platform staff verify posts with local police before publication (paper).
  - Top-6 destination provinces account for 71% of reported cases (paper Fig. 2a).
  output:
    unit_of_observation: Prefecture-year inflow counts (analysis); case-level posts (raw)
    structure: Prefecture-year panel (constructed)
    geography: Destination prefectures nationwide
    time_span: Platform 1900-2022; analysis 1974-1984 (+ long-term post-1984)
    key_variables:
    - Prefecture-year inflow count
    - HRS rollout ratio
    - Rural/non-rural shares
    formats:
    - not released
  reproducibility:
    level: low
    starting_point: https://baobeihuijia.com/ (case posts) + HRS gazette data (Almond et al. 2019)
    code_available: false
    code_url:
    requirements:
    - Collection and parsing of BCBH posts with the paper's inclusion rules
    - HRS rollout county data (Almond et al. 2019 JPE / Hu et al. 2021 WP)
    - Privacy review for personal data in posts
    blockers:
    - Paper dataset/code not released
    - Home page Cloudflare-blocked for automated clients (content pages OK)
    - Manual/NLP work for destination extraction and classification
  compliance:
    terms_or_license: Platform posts are public; personal data of children and families - privacy/IRB review needed
    robots_or_rate_limits: Content pages fetched fine via python HTTPS (2026-08-15); home page 521 - respect rate limits and site terms
    personal_or_sensitive_data: Yes - case posts contain names, dates, locations of missing children and families
    redistribution: Do not redistribute case-level personal data; aggregate statistics only with review
    review_needed: true

quality:
  profile_status: verified
  access_status: partial
  paper_use_status: verified
  last_audited: '2026-08-15'

used_by:
- cite: 'Li, Bai & Nakabayashi (2025), Land reform and illegal adoption of children'
  doi: https://doi.org/10.1016/j.jce.2025.01.002
  journal: JCE
  year: 2025
  dataset_role: >-
    Main outcome: prefecture-year inflow of illegally adopted children
    (purchased children aged 0-14, from self-reported BCBH cases), in a
    triple-differences design with the HRS rollout
  evidence_type: data-section
  evidence_url: https://researchmap.jp/masaki.nakabayashi/published_papers/49016344/attachment_file.pdf
  data_note: >-
    Full published text read 2026-08-15 (27 pp; author's researchmap
    attachment). Section 3.1: source = BCBH website (baobeihuijia.com),
    established after the MPS April 2009 anti-trafficking action; 110,000+
    cases 1900-2022, police-verified; fields incl. name, gender, DOB, lost
    type, year/location of disappearance, destination (post title), current
    location; analysis sample ~29,000 self-reported illegal-adoption cases
    (<14 at missing, destination identified), aggregated to destination
    prefecture-year; rural/non-rural keyword classification (Appendix B).
    Section 3.2: HRS rollout ratio from county gazettes digitized by Almond
    et al. (2019 JPE) and Hu et al. (2021 WP); baseline window 1974-1984.
    No DAS or replication package (supplementary = appendices B/C only).

provenance:
- source: https://researchmap.jp/masaki.nakabayashi/published_papers/49016344/attachment_file.pdf (full text, read 2026-08-15)
  field_scope:
  - data source identity (BCBH), construction rules, sample, fields, validation
  - HRS rollout data origin (Almond et al. 2019; Hu et al. 2021)
  - absence of DAS/replication
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://baobeihuijia.com/bbhj/contents/13/256644.html and /bbhj/channels/33.html (read 2026-08-15)
  field_scope:
  - platform live, machine-readable content pages; sections and forum
  - 宝贝回家志愿者协会; 吉ICP备08101543号-1; meta description (largest public missing-children search site)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://so.baobeihuijia.com/bbhj/contents/13/264918.html (read 2026-08-15)
  field_scope:
  - case page structure and detail level (case number, timeline, family/volunteer involvement)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://baobeihuijia.com/ (521 Cloudflare, 2026-08-15)
  field_scope:
  - home page automated-client block; content pages unaffected
  added: '2026-08-15'
  confidence: high
  verified: true

related_datasets:
- id: china-court-judgments-2014-2018-open-justice
  relation: complement
- id: china-agricultural-census-1997-1pct
  relation: complement
---

## Positioning in one sentence

The JCE 2025 trafficked-children dataset is a paper-constructed prefecture-year inflow panel (~29,000 self-reported illegal-adoption cases) built from the public 宝贝回家 (BCBH) missing-children platform - the paper's full text names the source and construction rules, the platform is live and machine-readable, but the cleaned dataset and code are not released, so the route is re-collection with the paper's inclusion rules.

## Select rules

- Use this record when a research idea needs Chinese child-trafficking inflow geography/timing: the BCBH-based approach is the documented measurement route (Wang et al. 2018; Bao et al. 2023; Li-Bai-Nakabayashi 2025).
- Prefer court-judgment records only for adjudicated cases; BCBH captures underground transfers not in court records.
- Do not treat platform case counts as total trafficking incidence, and do not promise the paper's dataset as a download.

## Get recipe

1. Collect self-reported BCBH case posts (宝贝寻家) from baobeihuijia.com content pages and bbs.baobeihuijia.com threads (content pages fetch fine; home 521 for automated clients).
2. Apply the paper's rules: destination prefecture from post titles, age<14, lost-type filters, rural/non-rural keyword classification; aggregate to prefecture-year.
3. Join the HRS rollout ratio (Almond et al. 2019 / Hu et al. 2021 county-gazette data) for the 1974-1984 design window; obtain privacy review before handling case-level personal data.

## Connections and Limitations

The paper dataset is not released; reproduction is manual/NLP collection work with personal-data handling. Destination prefectures exist only for self-reported cases, so family-reported-only case flows are invisible. The HRS rollout layer is a separate data asset (design/assignment details belong to Econ-Variation). Platform content pages are machine-readable; the home page is Cloudflare-blocked for automated clients.
