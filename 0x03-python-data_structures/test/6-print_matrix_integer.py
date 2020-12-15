#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 0
        for j in i:
            print("{:d}".format(j), end="")
            if count != (len(i) - 1):
                print("{}",.format(" "), end="")
            count += 1
        print()
