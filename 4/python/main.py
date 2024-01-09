# Outsiders libraris 
import numpy as np 
import random as rd
import openpyxl
import os


# My python scripts
from scripts.get_symbols import get_symbols
from scripts.create_noise_matrix import create_noise_matrix


# Excel files
path_input_xlsx = 'xlsx\input.xlsx' 
path_output_xlsx = 'xlsx\output.xlsx'


# Delite old output file
os.system(f'del "{path_output_xlsx}"')


symbols = get_symbols(path_input_xlsx)
noise_matrix = create_noise_matrix(path_output_xlsx, symbols)