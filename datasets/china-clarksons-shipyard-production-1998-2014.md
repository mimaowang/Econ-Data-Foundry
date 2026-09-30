---
schema_version: 3
catalog_status: grounding
id: china-clarksons-shipyard-production-1998-2014
name: Clarksons Research Shipyard Quarterly Production Data (1998 Q1–2014 Q1)
aka:
- Clarksons shipyard production data
- Shipyard Quarterly Production Data 1998-2014
- Clarksons Research shipyard panel
provider: Clarksons Research (United Kingdom)
china_related: true
domains:
- industrialization
- regional
- urban
- firm
- international-trade
- productivity

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: Quarterly shipyard-level production panel for ocean-transport shipyards, with orders, deliveries, and backlog by ship type measured in Compensated Gross Tons (CGT); the ReStud paper uses the Chinese, Japanese, and South Korean subset and links Chinese yards to NBS manufacturing-firm records.
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    The paper identifies a distinct commercial Clarksons product rather than a public table or a generic shipping statistic. The official manuscript names the product, its source window, observation level, and core fields, while the public Zenodo package says the Clarksons inputs are proprietary and must be obtained separately. A current provider subscription/contact route exists, but the academic price, historical export, and permission to redistribute a research extract are not confirmed.
  barrier: >-
    The underlying historical panel is subscription data. The paper's replication package releases code and non-confidential auxiliary files, not the shipyard observations; current Clarksons terms restrict copying, extraction, and redistribution without permission. A researcher must obtain a written quote and rights decision for the exact 1998 Q1–2014 Q1 product before treating the data as reproducible.

unit_of_observation: Shipyard–quarter–ship type record
structure: panel
geo_granularity:
- shipyard
- city
- province
- country
geography: Worldwide ocean-transport shipyards in the Clarksons source; the paper's empirical panel focuses on Chinese, Japanese, and South Korean yards, with Chinese location and ownership fields supplied by the separate NBS manufacturing-firm source.
time_span:
  start: '1998-Q1'
  end: '2014-Q1'
  last_confirmed_release: '2015 source edition cited in the paper'
  coverage_note: >-
    Clarksons data are described as covering all worldwide ocean-transport shipyards from 1998 Q1 through 2014 Q1. The merged quarterly panel used for estimation is described as 1998–2013 because the NBS annual firm component ends in 2013; the 2010 NBS gap affects construction of 2009–2010 investment, not the Clarksons production observations. The full yard count, missing-yard rules, and historical version metadata are not public.
  last_checked: '2026-08-12'
frequency:
- quarterly
sample_size: >-
  Full commercial yard count is not released. The paper's summary tables report more than 10,000 yard-quarter observations across the ship types, but this does not identify the complete provider file size.
key_variables:
- Orders by ship type, measured in CGT
- Deliveries by ship type, measured in CGT
- Backlog (undelivered orders under construction) by ship type, measured in CGT
- Shipyard identity and production characteristics as supplied by the provider extract
- Ship type categories including dry bulk carriers, tankers, and containerships
- Separate quarterly global prices per CGT and steel ship-plate prices used by the paper, not part of this shipyard-panel identity

research_fit:
  best_for:
  - Regional or urban research on shipyard entry, production capacity, delivery and backlog dynamics, and industrial concentration when physical ship output by yard and quarter matters.
  - Comparing Chinese yards with Japan and South Korea while preserving the paper's ship-type market split and CGT measurement.
  - Linking industrial production to Chinese city/province location and ownership after obtaining the separate NBS firm extract.
  choose_over:
  - Choose this over ASIF when the question needs physical ship orders, deliveries, backlog, or ship-type production at quarterly frequency.
  - Choose ASIF or the Second Industrial Survey for broader manufacturing financial and employment coverage; they do not replace the Clarksons production fields.
  - Use the public Zenodo package for code and workflow inspection, not as a substitute for the proprietary yard panel.
  not_good_for:
  - A free public shipyard database, a current post-2014 production panel, or a complete China-wide firm census.
  - Household, labor, or city-welfare outcomes without separate outcome data and a documented geographic join.
  - Assuming that visible Clarksons SIN tables or a current product label are identical to the historical paper extract.
  needs_join_for:
  - Chinese city/province, ownership, fixed assets, and investment require the paper's separate NBS manufacturing-firm data and its firm-linking rules.
  - Price-demand or cost analyses require the paper's separate Clarksons aggregate price series and steel-plate price source.
  - Local employment, population, or urban outcomes require an external city or firm dataset with compatible boundary and year definitions.
  variation_available:
  - Orders, deliveries, backlog, ship type, and location/ownership differences are observed data dimensions; no policy assignment or causal variation is catalogued here.
  topics:
  - shipbuilding
  - industrial policy
  - firm entry and exit
  - regional production
  - urban industrial geography
  - international competition

good_for:
- Measuring quarterly physical production and capacity dynamics of ocean-transport shipyards.
- Studying the location, ownership, entry, and production scale of Chinese shipyards relative to nearby competitors.
- Reconstructing the data boundary of the 2025 ReStud shipbuilding application when the proprietary source can be licensed.
identification:
- Descriptive and structural production/entry comparisons using the paper's documented data; causal or policy interpretation requires a separate research design.
linkable_keys:
- Clarksons shipyard identifier, if included in the licensed extract
- Shipyard name and normalized location
- Chinese province/city and ownership fields from the linked NBS extract
- Quarter and ship type

joins:
  - target: asif
    relation: complement
    keys:
    - Shipyard or firm name
    - Province/city
    - Year
    method: >-
      Reproduce the paper's documented firm-linking logic only after obtaining both products. Do not match by name alone; preserve ownership, city boundaries, missing years, and the fact that ASIF/NBS is annual while Clarksons is quarterly.
    evidence_status: literature-used

access_routes:
  - route: Clarksons Research subscription or provider contact
    access_status: needs-verification
    direct_url: https://www.clarksons.net/portal/
    requirements:
    - Ask Clarksons Research for the historical Shipyard Quarterly Production Data 1998 Q1–2014 Q1 or an explicitly equivalent product.
    - Obtain a written quote, field list, historical version, export format, academic-use terms, and permission status for derived variables and redistribution.
    steps:
    - Contact the provider through the official portal and name the paper-cited product and exact source window.
    - Confirm whether orders, deliveries, backlog, ship type, yard identifiers, and historical location fields are included.
    - Record the approved extract and restrictions before joining it to NBS or publishing any derivative.
    deliverable: A licensed historical shipyard panel or a written refusal/alternative route; no public download is established.
    cost: paid
    last_checked: '2026-08-12'
    caveat: Current provider terms establish subscription and reuse restrictions but do not establish an academic price, guaranteed historical availability, or redistribution rights.
  - route: ReStud Zenodo replication package (workflow only)
    access_status: available-with-conditions
    direct_url: https://zenodo.org/records/14083198
    requirements:
    - Download the package and read its README and current license metadata.
    - Obtain the Clarksons and NBS inputs independently for substantive reproduction.
    steps:
    - Inspect the README, code, and non-confidential auxiliary files to identify the expected proprietary inputs.
    - Use the package to understand variable construction and output checks, while keeping missing provider files explicit.
    deliverable: Public code and non-confidential auxiliary files; not the Clarksons yard observations or the paper's confidential matched panel.
    cost: free
    last_checked: '2026-08-12'
    caveat: Zenodo access does not turn proprietary Clarksons or NBS data into a public or redistributable dataset.

access:
  url: https://zenodo.org/records/14083198
  cost: mixed
  license: The code/package license and Clarksons provider terms must be checked separately; no redistribution permission for the historical yard observations is inferred.
  format:
  - unknown proprietary export
  - code
  - auxiliary files
  api: false
  how_to_get: Start with the Zenodo README to understand the paper's missing inputs, then request the exact historical product from Clarksons Research and obtain written use terms before analysis.
caveats:
- The public replication package is a workflow and documentation route, not the underlying shipyard panel.
- The source covers worldwide shipyards, but the paper's regional comparison is limited to China, Japan, and South Korea; do not generalize to every country or to post-2014 production.
- Chinese province/city and ownership fields come from the separate NBS manufacturing database, not from this Clarksons identity.
- The paper also uses aggregate Clarksons price series and steel-plate prices; those inputs should not be silently folded into this product.
- Provider access, historical version, missing-yard treatment, identifiers, export format, and redistribution terms remain conditional until Clarksons responds.

quality:
  profile_status: verified
  access_status: needs-verification
  paper_use_status: verified
  last_audited: '2026-08-12'

used_by:
  - cite: 'Barwick, Kalouptsidi & Zahur (2025), Industrial Policy Implementation: Empirical Evidence from China''s Shipbuilding Industry'
    doi: https://doi.org/10.1093/restud/rdaf011
    journal: Review of Economic Studies
    year: 2025
    dataset_role: Main quarterly shipyard production input for orders, deliveries, backlog, entry, and market-share measures
    evidence_type: data_section_and_replication_readme
    evidence_url: https://www.restud.com/wp-content/uploads/2025/02/MS31140manuscript.pdf
    data_note: >-
      The official manuscript identifies Clarksons Research (2015) Shipyard Quarterly Production Data, covering all worldwide ocean-transport shipyards from 1998 Q1 through 2014 Q1, with orders, deliveries, and backlog by major ship type in CGT. The paper merges the Chinese subset with annual NBS manufacturing-firm data and separately uses aggregate Clarksons price series; the Zenodo README states the Clarksons and NBS inputs are proprietary and not included in the public package.

provenance:
  - source: https://www.restud.com/wp-content/uploads/2025/02/MS31140manuscript.pdf
    field_scope:
    - Clarksons product name and 2015 citation
    - 1998 Q1–2014 Q1 source window
    - shipyard-quarter unit and orders/deliveries/backlog fields
    - CGT and ship-type coverage
    - China/Japan/South Korea analysis boundary
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://zenodo.org/records/14083198
    field_scope:
    - public replication package identity
    - code/non-confidential-input boundary
    - proprietary Clarksons and NBS input statement
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: https://www.clarksons.net/portal/Terms
    field_scope:
    - current subscription and reuse restrictions
    - need for provider permission before copying or redistribution
    added: '2026-08-12'
    confidence: med
    verified: true

related_datasets:
  - id: asif
    relation: complement
---

## Positioning in one sentence

This is the paper-identified commercial quarterly shipyard production panel behind the 2025 ReStud China shipbuilding study, not a public substitute for it. Its irreplaceable value is physical orders, deliveries, and backlog by yard and ship type; its practical boundary is that the historical file must be licensed from Clarksons and joined separately to NBS firm data.

## Select rules

- Prioritize it when a regional or industrial study needs quarterly physical ship output, entry, backlog, or ship-type heterogeneity.
- Switch to ASIF or another manufacturing source when the question needs broad firm financial or employment coverage rather than shipyard production.
- Treat the Zenodo package as code and workflow documentation only. Do not advertise it as a downloadable Clarksons panel, and do not treat the policy discussion as a data record.

## Get recipe

First download the public Zenodo package and read its README to see which proprietary inputs the code expects. Then contact Clarksons Research through its official portal, request the paper-cited 1998 Q1–2014 Q1 product, and obtain a written decision on historical coverage, fields, export, academic use, and redistribution. If licensed, keep the Clarksons panel separate from the NBS annual manufacturing extract and reproduce the paper's quarter/year and firm-linking conventions before creating any city-level outcome join.

## Connections and limitations

The paper's Chinese city/province and ownership information comes from NBS, so a new user must obtain and match that separate source rather than infer location from a general Clarksons page. Quarter, ship type, yard name/identifier, and normalized Chinese location are the likely connection fields, but the licensed codebook controls the final key. A missing or non-redistributable Clarksons extract prevents a faithful replication even when the Zenodo code is public; in that case record a documented design boundary rather than substituting a current shipping table.
