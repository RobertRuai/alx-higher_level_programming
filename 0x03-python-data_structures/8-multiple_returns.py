#!/usr/bin/python3
def multiple_returns(sentence):
    res = []
    a = len(tuple(sentence))
    res.append(a)
    first = sentence[0]
    if sentence[:] == "":
        first = None
        res.append(first)
    else:
        res.append(first)
    return res
