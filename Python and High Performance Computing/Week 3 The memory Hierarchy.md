
## Relevant performance metrics

- Wall-Clock time how long do we wait in the real world
- CPU time how long did the CPU work
- FLOP/s Floating point operations per seconds.
- - We measure FLOP/s by counting the number of FLOP we do and divide it by the number of seconds our program took to run.

Often the FLOP/s curve will look like this, because of caching

![[Pasted image 20240214084149.png]]

It also looks like this, because RAM is so much slower to access.

## Efficient use of CPU cache and main memory (?stack and heap?)

My cpu caches from `lscpu`
![[Pasted image 20240213164043.png]]

L1d is for data, and L1i is for instructions.

Things in the L1 cache match the speed of the cpu (Number of cycles).
In the ram most of the time is spent waiting for data.

This is my ram
![[Pasted image 20240213164252.png]]

> The rest of the caches as the number goes down get progressively smaller, but also progressively faster to access.

### Take away for testing

The cpu cache on your desktop will have lots of processes using it.
This is in contrast to on a server.

Thus benchmarking cache optimizations, if the end goal is a server, should be run on a server.

### Take away for performance

Have how you access data match your data layout.
## Blosc for compressed data arrays

Using effective compression can make access and write times much faster.
If the access times are what is bottle-necking us, then this can be a very good idea. 

## NumExpr to accelerate NumPy


NumExpr tries to make code cache efficient.
It won't always be the best choice, if you are sharing the machine with other processes.
It also only supports a subset of numpy's opperations.


### Note on numpy

Column indexing is faster than Row indexing. (C layout (row contiguous))

The reason for this is in the number of memory moves and what we have cached.

## Client/Server architectures for very fast networks.

__IF OPTIMIZED FOR IN THE PROTOCOL__
- It is often orders often magnitudes faster to talk to over the network then talking between local disks.

HTTPS IS SLOW, because it requires authentications and packets sent in JSON formart, which need to be unserialized.

UDP is FASTER, as it just sends packets. A drawback of this is that sometimes packets will be lost.
It is also not secure, but if we are in a somewhat closed system, this usually isn't an issue.

A potential new protocol is QUIC (Quikc UDP).


