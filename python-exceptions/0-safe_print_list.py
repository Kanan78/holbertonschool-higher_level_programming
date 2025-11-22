#!/usr/bin/python3
def safe_print_list(my_list, x):
    try:
        for i in range(x):
            print(my_list[i], end='')
        print(f"\n{x}")
    except IndexError:
        k = 0
        for i in my_list:
            print(i,end='')
            k += 1 
        print(f"\n{x}")

