#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Subtracting 1 for the script name itself
    arg_no = len(sys.argv) - 1
    total = 0

    if arg_no == 0:
        print("{}".format(arg_no))
    elif arg_no == 1:
        print("{}".format(int(sys.argv[1])))
    else:
        for index in range(1, arg_no + 1):
            total += int(sys.argv[index])
        print("{}".format(total))
