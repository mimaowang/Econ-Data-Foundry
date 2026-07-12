from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path
from typing import Any, Iterable

sys.dont_write_bytecode = True

import yaml  # noqa: E402

from kb_lib import ROOT, load_datasets  # noqa: E402


PUBLIC_CASES = ROOT / "benchmarks" / "idea-routing" / "public_cases.yaml"
FORBIDDEN_PUBLIC_KEYS = {
    "expected_top",
    "acceptable",
    "avoid",
    "must_explain",
    "required_any",
    "required_mentions",
    "must_not_claim",
    "gold",
}
PLACEHOLDER_URLS = {"", "needs-verification", "n/a", "na", "none", "null"}


def read_yaml(path: Path) -> Any:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def find_forbidden_public_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        found.update(FORBIDDEN_PUBLIC_KEYS.intersection(value))
        for child in value.values():
            found.update(find_forbidden_public_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_public_keys(child))
    return found


def load_public_cases(path: Path = PUBLIC_CASES) -> list[dict[str, Any]]:
    payload = read_yaml(path)
    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("public benchmark must contain a non-empty cases list")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for case in cases:
        if not isinstance(case, dict) or not case.get("id") or not case.get("prompt"):
            raise ValueError("every public case needs id and prompt")
        case_id = str(case["id"])
        if case_id in seen:
            raise ValueError(f"duplicate public case id: {case_id}")
        seen.add(case_id)
        leaked = sorted(find_forbidden_public_keys(case))
        if leaked:
            raise ValueError(f"public case {case_id} leaks evaluator fields: {leaked}")
        normalized.append(case)
    return normalized


def load_gold(path: Path, public_cases: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    payload = read_yaml(path)
    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("gold must contain a non-empty cases list")
    public_ids = {str(case["id"]) for case in public_cases}
    result: dict[str, dict[str, Any]] = {}
    for case in cases:
        if not isinstance(case, dict) or not case.get("id"):
            raise ValueError("every gold case needs an id")
        case_id = str(case["id"])
        if case_id in result:
            raise ValueError(f"duplicate gold case id: {case_id}")
        if case_id not in public_ids:
            raise ValueError(f"gold case is not present in public cases: {case_id}")
        result[case_id] = case
    missing = public_ids - set(result)
    if missing:
        raise ValueError(f"gold is missing public cases: {sorted(missing)}")
    return result


def load_records() -> tuple[dict[str, Any], list[tuple[Path, str]]]:
    records, failures = load_datasets()
    return {record.id: record for record in records if record.id}, failures


def record_text(record: Any) -> str:
    return json.dumps(record.data, ensure_ascii=False, default=str) + "\n" + record.body


def has_concrete_route(record: Any) -> bool:
    routes = record.data.get("access_routes")
    if not isinstance(routes, list):
        return False
    for route in routes:
        if not isinstance(route, dict):
            continue
        url = str(route.get("direct_url", "")).strip().casefold()
        if url in PLACEHOLDER_URLS:
            continue
        if route.get("steps") and route.get("requirements") and route.get("deliverable"):
            return True
    return False


def group_hits(text: str, groups: Iterable[Iterable[Any]]) -> tuple[int, int, list[list[str]]]:
    folded = text.casefold()
    hit = 0
    misses: list[list[str]] = []
    total = 0
    for group in groups:
        terms = [str(term) for term in group if str(term).strip()]
        if not terms:
            continue
        total += 1
        if any(term.casefold() in folded for term in terms):
            hit += 1
        else:
            misses.append(terms)
    return hit, total, misses


def repository_coverage(public_cases: list[dict[str, Any]], gold: dict[str, dict[str, Any]]) -> dict[str, Any]:
    records, failures = load_records()
    case_results: list[dict[str, Any]] = []
    for case in public_cases:
        case_id = str(case["id"])
        reference = gold[case_id]
        expected = [str(item) for item in reference.get("expected_top", []) or []]
        present = [item for item in expected if item in records]
        missing = [item for item in expected if item not in records]
        combined = "\n".join(record_text(records[item]) for item in present)
        fit_hit, fit_total, fit_misses = group_hits(combined, reference.get("required_any", []) or [])
        required_fields = [str(item) for item in reference.get("required_fields", []) or []]
        field_results: dict[str, bool] = {}
        for field in required_fields:
            if field == "access_routes":
                field_results[field] = bool(present) and all(has_concrete_route(records[item]) for item in present)
            else:
                field_results[field] = bool(present) and all(records[item].data.get(field) not in (None, "", [], {}) for item in present)
        case_results.append(
            {
                "case_id": case_id,
                "decision": reference.get("decision", "recommend"),
                "expected_top": expected,
                "present_top": present,
                "missing_top": missing,
                "top_available": len(present) == len(expected) if expected else True,
                "fit_groups_hit": fit_hit,
                "fit_groups_total": fit_total,
                "fit_groups_missing": fit_misses,
                "required_fields": field_results,
                "record_statuses": {item: records[item].status for item in present},
            }
        )
    expected_cases = [item for item in case_results if item["expected_top"]]
    top_available = sum(int(item["top_available"]) for item in expected_cases)
    all_field_checks = [value for item in case_results for value in item["required_fields"].values()]
    return {
        "schema_version": 2,
        "mode": "repository-coverage-heuristic",
        "project_root": str(ROOT),
        "record_count": len(records),
        "dataset_parse_failures": [{"path": str(path), "error": error} for path, error in failures],
        "case_count": len(case_results),
        "top_available_cases": top_available,
        "top_available_rate": top_available / len(expected_cases) if expected_cases else 1.0,
        "required_field_checks": sum(int(value) for value in all_field_checks),
        "required_field_total": len(all_field_checks),
        "required_field_rate": sum(int(value) for value in all_field_checks) / len(all_field_checks) if all_field_checks else 1.0,
        "cases": case_results,
        "warning": "This is a transparent structural coverage diagnostic, not a semantic truth score.",
    }


def answer_text(answer: dict[str, Any]) -> str:
    values = [answer.get("answer", ""), answer.get("rationale", ""), answer.get("uncertainty", "")]
    values.append(" ".join(str(item) for item in answer.get("recommended", []) or []))
    values.append(" ".join(str(item) for item in answer.get("shortlist", []) or []))
    return "\n".join(str(value or "") for value in values)


def score_answer(answer: dict[str, Any], reference: dict[str, Any]) -> dict[str, Any]:
    text = answer_text(answer)
    folded = text.casefold()
    expected = {str(item) for item in reference.get("expected_top", []) or []}
    acceptable = {str(item) for item in reference.get("acceptable", []) or []}
    avoid = {str(item) for item in reference.get("avoid", []) or []}
    recommended = {str(item) for item in answer.get("recommended", []) or []}
    shortlist = {str(item) for item in answer.get("shortlist", []) or []}
    gap_terms = ("clarify", "gap", "cannot", "unable", "insufficient", "not available", "temporarily")
    choice_hit = bool(recommended & expected) if expected else bool(
        reference.get("decision") in {"clarify", "knowledge-gap", "access-constrained-gap", "temporal-gap"}
        and any(term in folded for term in gap_terms)
    )
    avoid_hit = sorted(recommended & avoid)
    term_hit, term_total, term_misses = group_hits(text, reference.get("required_any", []) or [])
    mention_hit, mention_total, mention_misses = group_hits(text, [[item] for item in reference.get("required_mentions", []) or []])
    forbidden = [term for term in reference.get("must_not_claim", []) or [] if str(term).casefold() in folded]
    observed_present = "observed_files_read" in answer
    file_value = answer.get("observed_files_read") if observed_present else answer.get("files_read")
    files_read = [str(item) for item in file_value or []]
    files_read_source = "tool-observed" if observed_present else "model-self-report"
    def is_dataset_file(item: str) -> bool:
        normalized = "/" + str(item).replace("\\", "/").lstrip("/")
        return "/datasets/" in normalized

    dataset_files = [item for item in files_read if is_dataset_file(item)]
    relevant_ids = expected | acceptable | avoid
    irrelevant = [item for item in dataset_files if not any(dataset_id in item for dataset_id in relevant_ids)]
    constraints_ok = term_hit == term_total if term_total else True
    mentions_ok = mention_hit == mention_total if mention_total else True
    critical = bool(avoid_hit or forbidden)
    traces = [item for item in answer.get("claim_traces", []) if isinstance(item, dict)]
    trace_kinds = sorted({str(item.get("kind", "")) for item in traces if item.get("kind")})
    trace_by_dataset: dict[str, set[str]] = {}
    for trace in traces:
        dataset_id = str(trace.get("dataset_id", ""))
        if dataset_id:
            trace_by_dataset.setdefault(dataset_id, set()).add(str(trace.get("kind", "")))
    missing_fit_trace = sorted(
        dataset_id
        for dataset_id in recommended
        if not trace_by_dataset.get(dataset_id, set()).intersection({"fit", "coverage"})
    )
    missing_access_trace = sorted(
        dataset_id
        for dataset_id in recommended
        if not trace_by_dataset.get(dataset_id, set()).intersection({"access", "limitation"})
    )
    quality_parts = {
        "choice": int(choice_hit),
        "constraints": term_hit / term_total if term_total else 1.0,
        "required_mentions": mention_hit / mention_total if mention_total else 1.0,
        "avoidance": 0.0 if avoid_hit else 1.0,
        "uncertainty": 0.0 if forbidden else 1.0,
    }
    heuristic_score = round(
        100
        * (
            0.35 * quality_parts["choice"]
            + 0.25 * quality_parts["constraints"]
            + 0.15 * quality_parts["required_mentions"]
            + 0.15 * quality_parts["avoidance"]
            + 0.10 * quality_parts["uncertainty"]
        ),
        2,
    )
    return {
        "case_id": answer.get("case_id"),
        "model": answer.get("model"),
        "heuristic_score": heuristic_score,
        "choice_hit": choice_hit,
        "avoid_recommended": avoid_hit,
        "required_groups_hit": term_hit,
        "required_groups_total": term_total,
        "required_groups_missing": term_misses,
        "required_mentions_hit": mention_hit,
        "required_mentions_total": mention_total,
        "required_mentions_missing": mention_misses,
        "forbidden_phrase_hits": forbidden,
        "critical_failure": critical,
        "shortlist_recall": len(shortlist & expected) / len(expected) if expected else None,
        "files_read": len(files_read),
        "files_read_source": files_read_source,
        "self_reported_files_read": len(answer.get("files_read", []) or []),
        "dataset_files_read": len(dataset_files),
        "irrelevant_dataset_files": len(irrelevant),
        "elapsed_seconds": answer.get("elapsed_seconds"),
        "claim_trace_count": len(traces),
        "claim_trace_kinds": trace_kinds,
        "recommended_missing_fit_trace": missing_fit_trace,
        "recommended_missing_access_trace": missing_access_trace,
        "constraints_heuristic_pass": constraints_ok and mentions_ok and not critical,
        "warning": "Heuristic output matching requires blind semantic review before release decisions.",
    }


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} is not an object")
        rows.append(value)
    return rows


def score_answers(answer_path: Path, public_cases: list[dict[str, Any]], gold: dict[str, dict[str, Any]]) -> dict[str, Any]:
    public_ids = {str(case["id"]) for case in public_cases}
    answers = read_jsonl(answer_path)
    scored: list[dict[str, Any]] = []
    errors: list[str] = []
    seen: set[str] = set()
    for answer in answers:
        case_id = str(answer.get("case_id", ""))
        if case_id not in public_ids:
            errors.append(f"answer references unknown case: {case_id}")
            continue
        if case_id in seen:
            errors.append(f"answer contains duplicate case: {case_id}")
            continue
        seen.add(case_id)
        scored.append(score_answer(answer, gold[case_id]))
    missing = sorted(public_ids - seen)
    return {
        "schema_version": 2,
        "mode": "answer-heuristic-precheck",
        "answer_file": str(answer_path),
        "answer_count": len(scored),
        "errors": errors,
        "missing_case_ids": missing,
        "complete": not errors and not missing and len(scored) == len(public_ids),
        "critical_failures": sum(int(item["critical_failure"]) for item in scored),
        "choice_accuracy": sum(int(item["choice_hit"]) for item in scored) / len(scored) if scored else 0.0,
        "mean_heuristic_score": sum(float(item["heuristic_score"]) for item in scored) / len(scored) if scored else 0.0,
        "mean_files_read": sum(int(item["files_read"]) for item in scored) / len(scored) if scored else 0.0,
        "cases": scored,
        "warning": "This precheck is not a substitute for blind domain review or external-truth verification.",
    }


def numeric(value: Any) -> float | None:
    if isinstance(value, bool):
        return float(value)
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def trace_drift(trace_path: Path, window: int = 5) -> dict[str, Any]:
    """Summarize front/back window changes in a long-running evaluation trace."""
    if window < 1:
        raise ValueError("window must be positive")
    rows = read_jsonl(trace_path)
    if not rows:
        raise ValueError("trace must contain at least one JSONL row")
    for index, row in enumerate(rows, start=1):
        if numeric(row.get("turn")) is None:
            raise ValueError(f"trace row {index} needs numeric turn")
    rows.sort(key=lambda row: numeric(row.get("turn")) or 0)
    actual_window = min(window, len(rows))
    first = rows[:actual_window]
    last = rows[-actual_window:]

    def mean(rows_to_measure: list[dict[str, Any]], field: str) -> float | None:
        values = [value for value in (numeric(row.get(field)) for row in rows_to_measure) if value is not None]
        return round(statistics.mean(values), 4) if values else None

    fields = {
        "heuristic_score": "higher_is_better",
        "choice_hit": "higher_is_better",
        "critical_failure": "lower_is_better",
        "elapsed_seconds": "lower_is_better",
    }
    metrics: dict[str, Any] = {}
    for field, direction in fields.items():
        first_value = mean(first, field)
        last_value = mean(last, field)
        delta = round(last_value - first_value, 4) if first_value is not None and last_value is not None else None
        metrics[field] = {
            "direction": direction,
            "first_window_mean": first_value,
            "last_window_mean": last_value,
            "delta_last_minus_first": delta,
        }
    score_delta = metrics["heuristic_score"]["delta_last_minus_first"]
    choice_delta = metrics["choice_hit"]["delta_last_minus_first"]
    critical_delta = metrics["critical_failure"]["delta_last_minus_first"]
    degradation = bool(
        (score_delta is not None and score_delta < -5)
        or (choice_delta is not None and choice_delta < -0.1)
        or (critical_delta is not None and critical_delta > 0.1)
    )
    return {
        "schema_version": 1,
        "mode": "long-horizon-drift-summary",
        "trace_file": str(trace_path),
        "row_count": len(rows),
        "turn_range": [rows[0].get("turn"), rows[-1].get("turn")],
        "window": actual_window,
        "metrics": metrics,
        "degradation_flag": degradation,
        "warning": "Trend summary is a screening signal; inspect raw traces and blind semantic judgments before release decisions.",
    }


def emit(value: dict[str, Any], output: Path | None) -> None:
    text = json.dumps(value, ensure_ascii=False, indent=2, default=str) + "\n"
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text, encoding="utf-8")
        print(f"wrote {output}")
    else:
        print(text, end="")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run transparent, evaluator-side checks for Blind Benchmark v2.")
    sub = parser.add_subparsers(dest="command", required=True)

    coverage = sub.add_parser("coverage", help="measure whether current records cover hidden expectations")
    coverage.add_argument("--gold", type=Path, required=True)
    coverage.add_argument("--public", type=Path, default=PUBLIC_CASES)
    coverage.add_argument("--output", type=Path)

    answers = sub.add_parser("score-answers", help="pre-score evaluator JSONL answers without claiming semantic truth")
    answers.add_argument("--answers", type=Path, required=True)
    answers.add_argument("--gold", type=Path, required=True)
    answers.add_argument("--public", type=Path, default=PUBLIC_CASES)
    answers.add_argument("--output", type=Path)

    drift = sub.add_parser("drift", help="summarize front/back quality drift in a long-run JSONL trace")
    drift.add_argument("--trace", type=Path, required=True)
    drift.add_argument("--window", type=int, default=5)
    drift.add_argument("--output", type=Path)

    args = parser.parse_args()
    if args.command == "coverage":
        public_cases = load_public_cases(args.public)
        gold = load_gold(args.gold, public_cases)
        emit(repository_coverage(public_cases, gold), args.output)
    elif args.command == "score-answers":
        public_cases = load_public_cases(args.public)
        gold = load_gold(args.gold, public_cases)
        emit(score_answers(args.answers, public_cases, gold), args.output)
    else:
        emit(trace_drift(args.trace, args.window), args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
