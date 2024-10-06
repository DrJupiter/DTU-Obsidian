
Factorial design with k factors each at 2 levels.

Key assumptions:

- The factors are fixed (i.e don't vary with time)
- We have completely randomized designs
- Standard normality assumptions i.e noise is $\mathcal{N}(0,\sigma^2)$

- The response is approximately linear over the range of the factor levels chosen (response is the amount a factor contributes to what we are measuring.)

We have the main effect of a variable is the average effect of the variable over all its states isolated from the effect of the other variables.

### Example main effect for A and B (see notational fuckery)

**FOR SPECIFIC COMPUTATION TABLE SEE** [[5 (2) factor analysis]]

![[Pasted image 20241006195957.png]]
![[Pasted image 20241006200048.png]]

alternatively

![[Pasted image 20241006200219.png]]

### Total effect / contrast

![[Pasted image 20241006200429.png]]

### Key statistic for 2^K, k= 2

![[Pasted image 20241006200542.png]]

![[Pasted image 20241006200901.png]]


## Standard Order

Used for showing which level a factor is in an experiment, where -1 represents low and +1 represents high.
We then put the experiments into a matrix

### Orthogonal encoding/design matrix

An experiment with standard order is orthogonal if the matrix has orthogonal columns. *This helps with letting the variables be uncorrelated.*

## Effects encoding 

Relates to standard order.

It is a way of encoding the states of variables with more than two levels, they only show for 3, with -1 being a low presence, 0 being no presence, and +1 being a high presence.


## Notational fuckery

For to factor design
- (1) is the interaction of both factors on a low level.
- ab is both factors at a high level.
- a is A at a high level and B at a low level.
- and b is B at at a high level and A at a low level.




