
## Example Classical vs Bayesian

	1. A model

$$f(x)$$

![[Pasted image 20240129105834.png]]

The classical approach converges to one model, however due to a finite amount of data our parameters are an approximation. With Bayesian machine learning, we want to model our uncertainty about these parameters.

### Inference in Bayesian machine learning

![[Pasted image 20240129110057.png]]


## Scalar distribution rules

![[Pasted image 20240129110830.png]]


## A/B Testing with a stochastic process where each variable follows a Bernoulli distribution

[bernoulli]
![[Pasted image 20240129111411.png]]

[binomial]

![[Pasted image 20240129111733.png]]

![[Pasted image 20240129111818.png]]
![[Pasted image 20240129111846.png]]

### Example of doing bayesian machine learning for binomial distribution

![[Pasted image 20240129112058.png]]
![[Pasted image 20240129112208.png]]

As we collect more data, we can update our estimates and thus our model.

![[Pasted image 20240129112305.png]]

## Tips for choosing our prior distribution over our parameters

![[Pasted image 20240129112539.png]]


## Beta distribution

![[Pasted image 20240129112702.png]]
*In [Bayesian inference](https://en.wikipedia.org/wiki/Bayesian_inference "Bayesian inference"), the beta distribution is the [conjugate prior probability distribution](https://en.wikipedia.org/wiki/Conjugate_prior_distribution "Conjugate prior distribution") for the [Bernoulli](https://en.wikipedia.org/wiki/Bernoulli_distribution "Bernoulli distribution"), [binomial](https://en.wikipedia.org/wiki/Binomial_distribution "Binomial distribution"), [negative binomial](https://en.wikipedia.org/wiki/Negative_binomial_distribution "Negative binomial distribution"), and [geometric](https://en.wikipedia.org/wiki/Geometric_distribution "Geometric distribution") distributions.*

### Functional form of the beta distribution

![[Pasted image 20240129112907.png]]

### Analytical posterior for the beta prior

![[Pasted image 20240129112947.png]]

### The posterior mean of the beta distribution

![[Pasted image 20240129113157.png]]

## Calculating posterior summaries in practice

![[Pasted image 20240129113251.png]]


## Terms

### Types of uncertainty

Epistemic/reducible uncertainty: is from lack of knowledge i.e lack of data points

Aleatoric/irreducible uncertainty: is from inherent randomness in the distribution of the data.

### Bayes rule

$$
\begin{align}
p(w|y) = \cfrac{p(y|w)*p(w)}{p(y)}
\end{align}
$$
The different terms of the names, posterior, likelihood, prior over w, and prior over y.

### Mode

![[Pasted image 20240129112402.png]]

### Expectation

![[Pasted image 20240129112428.png]]

### Confidence interval for scalar parameter

![[Pasted image 20240129112451.png]]
