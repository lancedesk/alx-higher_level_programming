#!/usr/bin/python3
"""
Module: 6-base_geometry
Defines a class BaseGeometry with a method area().
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
