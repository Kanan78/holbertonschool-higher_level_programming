#!/usr/bin/python3
def safe_print_list(my_list, x):
    try:
        k = 0
        for i in range(x):
            k += 1
            print(my_list[i], end='')
    except IndexError:
        pass
    return k
