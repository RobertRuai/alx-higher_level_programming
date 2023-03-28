#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        try: 
            if  (isinstance(size, int) is False):
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size
