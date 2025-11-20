#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix += map(lambda k: k**2, i))
    return list(new_matrix)
