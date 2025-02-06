#!/usr/bin/python3

"""
module 0-lookup contains the function lookup.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the object.
    @obj: the object for which we want to obtain the attributes and methods.
    """
    return dir(obj)
