#!/usr/bin/python3
"""
Module to provide a function that creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): Name of the JSON file from which the object should be loaded.

    Returns:
        obj: Python data structure loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
