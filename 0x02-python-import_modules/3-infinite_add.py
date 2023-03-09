#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1
    s = 0
    for i in range(ac):
        s = s + int(sys.argv[i + 1])
    print("{}".format(s))
