#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        self.__size = size
        try:
            if not int(size):
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
