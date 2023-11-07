#!/usr/bin/python3
"""
Module to append a string to a text file (UTF8)
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF8)
    and return the number of characters added.

    Args:
        filename (str): Name of the file
        to which the text should be appended.
        text (str): String to be appended to the file.

    Returns:
        int: Number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
