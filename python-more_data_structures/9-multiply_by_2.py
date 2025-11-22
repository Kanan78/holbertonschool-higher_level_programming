#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i, v in a_dictionary.items():
        a_dictionary[i] = v*2
    return a_dictionary
