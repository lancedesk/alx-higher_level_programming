#!/usr/bin/python3
"""
Module to provide a function that returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: Object to be converted to JSON.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
