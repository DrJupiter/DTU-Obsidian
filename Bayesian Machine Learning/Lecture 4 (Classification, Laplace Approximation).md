
## Recap Predicting new data

![[Pasted image 20240219111232.png]]

![[Pasted image 20240219111406.png]]

![[Pasted image 20240219111756.png]]

Often we do MAP for hyperparameters as they are hard to marginalize over.


### Graphical models

![[Pasted image 20240219112229.png]]

So a circle means there is a distribution.
Shaded means we observe the variable.
An arrow means dependence.


## Probabilistic approaches for classification

### Overview

![[Pasted image 20240219114611.png]]

### Generative binary classification

![[Pasted image 20240219115040.png]]

![[Pasted image 20240219115050.png]]

#### Gaussian conditionals example

![[Pasted image 20240219115202.png]]

### Generative modelling multi-class classification

![[Pasted image 20240219115126.png]]



### Discriminative binary classification

![[Pasted image 20240219115439.png]]

### Discriminative multiclass classification

The same as generative, but only the conditional distribution, we don't model the data distribution.

## Bayesian logistic/sigmoid regression 


### Overview and problem

![[Pasted image 20240219120303.png]]

Problem: We can't calculate $p(y)$.

Let's approximate
![[Pasted image 20240219121513.png]]

### Laplace approximation






![[Pasted image 20240219122115.png]]

![[Pasted image 20240304113407.png]]


A slightly better approximation?

![[Pasted image 20240219121744.png]]

## Posterior predictive distribution with the laplace approximation


![[Pasted image 20240219123059.png]]

