#!/usr/bin/python3
"""Defines a function to print a square with '#' characters."""

def print_square(size):
    height_and_width = size
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
    # Ensure size is a non-negative integer

    if not isinstance(height_and_width, int):
        raise TypeError("size must be an integer")

    if height_and_width < 0:
        raise ValueError("size must be >= 0")

    # Iterate through rows and columns, printing '#' characters
    for index_i in range(height_and_width):
        [print("#", end="") for index_j in range(height_and_width)]
        print("")
