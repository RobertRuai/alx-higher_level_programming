#!/usr/bin/python3
""" base class module"""
import json
import os


class Base:
    """ base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string repr of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves instances as json strings """
        n_list = []
        if list_objs is not None and len(list_objs) > 0:
            for ob in list_objs:
                n_list.append(ob.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as file:
            file.write(Base.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj from a json string repr"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with set attrs"""
        if cls.__name__ == "rectangle":
            dummy = cls(2, 4)
	else:
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns instances in a list"""
        filename = ".json".format(cls.__name__)
        a_list = []

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as file:
            n_list = cls.from_json_string(file.read())
        for i, j in enumerate(n_list):
            a_list.append(cls.create(n_list[i]))
        return
