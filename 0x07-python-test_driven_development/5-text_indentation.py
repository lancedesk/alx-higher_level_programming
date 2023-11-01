#!/usr/bin/python3
"""
This module provides a function to format text by adding 2 new lines after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':' character.

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    message = "text must be a string"
    if not isinstance(text, str):
        raise TypeError(message)

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")

        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1

            while c < len(text) and text[c] == ' ':
                c += 1

            continue
        c += 1
