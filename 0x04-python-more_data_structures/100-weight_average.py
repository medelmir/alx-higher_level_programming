#!/usr/bin/python3
def weight_average(my_list=[]):
    x = 0
    y = 0
    if my_list == []:
        return 0
    for tuple in my_list:
        x = (tuple[0] * tuple[1]) + x
        y = tuple[1] + y
    average = x / y
    return average
