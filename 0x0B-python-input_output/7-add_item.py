#!/usr/bin/python3
""" script that adds all arguments to python list"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv
filename = "add_item.json"

with open(filename, mode='a+') as file:
    my_list = load_from_json_file(filename)
    for i in args[1:]:
        my_list.append(i)
    save_to_json_file(my_list, filename)
