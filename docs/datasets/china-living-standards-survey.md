---
schema_version: 3
catalog_status: ready
id: china-living-standards-survey-1995-1997
name: China Living Standards Survey (CLSS/LSS), 1995-1997
aka:
- China Living Standards Survey
- China Living Standards Survey 1995-1997
- Living Standards Survey of China
- 中国生活标准调查
- Hebei-Liaoning rural living standards survey
provider: Research Center for Rural Economy (RCRE), Ministry of Agriculture, with World Bank technical assistance
china_related: true
domains:
- agriculture
- development
- labor
- migration
- land
- demography
data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: Household, household-member, and village/community survey files and documentation for the 1995-1997 CLSS/LSS study period
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: The World Bank Microdata Library has a current, free-account login route to this historical household and community microdata product. A researcher must register, accept the current confidentiality and non-redistribution conditions, and use the delivered version rather than assuming access to the AER authors' cleaned analysis file.
  barrier: File access begins only after free-account login and acceptance of the catalog conditions. The route does not establish that the download contains every original identifier or the paper's final analysis files.
unit_of_observation: Household-year/household member/village-community observation
structure: Short study-period household and community survey; do not assume a balanced panel or annual household linkage without the delivered files and documentation
geo_granularity:
- village
- county
- province
geography: Three counties in each of Hebei and Liaoning, with 31 villages after an administrative change; the sample is not nationally representative
time_span:
  start: 1995
  end: 1997
  coverage_note: Catalog metadata describes a 1995-1997 study period with household and village/community questionnaires. The 1995-1997 period is not evidence of an annual panel; confirm each wave, questionnaire date, and longitudinal identifier in the delivered files.
  last_checked: '2026-08-10'
frequency:
- low-frequency survey
- household questionnaire
- village/community questionnaire
sample_size: Approximately 880 selected farm households in 31 villages across six counties; published analyses of the AER paper commonly report about 787 analytic farm households, so selected and analyzed samples must remain distinct
key_variables:
- Household demographics and family composition
- Schooling, employment, and labor allocation
- Migration and off-farm work
- Remittances and other income
- Farmland, agricultural management, inputs, and crop production
- Housing and durable goods
- Consumption
- Credit and savings
- Village labor migration, land institutions, and local conditions
- Prices and community-level context where supplied by the release
research_fit:
  best_for:
  - Migration, remittances, and agricultural production decisions in mid-1990s rural China
  - Household labor allocation, off-farm employment, land use, and rural living-standard mechanisms
  - Short-period comparisons between sampled counties and villages in Hebei and Liaoning
  choose_over:
  - Choose this survey when the research question needs the paper-era household and village questionnaires behind the 1999 AER migration/remittance analysis, rather than a later national panel.
  - Choose NFP/RFD for a longer national rural panel with repeated household, crop, and village observations when institutional access is available; choose CFPS or CHFS when a current public household panel or broader household balance-sheet coverage matters more.
  not_good_for:
  - Nationally representative estimates for all of China
  - City-level outcomes, prefecture-wide urban panels, or long-run annual trends
  - A guaranteed balanced household panel, stable public identifiers, or a one-click public download
  needs_join_for:
  - County or province policy timing, weather, prices, transport, and market access
  - Urban destinations and migration networks beyond the sampled villages
  variation_available:
  - Cross-household and cross-village differences in migration, remittances, farm production, and labor allocation
  - Limited study-period variation documented by the survey design; exact usable time variation depends on the released questionnaires
  topics:
  - rural migration
  - remittances
  - agricultural productivity
  - household labor allocation
  - rural living standards
  - land and farm management
good_for:
- Migration and remittance effects on farm labor and crop production
- Household off-farm employment and rural income composition
- Village institutions and agricultural resource allocation in the sampled provinces
identification:
- Household and village comparisons
- Simultaneous-equation or structural household production designs, as in the AER paper
- Cross-sectional or short-period designs with clearly stated sampling limits
linkable_keys:
- Province identifier, if released
- County identifier, if released
- Village identifier, if released
- Household/member identifiers, subject to the release and confidentiality rules
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province
  - Year or study-period reference
  method: Aggregate province-year or period-level match after confirming compatible definitions
  evidence_status: plausible
- target: china-census
  relation: complement
  keys:
  - County or province
  - Census year
  method: Geographic aggregate match; do not infer household-level linkage
  evidence_status: plausible
- target: rfd
  relation: often-confused-with
  keys: []
  method: Do not merge records merely because both are RCRE rural surveys; compare questionnaire, sampling frame, years, and identifiers first
  evidence_status: verified
access_routes:
- route: World Bank Microdata Library
  access_status: registered download route; current login gate verified
  direct_url: https://microdata.worldbank.org/catalog/409/get-microdata
  requirements: Register or log in to a free World Bank Microdata Library account, then accept the current confidentiality declaration and study-specific terms before accessing files.
  steps:
  - Open the World Bank study record and select Get Microdata.
  - Register or log in to the free account shown by the current gate.
  - Read and accept the confidentiality declaration and study conditions; do not pass downloaded files to third parties or use them commercially.
  - Download only the permitted household/community files and documentation, then reconcile their sample and variable definitions with the paper-specific sample.
  deliverable: Permitted CLSS/LSS microdata and documentation after account login and acceptance of conditions; the exact downloaded file inventory remains version- and account-session-specific.
  cost: registration
  last_checked: '2026-09-28'
  caveat: The public catalog proves a current login-based acquisition path, not that the delivered files reproduce the AER authors' cleaned sample or preserve every identifier.
- route: FAO microdata catalog
  access_status: metadata mirror; redirects to the World Bank login-based acquisition route
  direct_url: https://microdata.fao.org/index.php/catalog/1533
  requirements: Use the linked World Bank route for data acquisition; review the current file-level license and account conditions there.
  steps:
  - Open the study record and review the household and village/community questionnaire descriptions.
  - Follow the linked World Bank login route and download only files permitted under its current terms.
  - Preserve the catalog version, documentation, and access decision with the research project.
  - Validate the geography, sample, questionnaire date, and identifier structure before attempting joins.
  deliverable: Metadata/documentation; the linked World Bank catalog supplies the registered acquisition route for permitted files
  cost: registration
  last_checked: '2026-09-28'
  caveat: This mirror adds no separate file route and does not establish the AER authors' cleaned sample.
access:
  url: https://microdata.worldbank.org/catalog/409/get-microdata
  cost: registration
  license: "World Bank study conditions: confidentiality declaration; within-organization use; no third-party transfer, resale, or commercial use; citation required"
  format:
  - unknown until the current catalog deliverable is inspected
  api: false
  how_to_get: Open the World Bank Get Microdata route, register or log in to the free account, accept the current confidentiality declaration and study conditions, then obtain only the permitted files and documentation. Preserve the download date and delivered inventory; do not equate them with the AER authors' cleaned analysis file.
production:
  raw_sources:
  - name: CLSS/LSS household and village/community questionnaires and metadata
    source_type: survey
    role: Provider-collected raw survey materials and documentation underlying the household, member, and community observations
    access_route: World Bank Microdata Library login route, subject to the current confidentiality declaration and study permissions
    url: https://microdata.worldbank.org/catalog/409/get-microdata
    coverage: Three counties in each of Hebei and Liaoning; 31 villages after an administrative change; study period 1995-1997
    last_checked: '2026-09-28'
  acquisition_methods:
    - Free World Bank Microdata Library account login and acceptance of study terms
    - Download of permitted files and documentation
    - Manual verification of sample and questionnaire metadata
  sample_construction: The catalog reports a field survey covering selected counties and villages rather than a nationally representative probability sample. The exact household selection and the distinction between the approximately 880 selected households and paper-specific analytic samples must be read from the questionnaire and study documentation.
  pipeline_stages:
  - stage: collect
    inputs:
    - Household questionnaire
    - Household-member questionnaire
    - Village/community questionnaire
    method: RCRE field survey with World Bank technical assistance; use the catalog documentation to identify the released files and collection dates.
    tools:
    - Catalog documentation
    output: Provider-collected household, member, and community observations, if access is granted
    evidence: IHSN and FAO catalog study metadata
  - stage: validate
    inputs:
    - Delivered survey files
    - Catalog documentation
    - Rozelle, Taylor & deBrauw (1999) sample description
    method: Reconcile geography, questionnaire dates, selected sample, analytic sample, identifiers, and variable definitions before constructing a panel or joining external data.
    tools:
    - Codebook and tabular checks
    output: A documented version-specific sample and variable map with unresolved access or linkage limits
    evidence: Catalog metadata and the paper-specific use recorded below
  constructed_variables: []
  validation:
  - Confirm the six-county, 31-village geography and questionnaire dates from the delivered documentation
  - Keep selected-household and analytic-household counts separate
  - Check whether identifiers support within-household, village, or cross-period linkage
  - Audit missingness, non-random sampling, and any administrative-boundary change before interpreting differences
  output:
    unit_of_observation: Household, household member, or village/community observation
    structure: Version-specific survey files; panel structure is not assumed
    geography: Sampled villages in Hebei and Liaoning
    time_span: 1995-1997 study period, subject to wave-level confirmation
    key_variables:
    - Migration and off-farm work
    - Remittances and income
    - Farm land, inputs, and output
    - Household demographics and living standards
    formats:
    - Catalog-dependent microdata and documentation
  reproducibility:
    level: medium
    starting_point: World Bank Microdata Library study record and Get Microdata login route
    code_available: false
    code_url:
    requirements:
    - Free World Bank Microdata Library account
    - Acceptance of the confidentiality declaration and study conditions
    - Codebook and questionnaire documentation
    - Version-specific cleaning and sample reconciliation
    blockers:
    - The paper's analytic sample and the catalog's selected sample are not identical
    - Public identifiers and cross-period linkage must be verified
  compliance:
    terms_or_license: The current World Bank route requires login and a confidentiality declaration; use is within the receiving organization, with no third-party transfer, resale, or commercial use, and with required citation.
    robots_or_rate_limits: Use the catalog normally; do not automate around access controls.
    personal_or_sensitive_data: Household and individual records may be confidential; do not expose identifiers.
    redistribution: Do not redistribute files unless the catalog license explicitly permits it.
    review_needed: Recheck the current account gate, delivered file inventory, terms, sample, and identifier restrictions before each new project.
caveats: This is a geographically narrow, historically collected survey, not a national panel. The approximately 880 selected farm households and the approximately 787 households reported in analyses of the 1999 AER paper describe different boundaries. Do not substitute the National Rural Fixed Point Survey, the later National Rural Survey, or a paper's cleaned analysis file for the CLSS/LSS identity without evidence.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'
used_by:
- cite: 'Rozelle, Taylor & deBrauw (1999), Migration, Remittances, and Agricultural Productivity in China'
  doi: https://doi.org/10.1257/aer.89.2.287
  journal: AER
  year: 1999
  dataset_role: Household and village survey for migration, remittances, farm labor, and agricultural production analysis
  evidence_type: data_catalog_and_paper
  evidence_url: https://www.aeaweb.org/articles?id=10.1257%2Faer.89.2.287
  data_note: The IHSN and FAO catalog records identify the CLSS/LSS 1995-1997 study in Hebei and Liaoning with 31 villages and approximately 880 selected farm households. Secondary descriptions of the AER analysis report about 787 analytic households. Preserve this selected-versus-analyzed distinction and do not treat the catalog as proof that the exact AER cleaned file is public.
provenance:
- source: https://catalog.ihsn.org/catalog/298
  field_scope:
  - identity
  - provider
  - geography
  - sample
  - variables
  - access route
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://microdata.fao.org/index.php/catalog/1533
  field_scope:
  - identity
  - geography
  - sample
  - variables
  - access route
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://www.aeaweb.org/articles?id=10.1257%2Faer.89.2.287
  field_scope:
  - paper identity
  - journal
  - DOI
  - paper use
  added: '2026-08-10'
  confidence: high
  verified: true
- source: https://microdata.worldbank.org/catalog/409/get-microdata
  field_scope:
  - current acquisition route
  - login requirement
  - cost
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://microdata.worldbank.org/index.php/catalog/409
  field_scope:
  - provider
  - identity
  - coverage
  - collection and processing dates
  - current access conditions
  - join keys
  added: '2026-09-28'
  confidence: high
  verified: true
related_datasets:
- id: rfd
  relation: often-confused-with
- id: china-census
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

CLSS/LSS is a historically collected household and village survey from selected counties in Hebei and Liaoning, valuable for understanding the migration-remittance-agricultural production mechanism studied in the 1999 AER paper. It is currently obtainable through the World Bank Microdata Library after free-account login and acceptance of its confidentiality conditions; its narrow, non-national sample and non-transferable access remain part of the dataset identity.

## Select rules

Prioritize it when the question is close to the AER paper's mid-1990s rural household mechanism and the sampled provinces are substantively appropriate. Switch to NFP/RFD, CFPS, or another survey when national coverage, a longer panel, or a clearer public acquisition route is required. Do not use the catalog record alone to claim a nationally representative sample or a reproducible copy of the paper's cleaned file.

## Get recipe

Open the World Bank study's Get Microdata page, register or log in to its free account, and accept the current confidentiality declaration and study conditions. Download only the permitted household/community files and documentation, then read the codebook before analysis. Reconcile the six-county/31-village geography and questionnaire dates, and record the delivered sample separately from the AER analytic sample. Do not transfer files to third parties, use them commercially, or assume the delivered files are the AER authors' cleaned analysis file.

## Connections and Limitations

Province and county joins may support aggregate context, but household-level linkage to censuses, yearbooks, weather, prices, or city data is not established by the catalog record. A village identifier may be absent, masked, or version-specific. The survey's non-random, geographically narrow design and the difference between selected and analyzed households limit national inference and make sample reconciliation a required first step.

## Decision sufficiency check

From this record alone, an agent can choose CLSS/LSS for the specific mid-1990s migration/remittance/farm-production mechanism, reject it for national or long-panel questions, obtain the permitted source files through a concrete free-account route, and state why exact paper-file reproducibility remains conditional.
