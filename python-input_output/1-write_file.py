#!/usr/bin/python3
"""This module defines the function write_file"""


def write_file(filename, text):
    """This function writes the text to the file"""
    with (filename, 'w') as f:
        return f.write(text)
