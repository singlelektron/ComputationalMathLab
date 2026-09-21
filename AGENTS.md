# Agent guidance

## Ownership and scope

**AI assists with computation and engineering; the student owns the mathematics.**

This repository develops mathematical questions through analysis and reproducible
experiments. Do not populate it with unrelated algorithm implementations.
Respect the exact requested scope; initialization ends at infrastructure and
skeletons, without solving Lab 01.

Agents may assist with experiments after the student specifies the mathematical
objective, plotting, testing, numerical verification, refactoring, performance
measurement, reproducibility, and documentation formatting.

Do not automatically:

- Write mathematical conclusions or invent research findings.
- Fill unfinished derivations or replace mathematical TODOs with textbook prose.
- Implement many unrelated methods or replace a stated hypothesis with your own
  research question.
- Claim results without running the corresponding experiment.

If the mathematical objective is missing, request it before implementing the
dependent experiment. Preserve student writing and unfinished sections.

## Evidence

Keep **Hypothesis → Theory → Experiment → Observation → Interpretation** explicit.
Numerical observations are not mathematical proofs. Report the actual command,
parameters, reference, tolerances, and limitations for numerical verification.
Distinguish environment checks from method verification and scientific findings.
Do not fabricate data, citations, execution records, or successful test outcomes.

## Engineering

- Prefer small, readable scripts and explicit mathematical variable names.
- Avoid package architecture or experiment frameworks until there is a real need.
- Follow the root README's command, parameter, and output conventions.
- Keep generated outputs and environments out of ordinary commits.
- Use `uv sync --locked` and `uv run --locked pytest` for setup and checks.
- Add meaningful numerical tests when actual methods are introduced; justify
  their references and tolerances rather than testing implementation against itself.
- Keep documentation in English and cite sources for theory when supplied.
- Use focused commits. Do not push or merge unless authorized.
