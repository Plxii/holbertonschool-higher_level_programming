#!/usr/bin/python3

"""
module 6-base_geometry contains the class BaseGeometry.
"""


class BaseGeometry:
    """A base class for geometry-related operations.
    """
    def area(self):
        """Public instance method that raises an Exception.
        This method is intended to be overridden in subclasses.
        When called, it raises an Exception with the message
        'area() is not implemented' to indicate that the method
        has not been implemented in this base class.
        @self: The current instance of BaseGeometry, allowing access
        to its attributes and methods.
        """
        raise Exception('area() is not implemented')
