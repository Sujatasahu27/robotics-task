import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Extract:
# - first row
first_row = a[0, :]

# - second column
second_col = a[:, 1]

# - element 50
element_50 = a[1, 1]

print("First Row:", first_row)
print("Second Column:", second_col)
print("Element 50:", element_50)