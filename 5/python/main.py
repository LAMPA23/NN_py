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

vector_1, vector_2, vector_3  = get_symbols(path_i)
XTX_1 = get_XTX(path_o, workbook, 'XTX №1', vector_1)
XTX_2 = get_XTX(path_o, workbook, 'XTX №2', vector_2)
XTX_3 = get_XTX(path_o, workbook, 'XTX №3', vector_3)
W = get_W(path_o, workbook, 'W', (XTX_1,XTX_2,XTX_3))