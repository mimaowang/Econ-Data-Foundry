---
schema_version: 3
catalog_status: grounding
id: china-fujian-vat-invoice-transactions
name: Fujian firm-level VAT invoice transaction data (福建省企业增值税发票数据; tax-authority Golden-Tax family; Wang, Liang, Zhang & Chen 2026 CWE)
aka:
- 福建增值税发票数据
- 福建省企业增值税发票数据
- Fujian VAT invoice data
- 企业间贸易数据库 (firm-pair trade database)
provider: >-
  Fujian provincial tax authority invoice records (增值税发票, the Golden-Tax
  金税 family); the authors' research line accesses these records through
  research cooperation. The CWE 2026 paper (Wang, Liang, Zhang & Chen,
  10.1111/cwe.70026) uses firm-level VAT transaction data from Fujian
  province; a 2017 UIBE seminar abstract by the same research line
  (梁若冰) documents the 2008-2016 福建省企业增值税发票数据 construction of a
  firm-pair trade database.
china_related: true
domains:
- trade
- firm
- tax
- regional
- culture
- transport

data_pathway:
  mode: inaccessible
  origin: ready-made
  target_artifact: >-
    Paper-specific firm-level inter-firm trade records constructed from Fujian
    VAT invoices (firm-pair transactions; the seminar abstract documents a
    2008-2016 construction); the CWE 2026 paper's exact window, fields, and
    sample are unread (Wiley full text 403 for automated clients).
  availability: restricted
  ordinary_researcher_feasible: false
  summary: >-
    The paper (Wang, Liang, Zhang & Chen 2026, China & World Economy
    34(3):38-76, DOI 10.1111/cwe.70026) studies how culture (dialect/surname)
    and transport infrastructure shape inter-firm trade using firm-level value
    added tax transaction data from Fujian province. The source is tax-authority
    invoice records (Golden-Tax family) accessed by the authors' research line
    (Ruobing Liang 梁若冰, XMU - faculty page read in full); a 2017 UIBE seminar
    abstract (read in full) documents the construction of a 2008-2016 firm-pair
    trade database from Fujian VAT invoice data. No public route exists; the
    record documents the restricted boundary and the paper's identity.
  barrier: >-
    Tax-authority invoice data are confidential; access is via research
    cooperation with the tax authority, no public or application route is
    evidenced.

unit_of_observation: Firm-to-firm transaction (inter-firm trade edge derived from VAT invoices; paper-level unit unread)
structure: Paper-specific firm-pair trade records / panel (structure unread; the seminar abstract names a firm-pair trade database)
geo_granularity:
- firm
- province (Fujian)
geography: Fujian province, China (firm level)
time_span:
  start: '2008'
  end: '2016'
  last_confirmed_release: null
  coverage_note: >-
    The 2008-2016 window is documented in the 2017 UIBE seminar abstract of the
    same research line (梁若冰); the CWE 2026 paper's own invoice window is
    UNREAD - do not treat 2008-2016 as the published paper's window.
  last_checked: '2026-08-15'
frequency:
- transaction-level (unread)
sample_size: unknown (paper-level sample unread)
key_variables:
- Firm-pair trade (inter-firm transactions from VAT invoices; seminar abstract)
- Culture measures (dialect/surname) and transport-infrastructure measures (paper abstract; construction unread)
- Exact invoice fields, firm identifiers, and cleaning steps unread

research_fit:
  best_for:
  - Understanding what Fujian VAT-invoice-based inter-firm trade research contains and why ordinary researchers cannot obtain the data
  - Routing researchers to the restricted boundary before designing trade-network studies that would need such data
  choose_over:
  - Do not route researchers to this asset; prefer obtainable trade/flow layers (china-city-to-city-truck-flows openICPSR release, customs data via china-customs, or regional IO tables) unless a tax-authority cooperation already exists
  not_good_for:
  - Any research design needing Fujian VAT invoice records without an existing tax-authority cooperation (no public route)
  - Replication or extension of the paper (no release, data section unread)
  - Provinces other than Fujian (the invoice records are Fujian-specific)
  needs_join_for:
  - Firm registry/characteristics (see china-firm-registry) for firm-level controls
  - Dialect/surname and transport-infrastructure data used by the paper (construction unread)
  variation_available:
  - Firm-pair and region variation within Fujian (paper abstract; design details belong to Econ-Variation)
  topics:
  - VAT invoices
  - inter-firm trade
  - trade networks
  - culture and trade
  - transport infrastructure
  - Fujian

good_for:
- Documenting the restricted boundary of Fujian VAT-invoice trade data
identification: []
linkable_keys:
- Firm identifiers (unread; tax-invoice-based identifiers likely not public)

joins:
- target: china-firm-registry
  relation: complement
  keys:
  - Firm identity (name/unified code)
  method: Firm-level controls and registry joins would need the paper's invoice-side identifiers, which are unread and not public.
  evidence_status: plausible

access_routes:
- route: Tax-authority research cooperation (the route the authors' line uses)
  access_status: by-application
  direct_url: needs-verification
  requirements:
  - Research cooperation with the Fujian tax authority (no public application form evidenced)
  steps:
  - Approach the tax authority through institutional channels; expect strict confidentiality and non-disclosure terms.
  deliverable: Paper-specific invoice-derived trade records (exact deliverable unread)
  cost: by-application
  last_checked: '2026-08-15'
  caveat: No public route; the CWE full text (Wiley) is 403 for automated clients and the paper's exact window is unread.

access:
  url: needs-verification
  cost: by-application
  license: Confidential tax data; terms unread
  format: []
  api: false
  how_to_get: Tax-authority research cooperation only; no public route evidenced.
caveats:
- Provider identity (Fujian tax authority, Golden-Tax invoice family) is grounded in the Crossref abstract ("firm-level value-added tax transaction data from Fujian province") plus the XMU faculty page and 2017 UIBE seminar abstract of the same research line (read in full in an earlier pass).
- The 2008-2016 window comes from the 2017 seminar abstract (same research line), NOT from the CWE 2026 paper - the paper's own invoice window is unread (Wiley 403, failed_tasks 2026-08-15).
- A minor spelling variance between Crossref ("Xianmeng Chen") and the XMU faculty page ("Xiaomeng Chen") was retained unadjudicated in the candidate ledger.

production:
  raw_sources:
  - name: Fujian provincial VAT invoice records (Golden-Tax family)
    source_type: dataset
    role: Raw inter-firm transaction records
    access_route: Tax-authority cooperation; not public
    url: needs-verification
    coverage: Fujian province; 2008-2016 per the seminar abstract (paper window unread)
    last_checked: '2026-08-15'
  acquisition_methods:
  - vendor/government cooperation (paper-side)
  sample_construction: unknown (data section unread)
  pipeline_stages: []
  constructed_variables: []
  validation: []
  output:
    unit_of_observation: Firm-pair trade records (per seminar abstract)
    structure: Firm-pair trade database (seminar abstract)
    geography: Fujian, China
    time_span: 2008-2016 (seminar abstract; paper window unread)
    key_variables: []
    formats: []
  reproducibility:
    level: not-reproducible
    starting_point: none (confidential)
    code_available: false
    code_url: ''
    requirements: []
    blockers:
    - Confidential tax-invoice data; no release, no public route
  compliance:
    terms_or_license: Confidential tax data; terms unread
    robots_or_rate_limits: n/a
    personal_or_sensitive_data: Firm-level invoice records; confidentiality constraints
    redistribution: Not permitted
    review_needed: true

quality:
  profile_status: needs-verification
  access_status: blocked
  paper_use_status: grounded
  last_audited: '2026-08-15'

used_by:
- cite: 'Wang, Liang, Zhang & Chen (2026). Culture, transport infrastructure and inter-firm trade in Fujian, China & World Economy 34(3): 38-76'
  doi: 10.1111/cwe.70026
  journal: China & World Economy
  year: 2026
  dataset_role: Main data - firm-level value-added tax transaction data from Fujian province (inter-firm trade; culture and transport-infrastructure analysis)
  evidence_type: abstract-only
  evidence_url: https://doi.org/10.1111/cwe.70026
  data_note: >-
    Crossref abstract (read 2026-08-15): firm-level VAT transaction data from
    Fujian; culture (dialect/surname) and transport infrastructure shape
    inter-firm trade. Wiley full text 403 for automated clients (failed_tasks);
    the paper's own data section, invoice window, and fields are unread.
- cite: UIBE seminar abstract (2017-06-01) of the Ruobing Liang research line - 利用2008-2016年福建省企业增值税发票数据构建了企业间贸易数据库
  doi: ''
  journal: seminar abstract
  year: 2017
  dataset_role: Construction evidence for the same research line's Fujian VAT firm-pair trade database (2008-2016)
  evidence_type: data-section
  evidence_url: needs-verification
  data_note: >-
    The UIBE seminar abstract (read in full in an earlier pass, recorded in the
    candidate ledger) documents the construction of a firm-pair trade database
    from 2008-2016 Fujian VAT invoice data. It evidences the research line's
    data access, not the CWE 2026 paper's own window.

provenance:
- source: Crossref record 10.1111/cwe.70026 (abstract, read 2026-08-15)
  field_scope:
  - provider type (Fujian firm-level VAT transaction data)
  - paper use (culture/transport and inter-firm trade)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: XMU faculty page of Ruobing Liang (read in full, earlier pass) and UIBE seminar abstract (2017-06-01, read in full, earlier pass)
  field_scope:
  - research line identity
  - Fujian VAT invoice data access and 2008-2016 construction
  added: '2026-08-15'
  confidence: med
  verified: true
- source: Wiley full text (403 for automated clients; failed_tasks 2026-08-15)
  field_scope:
  - paper's own invoice window, fields, sample
  added: '2026-08-15'
  confidence: low
  verified: false

related_datasets:
- id: china-firm-registry
  relation: complement
---

## Positioning in one sentence

Fujian firm-level VAT invoice transaction data (Wang, Liang, Zhang & Chen 2026 CWE) are confidential tax-authority records reachable only through a research cooperation with the Fujian tax authority - no public route exists, the paper's own invoice window is unread, and the 2008-2016 construction window is documented only in a 2017 seminar abstract of the same research line.

## Select rules

- Use this record to understand the restricted boundary of Fujian VAT-invoice trade data and to route researchers away from false expectations.
- For obtainable trade/flow layers, prefer china-city-to-city-truck-flows (openICPSR CC BY), china-customs, or regional IO tables.
- The invoice window question: treat the 2008-2016 seminar-abstract window as evidence about the research line's construction, not as the CWE 2026 paper's window.

## Get recipe

1. There is no public recipe: the only evidenced route is a research cooperation with the Fujian tax authority (no application form documented).
2. For the paper's own claims, read the Crossref abstract (free); the full text (Wiley) requires a human browser or library access to resolve the paper's exact invoice window and fields.
3. For research needs, prefer the obtainable trade/flow layers listed above.

## Connections and Limitations

The asset is a firm-level inter-firm trade layer from Fujian VAT invoices; firm identifiers are tax-invoice-based and not public, so registry joins (china-firm-registry) are only plausible at the design level. The paper's own data section is unread (Wiley 403), the published window is unknown, and no release exists. Design and identification details belong to the Econ-Variation repository.
