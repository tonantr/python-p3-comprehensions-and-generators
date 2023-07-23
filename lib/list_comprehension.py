#!/usr/bin/env python3

def return_evens(num_list):
    # no_evens = []
    # evens_odds = [i if i % 2 == 0 else no_evens for i in num_list]
    evens = [i for i in num_list if i % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    sentence = [f'{i}!' for i in sentence_list]
    return sentence
