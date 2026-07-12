# Public Catalog Artifacts

These files are generated from the canonical records in `datasets/*.md` with `python scripts/export_catalog.py`.

- `catalog.json`: complete catalog envelope with one structured object per dataset.
- `catalog.jsonl`: one dataset object per line for streaming tools.
- `catalog.csv`: compact tabular index for spreadsheets and quick inspection.
- `catalog.jsonld`: Schema.org Dataset graph for interoperable metadata consumers.
- `joins.json`: dataset nodes and explicitly recorded join edges.
- `checksums.sha256`: SHA-256 checksums for the generated artifacts.

Do not edit these files by hand. Provider access, licensing, and availability must still be verified against the canonical record and the provider's current terms.
