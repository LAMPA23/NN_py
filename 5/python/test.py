import numpy as np

# Створимо матрицю для прикладу
matrix_A = np.array([[1, -1]])

# Помножимо матрицю на саму себе
result_square = np.dot(matrix_A, matrix_A)

# Виведемо результат
print("Result of matrix multiplication with itself:")
print(result_square)
