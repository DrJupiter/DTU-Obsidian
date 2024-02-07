## Probabilistic machine learning

We are often interested in the joint distribution:

$$p(\theta,y) = p(y|\theta) \cdot p(\theta)$$

This is because it is equal to the posterior/conjugate prior divided by a normalization constant

$$p(\theta|y) = \cfrac{p(\theta, y)}{p(y)} $$
The joint distribution also lets us calculate this normalization constant, maybe quite obviously
in the sense that

$$ \int_{dom(\theta)} p(\theta,y) d\mu(\theta) = p(y)$$

## Plug-in approximation

### p(y*|y)
The goal of this approximation is giving an updated estimate for new observations given our previous observations.

We denote previous observations $y$ and the ones we want to predict $y^*$.

We are interested in 

$$ p(y^*|y) = \int_{\theta} p(y^*|\theta) \cdot p(\theta | y) d\theta$$
We get this equality from the assumption of y and y* being drawn from the same distribution in an independent fashion. So they are i.i.d in some way.

### Approximating p(y*|y)

If we assume there exists a single best parameter, $\theta$ given  $y$, then we think our distribution $p(\theta|y)$ collapses i.e it becomes a dirac delta distribution: $p(\theta|y) = \delta(\theta - \hat{\theta})$.

From earlier we know 


![[Pasted image 20240205093512.png]]


thus our integral is approximated as 

$$ p(y^*|y) = \int_{\theta} p(y^*|\theta) \cdot p(\theta | y) d\theta \approx \int_{\theta} p(y^*|\theta) \cdot \delta(\theta - \hat{\theta}) d\theta = p(y^*|\hat{\theta})$$

The drawback of this estimate is that we remove all of our uncertainty about the parameters, $\theta$, and this can lead to over confident estimations. _This is what is done in most of non Bayesian deep learning._

#### Plugin approximation gets better with more data.

![[Pasted image 20240205094059.png]]

## Grid approximation for non-conjugate models

A lot of the time computing the evidence, $p(y)$,  is intractable/infeasible.

We define some grid of points, which is a subset of the possible parameter values.
We evaluate the posterior or joint distribution at these grid points.

![[Pasted image 20240205101340.png]]

__Note we would only use Dirac delta distribution in integrals__

### Moments

![[Pasted image 20240205101659.png]]

### CDF

![[Pasted image 20240205101811.png]]
![[Pasted image 20240205101852.png]]

#### Example 

![[Pasted image 20240205102006.png]]

### Choosing a good grid

![[Pasted image 20240205102123.png]]

Diminishing returns for smooth distributions I suppose, ones that don't grow too quickly.

## Logistic regression

### Example with proportion with N independent trials.

#### The (conditional) independent model

![[Pasted image 20240205105759.png]]


##### Parameter distribution.

![[Pasted image 20240205105911.png]]

We then do a [[#Grid approximation for non-conjugate models]]

![[Pasted image 20240205111029.png]]

and we obtain the likelihoods for new observations.

## Terms

### Conjugate distribution

Distribution that when convolved result in one of the two distributions with updated parameters.


### Quantile function

Produces parameters required to result in some % of chance given the cdf. It is essentially the inverse of a cumulative density function.

### Credibility/confidence intervals

There are many ways to find them, but most often a central estimate is made.

![[Pasted image 20240205090638.png]]
_I suppose the center interval is close to the most compact interval min |x_0| - |x_1| s.t int x0 to x1 p(x) = %._

### Dirac delta

![[Pasted image 20240205093529.png]]

The third property is called the sifting property, because we only have density at $\mu$.

### Approximate inference methods

![[Pasted image 20240205101005.png]]
