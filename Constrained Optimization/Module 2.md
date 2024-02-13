
## Lagrangian

![[Pasted image 20240206140753.png]]

## 1st order KKT conditions
![[Pasted image 20240206162905.png]]


## Active set algorithm

The Active Set method is an iterative approach used to solve constrained optimization problems. It involves identifying the set of constraints that are active at the solution (the active set) and solving the resulting equality-constrained problem.

Given the optimization problem:

$$
\begin{align*}
\text{minimize}\quad & f(x) = g^T x \\
\text{subject to}\quad & c(x) = Ax - b \geq 0
\end{align*}
$$

The constraints are given by$c(x) = Ax - b$ where $A$ is the matrix of constraint coefficients and$b$is the vector of bounds. The active set at a given point$x$includes all constraints that are equal to zero at$x$.

In matrix form, the constraints are:

$$
\begin{align*}
c_1(x) &= x_1 \geq 0 \\
c_2(x) &= x_2 \geq 0 \\
c_3(x) &= x_1 - x_2 \geq -2 \\
c_4(x) &= x_1 - 5x_2 \geq -20 \\
c_5(x) &= -5x_1 + x_2 \geq -15
\end{align*}
$$

To determine the active set from the contour plot, we would look for which constraints are binding at the optimal solution. A binding constraint is one where the inequality is satisfied as an equality at the optimal solution.

The contour plot would show us the feasible region, and typically the optimal solution would be at a vertex of this region or along a binding constraint boundary. Unfortunately, the active set cannot be determined solely from the contour plot provided earlier because it does not show the specific points or vertices of the feasible region.

To identify the active set, we usually need to:

1. Start with an initial feasible point $x_0$.
2. Determine which constraints are active at $x_0$ (i.e., those for which$c_i(x_0) = 0$).
3. Solve the quadratic programming subproblem that minimizes the objective function while only considering the active constraints as equalities.
4. Check if the solution found is feasible for the original problem.
5. If not all constraints are satisfied, update the active set by adding or removing constraints and repeat the process.

For the given problem, the equations we'd solve at each iteration of the active set method would look something like this:

$$
\begin{align*}
\text{minimize}\quad & f(x) = g^T x \\
\text{subject to}\quad & A_{\text{active}}x = b_{\text{active}}
\end{align*}
$$

where$A_{\text{active}}$and$b_{\text{active}}$are the rows of$A$and$b$that correspond to the active constraints. The solution to this system would give us the point that minimizes the objective function over the current active set. If this point does not satisfy all of the original constraints, we modify the active set accordingly and solve again. This process is repeated until we find a point that minimizes the objective within the entire feasible region.

