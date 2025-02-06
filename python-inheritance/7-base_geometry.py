#!/usr/bin/python3

"""
module 7-base_geometry contains the class BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry is a class that serves as a base
    for geometric shapes.
    It includes methods for validating parameters
    and raising exceptions.
    """
    def area(self):
        """
        Raises an Exception with the message
        'area() is not implemented'.
        This method is meant to be overridden in subclasses
        to calculate the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.
        @name: A string representing the name of the
        parameter being validated.
        @value: The value to be validated.
        Raises TypeError if value is not an integer.
        Raises ValueError if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
