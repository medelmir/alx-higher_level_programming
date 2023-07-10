#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        """method that returns the opposite of __eq__"""
        return super().__ne__(other)

    def __ne__(self, other):
        """method that returns the opposite of __ne__"""
        return super().__eq__(other)
