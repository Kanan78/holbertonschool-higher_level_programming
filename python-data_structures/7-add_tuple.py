#!/usr/bin/python3
def add_tuple(tuple_a, tuple_b):
    m = []
    for i in range(0,len(tuple_a)):
        for j in range(0,len(tuple_b)):
            m[i] = tuple_a[i] + tuple_b[i]
    return tuple(m)
