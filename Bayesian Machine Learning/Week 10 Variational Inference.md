
# Hamiltonian Metropolis sampling

Our setup is still knowing the target distribution up to some constant.
We augment the target distribution by a new parameter $\nu$.

$$p(\theta, \nu) \propto \tilde p(\theta) \mathcal{N}(\nu| 0, \Sigma)$$


To generate the next sample we do:

$$\theta_{0} = \theta_{k}, \nu_{0} \sim \mathcal{N}(\nu, \Sigma)$$
Then we loop over L integration steps and do

$$ \nu_{l} = \nu_{l-1} + \eta \nabla \log \tilde{p}(\theta_{l-1})$$
$$\theta_{l} = \theta_{l-1} + \eta \Sigma^{-1} \nu_{l}$$

Then we do $\theta* = \theta_{L}, \nu*=\nu_{l}$

Then we compute the acceptance probability, which we will threshold against a uniform distribution

$$ A_{k+1} = \min \left(1, ~\frac{p(\theta*,\nu*)}{p(\theta_{k},\nu_{k})}\right)$$

Our hyperparameters are the step-size, $\eta$, the covariance $\Sigma$, and the number of integration steps $L$.


# Variational inference

 Our goal is to approximate a posterior distribution 
$$ p(z|D) = \frac{p(D|z)p(z)}{p(D)}$$
We need 3 things:

-  A variational family, $Q$, of probability distributions which have the power to approximate $p$.
-  A distance measure/divergence between our family and our target distribution $p$.
-  Then we need a way to minimize the divergence _(usually SGD or smth.)_ 

Our loss/problem is thus

$$ q* = \underset{q \in Q}{\mathtt{argmin}} ~ \mathtt{Dist}(q\mid p) $$

## Examples of families

### Full rank Gaussian

$$q(z) = N(z|\mu, \Sigma)$$
### Mean-field Gaussian

Each index is independent of each other, thus

	$$q(z) = \Pi_{i=1}^D N(z_{i}| \mu_{i}, \Sigma_{i})$$
### General mean-field approximation

Each index is independent of each other, thus the distribution is fully factorized.

	$$q(z) = \Pi_{i=1}^D q_{i}(z_{i})$$

### Partially factorized approximations
Independent bins:

$$q(z) = \Pi_{i \in \mathtt{Bins}} ~ q_{i}(z_{i})$$

## Distance Measures

We will use the common Kullback-Leibler divergence

$$KL[q\mid p] = \int q(z)\ln \frac{q(z)}{p(z)} \, dz  $$
We know that $p = q \equiv KL[q \mid p] = 0$.
The divergence is also non negative, however it is not symmetric in general.

## Optimization of divergence

We use the ELBO on the KL

We will use the rewritten form for stability, that maximizes the propability of the data.

![[Pasted image 20240422101148.png]]
![[Pasted image 20240422101222.png]]

## Variational inference on factorized approximations for free form distributions

probably just summing the expectation when we apply log

![[Pasted image 20240422101534.png]]

here J is the bins.

### Coordinate/bin ascent/descent

We legit do loop optimization where we optimize one parameter at a time, we aren't guaranteed to converge this way btw, fuck this shit.

The step from expand product to marginalize is from that the function we are taking the exepectation over the log of q(z_j) only depends on z_j, and thus the rest of the distributions simply integrate to 1.


![[Pasted image 20240422102521.png]]

now for the first term

![[Pasted image 20240422102823.png]]

we could ELBO on this again, but we could also just set the two distributions equal to each other?

![[Pasted image 20240422103023.png]]

Thus our algorithm becomes

![[Pasted image 20240422103213.png]]

for

![[Pasted image 20240422103229.png]]

#### Example where he identifies a Gaussian update rule

![[Pasted image 20240422105318.png]]

![[Pasted image 20240422105259.png]]

# Mixture models

Mixture models are important in unsupervised learning ex clustering.

## The Gaussian Convex Sum


	$$p(x) = \sum_{k=1}^K \pi_{k}N(x|\mu_{k},\Sigma_{k}), \sum_{k=1}^K \pi_{k} =1, \pi_{k} \in [0,1] $$
	