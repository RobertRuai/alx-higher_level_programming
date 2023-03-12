#!/usr/bin/python3
def multiple_returns(sentence):
    res = []
    a = len(tuple(sentence))
    first = sentence[0]
    if  not sentence:
        first = None
        res.append(0, first)
    else:
        res.append(a)
        res.append(first)
    return res
