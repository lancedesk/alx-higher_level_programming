#!/usr/bin/python3
"""
Module: 101-add_attribute
Defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to the object if possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attribute (str): The name of the attribute.
        value (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
