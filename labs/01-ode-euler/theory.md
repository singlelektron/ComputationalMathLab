# Theory — Euler methods

## Problem, notation, and assumptions

Consider the initial value problem:
$$y'(t) = f(t,y(t)),\qquad  y(t_0)=y_0.$$

Let
$$t_n=t_0+nh,\qquad n \in \mathbb N.$$
be a uniform grid with step size $h>0$.

We denote the approximation by
$$y_n \approx y(t_n).$$

## Hypotheses

Hypothesis 1: As $h\to0$, the numerical solution produced by explicit Euler should approach the exact solution.

Set the end $T$
$$Nh = T - t_0.$$
So
$$t_N = T, \qquad h = \frac{T-t_0}{N}$$
$$ \max_{0\le n\le N} |y_n-y(t_n)| \to0 \qquad\text{as }h\to0. $$

## Explicit Euler derivation

We know that
$$y'(t) = \lim_{h \to 0}   \frac{y(t+h)-y(t)}{h}.$$

When h is small,
$$y'(t) \approx \frac{y(t+h)-y(t)}{h}.$$

So
$$\frac{y(t+h)-y(t)}{h} \approx f(t,y(t)),$$
$$y(t+h) \approx h f(t,y(t)) + y(t).$$

Now consider the approximation
$$y_{n+1} = h f(t_n, y_n) + y_n$$

## Local truncation error
$$ y(t_n+h) = y(t_n) +h y'(t_n) +\frac{h^2}{2}y''(\xi_n), \qquad \xi_n\in(t_n,t_{n+1}). $$
Let
$$d_{n+1} = y_{n+1} - y_{n},$$

$$y(t+h) = y(t) + h y'(t) + d_{n+1}.$$
So $d_{n+1}$ is $O(h^2).$

The local error every step made my Euler Method from the real value is $O(h^2)$.

## Global error and convergence

We know from the Existence and Uniqueness Theorem, if $f$ and $\frac{\partial f}{\partial y}$ are continuous in a rectangle $R$: $|t| \leqslant  a, |y| \leqslant b$, then there is some interval $|t| \leqslant h \leqslant a$ in which there exists a unique solution $y= \phi (t)$ of the initial value problem.

Here we assume the function f is contineous on
$$\left[t_0, T\right] $$

Let $e_n$ denotes the global error $e_n = y(t_{n}) - y_{n}$.

Since
$$y(t_{n+1}) = y(t_n) + h f(t_n, y(t_n)) + d_{n+1},$$
$$y{n+1} = y_n + h f(t_n, y_n),$$
$$y(t_{n+1})-y{n+1} = y(t_n)-y_n + h[f(t_n, y(t_n))-f(t_n, y_n)] + d_{n+1},$$
which is
$$e_{n+1} = e_n + h[f(t_n, y(t_n))-f(t_n, y_n)] + d_{n+1}.$$

Now we focus on $f(t_n, y(t_n))-f(t_n, y_n)$.

Since $\frac{\partial f}{\partial y}$ is continuous, by Extream Value Theorem we have 
$$\exists L,\qquad \frac{\partial f}{\partial y} \leqslant L.$$
By Mean Value Theorem,
$$\frac{f(t, y_i)-f(t, y_j)}{y_i-y_j} \leqslant L $$
for all $t, y_i, y_j$.

So
$$\left\lvert f(t, y_i)-f(t, y_j)  \right\rvert\leqslant L \left\lvert y_i-y_j \right\rvert,$$
which is Lipschitz condition.

Since
$$e_{n+1} = e_n + h[f(t_n, y(t_n))-f(t_n, y_n)] + d_{n+1},$$
We get
$$e_{n+1} \leqslant e_n + h L \left[ y(t_n) - y_n \right] + d_{n+1},$$
$$e_{n+1} \leqslant e_n ( hL + 1 ) + d_{n+1}.$$
So
$$e_{n} \leqslant e_{n-1} ( hL + 1 ) + d_{n}.$$
$$e_{n} \leqslant d_{n} \sum_{k = 0}^{n-1} (hL+1)^k .$$
$$e_{n} \leqslant d_{n} \frac{(hL+1)^n - 1}{hL} .$$
Since $d_n$ is $O(h^2)$,
$$\exists C,\qquad d_n \leqslant Ch^2,$$
$$e_{n} \leqslant Ch^2 \frac{(hL+1)^n - 1}{hL},$$
$$e_{n} \leqslant \frac{C}{L} h ((hL+1)^n-1),$$
$$e_{n} \leqslant \frac{C}{L} h (e^nhL-1),$$
$$e_{n} \leqslant \frac{C}{L} h (e^{L(T-t_0)}-1).$$
So $e_n$ is $O(h)$.

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
