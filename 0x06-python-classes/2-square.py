#!/usr/bin/python3

"""defines a class called Square"""


class Square:
    """Attributes:
        size: private (optional)
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size