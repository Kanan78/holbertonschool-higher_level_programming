#!/usr/bin/python3
"""This module defines the class BaseGeometry"""


class BaseGeometry:
    """This class defines basic geometry formulas"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """This class defines a Rectangle"""
    def __init__(self, width, height):
        if integer_validator(width, self.width):
            if integer_validator(height, self.height):
                self.__width = width
                self.__height = height
