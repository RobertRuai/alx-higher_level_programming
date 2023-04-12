#!/usr/bin/python3
""" script thar adds all arguments to python list"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv
filename = "add_item.json"
with open(filename, mode='a+') as file:
    my_list = args[1:]
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
