"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def compress(example: str) -> str:
    count = 0
    previous = ""
    result = []

    for letter in example:

        if previous and letter != previous:
            result.append(f"{previous}{count}")
            count = 1
            previous = letter
            continue

        previous = letter
        count += 1

    result.append(f"{previous}{count}")
    result = "".join(result)

    if len(result) >= len(example):
        return example
    return result


print(compress("aabcccc"))
