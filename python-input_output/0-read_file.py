#!/usr/bin/python3
"""This module defines the function read_file"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout"""
    with open(filename, 'r') as f:
        t = f.read()
        print(t, end='')
