#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1
    if ac == 1:
        print("1 argument:")
        print("{}: {}".format(ac, sys.argv[1]))
    elif ac == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(ac))
    if ac > 1:
        for i in range(ac):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
