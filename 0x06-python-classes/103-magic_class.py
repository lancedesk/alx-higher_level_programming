#!/usr/bin/python3
"""Define a class Square that represents a square."""
import math


class MagicClass:
    """
    A class that represents a magic circle with radius as its attribute.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
