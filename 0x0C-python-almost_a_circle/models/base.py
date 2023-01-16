#!/usr/bin/python3
"""This module contains the base class that will be used throughout
    several files"""


class Base:
    """this is the base class to be used by other 
    subclasses in this module
    This class will be the “base” of all other classes in
    this project. The goal of it is to manage id attribute
    in all your future classes and to avoid duplicating 
    the same code (by extension, same bugs)

    Args:
        __nb_objects(int): number of instances created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantilize  the base class
        Args:
            id(int): the identity of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

