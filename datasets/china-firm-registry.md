---
schema_version: 3
catalog_status: grounding
id: china-firm-registry
name: China Administrative Firm Registry (SAIC/SAMR registration records)
aka:
- China Firm Registry Data
- SAIC firm registry
- SAMR enterprise registration records
- 工商登记数据
- 企业注册登记数据
provider: State Administration for Industry and Commerce (SAIC), now within the State Administration for Market Regulation (SAMR)
china_related: true
domains:
- firm
- labor
- entrepreneurship
- regional
- urban
- migration
data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: Restricted administrative records of newly established Chinese firms, with county-level aggregates used in the paper
  availability: restricted
  ordinary_researcher_feasible: false
  summary: The paper identifies a registry of all newly established firms registered in China from 2010 through 2016, containing more than 16 million records and detailed registration fields. The publisher article is open access, but the registry itself is described as restricted-use proprietary administrative data and no public file or ordinary researcher download route is established.
  barrier: Access depends on a controlled administrative or institutional route that is not documented as a general public application in the checked sources. The paper's CC BY-NC article license covers the article, not the underlying registry.
unit_of_observation: Newly established firm registration record
structure: Administrative firm-entry records with status and location fields; paper aggregates observations to county-year measures
geo_granularity:
- firm
- registration authority
- county
- city or province when supplied by the approved extract
geography: China-wide registration universe as described by the paper; the analysis uses county-level firm-entry outcomes, but the exact public geographic fields and boundary vintage are not established.
time_span:
  start: 2010
  end: 2016
  last_confirmed_release: 2016
  coverage_note: The paper selects 2010-2016 around its research window. A current registry release, historical completeness outside that window, and post-2016 coverage are not established.
  last_checked: '2026-08-12'
frequency:
- event-based
- annual aggregation in the paper
sample_size: More than 16 million newly established firms in the paper's described 2010-2016 registry window
key_variables:
- Establishment date and registration location
- Firm type, including the distinction between firms and individual businesses
- Initial registered capital
- Industry code and registration authority
- Active or closed status
- Firm name, registration number, and Unified Social Credit identifier when present
research_fit:
  best_for:
  - County-level firm entry and entrepreneurship, including small firms outside the ASIF size threshold
  - Local labor-market adjustment and the spatial distribution or survival of newly established firms
  - Firm-type and industry heterogeneity in regional or urban business formation
  choose_over:
  - Prefer this registry over ASIF when small and newly registered firms, individual-business exclusions, or county-level entry are central.
  - Prefer ASIF for annual production, employment, and productivity of large industrial firms; prefer CSMAR for listed-firm financial statements.
  not_good_for:
  - A public, reproducible firm panel; household outcomes; informal activity without registration; or a current post-2016 firm census
  - Assuming registration records measure active production, employment quality, or survival without the registry's status and cleaning rules
  needs_join_for:
  - County or city economic context requires a documented geographic key and boundary vintage.
  - Labor, migration, or policy studies require separately sourced household or local-policy data; this record does not supply treatment timing.
  variation_available:
  - Firm entry, closure/status, location, type, and capital differences observed in the registry; no policy assignment or causal classification is recorded here.
  topics:
  - entrepreneurship
  - firm entry and exit
  - local labor markets
  - migration and hukou
  - urban-rural development
  - regional business formation
good_for:
- Measuring newly registered business formation at county or city scale
- Studying the extensive margin of entrepreneurship beyond large industrial firms
- Connecting local labor-market conditions to entry, firm type, size, and survival outcomes when access is approved
identification:
- County-year entry and survival comparisons using the paper's documented construction
- Firm-type and industry comparisons; causal interpretation requires an external design and is not asserted by this data record
linkable_keys:
- Firm registration number or Unified Social Credit identifier when supplied
- Registration county/city/province code and registration authority
- Establishment year and status date
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - County or city code and boundary vintage
  - Year
  method: Aggregate registry records to the same administrative unit and year after confirming code definitions; retain unmatched jurisdictions rather than silently reassigning them.
  evidence_status: plausible
- target: asif
  relation: complement
  keys:
  - Firm name, registration location, industry, and year where available
  method: Use a documented concordance only; the registry covers small/new firms while ASIF covers a different industrial universe and should not be treated as a one-to-one match.
  evidence_status: plausible
access_routes:
- route: Labour Economics article data description
  access_status: documentation-only
  direct_url: https://www.sciencedirect.com/science/article/pii/S0927537124001003
  requirements: Read the paper's data section and appendix; an approved data request or institutional route is still required for the underlying registry.
  steps:
  - Confirm the exact 2010-2016 scope and fields described in the paper.
  - Contact the authors or the responsible administrative data institution to ask whether an eligible controlled-use route exists.
  - Record the approved extract, fields, identifiers, output controls, and terms before analysis.
  deliverable: Documentation of the restricted registry and any written access decision; the open article is not the data file.
  cost: by-application
  last_checked: '2026-08-12'
  caveat: The checked article does not publish the registry, a download link, or a general application form.
access:
  url: https://www.sciencedirect.com/science/article/pii/S0927537124001003
  cost: by-application
  license: Article is open access under its stated terms; the registry remains controlled administrative data and has no inferred redistribution license.
  format:
  - unknown
  api: false
  how_to_get: Start with the paper's data description and ask the authors or relevant administrative data institution about a controlled-use application. Do not substitute public company directories or an ASIF extract for this registry.
caveats: The paper's more-than-16-million figure describes the research registry window, not a guarantee of a current national download. Registration is not the same as active production, and firm, individual-business, cooperative, and other record types must be separated using the paper's rules. County codes, boundary vintages, status definitions, missingness, and identifiers require the approved file or documentation.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-08-12'
used_by:
- cite: 'Liu, Xu & Zou (2024), Migration Barrier Relaxation and Entrepreneurship: Evidence from the Hukou Reform in China'
  doi: https://doi.org/10.1016/j.labeco.2024.102605
  journal: Labour Economics
  year: 2024
  dataset_role: Main county-level entrepreneurship outcomes from administrative records of newly established firms
  evidence_type: publisher_full_text
  evidence_url: https://www.sciencedirect.com/science/article/pii/S0927537124001003
  data_note: The paper states that it uses restricted-use administrative records of all newly established firms registered in China from 2010-2016, covering more than 16 million records, with date, location, firm type, registered capital, industry, status, registration authority, and identifier fields. It aggregates the registry to county-level entry outcomes. The paper is open access, but the underlying registry and any cleaned analysis file are not thereby public.
provenance:
- source: Liu, Xu & Zou (2024) ScienceDirect full article https://www.sciencedirect.com/science/article/pii/S0927537124001003
  field_scope:
  - actual registry use
  - restricted-use status
  - 2010-2016 period
  - more-than-16-million record scale
  - registration fields
  - county-level aggregation role
  added: '2026-08-12'
  confidence: high
  verified: true
- source: Liu, Xu & Zou (2024) RePEc record https://ideas.repec.org/a/eee/labeco/v90y2024ics0927537124001003.html
  field_scope:
  - authorship and DOI
  - Labour Economics publication identity
  - regional and entrepreneurship research context
  added: '2026-08-12'
  confidence: high
  verified: true
related_datasets:
- asif
- china-stat-yearbook
- china-economic-census
---

## Positioning in one sentence

This registry is the paper-identified administrative universe of newly registered Chinese firms, not a public web directory. Its value is county-level entry and small-firm coverage beyond ASIF; its main practical limitation is that the raw records and current ordinary-researcher access route remain restricted.

## Decision sufficiency check

For a question about local migration barriers and new business formation, this is the right asset conceptually if a controlled extract can be obtained. For production, employment, or productivity of established large industrial firms, use ASIF instead. If no approved registry access is available, stop at a documented non-reproducible design rather than replacing it with a different firm database and calling the result a replication.
