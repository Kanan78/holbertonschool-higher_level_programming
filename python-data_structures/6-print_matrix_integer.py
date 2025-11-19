#!/usr/bin/python3
def print_matrix_integer(matrix):
    for row in matrix:
        for idx,element in enmurate(row):
            if idx == len(matrix) - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()
