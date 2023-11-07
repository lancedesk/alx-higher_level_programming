#!/usr/bin/python3
"""
Module to read a text file and print its content to stdout.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): Name of the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
