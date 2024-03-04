

## Recap a model transformation marginalized over its weights

![[Pasted image 20240304072854.png]]

![[Pasted image 20240304073107.png]]

We model the randomness of f is a gaussian proccess.

with a covariance function being valid if it is positive semi-definite, but in reality if we wan't to calculate a meaningful density in the full dimension over x it should be positive definite at the points for which we wish it to be.

![[Pasted image 20240304073230.png]]

a stationary covariance is one which only depends on the distance between two points, and an isotropic one is one with scalar variance/the same variance in all directions, he says one which only depends on the norm of the difference, between the two points.


## Feature expansions

The non-linear function, which we apply to our data is the feature expansion.

![[Pasted image 20240304073915.png]]

Take away: upping our dimension can make our features linearly separable.

### The feature expansions effect on the kernel of a linear function

![[Pasted image 20240304074256.png]]

They are interconnected by mercer's theorem. So we can derive one from the other.

#### An example of a connection between the kernel and feature transformation

![[Pasted image 20240304074517.png]]

## Gaussian processes in practice

Here is a list of frameworks

![[Pasted image 20240304080016.png]]

## Gaussian processes for classification

### The feature transformed linear model with Bernoulli plus sigmoid to GP


![[Pasted image 20240304090326.png]]

Sigmoid vs CDF: sigmoid handles outliers better, but CDF comes with a tractable integral.

#### The framework

![[Pasted image 20240304090628.png]]

###### Computing the framework

![[Pasted image 20240304090756.png]]

![[Pasted image 20240304090835.png]]

	$$ \mathbf{k} = \mathtt{Kernel}(x*,x), k = \mathtt{Kernel}(x*,x*)$$
	


The result above holds in general, I do believe.
The next one is for our specific distribution, but hey we can always adapt it.
![[Pasted image 20240304090949.png]]

###### Summery 

![[Pasted image 20240304091235.png]]

### Using a neural network

![[Pasted image 20240304091411.png]]

![[Pasted image 20240304091446.png]]

#### The loss, and pros and cons

![[Pasted image 20240304091555.png]]


