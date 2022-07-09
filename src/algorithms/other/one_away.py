"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def is_one_away(first: str, second: str) -> bool:
    if first == second:
        return True

    first_len = len(first)
    second_len = len(second)

    difference = abs(first_len - second_len)

    if difference > 1:
        return False

    merge = set(first + second)
    unique_count = len(merge)

    if not first_len == second_len and unique_count == max(first_len, second_len):
        return True

    if unique_count == first_len + 1:
        return True

    return False


print(is_one_away("pale", "ple"))
print(is_one_away("pales", "pale"))
print(is_one_away("pale", "bale"))
print(is_one_away("pale", "bake"))
print(is_one_away("pale", "baksaasasae"))
