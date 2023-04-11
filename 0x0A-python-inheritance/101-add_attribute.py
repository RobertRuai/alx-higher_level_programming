#!/usr/bin/python3
"""function module that adds a new attribute to an object"""


def add_attribute(a, ad, add):
    """function"""

    if not hasattr(a, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(a, ad, add)
