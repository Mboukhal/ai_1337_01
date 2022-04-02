#! /usr/bin/env python

import sys

if __name__ == "__main__" :
    
    try:
        assert len(sys.argv) >= 2
    except AssertionError:
        exit()
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit()
    try:
        assert sys.argv[1].isnumeric(), "argument is not integer"
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        exit()

    num = int(sys.argv[1])

    if num == 0:
        print("I’m Zero.")
    elif (num % 2) == 0:
        print("I’m Even.")
    else:
        print("I’m Odd.")

