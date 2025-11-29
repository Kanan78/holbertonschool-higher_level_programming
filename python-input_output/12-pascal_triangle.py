#!/usr/bin/python3
"""This module defines the function pascal_triangle"""


def pascal_triangle(n):
    """It returns a 2D list for Pascal's triangle of n."""
    a = [[1], [1, 1]]

    for i in range(2, n):
        p = a[i-1]
        r = [1]
        for j in range(len(p)-1):
            r.append(p[j] + p[j+1])
        r.append(1)
        a.append(r)
    return a
