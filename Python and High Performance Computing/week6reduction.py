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
    batch_index, batch_index_offset, wtf, image_shape = args

    # this recovers the whole array
        # B x W x H x C
    arr = tonumpyarray(shared_arr).reshape((-1,) + image_shape)
    # We then add the all the offset numbers
    if batch_index >= len(arr) or batch_index_offset >= len(arr):
        pass
    else:
        arr[batch_index] += arr[batch_index_offset]
    
if __name__ == '__main__':
    
    n_processes = 1
    chunk = 2
    # Create shared array
    data = np.load(sys.argv[1]) # B x W x H x C

    #data = np.array([[1,2,3],[2,3,4],[4,5,6], [4,5,6]])
    #print(data.mean(axis=1))
    #B,W,H,C = data.shape
    B=len(data)
    elemshape = data.shape[1:] # W x H x C
    n_elements = np.prod(data.shape) # B * W * H * C
    shared_arr = mp.RawArray(ctypes.c_float, data.size) 
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data
    
    # Run parallel sum
    t = time()
    pool = mp.Pool(n_processes, initializer=init, initargs=(shared_arr,))
    # Change the code below to compute the full reduction and the mean
    # ---------------------------8<---------------------------
    # So we are iterating over the batch dimension by the chunk, first we sum the neighbours,
    # I suppose next time we should like jump
    chunk = 1
    #offset = 2**n
    #skip = 2**(n+1)
    n = 0
    while True:
        offset = 2**n
        skip = 2**(n+1)

        pool.map(reduce_step, [(i, i + offset, 1, elemshape) for i in range(0, B, skip)], chunksize=1)
        n += 1
        if offset > B - 1:
            break

        
    
    #pool.map(reduce_step, [(i, i + chunk, 1, elemshape) for i in range(0, len(arr), chunk)], chunksize=1)
    # Write output
    print(time() - t)
    final_image = arr[0]/len(arr)
    # final_image /= len(arr) # For mean
    Image.fromarray(
    (255 * final_image.astype(float)).astype('uint8')
    ).save('result.png')