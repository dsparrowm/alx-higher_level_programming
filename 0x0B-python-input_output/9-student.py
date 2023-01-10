#!/usr/bin/python3
"""This module creates a class that defines a student"""


class Student:
    """This class defines a student
    args:
        first_name(str): first name of the student
        last_name(str): last name of the student
        age(int): age of the student"""
    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary representation of the student"""
        return self.__dict__
