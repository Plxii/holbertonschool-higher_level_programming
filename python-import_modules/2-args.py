#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numarg = len(sys.argv) - 1
    if (numarg >= 1):
        print("{} argument: ".format(numarg))
    else:
        print("{} arguments.".format(numarg))
    for i in range(numarg, len(sys.argv)):
        print("{}: {}".format({sys.argv}))
