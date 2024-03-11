import numpy as np
arr = np.arange(10)
#arr = np.array([4, 9, 1, 2, 3, 7, 1, 8, 5, 2, 0, 4, 6, 2, 5, 7])
print(np.sum(arr))
chunk_size = 2
N = len(arr)
print(np.log2(10))
for i in range(1, np.log2(len(arr)).astype(int)-1):
    print(i)
    print(arr)
    for b in range(0,N, chunk_size*i):
        e = b + chunk_size*i
        arr[b] = arr[b:e:i].sum()

print(arr)