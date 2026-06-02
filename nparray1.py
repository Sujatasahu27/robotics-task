import numpy as np

a = np.array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

# Extract:
# - first column
first_col = a[:, 0]

# - last row
last_row = a[-1, :]  # or a[2, :]

# - sub-array [[22, 33], [55, 66]]
sub_array = a[0:2, 1:3]

print("First Column:", first_col)
print("Last Row:", last_row)
print("Sub-array:\n", sub_array)