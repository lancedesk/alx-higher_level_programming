#!/usr/bin/python3

def multiple_returns(sentence):
    if (len(sentence) == 0):
        return (None)
    else:
        sentence_length = len(sentence)
        resulting_tuple = (sentence_length, sentence[0])
    
        return (resulting_tuple)
