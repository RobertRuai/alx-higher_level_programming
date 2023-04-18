#!/usr/bin/python3
""" base class module"""
import json
import os
import csv
import turtle


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
        if cls.__name__ == "Rectangle":
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
            n_list = Base.from_json_string(file.read())
        for i, j in enumerate(n_list):
            a_list.append(cls.create(n_list[i]))
        return n_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes the CSV string representation to file"""
        fields = []
        with open(cls.__name__ + ".csv", 'w') as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write('[]')
            else:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes the CSV string representation
        of list_objs from a file.
        """
        fields = []
        try:
            with open(cls.__name__ + ".csv", 'r') as f:
                if cls.__name__ is "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ is "Square":
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in l.items())
                        for l in reader]
                return [cls.create(**dct) for dct in dcts]

        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): a list of rectangle instances.
            list_squares (list): a list of square instances.
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
