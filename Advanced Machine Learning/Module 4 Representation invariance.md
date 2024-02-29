
The goal of the next three


![[Pasted image 20240229131035.png]]

# Setup for the modules

![[Pasted image 20240229131446.png]]

f will start deterministic, but end up being non-deterministic.

Our goal is to extract information from our latent space.

Our problem setup is that we want our representation to be robust.

## Identifiable model

![[Pasted image 20240229131931.png]]

This means there is a singular set of weights that fits each density.

Practically almost all generative models don't satisfy this constraint.

Let's show PCA doesn't satisfy this

### Why PCA is __not__ identifiable

![[Pasted image 20240229132248.png]]

Because PCA is has lower dimensionality, we cannot have unique parameterizations?

No it is because our PCA loss is not independent of rotation, so we have infinetely many good solutions.

#### Exercise Showing PCA is rotation invarient

![[Pasted image 20240229133249.png]]

Use Rotation identity and insert them into the norm and pull them out and have them cancel.

### Why VAEs are __non__ identifiable

Because we can apply transformations to the prior without changing the distribution

![[Pasted image 20240229135446.png]]

### A geometric solution to making models identifiable

![[Pasted image 20240229135700.png]]

![[Pasted image 20240229135751.png]]

f is the decoder here, and x is the latent space. The space mapped to is the observation space.

We define a length of a curve by decoding it and compute the length of the curve in the observation space and say that it is the length of the curve in the latent space.

#### A good enough definition of a manifold

![[Pasted image 20240229140209.png]]

##### Embedded manifold

![[Pasted image 20240229140248.png]]

##### Immersed manifolds

![[Pasted image 20240229140315.png]]

##### Manifold distances

![[Pasted image 20240229141109.png]]
![[Pasted image 20240229141129.png]]

##### Key take away

The length of curves in the latent space is defined in the constant observation space.
Thus our latent space distance will be invariant to deformations.

#### Curve length

![[Pasted image 20240229140618.png]]


![[Pasted image 20240229140639.png]]

##### Problems with curves and curve length


![[Pasted image 20240229140858.png]]

Squishing our lengthening our walk doesn't change our length.

__Proof__
![[Pasted image 20240229140928.png]]

## Important note on the curve length in manifolds

The way we obtain our curve c is via an optimization problem, usually done post hoc after training my decoder.

The optimization problem is considering all possible curves between my latent points and then fitting my curve to the one which produces the smallest distance in my decoder/observation space.

### We will parameterize our curves

fx 
Spline
https://en.wikipedia.org/wiki/Spline_(mathematics)

NN

