#!/usr/bin/python3
"""This module defines the class CustomObject"""

import pickle


class CustomObject:
    """A class representing a person with name, age, and student status."""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for i, v in (self.__dict__).items():
            a = f"{i}: {v}"
            print(a.capitalize())

    def serialize(self, filename):
        with open(filename, 'r') as f:
            pickle.dump(self.__dict__, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'r') as f:
            return pickle.load(f)
