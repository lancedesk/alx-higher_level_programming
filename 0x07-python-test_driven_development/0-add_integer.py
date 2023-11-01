#!/usr/bin/python3
"""
This module provides a function to add two integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
