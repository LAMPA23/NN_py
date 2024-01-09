import numpy as np 
import openpyxl
import math

def apply_centroids(path_to_xlsx, workbook, centroids, noise_matrix):
    
    evclid_distance = np.zeros((675,3))
    ans = np.zeros((675,3))

    for row in range(225):
        for column in range(28):
            evclid_distance[row, 0] += (centroids[column,0] - noise_matrix[row,column])**2
            evclid_distance[row+225, 1] += (centroids[column,1] - noise_matrix[row+225,column])**2
            evclid_distance[row+450, 2] += (centroids[column,2] - noise_matrix[row+450,column])**2
        evclid_distance[row, 0] = math.sqrt(evclid_distance[row, 0])
        evclid_distance[row+225, 1] = math.sqrt(evclid_distance[row+225, 1])
        evclid_distance[row+450, 2] = math.sqrt(evclid_distance[row+450, 2])

        
        min_evclid_distance = min(evclid_distance[row, 0], evclid_distance[row+225, 1], evclid_distance[row+450, 2])
        for cnt in range(3):
            if evclid_distance[row, cnt] == min_evclid_distance:
                ans[row,cnt] = 1