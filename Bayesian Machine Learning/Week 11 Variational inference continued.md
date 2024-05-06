
# Big picture

We have a model 

$$p(y|w)$$ and some priors $p(w)$ 

our model is too complex to compute the posterior, so we want to approximate it.

We are searching within a family of distributions with a distance/divergence measure, and we minimize this divergence over our family.

# ELBO for deconstructed/factorized likelihood.

We suppose we have a model:

$$p(y,w) = \Pi_{n=1}^N p(y_{n}|w) \cdot p(w)$$

We have the elbo

$$L[q] = \mathbb{E}_{q}[\ln p(y,w)] - \mathbb{E}_{q}[\ln q(w)] $$

Inserting our distribution, we arrive at

$$L[q] = \sum_{n=1}^N \mathbb{E}_{q}[\ln p(y_{n}|w)] - \mathbb{E}_{q} [\ln \frac{q(w)}{p(w)}] = \sum_{n=1}^N \mathbb{E}_{q} [\ln p(y_{n}|w)] -\text{KL}[q(w)\mid p(w)]$$

# Free-form and fixed-form variational inference


## Last week for factorized variational inference

Free form factorized approximation for approximating the posterior

yielded the following

![[Pasted image 20240501120509.png]]

## Fixed form

In this form, we give up on searching for the optimal form, but instead do a parameter search over a family of distributions.

The parameters we search over are called the _variational parameters_.

Note the change from optimizing over a function space to a parameter space.

!! IDEA HOW DO OPTIMIZE OVER FUNCTION SPACES? !!
### Example a gaussian family

Here the parameters are the mean and the covariance matrix.

A full rank gaussian requires a d by d matrix for the covariance.

A low-rank gaussian of rank k requires a D by K matrix and a Diagonal matrix C
	$$ N(w|m, \mathbf{B} \mathbf{B}^T + \mathbf{C}^2)$$

A mean field gaussian is one with a fully diagonal covariance matrix

#### Example full rank gaussian

![[Pasted image 20240501121629.png]]

# Hyperparameter estimation in a variational framework

We assume we have a variational approximation over our parameters

$$p(\theta| y, \xi) \approx q(\theta) $$
for our setup

$$p(\theta| y, \xi) = \frac{p(y|\theta, \xi)\cdot p(\theta|\xi)}{p(y|\xi)}$$

![[Pasted image 20240501122256.png]]

# Scaling GP with variational inference


## Inducing points

Inducing points for M << N where N is the size of the data.
![[Pasted image 20240501123220.png]]


![[Pasted image 20240501123711.png]]

We are going to use these points U to get a better idea of what the f points should be.

We can choose points by randomly choosing and then optimizing their positions by the ELBO, which would just be another hyperparameter.
### Derivations on how to do variation approximation

##### The family for posteriors
![[Pasted image 20240501124407.png]]

##### Approximate posterior

![[Pasted image 20240501124631.png]]

##### The ELBO

![[Pasted image 20240501125133.png]]

![[Pasted image 20240501125420.png]]
![[Pasted image 20240501125914.png]]

![[Pasted image 20240501130032.png]]

![[Pasted image 20240501130210.png]]

##### We can actually solve for the solution

![[Pasted image 20240501130443.png]]

##### The big picture

![[Pasted image 20240501131956.png]]

