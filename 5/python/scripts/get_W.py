import numpy as np 
import openpyxl

def get_W(path_to_xlsx, workbook, sheet_name, XTXs):

    sheet = workbook.create_sheet(title=sheet_name)

    W = np.zeros((28,28))
    
    W = XTXs[0] + XTXs[1] + XTXs[2] 
    
    np.fill_diagonal(W, 0)

    for row in range(28):
        for column in range(28):
            sheet.cell(row=row+1, column=column+1, value=W[row,column]).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')

    workbook.save(path_to_xlsx)

    return W