---
schema_version: 3
catalog_status: ready
id: cnopendata-local-government-work-report-corpus
name: CnOpenData Chinese local government work-report text corpus
aka:
- 中国各地区政府工作报告文本数据
- CnOpenData 政府工作报告数据库
- Chinese Government Work Report Text Data
provider: CnOpenData (中国开放数据平台), which describes the product as a compiled corpus of official central, provincial and city government work reports.
china_related: true
domains:
- governance
- urban
- regional
- development
- public

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: A provider-delivered, paid corpus of report-level TXT/PDF files, distinct from a paper author's cleaned sample or constructed tone index.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CnOpenData's product page lists 9,595 Chinese government work reports:
    26 central, 1,097 provincial and 8,472
    city-level reports. The separate format counts (8,343 TXT and 129 PDF) sum to
    8,472, not 9,595; their scope is unresolved. The route lets a researcher choose and order a documented national
    text corpus without collecting thousands of local pages individually.
  barrier: >-
    It is a paid commercial product. The public product page does not establish the
    exact price, contract terms, delivery workflow, current update schedule, OCR/cleaning
    decisions, or whether a paper's author-built corpus is identical.

unit_of_observation: One central, provincial or city government work report for a stated government and report year.
structure: Annual government-report text corpus, delivered as provider-supplied TXT/PDF documents.
geo_granularity:
- central
- province
- prefecture/city
geography: China at central, provincial and city levels, as described on the provider product page.
time_span:
  start: '1979 for provincial reports; 1983 for city reports; 2000 for central reports'
  end: '2025'
  last_confirmed_release: Provider page re-read 2026-09-29; stated coverage ends in 2025.
  coverage_note: The page headline says 2000-2025; its detailed period section gives central 2000-2025, provincial 1979-2025 and city 1983-2025, varying by jurisdiction. Obtain a government-year file list when requesting a quote.
  last_checked: '2026-09-29'
frequency:
- annual
sample_size: 'Provider totals: 9,595 reports = 26 central + 1,097 provincial + 8,472 city. Its format counts total 8,472 = 8,343 TXT + 129 PDF; the page does not establish which subset those counts describe.'
key_variables:
- Full report text
- Government level
- Government/jurisdiction identity
- Report year
- Provider document format (TXT or PDF)

research_fit:
  best_for:
  - Building reproducible report-text measures of local policy focus, targets or language across Chinese cities and provinces
  - Regional, urban and development-economics research needing a documented ready-made national work-report corpus
  choose_over:
  - Choose this product over ad hoc local-site collection when broad 2000-2025 coverage and provider-supplied TXT files are worth the commercial cost.
  - Choose china-local-government-work-report-texts when the task is to reconstruct a paper-specific corpus, inspect raw official pages, or evaluate an alternative public source family.
  not_good_for:
  - Reproducing a paper's cleaned sample, release dates, dictionary or derived tone measure without that paper's data documentation
  - Inferring that every listed jurisdiction-year has identical source quality, OCR quality or text completeness
  needs_join_for:
  - City/province codes or normalized place names for panel joins to outcomes
  - A documented text-processing rule for any derived policy or sentiment measure
  variation_available:
  - Report content across governments and years; content variation is a data feature, not an identification claim.
  topics:
  - government work reports
  - local policy language
  - text analysis
  - regional development

good_for:
- National ready-made Chinese government-work-report text corpus
- City/province-year policy-language measures
identification:
- >-
  Identify this product by the CnOpenData canonical page titled 中国各地区政府工作报告文本数据,
  its three government levels and stated 9,595-document total; see time_span and sample_size for differing period/format scopes. Do not
  identify a paper's author-built corpus by this product name alone.
linkable_keys:
- Government level
- Government/jurisdiction name
- Report year

joins:
- target: china-local-government-work-report-texts
  relation: complement
  keys:
  - government level
  - jurisdiction
  - year
  method: Use this ready-made product for acquisition; use the source-family record when verifying official originals or paper-specific construction.
  evidence_status: verified
- target: china-stat-yearbook
  relation: complement
  keys:
  - city/province
  - year
  method: Normalize jurisdiction identity before a geography-year join.
  evidence_status: plausible

access_routes:
- route: CnOpenData commercial product page and purchase flow
  access_status: available
  direct_url: https://www.cnopendata.com/data/m/government-corpus/chinese-government-work-report.html
  requirements: Purchase or institutional access; verify the applicable commercial contract before download.
  steps:
  - Open the product page; request the government-year file list and format breakdown for the levels and years you need.
  - Use the page's purchase/contact flow or an institutional subscription to obtain the product.
  - After delivery, preserve the provider version, delivery date, terms, manifest and the observed government-year coverage.
  - Audit duplicates, missing government-years, file formats and text quality before constructing derived measures.
  deliverable: Paid provider-supplied corpus of TXT/PDF government work reports, not a paper's final analytical panel.
  cost: paid
  last_checked: '2026-09-28'
  caveat: The public page shows a purchase route but not a fixed public price, final contract, download format details beyond TXT/PDF, or a guarantee of paper-level equivalence.

access:
  url: https://www.cnopendata.com/data/m/government-corpus/chinese-government-work-report.html
  cost: paid
  license: Commercial product terms must be accepted and retained with the purchased version; public page terms were not independently reviewed.
  format:
  - TXT
  - PDF
  api: false
  how_to_get: Open the CnOpenData product page, confirm scope, purchase or obtain institutional access, download the supplied documents, then retain version and coverage evidence before analysis.
caveats: >-
  This is a provider-compiled corpus. The provider's counts and coverage are product
  descriptions, not an independent guarantee that every jurisdiction-year or document
  transcription is complete. OCR/text cleaning, duplicates, source-version choices and
  every paper's derived dictionary or event-date construction require a researcher audit.
  The format-count mismatch remains unresolved; equality with the city total alone
  does not prove that TXT/PDF counts describe only city reports.

production:
  raw_sources:
  - name: Official central, provincial and city government work reports
    source_type: webpage
    role: Original documents compiled into the provider corpus, according to the provider description
    access_route: CnOpenData provider product
    url: https://www.cnopendata.com/data/m/government-corpus/chinese-government-work-report.html
    coverage: 'Provider period section: central 2000-2025, provincial 1979-2025, city 1983-2025; jurisdiction coverage varies.'
    last_checked: '2026-09-29'
  acquisition_methods:
  - paid provider download
  sample_construction: Provider describes systematic compilation of official reports; its detailed collection, OCR and deduplication process is not independently documented here.
  pipeline_stages:
  - stage: collect
    inputs:
    - CnOpenData commercial corpus
    method: Purchase/access the product and retain its delivered version and manifest.
    tools:
    - browser
    output: Provider-supplied report-level TXT/PDF files
    evidence: Live CnOpenData product page
  - stage: validate
    inputs:
    - Provider-supplied files
    method: Check jurisdiction-year coverage, duplicate reports, text encoding/OCR quality and consistency with the intended panel definition.
    tools:
    - tabular/text-processing software
    output: Researcher-audited corpus or analytic sample
    evidence: Required researcher validation; not a provider promise
  constructed_variables: []
  validation:
  - Government-year completeness for the selected level and period
  - Duplicate, encoding and OCR checks
  - Place-name normalization before joins
  output:
    unit_of_observation: Government work report
    structure: Annual text corpus
    geography: Central, provincial and city China
    time_span: Varies by government level and jurisdiction; see time_span.coverage_note
    key_variables:
    - full text
    - government level and jurisdiction
    - report year
    formats:
    - TXT
    - PDF
  reproducibility:
    level: medium
    starting_point: CnOpenData product page and commercial purchase route
    code_available: false
    requirements:
    - Paid access or institutional subscription
    - A documented audit and text-processing plan
    blockers:
    - Commercial terms and price are transaction-specific
    - Provider collection/OCR decisions and paper-specific transformations are not established by the public page
  compliance:
    terms_or_license: Follow the purchased CnOpenData contract; do not assume redistribution rights for the compiled corpus.
    robots_or_rate_limits: Not applicable to the provider-delivered product; follow provider download conditions.
    personal_or_sensitive_data: Public government documents; still review delivery terms before sharing derived files.
    redistribution: Do not redistribute provider files unless the commercial agreement permits it.
    review_needed: true

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://www.cnopendata.com/data/m/government-corpus/chinese-government-work-report.html (re-read 2026-09-29)
  field_scope:
  - Provider totals, unreconciled format counts, and differing headline versus government-level period descriptions; no delivery manifest inspected.
  added: '2026-09-29'
  confidence: high
  verified: true
- source: https://www.cnopendata.com/data/m/government-corpus/chinese-government-work-report.html (live product page read 2026-09-28)
  field_scope:
  - product identity and purchase route
  - 2000-2025 scope
  - 9,595-document count and level breakdown
  - Provider-stated 8,343 TXT and 129 PDF counts; scope unresolved on the 2026-09-29 recheck
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-local-government-work-report-texts
  relation: complement
- id: china-gov-procurement
  relation: often-confused-with

---

## Positioning in one sentence

This purchasable corpus supplies Chinese central, provincial and city government work reports for policy-text research. Coverage varies by level and jurisdiction (see time_span); the delivered texts are inputs for constructing measures, not a paper's finished analytic panel.

## Select rules

- Choose it when a paid, broad national report-text corpus is preferable to collecting thousands of government pages.
- Use the source-family record to investigate official originals, alternate public collection or a paper-specific corpus.
- Treat each derived text measure as a separate, documented researcher construction.

## Get recipe

1. Request a file list for the needed government levels and years, and clarification of the 8,343 TXT / 129 PDF counts.
2. Purchase the product or use institutional access, retaining the version and contract.
3. Audit the delivered government-year files before deriving variables or joining outcomes.

## Connections and Limitations

The practical join key is government level, normalized jurisdiction and report year. The acquisition route is closed for the provider corpus, but the commercial product cannot by itself establish source-page completeness, specific event dates, or any author's text-cleaning and dictionary choices.
