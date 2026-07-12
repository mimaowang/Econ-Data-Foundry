from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import datetime
from typing import Any

import yaml

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
ALLOWED_COSTS = {"free", "paid", "by-application", "mixed", "registration"}
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


def validate_datasets(audit: Audit) -> tuple[list[Any], dict[str, Any]]:
    records, failures = load_datasets()
    for path, message in failures:
        audit.error(f"dataset {path.name}: {message}")

    by_id: dict[str, Any] = {}
    alias_targets: dict[str, set[str]] = defaultdict(set)

    for record in records:
        data = record.data
        record_id = record.id or record.path.stem

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

        if data.get("schema_version") != 2:
            audit.warn(f"dataset {record_id}: schema_version is not 2")

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


def validate_ledgers(audit: Audit, active_ids: set[str]) -> dict[str, int]:
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
        touched: list[str] = []
        for field in ("datasets_touched", "datasets", "datasets_added", "datasets_updated"):
            value = row.get(field, [])
            if value is None:
                continue
            if not isinstance(value, list):
                audit.error(f"completed task {row.get('id')}: {field} must be a list")
                continue
            touched.extend(str(item).strip() for item in value if str(item).strip())
        for dataset_id in sorted(set(touched)):
            if dataset_id not in active_ids:
                audit.error(f"completed task {row.get('id')}: dataset reference '{dataset_id}' is not an active dataset")

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
        if re.search(r"Just a moment|cf_chl|Cloudflare", text, re.IGNORECASE):
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the economic dataset knowledge base.")
    parser.add_argument("--write-report", action="store_true", help="write ledgers/health.json")
    args = parser.parse_args()

    audit = Audit()
    records, _ = validate_datasets(audit)
    active_ids = {record.id for record in records if record.status != "deprecated"}
    ledger_counts = validate_ledgers(audit, active_ids)
    cache_counts = validate_caches(audit)
    benchmark_cases = validate_benchmark(audit, active_ids)
    blind_benchmark_cases = validate_blind_benchmark(audit)
    collection_benchmark_tasks = validate_collection_benchmark(audit)
    validate_generated_views(audit, active_ids)

    statuses: dict[str, int] = defaultdict(int)
    for record in records:
        statuses[record.status] += 1

    report = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "error" if audit.errors else "ok",
        "errors": audit.errors,
        "warnings": audit.warnings,
        "dataset_status_counts": dict(sorted(statuses.items())),
        "active_dataset_count": len(active_ids),
        "ledger_counts": ledger_counts,
        "cache_counts": cache_counts,
        "idea_benchmark_cases": benchmark_cases,
        "blind_benchmark_v2_cases": blind_benchmark_cases,
        "collection_benchmark_tasks": collection_benchmark_tasks,
        "paper_evidence": paper_evidence_summary(records),
    }
    if args.write_report:
        dump_json(LEDGER_DIR / "health.json", report)

    print(f"datasets={len(records)} active={len(active_ids)} errors={len(audit.errors)} warnings={len(audit.warnings)}")
    for message in audit.errors:
        print(f"ERROR: {message}")
    for message in audit.warnings:
        print(f"WARN: {message}")
    return 1 if audit.errors else 0


if __name__ == "__main__":
    sys.exit(main())
