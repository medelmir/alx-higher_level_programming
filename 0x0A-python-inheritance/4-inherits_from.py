#!/usr/bin/python3
"""True if the object is an instance of aclass otherwise False."""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of aclass"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
