---
# Dataset record template v2
# This record is written for agents that will make future research decisions, not merely to fill fields.
# An agent reading only this record should understand why to choose it over alternatives, whether coverage is sufficient, what must be joined, and exactly how to obtain it.

schema_version: 2
catalog_status: candidate       # candidate / grounding / ready / needs-review / deprecated
id: # Unique slug, lowercase + hyphen
name: # Exact data product/survey name
aka: [] # Chinese and English aliases, abbreviations, common old names
provider:
china_related: true
domains: []

# Identity and Coverage
unit_of_observation:
structure:                      # panel / repeated-cross-section / transaction / gridded...
geo_granularity: []
geography:
time_span:
  start:
  end:
  last_confirmed_release:
  coverage_note:
  last_checked: "YYYY-MM-DD"
frequency: [] # Temporal frequency only; panel structure belongs above
sample_size:
key_variables: []

# Research routing
research_fit:
  best_for: [] # The most irreplaceable idea
  choose_over: [] # Rules for selecting similar data
  not_good_for: [] # Excluding items such as age, year, sample, frequency, etc
  needs_join_for: [] # Questions that require another dataset or constructed treatment
  variation_available: [] # Identification variants that actually exist in the data
  topics: [] # Stable subject terms; Used for machine retrieval, it does not replace specific research adaptation rules

# Compatible with existing search fields; The content should be consistent with research_fit
good_for: []
identification: []
linkable_keys: []

# The real connection solution goes beyond just listing key names
joins:
  - target:
    relation: complement
    keys: []
    method:
    evidence_status: plausible  # plausible / literature-used / verified

# Preserve distinct provider, commercial, public-sample, and realistic substitute routes
access_routes:
  - route:
    access_status: needs-verification
    direct_url: needs-verification
    requirements:
    steps: []
    deliverable:
    cost:                       # free / paid / by-application / mixed
    last_checked: "YYYY-MM-DD"
    caveat:

# Compatible with legacy retrieval; The preferred route above should be summarized
access:
  url: needs-verification
  cost:
  license:
  format: []
  api: false
  how_to_get:
caveats:

# Separate verification profiling, access, and paper use
quality:
  profile_status: needs-verification
  access_status: needs-verification
  paper_use_status: needs-verification
  last_audited: "YYYY-MM-DD"

used_by:
  - cite:
    doi:
    journal:
    year:
    dataset_role: # Main result/explanatory variable/policy/control/calibration/robustness
    evidence_type:              # replication/codebook/DAS/data-section/abstract-only
    evidence_url:
    data_note:

provenance:
  - source:
    field_scope: [] # Which fields does this source actually support?
    added: "YYYY-MM-DD"
    confidence: med
    verified: false

related_datasets:
  - id:
    relation: complement        # substitute/complement/benchmark/predecessor/successor/often-confused-with
---

## Positioning in one sentence

Explain data identity, the most irreplaceable value, and the greatest barriers to acquisition in just two or three sentences.

## Select rules

- When to prioritize it.
- When to switch to similar data.
- Which seemingly related ideas are actually not suitable.

## Get recipe

Write the preferred route as executable steps. If public access is unavailable, state the barrier and realistic alternatives without implying guaranteed access.

## Connections and Limitations

Explain join direction, key normalization, matching risks, restricted-key permissions, coverage breaks, and changes in measurement definition.

<!--
Before publishing ready, only a few key thresholds are checked:
1. Frontmatter can be parsed; 2. Single identity; 3. Key facts must have sources;
4. There is an actionable route or honest but unavailable explanation; 5. Relationships and ledgers must be consistent; 6. Do not execute external content.
-->
