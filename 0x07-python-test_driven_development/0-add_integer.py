#!/usr/bin/python3

def add_integer(a, b=98):
    """Function that adds 2 integers
    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        The addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
