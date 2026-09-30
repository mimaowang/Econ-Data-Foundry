from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

from kb_lib import (  # noqa: E402
    ROOT,
    access_cost,
    atomic_write_text,
    load_datasets,
    public_http_url_issues,
    strongest_use,
    time_summary,
    used_by_count,
    workspace_lock,
)


PLACEHOLDER_URLS = {"", "needs-verification", "n/a", "na", "none", "null"}


def clean_url(value: Any) -> str:
    text = str(value or "").strip()
    return "" if text.casefold() in PLACEHOLDER_URLS or public_http_url_issues(text) else text


def first_access_url(data: dict[str, Any]) -> str:
    routes = data.get("access_routes")
    if isinstance(routes, list):
        for route in routes:
            if isinstance(route, dict):
                url = clean_url(route.get("direct_url"))
                if url:
                    return url
    access = data.get("access")
    if isinstance(access, dict):
        return clean_url(access.get("url"))
    return ""


def markdown_description(body: str) -> str:
    paragraphs = [part.strip() for part in body.split("\n\n") if part.strip()]
    for paragraph in paragraphs:
        if paragraph.startswith("#") or paragraph.startswith("<!--"):
            continue
        return paragraph
    return ""


def provider_name(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("name", "institution", "organization"):
            if value.get(key):
                return str(value[key])
        return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    return str(value or "").strip()


def entry_for(record: Any) -> dict[str, Any]:
    entry = dict(record.data)
    entry["source_path"] = record.path.relative_to(ROOT).as_posix()
    entry["description_markdown"] = record.body.strip()
    entry["research_position"] = markdown_description(record.body)
    return entry


def join_graph(records: list[Any]) -> dict[str, Any]:
    nodes = [
        {"id": record.id, "name": record.data.get("name"), "status": record.status}
        for record in sorted(records, key=lambda item: item.id)
    ]
    known = {node["id"] for node in nodes}
    edges: list[dict[str, Any]] = []
    for record in sorted(records, key=lambda item: item.id):
        joins = record.data.get("joins") or []
        if not isinstance(joins, list):
            continue
        for join in joins:
            if not isinstance(join, dict) or str(join.get("target", "")).strip() not in known:
                continue
            edges.append(
                {
                    "source": record.id,
                    "target": str(join["target"]).strip(),
                    "relation": join.get("relation"),
                    "keys": join.get("keys", []),
                    "method": join.get("method"),
                    "evidence_status": join.get("evidence_status"),
                }
            )
    edges.sort(key=lambda item: (item["source"], item["target"], str(item.get("relation", ""))))
    return {"graph_schema_version": 1, "nodes": nodes, "edges": edges}


def catalog_payload(records: list[Any]) -> dict[str, Any]:
    entries = [entry_for(record) for record in sorted(records, key=lambda item: item.id)]
    versions_present = sorted(
        {int(record.data["schema_version"]) for record in records if isinstance(record.data.get("schema_version"), int)}
    )
    return {
        "catalog_schema_version": 1,
        "dataset_record_schema_version": 2,
        "dataset_record_schema_version_semantics": "minimum backward-compatible record version",
        "latest_dataset_record_schema_version": max(versions_present, default=2),
        "supported_dataset_record_schema_versions": [2, 3],
        "dataset_record_schema_versions_present": versions_present,
        "record_count": len(entries),
        "datasets": entries,
    }


def router_entry(record: Any) -> dict[str, Any]:
    """Return a deliberately lossy first-pass index; canonical records remain the evidence."""
    data = record.data
    fit = data.get("research_fit") if isinstance(data.get("research_fit"), dict) else {}
    time_span = data.get("time_span")
    routes: list[dict[str, Any]] = []
    for route in data.get("access_routes", []) or []:
        if not isinstance(route, dict):
            continue
        routes.append(
            {
                key: route[key]
                for key in (
                    "route",
                    "access_status",
                    "cost",
                    "last_checked",
                )
                if route.get(key) not in (None, "", [])
            }
        )
    pathway = data.get("data_pathway") if isinstance(data.get("data_pathway"), dict) else None
    pathway_summary = None
    if pathway is not None:
        pathway_summary = {
            key: pathway[key]
            for key in (
                "mode",
                "origin",
                "target_artifact",
                "availability",
                "ordinary_researcher_feasible",
            )
            if pathway.get(key) not in (None, "", [])
        }
    compact_joins = [
        {
            key: join[key]
            for key in ("target", "relation", "evidence_status")
            if join.get(key) not in (None, "", [])
        }
        for join in data.get("joins", []) or []
        if isinstance(join, dict) and join.get("target")
    ]
    compact_relations = [
        ({"id": item} if isinstance(item, str) else {key: item[key] for key in ("id", "relation") if item.get(key)})
        for item in data.get("related_datasets", []) or []
        if isinstance(item, str) or (isinstance(item, dict) and item.get("id"))
    ]
    entry: dict[str, Any] = {
        "id": record.id,
        "name": data.get("name"),
        "aka": data.get("aka", []),
        "catalog_status": record.status,
        "domains": data.get("domains", []),
        "unit_of_observation": data.get("unit_of_observation"),
        "structure": data.get("structure"),
        "geo_granularity": data.get("geo_granularity", []),
        "geography": data.get("geography"),
        "time_span": time_span,
        "frequency": data.get("frequency", []),
        "key_variables": data.get("key_variables", []),
        "linkable_keys": data.get("linkable_keys", []),
        "research_fit": {
            key: fit.get(key, [])
            for key in (
                "best_for",
                "choose_over",
                "not_good_for",
                "needs_join_for",
                "variation_available",
                "topics",
            )
            if fit.get(key) not in (None, "", [])
        },
        "access": {
            "cost": access_cost(record),
            "routes": routes,
        },
        "data_pathway": pathway_summary,
        "related_datasets": compact_relations,
        "joins": compact_joins,
        "source_path": record.path.relative_to(ROOT).as_posix(),
    }
    return {key: value for key, value in entry.items() if value not in (None, "", [])}


def router_index_payload(records: list[Any]) -> dict[str, Any]:
    entries = [router_entry(record) for record in sorted(records, key=lambda item: item.id)]
    return {
        "router_index_schema_version": 2,
        "purpose": (
            "Lossy first-pass research-idea recall. Open the canonical record for comparison, access, production, joins, "
            "evidence, and final claims."
        ),
        "record_count": len(entries),
        "datasets": entries,
    }


def write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False, default=str) + "\n")


def jsonld_payload(records: list[Any]) -> dict[str, Any]:
    graph: list[dict[str, Any]] = []
    for record in sorted(records, key=lambda item: item.id):
        data = record.data
        time_span = data.get("time_span") if isinstance(data.get("time_span"), dict) else {}
        start = time_span.get("start")
        end = time_span.get("end") or time_span.get("last_confirmed_release")
        node: dict[str, Any] = {
            "@type": "Dataset",
            "@id": f"dataset:{record.id}",
            "identifier": record.id,
            "name": data.get("name"),
            "description": markdown_description(record.body),
            "keywords": [*data.get("domains", []), *data.get("aka", [])]
            if isinstance(data.get("domains"), list) and isinstance(data.get("aka"), list)
            else [],
            "publisher": {"@type": "Organization", "name": provider_name(data.get("provider"))},
            "url": first_access_url(data),
            "temporalCoverage": f"{start}/{end}" if start and end else time_summary(record),
            "spatialCoverage": data.get("geography"),
            "isAccessibleForFree": access_cost(record) == "free",
            "additionalType": record.status,
            "source": record.path.relative_to(ROOT).as_posix(),
        }
        graph.append({key: value for key, value in node.items() if value not in (None, "", [])})
    return {"@context": "https://schema.org", "@graph": graph}


def export(output_dir: Path) -> list[Path]:
    with workspace_lock("derived-views"):
        records, failures = load_datasets()
        if failures:
            details = "; ".join(f"{path.name}: {message}" for path, message in failures)
            raise RuntimeError(f"cannot export invalid dataset records: {details}")
        output_dir.mkdir(parents=True, exist_ok=True)
        catalog = catalog_payload(records)
        graph = join_graph(records)
        json_path = output_dir / "catalog.json"
        jsonl_path = output_dir / "catalog.jsonl"
        csv_path = output_dir / "catalog.csv"
        jsonld_path = output_dir / "catalog.jsonld"
        joins_path = output_dir / "joins.json"
        router_path = output_dir / "router_index.json"
        write_json(json_path, catalog)
        atomic_write_text(
            jsonl_path,
            "".join(json.dumps(entry, ensure_ascii=False, sort_keys=False, default=str) + "\n" for entry in catalog["datasets"]),
        )
        columns = [
            "id",
            "catalog_status",
            "name",
            "provider",
            "domains",
            "unit_of_observation",
            "time_span",
            "access_url",
            "access_cost",
            "strongest_use",
            "used_by_count",
            "source_path",
        ]
        csv_buffer = io.StringIO(newline="")
        writer = csv.DictWriter(csv_buffer, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        for record in sorted(records, key=lambda item: item.id):
            data = record.data
            writer.writerow(
                {
                    "id": record.id,
                    "catalog_status": record.status,
                    "name": data.get("name", ""),
                    "provider": provider_name(data.get("provider")),
                    "domains": "; ".join(str(item) for item in data.get("domains", []) or []),
                    "unit_of_observation": data.get("unit_of_observation", ""),
                    "time_span": time_summary(record),
                    "access_url": first_access_url(data),
                    "access_cost": access_cost(record),
                    "strongest_use": strongest_use(record),
                    "used_by_count": used_by_count(record),
                    "source_path": record.path.relative_to(ROOT).as_posix(),
                }
            )
        atomic_write_text(csv_path, csv_buffer.getvalue())
        write_json(jsonld_path, jsonld_payload(records))
        write_json(joins_path, graph)
        write_json(router_path, router_index_payload(records))
        generated = [json_path, jsonl_path, csv_path, jsonld_path, joins_path, router_path]
        checksums = "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in sorted(generated, key=lambda item: item.name)
        )
        checksum_path = output_dir / "checksums.sha256"
        atomic_write_text(checksum_path, checksums)
        return [*generated, checksum_path]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a deterministic machine-readable dataset catalog.")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    paths = export(args.output_dir.resolve())
    print(f"exported {len(paths) - 1} catalog artifacts to {args.output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
