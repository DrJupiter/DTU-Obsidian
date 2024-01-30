## General constrained optimization formulation

We optimize in subsets of the real domain.

We concern ourselves with an objective function: $f: \mathbb{R}^n \mapsto \mathbb{R}$
We denote our constraint functions as: $c_i: \mathbb{R}^n \mapsto \mathbb{R}$
The index, i, spans an equality set and an inequality set denoted $\mathcal{E}, \mathcal{I}$ so $i \in \mathcal{E} \cup \mathcal{I}$.

We require all the functions to twice continuously differentiable for [smooth problems].

We then have the formulation

![[Pasted image 20240130113810.png]]

our with vector functions $g,h$.

![[Pasted image 20240130113841.png]]

### Nonlinear program (NLP)

Is an optimization problem where we allow the functions all the functions $(f,c_i)$ to be non-linear.

### Convex program

We require the [[#Feasible region]] to be [[#convex]] and the objective function, $f$, to be [[#convex]] too.

From this restriction, we can infer additional restrictions on the constraint functions, $c_i$ , on the program.

The equality constraints must be affine transformations and the inequality constrains must be concave i.e the negative of them must be convex.

![[Pasted image 20240130115913.png]]

#### Convex Quadratic Program (QP)

![[Pasted image 20240130120109.png]]

$H \succeq 0$, means $H$ is [[#Positive Semi-definite]].

#### Linear Program (LP)

![[Pasted image 20240130121327.png]]

![[Pasted image 20240130121403.png]]

Linear programs (1.32) are solved using either an interior-point algorithm or the simplex algorithm
## Terms

### Positive Semi-definite

Positive-definite and positive-semidefinite matrices can be characterized in many ways, which may explain the importance of the concept in various parts of mathematics. A matrix M is positive-definite if and only if it satisfies any of the following equivalent conditions.

- M is [congruent](https://en.wikipedia.org/wiki/Congruent_matrices "Congruent matrices") with a [diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix "Diagonal matrix") with positive real entries.
- M is symmetric or Hermitian, and all its [eigenvalues](https://en.wikipedia.org/wiki/Eigenvalue "Eigenvalue") are real and positive.
- M is symmetric or Hermitian, and all its leading [principal minors](https://en.wikipedia.org/wiki/Principal_minor "Principal minor") are positive.
- There exists an [invertible matrix](https://en.wikipedia.org/wiki/Invertible_matrix "Invertible matrix") $B$ with conjugate transpose $B^*$ such that $M = B^*B$

A matrix is positive semi-definite if it satisfies similar equivalent conditions where "positive" is replaced by "nonnegative", "invertible matrix" is replaced by "matrix", and the word "leading" is removed.

### convex

#### convex set

![[Pasted image 20240130115348.png]]
#### convex function

![[Pasted image 20240130115400.png]]

#### strictly convex function

![[Pasted image 20240130115517.png]]

### Feasible region

![[Pasted image 20240130114309.png]]

### Minimizer

A minimizer is : a solution to a constrained optimization problem.

A global minimizer is the solution, which results in the smallest value of the objective function.

![[Pasted image 20240130114545.png]]

### Changing between max and min

![[Pasted image 20240130114711.png]]

![[Pasted image 20240130114917.png]]







