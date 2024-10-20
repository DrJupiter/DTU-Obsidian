
Often we cannot do all the experiments we want in a $2^k$ experiment.
This leads us to either analyzing fewer factors or doing fewer replicants.
When we do fewer replicants an analysis we can do is checking whether certain interactions how a 0 mean normal distributed effect or not.
If they don't then we assume them on average to have some impact.

**Design projection**

When we do a factor analysis and find some factors are useless, we then in (future) experiments view or experiment as a $2^{k-\text{useless factors}}$ experiment.

we then check this assumption by analysing if the residuals follow a normal distribution.

**Adding robustness to a model with redundant points**

![[Pasted image 20241020111016.png]]

We then add some center points at (x=0, but y=random, y is the response?) when we fit our curve which creates more robustness for the second model (6.29).

![[Pasted image 20241020111258.png]]

$n_f =$ number of factorial points
$n_c =$ number of center points

We then do an F test to see if the model 6.29 is a better fit for the experiment.



