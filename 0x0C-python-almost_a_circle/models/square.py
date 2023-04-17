#!/usr/bin/python3
""" square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        "__str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            self.id = args[0] if 0 < len(args) else self.id
            self.size = args[1] if 1 < len(args) else self.size
            self.x = args[2] if 2 < len(args) else self.x
            self.y = args[3] if 3 < len(args) else self.y
        else:
            for i, j in kwargs.items():
                if i == 'id':
                    self.id = j
                if i == 'size':
                    self.size = j
                if i == 'x':
                    self.x = j
                if i == 'y':
                    self.y = j

    def to_dictionary(self):
        """to_dictionary method"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
               }
