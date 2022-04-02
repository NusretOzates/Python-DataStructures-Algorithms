"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
import collections


def is_unique_ds(example: str) -> bool:
    count = 0
    chars = set()

    for c in example:
        chars.add(c)
        count += 1

    return len(chars) == count


def is_unique_ds_2(example: str) -> bool:
    chars = collections.Counter()

    for c in example:
        chars[c] += 1

    return chars.most_common(1)[0][1] == 1


def is_unique(example: str) -> bool:
    for i in range(len(example) - 1):
        for j in range(i + 1, len(example)):
            if example[i] == example[j]:
                return False

    return True


def is_unique_2(example: str) -> bool:
    char_list = [0] * 128

    for c in example:
        c_as_int = ord(c)
        if char_list[c_as_int] != 0:
            return False
        char_list[c_as_int] = 1

    return True


print(is_unique('abc'))
print(is_unique('abb'))
print(is_unique('aba'))
print()
print(is_unique_2('abc'))
print(is_unique_2('abb'))
print(is_unique_2('aba'))
print()
print(is_unique_ds('aba'))
print(is_unique_ds('abb'))
print(is_unique_ds('abc'))
print()
print(is_unique_ds_2('aba'))
print(is_unique_ds_2('abb'))
print(is_unique_ds_2('abc'))
