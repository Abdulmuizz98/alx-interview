#!/usr/bin/python3
''' This module contains the function minOperations '''

import math


def minOperations(n):
    """ Given a number n, write a method that
        calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    """
    return sum(primeFactors(n))


# A function to print all prime factors of
# a given number n
def primeFactors(n):

    cache = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        cache += [2]
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):
        # while i divides n, print i ad divide n
        while n % i == 0:
            cache += [i]
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        cache += [n]
    return cache
