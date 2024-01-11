import numpy as np

arr = np.array([[1, -2, 3],
                [4, -5, 6],
                [-7, 8, -9]])

a = np.dot(arr, 10)
b = np.sign(a)
print(a)
print(b)