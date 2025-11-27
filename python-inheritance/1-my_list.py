#!/usr/bin/python3
"""This module defines a class MyList"""


class MyList(list):
    """This class inherits from the built-in list class"""

    def print_sorted(self):
        print(sorted(self))
