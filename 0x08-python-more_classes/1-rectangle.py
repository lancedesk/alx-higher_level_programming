#!/usr/bin/python3
"""
This module defines a Rectangle class with private width & height attributes.
"""


class Rectangle:
    """
    Rectangle class with private width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        # Set the private width attribute to the given width
        self.width = width
        # Set the private height attribute to the given height
        self.height = height

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        # Check if the input value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # Check if the input value is non-negative
        if value < 0:
            raise ValueError("width must be >= 0")
        # Set the private width attribute to the input value
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        # Check if the input value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Check if the input value is non-negative
        if value < 0:
            raise ValueError("height must be >= 0")
        # Set the private height attribute to the input value
        self.__height = value
