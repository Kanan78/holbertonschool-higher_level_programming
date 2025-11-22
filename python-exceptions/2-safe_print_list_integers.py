#!/usr/bin/python3
def safe_print_list(my_list, x):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
    except TypeError:
            pass
    return x
    
