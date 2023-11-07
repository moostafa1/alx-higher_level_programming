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

    def to_json(self, attrs=None):
        if attrs is not None:
            dic = {k: self.__dict__[k] for k in attrs if hasattr(self, k)}
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
