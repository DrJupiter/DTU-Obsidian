
We have a high dimensional representation $x \in \mathcal{X}^D$.
We want to map this high dimensional representation to a lower dimension manifold $\mathcal{Z}^M$.
We call this mapping an encoder : $E: \mathcal{X}^D \mapsto \mathcal{Z}^M$, $M < D$.
We want both of our spaces to be measurable with a probability measure, and thus we have a notion of probability distributions $z \sim p(z), x \sim p(x|z)$.

We use are assumption of probability spaces to marginalize over our lower dimension manifold $\mathcal{Z}^M$ and recover an expression for the distribution over our higher dimensional manifold $\mathcal{X}^D$.

$$ p(x) = \int_{\mathcal{Z}^M} p(x|z) \cdot p(z) d\mu(z)$$

This integral won't always be possible to calculate, in which case we approximate it.

### Example: Probabilistic Principal Component Analysis

We let the lower dimensional manifold be $\mathcal{Z}^M = \mathbb{R}^M$.
The higher dimensional manifold is $\mathcal{X}^D = \mathbb{R}^D$.

We assume the lower dimensional manifold is standard normally distributed i.e $p(z) = \mathcal{N}(z| 0, I)$.
We want to create a model for the higher dimensional manifold $\mathcal{X}^D$ to obtain the distribution $p(x|z)$.

The model we choose is:

$$ f(z| W, b) = Wz + b + \epsilon$$
$$\epsilon \sim \mathcal{N}(0, \sigma^2 I)$$

and we assume it is possible to have $f(z| W, b) = x$, in this model we map a fixed z to some fixed x and the randomness is only in $\epsilon$.

We can thus describe the conditional distribution over the higher dimensional manifold given the lower dimensional manifold, $p(x|z)$ 

$$ p(x|z) = \mathcal{N}(x| Wz+b| \sigma^2 I) $$

We can then recover $p(x)$

![[Pasted image 20240201105521.png]]

We can also recover $p(z|x) = \cfrac{p(x|z) \cdot p(z)}{p(x)}$.

![[Pasted image 20240201105705.png]]

We could also recover this distribution by applying the inverse of $f(z|W,b)$ to $x$ and see which distribution $z$ then follows.

This is nice, because it tells us how to morph the manifold $\mathcal{Z}^M$ to match our higher dimensional manifold $\mathcal{X}^D$.

### Example: Variational auto-encoders (non-linear models)

Suppose we apply some non-easily measurable transformation to our lower dimensional manifold $\mathcal{Z}^M$.
We hypothesize our model is a homomorphism between our higher dimensional space $\mathcal{X}^D$ and our lower dimensional space $\mathcal{Z}^M$.

$$ \phi(z|\Theta) = x $$
And we can't calculate the distribution over (x|z) easily.
![[Pasted image 20240201110626.png]]

or maybe we can

I practice, we learn the parameters for the distribution, we are going to sample from with our model $\phi$.

#### Issues with VAE

![[Pasted image 20240201145003.png]]

If this happens it is an issue, because our distribution $q$ is essentially useless, and we might as well have used a latent variable model.
This the stochastic variables $z$ and $x$ are independent.

![[Pasted image 20240201145326.png]]

![[Pasted image 20240201145407.png]]

_the same thing can happen to GANS_.

#### Fixes for issues

![[Pasted image 20240201145759.png]]

The function $\mathbb{H}$ is the entropy.

![[Pasted image 20240201150020.png]]

![[Pasted image 20240201150243.png]]

Another way to get a more flexible prior:

![[Pasted image 20240201150403.png]]

![[Pasted image 20240201150650.png]]
