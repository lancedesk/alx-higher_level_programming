#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Subtracting 1 for the script name itself
    arg_no = len(sys.argv) - 1
    if arg_no == 0:
        print("{} arguments.".format(arg_no))
    elif arg_no == 1:
        print("{} argument:".format(arg_no))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(arg_no))
        for index in range(1, arg_no + 1):
            print("{}: {}".format(index, sys.argv[index]))
