#!/usr/bin/python3
import sys


if len(sys.argv) == 3:
    key = sys.argv[1]
    target = sys.argv[2]
    print(target.count(key))
else:
    print("none")
