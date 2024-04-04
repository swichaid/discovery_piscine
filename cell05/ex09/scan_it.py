#!/usr/bin/python3
import sys

key = sys.argv[1]
target = sys.argv[2]
if len(sys.argv) == 3:
    print(target.count(key))
else:
    print("none")
