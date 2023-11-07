#!/usr/bin/python3

"""
creates object from json file
"""


def load_from_json_file(filename):
    """
    Loads data from json file
    """
    import json

    with open(filename) as f:
        json_object = json.load(f)
    return json_object
