#!/usr/bin/python3

"""
defines a function that prints a square of #
"""


def print_square(size):
    """
    Args:
    size - integer size of square

    Return: None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print(size*"#")
