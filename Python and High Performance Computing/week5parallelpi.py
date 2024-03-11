
def calculate_pi_serial(samples):
    import random
    hits = 0
    for i in range(samples):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        if x**2 + y**2 <= 1:
            hits += 1
    return 4.0 * hits/samples
import random
def sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

def calculate_pi_parallel(samples, n_proc):

    import multiprocessing
    pool = multiprocessing.Pool(n_proc)
    results_async = [pool.apply_async(sample) for i in range(samples)]
    hits = sum(r.get() for r in results_async)
    return 4.0 * hits/samples




def sample_multiple(samples_partial):
    return sum(sample() for i in range(samples_partial))

def calculate_pi_parallel_chunk(samples,n_proc):
    import multiprocessing


    hits = 0
    chunk_size = samples//n_proc
    pool = multiprocessing.Pool(n_proc)
    results_async = [pool.apply_async(sample_multiple, (chunk_size,)) for i in range(n_proc)]
    hits = sum(r.get() for r in results_async)
    pi = 4.0 * hits/samples
    return pi


if __name__ == "__main__":
    import sys
    type_run = sys.argv[1]
    match type_run:
        case "serial":
            samples = int(sys.argv[2])
            print(calculate_pi_serial(samples))
        case "parallel":
            samples = int(sys.argv[2])
            n_proc = int(sys.argv[3])
            print(calculate_pi_parallel(samples, n_proc))
        case "parallel_chunk":
            samples = int(sys.argv[2])
            n_proc = int(sys.argv[3])
            print(calculate_pi_parallel_chunk(samples, n_proc))
        case _:
            print("Invalid type of run")
            sys.exit(1)