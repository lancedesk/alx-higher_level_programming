#!/usr/bin/python3
"""
Module: 7-base_geometry
Defines a class BaseGeometry with public methods area()
and integer_validator().
"""


class BaseGeometry:
    """
    A class representing a base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.
        Raises:
            Exception: Always raises an exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
