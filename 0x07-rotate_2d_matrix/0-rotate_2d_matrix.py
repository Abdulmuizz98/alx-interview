#!/usr/bin/python3
"""
Contains the function rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix
    """
    r = 0
    c = len(matrix) - 1
    temp = [i[:] for i in matrix]

    for row in temp:
        for col in row:
            matrix[r][c] = col
            r = r + 1
        r = 0
        c = c - 1
