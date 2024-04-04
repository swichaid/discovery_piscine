#!/usr/bin/python3
import sys
def main():
    i = len(sys.argv)
    if len(sys.argv) > 2:
        while i > 1:
            print((sys.argv[i-1]))
            i -= 1
    else:
        print("none")
main()
