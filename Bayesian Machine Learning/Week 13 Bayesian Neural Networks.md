
# Relating VAEs to Variational Inference

![[Pasted image 20240504165755.png]]

In the context of this course this is accurate.

# Comparing VI (variational inference) to other methods so far in this course

![[Pasted image 20240504180146.png]]

Laplace is the simplest and quickest to implement. 
VI is sort of the middle ground between MCMC and Laplace, in that it has no theoretical guarentees, but it has more freedom than Laplace, and is faster than MCMC and it scales better with mini batching.

# Bayesian Neural Networks

We can gain a lot of predictive performance/calibration sometimes from this.

## Challenges 

High non-linearity, multi model posteriors, multiple optimal solutions, the data can be hard to fully represent.

Priors on the network weights in MLPs are hard to interpt in function space, like what they mean for the type of functions we will be getting, and thus it is often introduced as a form of regularization instead.


The focus/emphasis is post hoc adding a bayesian approximation from pretrained models.

## Approximating the posterior predictive distribution of NN

In this method the bottleneck is to obtain posterior samples

![[Pasted image 20240504183813.png]]

Two strategies

![[Pasted image 20240504183921.png]]

The second one for SGD bounces around near the optima to sample parameters around the mode. 

This is also close to the SWAG method, but it computes a gaussian approximation around the sampled SGD points.

## Monte Carlo Dropout 

Maintain your dropout active when doing a prediction and do several forward passes and do an average over these to get the results you want i.e means, covariances etc.

This method doesn't have a lot of theoretical justification, but it's easy to implement and test so it's worth a shot.

A big draw back is that epistemic uncertainty won't necessarily decrease with more data.
Another drawback is that we can get big drift from sampling like this.

## Mean-field approximation for NN

![[Pasted image 20240504190637.png]]


It is useful to initialize the mean vector with the MAP vector and then the variance with a small value.

For models with a single hidden layer it has shown that if the network is sufficiently wide then it will just converge to the prior over the weights and ignore the data.
So yeah don't make your network too wide and observe underfitting idk, instead make it deeper.
The paper shows a deeper approximation works better.

A result for mean-field networks of a single layer is that the variance of convex combinations of points is bounded by the sum of the variance of the two points.
This is a problem in that the model will be overly confident when predicting points outside of the training set potentially.

![[Pasted image 20240504190933.png]]

## Laplace approximations

We don't gain anything decision wise, but we gain in calibration.

If the network has a lot of parameters then the hessian is infeasible to have in memory, thus we approximate the hessian in some sort of way or just look at the last layer.

![[Pasted image 20240504191730.png]]

Hessian isn't gaurenteed to be positive definite, thus the Gauss-Newton matrix might be used instead.

### Last Layer Laplace Approximation

![[Pasted image 20240504192339.png]]

In practice you can use the Laplace Redux package for many pytorch models.

But doing the last layer approximation isn't necessarily the most optimal as shown in the following paper, where they use some subset of the parameters of the model.
![[Pasted image 20240504192656.png]]

For their networks they find a 5%-14% bayesian network is very close to a fully bayesian NN.
However maybe their model doesn't represent the posterior fully and better and better performance could be achieved.

## Deep ensemble

Retrain your model S times from different seeds, hopefully arrive at S different modes, compute the predictions for all the models and then average the result. Step 69 profit.

![[Pasted image 20240504193057.png]]

![[Pasted image 20240504193120.png]]

A draw back of this is the training time and that all models are weighted equally (unless multiple models converge to the same modes.)



# Overall key equation

![[Pasted image 20240504182211.png]]
