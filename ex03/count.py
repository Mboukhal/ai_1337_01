#! /usr/bin/env python

import string

def text_analyzer(*text):
    """This function counts the number of upper characters, lower characters,
    \npunctuation and spaces in a given text."""
    if len(text) > 1:
        print("Error")
        exit()
    if len(text[0]) == 0:
        print("What is the text to analyse?\n>>", end=' ')
        text = input()

    upper = 0
    lower = 0
    pm = 0
    total = 0
    char_spaces = 0

    for x in text:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        elif x in string.punctuation:
            pm += 1
        elif x.isspace():
            char_spaces += 1
        total += 1
    print(f"The text contains {total} characters:")
    print(f"- {upper} upper letters")
    print(f"- {lower} lower letters")
    print(f"- {pm} punctuation marks")
    print(f"- {char_spaces} spaces")
