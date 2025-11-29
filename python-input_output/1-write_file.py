#!/usr/bin/python3
"""This module defines the function write_file"""


def write_file(filename, text):
    """This function writes the text to the file"""
    with open(filename, 'w') as f:
        return f.write(text)
