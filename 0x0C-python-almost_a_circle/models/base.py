#!/usr/bin/python3
"""This module contains the base class that will be used throughout
    several files"""
import json
import csv



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

    @classmethod
    def safe_to_file(cls, list_objs):
        """write a list of objects to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries == None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
