#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    @obj: The object to check.
    @a_class: The class to compare the object against.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
