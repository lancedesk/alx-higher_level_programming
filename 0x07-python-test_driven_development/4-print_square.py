#!/usr/bin/python3
"""Defines a function to print a square with '#' characters."""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): Size of the square's height and width.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    # Iterate through rows and columns, printing '#' characters
    for index_i in range(size):
        [print("#", end="") for index_j in range(size)]
        print("")
