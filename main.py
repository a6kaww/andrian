import numpy as np

def transp_matrix(matrix):
    n = len (matrix)
    result = [[matrix[j][i].conjugate() for j in range(n)] for i in range(n)]
    return result

matrix_D = np.array([[1+1j, 3, 2],[8, -5j, 7-1j]])
print(matrix_D)
print(transp_matrix(matrix_D))

matrix_F = np.array([[2+1j, 1, 0, 0],[1, 2-1j, 0, 0],[0,0,1+1j, 1],[0, 0, 1, 1-1j]])
print(transp_matrix(matrix_F))