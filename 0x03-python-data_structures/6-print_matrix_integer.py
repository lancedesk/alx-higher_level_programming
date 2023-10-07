#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print("")  # Print an empty line if matrix is empty or has empty rows
    else:
        for row in matrix:
            for index, column in enumerate(row):
                print("{:d}".format(column), end="")
                if index != len(row) - 1:
                    print(" ", end="")  # Add space between numbers in same row
            print("")  # Move to the next line for the next row
