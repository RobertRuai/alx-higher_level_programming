#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary[i] > a_dictionary[i] + 1:
                return a_dictionary[i]
            return a_dictionary[i] + 1
        return None
