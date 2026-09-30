# Product Benchmarks

Econ-DataKnowhow has two isolated end-to-end benchmarks. They test different stages of the product and must not share network rules, workspaces, historical results, or evaluator material.

## Idea routing

[`idea-routing/README.md`](idea-routing/README.md) is the sole start prompt for the target agent. It is an offline, answer-free test of whether formal, oral, and incomplete research ideas can be matched quickly to canonical records with defensible comparisons, joins, limitations, and executable acquisition routes.

The harness creates a sanitized workspace under `econ-dataknowhow-benchmark-runs` beside the repository. `idea-regression.yaml` contains public development expectations and is deliberately excluded from blind workspaces.

## Autonomous collection

[`collection/README.md`](collection/README.md) is the sole start prompt for the target agent. It permits public web research and tests cold-start understanding, high-quality literature discovery, Chinese dataset identity resolution, duplicate and false-positive handling, acquisition grounding, safe repository updates, and quality stability across repeated tasks.

The harness creates a writable sanitized copy under `econ-dataknowhow-collection-benchmark-runs` beside the repository. Cycle reports, observed diffs, evidence URLs, sealed artifacts, timing, and final feedback remain in that external run directory and never write back to the source repository.

## Tool boundaries

- `scripts/validate_kb.py` validates canonical records, ledgers, public prompt integrity, and generated-index coverage.
- `scripts/benchmark_session.py` prepares and seals offline idea-routing sessions.
- `scripts/collection_benchmark_session.py` prepares writable collection sessions, observes changes, enforces content boundaries, runs gates, and seals evidence.
- `scripts/benchmark_v2.py` provides transparent development and evaluator-side diagnostics; it is not a substitute for semantic blind review.

Agent-reported searches, tools, and file reads are diagnostic claims. Harness-observed timing, file manifests, diffs, and sealed artifacts are the stronger evidence. Keep private gold and every historical run outside this repository.
