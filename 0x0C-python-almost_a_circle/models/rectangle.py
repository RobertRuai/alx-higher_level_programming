#!/usr/bin/python3
""" Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """ base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be => 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be => 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        s = ''

        if self.__width == 0 or self.__height == 0:
            return s

        if self.__y:
            print("\n" * self.__y, end='')
        for i in range(self.height):
            if self.__x:
                print(" " * self.__x, end='')
            print('#' * self.width)

    def __str__(self):
        return "[Rectangle] (" + str(self.id) + ") " + str(
            self.__x) + "/" + str(self.__y) + " - " + str(
                self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if 0 < len(args) else self.id
            self.width = args[1] if 1 < len(args) else self.width
            self.height = args[2] if 2 < len(args) else self.height
            self.x = args[3] if 3 < len(args) else self.x
            self.y = args[4] if 4 < len(args) else self.y
        else:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'width':
                    self.width = j
                if i == 'height':
                    self.height = j
                if i == 'x':
                    self.x = j
                if i == 'y':
                    self.y = j

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
               }
