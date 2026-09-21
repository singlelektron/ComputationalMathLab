# Explicit Euler global-error experiment

## Hypothesis

Student-selected objective: for $y'=y$, $y(0)=1$, and exact solution $e^t$,
check whether explicit Euler global error is consistent with $O(h)$ using
$h=1,0.5,0.1,0.05,0.01$.

## Theory

See the student's [global-error derivation](../theory.md#global-error-and-convergence).
This experiment does not complete or revise that derivation.

## Experiment

The interval is fixed at $[0,1]$ (an experiment choice); all quantities are
dimensionless. The initial value is exact. Each step uses
$y_{n+1}=y_n+h y_n$. No adaptive tolerance or randomness is involved.

Measure both $|e^1-y_N|$ and $E(h)=\max_{0\leq n\leq N}|e^{t_n}-y_n|$.
For successive coarse and fine steps, report
$p=\log(E(h_c)/E(h_f))/\log(h_c/h_f)$. The denominator uses the actual step
ratio, which is not always two. Also report $E(h)/h$.

Run from the repository root:

```sh
uv sync --locked
uv run --locked python labs/01-ode-euler/experiments/global_error.py
uv run --locked pytest
```

The recorded run on 2026-09-21 prefixed each command with
`UV_CACHE_DIR=/private/tmp/computational-math-lab-uv-cache` because the default
cache was not writable in the sandbox. Python was 3.14.2. Generated files:

- `../outputs/global_error.csv`: all measurements.
- `../outputs/global_error_metadata.json`: parameters, command, environment,
  source revision, and dirty state. The run used an uncommitted working tree.
- `../figures/global_error.png`: log-log error plot with a slope-one reference
  normalized to the finest measured point (a visual guide, not an error bound).

Reruns overwrite these files. Generated files remain ignored by Git.

## Verification

The discrete closed-form reference $(1+h)^n$ checks every computed node for
all five step sizes with relative tolerance $10^{-13}$ and zero absolute
tolerance, allowing float64 roundoff over at most 100 steps. This checks
implementation of the recurrence; the continuous reference $e^t$ measures
its discretization error. The one-step error is also checked against $e-2$.
A finite-resolution regression requires the finest observed order to lie within
0.05 of one; it does not establish an asymptotic theorem.

The recorded test run passed all 16 tests (4 infrastructure and 12 numerical or
input-validation cases). These tests do not establish stability for other IVPs.

## Observation

In this run the endpoint and maximum grid errors coincide:

| h | N | E(h) | E(h)/h | Adjacent observed order |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0.718281828 | 0.718282 | — |
| 0.5 | 2 | 0.468281828 | 0.936564 | 0.617173 |
| 0.1 | 10 | 0.124539368 | 1.245394 | 0.822926 |
| 0.05 | 20 | 0.064984123 | 1.299682 | 0.938443 |
| 0.01 | 100 | 0.013467999 | 1.346800 | 0.977873 |

## Interpretation boundary

The measured orders approach one as the steps decrease, consistent with the
student's first-order prediction on this interval. Five finite step sizes are
not a proof of $O(h)$ as $h\to0$. Student interpretation and unfinished
mathematics in the theory and report files remain to be completed.
