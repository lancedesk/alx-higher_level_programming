#!/usr/bin/python3
"""
Module: 11-square
Defines a class Square that inherits from Rectangle and implements area method.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
