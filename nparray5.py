import numpy as np

# 1D array containing numbers from 1 to 10 using random module
arr_1d = np.random.randint(1, 11, size=10)

# 2D array of shape (3, 3) containing numbers from 1 to 9
arr_2d = np.random.randint(1, 10, size=(3, 3))

print("1D Random Array:\n", arr_1d)
print("\n2D Random Array (3x3):\n", arr_2d)