import sys
import numpy as np

def main():

    diagonal = [float(value) for value in sys.argv[1:]]

    matrix = np.diag(diagonal)

    np.save('diagonal_matrix.npy', matrix)

if __name__ == "__main__":
    main()