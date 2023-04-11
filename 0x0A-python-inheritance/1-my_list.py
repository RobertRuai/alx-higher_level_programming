#!/usr/bin/python3
""" list module"""


class MyList(list):
    """ mylist class """

    def print_sorted(self):
        s_list = sorted(self)
        print(s_list)
