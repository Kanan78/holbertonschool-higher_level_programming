#!/usr/bin/python3
"""Module to serialize a Python dict to JSON and deserialize JSON to dict."""

import json


def serialize_and_save_to_file(data, filename):
    """This function serialize and save to file"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """This function load a file and deserialize it"""
    with open(filename, 'r') as f:
        return json.load(f)
