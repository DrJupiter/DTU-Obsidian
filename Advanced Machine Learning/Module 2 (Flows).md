
Transform any distribution to another with diffomorphisms.
We can then sample from the base distribution by sampling from the transformed distribution and then using the inverse of our transformation.

## In practice

We need to calculate the determinant of the Jacobian of the inverse transformation.
We also need to calculate the inverse transformation and the transformation for sampling.

We do this by stacking a lot of functions, which we can do this for together.

We have a nice composite decomposition rule for the Jacobian.

### Functions

#### Affine coupling layers

Partition my variable into two sets one counting the first d variables the others the rest.

Questions: How do I choose a good partition?

#### Permutation Layer

Permute the variables.

The jacobian, where there is a one on the places the variables were permuted to.

$(-1)^n = det(J)$


