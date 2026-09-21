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

### Hypothesis 1: 
As $h\to0$, the numerical solution produced by explicit Euler should approach the exact solution.

Set the end $T$
$$Nh = T - t_0.$$
So
$$t_N = T, \qquad h = \frac{T-t_0}{N}$$
$$ \max_{0\le n\le N} |y_n-y(t_n)| \to0 \qquad\text{as }h\to0. $$

## Assumptions 
$f$ and $\partial f/\partial y$ are continuous on a compact region containing the exact and numerical solutions.

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
$$d_{n+1} = y(t_{n+1}) - [y(t_n) +h f(t_n, y(t_n))],$$

$$y(t+h) = y(t) + h y'(t) + d_{n+1}.$$
So $d_{n+1}$ is $O(h^2).$

The local error every step from the real value is $O(h^2)$.

## Global error and convergence

We know from the Existence and Uniqueness Theorem, if $f$ and $\frac{\partial f}{\partial y}$ are continuous in a rectangle $R$: $|t| \leqslant  a, |y| \leqslant b$, then there is some interval $|t| \leqslant h \leqslant a$ in which there exists a unique solution $y= \phi (t)$ of the initial value problem.

Assume $f$ and $\partial f/\partial y$ are continuous on a compact region containing the exact and numerical solutions.

Let $e_n$ denote the global error $e_n = y(t_{n}) - y_{n}$.

Since
$$y(t_{n+1}) = y(t_n) + h f(t_n, y(t_n)) + d_{n+1},$$
$$y_{n+1} = y_n + h f(t_n, y_n),$$
$$y(t_{n+1})-y_{n+1} = y(t_n)-y_n + h[f(t_n, y(t_n))-f(t_n, y_n)] + d_{n+1},$$
which is
$$e_{n+1} = e_n + h[f(t_n, y(t_n))-f(t_n, y_n)] + d_{n+1}.$$

Now we focus on $f(t_n, y(t_n))-f(t_n, y_n)$.

Since $\frac{\partial f}{\partial y}$ is continuous, by Extreme Value Theorem we have 
$$\exists L,\qquad \left\lvert\frac{\partial f}{\partial y}  \right\rvert \leqslant L.$$
By Mean Value Theorem,
$$\left\lvert  \frac{f(t, y_i)-f(t, y_j)}{y_i-y_j}  \right\rvert \leqslant L $$
for all $t, y_i, y_j$.

So
$$\left\lvert f(t, y_i)-f(t, y_j)  \right\rvert\leqslant L \left\lvert y_i-y_j \right\rvert,$$
which is Lipschitz condition.

Since
$$e_{n+1} = e_n + h\left[ f(t_n, y(t_n))-f(t_n, y_n)\right] + d_{n+1},$$
We get
$$\left\lvert e_{n+1}\right\lvert \leqslant \left\lvert e_n \right\lvert + h\left\lvert f(t_n, y(t_n))-f(t_n, y_n)\right\lvert + \left\lvert d_{n+1}\right\lvert,$$
$$\left\lvert e_{n+1}\right\lvert \leqslant \left\lvert e_n\right\lvert + h L \left\lvert y(t_n) - y_n \right\lvert + \left\lvert d_{n+1}\right\lvert,$$
$$\left\lvert e_{n+1}\right\lvert \leqslant \left\lvert e_n ( hL + 1 )\right\lvert + \left\lvert d_{n+1}\right\lvert.$$
So
$$\left\lvert e_{n}\right\lvert \leqslant \left\lvert e_{n-1}\right\lvert ( hL + 1 ) + \left\lvert d_{n}\right\lvert.$$

Since $d_n$ is $O(h^2)$,
$$\exists C,\qquad \left\lvert d_n\right\lvert \leqslant Ch^2,$$
$$\left\lvert e_{n}\right\lvert \leqslant \left\lvert e_{n-1}\right\lvert ( hL + 1 ) + Ch^2.$$
$$\left\lvert e_{n}\right\lvert \leqslant Ch^2 \sum_{k = 0}^{n-1} (hL+1)^k .$$
$$\left\lvert e_{n}\right\lvert \leqslant Ch^2 \frac{(hL+1)^n - 1}{hL},$$
$$\left\lvert e_{n}\right\lvert \leqslant \frac{C}{L} h ((hL+1)^n-1),$$
$$\left\lvert e_{n}\right\lvert \leqslant \frac{C}{L} h (e^nhL-1),$$
$$\left\lvert e_{n}\right\lvert \leqslant \frac{C}{L} h (e^{L(T-t_0)}-1).$$
So $e_n$ is $O(h)$.

## Empirical convergence order

Assume the global error behaves asymptotically as
$$E(h) \approx Ch^k$$
$$ \ln E(h) \approx k \ln h + \ln C $$
We pick two different $h$: $h_1$, $h_2$ and corresponding global error $E_{h_1}$, $E_{h_2}$.
So
$$E_{h_1} \approx Ch_1^k$$
$$E_{h_2} \approx Ch_2^k$$
We get
$$ \frac{E_{h_1}}{E_{h_2}} \approx \frac{h_1^k}{h_2^k} $$
$$ \ln \frac{E_{h_1}}{E_{h_2}} \approx k\ln\frac{h_1}{h_2}$$
$$ k \approx \frac{\ln (E_{h_1}/E_{h_2})}{\ln(h_1/h_2)}$$
Consider
$$ p_{\text{obs}} = \frac{\ln (E_{h_1}/E_{h_2})}{\ln(h_1/h_2)} $$
As the step sizes enter the asymptotic regime, $p_{\text{obs}}$ should converge to the theoretical order $k$.

## Test equation and absolute stability

Consider $y'=\lambda y$:
$$ y_{n+1} = y_n + hf(t_n,y_n) = (\lambda h+1)y_n$$
$$ y_n = (\lambda h+1)^n y_0$$
$$ y(t) = e^{\lambda t} y_0$$

We first consider $y$ convergent to $0$ when $t->\infin$,
$$ \lim_{t \to \infty}  y(t) = 0.$$
We set
$$ \lim_{t \to \infty}  y_n = 0.$$
So
$$ \lim_{n \to \infty}  (\lambda h+1)^n = 0.$$
$$ \left\lvert\lambda h+1 \right\rvert < 1 $$
If we consider
$$ \lambda \in \mathbb{C},\qquad z = \lambda h $$
The Absolute Stability Region is
$$ S_{\text{Euler}} = \{z\in\mathbb C:|1+z|<1\}. $$


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
