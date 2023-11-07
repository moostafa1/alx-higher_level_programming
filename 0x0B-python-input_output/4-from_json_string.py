#!/usr/bin/python3

"""
Using json
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: input string
    """
    import json

    return json.loads(my_str)
