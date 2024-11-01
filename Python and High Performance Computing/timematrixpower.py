import numpy as np
from time import perf_counter

def main():


    file_path = './input.npy'
    p = 10

    A = np.load(file_path)

    start_time = perf_counter()

    result = A
    for _ in range(p):
        result = np.dot(result, A)

    end_time = perf_counter()

    np.save('result_matrix.npy', result)

    print(end_time - start_time)

if __name__ == "__main__":
    main()
