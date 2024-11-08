
## Design resolutions

**Definition:**

A design is of resolution `R` if no `p` factor effect is aliased with another effect containing less than `R-p` factors.

This means that given our generator, we can tell the difference between all factors `p` and all factors less than `R-p`.

**Common resolutions:**

![[Pasted image 20241108100254.png]]

By main effect they main a single effect A, B, C, .. etc.

## Generator analysis

The algebra is:

For single effects:
	$$ A \cdot A = I $$
We define a generator as:

$$ X = I \text{ or } X = -I $$
> The `-I` means whether or not the factors constructing it multiplied together equal -1, and the equivalent for `+I` 

The operator $\cdot$ is commutative.

All combinations, where we can make them be equivalent `=`, we say are indistinguishable/aliased.



