#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = [[v**2 for v in row] for row in matrix]
    return mat
