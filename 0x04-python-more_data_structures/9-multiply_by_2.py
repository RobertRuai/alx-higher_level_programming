#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new_dictionary = a_dictionary.copy()
    for key, value in enumerate(new_dictionary):
        new_dictionary[value] *= 2
    return new_dictionary
