# XKCD Roll
Simple terminal diceware to generate high-entropy passwords. The application
was inspired by [xkcd 936](https://xkcd.com/936/).

![xkcd 936](images/password_strength.png "xkcd 936")

## How it Works?
Simple! You choose the number of words you want in the final genrated phrase,
and the application will roll a die 5 times for each word. This will produce a
sequence of 5 numbers from 1-6 (ex. 12345). Then the app will parse through a
large list of words (7775 words), and match the number to a word in the
dictionary.

```
...
12344	around
12345	arousal <-
12346	arrange
...
```

## Commandline Arguments
```
-h, --help            show this help message and exit
-s STRATEGY, --strategy STRATEGY
                      capitalize strategy for generated words ('lower', 'upper', 'alternating_words', 'alternating_chars') (default 'lower')
-d DELIMITER, --delimiter DELIMITER
                      delimiter symbol to be used between words (default ' ')
-i, --interactive     interactive mode
-n NUM_WORDS, --number NUM_WORDS
                      number of words to be generated (default 3)
```

## EFF Word List
The application uses the Electronic Frontier Foundation's long list of words.
It can be found [here](https://www.eff.org/dice).

## How Entropy is Calculated?
Shannon's entropy is a common mathematical notation in Information Theory which
describes a measure of disorder or randomness. The highest the score is in
bits the more disordered or random a thing is, and the harder it is to be
recreated or reassembled.

$\log_2(P^L)$

Where P is the pool of possible symbols/words, and L is the number of words in
the phrase.

## What is the Recommended Entropy Score?
As computers get faster and faster, passwords can also get cracked faster. The
recommended entropy score for a password as of this writing should be above
70bits.

## How to Run the Code
1. Make sure you have python3 and pip
2. Install dependencies by running the following
```bash
$ pip install -r requirements.txt
```
3. Either run the program directly as a python script
```bash
$ python3 xkcdroll
```
4. Or copy the executable `xkcdroll` command somewhere in your `$PATH`
```bash
$ cp ./xkcdroll /usr/bin
$ xkcdroll -h
```
