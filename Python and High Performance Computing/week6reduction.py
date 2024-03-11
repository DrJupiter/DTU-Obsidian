import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time
import numpy as np
from PIL import Image
def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_
def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')

def reduce_step(args):
    b, e, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    
    # Change the code below to compute a step of the reduction
    # ---------------------------8<---------------------------
    #arr[b:e:s] = 1.0 - arr[b:e:s] # Negate element
    #arr[0::2] += arr[1::2]
    #arr[b:e:s, 0::2] = arr[b:e:s, 0::2] + arr[b:e:s, 1::2]
    #try:
    #    # Ensure operations are compatible with the shape of the data
    #    if e > arr.shape[0]:
    #        e = arr.shape[0]
    #    
    #    for i in range(b, e, s):
    #        if i + s < e:
    #            # Adjusting this to ensure compatibility with different shapes
    #            arr[i] += arr[i + s]
    #except ValueError as ve:
    #    print(f"Error processing data slice {b} to {e}: {ve}") 


if __name__ == '__main__':

    
    n_processes = 1
    chunk = 2
    # Create shared array
    data = np.load(sys.argv[1])

    elemshape = data.shape[1:]
    n_elements = np.prod(data.shape)
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data
    # Run parallel sum
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))
    # Change the code below to compute the full reduction and the mean
    # ---------------------------8<---------------------------

    
    for j in range(1, np.log2(len(arr)).astype(int)+1):
        pool.map(reduce_step, [(i, i + chunk, j, elemshape) for i in range(0, len(arr), chunk)], chunksize=1)
        chunk *= 2
    #pool.map(reduce_step, [(i, i + chunk, 1, elemshape) for i in range(0, len(arr), chunk)], chunksize=1)
    # Write output
    print(time() - t)
    final_image = arr[0]/len(arr)
    # final_image /= len(arr) # For mean
    Image.fromarray(
    (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')