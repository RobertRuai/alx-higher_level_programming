#!/usr/bin/python3
def multiple_returns(sentence):
    res = []
    a = len(sentence)
    first = sentence[0]
    if not sentence:
        return (0, "None")
    else:
        res.append(a)
        res.append(first)
    return res
