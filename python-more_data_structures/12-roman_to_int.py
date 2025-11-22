#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str):
        return 0
    n1, n2 = roman_string[i],roman_string[i+1]
    s = 0
    i = 0
    while i < len(roman_string):
        if i == len(roman_string) - 1 or r[n1] >= r[n2]:
            s += r[n1]
            i += 1
        else:
            s += r[n2] - r[n1]
            i += 2
    return s
