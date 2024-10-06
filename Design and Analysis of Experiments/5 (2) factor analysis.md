
## Design

We have two factors at a and b discrete levels and we want to measure their effect and their interactive effect.

## Anova analysis for 2 factors at different levels a and b
[2k2]

The F statistics in the table test if the effect from any row is 0.

![[Pasted image 20240929191352.png]]

![[Pasted image 20240929191416.png]]
![[Pasted image 20240929191433.png]]

## Checking the validity of using a linear model

We simply check if the residuals so $(y-\hat y)^2 \sim \mathcal{N}(\mu, \Sigma)$, if they do then we are good I guess. 

## Obtaining the model parameters

- Either we use some iterative algorithm 
- or we impose the constraints of the parameters summing to zero and obtain the closed form solution ![[Pasted image 20240929192105.png]] ![[Pasted image 20240929192135.png]]
- 

# Choosing sample size 5.3.5
Ask Andreas if he understood it or if relevant spend time to understand it yourself.

# The general factorial design

Essentially we just keep on adding parameters and checking for the effects of all the combinations of all the parameters. 5.4 in the book

So the factorial design doesn't scale well.

# In a block design

So now we are doing the factorial design several times with some additional noise depending on the block.
> In practice this could be different material types that we have a limited supply of or different times of day or something.

![[Pasted image 20240929193410.png]]

![[Pasted image 20240929193419.png]]


# Lack of fit degrees of freedom factorial design

Sum all the degrees of freedom from the model that have not been included in the model.
Example not including the interaction between two elements, would result in the lack of fit degrees of freedom being the degrees of freedom of that interaction.

! Although only when we have concluded a part of the model is non significant can we add it to the error !