#!/usr/bin/python3
"""defines a square by:
    Private instance attribute: size
    Instantiation with size 
    (no type/value verification)"""


class Square:
    """defines a square and initialize with size
       
       args:
            size(int): size of the square
    """
    def __init__(self, size):
        self.__size = size
