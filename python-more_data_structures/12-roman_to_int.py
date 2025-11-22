#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if type(roman_string) != str or roman_string == None:
        return 0
    s = 0
    i = 0
    while i < len(roman_string):
        if i == len(roman_string) - 1 or r[roman_string[i]] >= r[roman_string[i+1]]:
            s += r[roman_string[i]]
            i += 1
        else:
            s += r[roman_string[i+1]] - r[roman_string[i]]
            i += 2
    return s
