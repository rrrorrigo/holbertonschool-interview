#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers representing
    the Pascal’s triangle of n

    return: An empty list if n <= 0, else Pasca triangle of n"""
    p_triangle = []
    for y in range(n):
        aux_list = []
        if y > 0:
            aux_list.append(1)
        for x in range(y - 1):
            aux_list.append(p_triangle[y - 1][x] + p_triangle[y - 1][x + 1])
        aux_list.append(1)
        p_triangle.append(aux_list)
    return p_triangle
