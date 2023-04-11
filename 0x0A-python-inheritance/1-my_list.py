#!/usr/bin/python3
""" list module"""


class MyList(list):
    """ mylist class """

    def print_sorted(self):
        print(sorted(self))
