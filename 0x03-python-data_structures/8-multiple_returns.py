#!/usr/bin/python3

def multiple_returns(sentence):
    if (sentence == ""):
        return (0, None)
    else:
        sentence_length = len(sentence)
        return ((sentence_length, sentence[0]))
