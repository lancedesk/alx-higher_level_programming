#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print("{}".format(""))
    else:
        for row in matrix:
            for column in row:
                print("{:d}".format(column), end=" ")
            print()
