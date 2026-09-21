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

### Hypothesis 2: 
$f$ and $\partial f/\partial y$ are continuous on a compact region containing the exact and numerical solutions.

## Theory

[theory.md](theory.md)

## Experiment

TODO: Record the exact command, source revision and dirty state, environment,
effective parameters, seed if applicable, reference, and output locations.

## Verification

TODO: Record checks actually performed and their outcomes, including failures.

## Observation

TODO (student): Record measured results only after running the experiment.

## Interpretation

The log-log convergence plots shows as $h$ getting small, $p_{\text{obs}}$ approximately convergent to the theoretical value 1.

## Open Questions

TODO (student): What should be investigated next, and why?
