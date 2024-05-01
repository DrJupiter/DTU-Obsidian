

## q1 (check)

![[Pasted image 20240424094203.png]]

The `-J` option corresponds to the name, which is `proc`.
The `-q` option corresponds the queue, which is the compute cluster they are requesting their job in, `hpc`.
The `-W` time specifies the wall time, which is `5 min`.
The `-R "rusage[mem=2GB]` specifies that they are requesting 2GB memory per core.
The `-R "span[hosts=1]` option specifies that they are requesting for all of their compute to be in the same host.
The `-n 4` option specifies that they are requesting 4 cores.
The `-o proc_%J.out` is the file which the standard out is writtin to.
And `-e ...` is the file the standard error is written to.
The %J in these options will use the job id in the name of the files.

## q2


### q2.1 function to speed up (check)

Based on the output 

![[Pasted image 20240424094720.png]]

The `compute` function seems to be taking the longest out of the functions available, and the data processesing the next longest and finally the summarization is fairly fast.

So I would optimize the functions in that order.

(Yes, we are spending 16 seconds on it, and the answer is correct)

### q2.2 Amdahl's law (check)

16 s -> sequential

total is 24 so 

$$ S(\infty) = \frac{1}{1-F} = \frac{1}{1-16/24} = \frac{1}{8/24} = \frac{24}{8} = 3 $$
So the theoretical maximum speed up 3 seconds, which is not very much.
If we look at the 4 cores we were using for the job script it would be even less.
Thus I would investigate speeding up the sequential computation to see if I could shave off more than 3 seconds first.

(the program does take 24 seconds and only compute can be paralized so the compute fraction is correct.)

#### Corrections

_!!! the speed up is 3x not in seconds !!!_ thus he concludes that the speed up is worth it up to a certain amount of cores.

Here in the graph he shows the time

![[Pasted image 20240501084131.png]]
![[Pasted image 20240501084144.png]]
(Here procs is the number of cores)


### q2.3 source code optimization cache

As they are looping over the columns first I would store it in a column wise manner as then indexing the next row in the column would likely already be in a low cache level.

#### Correction

the inner loop is looping over the row indexing it means we are looping over a column and down, and this means we will get cache effecient access by using a column storing.

![[Pasted image 20240501084431.png]]


### q2.4 binary tree reduction with infinite cores

We only have to do around $\log(N)$ operations thus the theoretical speed up for $\log(N=2^{10}) \approx 10$.
Or just 10 is the base is log 2.

#### Correction, we need to use the relation

![[Pasted image 20240501084536.png]]

Time to do one (T(1)) is N for a sum.
The ($T(\infty)$) is ($log_2(N)$) because the number of levels is $log_2(N)$ in the binary tree

![[Pasted image 20240501084645.png]]

### q2.5

len(x) = n, len(measurements per day) = 10.
days = n/10. x[0] is x[1] as it is 1 indexed.

The opperation should be `x.reshape(-1,10).sum(axis=1)`

#### correction

we had misunderstood the question, they wanted to sum along the columns for some reason.
this is because the index into y with j.
### q2.6 job array (check)

to the `-J` line we add `[1-24]` $(2*12)=24$, so we get one job per month then we modify our `monthelystats.py` script to take an index which corresponds to one of the months and load and preprecoss and save that data via the `python monthlystats.py $LSB_JOBINDEX`.



### q2.7 optimizing a cross entropy matrix via cache efficiency / numpy (check)

As X is an NxN matrix and we do between row to column the opperation is the same as 


```python
D = -np.matmul(X,np.log(X))
```

### q2.8 data compression

![[Pasted image 20240424102554.png]]


![[Pasted image 20240424102534.png]]

based on the table below we see that the `dis: float64 -> float16` as the values are within the min and max range.
Following the same logic we can convert `rad: int64 -> int8`, `tax: int64 -> uint16`.
Thus we have shaved off around $1/(4+8+4) = \frac{1}{16}$ of the memory.

#### Correction 
for dis the number of unique values is very large, and we might lose a large number of precision, so for floating conversion errors we need to check for rounding errors.

he was also considering categorical for the float if it had had a small amount of unique values.

for the tax, we could also do a categorical potentially, but the uint/int16 is a good answer too.

for the rad it was good.
### q2.9 

NxHxW -> BxHxW 

The 1x1024 

#### Comment and Correction

We need to look at the threads, and how they index the data. 

Due to the nature of the loop we are acessing in 32x32 blocks
![[Pasted image 20240501091108.png]]

As we are storing stuff rowwise, the columns wise thread block will be the worst as almost everyone would result in a cache miss.



### q2.10

The reasoning is the way we access memory, here in 1x1024 each block has 1024 threads in a single row as these threads share cache and might be reading in different parts, we most likely would have more cache misses compared to a 32x32 setup which is the length of a `warp` and might load in data to the cache which the threads share which other threads need, thus resulting in faster computation.

### q2.11

understandably we are copying memory a lot back and forth, we might pin our memory to reduce the time of this. We are also not copying maybe as much memory as we could, so maybe we could increase the batch size, this is based on the max copy being 368 which is larger than the average.
We also might want to choose a number which is divisible by the warp size such as $208$ in order to not waste computation.

#### Comments

The memory is spending much more time than the kernel is correct.
Thus are thought process is correct.

For how to optimize this:

	We are doing 10 memory transfers

![[Pasted image 20240501091549.png]]

The give away is that a lot of transfers is happing here 

![[Pasted image 20240501091637.png]]

we don't need to transfer out nor image batch, thus we could put it on the gpu.
So it stays there.

In total we only need 6 now as we need to transfer image batch 5 times and then out only once.

