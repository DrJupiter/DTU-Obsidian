
## Sensitivity



__IS LITERALLY JUST THE GRADIENT OF THE LOSS W.R.T THE PARAMETERS OF INTEREST, WE CAN THEN TAKE THE NORM IF WE WANT A CONCRETE NUMBER__

The Lagrange multiplier ,$\lambda$, in 

![[Pasted image 20240213102455.png]]

tells us how much the minimization problem is influenced by the constraint it corresponds to.

The book argues

![[Pasted image 20240213102828.png]]



![[Pasted image 20240213134542.png]]


### Strong and weak activity

![[Pasted image 20240213102904.png]]

## Dual problems
## Lagrangian duality



![[Pasted image 20240213134107.png]]

For Equality constrains, the parameters are unconstrained.
## The active set method for QPs

![[Pasted image 20240213104837.png]]


![[Pasted image 20240213104752.png]]

## KKT Conditions

![[Pasted image 20240213113216.png]]


## Helpful

### Python Library to solve QPs

https://github.com/qpsolvers/qpsolvers

It can also just be done with Scipy's minimize.


