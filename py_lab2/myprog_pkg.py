#!/usr/bin/python3

import sys
from my_pkg.binary import*
from my_pkg.union import*

print("Select menu: 1) conversion 2) union/intersection 3) exit?")

a = int(input())

if a == 1:
    binaryfunc()
if a == 2:
    listfunc()
if a == 3:
    print("exit the program....")
    sys.exit()
