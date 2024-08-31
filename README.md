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
