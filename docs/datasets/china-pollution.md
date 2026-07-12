---
schema_version: 2
catalog_status: deprecated
id: china-pollution
name: China pollution data (old mixed entry, split)
aka:
- china-pollution
provider: multiple
china_related: true
domains:
- environment
deprecated_reason: The old entry mixed enterprise emissions, city/monitoring station air quality, satellite PM2.5 and environmental
  law enforcement data into the same data set and could not support accurate matching.
superseded_by:
- china-firm-pollution
- china-air-quality-monitoring
- china-satellite-pm25
quality:
  profile_status: invalid-mixed-identity
  access_status: invalid-mixed-identity
  paper_use_status: migrated
  last_audited: '2026-07-10'
used_by: []
provenance:
- source: 2026-07-10 identity audit
  field_scope:
  - deprecation
  added: '2026-07-10'
  confidence: high
  verified: true
related_datasets:
- id: china-firm-pollution
  relation: successor
- id: china-air-quality-monitoring
  relation: successor
- id: china-satellite-pm25
  relation: successor
---

# Split: Do not use for research matching

Old `china-pollution` is a topic bucket, not a single data set. Please select according to research question:

- Corporate emissions, governance facilities, environmental regulations and corporate performance: `china-firm-pollution`
- Official monitoring stations/urban AQI, PM2.5 and other high-frequency actual measurements: `china-air-quality-monitoring`
- National continuous, long-term grid PM2.5 exposure: `china-satellite-pm25`

Environmental enforcement/penalty records should be considered as independent candidate data sources and should not be reconsolidated into any of the above entries.
