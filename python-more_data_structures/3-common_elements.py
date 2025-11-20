#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = {}
    for v in set_1:
        if v in set_2:
            c_set.add(v)
