#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except BaseException as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
