#!/usr/bin/python3

"""
Denfines a function that takes command line arguments and append it
to json file
"""


def cmd_to_json():
    from sys import argv
    from os import listdir

    argv = argv[1:]
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

    if 'add_item.json' not in listdir():
        save_json([], 'add_item.json')
    data = load_json('add_item.json')
    data.extend(argv)
    save_json(data, 'add_item.json')


if __name__ == "__main__":
    cmd_to_json()
