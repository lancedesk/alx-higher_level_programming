#!/usr/bin/python3
"""
Module: 4-inherits_from
Contains the definition of the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from a_class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare with.

    Returns:
        bool: True if obj is an instance of a class inherited from a_class,
        False otherwise.
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
