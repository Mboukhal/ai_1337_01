#! /usr/bin/env python

import sys

def user_man():
    print("""Usage: python operations.py <number1> <number2>\
    \nExample:\
        \n\tpython operations.py 10 3""")
    exit(1)


def operations(arg1: int, arg2: int):

    addition = arg1 + arg2
    print(f"Sum:        {addition}")
    difference = arg1 - arg2
    if difference < 0:
        difference *= -1
    print(f"Difference: {difference}")
    product = arg1 * arg2
    print(f"Product:    {product}")
    try:
        quotient = arg1 / arg2
    except ZeroDivisionError:
        quotient = "ERROR (div by zero)"
    print(f"Quotient:   {quotient}")
    try:
        remainder: int = arg1 % arg2
    except ZeroDivisionError:
        remainder = "ERROR (modulo by zero)"
    print(f"Remainder:  {remainder}")


if __name__ == '__main__':

    try:
        assert  len(sys.argv) >= 2
    except AssertionError:
        user_man()
    
    try:
        assert len(sys.argv) <= 3
    except AssertionError:
        print("InputError: too many arguments\n")
        user_man()
    
    try:
        int(sys.argv[1]) and int(sys.argv[2])
    except ValueError:
        print("InputError: only numbers\n")
        user_man()
    
    operations(int(sys.argv[1]), int(sys.argv[2]))
