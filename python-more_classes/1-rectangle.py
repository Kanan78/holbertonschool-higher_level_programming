#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """This class defines a rectangle by: (based on 0-rectangle.py)"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = width

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
