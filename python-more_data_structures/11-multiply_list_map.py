#!/usr/bin/python3
def multiply_list_map(my_list, number):
    my_list = list(map(lambda x: x*number, my_list))
    return my_list
