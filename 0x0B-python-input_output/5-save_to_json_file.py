#!/usr/bin/python3

"""
Save to json files
"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    import json

    # data = json.dumps(my_obj)
    with open(filename, "w") as f:
        json.dump(my_obj, f)
