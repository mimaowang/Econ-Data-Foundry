# Idea-Routing Benchmark

This is an offline, answer-free product test. It measures whether an agent with no prior context can quickly understand Econ-Data-Foundry, retrieve the right canonical records, match unfamiliar research ideas to the best available datasets, and give an acquisition-ready answer using repository knowledge alone.

If this README is the only instruction you received, begin the protocol below. Do not ask for benchmark cases in advance.

## Integrity rules

The benchmark is valid only when the target agent:

- has not seen `benchmarks/idea-regression.yaml`, historical benchmark results, evaluator material, or another agent's answers;
- uses only the isolated workspace created by the harness after preparation;
- does not browse the web, read original papers, or use external dataset knowledge to fill repository gaps;
- processes one case at a time and does not inspect future cases;
- records the files and search terms actually used;
- preserves uncertainty instead of guessing missing coverage, variables, joins, or access conditions.

The public case file contains prompts but no gold answers. The harness removes it from the target workspace and reveals one case at a time.

## 1. Prepare an isolated run

From the source repository, run:

```powershell
python scripts/benchmark_session.py prepare --agent claude-code --model <visible-model-label> --variant-mode balanced
```

Use the actual visible model label when known. Never inspect credentials or configuration to infer it. The command prints a new workspace under `econ-data-foundry-benchmark-runs` beside the repository.

Change into the printed `workspace` directory. From that point onward, do not return to the source repository or open files outside the isolated workspace.

## 2. Orient before the first case

Act as an agent seeing the product for the first time. Read only enough to understand the mission and retrieval path. Suitable orientation files include `AGENTS.md`, `README.md`, `guides/operations.md`, and `guides/usage.md`. Do not read every dataset record before the test.

The time before the first `next` command is recorded as orientation time. In final feedback, list the files actually read during this stage.

## 3. Run one case at a time

```powershell
python scripts/benchmark_session.py next
```

The command reveals one formal, oral, or intentionally incomplete research idea and starts the harness timer. Do not run `next` again until the active case is submitted.

For each idea:

1. Extract the population, observation unit, outcomes, treatment or useful variation, geography, time, frequency, join needs, and access constraints.
2. Search `dist/router_index.json` to create a small candidate set.
3. Open the relevant files in `datasets/` and compare canonical evidence. The router is not final evidence.
4. Choose the best dataset, a justified joint design, a clarification, or an explicit knowledge gap.
5. Explain close alternatives, coverage limits, necessary joins, and the concrete acquisition route.

Do not recommend a dataset merely because one keyword matches. Do not claim variables, access, representativeness, or linkage that the canonical record does not support.

## 4. Write the submission

Write `.benchmark/submission.json` with this shape:

```json
{
  "case_id": "case ID shown by next",
  "decision": "recommend",
  "recommended": ["canonical-dataset-id"],
  "shortlist": ["canonical-dataset-id", "close-alternative-id"],
  "confidence": "medium",
  "answer": "A complete researcher-facing answer in natural English.",
  "evidence_files": ["datasets/canonical-record.md"],
  "claim_traces": [
    {
      "dataset_id": "canonical-dataset-id",
      "kind": "fit",
      "claim": "The recorded fact that determines research fit.",
      "evidence_file": "datasets/canonical-record.md",
      "evidence_anchor": "frontmatter.research_fit.best_for"
    },
    {
      "dataset_id": "canonical-dataset-id",
      "kind": "access",
      "claim": "The recorded fact that makes acquisition executable.",
      "evidence_file": "datasets/canonical-record.md",
      "evidence_anchor": "frontmatter.access_routes"
    }
  ],
  "files_read": ["dist/router_index.json", "datasets/canonical-record.md"],
  "search_terms": ["terms actually used for local retrieval"],
  "diagnostic_notes": "Retrieval friction, knowledge gaps, or protocol events; empty when none."
}
```

Allowed decisions are:

- `recommend`
- `recommend_with_gap`
- `clarify`
- `knowledge_gap`
- `infeasible_under_constraints`
- `temporal_gap`

Allowed claim kinds are `fit`, `coverage`, `access`, `limitation`, and `join`. Recommendation decisions require canonical traces for research fit or coverage and for acquisition or limitations. `evidence_files`, `claim_traces`, and `files_read` must reflect files actually opened.

Use `recommended: []` when the honest result is clarification, infeasibility, or a repository knowledge gap. The answer should still state what is missing and what decision could be made from existing knowledge.

Submit and seal the case:

```powershell
python scripts/benchmark_session.py submit
```

If validation fails, correct only the active submission. Do not inspect the next case. Repeat `next` and `submit` until no cases remain.

## 5. Check integrity

At any point, inspect mechanical progress without semantic scoring:

```powershell
python scripts/benchmark_session.py check
```

Do not edit sealed answers, the queue, manifest, or timing files. If the session is interrupted, return to the same workspace and run `next`; the harness resumes the active case.

## 6. Write diagnostic feedback

After all cases are sealed, complete `.benchmark/FEEDBACK.md`. Remove the HTML prompt comments and provide evidence under every existing heading:

- Run integrity
- Executive summary
- Case-level friction
- Knowledge-base gaps
- Retrieval and efficiency
- Protocol deviations

This is not a self-score. Cite case IDs and distinguish among missing knowledge, poor retrieval structure, unclear guidance, protocol friction, and model-specific behavior. Report unproductive searches and deviations honestly.

## 7. Finish

```powershell
python scripts/benchmark_session.py finish
```

The harness verifies completion and integrity, then packages answers, timing, diagnostics, and feedback in the run's `results/` directory. Leave that run outside the source repository so later agents cannot learn from previous answers.
