#!/usr/bin/python3
"""function that writes a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w") as file:
        return (file.write(text))
