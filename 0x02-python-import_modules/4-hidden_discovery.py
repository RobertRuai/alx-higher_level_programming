#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    lines = dir(hidden_4)
    for lines in hidden_4:
        if line[0:2] != "__":
            print(line)
