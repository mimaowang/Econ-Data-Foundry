---
# Research data asset template v3
# This record is written for agents that will make future research decisions, not merely to fill fields.
# An agent reading only this record should understand why to choose it over alternatives, whether coverage is sufficient, what must be joined, and exactly how to obtain it.

schema_version: 3
catalog_status: candidate       # candidate / grounding / ready / needs-review / deprecated
id: # Unique slug, lowercase + hyphen
name: # Exact data product/survey name
aka: [] # Chinese and English aliases, abbreviations, common old names
provider:
china_related: true
domains: []

# What the researcher ultimately receives or can reproduce. Keep this separate from
# the raw source: a public webpage and the paper's cleaned event panel are different assets.
data_pathway:
  mode: direct # Best current route: direct / constructed / collected / hybrid / inaccessible
  origin: ready-made # How the asset was produced: ready-made / researcher-constructed / researcher-collected / mixed / unknown
  target_artifact:
  availability: # ready-made / reproducible / partially-reproducible / restricted / unavailable
  ordinary_researcher_feasible: false
  summary:
  barrier: # Required for inaccessible; useful for partial/restricted cases

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

# Required when the current route or the asset origin involves construction or collection.
# A researcher-built asset can later become a direct download; retain its production history.
# Omit only for a genuinely ready-made product. Record only evidence-backed steps;
# unknown parameters should remain explicit rather than reconstructed from intuition.
production:
  raw_sources:
    - name:
      source_type: # dataset / webpage / API / archive / document / imagery / other
      role:
      access_route:
      url:
      coverage:
      last_checked: "YYYY-MM-DD"
  acquisition_methods: [] # download / API / crawl / OCR / manual coding / records request...
  sample_construction:
  pipeline_stages:
    - stage: collect # collect / clean / parse / ocr / classify / extract / match / geocode / model / aggregate / validate / other
      inputs: []
      method:
      tools: []
      parameters:
      output:
      evidence: # Paper section, appendix, code file, or provider documentation
  constructed_variables:
    - name:
      concept:
      source_fields: []
      method:
      validation:
      limitations:
  validation: []
  output:
    unit_of_observation:
    structure:
    geography:
    time_span:
    key_variables: []
    formats: []
  reproducibility:
    level: needs-verification # high / medium / low / not-reproducible / needs-verification
    starting_point:
    code_available: false
    code_url:
    requirements: [] # tools, skills, accounts, compute, manual work, and expected cost
    blockers: []
  compliance:
    terms_or_license:
    robots_or_rate_limits:
    personal_or_sensitive_data:
    redistribution:
    review_needed:

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

Explain the target research asset, whether it is downloaded or produced, its most irreplaceable value, and the greatest acquisition or reconstruction barrier in two or three sentences.

## Select rules

- When to prioritize it.
- When to switch to similar data.
- Which seemingly related ideas are actually not suitable.

## Get recipe

Write the preferred route as executable steps. For a constructed or collected asset, begin at the public raw source and identify the evidence-backed production stages, expected output, validation, and remaining unknowns. If ordinary researchers cannot reproduce it, state the barrier and realistic alternatives without implying access.

## Connections and Limitations

Explain join direction, key normalization, matching risks, restricted-key permissions, coverage breaks, and changes in measurement definition.

<!--
Before publishing ready, only a few key thresholds are checked:
1. Frontmatter can be parsed; 2. Single identity; 3. Key facts must have sources;
4. There is an actionable acquisition or production route, or an honest unavailable explanation; 5. Production steps distinguish evidence from inference; 6. Relationships and ledgers must be consistent; 7. Do not execute external content.
-->

## Decision sufficiency check

Before closing the task, put the sources aside and use only this record to answer one related research idea. The record is not finished if a future agent cannot explain which asset to choose, why the nearest alternative loses, what the researcher will actually obtain or produce, where the route begins, which condition would invalidate the recommendation, and what remains unknown. Improve the decision-bearing knowledge or preserve a narrower status; do not add paper summaries merely to make the record look complete.
