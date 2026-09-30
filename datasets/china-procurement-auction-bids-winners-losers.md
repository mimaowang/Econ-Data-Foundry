---
schema_version: 3
catalog_status: ready
id: china-procurement-auction-bids-winners-losers
name: China public-procurement auction bid data with winning and losing bidders (Tang, Wang & Wu 2025 JUE; replication on Mendeley Data 10.17632/nw6tjvzk33.1)
aka:
- 政府采购中标与落标企业数据
- Local Favoritism in China's Public Procurement replication data
- 中国政府采购拍卖投标数据（含中标与落标者）
- 10.17632/nw6tjvzk33.1
provider: Researcher-constructed from China Government Procurement Network (中国政府采购网, ccgp.gov.cn, Ministry of Finance) auction announcements, matched to firm-registration data (工商注册数据) and manually collected official career data; Mendeley Data distributes the replication folder
china_related: true
domains:
- public
- firm
- political-economy
- urban
- development

data_pathway:
  mode: direct
  origin: researcher-collected
  target_artifact: "Mendeley Data dataset 10.17632/nw6tjvzk33.1 'Replication: Local Favoritism in China's Public Procurement' (2024-10-25, CC BY 4.0) - a public 82,699,020-byte ZIP containing procurement_candidate.dta (468,603,183 bytes uncompressed), procurement_city.dta, promotion.dta, summary.dta, a README, and Stata replication scripts. The README identifies procurement_candidate.dta as the final major-analysis subset that reports all qualified bidders for a subset of 2014-2020 procurement contracts."
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    The paper's bidder-level data are released under CC BY 4.0. Its author README documents Ministry of Finance CGP/ccgp.gov.cn source records from 2014-2020: about 4.5 million tender invitations and 3.6 million bidding outcomes, matched through a procurement ID and reduced to about 2.2 million transactions after observations without procuring-city information are excluded. It identifies procurement_candidate.dta as the all-qualified-bidders major-analysis subset, and also documents released city-corruption and leader-promotion files. This bidder layer remains distinct from the contract/award-level china-gov-procurement asset.
  barrier: The released ZIP and README make the paper-specific artifact directly obtainable, but original CGP collection, firm-registration matching inputs, and table columns remain separate questions. The ZIP has a 469 MB uncompressed footprint; inspect Stata labels before treating a field as an identifier or treating the major-analysis subset as all procurement bidders.

unit_of_observation: Bidder-auction participation (one row per firm per procurement auction, with win/lose outcome) - contract-level aggregates also derivable
structure: Transaction records (bidder-auction level); aggregable to auction, firm-year, city-year
geo_granularity:
- City (firm registration location vs procuring agency city - local/outside classification)
- Procurement agency (central / local government levels)
geography: All mainland China (ccgp.gov.cn national coverage; ~409K auctions)
time_span:
  start: '2014'
  end: '2020'
  last_confirmed_release: '2024-10-25'
  coverage_note: "The released replication README (updated October 2024, inspected 2026-09-28) documents original CGP inputs from 2014-2020: approximately 4.5 million tender invitations and 3.6 million bidding outcomes matched on a procurement ID, then about 2.2 million transactions after records lacking procuring-city information are excluded. procurement_candidate.dta is explicitly the all-qualified-bidders subset used for major analysis; its row count and columns were not read in this unit. Replication folder issued 2024-10-25."
  last_checked: '2026-09-28'
frequency:
- transaction-level
sample_size: ~2.2M purchases (after dropping city-level-government observations with missing info), 1,411,236 bidding firms, 409,299 procurement auctions (Xiangzhang secondary summary of the paper; consistent with the 2.2M/1.4M/409K figures in the existing used_by entry); 93.2% bidder match rate to firm registration (existing used_by entry, source not re-verified)
key_variables:
- Auction/bid outcome (win vs lose per firm per auction)
- Bidder firm identity and registration location (matched from 工商注册/enterprise registration data)
- Procuring agency and its location/level
- Contract date, budget, value, procurement type (goods/services/engineering), rebate ratio
- Firm characteristics: registered capital, firm age, ownership, industry, location (from registration data)
- Firm performance/innovation: patents (CNIPA), tax-survey TFP, violation/penalty records, procurement blacklist status (complementary sources; low match rates, treated as 0 when unmatched per secondary summary)
- Mayor career variables: age, tenure, birthplace, prior/next positions (hand-collected from Baidu Baike)

research_fit:
  best_for:
  - Local favoritism / home bias in government contract allocation - comparing winning probabilities of local vs non-local bidders within the same auction (contract fixed effects)
  - Bureaucratic career incentives and procurement allocation (mayor promotion incentives as the mechanism)
  - Auction-level competition studies where losing bidders are needed for comparison (unique layer not available in contract-only procurement data)
  choose_over:
  - Choose over china-gov-procurement (contract/award level, no losing bidders) when the design requires the full bidder set of each auction - the losing-bidder sample is this asset's distinct value
  - Choose over ccgp.gov.cn raw announcement collection when the paper's cleaned bidder-level panel and code suffice (replication folder is directly downloadable)
  not_good_for:
  - Pre-2014 procurement analysis (coverage window starts 2014 per existing entry; unverified directly)
  - Firm production/financial outcomes without matching to ASIF or tax survey data (registration data carry no operating performance)
  - Procurement outside the public tender/auction system (below-threshold or non-announced purchases)
  needs_join_for:
  - Firm productivity/performance outcomes require matching to ASIF, tax survey (税调), or patent data - the paper uses tax-survey TFP and CNIPA patents, with low match rates
  - City-level economic conditions (GDP, employment, fiscal pressure) for incentive mechanisms
  - Mayor career and promotion data (hand-collected in the paper; not a public dataset)
  variation_available:
  - Within-auction local-vs-nonlocal bidder comparisons (contract fixed effects; bidder fixed effects)
  - Cross-city variation in mayor career incentives; mayor age/tenure discontinuities
  - Auction type and competitiveness variation (open auction vs restricted; number of bidders)
  topics:
  - government procurement
  - local favoritism
  - bidding
  - political economy
  - firm-government relationships
  - China

good_for:
- Local bias in public procurement contract allocation (winners vs losers)
- Bureaucratic incentives and discretionary resource allocation
identification:
- Contract fixed effects (within-auction comparison)
- Bidder fixed effects
- Mayor-age/tenure-based incentive variation
linkable_keys:
- Bidder firm name (matched to enterprise registration; key for ASIF/patent joins)
- Procuring agency name and city
- Auction/contract date

joins:
- target: asif
  relation: complement
  keys:
  - Bidder firm name
  - Year
  method: Firm-name entity resolution to enterprise registration; the paper's own match rate is 93.2% to registration data, and tax-survey data are used for TFP (match success low; unmatched treated as zero per secondary summary)
  evidence_status: literature-used
- target: china-patents
  relation: complement
  keys:
  - Bidder firm name
  - Year
  method: CNIPA patent data joined to bidders for innovation outcomes (low match rates per secondary summary)
  evidence_status: literature-used
- target: china-gov-procurement
  relation: often-confused-with
  keys:
  - Procuring agency
  - Contract date
  method: Same raw announcement family (ccgp.gov.cn); china-gov-procurement is the contract/award level (2013-2019 Beraja et al. extraction), this asset is the bidder-auction level including losing bidders (2014-2020 per existing entry)
  evidence_status: plausible

access_routes:
- route: Mendeley Data replication folder (DOI 10.17632/nw6tjvzk33.1)
  access_status: available
  direct_url: https://data.mendeley.com/datasets/nw6tjvzk33/1
  requirements:
  - Download the single public Replication.zip (82,699,020 bytes compressed; about 469 MB uncompressed) from the current V1 Mendeley record or its public-file URL.
  - Stata 18.0 for the supplied scripts, according to the README.
  steps:
  - Open https://doi.org/10.17632/nw6tjvzk33.1 or the dataset landing page and download Replication.zip.
  - Read Replication/Readme.docx; use Replication/data/procurement_candidate.dta for the documented all-qualified-bidders major-analysis subset. procurement_city.dta is the prefecture corruption-occurrence panel; promotion.dta contains extracted mayor/party-secretary profiles.
  - Set the global root in Replication/do_files/1_master.do, then run 1_master.do for main text tables/figures and 2_appendix.do for appendix outputs.
  - Cite as TANG Wei, WANG Yuan, WU Jiameng, 'Replication: Local Favoritism in China's Public Procurement', Mendeley Data, doi:10.17632/nw6tjvzk33.1 (2024).
  deliverable: Replication.zip with four named .dta data files, two named Stata scripts, and the README. The ZIP directly contains the major-analysis all-qualified-bidders subset, but the README does not state its row count or document every column.
  cost: free
  last_checked: '2026-09-28'
  caveat: Current Mendeley API reported V1 available=true, confidential=false and CC BY 4.0, with one completed public Replication.zip. The current API route exposed a public-file download URL; no account requirement was observed in that route, although platform terms may change.
- route: Rebuild from ccgp.gov.cn public announcements
  access_status: available-with-technical-friction
  direct_url: https://www.ccgp.gov.cn/htgg/main.htm
  requirements:
  - Comply with current site terms and reasonable request rates
  - Substantial collection/parsing/normalization effort (same pipeline as china-gov-procurement, plus bidder-set extraction per auction)
  steps:
  - Query the official announcement and contract search by region, agency, date range, category
  - Extract each auction's full bidder set (winners and losers) from announcement pages
  - Match bidders to enterprise-registration data by firm name; join patents/tax/penalty sources
  - Collect mayor career data from Baidu Baike (as the paper did)
  deliverable: Researcher-built bidder-level panel; completeness depends on historical announcement availability
  cost: free
  last_checked: '2026-08-14'
  caveat: Historical batch availability and anti-automation controls apply (see china-gov-procurement); exact paper cleaning pipeline is not readable this session (ScienceDirect 403).
- route: Published JUE article and SSRN working paper (data section)
  access_status: blocked
  direct_url: https://www.sciencedirect.com/science/article/abs/pii/S009411902400086X
  requirements:
  - Library subscription (ScienceDirect) or human browser
  steps:
  - Open the article page with a library subscription or human browser and read the data section (Section 2)
  - Check the data-availability statement for any supplementary data release beyond the Mendeley folder
  deliverable: The paper's own data section (authoritative construction details); not readable by automated clients in this environment (403)
  cost: mixed
  last_checked: '2026-08-14'
  caveat: IDEAS abstract read; Xiamen University seminar page (2022-12, official) records the earlier working-paper abstract including 'winners and runners-up' and a 10% local-bid advantage; SSRN abstract pages are CAPTCHA/403-blocked here.

production:
  raw_sources:
  - name: ccgp.gov.cn procurement auction announcements (中国政府采购网)
    source_type: webpage
    role: Raw source of auction identity, bidders (winners and losers), contract date/budget/value, procurement type
    access_route: Public search on www.ccgp.gov.cn (same route as china-gov-procurement)
    url: https://www.ccgp.gov.cn/htgg/main.htm
    coverage: National, ~2013/2014 onward; completeness varies by year/region
    last_checked: '2026-08-14'
  - name: Enterprise registration data (工商注册数据)
    source_type: dataset
    role: Firm characteristics (registered capital, age, ownership, industry, location) for bidder matching
    access_route: Commercial/registration-data products (as used by the paper); exact vendor unverified
    url: needs-verification
    coverage: National firm registry (basic information only; no operating performance)
    last_checked: '2026-08-14'
  - name: Complementary firm sources (国家企业信用信息公示系统, procurement blacklist, administrative penalties, CNIPA patents, tax survey 税调)
    source_type: dataset
    role: Supplementary firm performance/conduct variables (patents, TFP, violations)
    access_route: Various; match success low per the secondary summary
    url: needs-verification
    coverage: Sparse - most bidders unmatched on these dimensions (treated as 0)
    last_checked: '2026-08-14'
  - name: Mayor career records from Baidu Baike (百度百科)
    source_type: webpage
    role: Official career variables (age, tenure, birthplace, prior/next positions) for incentive measurement
    access_route: Manual collection by the authors
    url: https://baike.baidu.com/
    coverage: Prefecture-level mayors (city-level chief officials)
    last_checked: '2026-08-14'
  acquisition_methods:
  - web collection (ccgp.gov.cn announcements)
  - API/download of registration and complementary firm data
  - manual coding (mayor career records)
  sample_construction: All procurement auctions with winning and losing bidders on ccgp.gov.cn; observations with missing city-level government info dropped (yields ~2.2M purchases); bidders matched to registration data by firm name (93.2% per existing used_by entry; not re-verified this session).
  pipeline_stages:
  - stage: collect
    inputs:
    - ccgp.gov.cn announcement pages
    method: Collect auction announcements; retain full bidder sets per auction (winners and losers), contract date, budget/value, buyer and winning-supplier names/addresses, tender type
    tools: []
    parameters: []
    output: Raw auction-bidder records
    evidence: Xiangzhang Economics secondary summary (read 2026-08-14); existing china-gov-procurement used_by entry
  - stage: match
    inputs:
    - Raw auction-bidder records
    - Enterprise registration data
    method: Match bidding firms to registration data by firm name (93.2% match rate); join patents, penalties, blacklist, tax-survey data with low success (unmatched set to 0 per secondary summary)
    tools: []
    parameters: []
    output: Bidder-level panel with firm characteristics and outcomes
    evidence: Xiangzhang secondary summary; existing used_by entry
  - stage: collect
    inputs:
    - Baidu Baike mayor pages
    method: Manually collect prefecture-level chief officials' age, tenure, birthplace, prior/next positions
    tools: []
    parameters: []
    output: Mayor career panel
    evidence: Xiangzhang secondary summary
  - stage: model
    inputs:
    - Bidder-level panel
    - Mayor career panel
    method: Within-auction local-vs-nonlocal winning-probability regressions (contract fixed effects); rebate-ratio and winner-quality regressions; mayor incentive interactions
    tools: []
    parameters: []
    output: Estimation results and tables (replication folder)
    evidence: XMU seminar abstract (2022-12); Xiangzhang secondary summary
  constructed_variables:
  - name: Local bidder indicator
    concept: Bidder's registration city equals the procuring agency's city
    source_fields:
    - Firm registration location
    - Procuring agency location
    method: City-level match of registration vs agency address
    validation: Robustness uses main-investor city, bilateral distance/time, 300km distance splits
    limitations: Subcontractor/subsidiary structures may blur local status (paper tests investor-city alternative)
  - name: Rebate ratio
    concept: Actual payment / (actual payment - contract value); higher = cheaper procurement for the government
    source_fields:
    - Actual payment
    - Contract value
    method: Computed from contract fields
    validation: Used as cost-efficiency outcome; local winners have 15% lower rebate rates (existing used_by entry)
    limitations: Depends on consistent contract-value units across regions/years
  - name: Mayor promotion incentive
    concept: Career-incentive proxies (promotion prospects, economic/fiscal pressure)
    source_fields:
    - Mayor age, tenure, career history (Baidu Baike)
    method: Hand-collected official data; incentive proxies interacted with local-bidder dummy
    validation: Mayor age around 60 (retirement) and early-tenure patterns as incentive discontinuities
    limitations: Measurement of promotion prospects is proxy-based
  validation:
  - Bidder match-rate audit (93.2% to registration data, per existing entry)
  - Robustness: investor-city definition, distance controls, auction-type splits, bidder fixed effects
  output:
    unit_of_observation: Bidder-auction participation
    structure: Transaction records with win/lose outcomes; aggregable to auction/firm-year/city-year
    geography: Mainland China (national ccgp coverage)
    time_span: 2014-2020 (per existing used_by entry; not directly re-verified)
    key_variables:
    - win/lose, bidder firm, registration location, agency, contract value/budget/date, rebate ratio, firm characteristics, mayor career vars
    formats:
    - Stata .dta data files
    - Stata .do code
    - DOCX README
  reproducibility:
    level: medium
    starting_point: Mendeley Data 10.17632/nw6tjvzk33.1 (data + code); ccgp.gov.cn public announcements for rebuild
    code_available: true
    code_url: https://data.mendeley.com/datasets/nw6tjvzk33/1
    requirements:
    - Obtain the public ZIP; reserve about 469 MB after decompression and use Stata 18.0 for the supplied scripts
    - Registration-data access is needed only to rebuild or alter the firm layer, not to use the released replication files
    - Mayor career data are paper-specific hand-collected work; promotion.dta is released, but rebuilding it remains costly
    blockers:
    - Original CGP inputs and firm-registration matching are not reconstructed merely by downloading the ZIP
    - Table columns/labels and the major-analysis subset's row count were not inspected in this unit
  compliance:
    terms_or_license: Replication folder CC BY 4.0 (DataCite rightsList); ccgp.gov.cn collection per current site terms (see china-gov-procurement); registration-data access via commercial/application route
    robots_or_rate_limits: Current public Mendeley API exposed V1 metadata and the public-file URL; do not automate bulk retrieval without observing current platform limits
    personal_or_sensitive_data: The released files include business and public-official career information; inspect the README and local legal/ethical requirements before redistributing modified extracts
    redistribution: CC BY 4.0 covers the replication folder; bulk ccgp redistribution not authorized
    review_needed: Inspect table labels and current platform terms before redistributing a modified extract or claiming coverage beyond the README's major-analysis subset

access:
  url: https://data.mendeley.com/datasets/nw6tjvzk33/1
  cost: free
  license: CC BY 4.0 (replication folder)
  format:
  - Stata .dta
  - Stata .do
  - DOCX README
  api: true
  how_to_get: Download Replication.zip from Mendeley Data V1, read Replication/Readme.docx, use data/procurement_candidate.dta for the documented major-analysis bidder subset, and run the supplied Stata 18 scripts after setting the root path. Rebuild from CGP announcements only if different coverage or reconstruction transparency is required.
caveats: The distinctive value is the all-qualified-bidders layer, which contract-level procurement data (china-gov-procurement) do not contain. The released README now directly confirms the source family, 2014-2020 raw-input window, the about-2.2M post-exclusion transaction layer, the major-analysis role of procurement_candidate.dta, the prefecture corruption file, the leader-profile file, and the executable code. It does not document the exact columns/row count of the major-analysis file, prove that its bidder subset covers every auction, or provide a standalone route to reconstruct the underlying CGP or firm-registration inputs.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: 'Tang, Wei, Yuan Wang and Jiameng Wu (2025), Local Favoritism in China''s Public Procurement: Information Frictions or Incentive Distortion?'
  doi: https://doi.org/10.1016/j.jue.2024.103716
  journal: Journal of Urban Economics
  year: 2025
  dataset_role: Main data - bidder-level dataset of Chinese public procurement auctions including winning AND losing bidders; local bias in contract allocation (local bidders ~10% more likely to win), cost and winner-quality outcomes, mayor career-incentive mechanisms
  evidence_type: replication_readme
  evidence_url: https://data.mendeley.com/datasets/nw6tjvzk33/1
  data_note: "The current public V1 Replication.zip and its author README were inspected 2026-09-28. The README names the paper, says it describes and replicates its main and appendix results, identifies procurement_candidate.dta as the all-qualified-bidders major-analysis subset, documents the 2014-2020 CGP raw-input window and about-2.2M post-exclusion transaction layer, and identifies released city-corruption and leader-promotion files plus two Stata 18 scripts. Xiangzhang's secondary summary remains the source for the 1,411,236-firm, 409,299-auction, and 93.2% match-rate claims; those numbers were not independently rechecked here."

provenance:
- source: Xiangzhang Economics (香樟经济学术圈) blog post '政府采购中的本地偏好' (cec.blog.caixin.com/archives/279294), read in full 2026-08-14
  field_scope:
  - construction source (ccgp.gov.cn)
  - sample size (2.2M purchases, 1,411,236 bidders, 409,299 auctions)
  - firm matching and complementary sources
  - mayor career data collection
  added: '2026-08-14'
  confidence: med
  verified: false
- source: Xiamen University 基础科学中心 seminar page (eqpe.xmu.edu.cn/info/1331/5301.htm, 2022-12), read 2026-08-14
  field_scope:
  - early WP existence and abstract (winners and runners-up; 10% local advantage; cost +6.4%)
  - author identity (Yuan Wang, ECNU)
  added: '2026-08-14'
  confidence: high
  verified: true
- source: DataCite record for 10.17632/nw6tjvzk33.1 and Wayback snapshots of the Mendeley page (2024-11-13, 2025-12-09)
  field_scope:
  - replication folder identity, creators, description, CC BY 4.0, issue date 2024-10-25
  added: '2026-08-14'
  confidence: high
  verified: true
- source: Mendeley Data public API and downloaded V1 Replication.zip, including Replication/Readme.docx (queried and inspected 2026-09-28)
  field_scope:
  - current V1 availability, non-confidential status, CC BY 4.0 license, public-file route and ZIP size
  - exact ZIP manifest and formats
  - README evidence on procurement construction, coverage, released file roles, Stata version and replication instructions
  added: '2026-09-28'
  confidence: high
  verified: true
- source: Existing china-gov-procurement used_by entry for this paper (evidence_url ScienceDirect abstract page; not readable this session)
  field_scope:
  - 2014-2020 window, 93.2% match rate, 2.2M/1.4M/409K figures (carried, needs re-verification)
  added: '2026-08-14'
  confidence: low
  verified: false
- source: IDEAS/RePEc and OpenAlex (bibliographic identity, abstract)
  field_scope:
  - journal, volume, DOI, authors, abstract (winning and losing bidders)
  added: '2026-08-14'
  confidence: high
  verified: true

related_datasets:
- id: china-gov-procurement
  relation: often-confused-with
- id: asif
  relation: complement
- id: china-patents
  relation: complement
---

## Positioning in one sentence

Tang, Wang & Wu (2025 JUE) constructed a bidder-level dataset of Chinese public procurement auctions that uniquely includes losing as well as winning bidders (~2.2M purchases, ~1.4M firms, ~409K auctions, 2014-2020 per existing entry), collected from ccgp.gov.cn announcements, matched to enterprise registration data, and combined with hand-collected mayor career data. The replication folder is directly downloadable from Mendeley Data under CC BY 4.0, making the losing-bidder layer - not available in contract-level procurement data (china-gov-procurement) - obtainable.

## Select rules

- Prioritize this asset when the research design needs the full bidder set of each procurement auction - comparing winners with losers, local with non-local bidders, within the same auction.
- Choose it over china-gov-procurement when losing-bidder information is essential (contract-level records contain only winners); the two share the ccgp.gov.cn raw family but differ in observation unit.
- Choose the Mendeley replication folder over rebuilding from ccgp.gov.cn when the paper's cleaned panel and code suffice; rebuild only when extended years/regions or a different matching is needed.
- Not suitable for pre-2014 analysis, firm operating performance without further joins, or non-announced procurement.

## Get recipe

1. Download the public Mendeley V1 Replication.zip (DOI 10.17632/nw6tjvzk33.1), then read `Replication/Readme.docx`. Its verified manifest contains four named `.dta` files and two Stata scripts; `procurement_candidate.dta` is the documented all-qualified-bidders major-analysis subset.
2. Read the published JUE data section (library/human browser; 403-blocked here) only if an extension needs the exact construction, year window, or match procedure beyond the README; those finer details remain partly documented through secondary evidence and the existing used_by entry.
3. If rebuilding: collect ccgp.gov.cn auction announcements, extract full bidder sets, match to enterprise registration data (name-based), join patents/tax/penalties, collect mayor careers from Baidu Baike.
4. Join outcomes (ASIF, patents, tax survey) on bidder firm name; expect low match rates on non-registration dimensions.

## Connections and Limitations

- Distinct layer vs china-gov-procurement: that record is the contract/award level (2,997,105 contracts 2013-2019, Beraja et al. extraction); this asset is the bidder-auction level including losers (2014-2020 per existing entry).
- The 2014-2020 window and 93.2% match rate are carried from the existing china-gov-procurement used_by entry whose evidence_url is the ScienceDirect abstract page; they were not re-verified from a readable primary source this session.
- Construction details rest on a detailed secondary summary (Xiangzhang) plus the official XMU seminar abstract; the published data section is unread (ScienceDirect 403) and SSRN WPs are blocked here.
- Replication-folder identity, license (CC BY 4.0), current public availability, and the exact four-data-file/two-script manifest are verified. The README verifies that `procurement_candidate.dta` is the all-qualified-bidders major-analysis subset; it does not establish every table column, its row count, or whether every original auction is represented.
- Firm registration data and tax-survey data access routes are unverified; mayor career data are paper-specific hand-collected work.
