
## What Compute Tasks the GPU is good at

GPU's are good at doing a lot of reads and performing similar operations on all the read data.

> SIMD

The GPU's target is throughput and the CPU is latency.

### The architecture of the GPU

The entry point into the GPU from the CPU are _kernel functions_.
> The kernel function specifies what each thread and the GPU should do.

Has a main GPU memory.

Has L2 caches shared across all streaming multiprocessors.

#### Streaming Multiprocessors (SM)

Each SM has L1 caches, which can be shared across all its streaming processors.
##### Streaming processors (SP) (CUDA Cores)

We can calculate the number of threads is SM * SP.

## Numba (JIT compiler)

### JIT Compiler

![[Pasted image 20240403083459.png]]

![[Pasted image 20240403083857.png]]
#### JIT Eco-system

![[Pasted image 20240403083527.png]]

### Using GPU kernels through Numba

![[Pasted image 20240403084929.png]]

Here device means a GPU.

Kernel functions should not call other kernel functions.
In this example the mul is not a kernel, but a gpu functions <I suppose)

We can actually have threads have more than one element, it depends on the computation you are doing.

We must pass the input and output array to the kernel. We our built up around indexing.

We need to synchronize our kernels to ensure the GPU computation is done `cuda.synchronize()` in Numba. 
#### The thread block/compute block

![[Pasted image 20240403085647.png]]


##### More detailed thread index

![[Pasted image 20240403085851.png]]

## Warps

Opperations are performed in groups of 32 threads called warps.

![[Pasted image 20240403091220.png]]
![[Pasted image 20240403091236.png]]

The name for the SIMD.

![[Pasted image 20240403091306.png]]

Ex if statement requires an additional warp.

![[Pasted image 20240403091637.png]]

![[Pasted image 20240403091653.png]]
![[Pasted image 20240403091934.png]]
![[Pasted image 20240403091958.png]]
![[Pasted image 20240403092021.png]]

Warps can't diverge, if we need to do different things, we need to schedule multiple warps.


## Memory transfers

![[Pasted image 20240403092217.png]]

GPUs move data through a pinned buffer to avoid unnecessary memory moves.

![[Pasted image 20240403092654.png]]

![[Pasted image 20240403092710.png]]

# Summary

![[Pasted image 20240403093919.png]]
