#!/usr/bin/python3

"""
Defines a function that reads a file
"""


def read_file(filename=""):
    """
    reads a file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
