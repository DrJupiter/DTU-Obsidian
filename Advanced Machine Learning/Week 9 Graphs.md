
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

Intuition behind the adjacency matrix is the same as a stochastic (markov chain) matrix. Raising it to a power is and looking at an index gives us the number of ways to end back up at the given node if we took the number of steps equal to the power we raised the matrix to.

% idea, implement a switch given the time steps which is active for as long as the pixels are independent in the unet.

### Graph Features


# Encoder + Decoder Setup for Graphs
## (Encoder) Learning Node Embeddings

We want node embeddings to do the following:

- Contain where they are in the graph
- Geometric relations between embeddings should reveal relations between the corresponding nodes in the graph i.e edges.

The type of embedding we will focus on first is the shallow embedding

### Shallow Embedding

Each node is a key which looks up into a table of embeddings.
![[Pasted image 20240411085049.png]]

## (Decoder) The pairwise decoder

The pairwise decoder predicts a relation between two nodes.
This could be if an edge exists or something else.

![[Pasted image 20240411091532.png]]
![[Pasted image 20240411091545.png]]

### Architectures and what they achieve

![[Pasted image 20240411104903.png]]
![[Pasted image 20240411104920.png]]

A is the adjacency matrix.
$p_G(v|u)$ is the probability of visiting node v on a random walk of fixed length from node u.


