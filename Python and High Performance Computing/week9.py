import numba
from numba import cuda
import numpy as np

@numba.jit(nopython=True)
def matmul(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for k in range(A.shape[1]):
            for j in range(B.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C

@cuda.jit
def add_kernel(x, y, out):
    i = cuda.grid(1)
    if i < x.size:
        out[i] = x[i] + y[i]

def get_blocks_per_group(n, threadsperblock):
    blockspergrid = n // threadsperblock
    if n % threadsperblock:
        blockspergrid += 1
    return blockspergrid

if __name__ == '__main__':
    A = np.random.rand(100,100)
    B = np.random.rand(100,100)
    # Measure the wall time
    import time
    initial_time = time.time()
    C = matmul(A, B)
    wall_time = time.time() - initial_time
    print("Wall time:", wall_time)
    
    A = np.random.rand(100,100)
    B = np.random.rand(100,100)
    initial_time = time.time()
    print(matmul(A, B))
    wall_time = time.time() - initial_time
    print("Wall time:", wall_time)

    # CUDA kernel
    n = 1_000_000_00
    x = np.random.rand(n)
    y = np.random.rand(n)
    out = np.zeros(n)
    d_x = cuda.to_device(x)
    d_y = cuda.to_device(y)
    d_out = cuda.to_device(out)

    threadsperblock = 256
    blocks_per_group = get_blocks_per_group(n, threadsperblock)
    add_kernel[blocks_per_group, threadsperblock](d_x, d_y, d_out)
    print(d_out.copy_to_host(out)[:10])
    input()


