#!/usr/bin/python3

"""
Defines a Student Class
"""


class Student:
    """
    Uses json to retrive dictionary representation of the class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
