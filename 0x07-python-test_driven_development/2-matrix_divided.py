#!/usr/bin/python3
"""
This module provides functions for matrix operations,
including matrix division and element validation.
"""


def is_valid_element(elem):
    """
    Helper function to check if an element is an integer or float.

    Args:
        elem (int or float): Element to be validated.

    Returns:
        bool: True if elem is an instance of int or float, False otherwise.
    """
    return isinstance(elem, (int, float))


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    Returns a new matrix.

    Args:
        matrix (list of lists): Input matrix containing integers or floats.
        div (int or float): Divisor to divide the matrix elements by.

    Returns:
        list of lists: New matrix with elements divided by the divisor.

    Raises:
        TypeError: If input matrix is not a list of lists of integers/floats,
        or if any row has different sizes, or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Error message for invalid matrix format
    error = "matrix must be a matrix (list of lists) of integers/floats"

    # Validate input matrix format
    if not isinstance(matrix, list):
        raise TypeError(error)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error)

    # Validate elements in the matrix using the helper function
    if any(not all(is_valid_element(elem) for elem in row) for row in matrix):
        raise TypeError(error)

    # Validate equal row sizes
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Avoid division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    return [[round(elem / div, 2) for elem in row] for row in matrix]
