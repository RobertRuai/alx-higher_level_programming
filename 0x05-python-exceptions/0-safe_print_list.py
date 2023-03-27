#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            my_list[i]
        except Exception as e:
            print(end='')
        else:
            count += 1
            print(my_list[i], end='')
    print()
    return count
