#!/usr/bin/python3
""" a function that returns json string """
import json


def to_json_string(my_obj):
    """reads object string, returns json string"""
    return json.dumps(my_obj)
