#!/usr/bin/python3
"""
Module to write a string to a text file (UTF8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    and return the number of characters written.

    Args:
        filename (str): Name of the file to be written.
        text (str): String to be written to the file.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written
