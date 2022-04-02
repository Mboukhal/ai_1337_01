#! /usr/bin/env python

kata = (2019, 9, 25, 3, 30)

if __name__ == '__main__':

    print(str(kata[1] if kata[1] >= 10 else '0' + str(kata[1])) + '/'
            + str(kata[2] if kata[2] >= 10 else '0' + str(kata[2])) + '/' 
            + str((4 - len(str(kata[0]))) * '0' + str(kata[0])) + ' '
            + str(kata[3] if kata[3] >= 10 else '0' + str(kata[3])) + ':'
            + str(kata[4] if kata[4] >= 10 else '0' + str(kata[4])))
