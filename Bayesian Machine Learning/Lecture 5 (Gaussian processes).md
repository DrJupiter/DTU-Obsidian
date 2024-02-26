
##  Parametric models (Recapish)

![[Pasted image 20240226093133.png]]

parametric models have a finite amount of parameters regardless of the amount of data.
## From a parametric model to function spaces

![[Pasted image 20240226093233.png]]

$e_n$ is standard isotropic Gaussian noise.

![[Pasted image 20240226093347.png]]

We end up with f following a normal distribution with the parameters as given above.

![[Pasted image 20240226093809.png]]

this basically just means we sample from our distribution over f to generate a prediction from f.

![[Pasted image 20240226093914.png]]

the derivation of the covariance of f.

![[Pasted image 20240226094106.png]]

### The effect of different covariance matrix on our models

![[Pasted image 20240226094316.png]]

### Visualizing samples in higher dimensions

![[Pasted image 20240226094818.png]]

Each colored curve is a sample. Thus our kernels sort of represent different curves.

### Sampling when we have or impose some information (Conditioning)

![[Pasted image 20240226095019.png]]

This lets us have our curve be in certain ways.

![[Pasted image 20240226095106.png]]

We also notice that fitting and predicting these kernel functions allows us to do non-linear regression.

# Formal definition of a Gaussian process

![[Pasted image 20240226095258.png]]

![[Pasted image 20240226095314.png]]

## Linear Gaussian system

![[Pasted image 20240226100343.png]]

so we have $y = Wz + b$.

## Conditioning for a multivariate Gaussian

![[Pasted image 20240226100435.png]]

## Making a prediction

![[Pasted image 20240226100615.png]]

![[Pasted image 20240226100627.png]]

![[Pasted image 20240226100646.png]]

### Example

![[Pasted image 20240226100829.png]]


## Kernels / Covariance matrices

### Restrictions

![[Pasted image 20240226101131.png]]

### Constructing new kernels

![[Pasted image 20240226101239.png]]


### Hyper parameter optimization in a smart way


#### The setup

![[Pasted image 20240226104913.png]]

![[Pasted image 20240226105001.png]]

#### Smartly optimizing the log likelihood

![[Pasted image 20240226105036.png]]

## Computational complexity of a GP

![[Pasted image 20240226105121.png]]






