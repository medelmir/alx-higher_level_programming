#!/usr/bin/python3
""" class Student that defines a student"""


class Student:
    """ class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """ Instantiation of attributes for class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method that retrieves a dictionary representation of a Student"""
        return self.__dict__
