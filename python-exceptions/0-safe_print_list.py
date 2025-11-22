#!/usr/bin/python3
def safe_print_list(my_list, x):
    try:
        k = 0
        for i in range(x):
            print(my_list[i], end='')
            k += 1
    except IndexError:
        pass
    print()
    return k
