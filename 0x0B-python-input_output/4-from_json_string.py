#!/usr/bin/python3
""" a function that returns python obj from json string """
import json


def from_json_string(my_str):
    """reads json string, returns python object"""
    return json.loads(my_str)
