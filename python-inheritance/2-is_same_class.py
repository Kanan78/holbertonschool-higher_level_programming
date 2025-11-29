#!/usr/bin/python3
"""This module defines function is_same_class"""


def is_same_class(obj, a_class):
    """This function checks if object is exactly an instance of a_class"""
    return type(obj) is a_class
