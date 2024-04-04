
We will represent graphs in adjacency matrices.

A new type of graph is the multi relational graph.
This graph is in 3d instead of 2d.
Each slice represents a type of connection.

Some particular types of multi relational graphs to note are the heterogeneous graph and the multiplex graph.

The heterogeneous graph has it's nodes be a set of types and be disjoint.

![[Pasted image 20240404090604.png]]

The multiplex graph has k layers which represent a type of relation and we can connect the nodes by this relation within the layer, we can also create layer to layer edges which symbolize a connection between relations.

![[Pasted image 20240404092153.png]]


Often nodes might have an associated feature matrix which will often be one hot encoded or contain real values.

## Graph learning in Traditional ML

### Node Features 

#### Degree 

A common feature to extract is the degree (out or in).
![[Pasted image 20240404093533.png]]

#### Node centrality (eigenvector centrality)

![[Pasted image 20240404093919.png]]

Where A is the adjacency matrix and entry i in the eigenvector e corresponds to the i'th nodes eigen centrality.

> To obtain strictly positive eigenvectors use "Perron-Frobenius Theorem1 to further determine that the vector of centrality values e is given by the eigenvector corresponding to the largest eigenvalue of A"

##### Other centralities

__betweeness centrality__ which measures how often a node lies on the shortest path between two other nodes

__closeness centrality__ which measures the average shortest path length between a node and all other nodes

#### Clustering coefficient (local)

"clustering coefficient, which measures the proportion of closed triangles in a node’s local neighborhood."

![[Pasted image 20240404095607.png]]

### Graph Features



