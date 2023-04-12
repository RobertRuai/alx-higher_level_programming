#!/usr/bin/python3
""" Student module """


class Student():
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        n = {}
        if attrs is not None:
            for i, j in self.__dict__.items():
                if i in attrs:
                    n[i] = self.__dict__[i]
            return n
        return self.__dict__

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
