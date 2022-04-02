#! /usr/bin/env python

kata = "The right format"

if __name__ == '__main__':

    space = (42 - len(kata)) * '-'
    print(f"{space}{kata}", end='')
