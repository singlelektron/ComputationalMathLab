# Theory — Euler methods

## Problem, notation, and assumptions

Consider the initial value problem:
$$y'(t) = f(t,y(t)),\qquad  y(t_0)=y_0.$$

Let
$$t_n=t_0+nh,\qquad n \in \mathbb N.$$
be a uniform grid with step size $h>0$.

We know that
$$y'(t) = \lim_{h \to 0}   \frac{y(t+h)-y(t)}{h}.$$

We denote the approximation by
$$y_n \approx y(t_n).$$

When h is small,
$$y'(t) \approx \frac{y(t+h)-y(t)}{h}.$$

So
$$\frac{y(t+h)-y(t)}{h} \approx f(t,y(t)),$$
$$y(t+h) \approx h f(t,y(t)) + y(t).$$

Now consider the approximation
$$y_{n+1} = h f(t_n, y_n) + y_n$$

## Hypotheses

Hypothesis 1: As $h\to0$, the numerical solution produced by explicit Euler should approach the exact solution.

## Explicit Euler derivation

TODO (student).

## Local truncation error

TODO (student): Define the quantity and derive its behavior under stated assumptions.

## Global error and convergence

TODO (student): Develop the argument and distinguish local from global error.

## Empirical convergence order

TODO (student): Define the measurement and how it relates to the theoretical claim.

## Test equation and absolute stability

For the planned test equation $y'=\lambda y$:

TODO (student): Derive the numerical behavior and formulate a stability criterion.

## Stiff equations

TODO (student): Choose an example and explain the question it is intended to test.

## Implicit Euler derivation and comparison

TODO (student): Derive the method and decide what comparison is meaningful.

## Verification plan

TODO (student): Specify justified reference solutions, error measures, and checks.

## Open Questions

TODO (student).

## Sources

TODO (student).
