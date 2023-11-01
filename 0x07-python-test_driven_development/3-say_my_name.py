#!/usr/bin/python3
"""
This module provides a function to print a formatted name in the pattern "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the formatted name "My name is <first_name> <last_name>"

    Args:
        first_name (str): First name to be included in the formatted string.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    # Check if first_name is a string, raise TypeError if not
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string, raise TypeError if not
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Format and print the name
    formatted_name = "My name is {} {}".format(first_name, last_name)
    print(formatted_name)
