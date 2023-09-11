#!/usr/bin/python3

"""
Defines function that checks if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class, else False
    """
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    return False
