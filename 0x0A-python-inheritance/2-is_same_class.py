#!/usr/bin/python3
""" class module"""


def is_same_class(obj, a_class):
    """ determins if obj is instance of a_class """
    if type(obj) is a_class:
        return True
    return False
