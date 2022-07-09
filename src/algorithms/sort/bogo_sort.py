"""
Is this algorithm a joke?
"""
import random
from typing import List
from utils import is_sorted


def bogo_sort(elements: List[int]) -> List[int]:

    while not is_sorted(elements):
        random.shuffle(elements)
    return elements
