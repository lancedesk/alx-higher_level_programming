#!/usr/bin/python3
"""
This module defines a function called `lookup` that takes an object as input
and returns a list of its available attributes and methods.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The input object to inspect.

    Returns:
        list: A list containing the attributes and methods of the object.
    """
    return dir(obj)
