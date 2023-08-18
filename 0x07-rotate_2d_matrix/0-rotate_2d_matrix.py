from typing import List

def swap_items(matrix, i, j):
    temp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = temp

def rotate_2d_matrix(matrix: List[List[int]]):
    n = len(matrix)
    
    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i + 1, n):  # Avoid swapping diagonal elements
            swap_items(matrix, i, j)
    
    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i].reverse()