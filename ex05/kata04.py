#! /usr/bin/env python

kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == '__main__':

    if kata[0] < 10:
        print(f"module_0{kata[0]}, ", end='')
    else:
        print(f"module_{kata[0]}, ", end='')

    if kata[1] < 10:
        print(f"ex_0{kata[1]} : ", end='')
    else:
        print(f"ex_{kata[1]} : ", end='')
    
    print(f"{kata[2]:.2f}, ", end='')
    print(f"{kata[3]:.2e}, ", end='')
    print(f"{kata[4]:.2e}")