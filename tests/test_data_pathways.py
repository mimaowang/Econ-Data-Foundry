from __future__ import annotations

from validate_kb import Audit, load_dataset_schema, validate_against_schema, validate_data_pathway


def constructed_record() -> dict:
    return {
        "catalog_status": "grounding",
        "data_pathway": {
            "mode": "constructed",
            "origin": "researcher-constructed",
            "target_artifact": "A paper-specific event panel",
            "availability": "partially-reproducible",
            "ordinary_researcher_feasible": True,
            "summary": "Build from public documents.",
        },
        "production": {
            "raw_sources": [
                {
                    "name": "Public documents",
                    "source_type": "document",
                    "role": "Raw event evidence",
                    "access_route": "Public archive search",
                    "url": "https://example.org/archive",
                }
            ],
            "acquisition_methods": ["download"],
            "pipeline_stages": [
                {
                    "stage": "extract",
                    "inputs": ["documents"],
                    "method": "Evidence-backed extraction rule",
                    "output": "event rows",
                    "evidence": "paper appendix",
                }
            ],
            "output": {"unit_of_observation": "event"},
            "reproducibility": {
                "level": "medium",
                "starting_point": "public archive",
                "requirements": ["document parser"],
                "blockers": ["some parameters are not reported"],
            },
            "compliance": {"review_needed": "check archive terms"},
        },
    }


def test_constructed_pathway_contract_accepts_evidence_backed_route() -> None:
    audit = Audit()
    validate_data_pathway(audit, "example", constructed_record())
    assert audit.errors == []


def test_inaccessible_pathway_cannot_be_ready() -> None:
    audit = Audit()
    validate_data_pathway(
        audit,
        "private-example",
        {
            "catalog_status": "ready",
            "data_pathway": {
                "mode": "inaccessible",
                "origin": "unknown",
                "target_artifact": "Confidential administrative microdata",
                "availability": "unavailable",
                "ordinary_researcher_feasible": False,
                "summary": "Available only through a private agreement.",
                "barrier": "No public application or reproducible route.",
            },
        },
    )
    assert any("cannot be ready" in error for error in audit.errors)


def test_ready_pathway_requires_realistic_feasibility() -> None:
    record = constructed_record()
    record["catalog_status"] = "ready"
    record["data_pathway"]["ordinary_researcher_feasible"] = False
    audit = Audit()
    validate_data_pathway(audit, "example", record)
    assert any("feasible for an ordinary researcher" in error for error in audit.errors)


def test_direct_release_preserves_researcher_built_origin() -> None:
    record = constructed_record()
    record["data_pathway"]["mode"] = "direct"
    record["data_pathway"]["availability"] = "ready-made"
    record["access_routes"] = [{"route": "public replication package"}]
    audit = Audit()
    validate_data_pathway(audit, "example", record)
    assert audit.errors == []


def test_schema_v3_requires_data_pathway() -> None:
    audit = Audit()
    validator = load_dataset_schema(audit)
    assert validator is not None
    validate_against_schema(
        audit,
        "missing-pathway",
        {
            "schema_version": 3,
            "catalog_status": "grounding",
            "id": "missing-pathway",
            "name": "Missing pathway",
            "aka": [],
            "provider": "Example",
            "china_related": True,
            "domains": ["test"],
        },
        validator,
    )
    assert any("data_pathway" in error for error in audit.errors)
