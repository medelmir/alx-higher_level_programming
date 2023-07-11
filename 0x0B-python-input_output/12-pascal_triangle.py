#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
     """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    new_list = [[1], [1, 1]]
    for i in range(2, n):
        new_list.append([1])
        for j in range(1, i):
            new_list[i].append(new_list[i - 1][j - 1] + new_list[i - 1][j])
        new_list[i].append(1)
    return new_list
