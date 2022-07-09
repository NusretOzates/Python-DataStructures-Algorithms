"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""
import collections


def p_of_palindrome(example: str):

    example = example.lower()
    counter = collections.Counter(example)
    length = len(example)

    if length % 2 == 0:
        even_count = map(lambda x: x % 2 == 0, counter.values())
        return all(even_count)

    odds = list(filter(lambda x: x % 2 != 0, counter.values()))
    return len(odds) == 1


print(p_of_palindrome("abba"))
