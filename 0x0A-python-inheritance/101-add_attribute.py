#!/usr/bin/python3
"""
contains a function
"""

def add_attribute(obj, attr_name_attr_value):
    """function that adds a new attribute to an object"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("Can't add new attribute")
    else:
        obj.__setattr__(attr_name, attr_value)
