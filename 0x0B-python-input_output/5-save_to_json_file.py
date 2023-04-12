#!/usr/bin/python3
""" a function that writes object to txt file """
import json


def save_to_json_file(my_obj, filename):
    """ writes object to txt file """
    with open(filename, mode='w') as file:
        file.write(json.dumps(my_obj))
