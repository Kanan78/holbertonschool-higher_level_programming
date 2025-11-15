#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        if ord(str) < 65:
            print("{}".format(chr(ord(str)+32))
        else:
            print("{}".format(str))
