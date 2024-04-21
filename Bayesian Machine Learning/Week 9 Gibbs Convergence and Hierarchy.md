
Our goal is to decouple modelling and inference.

# Gibbs sampling

You update one coordinate at a time for some multidimensional parameter z.

Notation: $z_i^j$ is the j'th component in vector i, __in his notation it's the i'th component in vector j__.

What we do is 

```python
z = [None]*K
z[0] = z0
indicies = np.arange(1,d)
for k=1..K:
	z[k] = z[k-1]
	for j=1..d:
		z[k][j] = sample p(z[k][j]|z[k][j != indicies])
	#z[k] = sample p(z[k]|z[k][...]) I don't think this part must be a type in his thingy, yes it is
```

![[Pasted image 20240421163854.png]]

> He shows that the gibs sampler is a special case of metropolis hastings where the proposed sample is always accepted


# Convergence diagnostics

When should we stop sampling?

Run multiple chains in parallel from different initializations.
After a number of iterations we compare the distributions, we are at.
If we are at different distributions, we haven't reached the stationary distribution yet.

A way of formalizing this is through the potential scale reduction factor.
	We measure the variance between the $N$ length chains, $B$, and the variance within the chains, $W$.

We then compute $$ \hat R^2 = \frac{N-1}{N} + \frac{1}{N} \frac{B}{W}$$
if the potential scale reduction factor is larger than 1 then there is more variance between the chains than within the chains. In practice if $\hat R^2 < 1.1$ we are good as the chains have mixed. _for really precise applications we might want $\hat R^2 < 1.01$._

## Quantifying the error of mcmc

We compute the auto correlation to find the effective sample size.
We rescale our variance estimate for the effective sample size.
![[Pasted image 20240421182553.png]]


# Hierarcical models

We add a distribution over everything we can within reason, i.e

![[Pasted image 20240421185836.png]]
the arrow comment is that we might have hyper parameters in the like likehood over the data i.e $p(D|\theta, \xi)$.

Due to the smaller amount of hyperparameters (usually), doing a hyper parameter optimization first can be quite robust.

Typically we start check and then go down the bayesian train in complexity if needed.

Priors over the hyperparameters can be used to impose losely constrained optimization for real though. If there is no prior it's a little like a uniform over the entire space.

