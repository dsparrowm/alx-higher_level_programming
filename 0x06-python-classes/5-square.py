#!/usr/bin/python3
"""defines a square"""


class Square:
    """defines a square
    args:
        size(int): size of the square
    Return:
        the area of the square"""
    def __init__(self, size=0):
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if value < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
