#!/usr/bin/env python3
"""
XKCD Roll
"""
import argparse
import json
from random import SystemRandom

cryptogen = SystemRandom()


def parse_arguments():
    """
    Function to parse command line arguments

    :returns: argument dictionary
    """
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-n", "--number",
                        default=3,
                        dest="num_words",
                        help="number of words to be generated",
                        type=int
                        )
    parser.add_argument("-m", "--min-length",
                        default=3,
                        dest="min_length",
                        help="minimum length of word",
                        type=int
                        )
    parser.add_argument("-d", "--delimiter",
                        default="|",
                        dest="delimiter",
                        help="delimiter symbol to be used between words",
                        type=str
                        )
    args = parser.parse_args()
    return args


def load_dictionary():
    """
    Function to load english dictionary

    :returns: dicationary of english words as an array
    """
    with open("dictionary.json", "r", encoding="utf-8") as _file:
        words = _file.read()
    dct = json.loads(words)
    return dct


def roll(dct, rng, length):
    """
    Roll dice

    :returns: random word
    """
    while True:
        idx = cryptogen.randrange(rng) + 1
        word = dct[idx].lower()
        if len(word) >= length:
            break
    return word


def generate_phrase(num, length, delim, dct, dct_length):
    """
    Function to generate random phrase

    :num: number of words to generate
    :length: minimum length of each word
    :delim: delimiter between words
    :dct: dictionary
    :dct_length: dictionary length

    :returns: random phrase
    """
    random_phrase = ""
    for i in range(num):
        word = roll(dct, dct_length, length)
        random_phrase += word
        if i < num_words - 1:
            random_phrase += delim
    return random_phrase


if __name__ == "__main__":
    arguments = parse_arguments()
    dictionary = load_dictionary()
    dict_length = len(dictionary)

    num_words = arguments.num_words
    min_length = arguments.min_length
    delimiter = arguments.delimiter

    phrase = generate_phrase(num_words,
                             min_length,
                             delimiter,
                             dictionary,
                             dict_length)
    print(phrase)
