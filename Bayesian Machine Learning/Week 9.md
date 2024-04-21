
Our goal is to decouple modelling and inference.

# Gibbs sampling

You update one coordinate at a time for some multidimensional parameter z.

Notation: $z_i^j$ is the j'th component in vector i, __in his notation it's the i'th component in vector j__.

What we do is 

```python
z = [None]*K
z[0] = z0
indicies = np.arange(1,d)
for k=1..K:
	z[k] = z[k-1]
	for j=1..d:
		z[k][j] = sample p(z[k][j]|z[k][j != indicies])
	#z[k] = sample p(z[k]|z[k][...]) I don't think this part must be a type in his thingy, yes it is
```

![[Pasted image 20240421163854.png]]

> He shows that the gibs sampler is a special case of metropolis hastings where the proposed sample is always accepted


# Convergence diagnostics

# Hieracical models
