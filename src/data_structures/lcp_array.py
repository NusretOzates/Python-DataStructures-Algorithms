"""
Longest common string array
"""

from src.data_structures.suffix_array import SuffixArray


class LCP:

    def __init__(self, value: str):

        suffix_array = SuffixArray(value)
        suffixes = [value[i:] for i in range(len(value))]
        sorted_suffix = [suffixes[suffix] for suffix in suffix_array.suffix_array]
        lcp = [0]
        for first, second in zip(sorted_suffix[:-1], sorted_suffix[1:]):
            lcp.append(self.common_char_count(first, second))

        self.lcp = lcp
        self.sorted_suffix = sorted_suffix

    def common_char_count(self, first: str, second: str) -> int:
        count = 0
        for f, s in zip(first, second):
            if f != s:
                break
            count += 1
        return count

    def __getitem__(self, item):
        return self.lcp[item]

LCP('ababbab')
