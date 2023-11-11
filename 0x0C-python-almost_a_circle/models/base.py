#!/usr/bin/python3
"""Module containing the Base class for managing id attribute."""


class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id (int): If provided, assigns the public instance attribute id
                      with this value.
                      If not provided, increments __nb_objects and assigns
                      the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
