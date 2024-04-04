#!/usr/bin/python3
import sys
param = sys.argv[1:]
    
if not param:
        print("none")
else:
    print("parameters:", len(param))
    for i in param:
        print(i, len(i))
