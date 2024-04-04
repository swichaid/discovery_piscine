#!/usr/bin/python3
import sys

if len(sys.argv) == 2:   
    Hello = sys.argv[1]
    if Hello == input("What was the parameter is?: "):
        print("Good job!")
    else:
        print("Nope, sorry...")

else:
    print("none")
