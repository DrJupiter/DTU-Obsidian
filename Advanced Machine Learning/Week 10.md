
# Message passing

A sequential spreading algorithm

## High level overview

![[Pasted image 20240411131205.png]]

## Mathematics

![[Pasted image 20240411131220.png]]

### A basic example

![[Pasted image 20240411131517.png]]

## Aggregation functions

![[Pasted image 20240411132100.png]]

Note the mean can make us loose information ex (mean(a+b) = mean(a+b+a+b)).

![[Pasted image 20240411132220.png]]

Janossy pooling is permutation invariant on average, but not by itself.
![[Pasted image 20240411132758.png]]

## Making the architecture deeper

### Problem Over smoothing

![[Pasted image 20240411132922.png]]

#### Solutions for the update function

![[Pasted image 20240411133219.png]]

##### GRU Gating

![[Pasted image 20240411133625.png]]

## Generalized message passing

![[Pasted image 20240411133858.png]]

## Types nodes

![[Pasted image 20240411135606.png]]

## Design Invariance and Equivariance

![[Pasted image 20240411141804.png]]

![[Pasted image 20240411142627.png]]

# Pytorch Implementation

![[Pasted image 20240411142846.png]]

