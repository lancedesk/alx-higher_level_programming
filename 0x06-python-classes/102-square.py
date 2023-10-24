#!/usr/bin/python3
"""Define a class Square that represents a square."""


class Square:
    """
    Square class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares are equal in size."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in size."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the current square is smaller in size than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if current square is smaller / equal in size to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the current square is greater in size than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if current square is greater or equal in size to the other."""
        return self.area() >= other.area()
