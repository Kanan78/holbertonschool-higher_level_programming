#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:  # 'a'–'z' aralığı
            result += chr(ord(i) - 32)
        else:
            result += i
    print("{}".format(result), end="")
