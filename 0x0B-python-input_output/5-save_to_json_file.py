#!/usr/bin/python3
"""
Module to provide a function that writes an object
to a text file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: Object to be serialized and written to the file.
        filename (str): Name of the file to which the object should be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
