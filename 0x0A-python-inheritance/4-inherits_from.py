#!/usr/bin/python3
""" class module"""


def inherits_from(obj, a_class):
    """ determins if obj is instance of a_class """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    return False
