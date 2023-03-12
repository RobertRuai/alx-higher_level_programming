#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, "None")
    a = len(sentence)
    first = sentence[0]
    return (a, first)
