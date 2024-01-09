import numpy as np 
import openpyxl
import math


def apply_centroids(path_to_xlsx, workbook, sheet_name, centroids, noise_matrix, corect_ans):
    
    # Create void matrix
    Euclidean_distance = np.zeros((675,3))
    ans = np.zeros((675,3)).astype(int)
    err = np.zeros(3).astype(int)


    # Calculate Euclidean distance
    for row in range(675):
        for symbol in range(3): 
            for column in range(28):     
                Euclidean_distance[row, symbol] += (centroids[symbol][column] - noise_matrix[row,column])**2
            Euclidean_distance[row, symbol] = math.sqrt(Euclidean_distance[row, symbol])

        # Chack how Euclidean distance is less
        min_evclid_distance = min(Euclidean_distance[row, 0], Euclidean_distance[row, 1], Euclidean_distance[row, 2])
        for cnt in range(3):
            if Euclidean_distance[row, cnt] == min_evclid_distance:
                ans[row,cnt] = 1
    


    # Error check
    for row in range(225):
        for symbol in range(3):
            if not np.all(corect_ans[symbol * 225 + row, :] == ans[symbol * 225 + row, :]):
                err[symbol] += 1
    


    # Excel print ----------------------------

    # Create new sheet
    sheet = workbook.create_sheet(title=sheet_name) 

    # Centring a text in cell
    for row in range(676):
        for column in range(8):
            sheet.cell(row=row+1, column=column+1).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')

    # Add table
    sheet.cell(row=1, column=1, value='Символ №1').fill = openpyxl.styles.PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
    sheet.cell(row=1, column=2, value='Символ №2').fill = openpyxl.styles.PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
    sheet.cell(row=1, column=3, value='Символ №3').fill = openpyxl.styles.PatternFill(start_color="0000FF", end_color="0000FF", fill_type="solid")


    # # Add color and value to matrix
    # for row in range(675):
    #     sheet.cell(row=row+2, column=1, value=target_data[row,0]).fill = openpyxl.styles.PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
    #     sheet.cell(row=row+2, column=2, value=target_data[row,1]).fill = openpyxl.styles.PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
    #     sheet.cell(row=row+2, column=3, value=target_data[row,2]).fill = openpyxl.styles.PatternFill(start_color="0000FF", end_color="0000FF", fill_type="solid")


    # Save data to Excel   
    workbook.save(path_to_xlsx)