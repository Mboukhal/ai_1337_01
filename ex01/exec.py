#! /usr/bin/env python

import sys

if __name__ == "__main__":
    
    tmp = []
    for i in sys.argv:
        tmp.append(i)
    print(' '.join(tmp[1:]))
