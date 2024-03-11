
# Riemann metrics

## Tangent spaces

![[Pasted image 20240307131716 1.png]]

![[Pasted image 20240307131813 1.png]]

### Local inner products

![[Pasted image 20240307132137 1.png]]
![[Pasted image 20240307132459 1.png]]


The delta vectors are infinitesimal vectors.

This is a key point in differential geometry, having local inner products.

![[Pasted image 20240307132443 1.png]]

## The actual metric

![[Pasted image 20240307132538 1.png]]
![[Pasted image 20240307132558 1.png]]
![[Pasted image 20240307132609 1.png]]


## Abstract representation


Just construct your own local Rieman measure.

Here is an example of a simple density aware one.
![[Pasted image 20240307133306 1.png]]



# Applying Riemannian metrics

> We have local approximations. How do we use them globally?

## Geodesics - The shortest path

The path which results in the minimum length for a given measure.

A problem with this minimization problem is that we are not guaranteed uniqueness. We can do infinetly many parameterizations of that curve.

The speed fucks us over in the sense we must make a discrete approximation of the curve.
The continuous curve stays the same, but a discrete approximation is very dependent on where we have our points and how we connect them.

### Solution to the invariant parameterization of curves

One approach is to require constant speed

![[Pasted image 20240307141744 1.png]]

#### Curve energy

![[Pasted image 20240307143411 1.png]]

![[Pasted image 20240307143710 1.png]]

So if we actually arrive at the optimal solution i.e, we have equality, we will have constant speed.

## Making curves

![[Pasted image 20240307143926 1.png]]

### Choices
![[Pasted image 20240307145016 1.png]]

![[Pasted image 20240307145034 1.png]]
![[Pasted image 20240307145043 1.png]]

### Example a sphere - Don't expect uniqueness for geodesics.

![[Pasted image 20240307133721 1.png]]

Takeaway: Don't expect uniqueness

## Geodesic ODE / shooting geodesic

![[Pasted image 20240307145421.png]]
Shortest paths satisfy the differential equation above.

This is useful in the sense of abstracting our idea of a shortest paths.

![[Pasted image 20240307145605.png]]

Take away given an initial direction and a way to guide us, we end up with a unique path.
