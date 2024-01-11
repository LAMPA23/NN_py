import numpy as np 
import openpyxl
import os
import sys

# My scripts


from scripts.get_symbols import get_symbols
from scripts.create_noise_matrix import create_noise_matrix
from scripts.create_noise_matrix import create_target_ans_for_noise_matrix
from scripts.get_XTX import get_XTX
from scripts.get_W import get_W

path_i = 'xlsx\input.xlsx'
path_o = 'xlsx\output.xlsx'


os.system(f'del "{path_o}"')

workbook = openpyxl.Workbook()

# ------- Для звіту ----------- Start

# Створюю вектори символів 
# Дні буреуть з ексель файлу input.xlsx Дні буреуть з ексель файлу input.xlsx
vector_1, vector_2, vector_3  = get_symbols(path_i)


# Створюю матрицю, що містить оригінальні та зашумлені вектори.
# По 254 зашумлені вектори на символ.
# Дані будуть виведені на стрінці "NM" (файл - outpit.xlsx)
NM = create_noise_matrix(path_o, workbook, 'NM', (vector_1,vector_2,vector_3))


# Створюю матрицю, що вказує на те чим є зашмулений вестор.
# Ця матриця буде використовуватись для перевірок та навчання
# Дані будуть виведені на стрінці "NM_ans" (файл - outpit.xlsx)
NM_ans = create_target_ans_for_noise_matrix(path_o, workbook, 'NM_ans')


# Створюю матрицю з вектор символі. 
# Ці матриці будуть використані при стрворенні матриці вагів
# Дані будуть виведені на стрінці "XTX №х" (файл - outpit.xlsx)
XTX_1 = get_XTX(path_o, workbook, 'XTX №1', vector_1)
XTX_2 = get_XTX(path_o, workbook, 'XTX №2', vector_2)
XTX_3 = get_XTX(path_o, workbook, 'XTX №3', vector_3)


# Створюю матрицю вагів
# Дані будуть виведені на стрінці "W" (файл - outpit.xlsx)
W = get_W(path_o, workbook, 'W', (XTX_1,XTX_2,XTX_3))



noise_vector_1 = NM[224]
noise_vector_2 = NM[224 + 225]
noise_vector_3 = NM[224 + 450]




# ------- Для звіту ----------- End