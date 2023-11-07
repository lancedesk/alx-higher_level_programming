#!/usr/bin/python3
"""
Module to provide a function that serializes an instance of a class into a dictionary
with simple data structures for JSON serialization.
"""


def class_to_json(obj):
    """
    Serialize an instance of a class into a dictionary for JSON serialization.

    Args:
        obj: Instance of a class.

    Returns:
        dict: Dictionary representation of the object.
    """
    return obj.__dict__
