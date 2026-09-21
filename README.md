# Computational Math Lab

A long-term undergraduate exploration of computational mathematics through
mathematical analysis and reproducible numerical experiments.

**Status: Active learning and research exploration.**

This is a personal mathematical notebook. Mathematical reasoning, experimental
design, reproducibility, and interpretation matter more than code volume. Each
lab begins with a question and develops through this workflow:

```text
Mathematical Question
        ↓
Theory / Derivation
        ↓
Numerical Method
        ↓
Experiment
        ↓
Verification
        ↓
Interpretation
        ↓
Open Questions
```

## Lab status

- **Completed:** none yet.
- **Active:** [Lab 01 — Convergence and Stability of Euler Methods](labs/01-ode-euler/README.md).
  Explicit Euler global-error experiment available; student analysis remains in progress.
- **Planned directions:** numerical analysis, scientific computing, numerical
  linear algebra, optimization, differential equations, probability and Monte
  Carlo methods; possibly high-performance and parallel computing later.
  These are interests, not implemented projects or a fixed roadmap.

## Structure

```text
labs/01-ode-euler/    First lab: question, theory, experiments, figures, report
templates/lab/       Reusable student-completed lab skeleton
notes/               Numerical analysis, linear algebra, probability notes
common/              Shared utilities when an actual need arises
tests/               Infrastructure checks and future numerical verification
```

## Environment and checks

Install Python 3.12 or newer and [uv](https://docs.astral.sh/uv/), then from
the repository root:

```sh
uv sync --locked
uv run --locked pytest
```

`uv sync` creates `.venv` and installs NumPy, SciPy, Matplotlib, and the pytest
development dependency. `uv.lock` records the resolved dependency versions.
Use the same Python minor version when comparing runs; the initial environment
was checked with Python 3.14. The environment tests check infrastructure; the Euler tests separately check
the discrete solution against a closed-form reference and a finite-step convergence trend.

## Reproducible experiments

Keep the workflow small: one readable Python script per experiment, with a
`main()` entry point. Run scripts from the repository root. Use this command pattern:

```sh
uv run --locked python labs/<lab-id>/experiments/<experiment-name>.py
```

For each experiment:

1. State the student's hypothesis and theoretical prediction before implementing.
2. Keep chosen parameters in a clearly named configuration block or a tracked
   configuration file. Specify units, initial conditions, domain, discretization,
   tolerances, and a random seed where applicable.
3. Resolve output paths relative to the script's `__file__`. Save figures under
   the lab's `figures/` and tables or run metadata under its `outputs/`.
4. Alongside outputs, record the exact command, all effective parameters, seed,
   Python version, platform, Git revision and whether the source tree was dirty.
   Commit source and the lockfile before a recorded run when practical.
5. Use fixed filenames for intentional reruns or an explicit run label to preserve
   several runs. Scripts should create their output directories as needed.
6. Verify results against an independently justified reference or invariant where
   available. Record observations separately from interpretation and proof.

Generated outputs, caches, and environments are ignored. Source, configuration,
theory, and reports are tracked. A report should give the command and parameters
needed to regenerate any referenced figure. Selected figures can be deliberately
versioned with `git add -f` when needed for a public report; do not commit all runs.
Exact bitwise agreement across platforms is not assumed.

## Starting another lab

```sh
cp -R templates/lab labs/02-your-question
```

Choose an unused directory name, then replace the template TODOs with your own
question. Keep derivations, hypotheses, observations, interpretations, and open
questions distinct. Cite sources for borrowed theory and methods.

## Working with AI

AI assists with computation and engineering; the student owns the mathematics.
[AGENTS.md](AGENTS.md) defines the boundaries for future coding assistance.

## License

[MIT](LICENSE).
