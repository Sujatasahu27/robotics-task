import numpy as np

# Create a 2D array
arr_2d = np.array([[5, 10, 15], [20, 25, 30]])

# Print properties
print("Array:\n", arr_2d)
print("Shape:", arr_2d.shape)      # Dimensions of the array (rows, columns)
print("Size:", arr_2d.size)        # Total number of elements
print("Ndim:", arr_2d.ndim)        # Number of array dimensions (axes)
print("Dtype:", arr_2d.dtype)      # Current data type

# Change its datatype
arr_2d_changed = arr_2d.astype(np.float32)
print("\nChanged Dtype:", arr_2d_changed.dtype)