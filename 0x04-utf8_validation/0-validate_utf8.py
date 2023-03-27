#!/usr/bin/python3
"""
Contains the function validUTF8 which validates utf8 data
"""


def validUTF8(data):
    """Returns true if data is valid utf-8 data
    """
    return max(data) < 256 and min(data) > -1
