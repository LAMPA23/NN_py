import numpy as np 
import openpyxl

def restoration(path_to_xlsx, workbook, sheet_name, W, noise_vector):
    
    sheet = workbook.create_sheet(title=sheet_name)

    for row in range(7):
        for column in range(4):
            sheet.cell(row=row+1,column=column+1,value=noise_vector[row*4+column]).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')
            if noise_vector[row*4+column] == 1:
                sheet.cell(row=row+1,column=column+1).fill = openpyxl.styles.PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    
    restor_vector = np.dot(W,noise_vector)

    for row in range(7):
        for column in range(4):
            sheet.cell(row=row+10,column=column+1,value=restor_vector[row*4+column]).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')
            if restor_vector[row*4+column] >= 0:
                sheet.cell(row=row+10,column=column+1).fill = openpyxl.styles.PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')

    workbook.save(path_to_xlsx)
    return restor_vector

