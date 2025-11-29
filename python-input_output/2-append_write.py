#!/usr/bin/python3
"""This module defines the function append_write"""


def append_write(filename, text):
    """This function appends a string at the end of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
