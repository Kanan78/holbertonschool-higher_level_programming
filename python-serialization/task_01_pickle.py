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
        for i, v in self.__dict__.items():
            a = f"{i}: {v}"
            print(a.capitalize())

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self.__dict__, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            return cls(**data)
        except FileNotFoundError:
            return None
