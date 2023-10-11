#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    new_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        # Create a new row to store squared elements
        new_row = []
        # Iterate through the elements in the row and square them
        for element in row:
            new_row.append(element ** 2)
        # Add the new squared row to the new matrix
        new_matrix.append(new_row)

    return (new_matrix)
