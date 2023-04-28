#!/usr/bin/python3
"""Defines a function that checks if a box containing a list and if the list
   of lists can be opened using keys stored in the lists.
"""


def canUnlockAll(boxes):
    """Checks the boxes and determine the possibility of unlocking the boxes"""
   positionBox = 0
    unlockedBox = {}

    for box in boxes:
        if len(box) == 0 or positionBox == 0:
            unlockedBox[positionBox] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != positionBox:
                unlockedBox[key] = key
        if len(unlockedBox) == len(boxes):
            return True
        positionBox += 1
    return False
