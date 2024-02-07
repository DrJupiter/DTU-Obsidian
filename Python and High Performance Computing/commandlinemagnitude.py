import sys
import numpy as np

def main():
    # Extract vector components from command line arguments, convert them to floats
    vector = np.array([float(component) for component in sys.argv[1:]])
    
    # Calculate the magnitude of the vector
    magnitude = np.linalg.norm(vector)
    
    # Print the magnitude
    print(magnitude)

if __name__ == "__main__":
    main()
