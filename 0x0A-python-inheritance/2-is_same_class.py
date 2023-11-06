#!/usr/bin/python3

"""
Defines a function that returns True if the object is exactly an
instance of the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """
    check if the given object is an instance of the given class
    Args:
    abj - object to check
    class - class to compare with
    """
    # if isinstance(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
