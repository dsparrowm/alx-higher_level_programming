#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            num = num + 1
    except IndexError:
        break
    return num
