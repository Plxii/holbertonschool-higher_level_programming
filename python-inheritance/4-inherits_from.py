#!/usr/bin/python3

"""
module 4-inherits_from contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    @obj: The object to check.
    @a_class: The class to compare the object against.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
