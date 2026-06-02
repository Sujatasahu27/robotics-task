import numpy as np

a = np.array([1, 2, 3, 4])

# Convert integer array into float datatype
a_float = a.astype(float)

print("Original Array:", a, "| Datype:", a.dtype)
print("Converted Array:", a_float, "| Datype:", a_float.dtype)