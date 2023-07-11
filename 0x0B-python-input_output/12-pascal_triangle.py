#!/usr/bin/python3
"""function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascal’s
triangle of n"""


def pascal_triangle(n):
     """function def pascal_triangle(n)"""
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
