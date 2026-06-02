import numpy as np

# Create an array from 1 to 12
arr = np.arange(1, 13)

# Reshape into (3, 4)
shape_3_4 = arr.reshape(3, 4)

# Reshape into (2, 6)
shape_2_6 = arr.reshape(2, 6)

# Reshape into (2, 3, 2)
shape_2_3_2 = arr.reshape(2, 3, 2)

print("Shape (3, 4):\n", shape_3_4)
print("\nShape (2, 6):\n", shape_2_6)
print("\nShape (2, 3, 2):\n", shape_2_3_2)