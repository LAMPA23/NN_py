# Outsiders libraris 
import numpy as np 
import random as rd
import openpyxl
import os


# My python scripts
from scripts.get_symbols import get_symbols
from scripts.create_noise_matrix import create_noise_matrix
from scripts.create_noise_matrix import create_target_ans_for_noise_matrix
from scripts.create_mixed_data import create_mixed_data
from scripts.get_math_centroids import get_math_centroids
from scripts.apply_centroids import apply_centroids
from scripts.get_som import get_som


# Excel files
path_input_xlsx = 'xlsx\input.xlsx' # (input.xlsx)
path_output_xlsx = 'xlsx\output.xlsx' # (output.xlsx)


# Delite old output file
os.system(f'del "{path_output_xlsx}"')


# Create object for Excel
workbook = openpyxl.Workbook()


# ----------------------------  Using my functions

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
#math_ans = apply_centroids(path_output_xlsx, workbook, 'Класифівкація мат. центр.', math_centroids, noise_matrix, target_matrix)


# Перемішую вектори в середині зашумленої матриці
# Створюю відповідну до вже перемішаної матриці правильну класифікацію векторів
# Результати в "Перемішана зашум. дані" (output.xlsx)
mixed_noise_matrix, mixed_target_data = create_mixed_data(path_output_xlsx, workbook, 'Перемішана зашум. дані', noise_matrix)


# Засточовую математично обчислені центроїди для класифікації перемішаної зашумленої матриці 
# Результати в "Класифік. перем. мат.центр." (output.xlsx)
#math_ans = apply_centroids(path_output_xlsx, workbook, 'Класифік. перем. мат.центр.', math_centroids, mixed_noise_matrix, mixed_target_data)


som_map = get_som(mixed_noise_matrix)
math_ans = apply_centroids(path_output_xlsx, workbook, 'Класифівкація НМ. центр.', som_map, mixed_noise_matrix, mixed_target_data)

# ----------------------------  Using my functions ---------- END