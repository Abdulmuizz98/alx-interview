#!/usr/bin/python3
"""
Contains the function 'pascal_triangle'
"""


def pascal_triangle(n):
    res = []
    if n <= 0:
        return res
    for i in range(1, n+1):
        if i == 1:
            res.append([1])
        elif i == 2:
            res.append([1, 1])
        else:
            last = res[len(res) - 1]
            # print(last)
            seq = [1] + [last[i] + last[i+1]for i in range(
                len(last) - 1)] + [1]
            res.append(seq)
    return res
