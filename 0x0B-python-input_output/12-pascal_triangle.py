#!/usr/bin/python3
"""
Module for generating Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
