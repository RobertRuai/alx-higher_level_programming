#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        is_dgt = True
        print("{:d}".format(value))
    except Exception as e:
        is_dgt = False
        print(f"Exception: {e}", file=sys.stderr)
    return is_dgt
