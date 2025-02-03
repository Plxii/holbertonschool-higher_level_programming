#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of attributes and methods of the object.
    @obj: the object for which we want to obtain the attributes and methods.
    """
    return dir(obj)
