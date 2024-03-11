import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2.0:
            return i
    return 100

def generate_mandelbrot_set(points, num_processes):
    ########################
    # YOUR CODE HERE #
    pool = multiprocessing.Pool(num_processes)
    with pool as p:
        escape_times = p.map(mandelbrot_escape_time, points)
    ########################
    return np.array(escape_times)


def generate_mandelbrot_set_chunks(points, num_processes):
    ########################
    # YOUR CODE HERE #
    pool = multiprocessing.Pool(num_processes)
    chunks = len(points) // num_processes
    with pool as p:
        escape_times = p.map(mandelbrot_escape_time, points, chunksize=chunks)
    ########################
    return np.array(escape_times)

def plot_mandelbrot(escape_times):
    plt.imshow(escape_times, cmap='hot', extent=(-2, 2, -2, 2))
    plt.axis('off')
    plt.savefig('mandelbrot.png', bbox_inches='tight', pad_inches=0)
if __name__ == "__main__":
    import sys
    width = 800
    height = 800
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = int(sys.argv[1])
    # Precompute points
    x_values = np.linspace(xmin, xmax, width)
    y_values = np.linspace(ymin, ymax, height)
    points = np.array([complex(x, y) for x in x_values for y in y_values])
    # Compute set
    
    mandelbrot_set = generate_mandelbrot_set(points, num_proc)
