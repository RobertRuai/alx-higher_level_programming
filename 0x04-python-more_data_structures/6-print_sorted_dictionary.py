#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    for sortkey in sorted(a_dictionary.keys()):    
        print(f"{sortkey}: {a_dictionary[sortkey]}")
