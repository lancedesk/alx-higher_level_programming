#!/usr/bin/python3
"""
This module defines a Rectangle class with private width & height attributes.
"""


#!/usr/bin/python3

class Rectangle:
    # Class variables to keep track of number of instances & print symbol
    number_of_instances = 0
    print_symbol = "#"

    # Constructor to initialize object with width & height attributes
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # Getter and setter methods for the width attribute
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_dimension(value, "width")
        self.__width = value

    # Getter and setter methods for the height attribute
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_dimension(value, "height")
        self.__height = value

    # Method to validate if the dimension is a positive integer
    def validate_dimension(self, value, dimension):
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    # Method to calculate the area of the rectangle
    def area(self):
        return self.__width * self.__height

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.__width + self.__height)

    # Method to represent the rectangle as a string of print symbols
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(Rectangle.print_symbol) * self.__width for _ in range(self.__height)])

    # Method to provide a formal string representation of the rectangle
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # Destructor method to print a farewell message when an instance is deleted
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # Static method to compare two rectangles and return the one with a larger area
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
