#!/usr/bin/python3
""" function module"""


def class_to_json(obj):
    """ a function that returns the dictionary description """
    return obj.__dict__
