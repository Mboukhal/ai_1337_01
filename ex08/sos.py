#!/usr/bin/env python

from sys import argv, exit

letters = { 'A': '.-',     'B': '-...',   'C': '-.-.', 
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.' 
        }

if __name__ == '__main__':

    if len(argv) == 1 : exit()

    msg = ' '.join(argv[1:])
    if '/' in msg:
        print('ERROR')
        exit()
    msg = msg.upper()

    string = ''

    for char in msg:
        if char != ' ':
            string += str(letters[char]) + ' '
        else:
            string += '/ '
    string = string[:-1]
    
    print(string)