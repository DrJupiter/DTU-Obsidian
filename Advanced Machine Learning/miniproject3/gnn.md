

Goal: Generate adjacency matricies

Dataset: MUTAG (molecules) -> predict graph-level binary classification 
	Vertex: atom
	 Edges: bond
	 Node label: 1-7 -> type, one hot encoded
	 Len: 188

Baseline: Erdos Renyi - constant probability for connection as the avarage amount of links in the training set.

Model: VAE of some latent level, GAN or whatever else we want, flow maybe. Or something from bayesian. 
	Must include: A message passing gnn or a graph cnn as part of the architecture

Report:
	Technical description of your model
		Code snippets for the central components of our implementation.

Evaluation: 
	1000 graphs from baseline and model.
		Then compute:
			The percentage of graphs which are different from the ones in the training data: novelty

			 The percentage of unique graphs - uniqueness


			 The percentage of graphs which are novel and unique - novelty and uniqueness


		 Do the computation as if the graphs were isomorphic use Networkx and the weisfeiler-lehman algo for instance. 
		 "Two graphs are considered isomorphic if there is a way to relabel the vertices (nodes) of one graph to obtain the other graph, such that the connectivity (edges) between nodes is preserved. This means that the two graphs are structurally identical, even if the labels of their vertices are different."


Graph statistics:
		Compare generated graphs to training graphs with histrograms:
			node degree
			 clustering coefficient
			 eigenvector centrality


## Our model

Embedding: Graph level
Loss: Binary Cross entropy

Encoder: Gaussian prior
Decoder: tensor product
