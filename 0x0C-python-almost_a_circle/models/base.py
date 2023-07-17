#!/usr/bin/python3
"""Defines a base model class."""
import json
import turtle
import random


class Base:
    """Represent the base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes."""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as csvfile:
            if list_objs is None:
                csvfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                csvfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csvfile:
                list_dicts = cls.from_json_string(csvfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle"""

        turtle.title("Squares and Rectangles")
        turtle.bgcolor("black")
        turtle.hideturtle()
        turtle.speed(0)
        turtle.pensize(3)

        colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        for r in list_rectangles:
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.goto(r.x, r.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(r.width)
                turtle.left(90)
                turtle.forward(r.height)
                turtle.left(90)

        for s in list_squares:
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.goto(s.x, s.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(s.width)
                turtle.left(90)
                turtle.forward(s.height)
                turtle.left(90)

        turtle.exitonclick()
