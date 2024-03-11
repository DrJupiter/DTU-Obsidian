import numpy as np

def tree_sum(arr):
    N = len(arr)

    # Start from the second element since the first element will be the sum itself
    for i in range(1, N):
        for b in range(0, N - i, i * 2):
            arr[b] += arr[b + i]  # Accumulate sum to the current element

    return arr[0]  # Return the sum of the original array

# Test the function
arr = np.array([4, 9, 1, 2, 3, 7, 1, 8, 5, 2, 0, 4, 6, 2, 5, 7])
result = tree_sum(arr.copy())  # Make a copy to preserve the original array
original_sum = np.sum(arr)
if result == original_sum:
    print("The sum of the original array is equal to the first element after computation:", result)
else:
    print("Error: The sum of the original array is not equal to the first element after computation.")
