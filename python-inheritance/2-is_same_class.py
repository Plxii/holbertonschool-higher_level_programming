#!/usr/bin/python3

"""
module 2-is_same_class contains the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    @obj: The object to check.
    @a_class: The class to compare the object against.
    """
    return type(obj) is a_class
