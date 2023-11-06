#!/usr/bin/python3
"""
Module: 1-my_list
Contains the definition of the MyList class.
"""


class MyList(list):
    """
    Custom class inheriting from the list class with additional functionality.
    """

    def __init__(self):
        """
        Initializes a new instance of MyList.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
