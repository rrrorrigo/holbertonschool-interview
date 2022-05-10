#!/usr/bin/python3
"""Minor operations"""


def minOperations(n):
    """Function that calculates the fewest number of operations needed to
    result in exactly n 'H' characters in the file

    n: minimum number of operations

    Return: n"""
    if n <= 0:
        return 0
    r = 'H'
    copy = ''
    l = len(r)
    while l < n:
        l = len(r)
        if l % n and copy != r:
            copy = r
            continue
        if copy == r:
            r += copy
            continue
    return l
