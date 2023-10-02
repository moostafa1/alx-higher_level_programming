#!/usr/bin/python3

"""
Defines a function that returns list of lists
"""


def factorial(num):
    result = 1
    while num:
        result *= num
        num -= 1
    return result


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        pascal = [factorial(i) // (factorial(j) * factorial(i-j)) for
                  j in range(i+1)]
        pascal_triangle.append(pascal)
    return pascal_triangle
