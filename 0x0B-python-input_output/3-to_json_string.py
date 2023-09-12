#!/usr/bin/python3

"""
using JSON library
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
        my_obj: the object data structure
    """
    import json

    return json.dumps(my_obj)
