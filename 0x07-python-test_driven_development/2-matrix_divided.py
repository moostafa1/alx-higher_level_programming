#!/usr/bin/python3

def matrix_divided(matrix, div):
    try:
        for lst in matrix:
            for n in lst:
                if not isinstance(n, (int, float)):
                    raise TypeError("matrix must be a matrix\
                            (list of lists) of integers/floats")
    except TypeError:
        print("matrix must be a matrix\
                (list of lists) of integers/floats")
    row_len = [len(lst) for lst in matrix]

    if len(set(row_len)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda lst: list(map(lambda x: round(x/div, 2), lst)),
                matrix))
