#!/usr/bin/python3
"""This module defines the class Student"""


class Student:
    """This class defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        result = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result
        return self.__dict__
