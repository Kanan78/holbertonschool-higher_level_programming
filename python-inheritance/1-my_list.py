#!/usr/bin/python3
"""This module defines a class MyList"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
