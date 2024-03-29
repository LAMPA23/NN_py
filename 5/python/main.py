# Outside scripts
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
from scripts.restoration import restoration
from scripts.hopfield import hopfield_recall


# Excel files paths
path_i = 'xlsx\input.xlsx'
path_o = 'xlsx\output.xlsx'

# Delete old output.xlsx file
os.system(f'del "{path_o}"')

# Excel preparation
workbook = openpyxl.Workbook()




# ------- Для звіту ----------- Start

# Створюю вектори символів 
# Дні буреуть з ексель файлу input.xlsx Дні буреуть з ексель файлу input.xlsx
vector_1, vector_2, vector_3  = get_symbols(path_i)


# Створюю матрицю, що містить оригінальні та зашумлені вектори.
# По 254 зашумлені вектори на символ + 1 оригінал. Це 225 на символ. На 3 символи це 675 векторів.
# Дані будуть виведені на стрінці "NM" (файл - outpit.xlsx)
NM = create_noise_matrix(path_o, workbook, 'NM', (vector_1,vector_2,vector_3))


# Створюю матрицю, що вказує на те чим є зашмулений вестор.
# Ця матриця буде використовуватись для перевірок та навчання
# Дані будуть виведені на стрінці "NM_ans" (файл - outpit.xlsx)
NM_ans = create_target_ans_for_noise_matrix(path_o, workbook, 'NM_ans')


# Створюю матрицю з векторів символів. 
# Ці матриці будуть використані при стрворенні матриці вагів
# Дані будуть виведені на стрінці "XTX №х" (файл - outpit.xlsx)
XTX_1 = get_XTX(path_o, workbook, 'XTX №1', vector_1)
XTX_2 = get_XTX(path_o, workbook, 'XTX №2', vector_2)
XTX_3 = get_XTX(path_o, workbook, 'XTX №3', vector_3)


# Створюю матрицю вагів
# Дані будуть виведені на стрінці "W" (файл - outpit.xlsx)
W = get_W(path_o, workbook, 'W', (XTX_1,XTX_2,XTX_3))


# Роздляю матрицю зашумлених векторів на три частина
# Кожна частину містить вектори, що відностяться до певного символу
NM_1 = NM[0:225]
NM_2 = NM[225:450]
NM_3 = NM[450:675]


# Відновлюю вектори образи та рахую кільість неправильно відновлених векторів.
# Неправильно відновленим вектором вважається такий, в якого хочаб одна клітинка є неправильною
# Дані будуть виведені на стрінці "Rх" (файл - outpit.xlsx)
restoration(path_o, workbook, 'R1', W, NM_1, vector_1)
restoration(path_o, workbook, 'R2', W, NM_2, vector_2)
restoration(path_o, workbook, 'R3', W, NM_3, vector_3)



# Тепер відновлюю зображення за допогою самотушки написаної непомережі Хопфілда
# Математичний принцим такий ж само як в попередній функції, тільки тепер, вихідні данні -
# - можуть в циклі передаватись на вхід. 
# Таким чином, можна поступово покращувати якість відновлення.
# Дані будуть виведені на стрінці "Нх" (файл - outpit.xlsx)
hopfield_recall(path_o, workbook, 'H1', W, NM_1, vector_1, 3)
hopfield_recall(path_o, workbook, 'H2', W, NM_2, vector_2, 3)
hopfield_recall(path_o, workbook, 'H3', W, NM_3, vector_3, 3)

# ------- Для звіту ----------- End

