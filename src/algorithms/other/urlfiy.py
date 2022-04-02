"""
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
EXAMPLE
Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"
"""

def urlify(example: str, length: int) -> str:

    chars = []

    for i in range(length+1):
        if example[i] == ' ':
            chars.append('%20')
            continue
        chars.append(example[i])

    return "".join(chars)


print(urlify('Mr John Smith    ', 13))