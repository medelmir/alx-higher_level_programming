#!/usr/bin/python3
"""a function that appends a string at the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a") as file:
        return (file.write(text))
