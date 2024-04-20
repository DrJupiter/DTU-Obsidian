
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

