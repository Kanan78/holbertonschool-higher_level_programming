#!/usr/bin/python3
"""This module defines function is_same_class"""


def is_same_class(obj, a_class):
    """This function checks an existence of the object in the class"""

    if isinstance(obj, a_class):
        return True
    return False
