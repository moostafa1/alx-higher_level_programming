#!/usr/bin/python3
"""
Defines a function that returns True if the object is an instance of, or
if the object is an instance of a class that inherited from, the specified
class, otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or an instance of a class
    that is inherited from

    Args:
        obj - object to check
        a_class - the class to match the type of the object with
    Return:
        True if matched, else False
    """
    if isinstance(obj, a_class):
        return True
    return False
