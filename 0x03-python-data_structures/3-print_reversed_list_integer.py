#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    arr_len = len(my_list) - 1
    new_arr = []
    while arr_len >= 0:
        print('{}'.format(my_list[arr_len]))
        arr_len -= 1
