# Outsiders libraris 
import numpy as np 
import random as rd
import openpyxl
import os


# My python scripts
from scripts.get_symbols import get_symbols
from scripts.create_noise_matrix import create_noise_matrix
from scripts.get_center import get_centers


# Excel files
path_input_xlsx = 'xlsx\input.xlsx' 
path_output_xlsx = 'xlsx\output.xlsx'


# Delite old output file
os.system(f'del "{path_output_xlsx}"')


# Create object for Excel
workbook = openpyxl.Workbook()


# ----------------------------  Using my functions

# Отримую вектори символів
# Вхідні дані в input.xlsx
symbols = get_symbols(path_input_xlsx)

# Створюю зашумлену матрицю з векторів символів
# Результати в "Зашумлена матриця"
noise_matrix = create_noise_matrix(path_output_xlsx, workbook, symbols) 

# Обраховую центроїди метеметично
# Результати в "Центроїди"
math_centers = get_centers(path_output_xlsx, workbook, noise_matrix)
  
# Засточовую математично обчислені центроїди для класифікації зашумленої матриці 
# Результати в "Класиівкація математичними центроїдами"




# ----------------------------  Using my functions ---------- END