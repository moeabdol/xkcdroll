#!/usr/bin/env python3
"""
XKCD Roll
"""
import argparse


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
    :returns: dicationary of english words as dict
    """
    with open("dictionary.txt", "r", encoding="utf-8") as _file:
        dct = _file.read()
    return dct

def roll():
    """
    Roll dice
    :returns: random word

    """
    pass

if __name__ == "__main__":
    arguments = parse_arguments()
    dictionary = load_dictionary()

    num_words = arguments.num_words
    min_length = arguments.min_length
    delimiter = arguments.delimiter
