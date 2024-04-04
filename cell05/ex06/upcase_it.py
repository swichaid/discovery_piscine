#!/usr/bin/python3
import sys 

if len(sys.argv) == 2:
    wrd1 = sys.argv[1]
    print(wrd1.upper())
elif len(sys.argv) !=2:
    wrd = len(sys.argv)
    print('none')
