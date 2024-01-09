import numpy as np

# Ваша матриця
my_matrix = np.random.rand(30,10)

# Перемішування індексів рядків
shuffled_indices = np.random.permutation(my_matrix.shape[0])

# Застосування перемішаних індексів до матриці
shuffled_matrix = my_matrix[shuffled_indices, :]

print(shuffled_indices)
