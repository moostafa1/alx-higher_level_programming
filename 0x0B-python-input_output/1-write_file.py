#!/usr/bin/python3

"""
Defines a function that writes to a file
"""


def write_file(filename="", text=""):
    """
    Write to a given file

    Args:
        filename: file to write to (optional)
        text: text to write to a file (optional)
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
