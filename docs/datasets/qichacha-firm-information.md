---
schema_version: 3
catalog_status: grounding
id: qichacha-firm-information
name: Qichacha (企查查) firm information platform
aka:
- 企查查
- Qichacha
- qcc.com
- 企查查开放平台
- 企查查智能体数据平台
provider: >-
  企查查科技股份有限公司 (Qichacha Technology Co., Ltd.) - official site
  qcc.com, self-described as an 官方备案的企业征信机构 (officially filed
  enterprise-credit institution; footer ©2014-2026, fetched 200, read
  2026-08-15). Developer offerings: 企查查智能体数据平台 (agent.qcc.com,
  MCP + CLI + API key, fetched 200, read 2026-08-15); open.qichacha.com
  unresolved from this environment (DNS blocked, recorded 2026-08-15).
china_related: true
domains:
- firm
- finance
- public
- regional
- innovation

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Commercial firm-information platform data: registration/工商 records,
    litigation, penalties, ownership/relationships, credit and risk modules,
    delivered as paid API responses or subscription-based query exports.
    Official developer entry verified (agent.qcc.com): MCP and CLI share an
    API-key route for current company, risk, IP and operations responses.
    Its public data-capability page describes 185 atomic tools across six
    servers; the ordinary product is bounded entity-anchored responses, not a
    bulk historical firm panel.
  availability: restricted
  ordinary_researcher_feasible: true
  summary: >-
    Qichacha is one of the two dominant Chinese commercial firm-information
    platforms (alongside Tianyancha - see china-tianyancha-firm-information).
    Verified 2026-09-28: agent.qcc.com offers a current entity-anchored
    MCP/CLI/API-key route with enterprise, risk, IP and operations services.
    Registration supplies 500 trial credits (30 days); daily credits and
    prepaid credits are also offered (1 RMB = 10 credits), with public
    per-tool prices of 1/3/5/20 credits and an entity-month cap for many
    named-company queries. The classic open platform remains DNS-blocked from
    this environment. This makes a current bounded company lookup feasible,
    but not a licensed bulk extraction or a reproduction of a historical
    research-built city network.
  barrier: >-
    Current entity responses require an account/API key and credits. The
    published agreement prohibits unapproved automated capture, mirroring,
    bulk/continuous querying and supplying the data to third parties; it also
    limits storage/use to mainland China. Historical-archive service requires
    enterprise verification. Therefore a current query is feasible, whereas
    bulk panels, foreign access/storage, redistribution and the exact
    historical platform extracts used by papers are not ordinary routes.
  last_checked: '2026-09-28'

unit_of_observation: Company record or company-linked event returned by the selected module/API (firm grain; module-dependent)
structure: on-demand firm lookup with module-specific records
geo_granularity:
- firm registered/operating location where the module returns it
- province/city labels need endpoint-level verification
geography: Chinese firms and related entities in Qichacha's commercial database; universe completeness not established here
time_span:
  start: unknown
  end: ongoing
  last_confirmed_release: current/T+0 service claim; query-date must be retained
  coverage_note: >-
    Historical depth per module unverified; the platform's database is
    current-commercial (historical events where a module supplies them).
  last_checked: '2026-09-28'
frequency:
- on-demand query
sample_size: null
key_variables:
- Company identity fields (name, registration number, unified social credit code, status, capital, legal representative) in the selected module
- Litigation, penalty, ownership and credit/risk records where the selected module supplies them
  - Location fields after endpoint-level verification
  - Company, shareholder and outward-investment responses for a precisely identified entity, where the selected current tool returns them

research_fit:
  best_for:
  - Chinese firm identity resolution and enrichment where Qichacha's module
    coverage (registration/litigation/ownership/risk) fits and paid access is
    acceptable
  - Building bounded firm extracts from explicit identifiers with a
    documented query date
  choose_over:
  - Choose Qichacha or Tianyancha (china-tianyancha-firm-information) based
    on the specific module, price and coverage at purchase time - the two
    platforms are commercial competitors with high but unmeasured overlap;
    do not treat either as a complete census.
  - For legal-source authority or full-population coverage use the official
    registry (china-firm-registry) or released replication files.
  not_good_for:
  - Free, shareable, nationally complete firm panels
  - Reproducing another paper's historical platform snapshot (extraction
    date and cleaning are paper-side)
  - Causal treatment classification
  needs_join_for:
  - Procurement contracts (china-gov-procurement), production outcomes (asif),
    patents (china-patents) after entity resolution
  variation_available:
  - Cross-sectional firm and regional variation only
  topics:
  - firm information
  - enterprise credit
  - corporate networks
  - litigation
  - firm registry

good_for:
- firm identity resolution
- bounded firm-level extracts under a paid licence
identification: []
linkable_keys:
- Company name
- Unified social credit code
- Registration number
- Platform-specific company ID

joins:
- target: china-tianyancha-firm-information
  relation: substitute
  keys:
  - company name / unified social credit code
  method: treat as competing commercial platforms; resolve identities to official codes before any cross-platform merge
  evidence_status: plausible
- target: china-gov-procurement
  relation: complement
  keys:
  - awardee firm name / credit code
  method: entity resolution with query-date documentation
  evidence_status: plausible

access_routes:
- route: Qichacha developer platform (agent.qcc.com 智能体数据平台)
  access_status: available-with-conditions
  direct_url: https://agent.qcc.com/
  requirements:
  - Phone-number account registration and API key
  - Acceptance of current user agreement
  - Available credits: 500 registration credits for 30 days, daily credits or paid credits (1 RMB = 10 credits)
  steps:
  - Register on the official developer entry and obtain an API key.
  - Use a full company name or 18-digit unified social credit code to anchor one entity; use fuzzy entity recognition only to obtain human-reviewed candidates.
  - Select a needed tool (for example company, ownership/outward-investment, risk or IP), query the anchored entity, and retain the response, tool name and query date.
  - Check the displayed per-tool credit price before a larger but still permitted query plan.
  deliverable: Current, entity-anchored API/MCP/CLI responses; the platform describes 185 atomic tools across six servers.
  cost: paid
  last_checked: '2026-09-28'
  caveat: Company-data MCP queries are capped at 100 credits per named enterprise per calendar month (20 for an individual business; 100 per executive), but entity recognition, legal/tender data and document parsing are call-priced without that cap. The agreement prohibits bulk/continuous capture, copying/mirroring, third-party supply and out-of-mainland-China storage/use. Do not use it as a bulk-download route.
- route: Qichacha web query
  access_status: available-with-conditions
  direct_url: https://www.qcc.com/
  requirements:
  - User account and applicable subscription; manual use under site terms
  steps:
  - Search firms by name/identifier for manual verification
  deliverable: manual lookup only; not a bulk dataset
  cost: mixed
  last_checked: '2026-09-28'
  caveat: The public current agreement prohibits unapproved automated capture, copying/mirroring and unreasonable bulk/continuous queries; use the developer route for bounded API queries, not web scraping.

access:
  url: https://www.qcc.com/
  cost: paid
  license: 'Current intelligent-agent agreement: entity-anchored use under account/API-key terms; no unapproved crawling, bulk capture, mirroring, third-party supply, or out-of-mainland-China storage/use'
  format:
  - JSON API responses
  - web pages
  api: true
  how_to_get: Register on the official developer platform for API-key access, anchor a company with its full name or unified social credit code, select a current tool and retain its response/tool/date metadata. Review the displayed credit price and current agreement before further queries; this is not a bulk-download route.
caveats:
- The verified route is only a current, entity-anchored response route. It is not permission to acquire a national historical bulk extract, scrape the public web product, store/use the response outside mainland China, or redistribute it.
- The provider may change tools, fields, data sources or prices; record the tool name, returned fields, query date and displayed price at use time.
- Overlap with Tianyancha is high but unmeasured; neither platform's universe completeness is established.
- City-network research has demonstrably used Qichacha investment records, but those studies clean, deduplicate and aggregate historical extracts. A current MCP response must not be represented as the paper's 2017 investment panel.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Zhang, Lin, Gu & Zeng (2024), Research on urban economic centrality in the perspectives of knowledge stocks and flows'
  doi: https://doi.org/10.1016/j.heliyon.2023.e23889
  journal: Heliyon
  year: 2024
  dataset_role: Source of Chinese company-investment records, cleaned and aggregated by the authors into 2017 inter-city investment flows for urban-network analysis
  evidence_type: paper data section
  evidence_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10784156/
  data_note: >-
    The paper's data-source section states that it retrieved Qichacha company
    investment records, including investor and recipient addresses and
    investment timestamps. The authors removed duplicate within-city
    investments, non-cash investments and outliers, leaving 617,152 inter-city
    investment activities in 2017, then aggregated flows to city pairs. This is
    a researcher-built historical network, not a provider-delivered current
    MCP response or a reproducible Qichacha bulk export.

provenance:
- source: https://www.qcc.com/ (official home, fetched 200, read 2026-08-15)
  field_scope:
  - provider identity (企查查科技股份有限公司; 官方备案的企业征信机构)
  - product family (企业信息/信用/风险; 千寻地图; MCP entry)
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://agent.qcc.com/ (企查查智能体数据平台, fetched 200, read 2026-08-15)
  field_scope:
  - official developer/API offering exists
  - MCP protocol + CLI access
  - free API-key registration
  added: '2026-08-15'
  confidence: high
  verified: true
- source: https://agent.qcc.com/data and https://agent.qcc.com/credits (read 2026-09-28)
  field_scope:
  - current MCP/CLI/API-key route, six servers and 185 atomic tools
  - entity anchoring by full company name or unified social credit code
  - public trial, daily and prepaid-credit paths; 1 RMB = 10 credits; displayed tool prices and named-entity credit caps
  - provider-stated source families and current/T+0 claim
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://agent.qcc.com/user-agreement (effective 2026-06-17; read 2026-09-28)
  field_scope:
  - account/API-key and MCP/CLI service terms
  - no unapproved automated capture, mirroring, unreasonable bulk/continuous queries, third-party supply, or out-of-mainland-China storage/use
  - historical-archive enterprise-verification boundary and mutable-service/price boundary
  added: '2026-09-28'
  confidence: high
  verified: true
- source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10784156/ (paper data section indexed 2026-09-28; direct page challenged by reCAPTCHA)
  field_scope:
  - actual Qichacha investment-record use in China urban-network research
  - returned address/timestamp fields, 2017 construction, cleaning and city-pair aggregation boundary
  added: '2026-09-28'
  confidence: medium
  verified: true
- source: https://open.qichacha.com/ (probe, DNS getaddrinfo failure, 2026-08-15)
  field_scope:
  - classic open-platform domain unresolved from this environment (blocked, not absence)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: web search leads (blog posts on 企查查开放平台 API integration)
  field_scope:
  - open-platform API family exists (secondary)
  added: '2026-08-15'
  confidence: low
  verified: false

related_datasets:
- id: china-tianyancha-firm-information
  relation: substitute
- id: china-firm-registry
  relation: complement
- id: china-gov-procurement
  relation: complement
---

## Positioning in one sentence

Qichacha is a commercial firm-information platform with a ready, current developer route: register at agent.qcc.com, obtain an API key, anchor one Chinese company by full name or unified social credit code, choose an MCP/CLI tool, and retain the response with its tool/date metadata. This route is useful for bounded current firm enrichment, not for historic bulk extracts or a paper's constructed city network.

## Select rules

- Choose Qichacha or Tianyancha on module/price/coverage at purchase time; they are competing platforms with high, unmeasured overlap.
- Use official registries (china-firm-registry) or released replication files when legal-source authority or full-population coverage matters.
- Do not present a current query as a reproduction of any paper's historical platform snapshot.

## Get recipe

1. Register on agent.qcc.com and obtain an API key; the current public offer includes 500 registration credits valid for 30 days.
2. Anchor the company with its full name or 18-digit unified social credit code, then select the one current company/risk/IP/operations tool that answers the research need.
3. Check the displayed tool price (currently 1/3/5/20 credits; 1 RMB = 10 credits for prepaid credits), run the bounded query, and retain the tool name, returned fields and query date.
4. Stop before a bulk or repeated-wide retrieval plan: the agreement prohibits that use and no public permission for a national research extract is established.

## Connections and Limitations

Cross-platform merging with Tianyancha requires resolving both to official codes (unified social credit code). Universe completeness and historical depth remain unestablished. The provider's current agreement also prevents treating the bounded response route as a bulk download, a third-party dataset, or an offshore research store. The classic open.qichacha.com domain was DNS-blocked from this environment on 2026-08-15; that is a blocked route, not proof of absence.

## Decision sufficiency check

A researcher can now choose Qichacha for a narrow present-time Chinese-firm lookup or enrichment task, state what will be returned (an entity-anchored current response), begin through a public API-key route, estimate the stated credit cost, and see the decisive compliance boundary. It remains `grounding`: the platform contract makes the route restricted, and it is not a general research-data delivery route. The same record explicitly directs broader historical panel, universe-completeness, bulk-export, redistribution and paper-replication needs elsewhere.
