#! /usr/bin/env python

from time import sleep
from datetime import datetime

def ft_progress(lst):

    max_val = max(lst)
    counter = 0
    now = datetime.now()
    time_to = 0
    time_for_one = 0

    for x in lst:

        if counter == 1:
            time_for_one = float(((str(datetime.now() - now)).split(':'))[-1])
            time_to += time_for_one
        time_to += time_for_one
        counter += 1

        per = int((x * 100)/max_val)
        run = per
        per = ((3 - len(str(per))) *  ' ') + str(per)
        x_val = str(x)
        x_val = ((len(str(max_val)) - len(x_val) - 1) * ' ') + x_val
        cursore = ((run) * '=') + '>' + ((100 - run) * ' ')
        progress = ((len(str(max_val)) - len(x_val)) * ' ') + x_val + ' / ' + str(max_val)
        
        print(f"\rETA:  [{per}%] [{cursore}] {progress} elapsed time {time_to:.2f}s\t\t", end='\r')
        yield x
    print("\n...", end='')
