#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row 


    :param n: number of rows to generate
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: list of lists of integers
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j -1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
