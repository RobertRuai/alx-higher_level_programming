#!/usr/bin/python3
""" class module"""


def is_kind_of_class(obj, a_class):
    """ determins if obj is instance of a_class """
    if isinstance(obj, a_class):
        return True
    return False
