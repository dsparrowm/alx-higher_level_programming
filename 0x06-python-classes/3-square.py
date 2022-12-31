#!/usr/bin/python3
"""This module calculates the area of a square"""


class Square:
    """defines a square
    args:
        size(int): size of the square
    Returns:
        area of the square"""
    def __init__(self, size):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2
