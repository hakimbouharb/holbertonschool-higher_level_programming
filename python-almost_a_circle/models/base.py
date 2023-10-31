#!/usr/bin/python3
"""Create a folder named models with an empty file
__init__.py inside - with this file, the folder
will become a Python package"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
