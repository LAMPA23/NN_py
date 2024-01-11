import numpy as np

# Створимо масив для прикладу
arr_1 = np.array([[1, -2, 3],
                [4, -5, 6],
                [-7, 8, -9]])

arr_2 = np.array([[2, -2, 8],
                [-4, 7, 6],
                [-1, -6, 3]])



bin_restor_vector = np.where(restor_vector>0,1,-1)
if not np.all(bin_restor_vector == noise_vector):
    err_cnt += 1
    print()

# Виведемо результат
print("Original array:")
print(arr)

print("\nTransformed array:")
print(result)
