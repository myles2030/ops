#!/usr/bin/python3

def binaryfunc():
    print("input binary number: ")

    wow = str(input())
    
    num = 0

    for i,digit in enumerate(wow):
        num +=int(digit)*pow(2,len(wow) - 1 - i)


    valoct = format(num, 'o')
    valhex = format(num, 'x')

    print("OCT> ",valoct)
    print("DEC> ",num)
    print("HEX> ",valhex)
