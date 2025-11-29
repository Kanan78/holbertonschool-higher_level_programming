#!/usr/bin/python3
"""This module defines the function class_to_json"""

import json


def class_to_json(obj):
    """This function defines the dictionary description"""
    return obj.__dict__
