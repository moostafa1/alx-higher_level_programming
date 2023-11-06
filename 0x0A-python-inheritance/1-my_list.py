#!/usr/bin/python3

"""
Applying class inheritance
"""


class MyList(list):
    """print sorted list"""
    def print_sorted(self):
        print(sorted(self))
