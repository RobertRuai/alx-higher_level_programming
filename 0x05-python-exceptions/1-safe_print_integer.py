#!/usr/bin/python3
def safe_print_integer(value):
    try:
        is_dgt = True
        print("{:d}".format(value))
    except Exception as e:
        is_dgt = False
    return is_dgt
