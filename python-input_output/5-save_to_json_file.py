#!/usr/bin/python3
"""This module defines the function save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
