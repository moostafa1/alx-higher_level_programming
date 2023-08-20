#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [v**2 for v in row], matrix))
