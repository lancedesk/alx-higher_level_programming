#!/usr/bin/python3
"""
This module defines a Rectangle class with private width & height attributes.
"""


class Rectangle:
    """
    Represents a rectangle and provides methods to calculate its area,
    perimeter, & print its representation using '#'.
    It also provides a formal
    string representation of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle using '#'.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""

        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i < self.__height - 1:
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """
        Returns a formal string representation of the rectangle.

        Returns:
            str: Formal string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
