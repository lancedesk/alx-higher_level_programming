#!/usr/bin/python3
"""
Script to add command line arguments to a Python
list and save it to a JSON file.
"""
import sys
import json
from os.path import exists


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: Object to be serialized and written to the file.
        filename (str): Name of the file to which the object should be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): Name of the JSON file
        from which the object should be loaded.

    Returns:
        obj: Python data structure loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


filename = "add_item.json"

# Check if the file exists, if not, create an empty list
if not exists(filename):
    save_to_json_file([], filename)

# Load the existing list from the file
my_list = load_from_json_file(filename)

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
