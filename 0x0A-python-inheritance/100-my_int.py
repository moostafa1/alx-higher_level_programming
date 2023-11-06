#!/usr/bin/python3

"""
Defines MyInt class that inherits from the integer class
"""


class MyInt(int):
    """
    MyInt class is a rebel class
    """
    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
