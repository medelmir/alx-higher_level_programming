#!/usr/bin/python3
"""classthat inherits"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
