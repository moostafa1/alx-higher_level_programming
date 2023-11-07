#!/usr/bin/python3

"""
Defines a function that appends to a file
"""


def append_write(filename="", text=""):
    """
    Append text to a given file

    Args:
        filename: name of the file to append to (optional)
        text: text to append (optional)
    """
    with open(filename, "a") as f:
        return f.write(text)
