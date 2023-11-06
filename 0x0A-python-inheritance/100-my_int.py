#!/usr/bin/python3
"""
Module: 100-my_int
Defines a class MyInt that inherits from int and inverts == and != operators.
"""


class MyInt(int):
    """
    A class representing a rebellious integer.
    """
    def __eq__(self, other):
        """
        Checks if MyInt is not equal to other.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Checks if MyInt is equal to other.
        """
        return super().__eq__(other)
