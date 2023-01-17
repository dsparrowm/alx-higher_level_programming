#!/usr/bin/python3
"""implements a class that inherits from Rectangle class
    Square is a subclass of Rectangle
    Rectangle is a subclass of Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class to that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the width or height of square.
        As a reminder:
            Square is just a Rectangle with equal width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the width or height of square since both are the
        same with square"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        self.width = value
        self.height = value

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """returns the string representation of square attributes"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates the square class"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
