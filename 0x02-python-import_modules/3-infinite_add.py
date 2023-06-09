#!/usr/bin/python3
if __name__ == "__main__":
    """rints the result of the addition of all arguments"""
    from sys import argv
    sum = 0
    argc = len(argv) - 1
    for i in range(1, argc + 1):
        sum = sum + int(argv[i])
    print("{:d}".format(sum))
