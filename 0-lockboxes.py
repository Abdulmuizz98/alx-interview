#!/usr/bin/python3
"""Script that contains the function canUnlockAll """


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    keys = [] + boxes[0]  # we have boxesay 0 keys cos its already unlocked
    boxes[0] = 'unlocked'

    while len(keys) != 0:
        key = keys.pop()
        if boxes[key] != 'unlocked':
            keys += boxes[key]
            boxes[key] = 'unlocked'

    for i in boxes:
        if i != 'unlocked':
            return False
    return True
