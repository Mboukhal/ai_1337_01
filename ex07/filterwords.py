#! /usr/bin/env python

import sys

if __name__ == '__main__':

    try:
        assert len(sys.argv) == 3 and sys.argv[1].isalpha() \
            and sys.argv[2].isdigit(), "ERROR"
    except AssertionError as msg:
        print(msg)
        exit()
    
    S = str(sys.argv[1]).split(' ')
    N = int(sys.argv[2])
    tmp = []
    for i in S:
        if len(i) > N:
            tmp.append(i.replace(',', ''))
    print(tmp)