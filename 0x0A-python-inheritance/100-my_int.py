#!/usr/bin/python3
""" myInt module """


class MyInt(int):
    """ myInt class """

    def __eq__(self, op):
        return int(self) != op

    def __ne__(self, op):
        return int(self) == op
