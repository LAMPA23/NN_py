import numpy as np 
import openpyxl


def create_noise_matrix(path_to_xlsx, workbook, symbols):

    # Excel preparation
    sheet = workbook.create_sheet(title='Зашумлена матриця')
    

    # Creatin training matrix 675x28
    M = np.zeros((675,28)).astype(int)
    M[0:225,:] = symbols[0]
    M[225:450,:] = symbols[1]
    M[450:675,:] = symbols[2]


    # Add clear matrix to xlsx
    for row in range(0, M.shape[0]):
        for column in range(0, M.shape[1]):
            sheet.cell(row=row+1, column=column+1, value=M[row,column]).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')
            if M[row,column] == 1:
                sheet.cell(row=row+1, column=column+1).fill = openpyxl.styles.PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")


    # Add noise to clear matrix
    for cnt_1 in range(8):
        for cnt_2 in range(28):
            inverting_vector = np.array(range(cnt_2, cnt_2 + cnt_1 + 1)).astype(int) % 28
            rows = cnt_1 * 28 + cnt_2 + 1, cnt_1 * 28 + cnt_2 + 226, cnt_1 * 28 + cnt_2 + 451
            for row in rows:
                for column in inverting_vector:
                    M[row, column] = 1 if M[row, column] == -1 else -1
                    for column in inverting_vector:
                        sheet.cell(row=row+1, column=column+1, value=M[row, column]).fill = openpyxl.styles.PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
                

    # Save data to Excel
    workbook.save(path_to_xlsx)


    # Return noise matrix
    return M

