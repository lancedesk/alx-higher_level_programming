#!/usr/bin/python3
"""Module containing the Square class, a subclass of Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): ID of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square."""
        d = self.id
        x = self.x
        y = self.y
        size = self.width  # width and height are the same for a square
        return "[Square] ({}) {}/{} - {}".format(d, x, y, size)
