
# Recap

Expected calibration error

$$ ECE = \sum_{b=1}^{B} \frac{|B_b|}{M} \cdot |acc(B_b) - conf(B_b)|$$

The symbol B represents the bins.

### ECE for scalar regression

We use the cdf of $p(y*|y,x*) \equiv p(y*)$.

$$ F(\tau) = p(y* \le \tau)$$
We bin the cdf value axis.
The idea is to use the inverse  of the cdf


$$ \hat{p}(p) = \cfrac{\sum_{n=1}^{N} \mathbb{I}[y*_n \le F_n^{-1}(p)]}{N}$$
N is the size of the test/data set of $y*$.

extension for intervals

$$ \hat{p}(p_1, p_2) = \cfrac{\sum_{n=1}^{N} \mathbb{I}[F_n^{-1}(p_1) \le y*_n \le F_n^{-1}(p_2)]}{N}$$

# Markov chain Monte Carlo methods for handling integrals

Often we need to approximate the prior $p(y)$ or the distributions in the predictive posterior distribution

$$p(y*|x*,y) = \int p(y*|w,x*) p(w|y) dw $$

## Background

We need a method that scales that works via random sampling.

The monte carlo integration let's us approximate integrals.

The way they work are:

## How they work in an expectation framework

We want to compute some $$\bar f = E[f(w)]$$
We do so by sampling w from a distribution and by applying f and them summing and taking the mean.

The mean and variance of this estimater

	$$ \hat{f} = \frac{1}{S} \sum_{i=1}^S f(z_i), z_i~ i.i.d ~ \sim p(z)$$
$$E[\hat f] = \bar{f}$$
Thus the montecarlo estimator is unbiased.
The variance of the estimator is

$$V[\hat f] = \frac{1}{S^2} = V[\sum_{i=1}^S f(z_i)] = \frac{1}{S} V[f(z)]$$
Thus we can make the estimator more accurate by sampling more times.
We also see the variance is independent of the dimensionality of z, which is nice.

This result is exactly the law of large numbers for i.i.d samples.

For the monte carlo estimate the expected difference between the estimator and the true value is

	$$MCSE_f = \frac{1}{\sqrt{S}} \sqrt{V[f(z)]}$$
	
### Theoretical Example for the posterior predictive distribution

$$p(y*|x*,y) = E[f(x)], f(x) = p(y*|w,x*)$$

### Practical example

![[Pasted image 20240420181422.png]]


# Sampling methods

## Ancestral Sampling

### Example

![[Pasted image 20240420183303.png]]

We can do ancestral sampling by sampling in a tree like manner

where we sample from the outer most nodes and then sample at the next step and then so on.

So in this case it would be kappa into w, then sigma, and then w and sigma into y.

![[Pasted image 20240420183652.png]]

## Rejection sampling

This method requires knowing a distribution up to a normalization constant.

$$p(z) = \frac{1}{Z}\tilde p(z)$$
where we know $\tilde p(z)$.

Additionally we require a distribution

$$ \forall z ~ \tilde p(z) \le K \cdot q(z), K > 0 $$
We will be sampling from $q(z)$ _(this is a lot like the Laplacian approximation it seems to me)._

What we will do is sample z from q, then sample a uniform variable over the interval $u \sim \mathcal{U}[0, K \cdot q(z)]$, then evaluate if $u > \tilde p (z)$, if this is the case reject the sample, otherwise keep the sample z.

Con: In higher than a few dimensions, we will reject most things, but in 1d and 2d it works well.

## Importance sampling

We want to approximate an expectation over some complex distribution p.
We have access to an approximate distribution $q$ which is easier to evaluate.

We can rewrite our expectation as

$$ E_p[f(z)] = \int f(z)p(z)dz = \int f(z) \frac{q(z)}{q(z)} p(z) dz = E_q[f(z)\frac{p(z)}{q(z)}] $$
We can then approximate this via monte carlo integral approximation as

	$$ E_p[f(z)] \approx \hat f =  \frac{1}{S} \sum_{i=1}^S f(z_i) \frac{p(z_i)}{q(z_i)}, z_i \sim q(z)$$
The ratio between p and q is called _importance weights_.

$$ w_i = \frac{p(z_i)}{q(z_i)} $$
_q could be a laplace approximation._

the variance of this estimator is 

$$ \hat \sigma_q^2 = \frac{1}{S} \sum_{i=1}^S (w_i f(z_i) - \hat f)^2 $$

# Generating random numbers

Assume we can sample from a uniform distribution, $u \sim \mathcal{U}[0,1]$.

## Bernoulli

![[Pasted image 20240421113144.png]]

## Standard normal distribution

![[Pasted image 20240421113208.png]]

### Scale and change the location

![[Pasted image 20240421113226.png]]

## Exponential distribution

![[Pasted image 20240421113248.png]]

__in this course we assume we have it as a given that we can sample from distributions.__

# Markov Chain Monte Carlo methods

Markov methods extended to methods which aren't i.i.d.

These chains all have the markov property i.e the history only matters from our most recent point when predicting future points in the chain.

> This will help us in our sampling of points from distributions

__Example__

![[Pasted image 20240421131242.png]]

_the above situation is homogenous as the variance $e_k$ doesn't depend on k_

if the transition kernel doesn't depend on time/ an index set we say it is homogenous w.r.t that set.

### Design philosophy - invariant/stationary distributions for $p(z_t)$

We can calculate distributions over our variable over time with the sum rule

$$p(z_{t+1}) = \int p(z_{t+1}|z_t) p(z_t) d z_t$$

We want this result to be constant/have the same form of distribution independent of the index set.
If we meet this property we have an invariant/stationary distribution.

## The metropolis algorithm

We want to sample from a distribution $p(\theta)$, we have access to a symmetric distribution $q(\theta*|\theta^{k-1})$.

The algorithm works by

loop over some amount K given an initial parameter value $\theta_0$.

given the last value $\theta_{k-1}$ generate a sample from $\theta* \sim q(\theta*|\theta_{k-1})$.

compute a threshhold/acceptance probability $A_k$

$$ A_k = \min \left(1, \frac{p(\theta*)}{p(\theta_{k-1})}\right)$$

Sample from a uniform distribution $u_k \sim \mathcal{U}(0,1)$ and define the new parameter $\theta_k$ as follows

$$\theta_k = \begin{cases} \theta* \text{ if } u_k < A_k \\ \theta_{k-1} \end{cases}$$

As we are just evaluating the ratio to get our threshhold, this aids us as we just need to know our target density p up to a constant. An example of this is the posterior distribution:

![[Pasted image 20240421135247.png]]

so in essence, we are saying does our new sample have around the sameish density or greater of our target, if we are less dense then don't go there and if we are more dense go there, so this will lead us to higher density areas. This could be expanded with other terms to get a more wholesitic sample procedure.

