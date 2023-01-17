#!/usr/bin/python3
"""This module contains the class Rectangle and it is a subclass
    of Base class
    """
import unittest
from models.base import Base


class Rectangle(Base):
    """This class is a subclass of Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the rectangle's width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height, 'x': self.x,
                'y': self.y}

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """overide the string representation of an object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """displays the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """updaates rectangle
        args:
            *args: variable number of no-keyworded arguments
            **kwargs: key/value arguments
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass
