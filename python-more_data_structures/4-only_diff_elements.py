#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = set()
    for v in set_1:
        if not(v in set_2):
            c_set.add(v)
    return c_set
