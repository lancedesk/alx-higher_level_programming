#!/usr/bin/python3
"""
Module: 2-is_same_class
Contains the definition of the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare with.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
