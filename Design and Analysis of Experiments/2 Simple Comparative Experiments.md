
# Basic Statistical Concepts
Standard stuff and then unbiased estimations of the mean and variance.

![[Pasted image 20240909144322.png]]

# Sampling and Sampling Distributions
(reference to advanced)

The distributions we will work with are 

## Normal distributions

## Chi-square 

Relation: sum of k standard normal distributions  individually squared = X^2(k)

It follows that if we standardize our normally distributed variables and create a chi-squared distribution and then multiply it by $$\frac{\sigma^2}{n-1}$$
Where n refers to the number of samples used to the number of samples used to construct the chi squared variable, and $\sigma^2$ refers to that we assume identical variance of the variables in the sum, but this would just be replaced with the product of their variances, if this weren't the case.

Anyway we have that the sample variance this follows the distribution $$\frac{\sigma^2}{n-1} \cdot \mathcal{X}^2(n-1)$$ 

## t distribution

If for some reason we want to get the distribution of fx a normal variable divided by its sample standard deviation, then we get a t-distribution

$$t_{k} = \cfrac{z}{\sqrt{ \chi^2 \frac{1}{k} }}$$

$$z \sim N(0,1^2)$$

We can use the t distribution to test if some variables known to be i.i.d normal variables if they follow a certain normal distribution so the likelihood $p(\mu| data)$.

We have:

$$\cfrac{\bar{ y} - \mu}{S \cdot \frac{1}{\sqrt{ n }}} \sim t(n-1)$$
Where n is the number of variables summed into a mean to form $\bar y$.

relation: normally distributed random variables and their sample mean.

### Testing same variance different mean hypothesis 

![[Pasted image 20240909162635.png]]

Statistic:

![[Pasted image 20240909153711.png]]

Distribution:
$$ t(n_{1} + n_{2} - 2)$$
Typically we test for the absolute value of the test statistic to do a two sided test and thus we check for some significance level of $\alpha/2$.

### Testing different unknown variances different means hypothesis

![[Pasted image 20240909162638.png]]

Statistic:

![[Pasted image 20240909162418.png]]

Distribution:
We approximate the distribution with a t-distribution with degrees of freedom
![[Pasted image 20240909162451.png]]

### Testing different known variances different means hypothesis
![[Pasted image 20240909162641.png]]

Statistic:
![[Pasted image 20240909162705.png]]

Distribution:

Standard normal distribution

### Testing if the mean is just equal to same value

#### Known variance

Statistic:

![[Pasted image 20240909163121.png]]

Distribution:

Standard normal distribution
#### Unknown variance

Statistic:

![[Pasted image 20240909163150.png]]

Distribution:

t(n-1) degrees of freedom.

### Finding the interval of the difference in means assuming same variance

Statistic:
![[Pasted image 20240909160248.png]]

Distribution is t, but we just solve this equation:

![[Pasted image 20240909160327.png]]

### Finding the interval of the difference in means assuming different known variance

![[Pasted image 20240909162834.png]]

### Confidence interval over sample mean with known variance

![[Pasted image 20240909163325.png]]

Here Z is a standard normal distribution, where we evaluate $P(Z >= \alpha/2)$

### Confidence interval over the sample mean with only sample variance

![[Pasted image 20240909163411.png]]


## F distribution

The ratio between two independent chi-squared variables follows an F distribution.

$$ \cfrac{\chi^2_{u}}{\chi^2_{v}} \cfrac{v}{u} \sim F_{u, v} $$

We can then test that the probability of this ratio being one or whatever we need to for the ratio to be what we want, and then check the probability of two normal distributions' standard deviations being different.

Relation: normally distributed random variables and their standard deviations

# Differences in means and randomized designs

## Hypothesis Testing

## Confidence intervals

## Choice of Sample size

## Variance comparison of normally distributed variables

## Comparing the means of normal distributions

# Differences in means and paired comparisons 

## Paired Comparison Problem

## Advantages of paired comparison design

# Variances of normal distributions

