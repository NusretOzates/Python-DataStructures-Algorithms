"""
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
"""
import collections


def is_permutation(first: str, second: str) -> bool:
    c1 = collections.Counter(first)
    c2 = collections.Counter(second)

    return c1 == c2
