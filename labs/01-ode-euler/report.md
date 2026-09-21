# Experimental report

**Status:** The explicit Euler global-error experiment has been run; measurements
and verification are recorded in [the experiment guide](experiments/README.md).
The student report below remains unfinished.

## Hypothesis

### Hypothesis 1: 
As $h\to0$, the numerical solution produced by explicit Euler should approach the exact solution.

Set the end $T$
$$Nh = T - t_0.$$
So
$$t_N = T, \qquad h = \frac{T-t_0}{N}$$
$$ \max_{0\le n\le N} |y_n-y(t_n)| \to0 \qquad\text{as }h\to0. $$

## Assumptions 
$f$ and $\partial f/\partial y$ are continuous on a compact region containing the exact and numerical solutions.

## Theory

[theory.md](theory.md)

## Experiment

- IVP: $y' = y$, $y(0) = 1$, $T = 1$.
- Solution: $y(t) = e^t$.
- Step sizes $h$: 1,0.5,0.1,0.05,0.01
- Error Metric：
$$ E(h)=\max_n|e^{t_n}-y_n| $$

## Verification

| $h$ | $E(h)$ | $E(h)/h$ | $p_{\text{obs}}$ |
|---:|---:|---:|---:|
| 1 | 0.718281828 | 0.718282 | — |
| 0.5 | 0.468281828 | 0.936564 | 0.617173 |
| 0.1 | 0.124539368 | 1.245394 | 0.822926 |
| 0.05 | 0.064984123 | 1.299682 | 0.938443 |
| 0.01 | 0.013467999 | 1.346800 | 0.977873 |

## Observation

| $h$ | $E(h)$ | $E(h)/h$ | $p_{\text{obs}}$ |
|---:|---:|---:|---:|
| 1 | 0.718281828 | 0.718282 | — |
| 0.5 | 0.468281828 | 0.936564 | 0.617173 |
| 0.1 | 0.124539368 | 1.245394 | 0.822926 |
| 0.05 | 0.064984123 | 1.299682 | 0.938443 |
| 0.01 | 0.013467999 | 1.346800 | 0.977873 |

## Interpretation

The observed convergence order increases toward $1$ as $h$ decreases, which is consistent with the theoretical first-order convergence of the explicit Euler method.

## Open Questions

TODO (student): What should be investigated next, and why?
