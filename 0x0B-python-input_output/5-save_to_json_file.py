#!/usr/bin/python3

"""
Save to json files
"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    import json
    from pathlib import Path

    data = json.dumps(my_obj)
    Path(filename).write_text(data)
