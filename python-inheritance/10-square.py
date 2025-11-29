#!/usr/bin/python3
"""This module defines the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
