#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numarg = len(sys.argv) - 1
    if (numarg == 0):
        print("0 arguments.")
    elif (numarg == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(numarg))
    for i in range(numarg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
