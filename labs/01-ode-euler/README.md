# Lab 01 — Convergence and Stability of Euler Methods

**Status:** Explicit Euler derivation in progress; global-error experiment available.

## 1. Mathematical problem

How do convergence and stability determine whether an Euler method produces a
meaningful approximation to the initial value problem

$$
y'(t)=f(t,y), \qquad y(t_0)=y_0?
$$

TODO (student): Specify the assumptions, interval, examples, and precise hypotheses.

## 2. Method

Planned scope: explicit Euler, followed by a comparison with implicit Euler.

TODO (student): Define the methods and decide which question to investigate first.

## 3. Derivation

TODO (student): Develop the methods and error analysis in [theory.md](theory.md).

## 4. Theory

Topics to examine: local truncation error, global error, convergence order,
the test equation $y'=\lambda y$, absolute stability, and stiffness.

TODO (student): State definitions, assumptions, and theoretical predictions.

## 5. Experiment

The student-selected IVP is $y'=y$, $y(0)=1$, with exact solution $y(t)=e^t$.
The global-error experiment uses explicit Euler on the fixed interval $[0,1]$
with $h=1,0.5,0.1,0.05,0.01$ to examine the prediction $E(h)=O(h)$.

```sh
uv run --locked python labs/01-ode-euler/experiments/global_error.py
```

See the experiment guide for error definitions, references, and output files.
Stability experiments remain pending.

See [experiments/](experiments/README.md) for the execution convention.

## 6. Interpretation

Record student interpretation in [report.md](report.md). The experiment guide
records numerical observations; these do not constitute a convergence proof.

## Open Questions

TODO (student): Record questions raised by your analysis and future experiments.

## Sources

TODO (student): Cite the materials you actually use.
