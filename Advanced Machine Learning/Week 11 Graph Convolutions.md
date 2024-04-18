
# Convolutions and Fourier Transform

## Convolutions

![[Pasted image 20240418130624.png]]


![[Pasted image 20240418130636.png]]

Circular convolution has some loop over N from the mod N, N is the total length of the signal.
All the columns are just shifted by one, then up to N times.

## Fourier transform

![[Pasted image 20240418130939.png]]

### Filtering/Convolutions in fourior domain

![[Pasted image 20240418131707.png]]
![[Pasted image 20240418131721.png]]

### Exploring the basis

![[Pasted image 20240418131914.png]]

## On graphs

![[Pasted image 20240418132154.png]]

![[Pasted image 20240418132720.png]]

![[Pasted image 20240418133037.png]]
here the mlp is element wise/node wise.

#### The MLPs

X -> node features
Every node feature goes through the same MLP.




### Eigenvalue decompostion of graphs


#### Graph fourier transform

![[Pasted image 20240418132509.png]]


#### Cyclic graphs

![[Pasted image 20240418132237.png]]



# GNNs and probabilistic models

![[Pasted image 20240418133718.png]]


![[Pasted image 20240418133711.png]]

![[Pasted image 20240418134012.png]]

### Mean field variational inference

![[Pasted image 20240418134138.png]]

initialize the q's then iterate until convergence.

![[Pasted image 20240418134540.png]]

# Generative models

![[Pasted image 20240418140653.png]]

![[Pasted image 20240418140819.png]]

### Vae problems

![[Pasted image 20240418142237.png]]

### GANs

![[Pasted image 20240418142743.png]]
![[Pasted image 20240418142754.png]]

## Evaluating graphs

![[Pasted image 20240418143019.png]]
