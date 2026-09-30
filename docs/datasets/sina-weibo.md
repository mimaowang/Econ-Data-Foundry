---
schema_version: 3
catalog_status: grounding
id: sina-weibo
name: Sina Weibo Social Media Data (新浪微博数据)
aka:
- 微博数据
- 新浪微博
- Weibo
- Sina Weibo
- Chinese social media data
- 社交媒体数据
- 微博帖子数据
provider: Sina Weibo (新浪微博) / Weibo Corporation; Academic access via Weibo API or institutional data partnerships
china_related: true
domains:
- public
- development
- labor
- environment
- health
data_pathway:
  mode: collected
  origin: researcher-collected
  target_artifact: A focused, forward-collected public-post sample built under the API access and rate limits actually granted to the researcher
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: The ordinary-researcher target is a bounded public-post sample, conditional on the endpoints and permissions currently granted to the registered application. The full historical corpus used by some papers is a different, restricted asset and must not be presented as reproducible through ordinary API access.
  barrier: Full historical firehose data (billions of posts) is not publicly available. The public API has rate limits and restricted historical access. The exact data volume and time span reproducible by an ordinary researcher is a fraction of what top-journal papers use.
unit_of_observation: Social media post / comment / user-profile
structure: transaction-records-streaming
geo_granularity:
- Post (user-declared location or geotag)
- City (inferred from user profile or post content)
- province
geography: All mainland China (coverage depends on collection parameters; urban users over-represented; some regions may have limited representation)
time_span:
  start: 2009
  end: ongoing
  last_confirmed_release: ongoing
  coverage_note: Weibo launched in August 2009. Post-2012 data has richer user adoption. Historical full-text search access via API is limited; most research uses forward-collected samples or special-access firehose data.
  last_checked: "2026-07-12"
frequency:
- real-time-stream
- daily
sample_size: Paper-specific institutional corpora can contain billions of posts; an ordinary API-based sample has no guaranteed size and depends on approved endpoints, rate limits, query design, and collection duration.
key_variables:
- Post text content
- Post timestamp
- User ID (anonymized or original depending on access)
- Repost count / comment count / like count
- User-declared location or geotag
- User verification status
- Post topic / hashtag
- Image / media attachments (metadata)
- Sentiment / emotion classification (researcher-constructed)
- Topic / event classification (researcher-constructed via NLP)
research_fit:
  best_for:
  - Social media and collective action — how online communication shapes protest, civic engagement, and public opinion
  - Public sentiment and economic behavior — using social media sentiment as a high-frequency economic indicator
  - Information diffusion and media economics — how news and information spread through social networks
  - Environmental perception — public response to pollution events, environmental disasters, or policy announcements
  choose_over:
  - Choose Weibo data when you need real-time, large-scale, natural-language behavioral data from Chinese citizens
  - Switch to survey data (CGSS/CFPS) when you need representative population samples with demographic controls
  not_good_for:
  - Representative population inference (Weibo users skew young, urban, and educated)
  - Pre-2009 analysis
  - Private or encrypted messaging (WeChat data is not publicly accessible)
  needs_join_for:
  - Demographic or economic outcome data requires geographic aggregation and joining with statistical yearbook or survey data
  - Individual-level linkage to other datasets is generally not possible (no common identifier)
  variation_available:
  - 2009–present post-level time series
  - Cross-city / cross-province geographic variation (user-declared or inferred)
  - Event-level variation (natural experiments around specific incidents or policy announcements)
  - Topic and sentiment variation (researcher-constructed via NLP)
topics:
- social media
- collective action
- public opinion
- information diffusion
- sentiment analysis
- protest and civic engagement
good_for:
- High-frequency measurement of public attention, sentiment, and social coordination
- Event studies around policy announcements, environmental incidents, or political events
- Network analysis of information diffusion and social influence
identification:
- Event study (high-frequency sentiment/topic change around events)
- DID (geographic or temporal variation in social media activity)
- Spatial (geotagged posts aggregated to administrative units)
- Text-as-data (NLP-classified content as treatment or outcome)
linkable_keys:
- User-declared city/province (aggregation to administrative units)
- Post timestamp (temporal merge)
- Hashtag / topic (event identification)
- Geotag coordinates (spatial join to administrative boundaries)
access_routes:
- route: Weibo public API
  access_status: available-with-registration
  direct_url: https://open.weibo.com/
  requirements:
  - Registered developer account
  - Application for API access
  - Compliance with API terms of service and rate limits
  steps:
  - Register as Weibo developer at open.weibo.com
  - Create an application and obtain API credentials
  - Confirm which endpoints, historical windows, and query types are currently granted to the application
  - Collect only within the documented scope and rate limits; do not assume historical search or timeline access
  - Store collected data with retrieval provenance
  deliverable: A bounded sample from the public content and metadata exposed to the approved application; scope and historical depth require route-specific verification
  cost: free
  last_checked: "2026-07-12"
  caveat: API rate limits restrict collection volume. Historical search is limited — forward-collection designs are more reliable. API terms and endpoints may change.
- route: Institutional data partnership
  access_status: restricted-institutional
  direct_url: https://open.weibo.com/
  requirements:
  - Institutional agreement with Weibo Corporation
  - Research proposal and data use agreement
  - May involve fees or data-sharing restrictions
  steps:
  - Contact Weibo's academic partnership or data-sharing program
  - Submit research proposal and data management plan
  - Negotiate data scope, format, and use terms
  - Receive data under agreed conditions
  deliverable: Larger-scale or historical data access per partnership terms; may include firehose sample or specific time periods
  cost: by-application
  last_checked: "2026-07-12"
  caveat: Partnership terms are not standardized. The access used by top-journal papers (e.g., 13.2B posts) may not be replicable by researchers without existing relationships.
production:
  raw_sources:
  - name: Sina Weibo public posts and user data
    source_type: API
    role: Raw social media content for NLP processing and quantitative analysis
    access_route: Weibo public API (open.weibo.com) or institutional data partnership
    url: https://open.weibo.com/
    coverage: Public posts only; private posts and direct messages not accessible; historical depth varies by access route
    last_checked: "2026-07-12"
  acquisition_methods:
  - API access within rate limits
  - institutional data partnership
  sample_construction: Define topic keywords, user lists, time windows, or geographic filters; collect posts matching criteria together with retrieval provenance.
  pipeline_stages:
  - stage: collect
    inputs:
    - API query parameters (keywords, users, time window, geography)
    method: Query Weibo API by topic, user, or geography within rate limits; save raw post JSON with retrieval timestamp.
    tools:
    - Weibo API client
    output: Raw post records with collection provenance
    evidence: Weibo API documentation; Qin et al. (2024) describe social media data collection
  - stage: clean
    inputs:
    - Raw post records
    method: Remove duplicates, filter spam/bot content, normalize text encoding, parse user metadata, and extract geographic information.
    tools:
    - text-processing scripts
    output: Cleaned post-level dataset
    evidence: Inferred workflow only; exact deduplication, bot filtering, and location rules require project-specific evidence
  - stage: classify
    inputs:
    - Cleaned post-level dataset
    method: Apply NLP models for topic classification, sentiment analysis, event detection, or content categorization as required by research design.
    tools:
    - NLP libraries, LLM-based classifiers, or keyword dictionaries
    output: Post-level dataset with topic, sentiment, and event labels
    evidence: Qin et al. (2024) classify protest-related and collective-action content
  - stage: aggregate
    inputs:
    - Classified post-level dataset
    method: Aggregate to city-day, city-month, or event-level metrics (post counts, sentiment indices, topic prevalence).
    tools:
    - tabular data-processing software
    output: Aggregated panel dataset for econometric analysis
    evidence: Inferred workflow only; the aggregation unit and formulas must be justified by the research design
  constructed_variables:
  - name: Protest/collective-action intensity index
    concept: Frequency or sentiment-weighted measure of social-media discussion related to protest or collective action
    source_fields:
    - Post text content
    - Post timestamp
    - User-declared location
    method: NLP classification of protest-related content; aggregation to city-day or city-month counts
    validation: Cross-reference with known protest events; check classifier precision/recall
    limitations: NLP classification has inherent error; not all collective action is discussed on social media; user base is not representative
  - name: Public sentiment / attention index
    concept: High-frequency measure of public mood or attention toward specific topics, policies, or events
    source_fields:
    - Post text content
    - Post engagement metrics (reposts, comments, likes)
    method: Sentiment analysis or topic-model attention scores, aggregated to time-geography units
    validation: Compare with survey-based sentiment measures where available
    limitations: Social media sentiment may not reflect offline population sentiment
  validation:
  - NLP classifier accuracy (precision, recall, F1 against hand-labeled sample)
  - Geographic coverage audit
  - Temporal coverage and gaps check
  - Bot/spam filtering effectiveness
  output:
    unit_of_observation: Post-level or aggregated to city-day / event-level
    structure: streaming records, aggregable to panel
    geography: China where Weibo users post; urban-biased
    time_span: 2009–present depending on collection window
    key_variables:
    - post text, timestamp, user location, engagement metrics, topic/sentiment labels
    formats:
    - researcher-created tabular file
  reproducibility:
    level: low
    starting_point: Weibo public API (open.weibo.com)
    code_available: false
    requirements:
    - Weibo developer account and API access
    - NLP tools and models for Chinese text classification
    - Storage and processing capacity for large text datasets
    - Chinese language proficiency or NLP models for Chinese text
    blockers:
    - Public API provides only a fraction of full firehose data
    - Historical data access is limited
    - API terms and endpoints may change
    - Full-firehose access used by top papers requires institutional partnership not generally available
  compliance:
    terms_or_license: Weibo API terms of service; institutional agreement for partnership access
    robots_or_rate_limits: API rate limits apply; respect terms of service
    personal_or_sensitive_data: User posts are public but may contain personal information; handle with research ethics care; anonymize user IDs in published datasets
    redistribution: Do not redistribute raw post content; sharing of aggregated or derived variables may be permitted
    review_needed: Recheck current API terms, rate limits, and academic partnership availability before each new collection
access:
  url: https://open.weibo.com/
  cost: mixed
  license: API terms of service; institutional agreement for partnership access
  format:
  - json
  - csv
  api: true
  how_to_get: Register as developer at open.weibo.com for API access; contact Weibo for institutional data partnership for larger-scale access
caveats: Weibo users are not representative of the Chinese population (skew young, urban, educated). Content moderation and censorship affect what is posted and what remains accessible. API access limits mean most researchers can only collect focused samples, not the comprehensive firehose data used in top-journal papers. Historical data access is significantly restricted — forward-collection designs are more reliable than retrospective searches. Geotagging is sparse (most posts lack precise location). Bot and spam content requires filtering. NLP classification of Chinese social media text has domain-specific challenges (slang, memes, coded language).
quality:
  profile_status: partial
  access_status: partial
  paper_use_status: verified
  last_audited: "2026-07-12"
used_by:
- cite: 'Qin, Strömberg & Wu (2024), Social Media and Collective Action in China'
  doi: https://doi.org/10.3982/ecta20146
  journal: Econometrica
  year: 2024
  dataset_role: Primary data — 13.2 billion Sina Weibo posts (2009–2017) used to study how social media affects protest and collective action
  evidence_type: paper_data_section
  evidence_url: https://doi.org/10.3982/ecta20146
  data_note: Used 13.2 billion Sina Weibo posts spanning 2009–2017, obtained through special institutional data access, to construct measures of social-media discussion of protest and collective action. Combined with city-level protest event data. The replication package contains only aggregated outputs (not raw posts). The full firehose access used in the paper is not generally available to ordinary researchers — ordinary API access yields more limited samples. Weibo/social media data is a significant category where the paper demonstrates research potential but the exact replication data volume requires institutional partnership.
provenance:
- source: Qin et al. (2024) Econometrica paper confirming Weibo data use, volume (13.2B posts), and time span (2009–2017)
  added: "2026-07-12"
  confidence: high
  verified: true
- source: open.weibo.com identifying the developer-application starting point; current endpoint scope remains route-specific and must be verified
  added: "2026-07-12"
  confidence: high
  verified: true
related_datasets:
- id: cgss
  relation: complement
- id: china-stat-yearbook
  relation: complement
---
## Positioning in one sentence
Sina Weibo has produced a large stream of public text, image, and engagement data since 2009. Economists use Weibo data obtained through different routes to construct high-frequency measures of public sentiment, social coordination, protest activity, and information diffusion. Full historical corpora require special institutional access; an ordinary researcher should treat a bounded forward-collected sample as the target and verify the endpoints actually granted before designing the study.

## Select rules
- When you need high-frequency, large-scale behavioral text data from Chinese citizens
- When studying social coordination, protest, public opinion, or information diffusion in China
- Switch to survey data (CGSS/CFPS) when representative population inference or demographic controls are essential
- Weibo data is best for measuring revealed attention, sentiment, and social behavior — not for representative opinion polling
- Not suitable for pre-2009 analysis or for studying populations with low social media adoption (elderly, rural poor)

## Get recipe
1. Register as Weibo developer at open.weibo.com and create an application
2. Define collection scope: topic keywords, user list, time window, geography
3. Use API endpoints to collect posts within rate limits; store with retrieval metadata
4. Clean: remove duplicates, filter spam/bots, normalize text, extract location
5. Classify: apply NLP models for topic, sentiment, or event categorization
6. Aggregate to analysis unit (city-day, event, etc.)
7. Validate classifier accuracy against hand-labeled sample
8. For larger-scale access, explore institutional data partnership with Weibo Corporation

## Connections and Limitations
- Geographic aggregation via user-declared location or geotags links to city-level statistical and policy data
- Temporal aggregation enables DID and event-study designs with policy, environmental, or economic shocks
- Weibo users skew young, urban, and educated — results may not generalize to full population
- Content moderation affects what is observable; sensitive topics may be under-represented
- A registered developer application is the public starting point, not a guarantee of particular endpoints or historical coverage; plan only after verifying the granted scope
- NLP classification quality depends on training data and domain adaptation for Chinese social media language
