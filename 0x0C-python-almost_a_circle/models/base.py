#!/usr/bin/python3

"""
defines a Base class that should be the parent of all other created
classes in this code
"""


class Base:
    """
    contains:
    private attributes: __nb_objects
    public attributes: id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        it checks:
        - if id is not None, assign the public instance attribute id with this
          argument value - you can assume id is an integer and you don’t need
          to test the type of it

        - otherwise, increment __nb_objects and assign the new value to the
          public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
