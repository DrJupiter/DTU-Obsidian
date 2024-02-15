
Transform any distribution to another with diffomorphisms.
We can then sample from the base distribution by sampling from the transformed distribution and then using the inverse of our transformation.

## In practice

We need to calculate the determinant of the Jacobian of the inverse transformation.
We also need to calculate the inverse transformation and the transformation for sampling.

We do this by stacking a lot of functions, which we can do this for together.

We have a nice composite decomposition rule for the Jacobian.

### Functions

#### Affine coupling layers

Partition my variable into two sets one counting the first d variables the others the rest.

![[Pasted image 20240215093812.png]]
![[Pasted image 20240215093826.png]]

##### Determinant of the jacobian of an affine coupling layer

![[Pasted image 20240215093931.png]]



#### Permutation Layer

Permute the variables.

The jacobian, where there is a one on the places the variables were permuted to.

$(-1)^n = det(J)$

![[Pasted image 20240215094007.png]]

##### Checkerboard permutation

![[Pasted image 20240215094108.png]]

#### Smart optimization

![[Pasted image 20240215094129.png]]

Diminish the number of layers throughout the neural network over time.

Lower triangle neural network.


## The structure of a flow network



![[Pasted image 20240215093617.png]]


## Normalizing Flows

![[Pasted image 20240215093319.png]]

The base distribution will be normal, or the other way around.

### Learning normalizing flows

![[Pasted image 20240215093425.png]]


#### Requirements

![[Pasted image 20240215093447.png]]

##### Why is it called a normalizing flow

![[Pasted image 20240215093659.png]]

So u follows a normal distribution that we transform to the desired distribution of our data x.


## Data transformation: Dequantization - adding noise to datapoints

![[Pasted image 20240215094253.png]]

This helps bounding the loglikelihood and reduces the chance of overfitting. 
It is a form of regularization.


## Types of flows


![[Pasted image 20240215094343.png]]

![[Pasted image 20240215094353.png]]

## Combining flows and VAE

It can be quite useful to have the flow be the prior.
![[Pasted image 20240215094443.png]]


## Helpful

### Properties of a deteriminent of the jacobian

![[Pasted image 20240215093510.png]]

