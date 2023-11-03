#!/usr/bin/python3

"""
Defines a function that prints My name is <first name> <last name>
"""


def text_indentation(text):
    """
    Args:
    first_name - first input name
    last_name - last input name (optional)
    Return: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    rem = [".", "?", ":"]
    for i in rem:
        text = text.replace(i, i[0]+"\n\n").replace("\n ", "\n")
    print(text, end="")
