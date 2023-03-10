#!/usr/bin/python3
"""
Contains the function "isWinner"
"""


def isWinner(x, nums):
    """
    Example:
        - x = 3, nums = [4, 5, 1]

    First round: 4
        - Maria picks 2 and removes 2, 4, leaving 1, 3
        - Ben picks 3 and removes 3, leaving 1
        - Ben wins because there are no prime numbers left for Maria to choose

    Second round: 5

        - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
        - Ben picks 3 and removes 3, leaving 1, 5
        - Maria picks 5 and removes 5, leaving 1
        - Maria wins because there are no prime numbers left for Ben to choose

    Third round: 1

        - Ben wins because there are no prime numbers for Maria to choose
    """
    if x <= 0:
        return None
    m, b = 0, 0
    nums = nums[0:x]  # accomodate only playable rounds
    hash = [i for i in range(1, max(nums) + 1) if isPrime(i)]

    for num in nums:
        prime_num = [i for i in hash if i <= num]
        # print(prime_num)
        if (len(prime_num) % 2) == 0:
            b += 1
        else:
            m += 1
    if b > m:
        return 'Ben'
    elif m > b:
        return 'Maria'
    else:
        return None


def isPrime(num):
    """ Returns True if a number is prime otherwise False
    """
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True
