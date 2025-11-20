#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for i in matrix:
        new_matrix += list(map(lambda k: k**2, i))
    return list(new_matrix)
