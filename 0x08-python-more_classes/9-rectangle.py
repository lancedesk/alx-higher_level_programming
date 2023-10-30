#!/usr/bin/python3
"""
This module defines a Rectangle class with private width & height attributes.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        instance_no (int): The number of instances of Rectangle created.
        hash_symbol (str): symbol used for string
        representation of the rectangle.
    """

    instance_no = 0  # Number of instances created
    hash_symbol = "#"  # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        type(self).instance_no += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width attribute."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare two rectangles
        and return the larger one based on area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either rect_1 or
            rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The larger rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """Class method to create a square rectangle.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A square rectangle with equal width and height.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        r = []
        for i in range(self.__height):
            [r.append(str(self.hash_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Print a farewell msg on Rectangle instance deletion"""
        type(self).instance_no -= 1
        print("Bye rectangle...")
