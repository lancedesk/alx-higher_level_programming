#!/usr/bin/python3
"""
Module for appending a line of text after each line
containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    Args:
        filename (str): Name of the file to be modified.
        search_string (str): The specific string to search for in each line.
        new_string (str): The line of text to be inserted after lines
        containing the search string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
