

![[Pasted image 20240411144718.png]]

![[Pasted image 20240411150451.png]]

B1. Let A be the adjacency matrix then we get all the m's by $A @ h$, where this h contains all the current h's in a vector.
> Adjacency matrix, because we select the neighbours from it, i.e if there's an edge, then there's a neighbour.

The update step is then the l2 norm of the all the m's.

This is the same as 

$$ A @ h / (||A @ h||_2)$$
![[Pasted image 20240411150626.png]]

Following the power iteration rule the vector we will end up with is the eigenvector of the adjacency matrix, A, which corresponds to the largest eigenvalue in a direction where the initialization of h was non-zero.

![[Pasted image 20240411150840.png]]

![[Pasted image 20240411151228.png]]
My mistake was not including the full number parameters of the weight matrices in the drawing.
$$5 \cdot (10 \cdot (32 \cdot 32 + 32 \cdot 32) + 32) = 102560$$
Here I assume k yields unique parameters, I assume each node has a unique neighbor matrix too.
