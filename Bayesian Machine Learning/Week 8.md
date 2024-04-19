
## Recap

Expected calibration error

$$ ECE = \sum_{b=1}^{B} \frac{|B_b|}{M} \cdot |acc(B_b) - conf(B_b)|$$

The symbol B represents the bins.

### ECE for scalar regression

We use the cdf of $p(y*|y,x*) \equiv p(y*)$.

$$ F(\tau) = p(y* \le \tau)$$
We bin the cdf value axis.
The idea is to use the inverse  of the cdf


$$ \hat{p}(p) = \cfrac{\sum_{n=1}^{N} \mathbb{I}[y*_n \le F_n^{-1}(p)]}{N}$$
N is the size of the test/data set of $y*$.

extension for intervals

$$ \hat{p}(p_1, p_2) = \cfrac{\sum_{n=1}^{N} \mathbb{I}[F_n^{-1}(p_1) \le y*_n \le F_n^{-1}(p_2)]}{N}$$

