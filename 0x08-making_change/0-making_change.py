#!/usr/bin/python3
"""Contains the function makeChange
"""


def makeChange(coins, total):
    """Fewest number of denominations to make total
    """
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()

    count = 0
    for i in coins:
        if i <= total:
            count += total//i
            total %= i

    if total:
        return -1
    else:
        return count
