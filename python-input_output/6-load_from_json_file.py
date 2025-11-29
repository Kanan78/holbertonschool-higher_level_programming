#!/usr/bin/python3
"""This module defines the function load_from_json_file"""

import json


def save_to_json_file(filename):
    """This function writes an object to a text file"""
    with open(filename, 'r') as f:
        json.load(f)
