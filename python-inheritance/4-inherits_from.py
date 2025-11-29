#!/usr/bin/python3
"""This module defines the function inherits_from"""


def inherits_from(obj, a_class):
    """This function checks if the object is an instance of a subclass"""
    return (isinstance(obj, a_class)) and (type(obj) is not a_class)
