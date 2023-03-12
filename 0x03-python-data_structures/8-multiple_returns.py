#!/usr/bin/python3
def multiple_returns(sentence):
    res = []
    a = len(tuple(sentence))
    res.append(a)
    if sentence[:] == "":
        return None
    else:
        first = sentence[0]
        res.append(first)
    return res
