---
schema_version: 3
catalog_status: ready
id: pkulaw
name: PKULaw / Beida Fabao (北大法宝 — Peking University Legal Information Database)
aka:
- 北大法宝
- 北大法律信息网
- PKULaw
- Beida Fabao
- 中国法律数据库
- China Legal Database
- Peking University Law Database
provider: Peking University Legal Information Center (北京大学法制信息中心) / Beijing Beida Yinghua Technology Co., Ltd.
china_related: true
domains:
- public
- development
- firm
- labor
- environment
data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Searchable commercial database of Chinese laws, regulations, judicial cases, government documents, and policy instruments
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: PKULaw is a commercial database of Chinese legal and regulatory documents, judicial cases, and government documents. Its current legal-regulations and judicial-cases interfaces expose document-level searching by fields such as issuer, date, status, court and case type, and show document download options. A researcher can obtain a licensed, searchable corpus within the module and contract they purchase; a narrower analytic dataset remains researcher-constructed. The service agreement makes the contract or order—not the visible website alone—the boundary of member functions and export rights.
unit_of_observation: Legal/regulatory document; judicial case; government policy instrument
structure: document-database
geo_granularity:
- National
- province
- city
- county (for local regulations and documents)
geography: All mainland China (central + all provincial and major city-level regulations)
time_span:
  start: 1949
  end: ongoing
  last_confirmed_release: 'Current search results include legal and judicial materials published in September 2026; provider interfaces checked 2026-09-28'
  coverage_note: Comprehensive coverage of national laws and regulations from 1949; provincial and local documents coverage deepens from ~1990s onward; judicial cases from ~2000 onward
  last_checked: "2026-09-28"
frequency:
- continuously-updated
sample_size: Over 2 million legal/regulatory documents (laws, regulations, judicial interpretations, local regulations, government documents); millions of judicial cases
key_variables:
- Document title
- Issuing authority and administrative level
- Document type (law / regulation / judicial interpretation / departmental rule / local regulation / government document / policy notice)
- Issue date and effective date
- Status (effective / amended / abolished)
- Full text content (searchable)
- Subject / legal area classification
- Geographic scope (national / provincial / city / county)
- Case name, court, parties, judgment date (for judicial cases)
research_fit:
  best_for:
  - Building a documented corpus of Chinese laws, regulations, cases, and government documents
  - Locating dated local and national regulatory texts by issuer, geography, subject, and document status
  - Legal and regulatory text analysis, including document classification and institutional-history research
  choose_over:
  - Choose PKULaw when you need the raw text of Chinese laws, regulations, and government documents for constructing policy variables
  - Switch to hand-collected policy data when PKULaw's coverage of a specific document type/period is incomplete
  not_good_for:
  - A ready-made coded policy, regulatory-intensity, or treatment dataset (PKULaw is a raw document source)
  - Sub-national informal rules or internal government directives not published in the database
  needs_join_for:
  - A research-specific text-derived table must be constructed and joined to another data asset by an explicitly documented geography and time key
  variation_available:
  - Document metadata vary by issuing authority, legal area, place, and issue or effective date; these are corpus dimensions, not a treatment assignment or causal-design record.
topics:
- legal and regulatory data
- policy text analysis
- regulatory reform
- institutional economics
good_for:
- Legal and regulatory text corpus construction
- Document metadata and full-text analysis
- Tracking the evolution of China's legal and regulatory framework
identification:
- >-
  PKULaw is a module-based, licensed document corpus, not the paper's
  manually coded policy-pilot dataset. Select the legal-regulations corpus
  when the research needs enactments, issuing authorities, status and
  effective dates; select the judicial-cases corpus when it needs case-level
  searchable records. A contract or order determines which modules and
  functions the member receives, so retain the subscribed module, query
  fields, date of retrieval and any permitted export format with the derived
  research corpus.
linkable_keys:
- Issuing authority name and administrative code
- Document issue date / effective date
- Geographic scope (national / province / city / county)
- Legal subject / area classification
joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - Province/city code
  - Year
  method: spatial-temporal merge
  evidence_status: literature-used
access_routes:
- route: University library subscription
  access_status: available-with-subscription
  direct_url: https://sfb.pkulaw.com/
  requirements:
  - An institutional subscription that includes the needed document modules
  - On-campus or VPN access
  steps:
  - Check if your university library subscribes to PKULaw
  - Access the legal-regulations or judicial-cases interface through the library portal or the provider's subscribed-login route
  - Search by document type, issuing authority, date range, geographic scope, and keywords
  - Export document metadata or text only when the subscribed module and contract permit it
  deliverable: Searchable document-level legal text, metadata or case records inside the licensed module; any download/export scope is contract-dependent
  cost: paid
  last_checked: "2026-09-28"
  caveat: Current provider interfaces visibly support legal-regulations and judicial-cases searches and show document-download controls. They do not independently establish a university's subscription, unlimited bulk export, a bulk API, or permission to redistribute a derived corpus.
- route: Individual subscription
  access_status: needs-verification
  direct_url: https://www.pkulaw.com/
  requirements:
  - Individual account and payment
  steps:
  - Register at www.pkulaw.com
  - Verify whether a current individual plan covers the needed modules and export rights
  - Purchase only after confirming document scope and permitted use
  deliverable: Searchable access only if a suitable current plan is offered; module scope and export rights require verification
  cost: paid
  last_checked: "2026-09-28"
access:
  url: https://sfb.pkulaw.com/
  cost: paid
  license: Commercial service. Member functions and use scope are determined by the applicable written contract, order or other agreement; do not assume bulk export, automated collection or redistribution rights.
  format:
  - html
  - pdf
  - word (selected documents)
  api: false
  how_to_get: Check whether the university or research team has the needed PKULaw module, then use the subscribed legal-regulations or judicial-cases interface. Before building a corpus, record the module, query fields, retrieval date and contract-permitted download/export scope; otherwise verify an appropriate individual or organizational plan directly with the provider.
caveats: PKULaw is a commercial product — exact coverage varies by subscription tier. Local government document coverage may be incomplete for some regions or earlier periods. Judicial case coverage is not comprehensive (not all Chinese court judgments are published). Full-text search quality for older documents may vary. Export/download limits may restrict large-scale NLP projects — check institutional license terms.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: "2026-09-28"
used_by:
- cite: 'Wang & Yang (2025), Policy Experimentation in China: The Political Economy of Policy Learning'
  doi: https://doi.org/10.1086/734873
  journal: JPE
  year: 2025
  dataset_role: Raw source for policy experiment database — 19,812 government documents from PKULaw were coded to identify 633 policy pilots
  evidence_type: paper_data_section
  evidence_url: https://doi.org/10.1086/734873
  data_note: Collected 19,812 government documents from PKULaw (北大法宝) issued 1980–2020 and manually coded them to identify 633 policy pilots across ~200 prefectures spanning social welfare, public health, environmental regulation, and public safety domains. Combined with local official career data and socioeconomic statistics to study the political economy of policy experimentation. PKULaw served as the raw document source — policy pilot variables were constructed through manual coding of document text, not a ready-made dataset.
provenance:
- source: Wang & Yang (2025) JPE paper confirming PKULaw as the source for policy document corpus construction
  added: "2026-07-12"
  confidence: high
  verified: true
- source: www.pkulaw.com confirming database scope, subscription access, and document coverage
  added: "2026-07-12"
  confidence: high
  verified: true
- source: https://sfb.pkulaw.com/
  field_scope:
  - Current legal-regulations search interface, document metadata dimensions, current materials and document-level download controls
  added: "2026-09-28"
  confidence: high
  verified: true
- source: https://sfb.pkulaw.com/case
  field_scope:
  - Current judicial-cases corpus and searchable case-field dimensions
  added: "2026-09-28"
  confidence: high
  verified: true
- source: https://login.pkulaw.com/Register/ShowClause
  field_scope:
  - Membership functions being limited by the applicable contract, order, letter or data message
  added: "2026-09-28"
  confidence: high
  verified: true
related_datasets:
- id: china-stat-yearbook
  relation: complement
---
## Positioning in one sentence
PKULaw (北大法宝) is a commercial database of Chinese laws, regulations, judicial cases, and government documents. It is a searchable document repository, not a ready-made economic indicator or policy dataset: a researcher who needs a derived analytic table must define and document that separate construction from the retrieved text.

## Select rules
- When you need primary legal/regulatory text, document metadata, or judicial cases from a licensed Chinese legal-information source
- When locating documents by issuing authority, date, region, legal area, or status
- When studying the evolution of China's legal and regulatory framework through text analysis
- PKULaw is the raw source; any narrower coded research table is a separate researcher-constructed asset
- Not a substitute for ready-made policy indicators or economic statistics

## Get recipe
1. Check whether your university library subscribes to the PKULaw modules needed for the intended document corpus
2. Access via www.pkulaw.com with institutional IP or library portal
3. Define your document search criteria: document type, issuing authority, date range, geographic scope, keywords
4. Search and review document metadata and full text
5. Extract only the metadata or text fields needed for the stated research corpus, preserving the search scope and document identifiers
6. If a derived table is needed, document its coding and validation separately from PKULaw itself
7. Export results only as permitted by the institutional licence

## Connections and Limitations
- Document metadata (issuing authority, date, geographic scope) can be matched to another dataset only after the research-specific linkage rule is stated
- Some legal domains (e.g., environmental regulation, labor, social welfare) may complement domain-specific datasets
- Not all Chinese government documents are included — internal directives, unpublished notices, and some local-level documents may be missing
- Manual coding of large document corpora is labor-intensive; NLP/LLM-based extraction methods are increasingly common
- Subscription access may limit large-scale automated text collection — check institutional terms
