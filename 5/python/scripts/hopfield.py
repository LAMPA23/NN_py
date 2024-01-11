import numpy as np 
import openpyxl


def print_matrix_to_excle_with_color(sheet, offset_row, offset_column, M, color='FFFF00'):
     for row in range(M.shape[0]):
        for column in range(M.shape[1]):
            sheet.cell(row=row+1+offset_row,column=column+1+offset_column,value=M[row,column]).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')
            if M[row,column] >= 0:
                sheet.cell(row=row+1+offset_row,column=column+1+offset_column,).fill = openpyxl.styles.PatternFill(start_color=color, end_color=color, fill_type='solid')



def print_err(sheet, column, value):
    sheet.cell(row=1,column=column+1,value=f'Кількість помилок - {(value*100/225):.0f} %').alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')
    sheet.cell(row=1,column=column+1).fill = openpyxl.styles.PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')
    sheet.column_dimensions[openpyxl.utils.get_column_letter(column+1)].width = 25



def vector_to_matrix(vector):
    matrix = np.zeros((7,4))
    for cnt in range(7):
        matrix[cnt] = vector[cnt*4:(cnt+1)*4]
    return matrix



def hopfield_recall(path_to_xlsx, workbook, sheet_name, W, NM_x, orig_vactor, iter_max):

    sheet = workbook.create_sheet(title=sheet_name)
     

    # Print noise vectors
    for cnt in range(225):
        print_matrix_to_excle_with_color(sheet, cnt*10, 0, vector_to_matrix(NM_x[cnt]), color='00FF00')


    for iter_cnt in range(iter_max):
        
        err_cnt = 0  

        for cnt in range(225):

            if iter_cnt == 0:
                old_vector = NM_x[cnt]

            new_vector = np.dot(W,old_vector)

            print_matrix_to_excle_with_color(sheet, cnt*10, iter_cnt*10+10, vector_to_matrix(new_vector))

            if not np.all(np.sign(new_vector) == NM_x[cnt]):
                err_cnt += 1
            
            old_vector = np.sign(new_vector)

        print_err(sheet, iter_cnt*10+15, err_cnt)
   
    workbook.save(path_to_xlsx)