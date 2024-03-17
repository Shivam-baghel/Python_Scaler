""" 
split the array
"""

from itertools import count
from typing import Counter


def isPossibeToSplit(nums: list):

    counter = Counter(nums)
    
    for value in counter.values():

        if value > 2:
            return False

    return True
