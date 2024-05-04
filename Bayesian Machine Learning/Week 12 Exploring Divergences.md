
# Variational inference at scale

## The support of the approximation of KL

From the equation for the KL

$$ KL[q || p] = \int q(z) \ln \left[\frac{q(z)}{p(z)}\right] dz $$
This equation discourages situations, where q is large and p is small, because this causes the KL to blow up. Thus q's support is pushed to be similar to p's.
This obviously means that generating new samples is hard without some extrapolation in space by the model, probably also why training for an approximation is sometimes a better fit.

If we compare $KL[q||p]$ to $KL[p||q]$, then the first is more mode seeking, thus q tries to match p where p has the highest probabilities, compared to low values.

The second covers more mass, because it is weighted by p in the sense that q will balance out p by when p is large q needs to be too otherwise the KL will blow up, and when p is small then if q is large the values will actually be small too is fine.

If the distribution you are trying to approximate is multimodel, your family should also be for $KL[q||p]$, because otherwise we will just cover one of the modes. The mass covering one might be a better fit in these casses.

## Alpha divergence

$$D_{\alpha}[p||q] = \frac{1}{\alpha ( 1- \alpha)} \int \alpha p(z) + (1-\alpha) q(z) - p(z)^{\alpha} q(z)^{1-\alpha} dz $$
Apperently the limit of this for $\alpha$ approaching $0$ and $1$ is 

$$\lim_{\alpha \rightarrow 0} \rightarrow KL[q||p]
$$

$$\lim_{\alpha \rightarrow 1} \rightarrow KL[p||q]$$

It's like an interpolation between the two KL divergences, I suppose.

For $\alpha=\frac{1}{2}$ we get the _Hellinger distance_


$$D_{\frac{1}{2}}[p||q] = 2 \int \sqrt{p(z)} - \sqrt{q(z)} dz $$
![[Pasted image 20240503104055.png]]

## Connection between ML and KL

The KL between the data and a parameterized estimate is


$$ \text{argmin}_\theta KL[p_D(x) || p(x|\theta)] \approx \text{argmax}_{\theta} \sum_{n=1}^N \log(p(x_n)|\theta) $$

Thus it becomes the ML estimate as N goes to infinity.

## Information gain

He says that a result in information gain is the KL divergence between the posterior and the prior over the parameters:

$$ KL[p(w|D)|| p(w)] $$

This can be useful in active learning (sample label constrained learning.)

## Black box fixed form variational inference

Goal evaluate elbo, and gradient of elbo.

We consider our evidence lower bound (elbo)

$$ L[q] = \mathbb{E}_q[\ln(p(y,w))] - \mathbb{E}_q[\ln(q(w))] = E_q[\ln(p(y,w))] + \mathcal{H}(q)$$
$\mathcal{H}$ is the entropy of q often we can look this up, and also calculate the gradient easily.

We will thus focus on the expectation of the log joint term.

Usually we know the joint, so we can usually do a montecarlo estimate over the expectation over the log joint, which is an unbiased estimate. 

Usually we can also just calculate the gradients through this.

Thus will be valid from Leibniz' rule for measureable functions assuming we use functions which meet the conditions below:

![[Pasted image 20240503112728.png]]

Thus we can approximate the gradient of the integral as the integral of the gradient, which helps us with approximating it in the sum form.

We have thus arrived at

$$ \nabla_{\theta} \mathbb{E}_{q_{\theta}}[\log ( p(y,w))] = \nabla_{\theta}\int q_{\theta}(w) \log p(y,w) d w = \int\nabla_{\theta} q_{\theta}(w) \log p(y,w) d w$$ 
Instead of sampling the gradient from the montecarlo estimator, we are instered in sampling the gradient directly, however the gradient of the distribution is not sampling we can sample directly as it is not a distribution. We will tackle this now

In the following derivation we see that the gradient of any distribution of the setup can be sampled like this:

![[Pasted image 20240503152154.png]]

![[Pasted image 20240503152302.png]]

A down side of this estimator is that it usually has a high variance, thus yielding a harder optimization problem.

but also the log p could have been any function or distribution (obvously independent of the parameters.)

### Example for a mean field Gaussian

A mean field gaussian has a diagonal covariance.

We initialize with some parameters.

Then we sample the gradient at these parameters and update them in an SGD fassion.

We then continue to loop like this until we decide we are done/have converged.

!Note in his slide here there is no reason to actually waste computation on calculating the loss, rather just calculate the gradient estimate:

![[Pasted image 20240504161815.png]]

And then calculate the loss occasionally.

![[Pasted image 20240504162703.png]]

The student t distribution is better here, because we avoid outliers more.

## Ways to make stochastic optimization better

![[Pasted image 20240504163006.png]]

![[Pasted image 20240504163017.png]]

## Reparameterization for more robust optimization/lower variance

For normal distributions, we can sample from a standard normal and then shift them by our parameters to sample a normal distribution, this is more stable than sampling directly and then estimating the gradient.

![[Pasted image 20240504163127.png]]

We can also re-parameterize other distributions

![[Pasted image 20240504163254.png]]

The idea is that we put our parameters into the expectation of the function, we are trying to approximate.

## Mini batching for scaling to large datasets

![[Pasted image 20240504164119.png]]

Sample the dataset and then rescale the sample if you can assume the blocks of your data are i.i.d.

