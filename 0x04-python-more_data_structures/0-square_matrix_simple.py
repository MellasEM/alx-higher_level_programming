#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new_row = []
        for num in row:
            num = num ** 2
            new_row.append(num)
        new.append(new_row)
    return new
