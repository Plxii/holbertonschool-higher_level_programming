#!/usr/bin/python3

"""
module 8-rectangle contains the class Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a class that represents a rectangle.
    It inherits properties from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new rectangle with a width and a height.
        @width: The width of the rectangle.
        @height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
