#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        res = (0, None)
        return res
    else:
        res = (length, sentence[0:1])
        return res
