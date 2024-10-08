#print("SubModTest")

# Outsiders libraris 
import numpy as np 
import random as rd
import openpyxl
import os
import sys


# My python scripts
from scripts.get_symbols import get_symbols
from scripts.create_noise_matrix import create_noise_matrix
from scripts.create_noise_matrix import create_target_ans_for_noise_matrix
from scripts.create_mixed_data import create_mixed_data
from scripts.get_math_centroids import get_math_centroids
from scripts.check_centroids import check_centroids
from scripts.KM import create_KM
from scripts.KL import apply_KL
from scripts.show import plot_interpolated_vectors


# Excel files
path_input_xlsx = 'xlsx\input.xlsx' # (input.xlsx)
path_output_xlsx = 'xlsx\output.xlsx' # (output.xlsx)


# Delite old output file
os.system(f'del "{path_output_xlsx}"')


# Create object for Excel
workbook = openpyxl.Workbook()


# ----------------------------  MAIN  ---------- START

# Отримую вектори символів
# Вхідні дані в input.xlsx
symbols = get_symbols(path_input_xlsx)


# Створюю зашумлену матрицю з векторів символів
# Результати в "Зашумлена матриця" (output.xlsx)
noise_matrix = create_noise_matrix(path_output_xlsx, workbook, 'Зашумлена матриця', symbols) 


# Створюю матрицю з класифікацією векторів в зашумленій матриці 
# Результати в "Правильна класифікація" (output.xlsx)
target_matrix = create_target_ans_for_noise_matrix(path_output_xlsx, workbook, 'Правильна класифікація')


# Обраховую центроїди метеметично
# Результати в "Центроїди (математично обрах.)" (output.xlsx)
math_centroids = get_math_centroids(path_output_xlsx, workbook, 'Центроїди (математично обрах.)', noise_matrix)
  

# Засточовую математично обчислені центроїди для класифікації зашумленої матриці 
# Результати в "Класифівкація мат. центр." (output.xlsx)
check_centroids(path_output_xlsx, workbook, 'Класифівкація мат. центр.', math_centroids, noise_matrix, target_matrix)


# Перемішую вектори в середині зашумленої матриці
# Створюю відповідну до вже перемішаної матриці правильну класифікацію векторів
# Результати в "Перемішані зашум. дані" (output.xlsx)
mixed_noise_matrix, mixed_target_data = create_mixed_data(path_output_xlsx, workbook, 'Перемішані зашум. дані', noise_matrix)


# Засточовую математично обчислені центроїди для класифікації перемішаної зашумленої матриці 
# Результати в "Класифік. перем. мат.центр." (output.xlsx)
check_centroids(path_output_xlsx, workbook, 'Класифік. перем. мат.центр.', math_centroids, mixed_noise_matrix, mixed_target_data)


for cnt in range(100):

    # Засточовую центроїди отримані за допомогою НМ КК для класифікації перемішаної зашумленої матриці 
    # Результати в "Класифівкація НМ. центр." (output.xlsx)
    som_map = create_KM(path_output_xlsx, workbook, 'Центроїди (НМ КК)', mixed_noise_matrix)

    
    # Створюю НМ КК та використовую її для визначення координат центроїдів
    # Результати в "Центроїди (НМ КК)" (output.xlsx)
    err = check_centroids(path_output_xlsx, workbook, 'Класифівкація НМ. центр.', som_map, mixed_noise_matrix, mixed_target_data)

    # Застосування трьох конкурентних шарів Кохонена для класифікації векторів
    # Результати в "Результ. клсифікац. НМ ШК" (output.xlsx)
    apply_KL(path_output_xlsx, workbook, 'Результ. клсифікац. НМ ШК', mixed_noise_matrix, som_map, mixed_target_data)
    
    if err < 10:
        print('Good')
        plot_interpolated_vectors(np.concatenate((math_centroids[0],math_centroids[1],math_centroids[2])), np.concatenate((som_map[0],som_map[1],som_map[2])))
        sys.exit()

print('Fale')      
        
# ----------------------------  MAIN  ---------- END
