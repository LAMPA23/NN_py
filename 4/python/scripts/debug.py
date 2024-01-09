import numpy as np 
import openpyxl
import os




def create_new_xlsx(path_to_xlsx):
    os.system(f'rm {path_to_xlsx}')
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    return workbook, sheet




def degub_matrix(path_to_xlsx, M):
    workbook, sheet = create_new_xlsx(path_to_xlsx)
    for row in range(0, M.shape[0]):
        for column in range(0, M.shape[1]):
            sheet.cell(row=row+1, column=column+1, value=M[row,column])
    workbook.save(path_to_xlsx)