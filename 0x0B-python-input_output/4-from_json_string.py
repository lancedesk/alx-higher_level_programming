#!/usr/bin/python3
"""
Module to provide a function that returns
an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return the object represented by a JSON string.

    Args:
        my_str (str): JSON string to be converted to an object.

    Returns:
        obj: Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
