#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
Contains the definition of the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of, or inherited from specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare with.

    Returns:
        bool: True if obj is an instance of a_class or inherited from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
