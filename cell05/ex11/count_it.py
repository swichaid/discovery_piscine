#!/usr/bin/python3
import sys
param = sys.argv[1: ]
    
if len(sys.argv) <= 1:
        print("none")
else:
    print("parameters:", len(param))
    for i in param:
        print(f"{i}:", len(i))
