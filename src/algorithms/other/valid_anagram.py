"""

given s1 and s2.
If both of them made of same chars with same frequencies
they are anagrams

Time and Space O(n)
"""

from collections import Counter


def is_anagram(s1: str, s2: str):
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


print(is_anagram("nameless", "salesmen"))
