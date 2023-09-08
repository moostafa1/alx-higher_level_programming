#!/usr/bin/python3

"""

Defines an integer addition function

"""


def add_integer(a, b=98):
    """Args:
    a, b - integer or float
    Return: sum of a + b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
