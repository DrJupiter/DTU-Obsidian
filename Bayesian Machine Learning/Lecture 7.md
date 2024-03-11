
## Recap

![[Pasted image 20240311083240.png]]
Red is epistemic uncertainty, blue is alleotoric uncertainty that comes from the decision boundries between our known labels.

## Infinitely wide neural networks - The neural network with Gaussian priors is a GP

![[Pasted image 20240311083639.png]]

![[Pasted image 20240311083733.png]]

Knn is the covariance function of the neural network.

! This holds for the structure presented i.e linear layer into activation function and repeat. !

## Common distributions in ML

![[Pasted image 20240311084428.png]]

## The generalized linear model to let any distribution be parameterized by a linear transformation

### Link function

![[Pasted image 20240311085055.png]]

#### Example with Poisson distribution

![[Pasted image 20240311085148.png]]

![[Pasted image 20240311085246.png]]

We have a guassian prior and use a laplace approximation to get p(w|y).

![[Pasted image 20240311085657.png]]


## Adapting a generalized GP (or NN of type from before)

![[Pasted image 20240311085538.png]]

### The laplace transform on generalized GP (I suppose)

![[Pasted image 20240311085557.png]]

## Evaluating our models and loss

### Cross validation

![[Pasted image 20240311090945.png]]

### The risk

![[Pasted image 20240311091024.png]]

#### Estimating the risk

![[Pasted image 20240311091051.png]]

##### Example for linear model

![[Pasted image 20240311091132.png]]

Above is the approximation, below is the expected value.

![[Pasted image 20240311091205.png]]



## Uncertainty in multiclass classification


![[Pasted image 20240311091336.png]]

Above is the setup, below is the uncertainty

![[Pasted image 20240311091405.png]]

### Giving predictions and rejecting because of too high uncertainty

![[Pasted image 20240311091444.png]]

## Bayesian decision theory


![[Pasted image 20240311091600.png]]

### Example for computing the utility 

![[Pasted image 20240311091622.png]]

### Example for binary classification

![[Pasted image 20240311091726.png]]

![[Pasted image 20240311091741.png]]

### For regression

![[Pasted image 20240311091848.png]]

#### The impact of different norms

![[Pasted image 20240311091926.png]]

## Measuring calibration of models (how good they are)

### Expected calibration error

![[Pasted image 20240311092118.png]]

#### Example

![[Pasted image 20240311092142.png]]
