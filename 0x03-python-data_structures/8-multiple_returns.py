#!/usr/bin/python3

def multiple_returns(sentence):
    if (sentence == ""):
        return (0, None)
    else:
        sentence_length = len(sentence)
        resulting_tuple = (sentence_length, sentence[0])
    
        return (resulting_tuple)
