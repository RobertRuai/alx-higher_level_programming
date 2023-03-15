#!/usr/bin/python3
def uniq_add(my_list=[]):

    s = 0
    for i, j in enumerate(set(my_list)):
	    s = s + j
    return s
