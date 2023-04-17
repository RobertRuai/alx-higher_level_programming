#!/usr/bin/python3
""" Rectangle class module"""
from models.base import Base


class Rectangle(Base):
     """This class inherits from Base and defines a Rectangle object.
    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.
        __x (int): the horizontal (x) padding of the rectangle.
        __y (int): the vertical (y) padding of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object.
        Args:
            width (int): the wanted width of the rectangle.
            height (int): the wanted height of the rectangle.
            x (int): the wanted horizontal (x) padding of the rectangle.
            y (int): the wanted vertical (y) padding of the rectangle.
            id (int): the wanted identifier of the Base object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
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
        """ height getter"""
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
        """x getter"""
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
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be => 0")
        self.__y = value

    def area(self):
        """Returns the area"""
        return self.width * self.height

    def display(self):
        """prints rectangle using #"""
        if self.y:
            print("\n" * self.y, end='')
        for i in range(self.height):
            if self.x:
                print(" " * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """prints rectangle in str format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates rectangle by assigning attrs to args and kwargs"""
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
        """prints dict repr"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
               }
