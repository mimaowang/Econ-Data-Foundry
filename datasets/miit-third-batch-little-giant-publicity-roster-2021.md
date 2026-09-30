---
schema_version: 3
catalog_status: ready
id: miit-third-batch-little-giant-publicity-roster-2021
name: MIIT third-batch Little Giant enterprise publicity roster (2021)
aka:
- 第三批专精特新“小巨人”企业公示名单
- 第三批小巨人公示名单
- MIIT Little Giant third-batch publicity list
provider: Ministry of Industry and Information Technology (MIIT, 工业和信息化部), SME Bureau attachment.
china_related: true
domains:
- firm
- industrial
- innovation
- regional

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    The 63-page MIIT PDF attachment titled "第三批专精特新‘小巨人’企业公示名单":
    a numbered national roster of 2,930 proposed third-batch Little Giant
    enterprises. It is a publicity roster, not evidence that every listed firm
    was subsequently finally designated.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    The currently reachable MIIT attachment is a directly downloadable,
    text-readable national roster. Its table contains a sequence number and
    enterprise name; the final note says entries are ordered by registered
    location, but it does not provide a separate machine-readable location
    field. The record preserves this narrow, obtainable source rather than
    claiming the paper's five-batch final and geocoded data product.
  barrier: >-
    The PDF must be parsed or transcribed for tabular use. It supplies a
    proposed/publicized third-batch roster only: final-designation status,
    later name changes, identifiers, address fields and a multi-batch panel
    require separate evidence and work.

unit_of_observation: One named enterprise appearing as a numbered row in the third-batch publicity PDF.
structure: One national cross-sectional numbered roster.
geo_granularity:
- firm
geography: Mainland China; the PDF states that entries are ordered by enterprise registered location, without publishing a separate location column.
time_span:
  start: '2021'
  end: '2021'
  last_confirmed_release: MIIT attachment reachable and read on 2026-09-28
  coverage_note: The PDF has 63 pages and rows numbered 1 through 2,930. It is limited to the third-batch publicity roster.
  last_checked: '2026-09-28'
frequency:
- one-off publicity roster
sample_size: 2,930 numbered enterprise rows.
key_variables:
- Sequence number
- Enterprise name

research_fit:
  best_for:
  - Building a documented third-batch proposed-Little-Giant membership indicator from the exact public MIIT roster
  - Matching named third-batch roster firms to a separately obtained firm registry, patent source or city file after careful entity resolution
  choose_over:
  - Choose this when the required object is exactly the 2021 third-batch publicity roster and a directly obtainable source matters.
  - Use china-little-giant-enterprise-list when the question requires final designation, multiple batches, dates beyond this roster or researcher-derived geocoding; that broader asset remains grounding.
  not_good_for:
  - Identifying final third-batch awardees without a separate final-announcement source
  - Reproducing the ARS paper's five-batch, 12,950-firm geocoded sample
  - Firm identifiers, addresses, industry classifications, outcomes or a time panel
  needs_join_for:
  - A verified firm registry for unified social credit codes, address and later firm status
  - City/province identifiers if spatial aggregation is required; the PDF ordering note is not an explicit location field
  variation_available:
  - Cross-firm membership differences within this one public roster
  topics:
  - Little Giant enterprises
  - SME designation
  - industrial firms
  - firm matching

good_for:
- A reproducible firm-name roster for the 2021 third-batch publicized Little Giant list
- Documented matching of roster membership to independently sourced firm or regional data
identification:
- The roster establishes publicized proposed membership in this named batch only; it does not by itself establish a treatment, final qualification or causal comparison.
linkable_keys:
- Enterprise name
- Sequence number

joins:
- target: china-little-giant-enterprise-list
  relation: component
  keys:
  - enterprise name
  method: This is one directly obtainable third-batch publicity input to the broader multi-batch Little Giant collection; do not substitute it for final designation or geocoded output.
  evidence_status: verified
- target: china-firm-registry
  relation: complement
  keys:
  - enterprise name
  method: Resolve names cautiously to obtain identifiers and location; a PDF name match alone is not an identifier match.
  evidence_status: plausible

access_routes:
- route: Direct MIIT third-batch publicity PDF attachment
  access_status: available
  direct_url: https://www.miit.gov.cn/cms_files/filemanager/1226211233/attach/20217/71bd4daebeb44632b672b7747a36b65f.pdf
  requirements: A normal browser or PDF-capable client.
  steps:
  - Download the MIIT attachment and retain its source URL and retrieval date.
  - Confirm the title is "第三批专精特新‘小巨人’企业公示名单" before extraction.
  - Extract or transcribe the sequence-number and enterprise-name rows, preserving the original numbering.
  - Treat the output as a publicity roster; obtain a distinct final-announcement source before asserting final designation.
  deliverable: A 63-page PDF containing 2,930 numbered enterprise-name rows.
  cost: free
  last_checked: '2026-09-28'
  caveat: No structured download, identifier column, explicit location field or final-designation confirmation is established by this attachment.

access:
  url: https://www.miit.gov.cn/cms_files/filemanager/1226211233/attach/20217/71bd4daebeb44632b672b7747a36b65f.pdf
  cost: free
  license: Public government attachment; no separate reuse licence was identified in the checked PDF.
  format:
  - PDF
  api: false
  how_to_get: Download the direct MIIT PDF, verify its title, and extract its numbered enterprise-name roster while preserving the publicity-status boundary.
caveats:
- This is a publicity/proposed roster, not a verified final designation list.
- The document presents firm names and sequence numbers only; location is not a dedicated field.
- It is one batch, not the five-batch research sample used in the cited regional-science study.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: not-applicable
  last_audited: '2026-09-28'

used_by: []

provenance:
- source: https://www.miit.gov.cn/cms_files/filemanager/1226211233/attach/20217/71bd4daebeb44632b672b7747a36b65f.pdf
  field_scope:
  - direct delivery and 63-page PDF format
  - exact publicity-roster title
  - sequence-number and enterprise-name fields
  - 2,930-row boundary and registered-location ordering note
  - exclusion of final-designation, identifiers and dedicated location fields
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: china-little-giant-enterprise-list
  relation: component
- id: china-firm-registry
  relation: complement
---

## Positioning in one sentence

This is a genuinely obtainable, narrowly defined MIIT source: the 2021 third-batch *publicity* roster of 2,930 named enterprises. It can support transparent name-based matching, but it is neither a final-designation file nor the multi-batch spatial dataset used by the regional-science paper.

## Select rules

- Choose it when the research object is membership in this exact publicized third-batch roster.
- Switch to a separately verified final announcement if final qualification, not publicity, is material to the question.
- Do not use the roster alone to infer city, industry, ownership, later survival or a policy effect.

## Get recipe

1. Download the direct MIIT PDF and save the source URL and retrieval date.
2. Verify the title and retain all 2,930 original sequence numbers during extraction.
3. Match enterprise names to an independently documented registry only if identifiers or geography are needed.
4. Keep a separate final-status field empty unless a final third-batch announcement is independently verified.

## Connections and Limitations

Enterprise names can be useful matching anchors but are not stable identifiers. The document's registered-location ordering should not be reverse-engineered into an unverified city variable. Its strongest value is a reproducible, public membership roster with an explicit publicity-status boundary.

## Decision sufficiency check

A future agent can obtain the exact PDF, explain what each row is, extract the two observed fields, and know when to stop: any question needing final designation, locations or the five-batch paper sample needs another source or a documented matching step.
