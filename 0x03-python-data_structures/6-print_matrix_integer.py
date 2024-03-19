#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(" ".join("{:d}".format(n) for n in i))
        """
        for j in range(len(i)):
            if j == len(i) - 1:
                print("{}".format(i[j]), end="")
            else:
                print("{} ".format(i[j]), end="")
        print()
        """
