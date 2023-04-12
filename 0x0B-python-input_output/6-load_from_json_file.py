#!/usr/bin/python3
""" a function that creates object from json file """
import json


def load_from_json_file(filename):
    """ creates object from json file """
    with open(filename, 'r') as file:
        return json.loads(file.read())
