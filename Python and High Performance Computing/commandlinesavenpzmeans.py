import sys
import numpy as np

def main():

    file_path = sys.argv[1]
    

    matrix = np.load(file_path)
    

    col_means = np.mean(matrix, axis=0)
    row_means = np.mean(matrix, axis=1)
    
    np.save('cols.npy', col_means)
    np.save('rows.npy', row_means)

if __name__ == "__main__":
    main()