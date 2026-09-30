from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_CASES = ROOT / "benchmarks" / "idea-routing" / "public_cases.yaml"
BENCHMARK_README = ROOT / "benchmarks" / "idea-routing" / "README.md"
SESSION_DIRNAME = ".benchmark"
DEFAULT_SEED = 20260711
VARIANT_MODES = {"balanced", "formal", "oral", "incomplete"}
DECISIONS = {
    "recommend",
    "recommend_with_gap",
    "clarify",
    "knowledge_gap",
    "infeasible_under_constraints",
    "temporal_gap",
}
PROTOCOL_VERSION = 4
CLAIM_KINDS = {"fit", "coverage", "access", "limitation", "join"}
ROOT_FILES = (
    "AGENTS.md",
    "README.md",
    "guides/operations.md",
    "guides/usage.md",
    "DATASET_INDEX.md",
)
OPTIONAL_ROOT_FILES = ("COLLECTION_PROFILE.md",)
SNAPSHOT_FILES = (
    ("dist/router_index.json", "dist/router_index.json"),
    ("benchmarks/idea-routing/README.md", "benchmarks/idea-routing/README.md"),
    ("scripts/benchmark_session.py", "scripts/benchmark_session.py"),
)
FEEDBACK_HEADINGS = (
    "## Run integrity",
    "## Executive summary",
    "## Case-level friction",
    "## Knowledge-base gaps",
    "## Retrieval and efficiency",
    "## Protocol deviations",
)
FORBIDDEN_CASE_KEYS = {
    "expected_top",
    "acceptable",
    "avoid",
    "must_explain",
    "required_any",
    "required_mentions",
    "must_not_claim",
    "gold",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_number} must contain a JSON object")
        rows.append(value)
    return rows


def atomic_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    text = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def tree_digest(root: Path, *, exclude_session: bool = True) -> str:
    digest = hashlib.sha256()
    for path in sorted((item for item in root.rglob("*") if item.is_file()), key=lambda item: item.as_posix()):
        relative = path.relative_to(root)
        if exclude_session and relative.parts and relative.parts[0] == SESSION_DIRNAME:
            continue
        digest.update(relative.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def load_public_cases(path: Path = PUBLIC_CASES) -> list[dict[str, Any]]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    cases = value.get("cases") if isinstance(value, dict) else None
    if not isinstance(cases, list) or not cases:
        raise ValueError("public benchmark must contain a non-empty cases list")
    seen: set[str] = set()
    result: list[dict[str, Any]] = []
    for case in cases:
        if not isinstance(case, dict) or not case.get("id") or not case.get("prompt"):
            raise ValueError("every public case needs id and prompt")
        case_id = str(case["id"])
        if case_id in seen:
            raise ValueError(f"duplicate public case id: {case_id}")
        leaked = sorted(find_forbidden_keys(case))
        if leaked:
            raise ValueError(f"public case {case_id} leaks evaluator fields: {leaked}")
        seen.add(case_id)
        result.append(case)
    return result


def find_forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        found.update(FORBIDDEN_CASE_KEYS.intersection(value))
        for child in value.values():
            found.update(find_forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_keys(child))
    return found


def build_queue(cases: list[dict[str, Any]], seed: int, variant_mode: str) -> list[dict[str, Any]]:
    if variant_mode not in VARIANT_MODES:
        raise ValueError(f"variant mode must be one of {sorted(VARIANT_MODES)}")
    rng = random.Random(seed)
    ordered = list(cases)
    rng.shuffle(ordered)
    balanced_variants = ["formal", "oral", "incomplete"]
    rng.shuffle(balanced_variants)
    queue: list[dict[str, Any]] = []
    for index, case in enumerate(ordered):
        variant = balanced_variants[index % len(balanced_variants)] if variant_mode == "balanced" else variant_mode
        if variant == "formal":
            prompt = str(case["prompt"]).strip()
        else:
            variants = case.get("variants") or {}
            prompt = str(variants.get(variant, "")).strip()
            if not prompt:
                raise ValueError(f"case {case['id']} has no {variant} variant")
        queue.append(
            {
                "sequence": index + 1,
                "case_id": str(case["id"]),
                "family": str(case.get("family", "")),
                "difficulty": str(case.get("difficulty", "")),
                "variant": variant,
                "prompt": prompt,
            }
        )
    return queue


def copy_file(source_root: Path, workspace: Path, source: str, target: str | None = None) -> None:
    source_path = source_root / source
    if not source_path.is_file():
        raise FileNotFoundError(f"required snapshot file is missing: {source_path}")
    target_path = workspace / (target or source)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)


def copy_snapshot(source_root: Path, workspace: Path) -> None:
    workspace.mkdir(parents=True, exist_ok=False)
    for name in ROOT_FILES:
        copy_file(source_root, workspace, name)
    for name in OPTIONAL_ROOT_FILES:
        if (source_root / name).is_file():
            copy_file(source_root, workspace, name)
    dataset_source = source_root / "datasets"
    if not dataset_source.is_dir():
        raise FileNotFoundError(f"required snapshot directory is missing: {dataset_source}")
    shutil.copytree(dataset_source, workspace / "datasets")
    for source, target in SNAPSHOT_FILES:
        copy_file(source_root, workspace, source, target)


def git_revision(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip() or "unknown"
    except (FileNotFoundError, subprocess.SubprocessError):
        return "unavailable"


def safe_label(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-.")
    return cleaned[:40] or "unknown"


def unique_run_dir(output_root: Path, stem: str) -> Path:
    candidate = output_root / stem
    counter = 2
    while candidate.exists():
        candidate = output_root / f"{stem}-{counter}"
        counter += 1
    return candidate


def feedback_template(manifest: dict[str, Any]) -> str:
    return f"""# Benchmark Run Feedback

This report describes what happened during run `{manifest['run_id']}`. Preserve uncertainty and raw failures; do not self-award a benchmark score or rewrite submitted answers after seeing aggregate patterns.

## Run integrity

- Agent surface: {manifest['agent_surface']}
- Model label: {manifest['model_label']}
- External research/search used: <!-- yes or no -->
- Any source-repository, previous-run, legacy-benchmark, evaluator, or hidden-gold file opened after isolation: <!-- yes or no -->
- Tool transcript available to the evaluator: <!-- yes/no and location, without credentials -->
- Orientation files read before the first `next`: <!-- relative paths inside the isolated workspace -->
- Integrity notes: <!-- state deviations plainly; write `none` when there were none -->

## Executive summary

<!-- Summarize completion, recurring strengths, recurring failure modes, and confidence in this diagnosis. This is diagnostic feedback, not a score. -->

## Case-level friction

<!-- List only consequential cases. For each, cite the case ID and distinguish: retrieval failure, ambiguous idea, missing knowledge, conflicting records, access-route insufficiency, or protocol/tool failure. Say what local evidence supports that diagnosis. -->

## Knowledge-base gaps

<!-- Identify information that appears absent or too weak to support an answer. Cite case IDs, record paths, and fields. Separate an apparent knowledge-base gap from the possibility that the agent simply failed to retrieve existing information. -->

## Retrieval and efficiency

<!-- Describe whether the router index produced a useful shortlist, which queries caused excess reading, whether later cases became less careful, and any difference between formal, oral, and incomplete prompts. Do not treat self-reported file counts as tool-observed facts. -->

## Protocol deviations

<!-- Record external lookup, prohibited-file access, source edits, skipped or repeated cases, context resets, crashes, manual intervention, or timing anomalies. Write `none` only if none occurred. -->

## Candidate improvements

<!-- Rank a small number of improvements by expected effect on idea-to-dataset-to-acquisition quality. Ground every suggestion in one or more case IDs. Mark each as knowledge, retrieval/index, operating guidance, benchmark tooling, or model-specific hypothesis. -->
"""


def prepare_session(
    *,
    source_root: Path,
    output_root: Path,
    agent_surface: str,
    model_label: str,
    seed: int,
    variant_mode: str,
) -> Path:
    source_root = source_root.resolve()
    output_root = output_root.resolve()
    try:
        output_root.relative_to(source_root)
    except ValueError:
        pass
    else:
        raise ValueError("benchmark output root must be outside the source repository")
    cases = load_public_cases(source_root / "benchmarks" / "idea-routing" / "public_cases.yaml")
    queue = build_queue(cases, seed, variant_mode)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stem = f"{timestamp}-{safe_label(agent_surface)}-{safe_label(model_label)}-s{seed}"
    output_root.mkdir(parents=True, exist_ok=True)
    run_dir = unique_run_dir(output_root, stem)
    workspace = run_dir / "workspace"
    try:
        copy_snapshot(source_root, workspace)
    except Exception:
        if run_dir.is_dir():
            shutil.rmtree(run_dir)
        raise

    session_dir = workspace / SESSION_DIRNAME
    session_dir.mkdir()
    queue_path = session_dir / "case_queue.jsonl"
    atomic_jsonl(queue_path, queue)
    manifest = {
        "protocol_version": PROTOCOL_VERSION,
        "run_id": run_dir.name,
        "created_at": utc_now(),
        "created_epoch": time.time(),
        "agent_surface": agent_surface,
        "model_label": model_label,
        "seed": seed,
        "variant_mode": variant_mode,
        "case_count": len(queue),
        "source_revision": git_revision(source_root),
        "source_snapshot_sha256": tree_digest(workspace),
        "queue_sha256": sha256_file(queue_path),
        "network_policy": "Model API transport only; no web, browser, external search, external MCP, paper, or dataset lookup.",
        "isolation": {
            "method": "allowlisted snapshot outside the source repository",
            "contains_hidden_gold": False,
            "contains_legacy_benchmark": False,
            "contains_previous_results": False,
        },
        "measurement": {
            "elapsed_seconds": "harness-measured from next to submit",
            "files_read": "agent self-report unless a separate tool transcript is supplied",
        },
    }
    atomic_json(session_dir / "manifest.json", manifest)
    atomic_json(
        session_dir / "state.json",
        {
            "protocol_version": PROTOCOL_VERSION,
            "next_index": 0,
            "active_index": None,
            "active_started_epoch": None,
            "active_started_at": None,
            "first_case_started_epoch": None,
            "submission_hashes": {},
            "finished": False,
        },
    )
    (session_dir / "FEEDBACK.md").write_text(feedback_template(manifest), encoding="utf-8")
    return workspace


def session_paths(workspace: Path) -> dict[str, Path]:
    session_dir = workspace / SESSION_DIRNAME
    if not session_dir.is_dir():
        raise ValueError(f"no benchmark session found in {workspace}")
    return {
        "session": session_dir,
        "manifest": session_dir / "manifest.json",
        "state": session_dir / "state.json",
        "queue": session_dir / "case_queue.jsonl",
        "current": session_dir / "current_case.json",
        "answers": session_dir / "answers.jsonl",
        "feedback": session_dir / "FEEDBACK.md",
    }


def current_case(workspace: Path) -> dict[str, Any]:
    paths = session_paths(workspace)
    state = read_json(paths["state"])
    queue = read_jsonl(paths["queue"])
    if state.get("finished"):
        return {"status": "finished", "message": "This session has already been finalized."}
    active_index = state.get("active_index")
    if active_index is None:
        next_index = int(state.get("next_index", 0))
        if next_index >= len(queue):
            return {"status": "complete", "message": "All cases are submitted. Write FEEDBACK.md and run finish."}
        active_index = next_index
        state["active_index"] = active_index
        state["active_started_epoch"] = time.time()
        state["active_started_at"] = utc_now()
        if state.get("first_case_started_epoch") is None:
            state["first_case_started_epoch"] = state["active_started_epoch"]
        atomic_json(paths["state"], state)
    case = dict(queue[int(active_index)])
    case["status"] = "active"
    case["started_at"] = state.get("active_started_at")
    atomic_json(paths["current"], case)
    return case


def ensure_string_list(value: Any, field: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{field} must be a list of non-empty strings")
    return list(dict.fromkeys(item.strip() for item in value))


def ensure_mapping_list(value: Any, field: str) -> list[dict[str, Any]]:
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise ValueError(f"{field} must be a list of objects")
    return value


def validate_local_paths(workspace: Path, values: list[str], field: str) -> list[str]:
    normalized: list[str] = []
    for value in values:
        path = Path(value.replace("\\", "/"))
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"{field} must contain only paths inside the isolated workspace: {value}")
        candidate = (workspace / path).resolve()
        try:
            candidate.relative_to(workspace.resolve())
        except ValueError as exc:
            raise ValueError(f"{field} escapes the isolated workspace: {value}") from exc
        if not candidate.is_file():
            raise ValueError(f"{field} references a missing file: {value}")
        normalized.append(path.as_posix())
    return list(dict.fromkeys(normalized))


def normalize_claim_traces(
    workspace: Path,
    raw: Any,
    recommended: list[str],
    evidence_files: list[str],
    source_paths: dict[str, str],
) -> list[dict[str, str]]:
    """Keep decisive routing claims tied to their own canonical record."""
    traces: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for index, trace in enumerate(ensure_mapping_list(raw, "claim_traces"), start=1):
        dataset_id = str(trace.get("dataset_id", "")).strip()
        if dataset_id not in recommended:
            raise ValueError(f"claim_traces[{index}].dataset_id must be one of recommended")
        kind = str(trace.get("kind", "")).strip()
        if kind not in CLAIM_KINDS:
            raise ValueError(f"claim_traces[{index}].kind must be one of {sorted(CLAIM_KINDS)}")
        claim = str(trace.get("claim", "")).strip()
        anchor = str(trace.get("evidence_anchor", "")).strip()
        if not claim or not anchor:
            raise ValueError(f"claim_traces[{index}] requires non-empty claim and evidence_anchor")
        evidence_file = validate_local_paths(
            workspace, [str(trace.get("evidence_file", "")).strip()], f"claim_traces[{index}].evidence_file"
        )[0]
        expected_path = source_paths.get(dataset_id)
        if not expected_path or evidence_file != expected_path:
            raise ValueError(
                f"claim_traces[{index}].evidence_file must be the canonical source_path for dataset {dataset_id!r}"
            )
        if evidence_file not in evidence_files:
            raise ValueError(f"claim_traces[{index}].evidence_file must also appear in evidence_files")
        fingerprint = (dataset_id, kind, claim)
        if fingerprint in seen:
            raise ValueError(f"claim_traces[{index}] duplicates an earlier trace")
        seen.add(fingerprint)
        traces.append(
            {
                "dataset_id": dataset_id,
                "kind": kind,
                "claim": claim,
                "evidence_file": evidence_file,
                "evidence_anchor": anchor,
            }
        )
    for dataset_id in recommended:
        kinds = {item["kind"] for item in traces if item["dataset_id"] == dataset_id}
        if not kinds.intersection({"fit", "coverage"}):
            raise ValueError(f"recommended dataset {dataset_id!r} needs a fit or coverage claim trace")
        if not kinds.intersection({"access", "limitation"}):
            raise ValueError(f"recommended dataset {dataset_id!r} needs an access or limitation claim trace")
    return traces


def normalize_submission(workspace: Path, raw: dict[str, Any], active: dict[str, Any]) -> dict[str, Any]:
    case_id = str(raw.get("case_id", "")).strip()
    if case_id != active["case_id"]:
        raise ValueError(f"submission case_id must be {active['case_id']!r}")
    decision = str(raw.get("decision", "")).strip()
    if decision not in DECISIONS:
        raise ValueError(f"decision must be one of {sorted(DECISIONS)}")
    recommended = ensure_string_list(raw.get("recommended"), "recommended")
    shortlist = ensure_string_list(raw.get("shortlist"), "shortlist")
    router = read_json(workspace / "dist" / "router_index.json")
    dataset_rows = router.get("datasets")
    if not isinstance(dataset_rows, list):
        raise ValueError("dist/router_index.json has no datasets list")
    known_ids = {str(item.get("id", "")) for item in dataset_rows if isinstance(item, dict) and item.get("id")}
    source_paths = {
        str(item.get("id")): str(item.get("source_path"))
        for item in dataset_rows
        if isinstance(item, dict) and item.get("id") and item.get("source_path")
    }
    unknown_ids = sorted((set(recommended) | set(shortlist)) - known_ids)
    if unknown_ids:
        raise ValueError(f"recommended and shortlist must use dataset ids from the isolated router index: {unknown_ids}")
    if decision in {"recommend", "recommend_with_gap"} and not recommended:
        raise ValueError(f"decision {decision!r} needs at least one recommended dataset id")
    if any(item not in shortlist for item in recommended):
        raise ValueError("every recommended dataset id must also appear in shortlist")
    answer = str(raw.get("answer", "")).strip()
    if not answer:
        raise ValueError("answer must be non-empty")
    confidence = str(raw.get("confidence", "")).strip().lower()
    if confidence not in {"high", "medium", "low"}:
        raise ValueError("confidence must be high, medium, or low")
    evidence_files = validate_local_paths(
        workspace, ensure_string_list(raw.get("evidence_files"), "evidence_files"), "evidence_files"
    )
    files_read = validate_local_paths(workspace, ensure_string_list(raw.get("files_read"), "files_read"), "files_read")
    search_terms = ensure_string_list(raw.get("search_terms"), "search_terms")
    claim_traces = normalize_claim_traces(
        workspace,
        raw.get("claim_traces", []),
        recommended,
        evidence_files,
        source_paths,
    )
    return {
        "case_id": case_id,
        "decision": decision,
        "recommended": recommended,
        "shortlist": shortlist,
        "confidence": confidence,
        "answer": answer,
        "evidence_files": evidence_files,
        "files_read": files_read,
        "search_terms": search_terms,
        "claim_traces": claim_traces,
        "diagnostic_notes": str(raw.get("diagnostic_notes", "")).strip(),
    }


def submit_case(workspace: Path, submission_path: Path) -> dict[str, Any]:
    paths = session_paths(workspace)
    state = read_json(paths["state"])
    queue = read_jsonl(paths["queue"])
    active_index = state.get("active_index")
    if active_index is None:
        raise ValueError("there is no active case; run next first")
    active = queue[int(active_index)]
    raw = read_json(submission_path)
    answer = normalize_submission(workspace, raw, active)
    answers = read_jsonl(paths["answers"])
    if any(row.get("case_id") == answer["case_id"] for row in answers):
        raise ValueError(f"case {answer['case_id']} has already been submitted")
    started_epoch = float(state.get("active_started_epoch") or time.time())
    answer.update(
        {
            "sequence": active["sequence"],
            "family": active["family"],
            "difficulty": active["difficulty"],
            "prompt_variant": active["variant"],
            "started_at": state.get("active_started_at"),
            "completed_at": utc_now(),
            "elapsed_seconds": round(max(0.0, time.time() - started_epoch), 3),
            "file_measurement": "self-reported",
        }
    )
    answers.append(answer)
    atomic_jsonl(paths["answers"], answers)
    answer_hash = sha256_bytes(json.dumps(answer, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    hashes = state.get("submission_hashes")
    if not isinstance(hashes, dict):
        hashes = {}
    hashes[answer["case_id"]] = answer_hash
    state.update(
        {
            "next_index": int(active_index) + 1,
            "active_index": None,
            "active_started_epoch": None,
            "active_started_at": None,
            "submission_hashes": hashes,
        }
    )
    atomic_json(paths["state"], state)
    paths["current"].unlink(missing_ok=True)
    return {
        "status": "submitted",
        "case_id": answer["case_id"],
        "elapsed_seconds": answer["elapsed_seconds"],
        "remaining": len(queue) - len(answers),
    }


def integrity_report(workspace: Path, require_feedback: bool = False) -> dict[str, Any]:
    paths = session_paths(workspace)
    manifest = read_json(paths["manifest"])
    state = read_json(paths["state"])
    queue = read_jsonl(paths["queue"])
    answers = read_jsonl(paths["answers"])
    queue_ids = [str(row.get("case_id", "")) for row in queue]
    answer_ids = [str(row.get("case_id", "")) for row in answers]
    duplicates = sorted({item for item in answer_ids if answer_ids.count(item) > 1})
    missing = [item for item in queue_ids if item not in set(answer_ids)]
    unexpected = sorted(set(answer_ids) - set(queue_ids))
    hashes = state.get("submission_hashes") if isinstance(state.get("submission_hashes"), dict) else {}
    modified: list[str] = []
    for answer in answers:
        case_id = str(answer.get("case_id", ""))
        actual = sha256_bytes(json.dumps(answer, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        if hashes.get(case_id) != actual:
            modified.append(case_id)
    feedback_text = paths["feedback"].read_text(encoding="utf-8") if paths["feedback"].exists() else ""
    missing_headings = [heading for heading in FEEDBACK_HEADINGS if heading not in feedback_text]
    feedback_ready = len(feedback_text.strip()) >= 600 and not missing_headings and "<!--" not in feedback_text
    elapsed_values = [float(row["elapsed_seconds"]) for row in answers if isinstance(row.get("elapsed_seconds"), (int, float))]
    created_epoch = float(manifest.get("created_epoch") or time.time())
    first_case_epoch = state.get("first_case_started_epoch")
    orientation_seconds = (
        round(max(0.0, float(first_case_epoch) - created_epoch), 3) if isinstance(first_case_epoch, (int, float)) else None
    )
    snapshot_matches = tree_digest(workspace) == manifest.get("source_snapshot_sha256")
    queue_matches = sha256_file(paths["queue"]) == manifest.get("queue_sha256")
    complete = (
        len(answers) == len(queue)
        and not duplicates
        and not missing
        and not unexpected
        and not modified
        and queue_matches
        and snapshot_matches
        and (feedback_ready or not require_feedback)
    )
    return {
        "protocol_version": PROTOCOL_VERSION,
        "run_id": manifest.get("run_id"),
        "complete": complete,
        "case_count": len(queue),
        "answer_count": len(answers),
        "missing_case_ids": missing,
        "unexpected_case_ids": unexpected,
        "duplicate_case_ids": duplicates,
        "modified_after_submission": modified,
        "queue_hash_matches": queue_matches,
        "source_snapshot_hash_matches": snapshot_matches,
        "feedback_ready": feedback_ready,
        "missing_feedback_headings": missing_headings,
        "timing": {
            "orientation_seconds": orientation_seconds,
            "answer_elapsed_total": round(sum(elapsed_values), 3),
            "answer_elapsed_mean": round(statistics.mean(elapsed_values), 3) if elapsed_values else None,
            "answer_elapsed_median": round(statistics.median(elapsed_values), 3) if elapsed_values else None,
            "run_elapsed_so_far": round(max(0.0, time.time() - created_epoch), 3),
        },
        "measurement_note": "files_read and search_terms are self-reported unless accompanied by an external tool transcript.",
    }


def finish_session(workspace: Path) -> Path:
    paths = session_paths(workspace)
    report = integrity_report(workspace, require_feedback=True)
    if not report["complete"]:
        raise ValueError("session is not ready to finish:\n" + json.dumps(report, ensure_ascii=False, indent=2))
    run_dir = workspace.parent
    results = run_dir / "results"
    if results.exists():
        raise ValueError(f"results directory already exists: {results}")
    results.mkdir()
    shutil.copy2(paths["manifest"], results / "manifest.json")
    shutil.copy2(paths["queue"], results / "case_queue.jsonl")
    shutil.copy2(paths["answers"], results / "answers.jsonl")
    shutil.copy2(paths["feedback"], results / "FEEDBACK.md")
    atomic_json(results / "integrity.json", report)
    state = read_json(paths["state"])
    state["finished"] = True
    state["finished_at"] = utc_now()
    atomic_json(paths["state"], state)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare and record a contamination-resistant agent benchmark session.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="create an isolated, answer-free benchmark workspace")
    prepare.add_argument("--agent", default="unknown-agent", help="agent surface, for example claude-code or kimi-code")
    prepare.add_argument("--model", default="unknown-model", help="visible model label; never inspect credentials to find it")
    prepare.add_argument("--seed", type=int, default=DEFAULT_SEED)
    prepare.add_argument("--variant-mode", choices=sorted(VARIANT_MODES), default="balanced")
    prepare.add_argument("--output-root", type=Path, default=ROOT.parent / "econ-dataknowhow-benchmark-runs")

    subparsers.add_parser("next", help="show the next case and start its harness timer")
    submit = subparsers.add_parser("submit", help="validate and seal the active case answer")
    submit.add_argument("--file", type=Path, default=Path(SESSION_DIRNAME) / "submission.json")
    subparsers.add_parser("check", help="check progress and artifact integrity without scoring semantics")
    subparsers.add_parser("finish", help="seal a complete run and copy its evaluator packet to results/")

    args = parser.parse_args()
    try:
        if args.command == "prepare":
            workspace = prepare_session(
                source_root=ROOT,
                output_root=args.output_root.resolve(),
                agent_surface=args.agent,
                model_label=args.model,
                seed=args.seed,
                variant_mode=args.variant_mode,
            )
            print(json.dumps({"status": "prepared", "workspace": str(workspace)}, ensure_ascii=False, indent=2))
        elif args.command == "next":
            print(json.dumps(current_case(ROOT), ensure_ascii=False, indent=2))
        elif args.command == "submit":
            submission = args.file if args.file.is_absolute() else ROOT / args.file
            print(json.dumps(submit_case(ROOT, submission), ensure_ascii=False, indent=2))
        elif args.command == "check":
            print(json.dumps(integrity_report(ROOT), ensure_ascii=False, indent=2))
        else:
            results = finish_session(ROOT)
            print(json.dumps({"status": "finished", "results": str(results)}, ensure_ascii=False, indent=2))
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"benchmark session error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
