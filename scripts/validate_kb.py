from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

sys.dont_write_bytecode = True

from kb_lib import (  # noqa: E402
    BENCHMARK_PATH,
    LEDGER_DIR,
    ROOT,
    aliases,
    dump_json,
    load_datasets,
    normalize_alias,
    public_http_url_issues,
    read_jsonl,
    related_ids,
)


ALLOWED_STATUSES = {"candidate", "grounding", "ready", "needs-review", "deprecated"}
ALLOWED_TASK_STATUSES = {"pending", "claimed"}
ALLOWED_TASK_RESULTS = {
    "processed",
    "candidate",
    "skipped",
    "needs-review",
    "audited",
    "corrected",  # accepted legacy result
    "bootstrapped",  # accepted legacy result
}
ALLOWED_COSTS = {"free", "paid", "by-application", "mixed", "registration"}
ALLOWED_SCHEMA_VERSIONS = {2, 3}
ALLOWED_PATHWAY_MODES = {"direct", "constructed", "collected", "hybrid", "inaccessible"}
ALLOWED_DATA_ORIGINS = {"ready-made", "researcher-constructed", "researcher-collected", "mixed", "unknown"}
ALLOWED_AVAILABILITY = {"ready-made", "reproducible", "partially-reproducible", "restricted", "unavailable"}
ALLOWED_REPRODUCIBILITY = {"high", "medium", "low", "not-reproducible", "needs-verification"}
SEMANTIC_AUDIT_INTERVAL = 5
DATASET_SCHEMA_PATH = ROOT / "schema" / "dataset.schema.json"
REQUIRED_BASE = {"schema_version", "catalog_status", "id", "name", "aka", "provider", "china_related", "domains"}
REQUIRED_READY = {
    "unit_of_observation",
    "structure",
    "geo_granularity",
    "geography",
    "time_span",
    "frequency",
    "sample_size",
    "key_variables",
    "good_for",
    "identification",
    "linkable_keys",
    "access",
    "quality",
    "used_by",
    "provenance",
    "related_datasets",
}
REQUIRED_RESEARCH_FIT = {
    "best_for",
    "choose_over",
    "not_good_for",
    "needs_join_for",
    "variation_available",
}
BLIND_BENCHMARK_PATH = ROOT / "benchmarks" / "idea-routing" / "public_cases.yaml"
COLLECTION_BENCHMARK_PATH = ROOT / "benchmarks" / "collection" / "public_tasks.yaml"
FORBIDDEN_BLIND_KEYS = {
    "acceptable",
    "avoid",
    "expected_top",
    "gold",
    "must_explain",
    "must_not_claim",
    "required_any",
    "required_mentions",
}
FORBIDDEN_COLLECTION_KEYS = {
    "expected",
    "expected_paper",
    "expected_dataset",
    "target_paper",
    "target_dataset",
    "gold",
    "score",
    "scoring",
    "rubric_answer",
}


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def note(self, message: str) -> None:
        self.info.append(message)


def require_nonempty(audit: Audit, record_id: str, data: dict[str, Any], field: str) -> None:
    value = data.get(field)
    if value is None or value == "" or value == [] or value == {}:
        audit.error(f"dataset {record_id}: required field '{field}' is empty")


def load_dataset_schema(audit: Audit) -> Draft202012Validator | None:
    try:
        schema = json.loads(DATASET_SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        audit.error(f"dataset JSON Schema is invalid or unreadable: {exc}")
        return None
    return Draft202012Validator(schema)


def validate_against_schema(audit: Audit, record_id: str, data: dict[str, Any], validator: Draft202012Validator) -> None:
    for issue in sorted(validator.iter_errors(data), key=lambda item: tuple(str(part) for part in item.path)):
        location = ".".join(str(part) for part in issue.path) or "<root>"
        audit.error(f"dataset {record_id}: schema violation at {location}: {issue.message}")


def validate_data_pathway(audit: Audit, record_id: str, data: dict[str, Any]) -> None:
    """Validate the v3 research-data production contract without changing legacy v2 records."""
    pathway = data.get("data_pathway")
    if not isinstance(pathway, dict):
        audit.error(f"dataset {record_id}: schema v3 requires data_pathway")
        return
    for field in ("mode", "origin", "target_artifact", "availability", "ordinary_researcher_feasible", "summary"):
        if pathway.get(field) in (None, "", []):
            audit.error(f"dataset {record_id}: data_pathway.{field} is required")
    mode = str(pathway.get("mode", ""))
    origin = str(pathway.get("origin", ""))
    if mode not in ALLOWED_PATHWAY_MODES:
        audit.error(f"dataset {record_id}: data_pathway.mode must use {sorted(ALLOWED_PATHWAY_MODES)}")
    if origin not in ALLOWED_DATA_ORIGINS:
        audit.error(f"dataset {record_id}: data_pathway.origin must use {sorted(ALLOWED_DATA_ORIGINS)}")
    if str(pathway.get("availability", "")) not in ALLOWED_AVAILABILITY:
        audit.error(f"dataset {record_id}: data_pathway.availability must use {sorted(ALLOWED_AVAILABILITY)}")
    if not isinstance(pathway.get("ordinary_researcher_feasible"), bool):
        audit.error(f"dataset {record_id}: data_pathway.ordinary_researcher_feasible must be true or false")
    if data.get("catalog_status") == "ready" and pathway.get("ordinary_researcher_feasible") is False:
        audit.error(f"dataset {record_id}: ready data must be feasible for an ordinary researcher")
    if data.get("catalog_status") == "ready" and pathway.get("availability") in {"restricted", "unavailable"}:
        audit.error(f"dataset {record_id}: restricted or unavailable data cannot be ready for recommendation")
    if mode in {"constructed", "collected", "hybrid"} and origin == "ready-made":
        audit.error(f"dataset {record_id}: {mode} route conflicts with ready-made origin")

    if mode == "inaccessible":
        if record_id and not str(pathway.get("barrier", "")).strip():
            audit.error(f"dataset {record_id}: inaccessible pathway must explain data_pathway.barrier")
        if data.get("catalog_status") == "ready":
            audit.error(f"dataset {record_id}: inaccessible data cannot be ready for recommendation")
        return

    if mode == "direct" and not data.get("access_routes"):
        audit.error(f"dataset {record_id}: direct v3 pathway requires at least one access route")
    if mode == "direct" and origin in {"ready-made", "unknown"}:
        return

    production = data.get("production")
    if not isinstance(production, dict):
        audit.error(f"dataset {record_id}: {mode} pathway requires production details")
        return
    for field in ("raw_sources", "acquisition_methods", "pipeline_stages", "output", "reproducibility", "compliance"):
        if production.get(field) in (None, "", [], {}):
            audit.error(f"dataset {record_id}: production.{field} is required for {mode} pathways")
    for index, source in enumerate(production.get("raw_sources") or []):
        if not isinstance(source, dict):
            audit.error(f"dataset {record_id}: production.raw_sources[{index}] must be a mapping")
            continue
        for field in ("name", "source_type", "role", "access_route"):
            if source.get(field) in (None, "", []):
                audit.error(f"dataset {record_id}: production.raw_sources[{index}].{field} is required")
        if source.get("url"):
            issues = public_http_url_issues(source["url"])
            if issues:
                audit.error(f"dataset {record_id}: production.raw_sources[{index}].url is unsafe: {', '.join(issues)}")
    for index, stage in enumerate(production.get("pipeline_stages") or []):
        if not isinstance(stage, dict):
            audit.error(f"dataset {record_id}: production.pipeline_stages[{index}] must be a mapping")
            continue
        for field in ("stage", "inputs", "method", "output", "evidence"):
            if stage.get(field) in (None, "", []):
                audit.error(f"dataset {record_id}: production.pipeline_stages[{index}].{field} is required")
    reproducibility = production.get("reproducibility")
    if isinstance(reproducibility, dict):
        level = str(reproducibility.get("level", ""))
        if level not in ALLOWED_REPRODUCIBILITY:
            audit.error(f"dataset {record_id}: production.reproducibility.level must use {sorted(ALLOWED_REPRODUCIBILITY)}")
        for field in ("starting_point", "requirements", "blockers"):
            if reproducibility.get(field) in (None, "", []):
                audit.error(f"dataset {record_id}: production.reproducibility.{field} is required")
        if data.get("catalog_status") == "ready" and level == "not-reproducible":
            audit.error(f"dataset {record_id}: not-reproducible production cannot be ready")

    if data.get("catalog_status") == "ready":
        placeholders = {"needs-verification", "unknown", "tbd", "todo"}
        for index, stage in enumerate(production.get("pipeline_stages") or []):
            if not isinstance(stage, dict):
                continue
            for field in ("method", "output", "evidence"):
                if str(stage.get(field, "")).strip().casefold() in placeholders:
                    audit.error(
                        f"dataset {record_id}: ready production.pipeline_stages[{index}].{field} cannot be a placeholder"
                    )


def validate_datasets(audit: Audit) -> tuple[list[Any], dict[str, Any]]:
    records, failures = load_datasets()
    schema_validator = load_dataset_schema(audit)
    for path, message in failures:
        audit.error(f"dataset {path.name}: {message}")

    by_id: dict[str, Any] = {}
    alias_targets: dict[str, set[str]] = defaultdict(set)

    for record in records:
        data = record.data
        record_id = record.id or record.path.stem

        if schema_validator is not None:
            validate_against_schema(audit, record_id, data, schema_validator)

        missing = sorted(REQUIRED_BASE - set(data))
        if missing:
            audit.error(f"dataset {record.path.name}: missing base fields {', '.join(missing)}")

        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", record.id):
            audit.error(f"dataset {record.path.name}: invalid id '{record.id}'")
        elif record.id in by_id:
            audit.error(f"duplicate dataset id '{record.id}' in {record.path.name} and {by_id[record.id].path.name}")
        else:
            by_id[record.id] = record

        if record.status not in ALLOWED_STATUSES:
            audit.error(f"dataset {record_id}: invalid catalog_status '{record.status}'")

        schema_version = data.get("schema_version")
        if schema_version not in ALLOWED_SCHEMA_VERSIONS:
            audit.error(f"dataset {record_id}: schema_version must use {sorted(ALLOWED_SCHEMA_VERSIONS)}")
        elif schema_version == 3:
            validate_data_pathway(audit, record_id, data)

        if record.status == "deprecated":
            if not data.get("superseded_by"):
                audit.error(f"dataset {record_id}: deprecated entry must declare superseded_by")
        elif record.status == "ready":
            for field in sorted(REQUIRED_READY):
                if field == "used_by":
                    if field not in data:
                        audit.error(f"dataset {record_id}: required field 'used_by' is missing")
                else:
                    require_nonempty(audit, record_id, data, field)
            access = data.get("access")
            if not isinstance(access, dict):
                audit.error(f"dataset {record_id}: access must be a mapping")
            else:
                for field in ("url", "cost", "how_to_get"):
                    if not access.get(field):
                        audit.error(f"dataset {record_id}: access.{field} is required for ready entries")
                if str(access.get("cost")) not in ALLOWED_COSTS:
                    audit.error(f"dataset {record_id}: access.cost must use the controlled vocabulary {sorted(ALLOWED_COSTS)}")
                if not isinstance(access.get("api"), bool):
                    audit.error(f"dataset {record_id}: access.api must be true or false")

            for field in ("aka", "domains", "geo_granularity", "frequency", "key_variables", "identification", "linkable_keys", "used_by", "provenance", "related_datasets"):
                if not isinstance(data.get(field), list):
                    audit.error(f"dataset {record_id}: '{field}' must be a list")
            if not isinstance(data.get("time_span"), dict):
                audit.error(f"dataset {record_id}: time_span must be a mapping with last_checked")
            if not isinstance(data.get("research_fit"), dict):
                audit.error(f"dataset {record_id}: research_fit must be a mapping")
            else:
                for fit_field in sorted(REQUIRED_RESEARCH_FIT):
                    if data["research_fit"].get(fit_field) in (None, "", []):
                        audit.error(f"dataset {record_id}: research_fit.{fit_field} is required for ready entries")
            if not isinstance(data.get("access_routes"), list):
                audit.error(f"dataset {record_id}: access_routes must be a list")
            else:
                if not data["access_routes"]:
                    audit.error(f"dataset {record_id}: access_routes must contain at least one route for ready entries")
                for index, route in enumerate(data["access_routes"]):
                    if not isinstance(route, dict):
                        audit.error(f"dataset {record_id}: access_routes[{index}] must be a mapping")
                        continue
                    for field in ("route", "access_status", "direct_url", "requirements", "steps", "deliverable", "cost", "last_checked"):
                        if route.get(field) in (None, "", []):
                            audit.error(f"dataset {record_id}: access_routes[{index}].{field} is required")
                    url_issues = public_http_url_issues(route.get("direct_url"))
                    if url_issues:
                        audit.error(
                            f"dataset {record_id}: access_routes[{index}].direct_url is unsafe: {', '.join(url_issues)}"
                        )
                    if route.get("cost") and str(route["cost"]) not in ALLOWED_COSTS:
                        audit.error(f"dataset {record_id}: access_routes[{index}].cost must use the controlled vocabulary {sorted(ALLOWED_COSTS)}")
                    if not isinstance(route.get("steps"), list) or not route.get("steps"):
                        audit.error(f"dataset {record_id}: access_routes[{index}].steps must be a non-empty list")

        quality = data.get("quality")
        if record.status != "deprecated" and not isinstance(quality, dict):
            audit.error(f"dataset {record_id}: quality must be a mapping")

        if record.status == "grounding":
            fit = data.get("research_fit")
            if not isinstance(fit, dict) or any(fit.get(field) in (None, "", []) for field in REQUIRED_RESEARCH_FIT):
                audit.warn(f"dataset {record_id}: grounding entry lacks one or more research_fit comparison rules")
            if not isinstance(data.get("access_routes"), list) or not data.get("access_routes"):
                audit.warn(f"dataset {record_id}: grounding entry lacks a structured access route")

        routes = data.get("access_routes")
        if record.status != "ready" and isinstance(routes, list):
            for index, route in enumerate(routes):
                if not isinstance(route, dict):
                    continue
                url_issues = public_http_url_issues(route.get("direct_url"))
                if url_issues:
                    audit.error(
                        f"dataset {record_id}: access_routes[{index}].direct_url is unsafe: {', '.join(url_issues)}"
                    )

        record_aliases = aliases(record)
        normalized = [normalize_alias(item) for item in record_aliases]
        if len(normalized) != len(set(normalized)):
            audit.warn(f"dataset {record_id}: duplicate aliases inside aka")
        if record.status != "deprecated":
            for alias in normalized:
                alias_targets[alias].add(record_id)

        used_by = data.get("used_by", [])
        if not isinstance(used_by, list):
            audit.error(f"dataset {record_id}: used_by must be a list")
        else:
            seen_papers: set[str] = set()
            for index, paper in enumerate(used_by):
                if not isinstance(paper, dict):
                    audit.error(f"dataset {record_id}: used_by[{index}] must be a mapping")
                    continue
                fingerprint = str(paper.get("doi") or paper.get("cite") or "").strip().casefold()
                if not fingerprint:
                    audit.warn(f"dataset {record_id}: used_by[{index}] lacks cite/doi")
                elif fingerprint in seen_papers:
                    audit.error(f"dataset {record_id}: duplicate used_by paper '{fingerprint}'")
                seen_papers.add(fingerprint)
                if record.status == "ready" and not paper.get("dataset_role"):
                    audit.warn(f"dataset {record_id}: used_by[{index}] lacks dataset_role")

        text = record.path.read_text(encoding="utf-8")
        if "\ufffd" in text or "���" in text:
            audit.error(f"dataset {record_id}: contains Unicode replacement/mojibake text")
        lowered = text.casefold()
        if record.status == "ready" and ("example placeholder" in lowered or "handwritten example" in lowered):
            audit.error(f"dataset {record_id}: ready entry still contains example placeholder text")

    active_ids = {record.id for record in records if record.status != "deprecated"}
    all_ids = set(by_id)
    for record in records:
        for target in related_ids(record.data.get("related_datasets")):
            if target == record.id:
                audit.error(f"dataset {record.id}: related_datasets self-reference")
            elif target not in all_ids:
                audit.error(f"dataset {record.id}: related target '{target}' does not exist")
        joins = record.data.get("joins", [])
        if joins is not None and not isinstance(joins, list):
            audit.error(f"dataset {record.id}: joins must be a list")
        elif isinstance(joins, list):
            for index, join in enumerate(joins):
                if not isinstance(join, dict) or not join.get("target"):
                    audit.error(f"dataset {record.id}: joins[{index}] lacks target")
                elif str(join["target"]) not in active_ids:
                    audit.error(f"dataset {record.id}: join target '{join['target']}' is not an active dataset")

    for alias, targets in alias_targets.items():
        if alias and len(targets) > 1:
            audit.error(f"alias collision '{alias}' maps to {sorted(targets)}")

    return records, by_id


def validate_ledgers(audit: Audit, active_ids: set[str], all_ids: set[str] | None = None) -> dict[str, int]:
    known_ids = all_ids if all_ids is not None else active_ids
    transaction_path = LEDGER_DIR / ".task-queue.transaction.json"
    if transaction_path.exists():
        audit.error(f"task queue has an unfinished transaction: {transaction_path.name}")
    paths = {
        "pending": LEDGER_DIR / "pending_tasks.jsonl",
        "done": LEDGER_DIR / "completed_tasks.jsonl",
        "failed": LEDGER_DIR / "failed_tasks.jsonl",
        "candidates": LEDGER_DIR / "dataset_candidates.jsonl",
        "changes": LEDGER_DIR / "changes.jsonl",
    }
    loaded: dict[str, list[dict[str, Any]]] = {}
    for name, path in paths.items():
        rows, errors = read_jsonl(path)
        loaded[name] = rows
        for error in errors:
            audit.error(f"{path.name}: {error}")

    id_sets: dict[str, set[str]] = {}
    for name in ("pending", "done", "failed"):
        ids = [str(row.get("id", "")).strip() for row in loaded[name]]
        missing = sum(1 for item in ids if not item)
        if missing:
            audit.error(f"ledger {name}: {missing} rows lack id")
        duplicates = {item for item in ids if item and ids.count(item) > 1}
        if duplicates:
            audit.error(f"ledger {name}: duplicate ids {sorted(duplicates)}")
        id_sets[name] = {item for item in ids if item}

    for left, right in (("pending", "done"), ("pending", "failed"), ("done", "failed")):
        overlap = id_sets[left] & id_sets[right]
        if overlap:
            audit.error(f"{left}/{right} overlap: {sorted(overlap)}")

    # DOI is a hard identity key; exact normalized titles are a useful early warning.
    # This catches an agent re-queuing the same paper under a new task id.
    fingerprints: dict[tuple[str, str], list[str]] = defaultdict(list)
    titles: dict[str, list[str]] = defaultdict(list)
    for ledger_name in ("pending", "done", "failed"):
        for row in loaded[ledger_name]:
            row_id = str(row.get("id", "")).strip() or "<missing-id>"
            doi = str(row.get("doi", "")).strip().casefold()
            doi = re.sub(r"^https?://doi\.org/", "", doi).rstrip(" .;,)")
            if doi:
                fingerprints[("doi", doi)].append(f"{ledger_name}:{row_id}")
            title = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", str(row.get("title", "")).casefold())
            if title:
                titles[title].append(f"{ledger_name}:{row_id}")
    for (_, value), locations in fingerprints.items():
        if len(locations) > 1:
            audit.error(f"duplicate DOI across task ledgers '{value}': {locations}")
    for value, locations in titles.items():
        if len(locations) > 1:
            audit.warn(f"duplicate normalized title across task ledgers '{value}': {locations}")

    for row in loaded["done"]:
        task_id = row.get("id")
        result = row.get("result")
        if result not in ALLOWED_TASK_RESULTS:
            audit.error(f"completed task {task_id}: invalid result '{result}'")
        is_semantic_audit = row.get("type") == "semantic-audit"
        if is_semantic_audit:
            if result != "audited":
                audit.error(f"completed semantic audit {task_id}: result must be audited")
            if row.get("audit_outcome") not in {"pass", "repair-needed", "unverifiable"}:
                audit.error(f"completed semantic audit {task_id}: invalid or missing audit_outcome")
            if not _dataset_references(row, "datasets_reviewed"):
                audit.error(f"completed semantic audit {task_id}: datasets_reviewed is required")
            if "datasets_touched" in row:
                audit.error(f"completed semantic audit {task_id}: datasets_touched must not be used for reviewed records")
            if not str(row.get("note", "")).strip():
                audit.error(f"completed semantic audit {task_id}: a concrete note is required")
        elif result == "audited" or row.get("audit_outcome") is not None or row.get("datasets_reviewed") is not None:
            audit.error(f"completed task {task_id}: audit fields are only valid for semantic-audit tasks")
        touched: list[str] = []
        for field in ("datasets_touched", "datasets_reviewed", "datasets", "datasets_added", "datasets_updated"):
            value = row.get(field, [])
            if value is None:
                continue
            if not isinstance(value, list):
                audit.error(f"completed task {row.get('id')}: {field} must be a list")
                continue
            touched.extend(str(item).strip() for item in value if str(item).strip())
        for dataset_id in sorted(set(touched)):
            if dataset_id not in known_ids:
                audit.error(f"completed task {row.get('id')}: dataset reference '{dataset_id}' is not a canonical dataset")

    for row in loaded["pending"]:
        if row.get("status") not in ALLOWED_TASK_STATUSES:
            audit.error(f"pending task {row.get('id')}: invalid status '{row.get('status')}'")
        if row.get("status") == "claimed":
            if not row.get("claimed_by") or not row.get("claimed_at"):
                audit.error(f"claimed task {row.get('id')}: claimed_by and claimed_at are required")
            else:
                try:
                    datetime.fromisoformat(str(row["claimed_at"]))
                except ValueError:
                    audit.error(f"claimed task {row.get('id')}: claimed_at is not an ISO timestamp")

    for row in loaded["candidates"]:
        candidate_id = str(row.get("id", "")).strip()
        if not candidate_id:
            audit.error("candidate ledger row lacks id")
        if candidate_id in active_ids:
            audit.warn(f"candidate '{candidate_id}' already has an active dataset entry")

    return {name: len(rows) for name, rows in loaded.items()}


def validate_caches(audit: Audit) -> dict[str, int]:
    cache_dir = LEDGER_DIR / "_fetch_cache"
    failed_rows, _ = read_jsonl(LEDGER_DIR / "failed_tasks.jsonl")
    failed_cache_names = {str(row.get("cache", "")).replace("\\", "/").split("/")[-1] for row in failed_rows}
    counts = {"valid": 0, "blocked": 0, "unknown": 0}
    for path in sorted(cache_dir.glob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if re.search(r"Just a moment|cf_chl", text, re.IGNORECASE):
            counts["blocked"] += 1
            if path.name not in failed_cache_names:
                audit.error(f"cache {path.name}: Cloudflare/challenge page not recorded in failure ledger")
        elif re.search(r"<title|<html", text, re.IGNORECASE):
            counts["valid"] += 1
        else:
            counts["unknown"] += 1
            audit.warn(f"cache {path.name}: unclassified content")
    return counts


def validate_benchmark(audit: Audit, active_ids: set[str]) -> int:
    if not BENCHMARK_PATH.exists():
        audit.error("idea benchmark file is missing")
        return 0
    try:
        value = yaml.safe_load(BENCHMARK_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        audit.error(f"idea benchmark YAML parse failed: {exc}")
        return 0
    cases = value.get("cases", []) if isinstance(value, dict) else []
    if not isinstance(cases, list) or not cases:
        audit.error("idea benchmark has no cases")
        return 0
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict) or not case.get("id"):
            audit.error("idea benchmark case lacks id")
            continue
        case_id = str(case["id"])
        if case_id in seen:
            audit.error(f"duplicate benchmark case id '{case_id}'")
        seen.add(case_id)
        for field in ("expected_top", "avoid"):
            for dataset_id in case.get(field, []) or []:
                if dataset_id not in active_ids:
                    audit.error(f"benchmark {case_id}: {field} references inactive/missing dataset '{dataset_id}'")
    return len(cases)


def validate_blind_benchmark(audit: Audit) -> int:
    if not BLIND_BENCHMARK_PATH.exists():
        audit.error("blind benchmark v2 public cases are missing")
        return 0
    try:
        value = yaml.safe_load(BLIND_BENCHMARK_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        audit.error(f"blind benchmark v2 YAML parse failed: {exc}")
        return 0
    cases = value.get("cases", []) if isinstance(value, dict) else []
    if not isinstance(cases, list) or not cases:
        audit.error("blind benchmark v2 has no public cases")
        return 0
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict) or not case.get("id") or not case.get("prompt"):
            audit.error("blind benchmark v2 case lacks id or prompt")
            continue
        case_id = str(case["id"])
        if case_id in seen:
            audit.error(f"duplicate blind benchmark v2 case id '{case_id}'")
        seen.add(case_id)
        pending: list[Any] = [case]
        leaked_keys: set[str] = set()
        while pending:
            item = pending.pop()
            if isinstance(item, dict):
                leaked_keys.update(FORBIDDEN_BLIND_KEYS & set(item))
                pending.extend(item.values())
            elif isinstance(item, list):
                pending.extend(item)
        leaked = sorted(leaked_keys)
        if leaked:
            audit.error(f"blind benchmark v2 case '{case_id}' leaks evaluator fields: {leaked}")
        variants = case.get("variants")
        if not isinstance(variants, dict) or any(not str(variants.get(name, "")).strip() for name in ("oral", "incomplete")):
            audit.error(f"blind benchmark v2 case '{case_id}' needs non-empty oral and incomplete variants")
        if not str(case.get("family", "")).strip() or not str(case.get("difficulty", "")).strip():
            audit.error(f"blind benchmark v2 case '{case_id}' needs family and difficulty metadata")
    return len(cases)


def validate_collection_benchmark(audit: Audit) -> int:
    if not COLLECTION_BENCHMARK_PATH.exists():
        if (ROOT / ".collection_benchmark").is_dir():
            audit.note("collection benchmark tasks are evaluator-held in this isolated session")
            return 0
        audit.error("collection benchmark public tasks are missing")
        return 0
    try:
        value = yaml.safe_load(COLLECTION_BENCHMARK_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        audit.error(f"collection benchmark YAML parse failed: {exc}")
        return 0
    tasks = value.get("tasks", []) if isinstance(value, dict) else []
    if not isinstance(tasks, list) or not tasks:
        audit.error("collection benchmark has no public tasks")
        return 0
    seen: set[str] = set()
    for task in tasks:
        if not isinstance(task, dict) or not task.get("id") or not task.get("phase") or not task.get("prompt"):
            audit.error("collection benchmark task lacks id, phase, or prompt")
            continue
        task_id = str(task["id"])
        if task_id in seen:
            audit.error(f"duplicate collection benchmark task id '{task_id}'")
        seen.add(task_id)
        pending: list[Any] = [task]
        leaked_keys: set[str] = set()
        while pending:
            item = pending.pop()
            if isinstance(item, dict):
                leaked_keys.update(FORBIDDEN_COLLECTION_KEYS & set(item))
                pending.extend(item.values())
            elif isinstance(item, list):
                pending.extend(item)
        if leaked_keys:
            audit.error(f"collection benchmark task '{task_id}' leaks evaluator fields: {sorted(leaked_keys)}")
    return len(tasks)


def validate_generated_views(audit: Audit, active_ids: set[str]) -> None:
    index_path = ROOT / "DATASET_INDEX.md"
    if not index_path.exists():
        audit.error("DATASET_INDEX.md is missing")
        return
    text = index_path.read_text(encoding="utf-8")
    if "Generated by `scripts/build_views.py`" not in text:
        audit.warn("DATASET_INDEX.md is not marked as generated; run build_views.py")
        return
    indexed = set(re.findall(r"<!-- dataset:([a-z0-9-]+) -->", text))
    missing = active_ids - indexed
    extra = indexed - active_ids
    if missing:
        audit.error(f"generated index missing active datasets: {sorted(missing)}")
    if extra:
        audit.error(f"generated index contains inactive datasets: {sorted(extra)}")


def paper_evidence_summary(records: list[Any]) -> dict[str, Any]:
    """Expose legacy paper-evidence debt without suddenly invalidating old records."""
    required = ("cite", "dataset_role", "evidence_type", "evidence_url", "data_note")
    total = 0
    complete = 0
    incomplete_by_field: dict[str, int] = defaultdict(int)
    for record in records:
        papers = record.data.get("used_by")
        if not isinstance(papers, list):
            continue
        for paper in papers:
            if not isinstance(paper, dict):
                continue
            total += 1
            missing = [field for field in required if not str(paper.get(field, "")).strip()]
            if not missing:
                complete += 1
            for field in missing:
                incomplete_by_field[field] += 1
    return {
        "total": total,
        "structured_complete": complete,
        "incomplete": total - complete,
        "required_fields": list(required),
        "missing_by_field": dict(sorted(incomplete_by_field.items())),
        "interpretation": "A maintenance signal for used_by traceability, not a claim that incomplete entries are false.",
    }


def _dataset_references(row: dict[str, Any], field: str = "datasets_touched") -> list[str]:
    value = row.get(field)
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def semantic_audit_summary(done_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Derive an advisory slow-feedback signal from existing durable state."""
    audit_indexes = [
        index
        for index, row in enumerate(done_rows)
        if row.get("type") == "semantic-audit"
        and row.get("result") == "audited"
        and row.get("audit_outcome") in {"pass", "repair-needed", "unverifiable"}
    ]
    latest_row: dict[str, Any] | None = None
    latest_index = -1
    if audit_indexes:
        latest_index = audit_indexes[-1]
        latest_row = done_rows[latest_index]

    knowledge_tasks = []
    for row in done_rows[latest_index + 1 :]:
        if row.get("type") == "semantic-audit" or row.get("result") != "processed":
            continue
        if not _dataset_references(row):
            continue
        knowledge_tasks.append(row)

    latest_outcome = latest_row.get("audit_outcome") if latest_row else None
    reason = "current"
    if latest_row is None:
        reason = "no-prior-audit"
    elif latest_outcome in {"repair-needed", "unverifiable"}:
        reason = str(latest_outcome)
    elif len(knowledge_tasks) >= SEMANTIC_AUDIT_INTERVAL:
        reason = "interval-reached"
    due = reason != "current"
    return {
        "due": due,
        "reason": reason,
        "interpretation": (
            "Advisory slow feedback, not a quality score or automatic status change. When due, prioritize one semantic-audit "
            "task and test recent records from a fresh context before expanding. The threshold is a maximum feedback delay, "
            "not a productivity target."
        ),
    }


def data_pathway_summary(records: list[Any]) -> dict[str, Any]:
    """Track deliberate v3 adoption without treating legacy records as defective."""
    modes: dict[str, int] = defaultdict(int)
    versions: dict[str, int] = defaultdict(int)
    origins: dict[str, int] = defaultdict(int)
    for record in records:
        versions[str(record.data.get("schema_version", "unknown"))] += 1
        pathway = record.data.get("data_pathway")
        mode = pathway.get("mode") if isinstance(pathway, dict) else "legacy-unspecified"
        modes[str(mode)] += 1
        origin = pathway.get("origin") if isinstance(pathway, dict) else "legacy-unspecified"
        origins[str(origin)] += 1
    return {
        "schema_versions": dict(sorted(versions.items())),
        "pathway_modes": dict(sorted(modes.items())),
        "origins": dict(sorted(origins.items())),
        "interpretation": "A migration and coverage signal; legacy v2 records remain valid until evidence-backed pathway review.",
    }


def health_input_fingerprint() -> dict[str, Any]:
    """Identify durable catalog inputs; private fetch caches are checked separately."""
    paths = [
        Path(__file__),
        DATASET_SCHEMA_PATH,
        BENCHMARK_PATH,
        BLIND_BENCHMARK_PATH,
        COLLECTION_BENCHMARK_PATH,
    ]
    paths.extend(sorted((ROOT / "datasets").glob("*.md")))
    for name in (
        "pending_tasks.jsonl",
        "completed_tasks.jsonl",
        "failed_tasks.jsonl",
        "dataset_candidates.jsonl",
        "changes.jsonl",
    ):
        paths.append(LEDGER_DIR / name)

    digest = hashlib.sha256()
    included: list[str] = []
    for path in sorted({item.resolve() for item in paths if item.is_file()}, key=lambda item: item.as_posix()):
        relative = path.relative_to(ROOT).as_posix()
        included.append(relative)
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return {"algorithm": "sha256", "digest": digest.hexdigest(), "file_count": len(included)}


def validate_health_freshness(audit: Audit, fingerprint: dict[str, Any]) -> None:
    path = LEDGER_DIR / "health.json"
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        audit.error(f"health report is missing or unreadable: {exc}; run validate_kb.py --write-report")
        return
    recorded = existing.get("input_fingerprint") if isinstance(existing, dict) else None
    if not isinstance(recorded, dict) or recorded.get("digest") != fingerprint["digest"]:
        audit.error("health report is stale for the current canonical inputs; run validate_kb.py --write-report")


def health_generated_at(fingerprint: dict[str, Any]) -> str:
    """Keep report bytes stable when the summarized inputs have not changed."""
    path = LEDGER_DIR / "health.json"
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        existing = {}
    recorded = existing.get("input_fingerprint") if isinstance(existing, dict) else None
    generated_at = existing.get("generated_at") if isinstance(existing, dict) else None
    if isinstance(recorded, dict) and recorded.get("digest") == fingerprint["digest"] and generated_at:
        return str(generated_at)
    return datetime.now().astimezone().isoformat(timespec="seconds")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the economic dataset knowledge base.")
    parser.add_argument("--write-report", action="store_true", help="write ledgers/health.json")
    args = parser.parse_args()

    audit = Audit()
    records, _ = validate_datasets(audit)
    active_ids = {record.id for record in records if record.status != "deprecated"}
    all_ids = {record.id for record in records}
    ledger_counts = validate_ledgers(audit, active_ids, all_ids)
    done_rows, _ = read_jsonl(LEDGER_DIR / "completed_tasks.jsonl")
    semantic_audit = semantic_audit_summary(done_rows)
    benchmark_cases = validate_benchmark(audit, active_ids)
    blind_benchmark_cases = validate_blind_benchmark(audit)
    collection_benchmark_tasks = validate_collection_benchmark(audit)
    validate_generated_views(audit, active_ids)
    input_fingerprint = health_input_fingerprint()
    if not args.write_report:
        validate_health_freshness(audit, input_fingerprint)

    statuses: dict[str, int] = defaultdict(int)
    for record in records:
        statuses[record.status] += 1
    paper_evidence = paper_evidence_summary(records)
    if paper_evidence["incomplete"]:
        audit.warn(
            f"paper-use evidence backlog: {paper_evidence['incomplete']} of {paper_evidence['total']} entries lack one or more traceability fields"
        )

    report = {
        "generated_at": health_generated_at(input_fingerprint),
        "status": "error" if audit.errors else "ok",
        "errors": audit.errors,
        "warnings": audit.warnings,
        "dataset_status_counts": dict(sorted(statuses.items())),
        "active_dataset_count": len(active_ids),
        "ledger_counts": ledger_counts,
        "idea_benchmark_cases": benchmark_cases,
        "blind_benchmark_v2_cases": blind_benchmark_cases,
        "collection_benchmark_tasks": collection_benchmark_tasks,
        "paper_evidence": paper_evidence,
        "data_pathways": data_pathway_summary(records),
        "semantic_audit": semantic_audit,
        "input_fingerprint": input_fingerprint,
    }
    if args.write_report:
        dump_json(LEDGER_DIR / "health.json", report)

    print(f"datasets={len(records)} active={len(active_ids)} errors={len(audit.errors)} warnings={len(audit.warnings)}")
    for message in audit.errors:
        print(f"ERROR: {message}")
    for message in audit.warnings:
        print(f"WARN: {message}")
    # A fresh clone has no local downloads. Keep their diagnostics out of the
    # public report while retaining the existing failure gate for local work.
    cache_audit = Audit()
    cache_counts = validate_caches(cache_audit)
    print(f"local_cache_counts={cache_counts}")
    for message in cache_audit.errors:
        print(f"ERROR: {message}")
    for message in cache_audit.warnings:
        print(f"WARN: {message}")
    return 1 if audit.errors or cache_audit.errors else 0


if __name__ == "__main__":
    sys.exit(main())
