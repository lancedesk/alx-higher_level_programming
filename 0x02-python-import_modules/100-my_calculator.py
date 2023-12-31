#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    arg_no = len(sys.argv)
    program_name = sys.argv[0]

    if arg_no != 4:
        print("Usage: {} <a> <operator> <b>".format(program_name))
        sys.exit(1)
    else:
        operator = sys.argv[2][0]
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if operator == '+':
            print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))
        elif operator == '-':
            print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
