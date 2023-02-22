#!/usr/bin/python3
"""Contains the function makeChange
"""


def makeChange(coins, total):
    """Fewest number of denominations to make total
    """
    coins.sort()
    coins.reverse()# reverse

    count = 0
    for i in coins:
        if i <= total:
            count += total//i
            total %= i

    if total:
        return -1
    else:
        return count