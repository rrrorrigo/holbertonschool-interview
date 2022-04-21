#!/usr/bin/python3
"""LOCKBOXES"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened"""
    keys = set(boxes[0])
    check = set([])
    if len(keys) <= 0:
        return(False)
    for i in range(0, len(boxes)):
        if i in keys:
            keys.update(boxes[i])
    for i in range(0, len(boxes)):
        if i in keys:
            keys.update(boxes[i])
    for i in range(0, len(boxes)):
        check.add(i)
    if 0 in keys:
        keys.remove(0)
    if 0 in check:
        check.remove(0)
    if keys == check:
        return True
    else:
        return False
