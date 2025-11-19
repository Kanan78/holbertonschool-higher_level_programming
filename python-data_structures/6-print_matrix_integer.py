#!/usr/bin/python3
def print_matrix_integer(matrix):
    for row in matrix:
        for idx,element in enemurate(row):
            if idx == len(matrix) - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print()
