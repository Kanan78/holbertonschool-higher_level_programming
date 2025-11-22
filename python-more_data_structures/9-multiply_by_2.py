#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    for i, v in new_d.items():
        new_d[i] = v*2
    return new_d
