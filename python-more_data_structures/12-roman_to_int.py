#!/usr/bin/python3
def roman_to_int(roman_string):
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str):
        return 0
    s = 0
    le = len(roman_string)
    for i in range(le):
        if i+1 < le and r[roman_string[i+1]] > r[roman_string[i]]:
            s -= r[roman_string[i]]
        else:
            s += r[roman_string[i]]
    return s
